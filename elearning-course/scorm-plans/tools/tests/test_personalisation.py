import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import personalise  # noqa: E402
from map_hotspots import apply as apply_maps  # noqa: E402

PLANS = Path(__file__).resolve().parents[2]
MODULES = sorted(p for p in PLANS.glob("0[1-8]_*") if p.is_dir())


class LayerTests(unittest.TestCase):
    def test_every_module_has_a_role_picker_and_unchanged_total_points(self):
        totals = {"01": 220, "02": 145, "03": 145, "04": 50, "05": 100, "06": 80, "07": 95, "08": 90}
        for mdir in MODULES:
            spec = json.loads((mdir / "build" / "course-spec.json").read_text())
            self.assertTrue(any(s["type"] == "branching" for s in spec["screens"]), mdir.name)
            self.assertEqual(sum(s.get("points") or 0 for s in spec["screens"]), totals[mdir.name[:2]], mdir.name)
            self.assertFalse(spec["screens"][-1].get("visible_if"), mdir.name)
            self.assertEqual({v["name"] for v in spec.get("variables", [])}, {"role", "role_label", "xp"})
            self.assertEqual(spec.get("points_var"), "xp")
            self.assertEqual(len(spec.get("levels", [])), 4)

    def test_picker_continues_to_the_screen_that_follows_it(self):
        for mdir in MODULES:
            screens = json.loads((mdir / "build" / "course-spec.json").read_text())["screens"]
            i = next(i for i, s in enumerate(screens) if s["type"] == "branching")
            self.assertEqual({c["goto_screen_id"] for c in screens[i]["choices"]}, {screens[i + 1]["id"]}, mdir.name)
            self.assertTrue(screens[i + 1]["id"].endswith("-00m"), "mission brief follows the picker")

    def _run(self, layer: dict, screens: list[dict]):
        with tempfile.TemporaryDirectory() as d:
            mdir = Path(d) / "04_x"
            (mdir / "production").mkdir(parents=True)
            (mdir / "production" / "personalisation.json").write_text(json.dumps(layer))
            return personalise.apply(screens, "04_x", mdir, lambda aid: False)

    def test_converting_a_scored_screen_is_refused(self):
        screens = [{"id": "a", "type": "mcq", "points": 10, "objective_ids": ["o1"]},
                   {"id": "z", "type": "summary"}]
        with self.assertRaises(SystemExit):
            self._run({"convert": {"a": {"type": "flashcards", "cards": []}}}, screens)

    def test_inserted_screens_are_forced_unscored_and_staged_steps_wait_for_their_picture(self):
        screens = [{"id": "a", "type": "content_slide"}, {"id": "z", "type": "summary"}]
        layer = {"insert_after": {"a": [{"kind": "screen", "screen": {"id": "a1", "type": "true_false", "points": 10}}]},
                 "convert": {"a": {"type": "hotspot", "requires_asset": "x-img"}}}
        out, _, notes = self._run(layer, screens)
        self.assertEqual([s["id"] for s in out], ["a", "a1", "z"])
        self.assertEqual(out[1]["points"], 0)
        self.assertEqual(out[0]["type"], "content_slide")
        self.assertTrue(any("held back" in n for n in notes))


class HotspotMapTests(unittest.TestCase):
    def test_extra_regions_wait_for_sme_approval_on_scored_screens(self):
        with tempfile.TemporaryDirectory() as d:
            mdir = Path(d)
            (mdir / "production" / "hotspots").mkdir(parents=True)
            (mdir / "production" / "hotspots" / "pic.json").write_text(json.dumps({"screens": {
                "s1": {"regions": {"r1": [1, 2, 3, 4]}, "add_regions": [{"id": "r2", "coords": [5, 5, 5, 5]}]},
                "s2": {"regions": {"r1": [9, 9, 9, 9]}, "add_regions": [{"id": "r2", "coords": [5, 5, 5, 5]}]}}}))
            scored = {"id": "s1", "image_asset_id": "pic", "points": 10, "mode": "find", "regions": [{"id": "r1", "coords": [0, 0, 1, 1]}]}
            explore = {"id": "s2", "image_asset_id": "pic", "points": 0, "mode": "explore", "regions": [{"id": "r1", "coords": [0, 0, 1, 1]}]}
            apply_maps([scored, explore], mdir)
            self.assertEqual(scored["regions"][0]["coords"], [1, 2, 3, 4])
            self.assertEqual(len(scored["regions"]), 1)
            self.assertEqual([r["id"] for r in explore["regions"]], ["r1", "r2"])


if __name__ == "__main__":
    unittest.main()
