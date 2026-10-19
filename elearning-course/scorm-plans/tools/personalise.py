#!/usr/bin/env python3
"""Apply a module's personalisation and interactivity layer to its built screens.

The storyboard is the client-reviewed structure (ids, order, scored screens, points,
objectives). This layer sits on top of it and may only add **unscored** experience:

  * ``variables``      course variables (``role``, ``role_label``)
  * ``insert_after``   new screens after an existing id: the role picker (``branching``),
                       role tips (``visible_if`` on ``role``), formative checks (``points: 0``),
                       explorations, the 04 results-by-objective screen
  * ``convert``        replace an **unscored, passive** screen by an interactive one that keeps
                       its id, section and node (content slide → flashcards, explore hotspot …)
  * ``append_html``    add personalised lines (``{{role_label}}``) to an existing screen's body

Guards (the build stops if one fails): nothing scored is added, removed or changed; a converted
screen must have been unscored; ids are unique; the last screen is never hidden; a step that
needs a picture not made yet (``requires_asset``) is held back until the file exists.

Source: ``<module>/production/personalisation.json``. Role groups: ``00_program/roles.json``.
"""
from __future__ import annotations

import json
from pathlib import Path

PLANS = Path(__file__).resolve().parents[1]
SCORED_KEYS = ("points", "objective_ids")


def layer(mdir: Path) -> dict | None:
    p = mdir / "production" / "personalisation.json"
    return json.loads(p.read_text()) if p.exists() else None


def picker(module: str, after_id: str, next_id: str) -> dict:
    """The role picker screen for a module, built from 00_program/roles.json."""
    roles = json.loads((PLANS / "00_program" / "roles.json").read_text())
    cfg = roles["packages"][module[:2]]
    return {
        "type": "branching", "id": cfg["picker_id"], "title": "Make it yours",
        "prompt_html": "<p><strong>Which best describes your role?</strong></p>"
                       "<p>We'll add tips for your work. Every scored activity is the same for everyone.</p>",
        "choices": [{"id": g["id"], "text_html": f"<strong>{g['label']}</strong><br><small>{g['who']}</small>",
                     "goto_screen_id": next_id,
                     "set_vars": [{"var": "role", "op": "set", "value": g["id"]},
                                  {"var": "role_label", "op": "set", "value": g["role_label"]}]}
                    for g in cfg["groups"]] + [
            {"id": "all", "text_html": "<strong>Show me every role's tips</strong>", "goto_screen_id": next_id,
             "set_vars": [{"var": "role", "op": "set", "value": "all"},
                          {"var": "role_label", "op": "set", "value": "team member"}]}],
        "default_goto": next_id, "points": 0, "objective_ids": [],
    }


def role_tip(base: dict, groups: list[dict]) -> list[dict]:
    """One tip → one screen per role group (visible_if) + one 'all roles' tabs screen."""
    out = []
    for g in groups:
        out.append({"type": "accordion", "id": f"{base['id']}-{g['role']}", "title": base["title"],
                    "prompt_html": f"<p><strong>For your role.</strong> {base.get('lead', '')}</p>",
                    "items": g["items"], "visible_if": {"var": "role", "cmp": "==", "value": g["role"]},
                    "points": 0, "objective_ids": []})
    out.append({"type": "tabs", "id": f"{base['id']}-all", "title": base["title"],
                "prompt_html": f"<p>{base.get('lead', '')} Pick a role to compare.</p>",
                "tabs": [{"label": g["label"], "body_html": "".join(
                    f"<h4>{i['title']}</h4>{i['body_html']}" for i in g["items"])} for g in groups],
                "visible_if": {"var": "role", "cmp": "==", "value": "all"}, "points": 0, "objective_ids": []})
    return out


def apply(screens: list[dict], module: str, mdir: Path, asset_exists) -> tuple[list[dict], list[dict], list[str]]:
    """Return (screens, variables, notes). ``asset_exists(aid)`` says whether a picture is made."""
    L = layer(mdir)
    if not L:
        return screens, [], []
    notes: list[str] = []
    before = {s["id"]: (s.get("points") or 0, sorted(s.get("objective_ids") or [])) for s in screens}
    by_id = {s["id"]: i for i, s in enumerate(screens)}

    def ready(step: dict) -> bool:
        need = step.get("requires_asset")
        if need and not asset_exists(need):
            notes.append(f"held back until {need} exists: {step.get('id') or step.get('screen', {}).get('id')}")
            return False
        return True

    for sid, new in L.get("convert", {}).items():
        if not ready(new):
            continue
        old = screens[by_id[sid]]
        if old.get("points"):
            raise SystemExit(f"{module}: personalisation may not convert scored screen {sid}")
        keep = {k: old[k] for k in ("id", "section", "node_id", "narration_text", "notes") if k in old}
        screens[by_id[sid]] = {**{k: v for k, v in new.items() if k not in ("requires_asset", "brief")}, **keep,
                               "points": 0, "objective_ids": []}
        notes.append(f"{sid}: {old['type']} → {new['type']}")

    for sid, extra in L.get("append_html", {}).items():
        s = screens[by_id[sid]]
        field = "body_html" if "body_html" in s or s["type"] in {"summary", "content_slide", "results_breakdown"} else "prompt_html"
        s[field] = (s.get(field) or "") + extra

    out: list[dict] = []
    for s in screens:
        out.append(s)
        for step in L.get("insert_after", {}).get(s["id"], []):
            if not ready(step):
                continue
            kind = step.get("kind", "screen")
            if kind == "role_picker":
                nxt = screens[by_id[s["id"]] + 1]["id"]
                new = [picker(module, s["id"], nxt)]
            elif kind == "role_tip":
                new = role_tip(step, step["groups"])
            else:
                new = [{k: v for k, v in step["screen"].items()}]
            for n in new:
                n.setdefault("section", s.get("section"))
                n.setdefault("node_id", s.get("node_id"))
                n["points"], n["objective_ids"] = 0, []
                n.setdefault("notes", "Personalisation layer (production/personalisation.json) — unscored; SME confirms wording.")
            out += new
            notes.append(f"+{len(new)} after {s['id']} ({kind})")

    for i, s in enumerate(out):  # the picker continues to whatever now follows it
        if s["type"] == "branching" and s.get("notes", "").startswith("Personalisation layer"):
            for c in s["choices"]:
                c["goto_screen_id"] = out[i + 1]["id"]
            s["default_goto"] = out[i + 1]["id"]
    ids = [s["id"] for s in out]
    if len(ids) != len(set(ids)):
        raise SystemExit(f"{module}: duplicate screen ids after personalisation")
    if out[-1].get("visible_if"):
        raise SystemExit(f"{module}: the last screen may not be hidden")
    after = {s["id"]: (s.get("points") or 0, sorted(s.get("objective_ids") or [])) for s in out if s["id"] in before}
    changed = [k for k in before if before[k] != after.get(k) and before[k][0]]
    if changed or any((s.get("points") or 0) for s in out if s["id"] not in before):
        raise SystemExit(f"{module}: personalisation changed scoring on {changed}")
    variables = L.get("variables", [{"name": "role", "type": "text", "default": "all"},
                                     {"name": "role_label", "type": "text", "default": "team member"}])
    return out, variables, notes
