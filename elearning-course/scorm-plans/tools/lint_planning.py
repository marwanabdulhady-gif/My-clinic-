#!/usr/bin/env python3
"""Local planning-lint gate for the My Clinic storyboard packs.

The programme quality gate is the edumints server's ``lint_visual_plan`` and
``lint_narration_script`` (``core/playbook.py``, revision 4bbf4591). The MCP server is not
reachable from this workspace, so this tool ports the same deterministic rules locally and
writes ``storyboard/lint-report.json`` for every pack, so the gate can be rerun after any edit
instead of trusting an old report.

Honesty note kept inside every report: ``tool`` names this port, ``tool_revision`` names the
upstream revision the rules were ported from, and ``upstream_equivalence`` records that the
server-side lint must still be rerun before Phase 4. The report never claims an MCP result.

Usage:
    python3 elearning-course/scorm-plans/tools/lint_planning.py            # all eight packs
    python3 elearning-course/scorm-plans/tools/lint_planning.py 07_quality-safety-and-risk
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PLANS = ROOT / "elearning-course" / "scorm-plans"
TOOL_REVISION = "4bbf4591cf8a3ffcb63909fcb69f0547e1654db0"
TODAY = "2026-10-14"

WPM_DEFAULT = {"en": 140, "ar": 120, "tr": 130}
MAX_SEGMENT_SEC = 60.0
MAX_SENTENCE_WORDS = 25
MAX_ON_SCREEN_WORDS = 45
REDUNDANCY_RATIO = 0.8
REDUNDANCY_MIN_WORDS = 15
AA_TEXT = 4.5
AA_UI = 3.0

MARK_RE = re.compile(r"\[\[[^\]]*\]\]")
CUE_RE = re.compile(r"\[\[cue:([A-Za-z0-9_.-]+)\]\]")
PAUSE_RE = re.compile(r"\[\[pause:(\d+(?:\.\d+)?)\]\]")
ACRONYM_RE = re.compile(r"\b[A-Z][A-Z0-9]{1,5}\b")
WORD_RE = re.compile(r"[\w'’-]+", re.UNICODE)
SCREEN_TALK = (
    "as you can see on the screen", "on this slide", "this slide shows", "click next to continue",
    "in this screen", "as shown on the screen",
)

SCORED_TYPES = {
    "mcq", "true_false", "fill_blank", "drag_drop", "hotspot", "matching", "sorting",
    "decision_scenario", "labeled_diagram", "adaptive_practice", "game", "term_match_race",
    "escape_room", "simulation",
}
PASSIVE_TYPES = {"title_slide", "content_slide", "video", "summary", "lottie", "data_chart", "timeline"}
ASSESSMENT_TYPES = {"mcq", "true_false", "fill_blank"}
KNOWN_TYPES = SCORED_TYPES | PASSIVE_TYPES | {
    "tabs", "accordion", "flashcards", "timeline", "worked_example", "hotspot", "image_compare",
    "results_breakdown", "poll", "summary", "title_slide", "video",
}

PLAN_SCREEN_KEYS = (
    "screen_id", "screen_type", "purpose", "visual_concept", "layout", "background_role",
    "text_role", "accent_role", "imagery", "on_screen_text", "animation", "cue_targets",
)
SEGMENT_KEYS = ("screen_id", "narration", "target_sec", "tone")


def words(text):
    return WORD_RE.findall(text or "")


def spoken(text):
    return re.sub(r"\s+", " ", MARK_RE.sub(" ", text)).strip()


def issue(sev, code, message, path=None):
    return {"severity": sev, "code": code, "message": message, "path": path}


def report(issues, **extra):
    return {
        "error_count": sum(1 for i in issues if i["severity"] == "error"),
        "warn_count": sum(1 for i in issues if i["severity"] == "warn"),
        "clean": not issues,
        **extra,
        "issues": issues,
    }


def srgb(channel):
    channel /= 255.0
    return channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4


def luminance(hex_color):
    hex_color = hex_color.lstrip("#")
    r, g, b = (int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * srgb(r) + 0.7152 * srgb(g) + 0.0722 * srgb(b)


def contrast(fg, bg):
    l1, l2 = luminance(fg), luminance(bg)
    if l1 < l2:
        l1, l2 = l2, l1
    return (l1 + 0.05) / (l2 + 0.05)


def roles_from_adapter(adapter):
    c = adapter.get("colors", {})
    primary = c.get("primary", "#003867")
    on_primary = "#ffffff" if contrast("#ffffff", primary) >= contrast("#111111", primary) else "#111111"
    return {
        "primary": primary,
        "secondary": c.get("secondary") or primary,
        "accent": c.get("accent") or c.get("secondary") or primary,
        "dark": c.get("dark") or "#18181b",
        "light": c.get("light") or "#fafafa",
        "surface": c.get("surface") or "#ffffff",
        "success": c.get("success") or "#168139",
        "error": c.get("error") or "#cb2323",
        "warning": c.get("warning") or "#975606",
        "on_primary": on_primary,
    }


def estimate_sec(text, wpm):
    pauses = sum(float(p) for p in PAUSE_RE.findall(text))
    return round(len(words(spoken(text))) / wpm * 60.0 + pauses, 1)


def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?؟])\s+", spoken(text)) if s.strip()]


def validate_visual_plan(plan):
    problems = []
    if not isinstance(plan, dict):
        return ["visual plan is not an object"]
    for key in ("module_id", "module_title", "brand_name", "audience", "screens"):
        if key not in plan:
            problems.append(f"visual plan missing '{key}'")
    for i, screen in enumerate(plan.get("screens", [])):
        path = f"screens[{i}]"
        for key in PLAN_SCREEN_KEYS:
            if key not in screen:
                problems.append(f"{path} missing '{key}'")
        st = screen.get("screen_type")
        if st and st not in KNOWN_TYPES:
            problems.append(f"{path} unknown screen_type '{st}'")
        for j, img in enumerate(screen.get("imagery", []) or []):
            if not img.get("decorative") and not (img.get("alt_text") or "").strip():
                problems.append(f"{path}.imagery[{j}] missing alt_text")
    return problems


def validate_narration(script):
    problems = []
    if not isinstance(script, dict):
        return ["narration script is not an object"]
    for key in ("module_id", "language", "wpm", "segments"):
        if key not in script:
            problems.append(f"narration script missing '{key}'")
    if not isinstance(script.get("lexicon", {}), dict):
        problems.append("lexicon must be an object")
    for i, seg in enumerate(script.get("segments", [])):
        path = f"segments[{i}]"
        for key in SEGMENT_KEYS:
            if key not in seg:
                problems.append(f"{path} missing '{key}'")
        if seg.get("target_sec") is not None and not isinstance(seg.get("target_sec"), (int, float)):
            problems.append(f"{path}.target_sec must be a number")
    return problems


def lint_visual_plan(plan, roles):
    issues = []
    defined = set(roles)
    seen, run_type, run_len, passive_run, accent_bg, has_check = set(), None, 0, 0, 0, False
    for i, s in enumerate(plan.get("screens", [])):
        path = f"screens[{i}]({s.get('screen_id')})"
        if s.get("screen_id") in seen:
            issues.append(issue("error", "duplicate_screen_id", f"screen_id '{s.get('screen_id')}' is used twice", path))
        seen.add(s.get("screen_id"))
        if len(words(s.get("visual_concept"))) < 6:
            issues.append(issue("warn", "vague_visual_concept", "visual_concept should describe what the learner SEES (composition, subject, metaphor) in at least one full sentence", path))
        for j, img in enumerate(s.get("imagery", []) or []):
            if not img.get("decorative") and not (img.get("alt_text") or "").strip():
                issues.append(issue("error", "missing_alt_text", f"{img.get('kind')} needs alt_text (or decorative=true)", f"{path}.imagery[{j}]"))
        n_words = len(words(s.get("on_screen_text") or ""))
        if n_words > MAX_ON_SCREEN_WORDS:
            issues.append(issue("warn", "text_heavy_screen", f"{n_words} on-screen words (> {MAX_ON_SCREEN_WORDS}); move detail into narration or split the screen", path))
        for role in {s.get("background_role"), s.get("text_role"), s.get("accent_role")} - {None}:
            if role not in defined:
                issues.append(issue("warn", "role_not_in_brand", f"color role '{role}' is not defined in the brand kit; it falls back", path))
        ratio = contrast(roles[s.get("text_role")], roles[s.get("background_role")])
        if ratio < AA_TEXT:
            issues.append(issue("error", "low_contrast", f"text '{s.get('text_role')}' on background '{s.get('background_role')}' is {ratio:.2f}:1 (< {AA_TEXT}:1)", path))
        if s.get("background_role") == "accent":
            accent_bg += 1
        st = s.get("screen_type")
        if st == run_type:
            run_len += 1
        else:
            run_type, run_len = st, 1
        if run_len == 3:
            issues.append(issue("warn", "monotony", f"3 '{st}' screens in a row — vary the format", path))
        if st in PASSIVE_TYPES:
            passive_run += 1
            if passive_run == 5:
                issues.append(issue("warn", "passive_stretch", "5 passive screens in a row — add an interaction or check", path))
        else:
            passive_run = 0
        if st in SCORED_TYPES:
            has_check = True
    if not has_check:
        issues.append(issue("warn", "no_knowledge_check", "module has no scored/interactive check screen", "screens"))
    screens = plan.get("screens", [])
    if screens and accent_bg / len(screens) > 0.10:
        issues.append(issue("warn", "accent_overuse", f"accent used as background on {accent_bg}/{len(screens)} screens — keep accent to ~10% (60-30-10 rule)", "screens"))
    return report(issues, module_id=plan.get("module_id"), screen_count=len(screens))


def lint_narration_script(script, plan):
    issues = []
    wpm = script.get("wpm") or WPM_DEFAULT.get(str(script.get("language", "en")).split("-")[0].lower(), 135)
    plan_screens = {s.get("screen_id"): s for s in plan.get("screens", [])} if plan else {}
    lexicon = {k.upper() for k in script.get("lexicon", {})}
    total, per_screen, covered = 0.0, [], set()
    for i, seg in enumerate(script.get("segments", [])):
        path = f"segments[{i}]({seg.get('screen_id')}{('/' + seg['part']) if seg.get('part') else ''})"
        text = spoken(seg.get("narration", ""))
        if not text:
            issues.append(issue("error", "empty_narration", "narration is empty", path))
            continue
        covered.add(seg.get("screen_id"))
        est = estimate_sec(seg.get("narration", ""), wpm)
        total += est
        per_screen.append({"screen_id": seg.get("screen_id"), "part": seg.get("part"), "words": len(words(text)), "est_sec": est})
        if plan and seg.get("screen_id") not in plan_screens:
            issues.append(issue("error", "unknown_screen", f"screen_id '{seg.get('screen_id')}' is not in the visual plan", path))
        if est > MAX_SEGMENT_SEC:
            issues.append(issue("warn", "segment_too_long", f"~{est}s of narration (> {MAX_SEGMENT_SEC:.0f}s) — split into parts/layers or another screen", path))
        if seg.get("target_sec") and est > seg["target_sec"] * 1.15:
            issues.append(issue("warn", "over_target_time", f"~{est}s vs target {seg['target_sec']}s at {wpm} wpm", path))
        for sent in sentences(seg.get("narration", "")):
            n = len(words(sent))
            if n > MAX_SENTENCE_WORDS:
                issues.append(issue("warn", "long_sentence", f"{n}-word sentence — keep spoken sentences ≤ {MAX_SENTENCE_WORDS} words: '{sent[:60]}…'", path))
        low = text.lower()
        for phrase in SCREEN_TALK:
            if phrase in low:
                issues.append(issue("warn", "screen_talk", f"avoid '{phrase}' — narrate the idea, not the interface", path))
        for acr in sorted(set(ACRONYM_RE.findall(text))):
            if acr not in lexicon:
                issues.append(issue("warn", "pronunciation_missing", f"'{acr}' has no lexicon entry — add how TTS/voice talent should say it", path))
        ost = [w.lower() for w in words(seg.get("on_screen_text") or "")]
        if len(ost) >= REDUNDANCY_MIN_WORDS:
            narr = " ".join(w.lower() for w in words(text))
            grams = [" ".join(ost[k:k + 4]) for k in range(len(ost) - 3)]
            hit = sum(1 for g in grams if g in narr)
            if grams and hit / len(grams) >= REDUNDANCY_RATIO:
                issues.append(issue("warn", "redundant_on_screen_text", "narration reads the on-screen text word for word — show keywords on screen, explain in voice", path))
        ps = plan_screens.get(seg.get("screen_id"))
        for cue in CUE_RE.findall(seg.get("narration", "")):
            if ps is not None and cue not in (ps.get("cue_targets") or []):
                issues.append(issue("error", "unknown_cue_target", f"[[cue:{cue}]] is not in the plan's cue_targets {ps.get('cue_targets')}", path))
    if plan:
        for s in plan.get("screens", []):
            if s.get("screen_id") not in covered and s.get("screen_type") not in ASSESSMENT_TYPES:
                issues.append(issue("warn", "missing_narration", f"plan screen '{s.get('screen_id')}' ({s.get('screen_type')}) has no narration segment", s.get("screen_id")))
    return report(issues, module_id=script.get("module_id"), wpm=wpm,
                  total_est_sec=round(total, 1), total_est_min=round(total / 60, 1), screens=per_screen)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("modules", nargs="*", help="Module folders; default: all eight.")
    args = parser.parse_args()
    adapter_path = PLANS / "00_program" / "brand" / "brand-kit.edumints.json"
    adapter = json.loads(adapter_path.read_text(encoding="utf-8"))
    roles = roles_from_adapter(adapter)
    folders = args.modules or sorted(p.name for p in PLANS.glob("0[1-8]_*"))
    exit_code = 0
    for folder in folders:
        story = PLANS / folder / "storyboard"
        plan = json.loads((story / "visual-plan.json").read_text(encoding="utf-8"))
        script = json.loads((story / "narration-script.json").read_text(encoding="utf-8"))
        plan_problems = validate_visual_plan(plan)
        script_problems = validate_narration(script)
        vp = lint_visual_plan(plan, roles)
        ns = lint_narration_script(script, plan)
        report_path = story / "lint-report.json"
        existing = {}
        if report_path.exists():
            try:
                existing = json.loads(report_path.read_text(encoding="utf-8"))
            except ValueError:
                existing = {}
        keep = {k: v for k, v in existing.items()
                if k not in {"generated_at", "tool", "tool_revision", "brand_adapter", "model_validation",
                             "visual_plan", "narration_script", "production_note", "upstream_equivalence"}}
        out = {
            "generated_at": TODAY,
            "tool": "tools/lint_planning.py — deterministic local port of edumints core.playbook lint rules",
            "tool_revision": TOOL_REVISION,
            "brand_adapter": "../../00_program/brand/brand-kit.edumints.json",
            "upstream_equivalence": "Rules ported from edumints-scorm-mcp core/playbook.py at the "
                                    "revision above. The MCP server is not reachable from this "
                                    "workspace, so rerun lint_visual_plan and lint_narration_script "
                                    "on the server before Phase 4; this file is not an MCP result.",
            "model_validation": {
                "visual_plan": not plan_problems,
                "narration_script": not script_problems,
                "problems": plan_problems + script_problems,
            },
            "visual_plan": vp,
            "narration_script": ns,
            **keep,
            "production_note": "Planning lint only. Phase 0 approval, asset QA, type-specific build "
                               "JSON and SCORM QA remain required.",
        }
        report_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        status = "clean" if (vp["clean"] and ns["clean"] and not plan_problems and not script_problems) else "ISSUES"
        if status == "ISSUES":
            exit_code = 1
        print(f"{folder}: visual {vp['error_count']}e/{vp['warn_count']}w · "
              f"narration {ns['error_count']}e/{ns['warn_count']}w · model ok "
              f"{out['model_validation']['visual_plan'] and out['model_validation']['narration_script']} · {status}")
        for item in vp["issues"] + ns["issues"] + [issue("error", "model", p) for p in plan_problems + script_problems]:
            print(f"    [{item['severity']}] {item['code']}: {item['message']} ({item['path']})")
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
