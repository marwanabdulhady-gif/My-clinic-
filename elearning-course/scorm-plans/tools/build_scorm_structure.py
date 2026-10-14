#!/usr/bin/env python3
"""Generate <module>/scorm-structure.md from the storyboard build blocks.

Source of truth: the JSON build blocks in <module>/storyboard/storyboard.md (id, type,
node_id, points, objective_ids), the section and objective tables in the same file,
phase-4-build.md (course settings), phase-2-storyboard.md (companions) and the
storyboard narration script. Rerun after any approved storyboard change:

    python3 elearning-course/scorm-plans/tools/build_scorm_structure.py
"""
import argparse
import glob
import json
import os
import re
from collections import OrderedDict
from pathlib import Path
from assemble_storyboard_docs import parse_assets
from planned_visual_assets import assets_for_screen, is_visual

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SCORED_TYPES_HINT = "★ = scored"
SHORT = {"01": "FMS", "02": "SafetyLab", "03": "WelcomeOnBoard", "04": "OpsMyCare",
         "05": "RCM-A", "06": "RCM-B", "07": "ClinicalGov", "08": "EHR"}
SCENARIO_TYPES = {"decision_scenario", "game", "simulation", "adaptive_practice", "escape_room"}


def blocks(text):
    out = []
    for m in re.finditer(r"```json\s*\n(.*?)```", text, re.S):
        try:
            j = json.loads(m.group(1))
        except ValueError:
            continue
        if isinstance(j, dict) and "type" in j and "id" in j:
            out.append(j)
    return out


def table_rows(text, first_cell_re):
    rows = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and re.fullmatch(first_cell_re, cells[0].strip("`")):
            rows.append(cells)
    return rows


def course_settings(p4):
    m = re.search(r"```json\s*\n(\{.*?\})\s*```", p4, re.S)
    return json.loads(m.group(1)) if m else {}


def narration(module_dir, sb_text):
    path = os.path.join(module_dir, "storyboard", "narration-script.json")
    if os.path.exists(path):
        segs = json.loads(Path(path).read_text())["segments"]
        words, speakers = {}, {}
        for s in segs:
            t = s.get("narration", "")
            sid = s["screen_id"]
            speakers[sid] = sorted(set(speakers.get(sid, [])) | set(re.findall(r"\b(NOOR|OMAR):", t)))
            t = re.sub(r"\[\[.*?\]\]", "", t)
            t = re.sub(r"\b(NOOR|OMAR):", "", t)
            words[sid] = words.get(sid, 0) + len(t.split())
        return words, speakers, "narration-script.json"
    return {}, {}, None


def companions(p2):
    out = {}
    for cells in table_rows(p2, r"[a-z0-9]+-\d{3}"):
        if len(cells) == 3 and ("char-" in cells[1] or "Both" in cells[1]):
            out[cells[0]] = re.sub(r"\s*\(.*", "", cells[1])
    return out


# SCORM interaction type vocabulary. SCORM 1.2 and 2004 share these values
# (2004 additionally allows "long-fill-in", which no pack uses).
INTERACTION_TYPE = {
    "mcq": "choice", "true_false": "true-false", "fill_blank": "fill-in",
    "matching": "matching", "drag_drop": "matching", "sorting": "sequencing",
    "hotspot": "performance", "labeled_diagram": "performance", "image_compare": "other",
    "decision_scenario": "performance", "simulation": "performance", "game": "performance",
    "escape_room": "fill-in", "adaptive_practice": "choice", "term_match_race": "matching",
}
# Mechanics the approved gamification plan excludes; used by the base-structure audit.
BANNED_MECHANICS = ("leaderboard", "ranking", "streak", "badge", "countdown", "time limit")


def activity_rules(p3_text):
    """Phase 3 activity-rule rows (lives, hints, retry, pass) keyed by their first cell."""
    rows, header = [], None
    for line in p3_text.splitlines():
        if not line.startswith("|"):
            header = None
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and cells[0].strip().lower() == "activity":
            header = [c.lower() for c in cells]
            continue
        if header is None or not cells:
            continue
        if set("".join(cells)) <= set("-: "):
            continue
        rows.append(dict(zip(header, cells)))
    return rows


