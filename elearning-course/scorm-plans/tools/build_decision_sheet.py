#!/usr/bin/env python3
"""Build the Phase 0 decision sheet (roadmap chunk C1) from the controlled source plans.

One page that lists every open decision with a named owner role, a proposed due date and the exact
file the answer must be written back to, so the kick-off meeting closes items instead of
discovering them. Sources (never duplicated by hand):

* `00_program/cross-module-decisions.md` — programme decisions D1–D14,
* each module's `phase-0-source-lock.md` — blocking items B*/NEW*,
* `00_program/scorm-structure-summary.json` — thin objective evidence (programme gap G4),
* `00_program/programme-status.md` gap G2 — the companion-beside-unscored-poll check for 07.

Recommended answers are copied from the plans where they propose one; they are **drafts for the
owner to confirm**, never policy. Due dates assume kick-off K = 2026-10-19 (week 1 of the proposal
timeline): tier 1 (safety, identifiers, PHI, incident rules) K+3 working days, tier 3 (programme
enablers D9/D10/D11) K+5, tier 2 (module content facts) end of week 2.

Usage:
    python3 elearning-course/scorm-plans/tools/build_decision_sheet.py
"""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PLANS = ROOT / "elearning-course" / "scorm-plans"
TODAY = "2026-10-14"
KICKOFF = "2026-10-19 (proposed)"
DUE = {1: "2026-10-22 (K+3 wd)", 3: "2026-10-26 (K+5 wd)", 2: "2026-10-30 (end of week 2)"}

TIER1_RE = re.compile(
    r"code |codes|extension|spill|orange|radiation|laser|waste|identif|patient|PHI|incident|"
    r"sentinel|near miss|24-hour|24 hour|dpo|data protection|test (environment|patient)|transcript|"
    r"licence|license|watermark|consent|photo|personal data|dose", re.I)
TIER3 = {"D9", "D10", "D11"}
TIER1_D = {"D1", "D2", "D5", "D6", "D8"}
# Owner-reviewed tier overrides where the keyword heuristic misfires (abbreviations and payer
# coverage are content facts, not safety/PHI gates).
TIER_OVERRIDES = {"04/B3": 2, "05/B4": 2, "05/B5": 2}

# Thin-evidence objectives (G4): where a second short check is worth it vs accept-at-sign-off.
COMPLIANCE_CRITICAL = {"hs1-o6", "hs1-o7", "qsr-o5", "ehr-o2"}
CAPSTONES = {"hs1-o10", "rcma-o5"}

MODULE_TITLES = {
    "01_health-and-safety-1": "01 FMS", "02_health-and-safety-2": "02 Safety Lab",
    "03_hr-employee-induction": "03 Welcome On Board", "04_operations-and-my-care": "04 Who Does What",
    "05_rcm-documentation-and-coding": "05 RCM Part A", "06_rcm-ebp-benefits-and-rejections": "06 RCM Part B",
    "07_quality-safety-and-risk": "07 Clinical Governance", "08_it-ehr-consultation": "08 EHR",
}


def cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def tier_for(decision_id: str, module_folder: str, text: str) -> int:
    if decision_id in TIER3:
        return 3
    if decision_id in TIER1_D:
        return 1
    if decision_id.startswith("D"):
        return 2
    if TIER1_RE.search(text):
        return 1
    return 2


def parse_cross_module() -> list[dict]:
    rows = []
    for line in (PLANS / "00_program" / "cross-module-decisions.md").read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        c = cells(line)
        if len(c) < 7 or not re.fullmatch(r"D\d+", c[0]):
            continue
        if "Open" not in c[5]:
            continue
        rows.append({
            "id": c[0], "modules": c[2], "question": c[1], "recommendation": c[3],
            "owner": c[4], "status": c[5],
            "write_back": "`00_program/cross-module-decisions.md` (Decision column) → the Phase 0 "
                          "tables and storyboard cards of the modules listed",
        })
    return rows


def parse_module(folder: str) -> list[dict]:
    rows = []
    text = (PLANS / folder / "phase-0-source-lock.md").read_text(encoding="utf-8")
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        c = cells(line)
        if len(c) < 6 or not re.fullmatch(r"(?:B|NEW)\d+", c[0]):
            continue
        if "Open" not in c[-1]:
            continue
        item, source, needed, owner = c[1], c[2], c[3], c[-2]
        rows.append({
            "id": f"{folder[:2]}/{c[0]}", "modules": MODULE_TITLES[folder],
            "question": f"**{item}** (source: {source})", "recommendation": needed,
            "owner": owner, "status": c[-1],
            "write_back": f"`{folder}/phase-0-source-lock.md` row {c[0]} + §4 verified-facts register",
        })
    return rows


