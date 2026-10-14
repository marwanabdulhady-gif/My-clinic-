"""Regression gates for the pre-kickoff, template-driven draft batches."""
import copy
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from generate_screens import BRAND, PLANS, generate, load_cards, module_data
from review_inputs import MOCKUP_FILES, REPO, layout_for, mockup_contract, module_contract, phase_plan


class ReviewInputTests(unittest.TestCase):
    def setUp(self):
        self.module = PLANS / '03_hr-employee-induction'
        self.cards = load_cards(self.module / 'storyboard/storyboard.md')
        self.visuals = json.loads((self.module / 'storyboard/visual-plan.json').read_text())
        self.narration = json.loads((self.module / 'storyboard/narration-script.json').read_text())

    def test_phase_one_baseline_templates_and_all_six_plans_are_inputs(self):
        modules = [PLANS / name for name in phase_plan()['phases'][0]['modules']]
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            report = generate(modules, output, phase_id='1')
            self.assertEqual(report['screen_count'], 58)
            self.assertEqual(report['scored_screen_count'], 26)
            self.assertEqual(report['render_modes'], {'rendered': 48, 'review': 9, 'brief': 1})
            self.assertFalse(report['production_ready'])
            self.assertEqual([m['id'] for m in report['modules']], [m.name for m in modules])
            for module in report['modules']:
                contract = module['contract']
                self.assertEqual(contract['alignment'], 'review-required' if module['id'] == '03_hr-employee-induction' else 'matched')
                if module['id'] == '03_hr-employee-induction':
                    self.assertTrue(any('hr-001: Phase 2 layout full_media differs from storyboard text_media' in issue for issue in contract['issues']))
                self.assertEqual(contract['actual'], contract['expected'])
                self.assertEqual(len(contract['gates']), 8)
                self.assertFalse(any(g['checked'] for g in contract['gates']))
                paths = [p['path'] for p in contract['inputs']]
                self.assertTrue(any('production-worksheet.md' in p for p in paths))
                self.assertTrue(any('course-production-template.md' in p for p in paths))
                for phase in range(6):
                    self.assertTrue(any(f'/phase-{phase}-' in p for p in paths))
                for record in contract['inputs']:
                    self.assertEqual(hashlib.sha256((REPO / record['path']).read_bytes()).hexdigest(), record['sha256'])
                    self.assertTrue((output / 'reference/inputs' / record['path']).is_file())
            self.assertTrue((output / 'layout-tokens.css').is_file())
            self.assertEqual(len(report['layout_contract']['references']), 8)
            self.assertFalse(list(output.rglob('*.mp4')), 'Never copy the original videos')

    def test_missing_essential_inputs_fail_instead_of_becoming_optional(self):
        original = Path.read_text
        required = [self.module / 'storyboard/visual-plan.json', self.module / 'storyboard/narration-script.json',
                    PLANS / '00_program/course-templates/03-hr-employee-induction-production-worksheet.md',
                    PLANS / '00_program/course-templates/course-production-template.md']
        for missing in required:
            def read(path, *args, **kwargs):
                if path == missing:
                    raise FileNotFoundError(str(path))
                return original(path, *args, **kwargs)
            with patch.object(Path, 'read_text', read), self.assertRaises(FileNotFoundError):
                module_data(self.module)

    def test_mismatched_counts_or_objectives_are_reported_not_rewritten(self):
        cards = copy.deepcopy(self.cards)
        cards[0]['points'] = 1
        cards[0]['objective_ids'] = ['hr-o999']
        before = copy.deepcopy(cards)
        contract = module_contract(self.module, cards, self.visuals, self.narration)
        self.assertEqual(contract['alignment'], 'review-required')
        self.assertTrue(any('Worksheet baseline' in issue for issue in contract['issues']))
        self.assertTrue(any('Phase 2' in issue for issue in contract['issues']))
        self.assertTrue(any('objective IDs' in issue for issue in contract['issues']))
        self.assertEqual(cards, before)
        self.assertFalse(any(g['checked'] for g in contract['gates']))

    def test_stale_capture_gallery_is_invalidated_after_regeneration(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            generate([self.module], output)
            self.assertIn('Screenshots need to be refreshed', (output / 'review.html').read_text())
            (output / 'review').mkdir()
            current = hashlib.sha256((output / 'generation-report.json').read_bytes()).hexdigest()
            (output / 'review/capture-report.json').write_text(json.dumps({'generation_report_sha256': current}))
            (output / 'review.html').write_text('CURRENT VERIFIED GALLERY')
            generate([self.module], output)
            self.assertEqual((output / 'review.html').read_text(), 'CURRENT VERIFIED GALLERY')
            (output / 'review/capture-report.json').write_text('{"generation_report_sha256":"stale"}')
            generate([self.module], output)
            self.assertIn('Screenshots need to be refreshed', (output / 'review.html').read_text())

    def test_phase_selection_rejects_wrong_order_and_empty_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                generate([], Path(tmp))
            with self.assertRaises(ValueError):
                generate([PLANS / '07_quality-safety-and-risk', self.module], Path(tmp), phase_id='1')

    def test_mockup_geometry_really_comes_from_html_not_hardcoded_css(self):
        (REPO / '.generated').mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=REPO / '.generated') as tmp:
            folder = Path(tmp)
            for name in [*MOCKUP_FILES.values(), 'mockups.html']:
                shutil.copyfile(BRAND / 'screen-mockups' / name, folder / name)
            source = folder / 'mockups.html'
            source.write_text(source.read_text().replace('top:190px;width:600px', 'top:192px;width:600px'))
            contract = mockup_contract(folder)
            self.assertEqual(contract['metrics']['title-text-top'], '192px')
            self.assertEqual(contract['metrics']['canvas-width'], '960px')
            self.assertIn('linear-gradient', contract['metrics']['title-background'])
            source.write_text(source.read_text().replace('background:linear-gradient(120deg,#003867 0%,#003867 55%,#3B6A97 100%)', 'background:url(https://untrusted.example/picture)'))
            with self.assertRaises(ValueError):
                mockup_contract(folder)

    def test_visual_plan_and_phase_three_drive_layout_and_companion(self):
        hr = module_data(self.module)
        qsr = module_data(PLANS / '07_quality-safety-and-risk')
        welcome = hr['screens'][0]
        self.assertEqual(welcome['_layout']['reference_id'], 's7')
        self.assertEqual(welcome['_companion']['assets'], ['char-omar-welcome', 'char-noor-welcome'])
        opener = next(s for s in qsr['screens'] if s['id'] == 'qsr-001')
        self.assertEqual(opener['_layout']['id'], 'L2')
        self.assertEqual(opener['_pending'], ['B1'])
        tip = next(s for s in qsr['screens'] if s['id'] == 'qsr-040')
        self.assertEqual(tip['_layout']['reference_id'], 's8')
        self.assertEqual(tip['_companion']['assets'], ['char-omar-avatar-neutral'])
        with self.assertRaises(ValueError):
            layout_for({'screen_id': 'test-001', 'layout': 'invented'}, {})

    def test_preview_art_is_shown_without_clearing_missing_production_assets(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            report = generate([self.module], output)
            issue = next(s for s in report['issues'] if s['screen_id'] == 'hr-001')
            self.assertIn('char-omar-explaining', issue['unresolved_assets'])
            raw = (output / 'index.html').read_text().split('<script id="course-data" type="application/json">')[1].split('</script>')[0]
            data = json.loads(raw)
            self.assertIn('char-omar-explaining', data['preview_assets'])
            self.assertNotIn('char-omar-explaining', data['assets'])
            self.assertFalse(data['asset_provenance']['char-omar-explaining']['production_approved'])

    def test_bundled_font_checksums_and_licenses_are_verified(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            report = generate([self.module], output)
            for font in report['font_provenance']['files']:
                self.assertEqual(hashlib.sha256((output / 'fonts' / font['filename']).read_bytes()).hexdigest(), font['sha256'])
            self.assertTrue((output / 'fonts/Montserrat-OFL.txt').exists())
            self.assertTrue((output / 'fonts/Tajawal-OFL.txt').exists())
            self.assertNotIn('https://', (output / 'style.css').read_text())
            original = Path.read_text
            def corrupt(path, *args, **kwargs):
                text = original(path, *args, **kwargs)
                if path == BRAND / 'fonts/provenance.json':
                    data = json.loads(text); data['files'][0]['sha256'] = '0' * 64
                    return json.dumps(data)
                return text
            with patch.object(Path, 'read_text', corrupt), self.assertRaisesRegex(ValueError, 'checksum'):
                generate([self.module], output)


if __name__ == '__main__':
    unittest.main()