def rule_for(rules, screen_id):
    """The Phase 3 rule row that governs a screen, matched on its id (or its number list)."""
    number = screen_id.split("-")[-1]
    for row in rules:
        activity = row.get("activity", "")
        if screen_id in activity or re.search(rf"(?<!\d){re.escape(number)}(?!\d)", activity):
            return row
    return {}


def scenario_shape(screen, rule=None):
    """One-line description of the authored branch/step structure of a scenario screen.

    Where the storyboard block carries no branch JSON yet, the Phase 3 activity row is the
    only authored structure; saying "0 nodes" would misreport it as an empty scenario.
    """
    stype = screen["type"]
    rule_text = (rule or {}).get("rules", "")
    fallback = (f"not in the storyboard block yet — Phase 3: {rule_text}" if rule_text
                else "authored in Phase 3, no branch JSON in the storyboard block yet")
    if stype == "decision_scenario":
        nodes = screen.get("nodes") or []
        if not nodes:
            return fallback
        choices = sum(len(n.get("choices") or []) for n in nodes)
        branches = sum(1 for n in nodes for c in (n.get("choices") or []) if c.get("goto_node_id"))
        return f"{len(nodes)} decision nodes · {choices} authored choices · {branches} explicit branches"
    if stype == "simulation":
        steps = screen.get("steps") or []
        if not steps:
            return fallback
        targets = sum(len(s.get("regions") or []) + (1 if s.get("input_accepted") else 0)
                      for s in steps)
        return f"{len(steps)} click/type steps · {targets} scored targets"
    if stype == "adaptive_practice":
        bank = len(screen.get("items") or [])
        if not bank:
            return fallback
        return (f"{bank}-item bank · max {screen.get('max_items', '?')} served · "
                f"pass ratio {screen.get('pass_ratio', '?')} · "
                f"{screen.get('adaptive', {}).get('strategy', 'fixed')}")
    if stype == "escape_room":
        puzzles = screen.get("blocks") or screen.get("puzzles") or []
        return f"{len(puzzles)} sequential puzzles" if puzzles else fallback
    if stype == "game":
        nodes = screen.get("nodes") or []
        return f"{len(nodes)} nodes" if nodes else fallback
    return "—"


def suspend_estimate(screens, scored):
    """Rough suspend_data size: resume pointer + one small record per screen/scored screen.

    Deliberately conservative and documented as an estimate — the real payload depends on the
    built player. The point of the number is the SCORM 1.2 4,096-character cliff.
    """
    return len(screens) * 24 + len(scored) * 48


def has_feedback(screen):
    """True when the authored block carries answer feedback somewhere the player can show it."""
    if screen.get("feedback"):
        return True
    for option in screen.get("options") or []:
        if option.get("feedback_html"):
            return True
    for node in screen.get("nodes") or []:
        if any(c.get("feedback_html") for c in node.get("choices") or []):
            return True
    for item in (screen.get("items") or []) + (screen.get("blocks") or []):
        if item.get("explain_html") or item.get("feedback_html"):
            return True
    return False


def banned_mechanic_hits(text):
    """Heuristic scan for mechanics the approved gamification plan excludes.

    The packs legitimately use some of these words for other things — a staff "ID badge",
    "visitor badges", an incident-reporting "time limit" — so each word needs its own
    gamification context:

    * ``badge`` counts only when it is earned/awarded/unlocked/collected;
    * ``time limit`` / ``countdown`` count only next to a question, quiz, screen or timer;
    * ``leaderboard`` / ``ranking`` / ``streak`` are unambiguous here and always count.

    A negation ("no timer") is the plan restating the rule, so it is skipped. This is a
    reading aid for reviewers, not a proof.
    """
    contexts = {
        "badge": r"\b(earn\w*|award\w*|unlock\w*|collect\w*|reward\w*|gamif\w*|trophy)\b",
        "time limit": r"\b(question|quiz|answer|screen|timer|seconds?|attempt|per item)\b",
        "countdown": r"\b(question|quiz|answer|screen|timer|seconds?|attempt|per item)\b",
    }
    hits = []
    for line_number, line in enumerate(text.splitlines(), 1):
        for word in BANNED_MECHANICS:
            for match in re.finditer(re.escape(word), line, re.I):
                before = line[max(0, match.start() - 28):match.start()].lower()
                if re.search(r"\b(no|not|never|without|avoid|exclude[d]?|zero)\b[^.]{0,24}$",
                             before):
                    continue
                context = contexts.get(word)
                if context and not re.search(context, line, re.I):
                    continue
                hits.append((word, line_number))
    return hits


