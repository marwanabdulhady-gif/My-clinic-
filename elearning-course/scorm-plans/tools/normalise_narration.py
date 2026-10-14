#!/usr/bin/env python3
"""Bring hand-authored narration packs onto the canonical audio schema.

Modules 03 and 07 keep hand-written storyboard cards (this repository never regenerates them),
so their `narration-script.json`, `audio-script-export.json` and `voice_talent.md` are maintained
by this normaliser instead:

* one segment per spoken line (`part` = `omar` / `noor` / `omar-1` / `noor-1`),
* the shared companion voice block (provider and ids stay open until programme D10),
* the canonical export schema with `tts_text` free of speaker labels, `ssml`, `cues` and the
  recording table in `voice_talent.md`.

Run it after any hand edit of a 03/07 narration script:

    python3 elearning-course/scorm-plans/tools/normalise_narration.py 03_hr-employee-induction 07_quality-safety-and-risk
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audio_export  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
PLANS = ROOT / "elearning-course" / "scorm-plans"
LEADS = {"03_hr-employee-induction": "omar", "07_quality-safety-and-risk": "noor"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("modules", nargs="*", default=[], help="Module folders; default: 03 and 07.")
    args = parser.parse_args()
    folders = args.modules or sorted(LEADS)
    for folder in folders:
        module_dir = PLANS / folder
        script = audio_export.load_script(module_dir)
        before = len(script["segments"])
        export = audio_export.write_outputs(module_dir, script, lead=LEADS.get(folder))
        parts = sum(1 for s in script["segments"] if str(s.get("part", "")).endswith("-1"))
        print(f"{folder}: {before} → {len(script['segments'])} segments "
              f"({parts} two-voice parts) · {export['total_est_sec'] / 60:.1f} min")


if __name__ == "__main__":
    main()
