#!/usr/bin/env python3
"""Keep the caption text in ``build/screens.json`` in step with the narration script.

The six generated modules carry a hand-reviewed ``build/screens.json``: it is the production screen
set the SCORM build compiles, and its ``narration_text`` field is what the draft packages show as
captions.  ``build_course_spec.py`` deliberately guards the *structure* of that file (ids, order,
types, node ids, points, objectives) but not the narration, so after a narration change the captions
can silently drift from ``storyboard/narration-script.json`` — this tool closes that gap.

Rules (they reproduce the existing files exactly):

* one screen's caption = its narration segments in script order, joined with a single space;
* the speaker label is routing, not speech: ``NOOR:`` becomes ``Noor:`` and ``OMAR:`` becomes
  ``Dr. Omar:`` (the same label convention the storyboard cards use);
* nothing else in ``screens.json`` is touched — the file is edited by replacing the caption string
  in place, so an unchanged screen produces byte-identical output.

Usage::

    python3 elearning-course/scorm-plans/tools/sync_screen_captions.py            # write changes
    python3 elearning-course/scorm-plans/tools/sync_screen_captions.py --check    # fail on drift
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

PLANS = Path(__file__).resolve().parents[1]
LABELS = {"NOOR": "Noor", "OMAR": "Dr. Omar"}


def caption_for(narration: str) -> str:
    return re.sub(r"^(NOOR|OMAR):", lambda m: LABELS[m.group(1)] + ":", narration.strip())


def captions_from_script(module_dir: Path) -> dict[str, str]:
    script = json.loads((module_dir / "storyboard" / "narration-script.json").read_text(encoding="utf-8"))
    joined: dict[str, list[str]] = {}
    for segment in script.get("segments", []):
        joined.setdefault(segment["screen_id"], []).append(caption_for(segment["narration"]))
    return {sid: " ".join(parts) for sid, parts in joined.items()}


def screen_regions(text: str, screen_ids: list[str]) -> dict[str, tuple[int, int]]:
    """Byte ranges of each top-level screen object, keyed by screen id.

    The file is a JSON array of screen objects that contain nested ``id`` values (options, choices,
    nodes), so a plain "next id" scan is wrong.  Screen ids are matched with their closing quote
    (nested ids extend the string) and only the first match is used.
    """
    starts: list[tuple[int, str]] = []
    for screen_id in screen_ids:
        at = text.find(f'"id": "{screen_id}"')
        if at >= 0:
            starts.append((at, screen_id))
    starts.sort()
    regions: dict[str, tuple[int, int]] = {}
    for index, (at, screen_id) in enumerate(starts):
        end = starts[index + 1][0] if index + 1 < len(starts) else len(text)
        regions[screen_id] = (at, end)
    return regions


def replace_caption(text: str, region: tuple[int, int], new_value: str) -> tuple[str, str]:
    """Replace one screen's caption literal in place inside its region. Returns (text, status)."""
    at, end_of_region = region
    key = '"narration_text":'
    key_at = text.find(key, at)
    if key_at < 0 or key_at > end_of_region:
        return text, "no-field"
    start = text.find('"', key_at + len(key))
    if start < 0 or start > end_of_region:
        return text, "no-value"
    end = start + 1
    while True:
        if end >= len(text):
            return text, "unterminated"
        if text[end] == "\\":
            end += 2
            continue
        if text[end] == '"':
            break
        end += 1
    literal = text[start:end + 1]
    try:
        current = json.loads(literal)
    except json.JSONDecodeError:
        return text, "bad-literal"
    if current == new_value:
        return text, "unchanged"
    return text[:start] + json.dumps(new_value, ensure_ascii=False) + text[end + 1:], "updated"


def sync_module(module_dir: Path, check: bool) -> dict[str, int]:
    screens_path = module_dir / "build" / "screens.json"
    if not screens_path.exists():
        return {}
    text = screens_path.read_text(encoding="utf-8")
    original = text
    screens = json.loads(text)
    captions = captions_from_script(module_dir)
    regions = screen_regions(text, [screen["id"] for screen in screens])
    counts = {"updated": 0, "unchanged": 0, "missing": 0}
    # Replace from the end so earlier offsets stay valid while the text shifts.
    for screen in reversed(screens):
        screen_id = screen["id"]
        caption = captions.get(screen_id)
        if caption is None or screen_id not in regions:
            counts["missing"] += 1
            continue
        text, status = replace_caption(text, regions[screen_id], caption)
        if status == "updated":
            counts["updated"] += 1
        elif status == "unchanged":
            counts["unchanged"] += 1
        else:
            counts["missing"] += 1
    if not check and text != original:
        screens_path.write_text(text, encoding="utf-8")
    return counts


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("modules", nargs="*", help="Module folders; default: every module with build/screens.json.")
    parser.add_argument("--check", action="store_true", help="Exit non-zero when a caption is out of step.")
    args = parser.parse_args()
    folders = args.modules or sorted(p.name for p in PLANS.glob("0[1-8]_*") if (p / "build" / "screens.json").exists())
    drift = 0
    for folder in folders:
        counts = sync_module(PLANS / folder, args.check)
        if not counts:
            print(f"{folder}: no build/screens.json — skipped")
            continue
        drift += counts["updated"]
        print(f"{folder}: updated {counts['updated']} · unchanged {counts['unchanged']} · missing {counts['missing']}")
    if args.check and drift:
        raise SystemExit(f"{drift} caption(s) out of step with narration-script.json")


if __name__ == "__main__":
    main()
