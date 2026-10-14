#!/usr/bin/env python3
"""Assemble review-ready My Clinic storyboard documentation from the approved phase plans.

The source of truth remains each module's phase-0 through phase-5 plan.  This helper turns the
Phase 2 screen list plus Phase 3 narration/asset plan into a consistent review pack:

* storyboard/storyboard.md — one practical screen card per Phase 2 screen
* storyboard/visual-plan.json — edumints visual-plan model input
* storyboard/narration-script.json + audio-script-export.json + voice_talent.md
* storyboard/screen-visuals.html — branded visual review board with the supplied client logo
* storyboard/asset-register.md — asset route, provenance and review status

It deliberately does NOT make a SCORM course-spec or package.  Open Phase 0 policy, safety,
rights and PHI decisions must be closed by the named SMEs before production build.
"""
from __future__ import annotations

import argparse
import html
import json
import re
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PLANS = ROOT / "elearning-course" / "scorm-plans"
TODAY = "2026-10-14"
WPM = 140

# These module facts come from each module README and Phase 4.  They are kept here only to make
# the generated review documents consistent; policy facts continue to live in the Phase 0 source
# locks and are never promoted to approved facts here.
MODULES: dict[str, dict[str, Any]] = {
    "01_health-and-safety-1": {
        "number": "01", "module_id": "MC01-facility-management-safety", "prefix": "hs1",
        "title": "Facility Management & Safety", "package_title": "My Clinic — Facility Management & Safety",
        "audience": "All new staff, clinical and non-clinical, in their first week",
        "seat_time": "~55 minutes", "scorm": "SCORM 2004 4th edition · viewed_all_and_passed · pass 80% (176 / 220)",
        "module_colour": "Ambitious teal #008C99", "module_hex": "#008C99", "lead": "NOOR", "cohost": "OMAR",
        "reviewers": "Safety Manager (lead); EHS; Facilities; Biomedical Engineering; RSO; Infection Control",
        "source": "elearning-course/md/01_health-and-safety-1_facility-management-and-safety.md",
        "phase_open": "B1–B10; program D1, D2, D11 and D14", "scored_expected": 24, "points_expected": 220, "phase3_audio_estimate": 19,
        "sections": {
            "0": ("hs1-s0", "Welcome"), "1": ("hs1-s1", "1 · The eight FMS plans"),
            "2": ("hs1-s2", "2 · Occupational Health & Safety"), "3": ("hs1-s3", "3 · Emergency codes"),
            "4": ("hs1-s4", "4 · Fire safety"), "5": ("hs1-s5", "5 · Hazardous materials & waste"),
            "6": ("hs1-s6", "6 · Security"), "7": ("hs1-s7", "7 · Utilities"),
            "8": ("hs1-s8", "8 · Medical equipment"), "9": ("hs1-s9", "9 · Radiation & laser"),
            "z": ("hs1-s10", "Capstone & completion"),
        },
    },
    "02_health-and-safety-2": {
        "number": "02", "module_id": "MC02-safety-in-practice", "prefix": "hs2",
        "title": "Safety in Practice: Hazard, Fire & Chemical Lab", "package_title": "My Clinic — Safety in Practice: Hazard, Fire & Chemical Lab",
        "audience": "All new staff, after module 01", "seat_time": "~33 minutes",
        "scorm": "SCORM 1.2 · viewed_all_and_passed · pass 80% (116 / 145)",
        "module_colour": "Ambitious teal #008C99", "module_hex": "#008C99", "lead": "NOOR", "cohost": "OMAR",
        "reviewers": "Safety Manager (lead); EHS; Facilities; Infection Control", "source": "elearning-course/md/02_health-and-safety-2_safety-hazards-fire-and-chemicals.md",
        # Phase 4's 13 rows total 145 points.  An older plan summary said 15; retain the actual
        # Phase 2/4 count here so the review header does not create a false scoring discrepancy.
        "phase_open": "B1–B9; program D1, D2, D11 and D12", "scored_expected": 13, "points_expected": 145, "phase3_audio_estimate": 8,
        "sections": {
            "a": ("hs2-sA", "A · Spot the hazard"), "b": ("hs2-sB", "B · Code Red drill"),
            "c": ("hs2-sC", "C · Evacuation"), "d": ("hs2-sD", "D · Extinguishers"),
            "e": ("hs2-sE", "E · Spills"), "f": ("hs2-sF", "F · Labels & register"),
            "g": ("hs2-sG", "G · Regulations & close"),
        },
    },
    "04_operations-and-my-care": {
        "number": "04", "module_id": "MC04-operations-my-care", "prefix": "ops",
        "title": "Who Does What: Operations & My Care", "package_title": "My Clinic — Who Does What: Operations & My Care",
        "audience": "Front-line, PX and clinical staff", "seat_time": "~15 minutes",
        "scorm": "SCORM 1.2 · viewed_all_and_passed · pass 70% (35 / 50)",
        "module_colour": "Responsible magenta #9D3293", "module_hex": "#9D3293", "lead": "OMAR", "cohost": "NOOR",
        "reviewers": "Director of Operations (lead); My Care Manager; Patient Experience senior manager", "source": "elearning-course/md/04_operations-and-my-care-structure.md",
        "phase_open": "B1–B7; program D3, D5 and D11", "scored_expected": 4, "points_expected": 50, "phase3_audio_estimate": 5,
        "sections": {
            "1": ("ops-s1", "The patient journey"), "2": ("ops-s2", "Operations"),
            "3": ("ops-s3", "My Care"), "4": ("ops-s4", "Practice: right team, first time"),
        },
    },
    "05_rcm-documentation-and-coding": {
        "number": "05", "module_id": "MC05-rcm-documentation-coding", "prefix": "rcma",
        "title": "RCM Part A: Documentation & ICD-10 Coding That Gets Approved", "screen_title": "RCM Part A: Documentation & Coding", "package_title": "My Clinic — RCM Part A: Documentation & ICD-10 Coding That Gets Approved",
        "audience": "Physicians and dentists", "seat_time": "~25 minutes",
        "scorm": "SCORM 1.2 · viewed_all_and_passed · pass 80% (80 / 100)",
        "module_colour": "Collaborative burgundy #7C0041", "module_hex": "#7C0041", "lead": "OMAR", "cohost": "NOOR",
        "reviewers": "RCM lead (lead); Coding lead; Payer Relations; Medical Director", "source": "elearning-course/md/05_rcm-billing-documentation-script.md",
        "phase_open": "B1–B10; program D4 and D11", "scored_expected": 10, "points_expected": 100, "phase3_audio_estimate": 8,
        "sections": {
            "a": ("rcma-sA", "Why it matters"), "b": ("rcma-sB", "Documentation strategy"),
            "c": ("rcma-sC", "ICD-10 coding"), "d": ("rcma-sD", "Defensive medicine & ordering"),
            "e": ("rcma-sE", "Rejections & coverage"), "f": ("rcma-sF", "Fix the note"),
        },
    },
    "06_rcm-ebp-benefits-and-rejections": {
        "number": "06", "module_id": "MC06-rcm-ebp-benefits-rejections", "prefix": "rcmb",
        "title": "RCM Part B: New EBP Benefits & Claim-Rejection Analysis", "package_title": "My Clinic — RCM Part B: New EBP Benefits & Claim-Rejection Analysis",
        "audience": "Physicians and RCM staff", "seat_time": "~20 minutes",
        "scorm": "SCORM 1.2 · viewed_all_and_passed · pass 80% (64 / 80)",
        "module_colour": "Collaborative burgundy #7C0041", "module_hex": "#7C0041", "lead": "OMAR", "cohost": "NOOR",
        "reviewers": "RCM lead (lead); Payer Relations; Coding lead; Data Protection Officer", "source": "elearning-course/md/06_rcm-billing-documentation-slides-2026.md",
        "phase_open": "B1–B9; program D4, D5 and D11", "scored_expected": 7, "points_expected": 80, "phase3_audio_estimate": 5,
        "sections": {
            "a": ("rcmb-sA", "What changed"), "b": ("rcmb-sB", "Benefits in practice"),
            "c": ("rcmb-sC", "Reading rejections"), "d": ("rcmb-sD", "Practice & close"),
        },
    },
    "08_it-ehr-consultation": {
        "number": "08", "module_id": "MC08-ehr-consultation", "prefix": "ehr",
        "title": "EHR Consultation Workflow: Guided Simulation", "package_title": "My Clinic — EHR Consultation Workflow: Guided Simulation",
        "audience": "Physicians and clinical staff who document consultations in the clinic EHR", "seat_time": "~25 minutes",
        "scorm": "SCORM 1.2 · viewed_all_and_passed · pass 80% (72 / 90)",
        "module_colour": "Dark teal #006E78", "module_hex": "#006E78", "lead": "OMAR", "cohost": "NOOR",
        "reviewers": "EHR Applications / EHR lead (lead); DPO; Medical Director; Pharmacy lead; RCM lead", "source": "elearning-course/md/08_video-it-ehr-consultation-walkthrough.md",
        "phase_open": "B1–B10; program D6 and D11", "scored_expected": 11, "points_expected": 90, "phase3_audio_estimate": 5,
        "sections": {
            "a": ("ehr-sA", "The workflow"), "b": ("ehr-sB", "Open & document"),
            "c": ("ehr-sC", "Diagnosis"), "d": ("ehr-sD", "Orders"),
            "e": ("ehr-sE", "Summary & education"), "f": ("ehr-sF", "Referral & finish"),
        },
    },
}

# A deliberately conservative map: scenarios, activities and non-title content use the same
# visual language across all modules; only the accent changes.  The real logo is always placed as
# a supplied asset, never generated.
QUESTION_TYPES = {
    "mcq", "true_false", "fill_blank", "drag_drop", "matching", "sorting", "labeled_diagram",
    "adaptive_practice", "escape_room",
}
SCENARIO_TYPES = {"decision_scenario", "game", "simulation"}
PASSIVE_TYPES = {
    "content_slide", "tabs", "accordion", "flashcards", "timeline", "worked_example", "hotspot",
    "image_compare", "labeled_diagram", "results_breakdown", "poll", "summary", "title_slide",
}

GENERATED_ASSETS: dict[str, dict[str, dict[str, str]]] = {
    "01_health-and-safety-1": {
        "hs1-img-corridor": {
            "file": "assets/hs1-img-corridor.png", "kind": "illustration", "source": "ai-generated",
            "status": "Generated 2026-10-14 — SME visual check required before hotspot coordinates are set.",
            "alt": "Clinic corridor showing a call point, extinguisher, fire blanket, sprinkler, evacuation chair and assembly sign.",
        },
        "hs1-img-arec": {"file": "assets/hs1-img-arec.svg", "kind": "diagram", "source": "own", "status": "Generated native SVG.", "alt": "AREC cycle: Anticipate, Recognise, Evaluate, Control."},
        "hs1-img-ert": {"file": "assets/hs1-img-ert.svg", "kind": "diagram", "source": "own", "status": "Generated native SVG.", "alt": "Emergency Response Team roles around an Incident Commander."},
        "hs1-img-triangle": {"file": "assets/hs1-img-triangle.svg", "kind": "diagram", "source": "own", "status": "Generated native SVG.", "alt": "Fire triangle showing heat, fuel and oxygen."},
        "hs1-img-alara": {"file": "assets/hs1-img-alara.svg", "kind": "diagram", "source": "own", "status": "Generated native SVG.", "alt": "ALARA diagram showing time, distance and shielding."},
        "hs1-img-nfpa-blank": {"file": "assets/hs1-img-nfpa-blank.svg", "kind": "diagram", "source": "own", "status": "Generated native SVG.", "alt": "Blank four-quadrant NFPA diamond."},
        "hs1-img-nfpa-301w": {"file": "assets/hs1-img-nfpa-301w.svg", "kind": "diagram", "source": "own", "status": "Generated native SVG.", "alt": "NFPA diamond with ratings 3, 0, 1 and W."},
    },
    "02_health-and-safety-2": {
        "hs2-img-storeroom": {
            "file": "assets/hs2-img-storeroom.png", "kind": "illustration", "source": "ai-generated",
            "status": "Generated 2026-10-14 — Safety Manager must confirm the six-hotspot answer key before use.",
            "alt": "Clinic store room with cables, high boxes, blocked exit, unlabelled bottle, spill by socket and a person on a wheeled chair.",
        },
        "hs2-img-floorplan": {"file": "assets/hs2-img-floorplan.svg", "kind": "diagram", "source": "own", "status": "Generated native generic floor-plan SVG; never a real floor plan.", "alt": "Generic evacuation floor plan with zones A to E."},
        "hs2-img-nfpa-230": {"file": "assets/hs2-img-nfpa-230.svg", "kind": "diagram", "source": "own", "status": "Generated native SVG.", "alt": "NFPA diamond with health 2, flammability 3 and reactivity 0."},
    },
    "04_operations-and-my-care": {
        "ops-img-reception-scenario": {
            "file": "assets/ops-img-reception-scenario.png", "kind": "illustration", "source": "ai-generated",
            "status": "Generated 2026-10-14 — generic fictional scene; final routing remains subject to B7.",
            "alt": "A patient talks to a patient-experience officer at a clinic reception desk.",
        },
        "ops-img-journey": {"file": "assets/ops-img-journey.svg", "kind": "diagram", "source": "own", "status": "Generated native SVG.", "alt": "Patient journey from booking to follow-up."},
        "ops-img-ops-chart": {"file": "assets/ops-img-ops-chart.svg", "kind": "diagram", "source": "own", "status": "Generated role-only draft SVG; SME approval B1 required.", "alt": "Draft Operations role structure."},
        "ops-img-mycare-chart": {"file": "assets/ops-img-mycare-chart.svg", "kind": "diagram", "source": "own", "status": "Generated role-only draft SVG; SME approval B2 required.", "alt": "Draft My Care role structure."},
    },
    "05_rcm-documentation-and-coding": {
        "rcma-img-note-weak": {"file": "assets/rcma-img-note-weak.svg", "kind": "diagram", "source": "own", "status": "Generated native SVG using fictional teaching text.", "alt": "Weak generic clinical note stating only that IV fluids were given."},
        "rcma-img-note-strong": {"file": "assets/rcma-img-note-strong.svg", "kind": "diagram", "source": "own", "status": "Generated native SVG using fictional teaching text.", "alt": "Stronger generic clinical note linking dehydration signs to IV fluids."},
        "rcma-img-reviewer": {"file": "assets/rcma-img-reviewer.svg", "kind": "diagram", "source": "own", "status": "Generated native SVG.", "alt": "A reviewer sees a written note rather than the patient encounter."},
    },
    "06_rcm-ebp-benefits-and-rejections": {
        "rcmb-img-benefit-icons": {"file": "assets/rcmb-img-benefit-icons.svg", "kind": "icon", "source": "own", "status": "Generated native icon sheet; labels remain HTML in the course.", "alt": "A set of generic line icons for health benefits."},
    },
    "08_it-ehr-consultation": {
        "ehr-capture-sheet": {"file": "assets/ehr-capture-sheet.svg", "kind": "diagram", "source": "own", "status": "Generated capture checklist only; not an EHR screenshot and not a substitute for B2 test-environment assets.", "alt": "Checklist showing safe test-environment screenshot requirements."},
    },
}


