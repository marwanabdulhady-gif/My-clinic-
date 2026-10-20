import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[3] / "video" / "_shared" / "scripts"


class VideoScriptTests(unittest.TestCase):
    def test_resolve_cues_fails_loudly_on_a_missing_phrase(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            (d / "w.json").write_text(json.dumps([{"word": "Check", "start": 2.1}, {"word": "the", "start": 2.4},
                                                  {"word": "exit.", "start": 2.6}]))
            (d / "ok.json").write_text(json.dumps({"exit": "the exit"}))
            (d / "bad.json").write_text(json.dumps({"exit": "the exit", "door": "fire door"}))
            run = lambda c: subprocess.run([sys.executable, SCRIPTS / "resolve_cues.py", "--cues", d / c,
                                            "--words", d / "w.json", "--out", d / "out.json"], capture_output=True, text=True)
            self.assertEqual(run("ok.json").returncode, 0)
            self.assertEqual(json.loads((d / "out.json").read_text()), {"exit": 2.4})
            bad = run("bad.json")
            self.assertEqual(bad.returncode, 1)
            self.assertIn("fire door", bad.stderr)

    def test_srt_to_vtt_adds_speaker_tags(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            (d / "c.srt").write_text("1\n00:00:00,500 --> 00:00:02,000\nHello.\n\n2\n00:00:02,100 --> 00:00:04,000\nBye.\n")
            (d / "m.json").write_text(json.dumps({"scenes": [{"start": 0, "end": 2.05, "speaker": "noor"},
                                                             {"start": 2.05, "end": 9, "speaker": "omar"}]}))
            r = subprocess.run([sys.executable, SCRIPTS / "srt_to_vtt.py", d / "c.srt", d / "c.vtt", "--manifest", d / "m.json"],
                               capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            vtt = (d / "c.vtt").read_text()
            self.assertTrue(vtt.startswith("WEBVTT"))
            self.assertIn("<v Noor>Hello.", vtt)
            self.assertIn("<v Dr. Omar>Bye.", vtt)


if __name__ == "__main__":
    unittest.main()
