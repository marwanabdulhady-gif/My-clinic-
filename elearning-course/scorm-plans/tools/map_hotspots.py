#!/usr/bin/env python3
"""Map hotspot boxes onto a produced picture, and check them visually.

A hotspot screen's regions are only right for the picture they were drawn on. When an agent
generates or replaces a picture, the boxes are re-mapped here instead of edited in the
storyboard; ``build_course_spec.py`` applies the map at build time.

  init    <module> <asset-id>   write production/hotspots/<asset-id>.json from the screens that
                                use the picture (region ids, labels, current boxes, image size)
  preview <module>              write production/hotspots/preview.html: every mapped picture with
                                its boxes and labels drawn on top, for the visual check

Map file (pixel boxes on the picture's own size, ``[x, y, w, h]``; circles ``[cx, cy, r]``)::

    {"asset_id": "hs1-img-corridor", "image_size": [1536, 1024],
     "mapped_by": "image agent 2026-10-20", "checked_by": null,
     "screens": {"hs1-404": {
        "regions": {"extinguisher": [812, 402, 96, 210], ...},
        "add_regions": [{"id": "first-aid", "shape": "rect", "coords": [..],
                         "label_html": "<strong>First-aid kit</strong>", "feedback_html": "<p>..</p>"}]}}}

``add_regions`` (extra hotspots the new picture makes possible) are applied only on unscored or
explore-mode screens unless the map carries ``"sme_approved": true`` — new regions on a scored
find-the-hazard screen change the answer key.
"""
from __future__ import annotations

import base64
import html
import json
import sys
from pathlib import Path

PLANS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))


def maps(mdir: Path) -> dict[str, dict]:
    d = mdir / "production" / "hotspots"
    return {p.stem: json.loads(p.read_text()) for p in sorted(d.glob("*.json"))} if d.exists() else {}


def apply(screens: list[dict], mdir: Path) -> list[str]:
    """Apply every map in ``production/hotspots`` to the built screens. Returns notes."""
    notes = []
    for aid, m in maps(mdir).items():
        for s in screens:
            if s.get("image_asset_id") != aid or s["id"] not in m.get("screens", {}):
                continue
            sm = m["screens"][s["id"]]
            boxes = sm.get("regions", {})
            for r in s.get("regions", []):
                if r["id"] in boxes:
                    r["coords"] = boxes[r["id"]]
            missing = [r["id"] for r in s.get("regions", []) if r["id"] not in boxes]
            if missing:
                notes.append(f"{s['id']}: {aid} map has no box for {missing}")
            extra = sm.get("add_regions", [])
            if extra and (not s.get("points") or s.get("mode") == "explore" or m.get("sme_approved")):
                have = {r["id"] for r in s["regions"]}
                s["regions"] += [r for r in extra if r["id"] not in have]
                notes.append(f"{s['id']}: +{len(extra)} regions from the {aid} map")
            elif extra:
                notes.append(f"{s['id']}: {len(extra)} extra regions held — scored screen, needs sme_approved")
    return notes


def init(module: str, aid: str) -> Path:
    mdir = PLANS / module
    spec = json.loads((mdir / "build" / "course-spec.json").read_text())
    from build_course_spec import natural_size
    src = next((a["source"] for a in spec["assets"] if a["id"] == aid), None)
    out = {"asset_id": aid, "image_size": list(natural_size(src)) if src else None,
           "mapped_by": None, "checked_by": None, "sme_approved": False, "screens": {}}
    for s in spec["screens"]:
        if s.get("image_asset_id") == aid and s.get("regions"):
            out["screens"][s["id"]] = {
                "mode": s.get("mode"), "scored": bool(s.get("points")),
                "labels": {r["id"]: html.unescape(r.get("label_html", r["id"])) for r in s["regions"]},
                "regions": {r["id"]: r.get("coords") for r in s["regions"]}, "add_regions": []}
    p = mdir / "production" / "hotspots" / f"{aid}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, ensure_ascii=False, indent=1))
    return p


def preview(module: str) -> Path:
    mdir = PLANS / module
    from build_course_spec import find_asset, data_uri
    parts = []
    for aid, m in maps(mdir).items():
        f = find_asset(aid, mdir)
        if not f:
            parts.append(f"<h2>{aid}</h2><p>No picture yet.</p>")
            continue
        w, h = m.get("image_size") or (960, 540)
        for sid, sm in m["screens"].items():
            boxes = list(sm.get("regions", {}).items()) + [(r["id"], r["coords"]) for r in sm.get("add_regions", [])]
            shapes = []
            for rid, c in boxes:
                if not c:
                    continue
                if len(c) == 3:
                    shapes.append(f'<circle cx="{c[0]}" cy="{c[1]}" r="{c[2]}"/><text x="{c[0]}" y="{c[1]}">{rid}</text>')
                else:
                    shapes.append(f'<rect x="{c[0]}" y="{c[1]}" width="{c[2]}" height="{c[3]}"/>'
                                  f'<text x="{c[0] + 6}" y="{c[1] + 22}">{rid}</text>')
            parts.append(f'<h2>{sid} · {aid}</h2><svg viewBox="0 0 {w} {h}"><image href="{data_uri(f)}" width="{w}" height="{h}"/>'
                         f'<g>{"".join(shapes)}</g></svg>')
    page = ("<!doctype html><meta charset=utf-8><title>Hotspot check</title><style>body{font-family:Montserrat,Arial;margin:24px;background:#F4F7FA;color:#003867}"
            "svg{width:100%;max-width:1100px;background:#fff;border-radius:12px}rect,circle{fill:rgba(0,140,153,.18);stroke:#008C99;stroke-width:4}"
            "text{font:600 22px Montserrat,Arial;fill:#003867;paint-order:stroke;stroke:#fff;stroke-width:5}</style>"
            "<h1>Hotspot map check</h1><p>Every box must sit on its object. Fix the map JSON, not the storyboard.</p>" + "".join(parts))
    p = mdir / "production" / "hotspots" / "preview.html"
    p.write_text(page)
    return p


if __name__ == "__main__":
    cmd, module, *rest = sys.argv[1:]
    print(init(module, rest[0]) if cmd == "init" else preview(module))