def parse_thin_evidence() -> list[dict]:
    summary = json.loads((PLANS / "00_program" / "scorm-structure-summary.json").read_text(encoding="utf-8"))
    rows = []
    for entry in summary:
        weak = entry.get("weak") or []
        if not weak:
            continue
        folder = entry["name"]
        advice = []
        for objective in weak:
            if objective in COMPLIANCE_CRITICAL:
                advice.append(f"`{objective}`: add one second short scored check (Phase 2 change, SME approves)")
            elif objective in CAPSTONES:
                advice.append(f"`{objective}`: capstone — accept the single case at sign-off")
            else:
                advice.append(f"`{objective}`: accept single-evidence at SME sign-off, or add a short check")
        rows.append({
            "id": f"{folder[:2]}/G4", "modules": MODULE_TITLES[folder],
            "question": f"Thin objective evidence: {len(weak)} objective(s) assessed by one scored screen "
                        f"({', '.join('`' + w + '`' for w in weak)})",
            "recommendation": "; ".join(advice),
            "owner": "SME lead + L&D", "status": "Open",
            "write_back": f"`{folder}/phase-1-action-map.md` evidence map"
                          + (f" + `{folder}/phase-2-storyboard.md` if a check is added" or ""),
        })
    return rows


def main() -> None:
    rows = parse_cross_module()
    for folder in sorted(MODULE_TITLES):
        rows += parse_module(folder)
    rows.append({
        "id": "07/P01", "modules": MODULE_TITLES["07_quality-safety-and-risk"],
        "question": "Companion placement on `qsr-002`: Noor sits beside the opening poll, while "
                    "companions.md §5 keeps companions off question screens. The poll is unscored.",
        "recommendation": "Allow the companion beside **unscored** polls/reflections (amend "
                          "companions.md §5 wording), or move Noor to the reflection that follows.",
        "owner": "Quality Director + L&D", "status": "Open",
        "write_back": "`00_program/characters/companions.md` §5 + `07_…/phase-2-storyboard.md` companion table",
    })
    rows += parse_thin_evidence()

    for row in rows:
        row["tier"] = TIER_OVERRIDES.get(row["id"]) or tier_for(
            row["id"].split("/")[-1], row["modules"], row["question"] + " " + row["recommendation"])
        row["due"] = DUE[row["tier"]]
    rows.sort(key=lambda r: (r["tier"], r["id"]))

    md = [
        "# Phase 0 decision sheet — kick-off working document",
        "",
        "![My Clinic logo](brand/logo-preview.png)",
        "",
        f"> Generated by `tools/build_decision_sheet.py` on **{TODAY}** from the controlled Phase 0 "
        "files, the cross-module decision log, the SCORM structure summary and programme gap G2/G4. "
        f"Proposed kick-off: **{KICKOFF}**. Recommended answers are drafts copied from the plans for "
        "the owner to confirm — **nothing here is policy until the owner writes it into the file "
        "named in “Write back to”.**",
        "",
        f"| Scope | Count |", "|---|---:|",
        f"| Open decisions listed | {len(rows)} |",
        f"| Tier 1 — safety, identifiers, PHI, incident rules (due {DUE[1]}) | {sum(1 for r in rows if r['tier'] == 1)} |",
        f"| Tier 3 — programme enablers D9/D10/D11 (due {DUE[3]}) | {sum(1 for r in rows if r['tier'] == 3)} |",
        f"| Tier 2 — module content facts (due {DUE[2]}) | {sum(1 for r in rows if r['tier'] == 2)} |",
        "",
        "How to close a row: the owner writes the decision and its source (policy number, poster, "
        "email) in the Phase 0 / decision-log file named in “Write back to”, sets its status to "
        "`Closed (date)`, then rerun the standard gate chain (see `next-phases-roadmap.md`). This "
        "sheet is regenerated, never edited by hand.",
        "",
    ]
    for tier in (1, 3, 2):
        md += [f"## Tier {tier} — due {DUE[tier]}", "",
               "| ID | Module(s) | Decision needed | Recommended answer (draft) | Owner (role) | Due | Write back to | Status |",
               "|---|---|---|---|---|---|---|---|"]
        for r in [x for x in rows if x["tier"] == tier]:
            md.append(f"| `{r['id']}` | {r['modules']} | {r['question']} | {r['recommendation']} | "
                      f"{r['owner']} | {r['due']} | {r['write_back']} | {r['status']} |")
        md.append("")
    (PLANS / "00_program" / "decision-sheet.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    with (PLANS / "00_program" / "decision-sheet.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=[
            "id", "tier", "modules", "question", "recommendation", "owner", "due", "write_back", "status"],
            lineterminator="\n")
        writer.writeheader()
        for r in rows:
            writer.writerow({k: re.sub(r"[*`]", "", str(r[k])) for k in writer.fieldnames})

    print(f"decision sheet: {len(rows)} open rows "
          f"(tier1={sum(1 for r in rows if r['tier'] == 1)}, tier3={sum(1 for r in rows if r['tier'] == 3)}, "
          f"tier2={sum(1 for r in rows if r['tier'] == 2)})")


if __name__ == "__main__":
    main()
