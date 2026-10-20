#!/usr/bin/env python3
"""Add the programme gamification system to a module's built screens (decision D18).

Driven by ``00_program/gamification.json``; applied by ``build_course_spec.py`` after the
personalisation layer. What it adds, per package:

  * a **challenge**: a "Can you …?" hook, shown on a mission-brief screen after the role picker
  * **missions**: every teaching section becomes "Mission n · <title>" in the menu
  * **XP**: +10 for each scored activity answered correctly, +5 for each quick check,
    +2 for each screen you explore — a course variable shown in the header (★ n XP)
  * **ranks**: four themed ranks per package, unlocked at 0 / 30 / 60 / 85 % of the package's
    maximum XP, shown in the header (◆ Safety Ally)
  * a close line: "You finished with n XP"

XP lives only in the course variables (resume data). It is never part of the score, the pass mark
or the LMS record, so nothing scored changes (``personalise.py`` guards still hold). No timers,
no leaderboards, no lives outside the games that already have them.
"""
from __future__ import annotations

import json
from pathlib import Path

PLANS = Path(__file__).resolve().parents[1]
QUIZ = {"mcq", "true_false", "fill_blank", "drag_drop", "hotspot", "matching", "sorting", "simulation",
        "decision_scenario", "game", "escape_room", "adaptive_practice", "labeled_diagram"}
EXPLORE = {"accordion", "tabs", "flashcards", "timeline", "exploration", "poll", "image_compare",
           "worked_example", "hotspot", "labeled_diagram"}
OPEN_CLOSE = {"welcome", "close", "capstone & completion", "regulations & close", "practice & close"}


def config(module: str) -> dict | None:
    p = PLANS / "00_program" / "gamification.json"
    if not p.exists():
        return None
    g = json.loads(p.read_text())
    m = g["modules"].get(module[:2])
    return {**g, **m} if m else None


def _act(s: dict, field: str, var: str, value, op: str = "add") -> None:
    s.setdefault(field, [])
    s[field] = [a for a in s[field] if a.get("var") != var] + [{"var": var, "op": op, "value": value}]


def _add(s: dict, field: str, value: int) -> None:
    _act(s, field, "xp", value)


PERFORM = {"decision_scenario", "game", "escape_room", "simulation"}
WHO = {"noor": ("Noor", "char-noor-explaining"), "omar": ("Dr. Omar", "char-omar-explaining")}


def _inspiration(screens: list[dict], g: dict) -> tuple[list[dict], list[str]]:
    """The portfolio upgrades (inspiration-portfolio-review.md): outcome meter, outcome-first
    feedback with replies from the other side, and Ask Noor / Ask Dr. Omar before decisions."""
    notes = []
    target, replies, hints = g.get("outcome_target", "the patient"), g.get("replies", {}), g.get("hints", {})
    for s in screens:
        if (s.get("points") or 0) and s["type"] in PERFORM:  # the meter moves with real performance
            _act(s, "on_correct", "meter", 1)
            _act(s, "on_wrong", "meter", -1)
        if s["type"] != "decision_scenario":
            continue
        for n in s.get("nodes", []):
            for c in n["choices"]:
                if c.get("_framed"):
                    continue
                good = (c.get("score_delta") or 0) > 0
                reply = replies.get(s["id"], {}).get(n["id"], {}).get(c["id"])
                head = (f"<p><em>{reply}</em></p>" if reply else "") + (
                    f"<p><strong>{'✓ Better for ' if good else '⚠ Risk for '}{target}.</strong></p>")
                c["feedback_html"] = head + c["feedback_html"]
        if s["id"] in hints:
            s["on_enter"] = [a for a in s.get("on_enter", []) if a.get("var") != "hint"] + [{"var": "hint", "op": "set", "value": 0}]
    out = []
    for s in screens:
        h = hints.get(s["id"])
        if h:
            name, pose = WHO[h["who"]]
            ask, tip = f"{s['id']}-ask", f"{s['id']}-hint"
            base = {"section": s.get("section"), "node_id": s.get("node_id"), "points": 0, "objective_ids": [],
                    "notes": "Ask-a-companion hint (tools/gamify.py, inspiration review #2)."}
            out.append({**base, "type": "branching", "id": ask, "title": s["title"],
                        "prompt_html": f"<p><strong>Next: a decision.</strong> Want a hint from {name} first? It's a nudge, not the answer.</p>",
                        "choices": [{"id": "ask", "text_html": f"<strong>Ask {name}</strong>", "goto_screen_id": tip,
                                     "set_vars": [{"var": "hint", "op": "set", "value": 1}]},
                                    {"id": "go", "text_html": "<strong>I'm ready</strong>", "goto_screen_id": s["id"],
                                     "set_vars": [{"var": "hint", "op": "set", "value": 0}]}],
                        "default_goto": s["id"]})
            out.append({**base, "type": "content_slide", "id": tip, "title": f"{name}'s hint", "layout": "text_media",
                        "body_html": f"<p><strong>{name}:</strong> “{h['text']}”</p>",
                        "media_asset_id": pose, "media_alt": f"{name}, the course guide.",
                        "visible_if": {"var": "hint", "cmp": "==", "value": 1}})
            notes.append(f"ask-{h['who']} before {s['id']}")
        out.append(s)
    return out, notes


