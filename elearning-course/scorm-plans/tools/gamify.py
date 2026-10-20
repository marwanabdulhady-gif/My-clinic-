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


def _add(s: dict, field: str, value: int) -> None:
    s.setdefault(field, [])
    s[field] = [a for a in s[field] if a.get("var") != "xp"] + [{"var": "xp", "op": "add", "value": value}]


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

    sections = []
    for s in screens:
        if s.get("section") and s["section"] not in sections:
            sections.append(s["section"])
    missions = [t for t in sections if t.split("·")[-1].strip().lower() not in OPEN_CLOSE]
    ranks = g["ranks"]
    levels = [{"name": r, "min_points": int(round(total * t))} for r, t in zip(ranks, g["rank_thresholds"])]
    clean = lambda t: t.split("·")[-1].strip()
    items = " · ".join(f"<strong>{i + 1}</strong> {clean(t)}" for i, t in enumerate(missions))
    brief = {
        "type": "content_slide", "id": f"{screens[0]['id'].split('-')[0]}-00m", "title": g["challenge"],
        "layout": "text_media" if hero_asset else "text",
        "body_html": (f"<h3>{g['hook']}</h3>"
                      f"<p class=\"mc-missions\"><strong>{len(missions)} missions:</strong> {items}</p>"
                      f"<p class=\"mc-xp-rules\"><strong>Earn XP:</strong> +{xp['scored_correct']} for each activity you get right · "
                      f"+{xp['check_correct']} for each quick check · +{xp['explore']} for each screen you explore. "
                      f"<strong>Ranks:</strong> {' → '.join(ranks)}.</p>"
                      "<p class=\"mc-note\">XP is just for you: it never counts towards your pass mark.</p>"),
        "points": 0, "objective_ids": [], "notes": "Gamification (tools/gamify.py, decision D18).",
    }
    if hero_asset:
        brief["media_asset_id"] = hero_asset
        brief["media_alt"] = f"Illustration for the {g['challenge'].lower()}."
    at = next((i + 1 for i, s in enumerate(screens) if s["id"] == picker_id), 1)
    brief["section"] = screens[at - 1].get("section")
    brief["node_id"] = screens[at - 1].get("node_id")
    screens = screens[:at] + [brief] + screens[at:]
    for s in screens:  # the picker continues to the brief
        if s["id"] == picker_id:
            for c in s.get("choices", []):
                c["goto_screen_id"] = brief["id"]
            s["default_goto"] = brief["id"]
    last = screens[-1]
    last["body_html"] = (last.get("body_html") or "") + (
        "<p class=\"mc-xp-final\"><strong>You finished with {{xp}} XP.</strong> "
        "Your rank is at the top of the screen.</p>")
    course = {"points_var": "xp", "levels": levels,
              "mission_titles": {t: f"Mission {i + 1} · {clean(t)}" for i, t in enumerate(missions)}}
    return screens, course, [f"gamification: {len(missions)} missions, max {total} XP, ranks at "
                             + "/".join(str(l["min_points"]) for l in levels)]