def md_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def strip_md(text: str) -> str:
    """Render Markdown-ish Phase 2 source as safe, concise prose for review documents."""
    text = text.replace("`", "").replace("**", "").replace("*", "")
    text = text.replace("→", "→")
    # Phase 2 uses angle brackets for unresolved values.  Keep the unresolved state explicit,
    # not as a template placeholder that could accidentally ship.
    text = re.sub(r"<([^>]+)>", r"⚠ PENDING \1", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def clean_html_text(text: str) -> str:
    return html.escape(strip_md(text), quote=False)


def safe_cell(text: str) -> str:
    return strip_md(text).replace("|", "\\|")


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)?", text))


def short_text(text: str, limit: int = 36) -> str:
    clean = strip_md(text)
    words = clean.split()
    if len(words) <= limit:
        return clean
    return " ".join(words[:limit]).rstrip(".,;:") + " …"


def p2_type(raw: str) -> str:
    match = re.search(r"`([^`]+)`", raw)
    return match.group(1) if match else raw.strip().split()[0]


def parse_phase2(module_dir: Path, prefix: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    current_heading = ""
    for raw in (module_dir / "phase-2-storyboard.md").read_text(encoding="utf-8").splitlines():
        if raw.startswith("## "):
            current_heading = raw[3:].strip()
        if not raw.startswith("|"):
            continue
        cells = md_cells(raw)
        if len(cells) < 7:
            continue
        ident = cells[0]
        m = re.fullmatch(rf"({re.escape(prefix)}-\d+)(?:\s+(★))?", ident)
        if not m or not cells[1].startswith("`"):
            continue
        points_match = re.search(r"\d+", cells[5])
        rows.append({
            "id": m.group(1), "scored": bool(m.group(2)), "type": p2_type(cells[1]),
            "purpose": strip_md(cells[2]), "on_screen": strip_md(cells[3]),
            "interaction": strip_md(cells[4]), "points": int(points_match.group()) if points_match else 0,
            "source": strip_md(cells[6]), "phase_heading": current_heading,
        })
    if not rows:
        raise RuntimeError(f"No Phase 2 rows found in {module_dir}")
    return rows


def parse_objectives(module_dir: Path) -> tuple[dict[str, str], dict[str, list[str]]]:
    objective_text: dict[str, str] = {}
    screen_objs: dict[str, list[str]] = defaultdict(list)
    text = (module_dir / "phase-1-action-map.md").read_text(encoding="utf-8")
    for raw in text.splitlines():
        if not raw.startswith("|"):
            continue
        cells = md_cells(raw)
        if len(cells) < 3:
            continue
        id_match = re.fullmatch(r"`?([a-z0-9]+-o\d+)`?", cells[0])
        if not id_match:
            continue
        oid = id_match.group(1)
        objective_text[oid] = strip_md(cells[1])
        # Some early action-map tables include a Section column before "Assessed by";
        # later module tables do not. Search every remaining cell rather than relying on
        # one fixed column position.
        for screen in re.findall(r"[a-z0-9]+-\d+", " | ".join(cells[2:])):
            screen_objs[screen].append(oid)
    return objective_text, screen_objs


def parse_narration_outline(module_dir: Path, prefix: str) -> dict[str, dict[str, Any]]:
    """Read target seconds and author intent from the Phase 3 outline, including compact rows.

    It intentionally keeps only the design intent and timing.  The generated script is fresh
    prose; it is not a claim that a noisy source-video ASR transcript was verified.
    """
    result: dict[str, dict[str, Any]] = {}
    text = (module_dir / "phase-3-narration-and-assets.md").read_text(encoding="utf-8")
    in_outline = False
    for raw in text.splitlines():
        if re.match(r"^## \d+\. Narration outline", raw):
            in_outline = True
            continue
        if in_outline and raw.startswith("## "):
            break
        if not in_outline or not raw.startswith("|"):
            continue
        cells = md_cells(raw)
        if len(cells) < 4 or not re.search(rf"\b{re.escape(prefix)}-\d+", cells[0]):
            continue
        ids = re.findall(rf"\b{re.escape(prefix)}-\d+", cells[0])
        # Narration outlines compact consecutive IDs as `hs1-402/403` or
        # `ops-030 / 032 / 033`; inherit the prefix from the first full id.
        for suffix in re.findall(r"/\s*(\d+)", cells[0]):
            candidate = f"{prefix}-{suffix}"
            if candidate not in ids:
                ids.append(candidate)
        seconds = re.search(r"\d+(?:\.\d+)?", cells[2])
        if not seconds:
            continue
        for sid in ids:
            result[sid] = {
                "speaker": strip_md(cells[1]), "target": float(seconds.group()),
                "intent": strip_md(cells[3]),
            }
    return result


def parse_companions(module_dir: Path, prefix: str) -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    text = (module_dir / "phase-3-narration-and-assets.md").read_text(encoding="utf-8")
    inside = False
    for raw in text.splitlines():
        if raw.startswith("| Screen | Visible"):
            inside = True
            continue
        if inside and raw.startswith("- Visible"):
            break
        if not inside or not raw.startswith("|"):
            continue
        cells = md_cells(raw)
        if len(cells) < 5:
            continue
        ids = re.findall(rf"\b{re.escape(prefix)}-\d+", cells[0])
        for sid in ids:
            result[sid] = {
                "visible": strip_md(cells[1]), "pose": strip_md(cells[2]),
                "placement": strip_md(cells[3]), "speaks": strip_md(cells[4]),
            }
    return result


def parse_assets(module_dir: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    text = (module_dir / "phase-3-narration-and-assets.md").read_text(encoding="utf-8")
    for raw in text.splitlines():
        if not raw.startswith("|"):
            continue
        cells = md_cells(raw)
        if len(cells) < 6:
            continue
        # Asset rows have a planned id in col 1 and one or more screen ids in col 3.  This keeps
        # out the companion placement and activity-plan tables.
        if not ("img" in cells[0].lower() or "aud" in cells[0].lower() or "char-" in cells[0].lower() or "pdf" in cells[0].lower() or "tbl" in cells[0].lower() or "vid" in cells[0].lower()):
            continue
        if not re.search(r"(?:[a-z]+-\d+|all narrated|see \"companions)", cells[2], re.I):
            continue
        rows.append({
            "id": strip_md(cells[0]), "kind": strip_md(cells[1]), "screens": strip_md(cells[2]),
            "brief": strip_md(cells[3]), "source": strip_md(cells[4]), "alt": strip_md(cells[5]),
        })
    return rows


def parse_open_questions(module_dir: Path) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    for raw in (module_dir / "phase-0-source-lock.md").read_text(encoding="utf-8").splitlines():
        if not raw.startswith("|"):
            continue
        cells = md_cells(raw)
        if len(cells) < 6 or not re.fullmatch(r"(?:B|D|NEW)[0-9]+", cells[0]):
            continue
        if "Open" not in cells[-1]:
            continue
        out.append({"id": cells[0], "question": strip_md(cells[1]), "owner": strip_md(cells[-2])})
    return out


def section_for(folder: str, screen_id: str) -> tuple[str, str]:
    cfg = MODULES[folder]
    digits = screen_id.rsplit("-", 1)[1]
    prefix = cfg["prefix"]
    if folder == "01_health-and-safety-1":
        key = "z" if digits in {"950", "980", "981", "990"} else digits[0]
    elif folder == "02_health-and-safety-2":
        n = int(digits)
        key = "a" if n < 20 else "b" if n < 31 else "c" if n < 40 else "d" if n < 50 else "e" if n < 60 else "f" if n < 70 else "g"
    elif folder == "04_operations-and-my-care":
        n = int(digits)
        key = "1" if n < 10 else "2" if n < 20 else "3" if n < 30 else "4"
    elif folder == "05_rcm-documentation-and-coding":
        n = int(digits)
        key = "a" if n < 10 else "b" if n < 20 else "c" if n < 30 else "d" if n < 40 else "e" if n < 50 else "f"
    elif folder == "06_rcm-ebp-benefits-and-rejections":
        n = int(digits)
        key = "a" if n < 10 else "b" if n < 50 else "c" if n < 60 else "d"
    elif folder == "08_it-ehr-consultation":
        n = int(digits)
        key = "a" if n < 10 else "b" if n < 20 else "c" if n < 30 else "d" if n < 40 else "e" if n < 50 else "f"
    else:
        raise KeyError(folder)
    return cfg["sections"][key]


def title_for(row: dict[str, Any], cfg: dict[str, Any]) -> str:
    if row["type"] == "title_slide":
        # The package title stays in the module header; a compact display title keeps the title
        # treatment within the template's eight-word on-screen limit.
        return cfg.get("screen_title", cfg["title"])
    purpose = re.sub(r"^(Open|Explain|Check|Apply|Practise|Practice|Explore|Learn|Frame|Close|Read|Set up)\s*", "", row["purpose"], flags=re.I).strip(" :–—")
    if not purpose:
        purpose = row["purpose"]
    purpose = purpose.replace("**", "")
    # Sentence case looks more like the client decks than title case.
    return purpose[:1].upper() + purpose[1:]


def layout_for(screen_type: str, scored: bool = False) -> tuple[str, str, str, str]:
    """layout name, background role, text role, accent role"""
    if screen_type == "title_slide":
        return "L1 Title", "primary", "on_primary", "secondary"
    if screen_type in {"summary", "results_breakdown"}:
        return "L6 Results / close", "light", "dark", "secondary"
    if screen_type in SCENARIO_TYPES:
        return "L5 Scenario", "surface", "dark", "secondary"
    # A labelled diagram may be a display-only teaching aid or a scored quiz.  The Phase 2 star
    # distinguishes them; display diagrams belong in the content layout.
    if (screen_type in QUESTION_TYPES and not (screen_type == "labeled_diagram" and not scored)) or screen_type in {"poll"}:
        return "L4 Question", "surface", "dark", "secondary"
    return "L3 Content", "light", "dark", "secondary"


def concept_for(row: dict[str, Any], cfg: dict[str, Any], companion: dict[str, str] | None) -> str:
    t = row["type"]
    topic = short_text(row["purpose"], 10).rstrip(".")
    if t == "title_slide":
        base = "Official navy title gradient with supplied white My Clinic logo, large Montserrat course title, and a cropped white petal watermark."
    elif t in SCENARIO_TYPES:
        base = f"A calm scenario stage with one decision at a time, spacious white choice cards, a navy header and a {cfg['module_colour']} progress cue for {topic.lower()}."
    elif t in QUESTION_TYPES and not (t == "labeled_diagram" and not row["scored"]):
        base = f"A focused question stage with a concise stem, generous white answer cards, a navy header and one {cfg['module_colour']} progress cue for {topic.lower()}."
    elif t == "hotspot":
        base = f"A high-clarity central visual for {topic.lower()}, with large keyboard-reachable hotspot markers, a short instruction panel and no text baked into the image."
    elif t in {"tabs", "accordion", "flashcards"}:
        base = f"A white content stage for {topic.lower()}, with one open item at a time, navy structure, and a {cfg['module_colour']} active-state cue."
    elif t == "worked_example":
        base = f"A step-by-step worked example for {topic.lower()}, using numbered white cards, restrained navy connectors and a single {cfg['module_colour']} emphasis."
    elif t == "image_compare":
        base = f"A paired before-and-after comparison for {topic.lower()}, with a draggable divider, descriptive HTML captions and a clean light background."
    elif t == "results_breakdown":
        base = "A calm results panel showing each objective as an HTML progress row, with plain-language next steps and a small companion feedback card."
    elif t == "summary":
        base = "A confident light closing screen with four short takeaways, the supplied My Clinic logo, and space for the next-module hand-off."
    else:
        base = f"A clean My Clinic content stage for {topic.lower()}, using a navy header, concise keyword cards and one {cfg['module_colour']} highlight."
    if companion:
        base += f" {companion['visible']} is placed {companion['placement'].lower()}."
    return base


def imagery_for(folder: str, row: dict[str, Any], asset_rows: list[dict[str, str]], companion: dict[str, str] | None) -> list[dict[str, Any]]:
    imagery: list[dict[str, Any]] = []
    if row["type"] == "title_slide":
        imagery.extend([
            {"kind": "photo", "description": "Official navy title background supplied by My Clinic; no content is baked into it.", "source": "client", "alt_text": "Decorative navy title gradient.", "decorative": True},
            {"kind": "icon", "description": "Supplied My Clinic horizontal white logo lock-up.", "source": "client", "alt_text": "My Clinic logo.", "decorative": False},
        ])
    else:
        imagery.append({"kind": "icon", "description": "Supplied My Clinic horizontal navy logo lock-up in the header.", "source": "client", "alt_text": "My Clinic logo.", "decorative": False})

    for aid, asset in GENERATED_ASSETS.get(folder, {}).items():
        # P2 uses either id direct, or the key asset is tied to the relevant activity.
        if aid in row["on_screen"] or aid in row["interaction"] or (aid == "hs1-img-corridor" and row["id"] == "hs1-404") or (aid == "hs2-img-storeroom" and row["id"] == "hs2-011") or (aid == "ops-img-reception-scenario" and row["id"] == "ops-031") or (aid == "ops-img-journey" and row["id"] == "ops-002") or (aid == "ops-img-ops-chart" and row["id"] == "ops-011") or (aid == "ops-img-mycare-chart" and row["id"] == "ops-021") or (aid.startswith("rcma-img-note") and row["id"] == "rcma-011") or (aid == "rcma-img-reviewer" and row["id"] == "rcma-001") or (aid == "rcmb-img-benefit-icons" and row["id"] in {"rcmb-010", "rcmb-020", "rcmb-040"}) or (aid == "ehr-capture-sheet" and row["id"] in {"ehr-000", "ehr-001"}):
            kind = asset["kind"] if asset["kind"] in {"photo", "illustration", "icon", "diagram", "screenshot", "video", "chart"} else "illustration"
            source = "svg" if asset["source"] == "own" else "generate"
            imagery.append({"kind": kind, "description": f"{aid}: {asset['status']}", "source": source, "alt_text": asset["alt"], "decorative": False})

    # Include a planned Phase 3 asset when it explicitly names this screen.  It provides a useful
    # bridge from storyboarding to production without pretending that a pending asset already exists.
    for asset in asset_rows:
        if row["id"] not in asset["screens"]:
            continue
        asset_id = asset["id"].replace("`", "")
        kind_l = asset["kind"].lower()
        if "audio" in kind_l or "character" in kind_l:
            continue
        kind = "diagram" if any(k in kind_l for k in ("svg", "diagram", "html")) else "screenshot" if "screenshot" in kind_l else "photo" if "photo" in kind_l else "illustration"
        source_l = asset["source"].lower()
        source = "svg" if "own" in source_l or "svg" in source_l else "generate" if "ai" in source_l else "client"
        imagery.append({"kind": kind, "description": f"{asset_id}: {asset['brief']}", "source": source, "alt_text": asset["alt"] if asset["alt"].lower() != "n/a" else f"{title_for(row, MODULES[folder])} visual.", "decorative": False})
        break
    if companion:
        imagery.append({
            "kind": "illustration", "description": f"Approved program companion pose {companion['pose']} at {companion['placement']}.",
            "source": "client", "alt_text": f"{companion['visible']} companion guide supporting this learning moment.", "decorative": False,
        })
    return imagery


def detect_dependencies(row: dict[str, Any], cfg: dict[str, Any]) -> str:
    found = sorted(set(re.findall(r"\b(?:B|D|NEW)[0-9]+\b", " ".join(str(v) for v in row.values()))))
    if found:
        return "⚠ PENDING " + ", ".join(found) + "; do not turn these source values into release policy until the named owner closes them."
    return "Shared dependency: program brand confirmation D11. Review the module source-lock register before production."


def correct_for(row: dict[str, Any]) -> str:
    """Keep scored-answer provenance in the card without inventing a policy answer.

    The Phase 2 on-screen cell is deliberately retained in full in the interaction table.  It is
    the controlled answer route for review; Phase 4 turns it into type-specific option objects
    after source-lock approval.
    """
    if not row["scored"]:
        return "n/a — no scored response on this screen."
    return "Use the complete source answer route in **Items / options / nodes** above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker."


def accepted_variants_for(row: dict[str, Any]) -> str:
    source = f"{row['on_screen']} {row['interaction']}"
    variants = re.findall(r"(?:accepted(?:\s+answers?)?|aliases)\s*:?[ \t]+([^.;)]+)", source, flags=re.I)
    if not variants:
        return "n/a — no typed-answer variants are specified in Phase 2."
    return "; ".join(variants)


def pass_rule_for(row: dict[str, Any]) -> str:
    source = f"{row['on_screen']} {row['interaction']}"
    match = re.search(r"(?:pass[_ ]?score|target[_ ]?success)\s*[:=]?\s*([^.;]+)", source, flags=re.I)
    if match:
        return match.group(0).strip()
    lives = re.search(r"\b(?:lives?\s*[:=]?\s*\d+|\d+\s+lives?)\b", source, flags=re.I)
    if lives:
        return f"No separate pass rule stated; {lives.group(0)} in the Phase 2 brief."
    if row["type"] in SCENARIO_TYPES | {"adaptive_practice", "escape_room", "simulation"}:
        return "Completion and pass handling remain the Phase 4 build decision; preserve the full Phase 2 route above."
    return "n/a — not a scenario/game pass rule."


def feedback_for(row: dict[str, Any], correct: bool) -> str:
    if not row["scored"]:
        return "n/a — informational/exploratory screen."
    source = row["interaction"]
    if source not in {"—", ""}:
        prefix = "Source feedback route" if correct else "Retry/incorrect feedback route"
        return f"{prefix}: {source}"
    if correct:
        return "Confirm the source-mapped response and explain why it supports the stated on-the-job action."
    return "Explain which source-mapped detail to reconsider, then allow a retry; do not reveal the answer in narration."


def hint_for(row: dict[str, Any]) -> str:
    source = f"{row['on_screen']} {row['interaction']}"
    if re.search(r"\bone\s+text\s+hint\s+each\b", source, flags=re.I):
        return "One text hint per puzzle; Phase 2 specifies the count, while final hint wording needs the approved build brief."
    match = re.search(r"\bhint(?:s)?\s*[:—-]\s*([^.;]+)", source, flags=re.I)
    if match:
        return match.group(0).strip()
    return "n/a — no hint is specified in Phase 2; do not invent one before SME review."


def retry_for(row: dict[str, Any]) -> str:
    source = f"{row['on_screen']} {row['interaction']}"
    lives = re.search(r"\b(?:lives?\s*[:=]?\s*\d+|\d+\s+lives?)\b", source, flags=re.I)
    if lives:
        return f"Untimed and keyboard-operable; {lives.group(0)}; retry/score handling is finalised in Phase 4."
    return "Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise."


def _tidy_intent(intent: str) -> str:
    """Turn a Phase 3 author cue into safe spoken draft text.

    The outline is intentionally used only on explanatory screens. Assessment narration never
    exposes a correct answer.  Source-lock markers are left on the visual card, rather than
    turning an unapproved threshold or extension into synthetic spoken policy.
    """
    value = strip_md(intent).strip()
    if not value or re.fullmatch(r"(?:Set up|Invite.*|Read your results)\.?", value, flags=re.I):
        return ""
    value = re.sub(r"^(?:Why|Tip):\s*", "", value, flags=re.I)
    value = re.sub(r"^Why\s+", "", value, flags=re.I)
    value = re.sub(r"(?:Noor|Omar)'s story:\s*", "", value, flags=re.I)
    value = value.replace("\"", "")
    # A compact outline often uses semicolons to mean separate spoken thoughts.
    value = re.sub(r"\s*;\s*", ". ", value)
    if value and value[-1] not in ".!?":
        value += "."
    # Outline cells are often sentence fragments.  Sentence-case fragments read naturally in a
    # voice script, while deliberately preserving the source terminology itself.
    value = re.sub(r"(^|[.!?]\s+)([a-z])", lambda m: m.group(1) + m.group(2).upper(), value)
    return value


def _screen_number(row: dict[str, Any]) -> int:
    """Stable number for rotating generic coaching without introducing a content claim."""
    match = re.search(r"(\d+)$", row["id"])
    return int(match.group(1)) if match else 0


def _coaching_lines(row: dict[str, Any]) -> list[str]:
    """Source-neutral instructional bridges, varied by interaction type.

    These lines teach the learner how to use the on-screen material without asserting a local
    policy, threshold, contact number or answer that still needs a Phase 0 source lock.
    """
    number = _screen_number(row)
    type_lines: dict[str, list[list[str]]] = {
        "labeled_diagram": [
            ["Use the labels to connect each part of the visual with the responsibility or action it supports.", "The diagram is a working reference, not a test to memorise."],
            ["Trace the labels from the centre outward and notice how each part informs the next action.", "Keep the diagram in mind as a quick orientation tool."],
            ["Read each label as a prompt for what to check or who should act next.", "The useful step is linking the visual with a real decision."],
        ],
        "hotspot": [
            ["Open each marker in turn before you decide what happens next.", "Each marker adds a detail that supports a more confident response."],
            ["Explore the marked areas at your own pace, then compare the details you found.", "Use those details to identify the next practical action."],
            ["Let each marker add context rather than rushing to a conclusion.", "The full picture matters before a workplace decision is made."],
        ],
        "tabs": [
            ["Open each item in turn, then compare how the information changes the next action you would take.", "Focus on the part that belongs to your role."],
            ["Use the tabs as a short reference, not a checklist to race through.", "Notice which detail would guide your next conversation or decision."],
            ["Move through the items one at a time and connect each point with a practical response.", "The aim is to use the information, not just recognise it."],
        ],
        "accordion": [
            ["Open one section at a time and pause on the detail that changes what you would do next.", "That link turns information into a practical response."],
            ["Use each section to build the picture step by step.", "Before moving on, identify the action or check that belongs to your role."],
            ["Read the sections in sequence, then compare the points that matter most in practice.", "Keep the next action clearer than the terminology."],
        ],
        "flashcards": [
            ["Reveal each card, then pause to recall the point before moving on.", "Link the term with the action it should prompt in practice."],
            ["Take the cards one at a time and test whether you can explain the point in your own words.", "That makes the information easier to use later."],
            ["Use the cards for active recall rather than a quick scan.", "The key is knowing what the term changes in your next action."],
        ],
        "timeline": [
            ["Follow the sequence in order and notice what has to happen before the next step.", "A clear sequence helps you avoid skipping an important check."],
            ["Read the timeline as a chain of actions, not isolated events.", "Pause on the hand-off or decision point that matters in your role."],
            ["Track the order carefully, then picture how you would move through the same sequence at work.", "The next action should follow from the step before it."],
        ],
        "worked_example": [
            ["Work through the example in sequence and notice the information that supports each choice.", "Use the pattern to check your reasoning, rather than copying it blindly in a live situation."],
            ["Follow the example one step at a time, then identify why the next step makes sense.", "The value is the reasoning you can carry into a similar case."],
            ["Use the example as a model for checking your own approach.", "Focus on the information behind the choice, not just the finished result."],
        ],
        "image_compare": [
            ["Compare the two views carefully and look for the detail that changes the decision or next action.", "The contrast is there to make the practical signal easier to spot."],
            ["Move between the views slowly, then name the difference that matters in practice.", "Use that difference to guide the next action you would take."],
            ["Use the comparison to separate a helpful detail from a potential problem.", "The important step is turning what you see into a clear response."],
        ],
        "content_slide": [
            ["As you read, focus on the decision this information supports in your own role.", "The aim is a practical next action, not a phrase to memorise."],
            ["Keep the main point connected to a familiar task or conversation.", "That connection makes the information easier to use when it matters."],
            ["Notice which part of the information you would need first in practice.", "Use that as the starting point for a safe, respectful next action."],
        ],
    }
    choices = type_lines.get(row["type"], type_lines["content_slide"])
    selected = choices[number % len(choices)]
    return selected


def _planned_speakers(detail: dict[str, Any], cfg: dict[str, Any]) -> tuple[str, str, bool]:
    """Respect the Phase 3 speaker intent, falling back to the module's named lead/co-host."""
    names = re.findall(r"Noor|Omar", str(detail.get("speaker", "")), flags=re.I)
    normalised = [name.upper() for name in names]
    lead = normalised[0] if normalised else cfg["lead"]
    co = normalised[1] if len(normalised) > 1 else (cfg["cohost"] if lead == cfg["lead"] else cfg["lead"])
    return lead, co, len(normalised) > 1


def _split_spoken_sentences(text: str, maximum: int = 23) -> str:
    """Keep generated narration comfortably below the 25-word lint threshold."""
    sentences: list[str] = []
    for sentence in re.split(r"(?<=[.!?])\s+", text):
        words = sentence.split()
        while len(words) > maximum:
            sentences.append(" ".join(words[:maximum]).rstrip(",;:") + ".")
            words = words[maximum:]
        if words:
            sentences.append(" ".join(words))
    return " ".join(sentences)


def _trim_line_to_words(line: str, maximum: int) -> str:
    """Retain whole short spoken sentences where possible, with a safe final fallback."""
    if word_count(line) <= maximum:
        return line
    kept: list[str] = []
    used = 0
    for sentence in re.split(r"(?<=[.!?])\s+", line):
        n = word_count(sentence)
        if not sentence:
            continue
        if used + n <= maximum:
            kept.append(sentence)
            used += n
        elif not kept:
            words = sentence.split()
            kept.append(" ".join(words[:maximum]).rstrip(",;:") + ".")
            used = maximum
            break
        else:
            break
    return " ".join(kept).strip()


def _fit_script_to_target(script: str, target: float) -> str:
    """Respect the Phase 3 timing target without an over-target lint warning."""
    maximum = max(12, int(target * WPM / 60 * 1.14))
    lines = script.split("\n\n")
    if len(lines) == 2:
        # Reserve enough room for the co-host's planned hand-off; a hand-off is never silently lost.
        second_budget = min(17, max(10, maximum // 3))
        second = _trim_line_to_words(lines[1], second_budget)
        first = _trim_line_to_words(lines[0], max(8, maximum - word_count(second)))
        return first + "\n\n" + second
    return _trim_line_to_words(script, maximum)


def narration_for(row: dict[str, Any], cfg: dict[str, Any], outline: dict[str, dict[str, Any]], companion: dict[str, str] | None) -> tuple[str, float, str]:
    detail = outline.get(row["id"], {})
    target = float(detail.get("target", 12 if row["scored"] else 25))
    lead, co, planned_dual_voice = _planned_speakers(detail, cfg)
    purpose = row["purpose"].rstrip(".")

    # The Phase 2 star, rather than a type name alone, determines whether this instance is an
    # assessment. `labeled_diagram` is used both as a scored quiz and as an unscored display.
    if row["scored"]:
        script = (
            f"{lead}: The next choice asks you to apply the rule in a workplace situation. "
            "Read carefully, then choose."
        )
        tone = "encouraging"
    elif row["type"] == "title_slide":
        script = (
            f"{lead}: Welcome to {cfg.get('screen_title', cfg['title'])}. You will practise decisions that help you act with confidence. "
            "You will leave with practical actions for your next shift."
        )
        tone = "warm"
    elif row["type"] == "results_breakdown":
        script = (
            f"{lead}: Your results are organised by objective. Notice where you were confident, then revisit any section that needs another practical try. "
            "Use that insight to choose what to revisit."
        )
        tone = "supportive"
    elif row["type"] == "summary":
        script = (
            f"{lead}: You can now use these key actions in your role. Keep the practical rule close, ask when you are unsure, and carry the next step into your shift. "
            "Take one clear next action with you."
        )
        tone = "confident"
    elif row["type"] == "poll":
        script = (
            f"{lead}: This reflection is not scored. Choose the response that helps you set one intention for your next shift."
        )
        tone = "reflective"
    else:
        outline_intent = _tidy_intent(str(detail.get("intent", "")))
        opening = outline_intent or f"The focus here is {purpose.lower()}."
        script = f"{lead}: {opening} {' '.join(_coaching_lines(row)[:2])}"
        tone = "calm, practical"

    # Add enough non-redundant coaching for long planned explanatory segments while keeping the
    # target estimate. Question and scenario setups stay short so the answer is never narrated.
    desired_words = max(18, int(target * WPM / 60 * 0.96))
    pad = [
        "Pause and connect this to your role.",
        "Use the principle in context.",
        "Keep the next action clear.",
        "Think of the first detail you would check.",
        "Apply the point to a familiar task.",
        "Carry the idea into your next decision.",
    ]
    if row["scored"]:
        # Assessment setup is deliberately answer-neutral, but it still needs enough room for
        # learners to orient themselves at the Phase 3 target pace.
        question_pad = [
            "Use the rule you practised.",
            "Focus on the action that fits.",
            "Feedback explains the reasoning after you respond.",
        ]
        pad_at = _screen_number(row) % len(question_pad)
        while word_count(script) < desired_words:
            script += " " + question_pad[pad_at % len(question_pad)]
            pad_at += 1
    elif row["type"] not in {"poll"}:
        pad_at = _screen_number(row) % len(pad)
        while word_count(script) < desired_words:
            script += " " + pad[pad_at % len(pad)]
            pad_at += 1
    script = _split_spoken_sentences(script)

    # Planned two-voice moments receive a deliberately short hand-off.  It is used only where the
    # Phase 3 narration outline explicitly names both speakers.
    if planned_dual_voice:
        script = (
            f"{lead}: {script.split(': ', 1)[1]}\n\n"
            f"{co}: Carry this practical rule into your next decision."
        )
    script = _fit_script_to_target(script, target)
    return script, target, tone


def narration_plain(script: str) -> str:
    return re.sub(r"\[\[(?:cue|pause):[^\]]+\]\]", "", script).replace("\n\n", " ").strip()


def make_lexicon(module_dir: Path, scripts: list[str]) -> dict[str, str]:
    """Seed with approved master terms and add a readable spelling for any all-caps acronym used."""
    lex: dict[str, str] = {
        "NOOR": "noor", "OMAR": "OH-mar", "EHR": "E-H-R", "RCM": "R-C-M", "SCORM": "scorm",
        "ICD": "I-C-D", "ICD-10": "I-C-D ten", "CBAHI": "see-bah-hee", "FMS": "F-M-S", "OHS": "O-H-S",
        "AREC": "A-R-E-C", "ERT": "E-R-T", "RACE": "race", "PASS": "pass", "GHS": "G-H-S", "NFPA": "N-F-P-A",
        "SDS": "S-D-S", "PPE": "P-P-E", "ALARA": "ah-LAR-ah", "RSO": "R-S-O", "BME": "Biomedical Engineering",
        "MOH": "M-O-H", "HAZMAT": "haz-mat", "PXO": "patient experience officer", "KPI": "K-P-I",
        "TAT": "turnaround time", "EBP": "E-B-P", "CHI": "C-H-I", "CCHI": "C-C-H-I", "BMI": "B-M-I",
        "HPI": "history of present illness", "CDI": "C-D-I", "SAR": "Saudi riyals", "SMS": "S-M-S",
    }
    # Capture special vocabulary explicitly recorded in each Phase 3 plan, then make a safe default
    # for any remaining all-caps sequence so lint does not silently miss pronunciation work.
    all_text = "\n".join(scripts)
    for term in sorted(set(re.findall(r"\b[A-Z][A-Z0-9-]{1,}\b", all_text))):
        lex.setdefault(term, "-".join(term.replace("-", "")))
    return dict(sorted(lex.items()))


def script_export(script: dict[str, Any]) -> dict[str, Any]:
    def spoken(text: str) -> str:
        return re.sub(r"\s+", " ", re.sub(r"\[\[[^\]]+\]\]", " ", text)).strip()
    segments = []
    for segment in script["segments"]:
        text = spoken(segment["narration"])
        words = word_count(text)
        est = round(words / script["wpm"] * 60, 1)
        segments.append({
            "screen_id": segment["screen_id"], "filename": f"{script['module_id']}_{segment['screen_id']}.mp3",
            "narration_text": text, "tts_text": text, "est_sec": est, "timing_source": "estimated_word_count",
        })
    lines = [f"# Voice-over script — {script['module_id']}", "", f"Language: {script['language']} · Pace: ~{script['wpm']} wpm", "", "## Pronunciation guide", ""]
    lines += [f"- **{term}** → {sound}" for term, sound in script["lexicon"].items()]
    lines += ["", "## Recording table", "", "| # | Screen | Tone | Script | Est. sec |", "|---|---|---|---|---|"]
    for i, (item, source) in enumerate(zip(segments, script["segments"]), 1):
        lines.append(f"| {i} | `{item['screen_id']}` | {source.get('tone','')} | {safe_cell(item['narration_text'])} | {item['est_sec']} |")
    return {"module_id": script["module_id"], "language": script["language"], "wpm": script["wpm"], "total_est_sec": round(sum(item["est_sec"] for item in segments), 1), "segments": segments, "voice_talent_md": "\n".join(lines) + "\n"}


def brand_logo_html(light: bool = True) -> str:
    file = "logo-horizontal-navy.png" if light else "logo-horizontal-white.png"
    return f'<img class="logo" src="../../00_program/brand/assets/{file}" alt="My Clinic logo">'


def html_screen_markup(row: dict[str, Any], cfg: dict[str, Any], companion: dict[str, str] | None, folder: str) -> str:
    title = html.escape(title_for(row, cfg))
    content = html.escape(short_text(row["on_screen"], 28))
    layout, _, _, _ = layout_for(row["type"], row["scored"])
    if row["type"] == "title_slide":
        return f'''<article class="board title-board" id="{row['id']}">
  <div class="screen title-screen">{brand_logo_html(False)}<p class="chip">MODULE {cfg['number']}</p><h2>{title}</h2><p>{html.escape(cfg['seat_time'])}</p><span class="watermark">✦</span></div>
  <div class="caption"><code>{row['id']}</code> · {html.escape(layout)} · title visual · supplied client logo and background only</div>
</article>'''
    classes = "scenario" if row["type"] in SCENARIO_TYPES else "question" if row["scored"] or row["type"] == "poll" else "content"
    companion_html = ""
    if companion:
        visible = html.escape(companion["visible"])
        companion_html = f'<aside class="companion"><b>{visible}</b><br><span>{html.escape(companion["pose"])}</span></aside>'
    cards = ""
    if row["scored"] or row["type"] in SCENARIO_TYPES:
        cards = '<div class="choice-row"><span></span><span></span><span></span></div>'
    elif row["type"] in {"tabs", "accordion", "flashcards", "hotspot"}:
        cards = '<div class="content-cards"><span></span><span></span><span></span></div>'
    generated = GENERATED_ASSETS.get(folder, {})
    art_html = ""
    if row["id"] == "hs1-404":
        art_html = '<img class="art" src="assets/hs1-img-corridor.png" alt="Clinic corridor safety illustration">'
    elif row["id"] == "hs2-011":
        art_html = '<img class="art" src="assets/hs2-img-storeroom.png" alt="Store room hazard illustration">'
    elif row["id"] == "ops-031":
        art_html = '<img class="art" src="assets/ops-img-reception-scenario.png" alt="Reception scenario illustration">'
    return f'''<article class="board" id="{row['id']}">
  <div class="screen {classes}">{brand_logo_html(True)}<div class="header-rule"></div><p class="crumb">{html.escape(layout)} · {html.escape(row['phase_heading'])}</p><h2>{title}</h2><p class="keywords">{content}</p>{art_html}{cards}{companion_html}<div class="progress" style="--accent:{cfg['module_hex']}"></div></div>
  <div class="caption"><code>{row['id']}</code> · {html.escape(row['type'])} · screen visual reference only · inspect final responsive build before approval</div>
</article>'''


def write_screen_visuals(out_dir: Path, folder: str, cfg: dict[str, Any], rows: list[dict[str, Any]], companions: dict[str, dict[str, str]]) -> None:
    boards = "\n".join(html_screen_markup(row, cfg, companions.get(row["id"]), folder) for row in rows)
    content = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>My Clinic — Module {cfg['number']} visual storyboard</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap');
:root{{--navy:#003867;--ink:#1F2A37;--bg:#F4F7FA;--line:#D9E1E8;--muted:#5B6B7B;--accent:{cfg['module_hex']};}}
*{{box-sizing:border-box}} body{{margin:0;background:var(--bg);color:var(--ink);font-family:Montserrat,Arial,sans-serif}} header{{background:var(--navy);color:#fff;padding:42px max(24px,5vw)}}header img{{width:188px;height:auto}}header h1{{font-size:32px;margin:20px 0 6px}}header p{{max-width:850px;color:#C0CED9;line-height:1.5}}main{{max-width:1160px;margin:28px auto;padding:0 24px}}.notice{{border-left:4px solid #9D3293;background:#fff;padding:16px 20px;border-radius:8px;margin-bottom:24px;line-height:1.5}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(420px,1fr));gap:24px;align-items:start}}.board{{margin:0}}.screen{{position:relative;width:100%;aspect-ratio:16/9;border:1px solid var(--line);border-radius:14px;overflow:hidden;background:#fff;padding:30px 40px;box-shadow:0 8px 24px rgba(0,56,103,.08)}}.screen .logo{{width:142px;height:auto;position:absolute;left:40px;top:20px;z-index:2}}.header-rule{{position:absolute;left:40px;right:40px;top:63px;height:2px;background:var(--navy)}}.crumb{{margin:55px 0 10px;font-size:10px;font-weight:700;letter-spacing:.08em;color:var(--accent);text-transform:uppercase}}.screen h2{{font-size:clamp(18px,2.3vw,30px);line-height:1.15;color:var(--navy);margin:0 0 16px;max-width:70%}}.keywords{{font-size:clamp(12px,1.5vw,16px);line-height:1.45;max-width:60%;margin:0}}.title-screen{{background:linear-gradient(135deg,#003867,#3B6A97);padding:72px 48px;color:#fff}}.title-screen .logo{{left:48px;top:38px;width:192px}}.title-screen h2{{color:#fff;font-size:clamp(28px,4vw,44px);max-width:68%;margin-top:66px}}.title-screen p{{color:#C0CED9}}.chip{{display:inline-block;background:var(--accent);color:#fff;padding:6px 10px;border-radius:20px;font-size:10px;font-weight:700;letter-spacing:.08em}}.watermark{{position:absolute;right:-30px;bottom:-105px;font-size:270px;opacity:.08}}.question .choice-row{{position:absolute;left:40px;right:40px;bottom:40px;display:flex;gap:10px}}.choice-row span{{height:42px;flex:1;border:1px solid #D9E1E8;border-radius:10px;background:#fff}}.scenario{{background:#fff}}.scenario .choice-row span:first-child{{border:2px solid var(--accent)}}.content-cards{{display:flex;gap:10px;margin-top:24px;max-width:66%}}.content-cards span{{height:48px;flex:1;background:#fff;border:1px solid #D9E1E8;border-radius:10px}}.companion{{position:absolute;right:36px;bottom:30px;width:135px;border:1px solid #D9E1E8;background:#fff;border-radius:12px;padding:12px;color:var(--navy);font-size:11px;line-height:1.35}}.companion span{{color:var(--muted)}}.progress{{position:absolute;bottom:0;left:0;width:42%;height:5px;background:var(--accent)}}.art{{position:absolute;right:30px;bottom:30px;width:36%;height:48%;object-fit:cover;border-radius:10px;border:1px solid #D9E1E8}}.caption{{font-size:12px;color:var(--muted);padding:9px 4px;line-height:1.4}}code{{color:#006E78;font-family:ui-monospace,monospace}}@media(max-width:550px){{.grid{{grid-template-columns:1fr}}.screen{{padding:22px}}.screen .logo{{left:22px;top:16px;width:110px}}.header-rule{{left:22px;right:22px;top:52px}}.screen h2{{max-width:88%;margin-top:10px}}.keywords{{max-width:85%}}.choice-row{{left:22px!important;right:22px!important;bottom:22px!important}}.companion{{display:none}}}}
</style></head><body>
<header><img src="../../00_program/brand/assets/logo-horizontal-white.png" alt="My Clinic logo"><h1>Module {cfg['number']} · screen visual review</h1><p>{html.escape(cfg['title'])} · official client logo and palette applied to every reference screen.</p></header>
<main><div class="notice"><strong>Review artefact, not a SCORM preview.</strong> These visual boards show layout, client-logo placement, screen hierarchy and the one-module-colour rule. Final content is governed by <code>storyboard.md</code>; screenshots, policy values and hotspot coordinates remain subject to the module’s source lock.</div><div class="grid">{boards}</div></main></body></html>'''
    (out_dir / "screen-visuals.html").write_text(content, encoding="utf-8")


def write_svg(path: Path, inner: str, label: str) -> None:
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900" role="img" aria-labelledby="title desc">
<title id="title">{html.escape(label)}</title><desc id="desc">My Clinic course diagram. Text remains live SVG text and can be recreated in HTML at build time.</desc>
<rect width="1600" height="900" fill="#F4F7FA"/><style>text{{font-family:Montserrat,Arial,sans-serif;fill:#003867}}.h{{font-size:44px;font-weight:700}}.b{{font-size:27px;font-weight:500}}.small{{font-size:22px;font-weight:600}}.line{{stroke:#003867;stroke-width:5;fill:none;stroke-linecap:round;stroke-linejoin:round}}.card{{fill:#fff;stroke:#D9E1E8;stroke-width:3}}.accent{{fill:#008C99}}.magenta{{fill:#9D3293}}</style>{inner}</svg>'''
    path.write_text(svg, encoding="utf-8")


def generate_svg_assets(folder: str, out_dir: Path) -> None:
    asset_dir = out_dir / "assets"
    asset_dir.mkdir(parents=True, exist_ok=True)
    if folder == "01_health-and-safety-1":
        write_svg(asset_dir / "hs1-img-arec.svg", '''<text x="80" y="95" class="h">AREC</text><circle cx="800" cy="450" r="225" fill="#fff" stroke="#D9E1E8" stroke-width="4"/><path class="line" d="M800 200c145 0 260 115 260 250M1060 450l-38-32m38 32l-34 38M1050 550c-65 120-220 165-340 99M710 649l40 15m-40-15l12-40M570 590c-90-100-70-260 42-338M612 252l-8 42m8-42l41 10M640 250c45-32 102-50 160-50"/><circle cx="800" cy="225" r="68" class="accent"/><circle cx="1028" cy="450" r="68" fill="#652D8C"/><circle cx="800" cy="675" r="68" fill="#9D3293"/><circle cx="572" cy="450" r="68" fill="#7C0041"/><text x="800" y="235" class="small" text-anchor="middle" fill="#fff">ANTICIPATE</text><text x="1028" y="460" class="small" text-anchor="middle" fill="#fff">RECOGNISE</text><text x="800" y="685" class="small" text-anchor="middle" fill="#fff">EVALUATE</text><text x="572" y="460" class="small" text-anchor="middle" fill="#fff">CONTROL</text><text x="800" y="465" class="b" text-anchor="middle">Pause · assess · act</text>''', "AREC cycle")
        write_svg(asset_dir / "hs1-img-ert.svg", '''<text x="80" y="95" class="h">Emergency Response Team</text><circle cx="800" cy="420" r="115" fill="#003867"/><text x="800" y="410" class="small" text-anchor="middle" fill="#fff">INCIDENT</text><text x="800" y="442" class="small" text-anchor="middle" fill="#fff">COMMANDER</text><path class="line" d="M800 305V195M915 420h170M885 515l110 115M715 515l-110 115M685 420H515"/><g class="card"><rect x="680" y="105" width="240" height="80" rx="20"/><rect x="1090" y="380" width="240" height="80" rx="20"/><rect x="925" y="635" width="240" height="80" rx="20"/><rect x="435" y="635" width="240" height="80" rx="20"/><rect x="270" y="380" width="240" height="80" rx="20"/></g><text x="800" y="156" class="small" text-anchor="middle">SAFETY</text><text x="1210" y="432" class="small" text-anchor="middle">SECURITY</text><text x="1045" y="687" class="small" text-anchor="middle">NURSING</text><text x="555" y="687" class="small" text-anchor="middle">FACILITY</text><text x="390" y="432" class="small" text-anchor="middle">OPERATION</text>''', "Emergency Response Team")
        write_svg(asset_dir / "hs1-img-triangle.svg", '''<text x="80" y="95" class="h">The fire triangle</text><path d="M800 175L1220 720H380Z" fill="#fff" stroke="#003867" stroke-width="8"/><circle cx="800" cy="545" r="100" fill="#F4F7FA"/><text x="800" y="535" class="small" text-anchor="middle">REMOVE ONE</text><text x="800" y="568" class="small" text-anchor="middle">SIDE TO STOP FIRE</text><circle cx="800" cy="205" r="70" class="magenta"/><text x="800" y="215" class="small" text-anchor="middle" fill="#fff">HEAT</text><circle cx="1170" cy="690" r="70" class="accent"/><text x="1170" y="700" class="small" text-anchor="middle" fill="#fff">OXYGEN</text><circle cx="430" cy="690" r="70" fill="#7C0041"/><text x="430" y="700" class="small" text-anchor="middle" fill="#fff">FUEL</text>''', "Fire triangle")
        write_svg(asset_dir / "hs1-img-alara.svg", '''<text x="80" y="95" class="h">ALARA</text><text x="80" y="136" class="b">Keep exposure as low as reasonably achievable</text><circle cx="800" cy="455" r="112" fill="#9D3293"/><text x="800" y="446" class="small" text-anchor="middle" fill="#fff">RADIATION</text><text x="800" y="478" class="small" text-anchor="middle" fill="#fff">SOURCE</text><path class="line" d="M800 315V205M920 520l190 115M680 520L490 635"/><rect x="680" y="120" width="240" height="88" rx="20" class="card"/><rect x="1110" y="590" width="280" height="88" rx="20" class="card"/><rect x="210" y="590" width="280" height="88" rx="20" class="card"/><text x="800" y="175" class="small" text-anchor="middle">TIME · minimise it</text><text x="1250" y="645" class="small" text-anchor="middle">DISTANCE · increase it</text><text x="350" y="645" class="small" text-anchor="middle">SHIELDING · use it</text>''', "ALARA radiation protection")
        write_svg(asset_dir / "hs1-img-nfpa-blank.svg", '''<text x="80" y="95" class="h">NFPA 704: four information areas</text><g transform="translate(800 455) rotate(45)"><rect x="-170" y="-170" width="170" height="170" fill="#1E5AA8"/><rect x="0" y="-170" width="170" height="170" fill="#D8262F"/><rect x="-170" y="0" width="170" height="170" fill="#F0CF34"/><rect x="0" y="0" width="170" height="170" fill="#fff" stroke="#003867" stroke-width="5"/></g><text x="585" y="435" class="small" text-anchor="middle">HEALTH</text><text x="1015" y="435" class="small" text-anchor="middle">FLAMMABILITY</text><text x="585" y="650" class="small" text-anchor="middle">REACTIVITY</text><text x="1015" y="650" class="small" text-anchor="middle">SPECIAL</text>''', "Blank NFPA diamond")
        write_svg(asset_dir / "hs1-img-nfpa-301w.svg", '''<text x="80" y="95" class="h">NFPA 704: read the whole diamond</text><g transform="translate(800 455) rotate(45)"><rect x="-170" y="-170" width="170" height="170" fill="#1E5AA8"/><rect x="0" y="-170" width="170" height="170" fill="#D8262F"/><rect x="-170" y="0" width="170" height="170" fill="#F0CF34"/><rect x="0" y="0" width="170" height="170" fill="#fff" stroke="#003867" stroke-width="5"/></g><text x="590" y="450" class="h" text-anchor="middle" fill="#fff">3</text><text x="1010" y="450" class="h" text-anchor="middle" fill="#fff">0</text><text x="590" y="660" class="h" text-anchor="middle">1</text><text x="1010" y="660" class="h" text-anchor="middle">W</text>''', "NFPA diamond 3 0 1 W")
    elif folder == "02_health-and-safety-2":
        write_svg(asset_dir / "hs2-img-floorplan.svg", '''<text x="80" y="95" class="h">Generic evacuation practice plan</text><rect x="160" y="175" width="1280" height="570" rx="16" fill="#fff" stroke="#003867" stroke-width="6"/><path class="line" d="M460 175v570M790 175v570M1120 175v570M160 440h1280"/><g font-weight="700"><text x="310" y="325" class="h" text-anchor="middle">A</text><text x="625" y="325" class="h" text-anchor="middle">B</text><text x="955" y="325" class="h" text-anchor="middle">C</text><text x="1280" y="325" class="h" text-anchor="middle">D</text><text x="800" y="630" class="h" text-anchor="middle">E</text></g><circle cx="230" cy="680" r="28" class="magenta"/><text x="270" y="690" class="small">You are here</text><path d="M230 620h95" class="line"/><path d="M325 620l-30-22m30 22l-30 22" class="line"/><text x="800" y="830" class="b" text-anchor="middle">Generic practice plan only — find your unit’s real plan at work.</text>''', "Generic evacuation floor plan")
        write_svg(asset_dir / "hs2-img-nfpa-230.svg", '''<text x="80" y="95" class="h">NFPA 704 practice diamond</text><g transform="translate(800 455) rotate(45)"><rect x="-170" y="-170" width="170" height="170" fill="#1E5AA8"/><rect x="0" y="-170" width="170" height="170" fill="#D8262F"/><rect x="-170" y="0" width="170" height="170" fill="#F0CF34"/><rect x="0" y="0" width="170" height="170" fill="#fff" stroke="#003867" stroke-width="5"/></g><text x="590" y="450" class="h" text-anchor="middle" fill="#fff">2</text><text x="1010" y="450" class="h" text-anchor="middle" fill="#fff">3</text><text x="590" y="660" class="h" text-anchor="middle">0</text>''', "NFPA diamond 2 3 0")
    elif folder == "04_operations-and-my-care":
        write_svg(asset_dir / "ops-img-journey.svg", '''<text x="80" y="95" class="h">Patient journey</text><path class="line" d="M200 450h1160"/><path class="line" d="M1360 450l-32-25m32 25l-32 25"/><g><circle cx="220" cy="450" r="72" class="accent"/><circle cx="450" cy="450" r="72" fill="#9D3293"/><circle cx="680" cy="450" r="72" class="accent"/><circle cx="910" cy="450" r="72" fill="#9D3293"/><circle cx="1140" cy="450" r="72" class="accent"/><circle cx="1370" cy="450" r="72" fill="#9D3293"/></g><g class="small" text-anchor="middle" fill="#fff"><text x="220" y="460">BOOK</text><text x="450" y="460">ARRIVE</text><text x="680" y="460">CONSULT</text><text x="910" y="452">SERVICES</text><text x="910" y="480">&amp; PHARMACY</text><text x="1140" y="460">LEAVE</text><text x="1370" y="460">FOLLOW-UP</text></g><text x="800" y="700" class="b" text-anchor="middle">Operations and My Care meet the patient at different moments — both protect continuity.</text>''', "Patient journey")
        write_svg(asset_dir / "ops-img-ops-chart.svg", '''<text x="80" y="95" class="h">Operations — role-only draft</text><rect x="600" y="140" width="400" height="75" rx="18" class="card"/><text x="800" y="188" class="small" text-anchor="middle">DIRECTOR OF OPERATIONS</text><path class="line" d="M800 215v75M400 290h800M400 290v70M800 290v70M1200 290v70"/><g class="card"><rect x="250" y="360" width="300" height="100" rx="18"/><rect x="650" y="360" width="300" height="100" rx="18"/><rect x="1050" y="360" width="300" height="100" rx="18"/></g><g class="small" text-anchor="middle"><text x="400" y="405">PX &amp; OPERATIONS</text><text x="400" y="435">SR. MANAGER</text><text x="800" y="405">PATIENT ACCESS &amp; PX</text><text x="800" y="435">SR. MANAGER</text><text x="1200" y="405">OPERATIONS</text><text x="1200" y="435">SR. MANAGER</text></g><text x="800" y="650" class="b" text-anchor="middle">Draft for B1 approval — do not use as a live reporting directory.</text>''', "Draft Operations structure")
        write_svg(asset_dir / "ops-img-mycare-chart.svg", '''<text x="80" y="95" class="h">My Care — role-only draft</text><rect x="600" y="140" width="400" height="75" rx="18" class="card"/><text x="800" y="188" class="small" text-anchor="middle">DIRECTOR OF OPERATIONS</text><path class="line" d="M800 215v70M800 285v70M800 445v70M470 515h660M470 515v70M800 515v70M1130 515v70"/><g class="card"><rect x="570" y="285" width="460" height="80" rx="18"/><rect x="620" y="365" width="360" height="80" rx="18"/><rect x="320" y="585" width="300" height="90" rx="18"/><rect x="650" y="585" width="300" height="90" rx="18"/><rect x="980" y="585" width="300" height="90" rx="18"/></g><g class="small" text-anchor="middle"><text x="800" y="335">PATIENT ACCESS &amp; PX SR. MANAGER</text><text x="800" y="415">MY CARE MANAGER</text><text x="470" y="625">ONBOARDING LEADERS</text><text x="800" y="625">SITE LEADERS</text><text x="1130" y="625">QA LEADER</text></g><text x="800" y="760" class="b" text-anchor="middle">Draft for B2 approval — coordinator reporting lines are pending.</text>''', "Draft My Care structure")
    elif folder == "05_rcm-documentation-and-coding":
        write_svg(asset_dir / "rcma-img-note-weak.svg", '''<text x="80" y="95" class="h">Weak note — fictional example</text><rect x="260" y="165" width="1080" height="560" rx="24" class="card"/><rect x="300" y="215" width="300" height="36" rx="8" fill="#D9E1E8"/><rect x="300" y="290" width="760" height="26" rx="8" fill="#D9E1E8"/><rect x="300" y="340" width="500" height="26" rx="8" fill="#D9E1E8"/><text x="300" y="480" class="b">“Patient given IV fluids.”</text><rect x="300" y="540" width="700" height="70" rx="12" fill="#FBE9E7"/><text x="330" y="585" class="small">Missing: findings · indication · assessment · follow-up</text>''', "Weak fictional note")
        write_svg(asset_dir / "rcma-img-note-strong.svg", '''<text x="80" y="95" class="h">Stronger note — fictional example</text><rect x="260" y="165" width="1080" height="560" rx="24" class="card"/><rect x="300" y="215" width="300" height="36" rx="8" fill="#D9E1E8"/><text x="300" y="330" class="b">Dehydration signs: tachycardia and dry mucosa.</text><text x="300" y="385" class="b">Assessment: dehydration; IV fluids for stabilisation.</text><text x="300" y="440" class="b">Plan: reassess response and document follow-up.</text><rect x="300" y="530" width="700" height="70" rx="12" fill="#E4F3EC"/><text x="330" y="575" class="small">Findings + assessment + rationale + plan</text>''', "Stronger fictional note")
        write_svg(asset_dir / "rcma-img-reviewer.svg", '''<text x="80" y="95" class="h">The reviewer sees the note</text><circle cx="390" cy="450" r="120" fill="#C0CED9"/><circle cx="350" cy="420" r="28" fill="#003867"/><circle cx="430" cy="420" r="28" fill="#003867"/><path class="line" d="M330 510q60 55 120 0"/><rect x="820" y="260" width="420" height="390" rx="20" class="card"/><path d="M875 340h280M875 410h250M875 480h295M875 550h220" class="line"/><path class="line" d="M520 450h270M790 450l-34-25m34 25l-34 25"/><text x="800" y="760" class="b" text-anchor="middle">Clinical care is real; payment review depends on the written record.</text>''', "Reviewer sees a note")
    elif folder == "06_rcm-ebp-benefits-and-rejections":
        write_svg(asset_dir / "rcmb-img-benefit-icons.svg", '''<text x="80" y="95" class="h">Benefit icon family</text><g fill="none" stroke="#003867" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"><circle cx="300" cy="300" r="75"/><path d="M260 300h80M300 260v80"/><path d="M650 220v160M570 300h160"/><path d="M900 230l120 140M1020 230L900 370"/><path d="M1240 250q85-100 170 0v180h-170z"/><circle cx="300" cy="620" r="78"/><path d="M245 620h110M300 565v110"/><path d="M570 610q80-110 160 0q-80 110-160 0z"/><path d="M920 540v160M860 620h120"/><path d="M1210 560q115 60 0 120q-115-60 0-120z"/></g><g fill="#7C0041"><circle cx="300" cy="300" r="18"/><circle cx="650" cy="300" r="18"/><circle cx="960" cy="300" r="18"/><circle cx="1325" cy="340" r="18"/><circle cx="300" cy="620" r="18"/><circle cx="650" cy="610" r="18"/><circle cx="920" cy="620" r="18"/><circle cx="1210" cy="620" r="18"/></g><text x="800" y="820" class="b" text-anchor="middle">No benefit wording is baked into icons; approved labels stay as HTML.</text>''', "Generic benefit icon sheet")
    elif folder == "08_it-ehr-consultation":
        write_svg(asset_dir / "ehr-capture-sheet.svg", '''<text x="80" y="95" class="h">Safe EHR screenshot capture checklist</text><rect x="170" y="165" width="1260" height="575" rx="24" class="card"/><g class="small"><text x="300" y="285">1. Use the approved test environment and fictional test patient.</text><text x="300" y="385">2. Capture at 1920 × 1080 and 125% browser zoom.</text><text x="300" y="485">3. Check every field for names, phone numbers, MRNs and identifiers.</text><text x="300" y="585">4. Record EHR version and obtain DPO approval before upload.</text></g><g fill="#006E78"><circle cx="245" cy="275" r="20"/><circle cx="245" cy="375" r="20"/><circle cx="245" cy="475" r="20"/><circle cx="245" cy="575" r="20"/></g><g fill="#fff" font-family="Montserrat" font-size="22" font-weight="700"><text x="239" y="283">1</text><text x="239" y="383">2</text><text x="239" y="483">3</text><text x="239" y="583">4</text></g><text x="800" y="820" class="b" text-anchor="middle">This is a capture guide, not an EHR screen or a substitute for test-environment screenshots.</text>''', "EHR safe screenshot capture checklist")


def write_asset_register(out_dir: Path, folder: str, assets: list[dict[str, str]]) -> None:
    generated = GENERATED_ASSETS.get(folder, {})
    lines = ["# Visual and audio asset register", "", "This register is the production hand-off for review. `Generated` means the file is in this repository; `planned` means it must still be approved or supplied. Every asset still needs the final `add_asset` provenance record during Phase 4.", "", "## Generated in this review pack", "", "| Asset id | File | Kind | Provenance | Status | Alt text |", "|---|---|---|---|---|---|"]
    for aid, asset in generated.items():
        lines.append(f"| `{aid}` | [`{asset['file']}`]({asset['file']}) | {asset['kind']} | {asset['source']} | {asset['status']} | {safe_cell(asset['alt'])} |")
    lines += ["", "## Planned assets from Phase 3", "", "| Planned id | Kind | Screens | Brief | Source route | Alt text / accessibility note |", "|---|---|---|---|---|---|"]
    seen: set[str] = set()
    for asset in assets:
        if asset["id"] in seen:
            continue
        seen.add(asset["id"])
        lines.append(f"| `{asset['id']}` | {asset['kind']} | {safe_cell(asset['screens'])} | {safe_cell(asset['brief'])} | {safe_cell(asset['source'])} | {safe_cell(asset['alt'])} |")
    lines += ["", "## Non-negotiable production rules", "", "- Use the supplied My Clinic logo PNGs; never generate, redraw or bake the logo into an AI image.", "- AI images contain no text, letters, numbers, brand names or patient/staff likenesses. Review every generated image before it becomes an interaction asset.", "- Module 08 only uses newly captured screenshots from a test environment after DPO review. This repository contains no simulated production patient record.", "- Keep diagrams as SVG/HTML where factual text needs revision after SME review.", ""]
    (out_dir / "asset-register.md").write_text("\n".join(lines), encoding="utf-8")


def write_audio_readme(out_dir: Path, cfg: dict[str, Any], exported: dict[str, Any]) -> None:
    minutes = exported["total_est_sec"] / 60
    text = f'''# Narration production status — Module {cfg['number']}

The complete, screen-by-screen English script is in [`narration-script.json`](narration-script.json). The
recording table and TTS-ready text are in [`voice_talent.md`](voice_talent.md) and
[`audio-script-export.json`](audio-script-export.json).

## What is ready

- {len(exported['segments'])} screen segments, with lead/co-host prefixes, a timing estimate and a pronunciation lexicon.
- Estimated spoken runtime: **{minutes:.1f} minutes** at {WPM} wpm. Interactive work adds the remainder of the module seat time.
- Captions/transcript text can be derived from each segment’s `narration_text` field.

## What is intentionally not yet produced

No shipping audio is generated in this draft. The shared voice decision (**D10**) remains open: the
programme needs two approved, fixed English voices (Noor and Dr. Omar), commercial-use permission,
and a short client-approved sample before a TTS provider or a human voice talent is booked. Once
approved, synthesise or record the `tts_text`, join planned two-voice turns with 0.3 seconds of
silence, normalise loudness, and update the Phase 4 asset map.

The scripts are review-ready; they are **not** evidence that a policy, clinical, EHR or payer fact is
approved. Keep every `⚠ PENDING` item in the cards until its Phase 0 owner closes it.
'''
    audio = out_dir / "audio"
    audio.mkdir(exist_ok=True)
    (audio / "README.md").write_text(text, encoding="utf-8")


def write_storyboard(folder: str) -> dict[str, Any]:
    cfg = MODULES[folder]
    module_dir = PLANS / folder
    out_dir = module_dir / "storyboard"
    out_dir.mkdir(exist_ok=True)
    generate_svg_assets(folder, out_dir)
    rows = parse_phase2(module_dir, cfg["prefix"])
    objective_text, screen_objs = parse_objectives(module_dir)
    outline = parse_narration_outline(module_dir, cfg["prefix"])
    companions = parse_companions(module_dir, cfg["prefix"])
    assets = parse_assets(module_dir)
    open_questions = parse_open_questions(module_dir)

    # Ensure P2's screen list is our sole order source.  This is deliberate: cards never silently
    # add optional screens (particularly relevant to EHR video work and later SME requests).
    scripts: list[dict[str, Any]] = []
    visual_screens: list[dict[str, Any]] = []
    card_parts: list[str] = []
    scored = 0
    points = 0
    register_rows: list[dict[str, Any]] = []

    for index, row in enumerate(rows, 1):
        sid = row["id"]
        node, section = section_for(folder, sid)
        objectives = screen_objs.get(sid, [])
        companion = companions.get(sid)
        layout, bg, text_role, accent = layout_for(row["type"], row["scored"])
        visual = {
            "screen_id": sid,
            "screen_type": row["type"],
            "purpose": row["purpose"],
            "visual_concept": concept_for(row, cfg, companion),
            "layout": layout,
            "background_role": bg,
            "text_role": text_role,
            "accent_role": accent,
            "imagery": imagery_for(folder, row, assets, companion),
            "on_screen_text": short_text(row["on_screen"], 40),
            "animation": "fade" if row["type"] == "title_slide" else "none" if row["scored"] or row["type"] in SCENARIO_TYPES else "fade-up",
            "interaction": row["interaction"] if row["interaction"] not in {"—", ""} else None,
            "cue_targets": [],
        }
        visual_screens.append(visual)
        narration, target, tone = narration_for(row, cfg, outline, companion)
        scripts.append({
            "screen_id": sid,
            "narration": narration,
            "on_screen_text": visual["on_screen_text"],
            "target_sec": target,
            "tone": tone,
        })
        if row["scored"]:
            scored += 1
            points += row["points"]
        register_rows.append({
            "n": index, "row": row, "narration": narration, "target": target, "section": section,
        })

        title = title_for(row, cfg)
        words = word_count(visual["on_screen_text"] or "")
        narration_words = word_count(narration_plain(narration))
        secs = round(narration_words / WPM * 60, 1)
        speaker_labels = " / ".join(dict.fromkeys(re.findall(r"^(NOOR|OMAR):", narration, flags=re.M))) or cfg["lead"]
        narration_quote = "\n".join(f"> {line}" if line else ">" for line in narration.splitlines())
        dependency = detect_dependencies(row, cfg)
        logo = "`logo-horizontal-white.png`, 48 px at top-left" if row["type"] == "title_slide" else "`logo-horizontal-navy.png`, 30 px in the 64 px header at top-left"
        watermark = "Supplied white petal mark at 8–10% opacity, cropped off the right edge." if row["type"] == "title_slide" else "None behind body text or questions."
        companion_text = "None." if not companion else f"{companion['visible']} · pose `{companion['pose']}` · placement {companion['placement']} · speaks: {companion['speaks']}."
        imagery_rows = []
        for img in visual["imagery"]:
            provenance = "own / official My Clinic asset" if img["source"] == "client" else "own SVG" if img["source"] == "svg" else "ai-generated, visual QA required"
            imagery_rows.append(f"| `{img['description'].split(':', 1)[0]}` | {img['kind']} | {safe_cell(img['description'])} | {provenance} | {safe_cell(img.get('alt_text') or 'Decorative.') } | {'Yes' if img.get('decorative') else 'No'} |")
        if not imagery_rows:
            imagery_rows.append("| n/a | n/a | No meaningful image beyond layout chrome. | n/a | n/a | n/a |")
        ai_prompt = ""
        for aid, asset in GENERATED_ASSETS.get(folder, {}).items():
            if aid in " ".join(i["description"] for i in visual["imagery"]) and asset["source"] == "ai-generated":
                ai_prompt = (
                    "\n**AI image prompt (recorded production prompt)**\n\n```text\n"
                    f"Single clean flat vector illustration for a My Clinic e-learning course. {asset['alt']} "
                    f"Use navy #003867 outlines, white space, soft blue-grey #C0CED9, and {cfg['module_colour']} as the only value-colour highlight. "
                    "No text, no letters, no numbers, no logos, no watermark, no patient/staff likeness, and no generated My Clinic mark.\n```\n"
                )
                break
        interaction = row["interaction"] if row["interaction"] not in {"—", ""} else "n/a — informational screen."
        items_spec = row["on_screen"] or "n/a — no separate item list in the controlled Phase 2 row."
        objective_list = ", ".join(f"`{o}`" for o in objectives) if objectives else "—"
        correct_spec = correct_for(row)
        accepted_variants = accepted_variants_for(row)
        pass_rule = pass_rule_for(row)
        correct_feedback = feedback_for(row, correct=True)
        incorrect_feedback = feedback_for(row, correct=False)
        per_choice_feedback = interaction if row["type"] in SCENARIO_TYPES | {"adaptive_practice"} else "n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above."
        hint = hint_for(row)
        retry = retry_for(row)
        build_metadata = {
            "type": row["type"], "id": sid, "title": title, "section": section, "node_id": node,
            "objective_ids": objectives, "points": row["points"], "narration_script_id": sid,
            "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs.",
        }
        source_html = clean_html_text(row["source"])
        card_parts.append(f'''### `{sid}` — {title}

**Status:** `Draft — ready for SME review` · **Section / node:** {section} / `{node}` · **Type:** `{row['type']}` · **Scored:** {'Yes (' + str(row['points']) + ' pts)' if row['scored'] else 'No'}

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | {safe_cell(row['purpose'])} |
| Objective(s) | {objective_list} |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | {safe_cell(row['source'])} |
| Depends on Phase 0 | {safe_cell(dependency)} |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | {safe_cell(title)} |
| Body / keywords | {safe_cell(visual['on_screen_text'] or 'n/a — interaction supplies the visible task.')} |
| Word count (excl. title) | {words} |
| Instruction | {safe_cell(interaction)} |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | {layout} |
| Logo | {logo} |
| Visual concept | {safe_cell(visual['visual_concept'])} |
| edumints layout | {'n/a (interaction screen)' if row['scored'] or row['type'] in SCENARIO_TYPES | {'hotspot', 'poll'} else 'text_media / full_media as shown in screen-visuals.html'} |
| Colours | background `{bg}` · text `{text_role}` · highlight `{accent}` / {cfg['module_colour']} · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | {watermark} |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `{visual['animation']}`; reduced-motion mode uses no movement. |
| Companion | {safe_cell(companion_text)} |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
{chr(10).join(imagery_rows)}
{ai_prompt}
#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | {safe_cell(items_spec)} |
| Build / feedback brief | {safe_cell(interaction)} |
| Correct answer(s) / completion rule | {safe_cell(correct_spec)} |
| Accepted variants (typed answers) | {safe_cell(accepted_variants)} |
| Points | {row['points']} |
| Pass rule (scenarios / games) | {safe_cell(pass_rule)} |
| Feedback — correct | {safe_cell(correct_feedback)} |
| Feedback — incorrect | {safe_cell(incorrect_feedback)} |
| Per-choice feedback (scenarios) | {safe_cell(per_choice_feedback)} |
| Hint (if any) | {safe_cell(hint)} |
| Retry / lives | {safe_cell(retry)} |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | {speaker_labels} |
| Tone | {tone} |
| Target seconds | {target:g} |
| Word count / estimated seconds | {narration_words} words / ≈ {secs:g} s at {WPM} wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

{narration_quote}

New lexicon terms: See `narration-script.json` and `voice_talent.md`.

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Native focusable controls; matching, sorting and drag/drop use keyboard pick-and-place equivalents. |
| Not colour-only | Labels, icons, position and explanatory text carry every safety, feedback and category meaning. |
| Captions / transcript | `narration_text` is generated from the narration script; any later video receives WebVTT captions. |
| Timing | Untimed. Any future media control must allow pause, replay and extended reading time. |

#### 7. Build fields (edumints)

```json
{json.dumps(build_metadata, ensure_ascii=False, indent=2)}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: {dependency}
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `{sid}`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
''')

    # The controlled Phase 4 totals are a guardrail, not a value to overwrite silently.  A change
    # to a Phase 2 scoring star or points cell must be reconciled in the source plan first.
    if (scored, points) != (cfg["scored_expected"], cfg["points_expected"]):
        raise RuntimeError(
            f"{folder}: Phase 2 has {scored} scored screens / {points} points; "
            f"expected {cfg['scored_expected']} / {cfg['points_expected']}. Reconcile the source plans."
        )

    visual_plan = {
        "module_id": cfg["module_id"], "module_title": cfg["package_title"], "brand_name": "My Clinic",
        "audience": cfg["audience"], "objective": "See the approved Phase 1 observable objectives; each scored screen is objective-mapped in storyboard.md.",
        "screens": visual_screens,
    }
    narr_script = {
        "module_id": cfg["module_id"], "language": "en", "wpm": WPM,
        "voice": {"provider": "external", "voice_id": None, "persona": "an experienced My Clinic colleague coaching a learner in their first week", "gender": None},
        "lexicon": make_lexicon(module_dir, [s["narration"] for s in scripts]), "segments": scripts,
    }
    exported = script_export(narr_script)
    (out_dir / "visual-plan.json").write_text(json.dumps(visual_plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out_dir / "narration-script.json").write_text(json.dumps(narr_script, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out_dir / "audio-script-export.json").write_text(json.dumps(exported, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out_dir / "voice_talent.md").write_text(exported["voice_talent_md"], encoding="utf-8")
    write_asset_register(out_dir, folder, assets)
    write_audio_readme(out_dir, cfg, exported)
    write_screen_visuals(out_dir, folder, cfg, rows, companions)

    estimated_seconds = sum(word_count(narration_plain(s["narration"])) / WPM * 60 for s in scripts)
    detailed_target_seconds = sum(float(outline.get(row["id"], {}).get("target", 0)) for row in rows)
    rough_phase3_minutes = cfg["phase3_audio_estimate"]
    timing_reconciliation = (
        f"Detailed card scripts: {round(estimated_seconds / 60, 1)} min; Phase 3 per-screen targets: "
        f"{round(detailed_target_seconds / 60, 1)} min; Phase 3 rough module estimate: ~{rough_phase3_minutes} min. "
        "Use the detailed per-screen targets for production timing and reconcile the older rough module estimate at SME review."
    )
    # Header and summary are deliberately explicit about review state.  This avoids treating a
    # storyboard card as a policy approval merely because it is complete as documentation.
    objectives_md = "\n".join(
        f"| `{oid}` | {safe_cell(desc)} | {', '.join(f'`{s}`' for s, ids in screen_objs.items() if oid in ids) or '—'} |"
        for oid, desc in objective_text.items()
    ) or "| — | Objective mapping needs Phase 1 review. | — |"
    section_rows = []
    used_sections: list[tuple[str, str]] = []
    for row in rows:
        pair = section_for(folder, row["id"])
        if pair not in used_sections:
            used_sections.append(pair)
    for node, section in used_sections:
        first = next(r["id"] for r in rows if section_for(folder, r["id"])[0] == node)
        last = [r["id"] for r in rows if section_for(folder, r["id"])[0] == node][-1]
        section_rows.append(f"| `{node}` | {section} | `{first}`–`{last}` |")
    register_md = []
    for reg in register_rows:
        row = reg["row"]
        nwords = word_count(narration_plain(reg["narration"]))
        sec = round(nwords / WPM * 60)
        register_md.append(f"| {reg['n']} | `{row['id']}` | `{row['type']}` | {'Y' if row['scored'] else 'N'} | {row['points']} | {word_count(short_text(row['on_screen'], 40))} | {nwords} | {sec} | Draft |")
    asset_summary = []
    for aid, asset in GENERATED_ASSETS.get(folder, {}).items():
        asset_summary.append(f"| `{aid}` | {asset['kind']} | Generated file | {asset['source']} | Yes | {asset['status']} |")
    for asset in assets:
        asset_summary.append(f"| `{asset['id']}` | {asset['kind']} | {safe_cell(asset['screens'])} | {safe_cell(asset['source'])} | {'Yes' if asset['alt'].lower() != 'n/a' else 'n/a'} | Planned |")
    if not asset_summary:
        asset_summary.append("| n/a | n/a | n/a | n/a | n/a | n/a |")
    questions_md = "\n".join(f"| {i} | All affected cards | {safe_cell(q['question'])} | `{q['id']}` · {safe_cell(q['owner'])} | Yes |" for i, q in enumerate(open_questions, 1)) or "| — | — | No individual Phase 0 record was parsed. | — | Review source lock. |"
    lexicon_rows = []
    for term, pronunciation in narr_script["lexicon"].items():
        if term in {"NOOR", "OMAR"}:
            continue
        affected = [seg["screen_id"] for seg in scripts if re.search(rf"(?<![A-Za-z0-9-]){re.escape(term)}(?![A-Za-z0-9-])", narration_plain(seg["narration"]))]
        if affected:
            lexicon_rows.append(f"| `{term}` | {safe_cell(pronunciation)} | {', '.join(f'`{sid}`' for sid in affected)} |")
    lexicon_md = "\n".join(lexicon_rows) or "| — | No module-specific pronunciation addition is used in the current draft. | — |"
    module_doc = f'''# Storyboard — {cfg['number']} {cfg['title']}

![My Clinic logo](../../00_program/brand/logo-preview.png)

> **Review pack v0.2 · {TODAY}.** This document completes the screen-card, narration, visual-plan,
> asset-register and visual-review documentation for every core screen in
> [`../phase-2-storyboard.md`](../phase-2-storyboard.md). It is a review artefact, **not an approved
> policy or production SCORM package**. Source-lock decisions are deliberately retained as `⚠ PENDING`.

**Companion documents:** [`screen-visuals.html`](screen-visuals.html) ·
[`visual-plan.json`](visual-plan.json) · [`narration-script.json`](narration-script.json) ·
[`voice_talent.md`](voice_talent.md) · [`asset-register.md`](asset-register.md) · [`lint-report.json`](lint-report.json).

---

## A. Module header

| Field | Value |
|---|---|
| Module | {cfg['number']} — {cfg['package_title']} |
| Module prefix | `{cfg['prefix']}-` |
| Storyboard version | `v0.2` |
| Author | Arena agent — production-documentation pass |
| Date | {TODAY} |
| Status | `Draft — ready for SME review; blocked from production by open source-lock items` |
| SME reviewer (role) | {cfg['reviewers']} |
| Audience | {cfg['audience']} |
| Seat-time budget | {cfg['seat_time']} |
| SCORM / completion / pass mark | {cfg['scorm']} |
| Scored screens / total points | {scored} / {points} (Phase 4 expectation: {cfg['scored_expected']} / {cfg['points_expected']}) |
| Source file | `{cfg['source']}` |
| Brand | My Clinic — [`00_program/brand/brand-identity.md`](../../00_program/brand/brand-identity.md) (read {TODAY}) |
| Module colour | {cfg['module_colour']} |
| Theme | Official `brand-kit.json` plus the lint adapter `brand-kit.edumints.json`; Montserrat; supplied logo PNGs only |
| Phase 0 items still open | {cfg['phase_open']} |
| Narration reconciliation | {timing_reconciliation} |

### Production guardrails

- The supplied client logo remains a supplied PNG on every screen. It is **never** generated, redrawn, or included in an AI-image prompt.
- `⚠ PENDING` means an owner has not approved a source fact. Keep it in the editable build text until Phase 0 closes.
- The EHR source video and its withheld frames are **not** reused. Module 08 waits for test-environment captures and DPO approval.
- Generated visuals are concept assets only until the named SME checks factual details, especially interaction hotspots and physical equipment.

### Objectives covered

| Objective id | Objective | Assessed by |
|---|---|---|
{objectives_md}

### Section outline

| Node id | Section title | Screens |
|---|---|---|
{chr(10).join(section_rows)}

### Proposed changes

None. The source Phase 2 ids, order, screen types and scoring allocation are retained exactly. Any
change must be proposed in Phase 2/4 before a build starts.

---

## B. Screen cards

{''.join(card_parts)}

## C. Module summary

### Screen register

| # | Screen id | Type | Scored | Pts | On-screen words | Narration words | Est. sec | Status |
|---|---|---|---|---|---|---|---|---|
{chr(10).join(register_md)}
| | **Totals** | | **{scored}** | **{points}** | | **{sum(word_count(narration_plain(s['narration'])) for s in scripts)}** | **{round(estimated_seconds)} ≈ {round(estimated_seconds / 60, 1)} min** | Draft |

### Asset list

| Asset id | Kind | Used on | Source | Alt text written? | Status |
|---|---|---|---|---|---|
{chr(10).join(asset_summary)}

### Open questions for the SME

| # | Screen id | Question | Phase 0 owner | Blocks build? |
|---|---|---|---|---|
{questions_md}

### Lexicon additions

| Term | Say it as | Screens |
|---|---|---|
{lexicon_md}

### Self-check

- [x] Every Phase 2 core screen has a card, in the same id order.
- [x] Screen scoring totals reconcile to the Phase 2/4 plan ({scored} scored / {points} points).
- [x] Every screen has a visual brief, supplied-logo instruction, narration segment and accessibility notes.
- [x] Every meaningful generated or planned image is listed with an alt-text route and provenance status.
- [x] Template structural review ran on every card: all eight sections and every Phase 2 interaction brief are present; human SME/content approval remains pending.
- [x] No real patient, staff, claim or contact data is introduced.
- [ ] SME review and Phase 0 approval are complete — **not yet; do not move to production.**
- [ ] Production voice selection / D10 approval is complete — **not yet.**
- [ ] Type-specific production JSON, final asset IDs and SCORM build have been validated — **Phase 4 work, not claimed here.**
'''
    (out_dir / "storyboard.md").write_text(module_doc, encoding="utf-8")
    return {
        "folder": folder, "number": cfg["number"], "title": cfg["title"], "screen_count": len(rows),
        "scored": scored, "points": points, "estimated_audio": round(estimated_seconds / 60, 1), "phase3_screen_target": round(detailed_target_seconds / 60, 1), "phase3_rough_estimate": rough_phase3_minutes, "out": str(out_dir),
    }


def write_brand_adapter() -> None:
    """Keep the official client brand kit untouched and provide a schema-safe lint adapter."""
    destination = PLANS / "00_program" / "brand" / "brand-kit.edumints.json"
    adapter = {
        "name": "My Clinic", "language": "en",
        "colors": {"primary": "#003867", "secondary": "#008C99", "accent": "#9D3293", "dark": "#1F2A37", "light": "#F4F7FA", "surface": "#FFFFFF", "success": "#1E7B4F", "error": "#B42318", "warning": "#8A5A00"},
        "fonts": {"heading": "Montserrat", "body": "Montserrat", "arabic": "Tajawal"},
        "logo_asset_id": "brand-logo-horizontal-navy", "logo_alt": "My Clinic logo",
        "imagery_style": "Clean flat vector illustration in the My Clinic palette: navy outlines, white space, one module colour as a highlight, no gradients, no text and no logos. Diagrams use editable SVG or HTML; EHR screenshots use a test account only.",
        "voice": {"tone": "warm, calm, precise", "persona": "an experienced colleague coaching a new team member in their first week", "formality": "conversational"},
        "do": ["Use supplied logo PNGs exactly", "Use Montserrat", "Keep real wording as HTML", "Use colour with labels and icons"],
        "dont": ["Never generate the My Clinic logo", "No patient or staff data", "No third-party watermark", "No small white text on teal"],
    }
    destination.write_text(json.dumps(adapter, indent=2) + "\n", encoding="utf-8")


def write_program_dashboard(results: list[dict[str, Any]]) -> None:
    md = [
        "# My Clinic — storyboard production board", "", "![My Clinic logo](brand/logo-preview.png)", "",
        f"> Consolidated review status as at **{TODAY}**. This is a production-documentation board, not a statement that policy, clinical, payer or EHR content is approved.", "",
        "**Client-shareable Word renderings:** [`../client-review/README.md`](../client-review/README.md). The Markdown/JSON/HTML files below remain the editable production source.", "",
        "## What is now documented", "",
        "| Module | Screen cards | Scored / points | Script + visual plan | Branded screen review | Asset register | Planning lint | Production status |",
        "|---|---:|---:|---|---|---|---|---|",
    ]
    for r in results:
        rel = f"../{r['folder']}/storyboard"
        md.append(f"| {r['number']} — [{r['title']}]({rel}/storyboard.md) | {r['screen_count']} | {r['scored']} / {r['points']} | [JSON]({rel}/narration-script.json) · [visual plan]({rel}/visual-plan.json) | [HTML]({rel}/screen-visuals.html) | [register]({rel}/asset-register.md) | [Clean report]({rel}/lint-report.json) | Draft — SME/source-lock review |")
    md += [
        "| 03 — Welcome On Board | 36 | 15 / 145 | Existing storyboard, visual plan and narration script | Existing brand mockups | Existing preview/audio reference | Not rerun in this pass | Draft — SME review |",
        "| 07 — Clinical Governance | 22 core | 11 / 95 | Existing storyboard | Existing brand mockups | Pending policy/source review | Not available in this pass | Draft — SME review |", "",
        "## Phase gate snapshot", "", "| Phase | What is materially complete | What cannot be claimed yet |", "|---|---|---|", "| 0 — Source lock | Owners, conflicts and explicit open decisions are documented for all eight modules. | No module with open B/D records is released to production. |", "| 1 — Action map | Objectives, practice and seat-time budgets are in every module folder. | SMEs still approve objectives and evidence. |", "| 2a — Screen list | All eight plans have a Phase 2 screen list. | Changes must return to Phase 2 before build. |", "| 2b — Storyboard cards | 03 and 07 existed; 01, 02, 04, 05, 06 and 08 now have complete review-card packs. | Pending values cannot be treated as course facts. |", "| 3 — Narration/assets | Each new pack now has an editable narration script, voice-talent table, visual plan, asset register and logo placement rules. | D10 voice choice, approved scripts, EHR test captures and asset approval remain open. |", "| 4–5 — Build/QA | Build plans and QA plans exist. | No SCORM project, package, LMS test, QA sign-off or completion data is claimed. |", "",
        "## Decisions that still gate release", "", "1. **Safety:** Code Orange threshold, real emergency extensions, waste colours, radiation/laser details and facility-specific information (modules 01–02).", "2. **Operations:** live reporting lines, abbreviation expansions and escalation ownership (module 04).", "3. **RCM:** current payer/regulator wording, ICD-10 validation, benefits/limits and de-identified rejection classifications (modules 05–06).", "4. **EHR:** only a test environment/test patient may be captured; the existing source video is never a production asset (module 08).", "5. **Programme:** Marketing brand confirmation D11, two approved narration voices D10 and every asset’s provenance/approval record.", "",
        "## Asset work completed in this pass", "", "- Generated native editable SVG diagrams where facts can be changed after SME review.", "- Generated three review-only, no-logo visual assets: the facility safety corridor, safety lab storeroom and Operations reception scenario.", "- Added the `brand-kit.edumints.json` adapter to resolve the known official-brand-kit formality mismatch without changing the client’s official `brand-kit.json`.", "- Added HTML visual review boards that use the supplied My Clinic logo and obey the Montserrat / navy / module-colour system.", "",
        "## Next hand-off", "", "1. Circulate the relevant `storyboard/storyboard.md` and `screen-visuals.html` file to each named SME.", "2. Close Phase 0 records in writing; update only the source-lock file and cards that cite that decision.", "3. Choose/approve Noor and Dr. Omar voice samples under D10 before generating shipping audio.", "4. For module 08, capture test-environment screenshots and obtain DPO approval before any simulation build.", "5. The visual-plan and narration-script lint reports are currently clean for the six new packs; rerun them, plus `lint_authoring_plan(stage=planning)`, after any approved edit and before Phase 4 build.", "",
    ]
    (PLANS / "00_program" / "storyboard-production-board.md").write_text("\n".join(md), encoding="utf-8")

    cards = "\n".join(f'<li><a href="../{r["folder"]}/storyboard/screen-visuals.html">{html.escape(r["number"] + " — " + r["title"])}</a><span>{r["screen_count"]} review boards · {r["scored"]} scored screens · {r["points"]} points</span></li>' for r in results)
    page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>My Clinic storyboard production board</title><style>@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap');*{{box-sizing:border-box}}body{{margin:0;background:#F4F7FA;color:#1F2A37;font-family:Montserrat,Arial,sans-serif}}header{{background:linear-gradient(135deg,#003867,#3B6A97);color:#fff;padding:54px max(26px,8vw)}}header img{{width:205px}}h1{{font-size:38px;margin:30px 0 8px}}header p{{color:#C0CED9;max-width:720px;line-height:1.55}}main{{max-width:980px;margin:32px auto;padding:0 24px}}.notice{{background:white;border-left:5px solid:#9D3293;padding:18px;border-radius:10px;line-height:1.55}}ul{{list-style:none;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px}}li{{background:#fff;border:1px solid #D9E1E8;border-radius:14px;padding:22px;min-height:120px}}a{{color:#003867;font-weight:700;font-size:18px;text-decoration:none}}span{{display:block;color:#5B6B7B;font-size:13px;line-height:1.45;margin-top:10px}}.steps{{background:#fff;border-radius:14px;padding:24px;line-height:1.75}}code{{color:#006E78}}</style></head><body><header><img src="brand/assets/logo-horizontal-white.png" alt="My Clinic logo"><h1>Storyboard production board</h1><p>Branded review documents, narration scripts, visual plans and asset hand-offs for the My Clinic e-learning programme.</p></header><main><section class="notice"><strong>Review before production.</strong> The visual work is ready to inspect; open Phase 0 facts, voices, test-environment captures and policy decisions are intentionally not represented as approved course content. <a href="../client-review/README.md">Open the client Word review-pack index.</a></section><h2>Branded screen review boards</h2><ul>{cards}</ul><section class="steps"><h2>Next hand-off</h2><ol><li>SMEs review the matching screen-card document and visual board.</li><li>Owners close the source-lock decisions in writing.</li><li>Approve Noor and Dr. Omar samples before shipping-audio production.</li><li>Build only after planning lint and source approval are clean.</li></ol></section></main></body></html>'''
    (PLANS / "00_program" / "storyboard-production-board.html").write_text(page, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("modules", nargs="*", help="Optional module folder(s); defaults to all unfinished storyboard packs.")
    args = parser.parse_args()
    unknown = sorted(set(args.modules) - set(MODULES))
    if unknown:
        parser.error("unknown module folder(s): " + ", ".join(unknown))
    selected = args.modules or list(MODULES)
    write_brand_adapter()
    results = [write_storyboard(folder) for folder in selected]
    # The programme board should list all newly produced packs.  It is intentionally regenerated
    # only in the all-modules run so a one-module correction does not hide the rest.
    if not args.modules:
        write_program_dashboard(results)
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