def apply(screens: list[dict], module: str, picker_id: str | None, hero_asset: str | None) -> tuple[list[dict], dict, list[str]]:
    """Return (screens, course fields, notes)."""
    g = config(module)
    if not g:
        return screens, {}, []
    xp = g["xp"]
    total = 0
    for s in screens:
        pts = s.get("points") or 0
        if pts and s["type"] in QUIZ:
            _add(s, "on_correct", xp["scored_correct"]); total += xp["scored_correct"]
        elif s["type"] in QUIZ and not pts and s["type"] not in {"hotspot", "labeled_diagram"}:
            _add(s, "on_correct", xp["check_correct"]); total += xp["check_correct"]
            if not s.get("evidence_screen_ids"):  # a quick check rehearses the screen before it
                i = screens.index(s)
                s["evidence_screen_ids"] = [screens[i - 1]["id"]] if i else []
        elif s["type"] in EXPLORE and not s.get("visible_if"):
            _add(s, "on_enter", xp["explore"]); total += xp["explore"]
    # one role-tip variant is visible per learner; count it once
    tips = {s["id"].rsplit("-", 1)[0] for s in screens if s.get("visible_if") and s["type"] in EXPLORE}
    for s in screens:
        if s.get("visible_if") and s["type"] in EXPLORE:
            _add(s, "on_enter", xp["explore"])
    total += xp["explore"] * len(tips)

    screens, inotes = _inspiration(screens, g)

    sections = []
    for s in screens:
        if s.get("section") and s["section"] not in sections:
            sections.append(s["section"])
    missions = [t for t in sections if t.split("·")[-1].strip().lower() not in OPEN_CLOSE]
    ranks = g["ranks"]
    levels = [{"name": r, "min_points": int(round(total * t))} for r, t in zip(ranks, g["rank_thresholds"])]
    clean = lambda t: t.split("·")[-1].strip()
    shift = g.get("shift") or []
    when = lambda i: f"{shift[i]} " if i < len(shift) else ""
    items = " · ".join(f"<strong>{i + 1}</strong> {when(i)}{clean(t)}" for i, t in enumerate(missions))
    brief = {
        "type": "content_slide", "id": f"{screens[0]['id'].split('-')[0]}-00m", "title": g["challenge"],
        "layout": "text_media" if hero_asset else "text",
        "body_html": (f"<h3>{g['hook']}</h3>"
                      f"<p class=\"mc-missions\"><strong>{len(missions)} missions:</strong> {items}</p>"
                      f"<p class=\"mc-xp-rules\"><strong>Earn XP:</strong> +{xp['scored_correct']} for each activity you get right · "
                      f"+{xp['check_correct']} for each quick check · +{xp['explore']} for each screen you explore. "
                      f"<strong>Ranks:</strong> {' → '.join(ranks)}.</p>"
                      f"<p><strong>{g.get('meter', 'Patient safety')}</strong> (the dots at the top) goes up with each good decision "
                      "and down with each risky one. Ask Noor or Dr. Omar for a hint before a big decision.</p>"
                      "<p class=\"mc-note\">XP is just for you: it never counts towards your pass mark.</p>"),
        "points": 0, "objective_ids": [], "notes": "Gamification (tools/gamify.py, decision D18).",
    }
    if hero_asset:
        brief["media_asset_id"] = hero_asset
        brief["media_alt"] = f"Illustration for the {g['challenge'].lower()}."
    at = next((i + 1 for i, s in enumerate(screens) if s["id"] == picker_id), 1)
    brief["section"] = screens[at - 1].get("section")
    brief["node_id"] = screens[at - 1].get("node_id")
    day = []
    if shift:  # a day-at-the-clinic spine (inspiration review #4)
        day = [{"type": "timeline", "id": f"{brief['id'][:-1]}t", "title": g.get("shift_title", "Your day"),
                "prompt_html": "<p>One shift, six missions. Open each time to see what is coming.</p>",
                "events": [{"date": shift[i], "title": f"Mission {i + 1} · {clean(t)}",
                            "body_html": f"<p>{(g.get('shift_notes') or [''] * len(missions))[i]}</p>"}
                           for i, t in enumerate(missions) if i < len(shift)],
                "section": screens[at - 1].get("section"), "node_id": screens[at - 1].get("node_id"),
                "points": 0, "objective_ids": [], "notes": "Day-at-the-clinic spine (tools/gamify.py)."}]
    screens = screens[:at] + [brief] + day + screens[at:]
    for s in screens:  # the picker continues to the brief
        if s["id"] == picker_id:
            for c in s.get("choices", []):
                c["goto_screen_id"] = brief["id"]
            s["default_goto"] = brief["id"]
    titles = {t: f"Mission {i + 1} · {when(i)}{clean(t)}" for i, t in enumerate(missions)}
    sec_of = {x["id"]: x.get("section") for x in screens}
    for x in screens:  # revisit map on the results screen (inspiration review #5)
        if x["type"] == "results_breakdown":
            for sec in x.get("sections", []):
                by_id = {y["id"]: y for y in screens}
                taught = [e for i in sec.get("screen_ids", []) for e in (by_id.get(i, {}).get("evidence_screen_ids") or [i])]
                where = list(dict.fromkeys(titles[sec_of[i]] for i in taught if sec_of.get(i) in titles))[:2]
                if where and "Open " not in (sec.get("advice_html") or ""):
                    sec["advice_html"] = (sec.get("advice_html") or "") + (
                        "<p><strong>Open " + " and ".join(where) + "</strong> from the menu (☰) to revisit it.</p>")
    last = screens[-1]
    last["body_html"] = (last.get("body_html") or "") + (
        "<p class=\"mc-xp-final\"><strong>You finished with {{xp}} XP.</strong> "
        "Your rank is at the top of the screen.</p>")
    course = {"points_var": "xp", "levels": levels, "lives_var": "meter", "max_lives": 5,
              "extra_vars": [{"name": "meter", "type": "number", "default": 3},
                             {"name": "hint", "type": "number", "default": 0}],
              "meter_label": g.get("meter", "Patient safety"),
              "mission_titles": titles}
    return screens, course, inotes + [f"gamification: {len(missions)} missions, max {total} XP, ranks at "
                             + "/".join(str(l["min_points"]) for l in levels)]
