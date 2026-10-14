#!/usr/bin/env python3
"""Programme-wide audit of the base SCORM structure across all eight packages.

Answers one question with evidence: *does every package carry the SCORM structure it needs
for objectives, interactions, tracking, resume, gamification and scenarios — and is the
generated documentation still in step with the storyboard?*

It reuses the generator (``build_scorm_structure.build``) rather than re-reading the
storyboards with a second parser, so the audit and the per-module documents cannot drift
apart. Checks:

1. **Freshness** — each ``<module>/scorm-structure.md`` on disk equals what the generator
   produces now. A stale file is a hard failure: it means a storyboard change was not
   regenerated.
2. **Base structure** — the checklist rows the generator emits, rolled up (manifest, pass
   mark, objective evidence, interaction mapping, completion rule, suspend_data budget).
3. **Gamification** — every scenario screen has a Phase 3 rule row; no excluded mechanic
   (leaderboard, ranking, streak, badge, countdown, time limit) is introduced.
4. **Scenarios** — per-package counts reconcile with ``scenario-design-plan.md``
   (5 + 3 + 4 + 1 + 2 + 2 + 2 + 7 = 26, the Rev01 commitment).
5. **Motion** — every screen carries a reduced-motion-safe motion spec.

Writes ``00_program/scorm-base-audit.json`` and ``00_program/scorm-base-audit.md``.
Exits non-zero when a hard failure is found.

Usage:
    python3 elearning-course/scorm-plans/tools/audit_scorm_base.py
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_scorm_structure import build  # noqa: E402

PLANS = Path(__file__).resolve().parents[1]
TODAY = "2026-10-14"

# scenario-design-plan.md: the Rev01 reconciliation, per package.
EXPECTED_SCENARIOS = {"01": 5, "02": 3, "03": 4, "04": 1, "05": 2, "06": 2, "07": 2, "08": 7}
EXPECTED_SCENARIO_TOTAL = 26
# scorm-structure.md §1 (programme): the eight-package baseline.
EXPECTED_SCREEN_TOTAL = 207
EXPECTED_SCORED_TOTAL = 95

# Checklist rows that block a Phase 4 build if they fail.
HARD_REQUIREMENTS = (
    "Manifest: one organization, one item, one SCO resource",
    "Every objective has at least one scored screen",
    "Every scored screen names its objective",
    "Every scored screen maps to an interaction type",
    "Completion rule set",
    "Resume state fits the SCORM version's suspend_data limit",
    "Gamification rules recorded for every scenario screen",
    "No excluded gamification mechanic introduced",
    "Motion spec present for every screen (reduced-motion safe)",
)


def label_key(label: str) -> str:
    """Checklist label without the per-module values interpolated into it.

    The generator writes "Pass mark written to the manifest (80%)" for one pack and "(70%)"
    for another; the roll-up matrix needs one row per requirement, not one per value.
    """
    return re.sub(r"\s*\([^)]*\)", "", label).replace("`", "").strip()


def is_hard(label: str) -> bool:
    key = label_key(label)
    return any(key.startswith(prefix) for prefix in HARD_REQUIREMENTS)


def audit_module(folder: Path) -> dict:
    num = folder.name[:2]
    result = build(str(folder))
    generated = result.pop("text")
    on_disk_path = folder / "scorm-structure.md"
    on_disk = on_disk_path.read_text(encoding="utf-8") if on_disk_path.exists() else ""
    fresh = on_disk == generated
    hard_failed = [c["requirement"] for c in result["checklist"]
                   if not c["ok"] and is_hard(c["requirement"])]
    open_items = [c["requirement"] for c in result["checklist"] if not c["ok"]]
    expected_scen = EXPECTED_SCENARIOS.get(num)
    return {
        "num": num,
        "module": folder.name,
        "title": result["title"],
        "scorm": result["scorm"],
        "zip": result["zip"],
        "screens": result["screens"],
        "scored": result["scored"],
        "points": result["points"],
        "pass_mark": result["pass"],
        "pass_points": result["pass_pts"],
        "objectives": result["objectives"],
        "thin_evidence_objectives": result["weak"],
        "interaction_types": result["interaction_types"],
        "suspend_chars": result["suspend_chars"],
        "suspend_limit": result["suspend_limit"],
        "suspend_headroom": result["suspend_limit"] - result["suspend_chars"],
        "scenario_screens": result["scenario_screens"],
        "scenario_count": len(result["scenario_screens"]),
        "scenario_count_expected": expected_scen,
        "scenario_count_ok": len(result["scenario_screens"]) == expected_scen,
        "feedback_screens": result["feedback_screens"],
        "banned_mechanic_hits": result["banned_mechanic_hits"],
        "checklist": result["checklist"],
        "checklist_ok": sum(1 for c in result["checklist"] if c["ok"]),
        "checklist_total": len(result["checklist"]),
        "open_items": open_items,
        "hard_failures": hard_failed,
        "structure_document_fresh": fresh,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-write", action="store_true",
                        help="Print the audit without writing the JSON/Markdown reports.")
    args = parser.parse_args()

    folders = sorted(p for p in PLANS.glob("0[1-8]_*") if p.is_dir())
    modules = [audit_module(folder) for folder in folders]

    hard_failures = []
    for m in modules:
        if not m["structure_document_fresh"]:
            hard_failures.append(
                f"{m['module']}: scorm-structure.md is stale — rerun "
                "tools/build_scorm_structure.py")
        for label in m["hard_failures"]:
            hard_failures.append(f"{m['module']}: {label}")
        if not m["scenario_count_ok"]:
            hard_failures.append(
                f"{m['module']}: {m['scenario_count']} scenario screens vs "
                f"{m['scenario_count_expected']} in scenario-design-plan.md")

    totals = {
        "modules": len(modules),
        "screens": sum(m["screens"] for m in modules),
        "scored": sum(m["scored"] for m in modules),
        "points": sum(m["points"] for m in modules),
        "scenarios": sum(m["scenario_count"] for m in modules),
        "interactions": sum(sum(m["interaction_types"].values()) for m in modules),
        "objectives": sum(m["objectives"] for m in modules),
        "thin_evidence_objectives": sum(len(m["thin_evidence_objectives"]) for m in modules),
        "feedback_screens": sum(m["feedback_screens"] for m in modules),
        "banned_mechanic_hits": sum(len(m["banned_mechanic_hits"]) for m in modules),
    }
    if totals["screens"] != EXPECTED_SCREEN_TOTAL:
        hard_failures.append(f"programme screen total {totals['screens']} != "
                             f"{EXPECTED_SCREEN_TOTAL} in the programme structure §1")
    if totals["scored"] != EXPECTED_SCORED_TOTAL:
        hard_failures.append(f"programme scored total {totals['scored']} != "
                             f"{EXPECTED_SCORED_TOTAL} in the programme structure §1")
    if totals["scenarios"] != EXPECTED_SCENARIO_TOTAL:
        hard_failures.append(f"programme scenario total {totals['scenarios']} != "
                             f"{EXPECTED_SCENARIO_TOTAL} committed in Rev01")

    summary = {
        "generated_at": TODAY,
        "tool": "tools/audit_scorm_base.py",
        "scope": "base SCORM structure for objectives, interactions, tracking, resume, "
                 "gamification and scenarios across all eight packages",
        "honesty_note": "Planning-stage audit of the storyboard build blocks and the generated "
                        "structure documents. No SCORM package has been built or launched, so "
                        "nothing here is an LMS or SCORM conformance result.",
        "hard_failures": hard_failures,
        "clean": not hard_failures,
        "totals": totals,
        "modules": modules,
    }

    if not args.no_write:
        (PLANS / "00_program" / "scorm-base-audit.json").write_text(
            json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (PLANS / "00_program" / "scorm-base-audit.md").write_text(
            markdown(summary), encoding="utf-8")

    for m in modules:
        print(f"{m['module']}: {m['scorm']} · {m['screens']} screens · {m['scored']} scored · "
              f"{m['scenario_count']}/{m['scenario_count_expected']} scenarios · "
              f"{m['objectives']} objectives · suspend {m['suspend_chars']:,}/"
              f"{m['suspend_limit']:,} · checklist {m['checklist_ok']}/{m['checklist_total']} · "
              f"doc {'fresh' if m['structure_document_fresh'] else 'STALE'}")
        for item in m["open_items"]:
            print(f"    ⚠ {item}")
    print(f"totals: {totals['screens']} screens · {totals['scored']} scored · "
          f"{totals['scenarios']} scenarios · {totals['interactions']} interaction records · "
          f"{totals['objectives']} objectives · {totals['thin_evidence_objectives']} thin")
    if hard_failures:
        print("HARD FAILURES:")
        for failure in hard_failures:
            print(f"    ✗ {failure}")
        return 1
    print(f"audit clean · modules={totals['modules']} hard_failures=0")
    return 0


def markdown(summary: dict) -> str:
    totals = summary["totals"]
    lines = [
        "# Base SCORM structure audit — all eight packages",
        "",
        f"Generated {summary['generated_at']} by `tools/audit_scorm_base.py`. "
        f"**{'Clean — no hard failures.' if summary['clean'] else 'HARD FAILURES BELOW.'}**",
        "",
        f"> {summary['honesty_note']}",
        "",
        "## Programme totals",
        "",
        "| Measure | Value | Reconciles with |",
        "|---|---:|---|",
        f"| Packages | {totals['modules']} | six commercial courses → eight SCORM packages |",
        f"| Screens | {totals['screens']} | programme structure §1 |",
        f"| Scored screens | {totals['scored']} | programme structure §1 |",
        f"| Interaction records | {totals['interactions']} | one per scored screen |",
        f"| Scenario / game / simulation screens | {totals['scenarios']} | "
        "Rev01: 26 experiences |",
        f"| LMS objectives | {totals['objectives']} | per-package §5 |",
        f"| Objectives on a single scored screen | {totals['thin_evidence_objectives']} | "
        "programme gap G4 |",
        f"| Scored screens with authored feedback | {totals['feedback_screens']} / "
        f"{totals['scored']} | Phase 4 build work |",
        f"| Excluded-mechanic mentions | {totals['banned_mechanic_hits']} | "
        "gamification-plan.md |",
        "",
        "## Per package",
        "",
        "| # | Package | SCORM | Screens | Scored | Pts | Pass | Objectives | Scenarios | "
        "Interactions | Resume (est./limit) | Checklist | Structure doc |",
        "|---|---|---|---:|---:|---:|---|---:|---|---|---|---|---|",
    ]
    for m in summary["modules"]:
        interactions = ", ".join(f"{k}×{v}" for k, v in sorted(m["interaction_types"].items()))
        lines.append(
            f"| {m['num']} | {m['module'].split('_', 1)[1]} | {m['scorm']} | {m['screens']} | "
            f"{m['scored']} | {m['points']} | {m['pass_mark']}% ({m['pass_points']}) | "
            f"{m['objectives']} | {m['scenario_count']}/{m['scenario_count_expected']} | "
            f"{interactions} | {m['suspend_chars']:,} / {m['suspend_limit']:,} | "
            f"{m['checklist_ok']}/{m['checklist_total']} | "
            f"{'fresh' if m['structure_document_fresh'] else '⚠ stale'} |")
    lines += ["", "## Base requirements per package", ""]
    # Labels carry per-module values ("Pass mark written to the manifest (80%)"), so the
    # matrix is keyed on the label with those values stripped.
    labels = []
    for c in summary["modules"][0]["checklist"]:
        key = label_key(c["requirement"])
        if key not in labels:
            labels.append(key)
    lines.append("| Requirement | " + " | ".join(m["num"] for m in summary["modules"]) + " |")
    lines.append("|---|" + "---|" * len(summary["modules"]))
    for key in labels:
        cells = []
        for m in summary["modules"]:
            row = next((c for c in m["checklist"] if label_key(c["requirement"]) == key), None)
            cells.append("—" if row is None else
                         ("✅" if row["ok"] else ("⛔" if is_hard(key) else "⚠")))
        hard = " **(hard)**" if is_hard(key) else ""
        lines.append(f"| {key}{hard} | " + " | ".join(cells) + " |")
    lines += ["", "⛔ = hard failure (blocks the Phase 4 gate) · ⚠ = open work, SME sign-off "
                  "or Phase 4 authoring.", "", "## Open items", ""]
    for m in summary["modules"]:
        if m["open_items"]:
            lines.append(f"- **{m['num']} {m['module']}** — " + "; ".join(m["open_items"]))
    if not any(m["open_items"] for m in summary["modules"]):
        lines.append("- none")
    lines += ["", "## Hard failures", ""]
    if summary["hard_failures"]:
        lines += [f"- ✗ {failure}" for failure in summary["hard_failures"]]
    else:
        lines.append("- none")
    lines += ["", "## What this audit does not cover", "",
              "- SCORM conformance: no package has been built, launched or tested against an LMS.",
              "- Answer-key or SME approval status: see each pack's Phase 0 decision sheet and "
              "`programme-status.md`.",
              "- The real `suspend_data` payload, which only the built player can measure; the "
              "figures here are the documented estimate.",
              ""]
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
