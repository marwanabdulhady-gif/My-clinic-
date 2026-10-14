#!/usr/bin/env python3
"""Write the structured motion spec into every screen of the eight visual plans.

The plans used to carry one free-text token per screen (``"animation": "fade-up"``). That
token is kept — the storyboard cards and the review player read it — and this tool adds a
machine-checkable ``motion`` object next to it: entrance preset with duration and easing,
the layer order (bound to the narration ``[[cue:…]]`` marks where the plan declares
``cue_targets``), emphasis, answer-feedback motion, exit, the entrance budget in
milliseconds and the reduced-motion fallback.

The spec is derived, never hand-edited, so rerunning this after a storyboard change is
safe and idempotent:

    python3 elearning-course/scorm-plans/tools/build_motion_spec.py            # all eight packs
    python3 elearning-course/scorm-plans/tools/build_motion_spec.py 07_quality-safety-and-risk

Vocabulary and rules live in ``tools/motion_spec.py``; ``tools/lint_planning.py`` re-checks
every spec on each run, and ``tools/tests/test_motion_spec.py`` pins the behaviour.
Writes ``00_program/motion-spec-summary.json``.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from motion_spec import SPEC_VERSION, lint_motion, motion_for_screen  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
PLANS = ROOT / "elearning-course" / "scorm-plans"
TODAY = "2026-10-14"


def build_module(folder: str) -> dict:
    plan_path = PLANS / folder / "storyboard" / "visual-plan.json"
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    intents, entries, cue_layers, problems = Counter(), Counter(), 0, []
    for screen in plan.get("screens", []):
        spec = motion_for_screen(screen)
        screen["motion"] = spec
        problems.extend(lint_motion(spec, screen))
        intents[spec["intent"]] += 1
        entries[spec["entry"]["preset"]] += 1
        cue_layers += sum(1 for layer in spec["layers"] if layer["trigger"] == "cue")
    plan["motion_spec_version"] = SPEC_VERSION
    plan["motion_generated"] = {
        "generated_at": TODAY,
        "tool": "tools/build_motion_spec.py (vocabulary in tools/motion_spec.py)",
        "note": "Derived from screen_type, layout, cue_targets and the legacy animation token. "
                "Rerun this tool after any storyboard or visual-plan change; do not edit the "
                "motion objects by hand. Every preset is implemented in "
                "tools/screen_generator/style.css and honours prefers-reduced-motion.",
    }
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"module": folder, "screens": len(plan.get("screens", [])),
            "intents": dict(intents), "entry_presets": dict(entries),
            "cue_bound_layers": cue_layers, "problems": problems}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("modules", nargs="*", help="Module folders; default: all eight.")
    args = parser.parse_args()
    folders = args.modules or sorted(p.name for p in PLANS.glob("0[1-8]_*"))
    results, failures = [], 0
    for folder in folders:
        result = build_module(folder)
        results.append(result)
        failures += len(result["problems"])
        print(f"{folder}: {result['screens']} screens · intents "
              f"{', '.join(f'{k}={v}' for k, v in sorted(result['intents'].items()))} · "
              f"cue-bound layers {result['cue_bound_layers']} · "
              f"problems {len(result['problems'])}")
        for problem in result["problems"]:
            print(f"    [{problem['severity']}] {problem['code']}: {problem['message']} "
                  f"({problem['path']})")
    summary_path = PLANS / "00_program" / "motion-spec-summary.json"
    summary = {
        "generated_at": TODAY,
        "spec_version": SPEC_VERSION,
        "tool": "tools/build_motion_spec.py",
        "modules": results,
        "totals": {
            "screens": sum(r["screens"] for r in results),
            "cue_bound_layers": sum(r["cue_bound_layers"] for r in results),
            "problems": sum(len(r["problems"]) for r in results),
        },
    }
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
                            encoding="utf-8")
    print(f"total: {summary['totals']['screens']} screens, "
          f"{summary['totals']['cue_bound_layers']} cue-bound layers, "
          f"{summary['totals']['problems']} problems → {summary_path.name}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
