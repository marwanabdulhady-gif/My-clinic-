"""Run: python3 -m unittest discover -s elearning-course/scorm-plans/tools/tests -v"""
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from generate_screens import PLANS, generate, load_cards, missing_fields, sanitize, asset_ids, scenario_issues


class GeneratorTests(unittest.TestCase):
    def test_all_modules_preserve_order_ids_and_scoring(self):
        modules = sorted(p for p in PLANS.glob('0[1-8]_*') if p.is_dir())
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            report = generate(modules, output)
            self.assertEqual(report['screen_count'], 207)
            self.assertEqual(report['scored_screen_count'], 95)
            self.assertFalse(report['production_ready'])
            content = (output / 'index.html').read_text()
            raw = content.split('<script id="course-data" type="application/json">')[1].split('</script>')[0]
            data = json.loads(raw)
            for module, result in zip(modules, data['modules']):
                original = load_cards(module / 'storyboard' / 'storyboard.md')
                self.assertEqual([s['id'] for s in result['screens']], [s['id'] for s in original])
                self.assertEqual([s.get('points') for s in result['screens']], [s.get('points') for s in original])
                self.assertEqual([s.get('evidence_screen_ids') for s in result['screens']], [s.get('evidence_screen_ids') for s in original])
            for path in data['assets'].values():
                self.assertTrue((output / path).is_file())
            self.assertTrue(all(s['_mode'] == 'brief' for s in data['modules'][0]['screens']))
            self.assertTrue(any(s['_mode'] == 'rendered' for s in data['modules'][2]['screens']))

    def test_deterministic_output(self):
        module = PLANS / '03_hr-employee-induction'
        with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
            generate([module], Path(a))
            generate([module], Path(b))
            for name in ['index.html', 'generation-report.json', 'player.js', 'scenario.js', 'style.css']:
                self.assertEqual((Path(a) / name).read_bytes(), (Path(b) / name).read_bytes())

    def test_invalid_json_duplicate_and_unknown_type_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'storyboard.md'
            for content in ['```json\n{bad}\n```',
                            '```json\n{"id":"x-1","type":"title_slide"}\n```\n' * 2,
                            '```json\n{"id":"x-1","type":"invented"}\n```', 'no blocks']:
                path.write_text(content)
                with self.assertRaises(ValueError):
                    load_cards(path)

    def test_html_is_inert_and_text_preserved(self):
        data = sanitize({'body_html': '<p onclick="bad()">Keep <strong>this</strong><script>alert(1)</script><a href="javascript:bad()">link</a><img src=x onerror=bad()></p>',
                         'items': [{'body_html': '<iframe>drop me</iframe><p>OK</p>'}]})
        self.assertEqual(data['body_html'], '<p>Keep <strong>this</strong>link</p>')
        self.assertEqual(data['items'][0]['body_html'], '<p>OK</p>')

    def test_pending_answer_key_does_not_become_correct(self):
        self.assertEqual(missing_fields({'type':'true_false', 'prompt_html':'Q', 'correct':False}), [])
        self.assertIn('accepted answers', missing_fields({'type':'fill_blank', 'prompt_html':'Q', 'blanks':[{'accepted':[]}]}))
        self.assertIn('correct option', missing_fields({'type':'mcq', 'prompt_html':'Q', 'options':[{'id':'a'}]}))

    def test_nested_assets_and_explicit_mapping(self):
        self.assertEqual(asset_ids({'steps':[{'image_asset_id':'<example>'}]}), {'example'})
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            asset = root / 'approved-review.png'
            asset.write_bytes((PLANS / '00_program/brand/assets/mark-navy.png').read_bytes())
            mapping = root / 'map.json'
            mapping.write_text(json.dumps({'char-omar-explaining': asset.name}))
            out = root / 'preview'
            report = generate([PLANS / '03_hr-employee-induction'], out, mapping)
            screen = next(i for i in report['issues'] if i['screen_id'] == 'hr-001')
            self.assertNotIn('char-omar-explaining', screen['unresolved_assets'])
            self.assertTrue((out / 'assets/char-omar-explaining.png').exists())
            mapping.write_text('{"bad/path":"approved-review.png"}')
            with self.assertRaises(ValueError):
                generate([PLANS / '03_hr-employee-induction'], out, mapping)

    def test_authored_scenario_graphs_and_invalid_branches(self):
        import copy
        scenarios = [s for name in ['03_hr-employee-induction', '07_quality-safety-and-risk']
                     for s in load_cards(PLANS / name / 'storyboard/storyboard.md')
                     if s['type'] == 'decision_scenario']
        self.assertEqual(len(scenarios), 4)
        for scenario in scenarios:
            self.assertEqual(scenario_issues(scenario), [])
        for field, value in [('goto_node_id', 'missing'), ('goto_node_id', {}),
                             ('score_delta', True), ('score_delta', float('inf')),
                             ('feedback_html', '')]:
            invalid = copy.deepcopy(scenarios[0])
            invalid['nodes'][0]['choices'][0][field] = value
            self.assertTrue(scenario_issues(invalid))
        invalid = copy.deepcopy(scenarios[0])
        invalid['nodes'][-1]['choices'][0]['goto_node_id'] = invalid['start_node_id']
        self.assertTrue(scenario_issues(invalid))

    def test_output_cannot_overwrite_sources(self):
        for output in [PLANS, PLANS / '03_hr-employee-induction', PLANS.parents[1], PLANS.parents[2]]:
            with self.assertRaises(ValueError):
                generate([PLANS / '03_hr-employee-induction'], output)


if __name__ == '__main__':
    unittest.main()
