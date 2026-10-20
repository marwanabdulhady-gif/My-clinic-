import json
from pathlib import Path
import re
import sys
import unittest
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_package  # noqa: E402

PLANS = Path(__file__).resolve().parents[2]
MODULES = sorted(p for p in PLANS.glob("0[0-8]_*") if (p / "build" / "course-spec.json").exists())


def course(mdir: Path) -> dict:
    t = (mdir / "build" / "package" / "course.js").read_text()
    return json.loads(t[len("window.COURSE="):].rstrip().rstrip(";"))


class PackageTests(unittest.TestCase):
    def test_every_package_is_scorm_12_with_the_manifest_at_the_root(self):
        for mdir in MODULES:
            rep = json.loads((mdir / "build" / "build-report.json").read_text())
            self.assertTrue(rep["validate_package"]["ok"], (mdir.name, rep["validate_package"]["issues"]))
            with zipfile.ZipFile(mdir / "build" / rep["package"]["file"]) as z:
                names = set(z.namelist())
                self.assertIn("imsmanifest.xml", names)
                self.assertIn("index.html", names)
                m = z.read("imsmanifest.xml").decode()
                self.assertIn("<schemaversion>1.2</schemaversion>", m)
                self.assertIn('adlcp:scormtype="sco"', m)
                self.assertFalse(any("scorm-again" in n or n.startswith("runtime/") for n in names), "old edumints runtime left in the zip")

    def test_the_package_keeps_every_scored_screen_and_its_points(self):
        for mdir in MODULES:
            spec = json.loads((mdir / "build" / "course-spec.json").read_text())
            c = course(mdir)
            scored = lambda ss: [(s["id"], s["type"], s.get("points"), tuple(s.get("objective_ids") or [])) for s in ss if s.get("points")]
            self.assertEqual(scored(c["screens"]), scored(spec["screens"]), mdir.name)
            self.assertEqual(c["tracking"], spec["tracking"])

    def test_every_screen_type_has_a_renderer_and_every_picture_is_packaged(self):
        js = (Path(build_package.PLAYER) / "player.js").read_text()
        for mdir in MODULES:
            c = course(mdir)
            for s in c["screens"]:
                self.assertTrue(re.search(r"R\.%s\s*=" % s["type"], js), s["type"])
            for p in c["assets"].values():
                self.assertTrue((mdir / "build" / "package" / p).is_file(), p)

    def test_motion_is_switched_off_for_reduced_motion(self):
        css = (Path(build_package.PLAYER) / "player.css").read_text()
        self.assertIn("prefers-reduced-motion:reduce", css)
        js = (Path(build_package.PLAYER) / "player.js").read_text()
        self.assertIn("prefers-reduced-motion: reduce", js)


if __name__ == "__main__":
    unittest.main()
