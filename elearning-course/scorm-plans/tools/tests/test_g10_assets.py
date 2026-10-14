"""G10 regression gate: no silently omitted Phase 3 images or captures."""
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from assemble_storyboard_docs import MODULES, PLANS, imagery_for, parse_assets, parse_phase2
from generate_screens import load_cards
from planned_visual_assets import assets_for_screen, expand_ids, is_visual


class G10AssetTests(unittest.TestCase):
    def assets(self, folder):
        return parse_assets(PLANS / folder)

    def plan(self, folder):
        return json.loads((PLANS / folder / 'storyboard/visual-plan.json').read_text())

    def planned_ids(self, folder, sid):
        screen = next(s for s in self.plan(folder)['screens'] if s['screen_id'] == sid)
        return [image['description'].split(':', 1)[0] for image in screen['imagery']
                if ':' in image['description']]

    def test_grouped_ids_and_exact_screen_matching(self):
        self.assertEqual(expand_ids('hs2-img-drill-1..6'), [f'hs2-img-drill-{i}' for i in range(1, 7)])
        self.assertEqual(expand_ids('hs2-img-kit-chem / hs2-img-kit-bio'), ['hs2-img-kit-chem', 'hs2-img-kit-bio'])
        self.assertEqual(expand_ids('ehr-vid-walkthrough *(optional)*'), ['ehr-vid-walkthrough'])
        self.assertEqual(expand_ids('char-noor-* / char-omar-*'), ['char-noor-*', 'char-omar-*'])
        self.assertEqual(assets_for_screen([{'screens':'ehr-0100'}], 'ehr-010'), [])
        self.assertEqual(len(assets_for_screen([{'screens':'ehr-010, 011'}], 'ehr-011')), 1)
        self.assertEqual(len(assets_for_screen([{'screens':'hs2-060, 062, 063, 064'}], 'hs2-064')), 1)
        with self.assertRaises(ValueError):
            expand_ids('ehr-shot-dx-5..1')

    def test_hs1_required_images_restored(self):
        for sid, aid in [('hs1-506','hs1-img-eyewash'), ('hs1-701','hs1-img-treatment-room'), ('hs1-802','hs1-img-pump-label')]:
            self.assertIn(aid, self.planned_ids('01_health-and-safety-1', sid))

    def test_full_six_scene_drill_mapping(self):
        folder = '02_health-and-safety-2'
        expected = [f'hs2-img-drill-{i}' for i in range(1, 7)]
        self.assertEqual(self.planned_ids(folder, 'hs2-030'), expected)
        manifest = json.loads((PLANS / folder / 'storyboard/drill-scene-manifest.json').read_text())
        self.assertEqual(manifest['scene_count'], 6)
        self.assertEqual([a['id'] for a in manifest['assets']], expected)
        for index, asset in enumerate(manifest['assets'], 1):
            self.assertTrue(asset['placement'].startswith(f'Node {index}'))
            self.assertTrue(asset['alt'])
            self.assertIn('PENDING', asset['gate'])
        self.assertIn('Planned', manifest['status'])

    def test_spill_photos_and_both_kits_restored(self):
        folder = '02_health-and-safety-2'
        self.assertIn('hs2-img-spill-photo', self.planned_ids(folder, 'hs2-064'))
        self.assertIn('hs2-img-extinguisher', self.planned_ids(folder, 'hs2-040'))
        self.assertEqual(self.planned_ids(folder, 'hs2-051'), ['hs2-img-kit-chem', 'hs2-img-kit-bio'])
        # The puzzle needs its register and NFPA diamond as well as the spill scene.
        self.assertIn('hs2-img-register', self.planned_ids(folder, 'hs2-064'))
        self.assertIn('hs2-img-nfpa-230', self.planned_ids(folder, 'hs2-064'))

    def test_31_unique_ehr_captures_shared_form_and_privacy(self):
        folder = '08_it-ehr-consultation'
        manifest = json.loads((PLANS / folder / 'storyboard/capture-manifest.json').read_text())
        expected = {'ehr-010':2, 'ehr-011':1, 'ehr-020':5, 'ehr-031':6,
                    'ehr-032':4, 'ehr-040':3, 'ehr-041':5, 'ehr-050':6}
        self.assertEqual(manifest['screenshot_count'], 31)
        self.assertEqual(len({a['id'] for a in manifest['assets']}), 31)
        self.assertEqual(manifest['viewport'], [1920, 1080])
        self.assertEqual(manifest['browser_zoom_percent'], 125)
        self.assertIsNone(manifest['dpo_approval'])
        self.assertEqual(manifest['optional_crops']['max_count'], 4)
        for sid, count in expected.items():
            self.assertEqual(len(self.planned_ids(folder, sid)), count)
        for asset in manifest['assets']:
            self.assertIn('D6', asset['gate'])
            self.assertIn('DPO', asset['gate'])
            self.assertTrue(asset['alt'])
        self.assertEqual(self.planned_ids(folder, 'ehr-011'), ['ehr-shot-form'])

    def test_no_phase3_visual_silently_omitted_or_duplicated(self):
        for folder in ['01_health-and-safety-1', '02_health-and-safety-2', '08_it-ehr-consultation']:
            assets = self.assets(folder)
            rows = parse_phase2(PLANS / folder, MODULES[folder]['prefix'])
            for row in rows:
                images = imagery_for(folder, row, assets, None)
                included = [i['description'].split(':', 1)[0] for i in images if ':' in i['description']]
                expected = [a['id'] for a in assets_for_screen(assets, row['id']) if is_visual(a)]
                self.assertTrue(set(expected).issubset(included), (row['id'], expected, included))
                self.assertEqual(len(included), len(set(included)), row['id'])

    def test_no_optional_video_or_new_screens_and_scoring_unchanged(self):
        for folder, expected_count in [('01_health-and-safety-1',54), ('02_health-and-safety-2',26), ('08_it-ehr-consultation',20)]:
            rows = parse_phase2(PLANS / folder, MODULES[folder]['prefix'])
            cards = load_cards(PLANS / folder / 'storyboard/storyboard.md')
            self.assertEqual(len(cards), expected_count)
            self.assertEqual([(s['id'],s['type'],s['points']) for s in cards],
                             [(s['id'],s['type'],s['points']) for s in rows])
            self.assertFalse(any(s['type'] == 'video' for s in cards))
            if folder == '08_it-ehr-consultation':
                from build_scorm_structure import build
                structure = build(str(PLANS / folder))['text']
                self.assertNotIn('ehr-vid-walkthrough', structure)
                for asset in self.assets(folder):
                    if asset['id'].startswith('ehr-shot-'):
                        self.assertIn(asset['id'], structure)
            for card in cards:
                expected = [a['id'] for a in assets_for_screen(self.assets(folder), card['id']) if is_visual(a)]
                for aid in expected:
                    self.assertIn(f'<{aid}>', card.get('notes', ''))


if __name__ == '__main__':
    unittest.main()