def build(module_dir):
    name = os.path.basename(module_dir)
    num = name[:2]
    sb_path = os.path.join(module_dir, "storyboard", "storyboard.md")
    sb = Path(sb_path).read_text()
    p2 = (Path(module_dir) / "phase-2-storyboard.md").read_text()
    p3 = (Path(module_dir) / "phase-3-narration-and-assets.md").read_text()
    p4 = (Path(module_dir) / "phase-4-build.md").read_text()
    readme = (Path(module_dir) / "README.md").read_text()
    settings = course_settings(p4)
    screens = blocks(sb)
    prefix = screens[0]["id"].split("-")[0]
    title = settings.get("title") or re.search(r"Package title \| (.*?) \|", readme).group(1)
    scorm = settings.get("scorm_version", "1.2")
    tracking = settings.get("tracking", {})
    passing = tracking.get("passing_score", 80)
    rule = tracking.get("completion_rule", "viewed_all_and_passed")

    sec_titles = OrderedDict()
    for cells in table_rows(sb, rf"{prefix}-s[A-Z0-9]+"):
        sec_titles.setdefault(cells[0].strip("`"), cells[1])
    obj_desc = OrderedDict()
    for cells in table_rows(sb, rf"{prefix}-o\d+"):
        obj_desc.setdefault(cells[0].strip("`"), cells[1])

    words, speakers, nar_src = narration(module_dir, sb)
    comp = companions(p2)

    nodes = OrderedDict()
    for s in screens:
        nodes.setdefault(s.get("node_id") or s.get("section"), []).append(s)
    total_pts = sum(s.get("points") or 0 for s in screens)
    scored = [s for s in screens if s.get("points")]
    scen = [s for s in screens if s["type"] in SCENARIO_TYPES]
    narrated = [s for s in screens if words.get(s["id"])]
    minutes = sum(words.values()) / 140 if words else None
    pass_pts = -(-total_pts * passing // 100)

    zip_name = f"MC_{num}_{SHORT.get(num, prefix)}_v1.0_{scorm}.zip"
    L = []
    w = L.append
    w(f"# SCORM structure — {num} {title.replace('My Clinic — ', '')}\n")
    w("> Generated by `tools/build_scorm_structure.py` from the storyboard build blocks "
      "(`storyboard/storyboard.md`), `phase-4-build.md` and `phase-2-storyboard.md`. "
      "Do not edit by hand: change the storyboard, then rerun the script. "
      "Programme-wide rules: [`../00_program/scorm-structure.md`](../00_program/scorm-structure.md).\n")

    w("## 1. Package at a glance\n")
    w("| Item | Value |\n|---|---|")
    w(f"| Package file | `{zip_name}` (stored in Drive, not Git) |")
    w(f"| Manifest title | {title} |")
    w(f"| Standard | SCORM {'2004 4th edition' if scorm == '2004' else '1.2'} · one SCO · launch `index.html` |")
    w(f"| Manifest ids | `MANIFEST-<project_id>` → `ORG-1` → `ITEM-1` → `RES-1` |")
    w(f"| Language / layout | `{settings.get('language', 'en')}` · `{settings.get('layout_mode', 'stage')}` 960×540 |")
    w(f"| Completion rule | `{rule}` |")
    w(f"| Pass mark | {passing}% = **{pass_pts} / {total_pts} points** |")
    w(f"| Screens | {len(screens)} in {len(nodes)} outline sections |")
    w(f"| Scored screens | {len(scored)} · scenarios, games and simulations: {len(scen)} |")
    if minutes is not None:
        w(f"| Narration | {len(narrated)} narrated screens · ≈{minutes:.1f} min at 140 wpm (from `{nar_src}`) |")
    else:
        w("| Narration | `storyboard/narration-script.json` not produced yet — see §6 |")
    w(f"| LMS objectives | {len(obj_desc) or len({o for s in screens for o in s.get('objective_ids') or []})} (`cmi.objectives`) |")
    w("")

    w("## 2. Package contents (inside the zip)\n")
    w("```text")
    w(f"{zip_name}")
    w("├── imsmanifest.xml            # 1 organization, 1 item, 1 SCO resource listing every file")
    w("├── index.html                 # the whole course: player + all screens (rendered by edumints)")
    w("├── runtime/")
    w("│   └── scorm-again.min.js     # SCORM API wrapper (1.2 and 2004)")
    w("└── assets/")
    planned_assets = parse_assets(Path(module_dir))
    inactive_optional = {asset['id'] for asset in planned_assets if asset['optional'] and
                         not any(assets_for_screen([asset], screen['id']) for screen in screens)}
    planned_visual_ids = {asset['id'] for screen in screens
                         for asset in assets_for_screen(planned_assets, screen['id']) if is_visual(asset)}
    img_ids = sorted((set(re.findall(rf"`({prefix}-(?:img|shot|tbl|pdf|vid|cap)[a-z0-9-]*)`", sb + p2)) |
                      planned_visual_ids) - inactive_optional)
    if os.path.isdir(os.path.join(module_dir, "storyboard", "assets")):
        img_ids = sorted(set(img_ids) | {os.path.splitext(f)[0] for f in os.listdir(os.path.join(module_dir, "storyboard", "assets"))})
    for i in img_ids:
        w(f"    ├── {i}.*")
    char_ids = sorted(set(re.findall(r"`(char-(?:noor|omar)-[a-z-]+)", p2 + (Path(module_dir) / 'phase-3-narration-and-assets.md').read_text())))
    for c in char_ids:
        w(f"    ├── {c}.png")
    if narrated:
        w(f"    ├── {prefix}-aud-<screen>.mp3   # × {len(narrated)}, one per narrated screen, normalised")
    else:
        w(f"    ├── {prefix}-aud-<screen>.mp3   # one per narrated screen, normalised")
    w("    ├── brand: logo PNGs, title background, petal watermark")
    w("    └── PROVENANCE.json        # written when media provenance is recorded")
    w("```\n")
    w("Asset file names are fixed at `add_asset` time (`assets/<file>`); the list above is the planned set "
      "from the storyboard, Phase 2 and Phase 3. Final names come from the asset map in Phase 4.\n")

    w("## 3. Manifest sketch\n")
    if scorm == "2004":
        w("```xml\n<organizations default=\"ORG-1\">\n  <organization identifier=\"ORG-1\">\n"
          f"    <title>{title}</title>\n    <item identifier=\"ITEM-1\" identifierref=\"RES-1\">\n"
          f"      <title>{title}</title>\n      <imsss:sequencing>\n        <imsss:objectives>\n"
          f"          <imsss:primaryObjective satisfiedByMeasure=\"true\"><imsss:minNormalizedMeasure>{passing/100:.2f}</imsss:minNormalizedMeasure></imsss:primaryObjective>")
        for o in obj_desc or sorted({o for s in screens for o in s.get('objective_ids') or []}):
            w(f"          <imsss:objective objectiveID=\"{o}\"/>")
        w("        </imsss:objectives>\n      </imsss:sequencing>\n    </item>\n  </organization>\n</organizations>\n"
          "<resources>\n  <resource identifier=\"RES-1\" type=\"webcontent\" adlcp:scormType=\"sco\" href=\"index.html\">…every file…</resource>\n</resources>\n```\n")
    else:
        w("```xml\n<organizations default=\"ORG-1\">\n  <organization identifier=\"ORG-1\">\n"
          f"    <title>{title}</title>\n    <item identifier=\"ITEM-1\" identifierref=\"RES-1\">\n"
          f"      <title>{title}</title>\n      <adlcp:masteryscore>{passing}</adlcp:masteryscore>\n"
          "    </item>\n  </organization>\n</organizations>\n"
          "<resources>\n  <resource identifier=\"RES-1\" type=\"webcontent\" adlcp:scormtype=\"sco\" href=\"index.html\">…every file…</resource>\n</resources>\n```\n")
        w("SCORM 1.2 has no objectives in the manifest; the objectives below are reported at runtime "
          "through `cmi.objectives.n.*`.\n")

    w("## 4. Course structure (outline → screens)\n")
    w("The outline is the section menu the learner sees. Every section is `kind: \"section\"`, `unlock_rule: \"free\"`. "
      f"{SCORED_TYPES_HINT}; 🗣 = companion visible (Phase 2 companion table).\n")
    for node, ss in nodes.items():
        pts = sum(s.get("points") or 0 for s in ss)
        objs = sorted({o for s in ss for o in s.get("objective_ids") or []})
        head = f"### `{node}` — {sec_titles.get(node, '')}".rstrip(" —")
        w(f"{head}\n")
        w(f"{len(ss)} screens · {pts} points" + (f" · objectives {', '.join('`'+o+'`' for o in objs)}" if objs else "") + "\n")
        w("| # | Screen | Type | Title | Pts | Objective | Companion | Narration |")
        w("|---|---|---|---|---|---|---|---|")
        for i, s in enumerate(ss, 1):
            p = s.get("points") or 0
            star = " ★" if p else ""
            obj = ", ".join(s.get("objective_ids") or []) or "—"
            c = comp.get(s["id"], "")
            c = ("🗣 " + c) if c else "—"
            spk = "/".join(x.title() for x in speakers.get(s["id"], [])) or ("—" if not words else "")
            nw = words.get(s["id"])
            if nw and not spk:
                spk = "untagged"
            nar = f"{spk} · {round(nw / 140 * 60)} s" if nw else ("—" if words else "per card")
            w(f"| {i} | `{s['id']}`{star} | `{s['type']}` | {s.get('title', '')} | {p or ''} | {obj} | {c} | {nar} |")
        w("")

    w("## 5. Objectives, evidence and scoring\n")
    w("| Objective | What the learner can do | Scored evidence | Points | Share |")
    w("|---|---|---|---|---|")
    ev = OrderedDict()
    for s in screens:
        for o in s.get("objective_ids") or []:
            ev.setdefault(o, []).append(s)
    keys = list(obj_desc) or list(ev)
    weak = []
    for o in keys:
        ss = ev.get(o, [])
        pts = sum(s.get("points") or 0 for s in ss)
        if len(ss) < 2:
            weak.append(o)
        w(f"| `{o}` | {obj_desc.get(o, '')} | {', '.join('`'+s['id']+'`' for s in ss) or '**none**'} | {pts} | {pts * 100 // total_pts if total_pts else 0}% |")
    w(f"| **Total** | | {len(scored)} scored screens | **{total_pts}** | 100% |\n")
    if weak:
        w(f"⚠ Thin evidence (one scored screen each): {', '.join('`'+o+'`' for o in weak)}. "
          "The LMS objective result then swings on a single answer; add a second check or accept the risk at SME sign-off.\n")

    w("## 6. Tracking (what the LMS receives)\n")
    if scorm == "2004":
        w("| Data | SCORM 2004 element | Set from |\n|---|---|---|")
        w("| Completed | `cmi.completion_status` | all screens viewed |")
        w(f"| Passed / failed | `cmi.success_status` | score ≥ {passing}% (`cmi.scaled_passing_score` {passing/100:.2f}) |")
        w("| Score | `cmi.score.raw / .max / .scaled` | sum of screen points |")
        w("| Per objective | `cmi.objectives.n.id / .score / .success_status` | scored screens' `objective_ids` |")
        w("| Per question | `cmi.interactions.n.*` | each scored screen |")
        w("| Resume | `cmi.suspend_data` (64,000 chars) · `cmi.location` | player state |")
    else:
        w("| Data | SCORM 1.2 element | Set from |\n|---|---|---|")
        w(f"| Status | `cmi.core.lesson_status` (passed / failed / completed / incomplete) | all screens viewed + score vs mastery {passing} |")
        w("| Score | `cmi.core.score.raw / .max / .min` | sum of screen points |")
        w("| Per objective | `cmi.objectives.n.id / .score / .status` | scored screens' `objective_ids` |")
        w("| Per question | `cmi.interactions.n.*` | each scored screen |")
        w(f"| Resume | `cmi.suspend_data` (**4,096 chars**) · `cmi.core.lesson_location` | player state — {len(screens)} screens; check the `SUSPEND_OVERFLOW` lint before build |")
    w("")

    # Interaction types and the resume budget, both derived from the authored blocks.
    rules = activity_rules(p3)
    inter_counts = OrderedDict()
    for s in scored:
        inter_counts.setdefault(INTERACTION_TYPE.get(s["type"], "other"), []).append(s["id"])
    suspend_chars = suspend_estimate(screens, scored)
    suspend_limit = 64000 if scorm == "2004" else 4096
    w("### Interaction records (`cmi.interactions.n.type`)\n")
    w("One interaction record per scored screen, in screen order. `poll` screens are unscored "
      "reflections and are **not** reported as interactions.\n")
    w("| Interaction type | Scored screens | Screen ids |")
    w("|---|---:|---|")
    for itype, ids in sorted(inter_counts.items()):
        shown = ", ".join("`" + i + "`" for i in ids[:8]) + (" …" if len(ids) > 8 else "")
        w(f"| `{itype}` | {len(ids)} | {shown} |")
    unknown = sorted({s["type"] for s in scored if s["type"] not in INTERACTION_TYPE})
    if unknown:
        w(f"\n⚠ Screen types with no mapped interaction type fall back to `other`: "
          f"{', '.join('`'+t+'`' for t in unknown)}. Confirm the mapping with the LMS owner (D9).\n")
    w(f"\nResume payload: ~**{suspend_chars:,} characters** estimated "
      f"({len(screens)} screens × 24 + {len(scored)} scored × 48) against the "
      f"{suspend_limit:,}-character limit of SCORM {'2004' if scorm == '2004' else '1.2'} — "
      f"{'comfortably inside' if suspend_chars < suspend_limit else '⚠ over the limit'}. "
      "Estimate only; the built player's payload is what `lint_course` measures.\n")

    # --- Gamification -------------------------------------------------------
    w("## 7. Gamification (what the record carries, and what it must not)\n")
    w("Rules come from `../00_program/gamification-plan.md` and this pack's Phase 3 activity "
      "table. Points are the only score the LMS sees; nothing here adds a mechanic the "
      "proposal does not contain.\n")
    w("| Mechanic | Planned rule (Phase 3) | Objective | Reported to the LMS as |")
    w("|---|---|---|---|")
    mechanic_rows = 0
    for s in scen:
        row = rule_for(rules, s["id"])
        rule_text = row.get("rules", "—")
        objs = ", ".join(s.get("objective_ids") or []) or "—"
        w(f"| `{s['id']}` {s['type'].replace('_', ' ')} | {rule_text} | {objs} | "
          f"`cmi.interactions.n.*` + {s.get('points') or 0} pts in `cmi.score.raw` |")
        mechanic_rows += 1
    if not mechanic_rows:
        w("| — | no scenario, game or simulation screens in this pack | — | — |")
    w("")
    section_pts = OrderedDict()
    for node, ss in nodes.items():
        pts = sum(s.get("points") or 0 for s in ss)
        if pts:
            section_pts[node] = pts
    w("**Points economy.** " + " · ".join(
        f"`{node}` {pts}" for node, pts in section_pts.items()) +
      f" · **total {total_pts}**, pass {passing}% = {pass_pts}.\n")
    scored_with_feedback = [s for s in scored if has_feedback(s)]
    w(f"**Feedback coverage.** {len(scored_with_feedback)} of {len(scored)} scored screens carry "
      "authored answer feedback in the build block"
      + (f" ({', '.join('`'+s['id']+'`' for s in scored[:12] if s not in scored_with_feedback)} "
         "take it from the Phase 3 activity table or the player default)."
         if len(scored_with_feedback) < len(scored) else "."))
    hits = banned_mechanic_hits(sb + p3 + p4)
    if hits:
        w("\n⚠ Reviewer check — wording that names an excluded mechanic: "
          + ", ".join(f"'{word}' (line {line})" for word, line in hits[:10])
          + ". `gamification-plan.md` excludes leaderboards, public ranking, time pressure, "
            "streaks and badges; confirm each mention is a negation or remove it.\n")
    else:
        w("\nNo excluded mechanic (leaderboard, ranking, streak, badge, countdown, time limit) "
          "is introduced by this pack's storyboard or Phase 3/4 text.\n")

    # --- Scenarios ----------------------------------------------------------
    w("## 8. Scenarios and branching\n")
    w(f"{len(scen)} scenario, game, simulation or adaptive-practice screen(s). Branch structure "
      "is read from the authored build blocks; retry and pass rules from Phase 3.\n")
    if scen:
        w("| Screen | Type | Authored structure | Objective | Pts | Pass / retry rule (Phase 3) |")
        w("|---|---|---|---|---:|---|")
        for s in scen:
            row = rule_for(rules, s["id"])
            pass_rule = row.get("success", "—")
            retry = row.get("failure / retry") or row.get("failure") or "—"
            w(f"| `{s['id']}` | `{s['type']}` | {scenario_shape(s, row)} | "
              f"{', '.join(s.get('objective_ids') or []) or '—'} | {s.get('points') or 0} | "
              f"{pass_rule} · {retry} |")
        w("")
        branchless = [s["id"] for s in scen if s["type"] == "decision_scenario" and not s.get("nodes")]
        if branchless:
            w(f"⚠ Decision screens whose nodes are still authored only in the Phase 3 table "
              f"(no branch JSON yet): {', '.join('`'+b+'`' for b in branchless)}. Phase 4 needs "
              "the node/choice graph before the package can report per-branch interactions.\n")
    else:
        w("None — this pack teaches through checks and explorations only.\n")

    # --- Base checklist -----------------------------------------------------
    plan_path = Path(module_dir) / "storyboard" / "visual-plan.json"
    plan = json.loads(plan_path.read_text()) if plan_path.exists() else {}
    plan_screens = plan.get("screens", [])
    motion_ok = bool(plan_screens) and all(isinstance(s.get("motion"), dict)
                                           for s in plan_screens)
    objectives_missing_evidence = [o for o in keys if not ev.get(o)]
    scored_without_objective = [s["id"] for s in scored if not s.get("objective_ids")]
    scen_without_rule = [s["id"] for s in scen if not rule_for(rules, s["id"])]
    checks = [
        ("Manifest: one organization, one item, one SCO resource", True,
         "§3 manifest sketch; single-SCO rule in the programme structure §2"),
        (f"Pass mark written to the manifest ({passing}%)", bool(scored),
         "`adlcp:masteryscore`" if scorm != "2004" else "`imsss:minNormalizedMeasure`"),
        ("Every objective has at least one scored screen", not objectives_missing_evidence,
         f"{len(keys) - len(objectives_missing_evidence)}/{len(keys)} objectives evidenced"
         + (f"; missing: {', '.join(objectives_missing_evidence)}" if objectives_missing_evidence else "")),
        ("Every scored screen names its objective", not scored_without_objective,
         f"{len(scored)} scored screens"
         + (f"; missing: {', '.join(scored_without_objective)}" if scored_without_objective else "")),
        ("Every scored screen maps to an interaction type", not unknown,
         f"{sum(len(v) for v in inter_counts.values())} interaction records"
         + (f"; unmapped types: {', '.join(unknown)}" if unknown else "")),
        (f"Completion rule set (`{rule}`)", bool(rule), "Phase 4 course settings"),
        ("Resume state fits the SCORM version's suspend_data limit",
         suspend_chars < suspend_limit,
         f"~{suspend_chars:,} chars vs {suspend_limit:,} limit"),
        ("Gamification rules recorded for every scenario screen", not scen_without_rule,
         f"{len(scen) - len(scen_without_rule)}/{len(scen)} scenario screens have a Phase 3 rule row"
         + (f"; missing: {', '.join(scen_without_rule)}" if scen_without_rule else "")),
        ("Answer feedback authored for the scored checks", bool(scored_with_feedback),
         f"{len(scored_with_feedback)}/{len(scored)} scored screens carry feedback in the block"),
        ("No excluded gamification mechanic introduced", not hits,
         "storyboard + Phase 3/4 scanned for leaderboards, ranking, streaks, badges, timers"),
        ("Motion spec present for every screen (reduced-motion safe)", motion_ok,
         f"{sum(1 for s in plan_screens if isinstance(s.get('motion'), dict))}/{len(plan_screens)} "
         "screens carry a `motion` object"),
        ("Thin-evidence objectives flagged for SME sign-off", not weak,
         f"{len(weak)} objective(s) rest on a single scored screen" if weak else "all objectives have ≥2 checks"),
    ]
    w("## 9. Base SCORM structure checklist\n")
    w("Generated evidence for the Phase 4 entry gate. ⚠ rows are open work, not build blockers "
      "unless the note says so.\n")
    w("| Requirement | Status | Evidence |")
    w("|---|---|---|")
    for label, ok, evidence in checks:
        w(f"| {label} | {'✅' if ok else '⚠'} | {evidence} |")
    ok_count = sum(1 for _, ok, _ in checks if ok)
    w(f"\n**{ok_count}/{len(checks)} base requirements met.** Rerun "
      "`tools/build_scorm_structure.py` after any storyboard change, then "
      "`tools/audit_scorm_base.py` for the programme-wide view.\n")

    return {"num": num, "name": name, "title": title, "scorm": scorm, "screens": len(screens),
            "scored": len(scored), "points": total_pts, "pass": passing, "pass_pts": pass_pts,
            "sections": len(nodes), "scen": len(scen), "minutes": minutes, "objectives": len(keys),
            "weak": weak, "zip": zip_name,
            "interaction_types": {k: len(v) for k, v in inter_counts.items()},
            "suspend_chars": suspend_chars, "suspend_limit": suspend_limit,
            "scenario_screens": [{"id": s["id"], "type": s["type"],
                                  "structure": scenario_shape(s, rule_for(rules, s["id"])),
                                  "points": s.get("points") or 0,
                                  "objectives": s.get("objective_ids") or []} for s in scen],
            "feedback_screens": len(scored_with_feedback),
            "banned_mechanic_hits": [{"word": word, "line": line} for word, line in hits],
            "checklist": [{"requirement": label, "ok": bool(ok), "evidence": evidence}
                          for label, ok, evidence in checks],
            "text": "\n".join(L)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('modules', nargs='*', help='Optional module folders; summary always covers all eight.')
    args = parser.parse_args()
    folders = sorted(glob.glob(os.path.join(ROOT, '0[1-8]_*')))
    unknown = set(args.modules) - {os.path.basename(d) for d in folders}
    if unknown:
        parser.error('Unknown module folders: ' + ', '.join(sorted(unknown)))
    results = []
    for d in folders:
        r = build(d)
        text = r.pop('text')
        if not args.modules or os.path.basename(d) in args.modules:
            (Path(d) / 'scorm-structure.md').write_text(text)
        results.append(r)
    (Path(ROOT) / "00_program" / "scorm-structure-summary.json").write_text(json.dumps(results, indent=2))
    for r in results:
        print(r)


if __name__ == "__main__":
    main()
