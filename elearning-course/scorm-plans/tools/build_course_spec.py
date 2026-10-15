#!/usr/bin/env python3
"""Turn a module's storyboard build blocks into an edumints CourseSpec (Phase 4 draft).

Inputs (all in the repo, nothing invented):
  * ``<module>/storyboard/storyboard.md`` — one JSON build block per screen (the Phase 4 source)
  * ``<module>/phase-4-build.md``          — course settings (title, SCORM version, tracking)
  * the storyboard's section and objective tables — outline and ``cmi.objectives``
  * asset files: the module's ``storyboard/assets/``, ``00_program/brand/assets/`` and
    ``00_program/characters/assets|previews/``

Asset placeholders written as ``"<asset-id>"`` in ``*_asset_id`` fields are resolved to files.
An asset that does not exist yet (not generated, not captured, not supplied by My Clinic) becomes
a branded **PENDING card** SVG that names the asset id and its gate, so a draft build never
shows invented imagery. Narration audio placeholders are dropped (no shipping voice until D10);
``narration_text`` stays as captions/transcript.

Companions: where a screen's ``notes`` name a ``char-noor-*`` / ``char-omar-*`` pose and the
screen type has a free media slot (title background is never used), the pose is placed in that
slot. Otherwise the companion stays in ``notes`` for the Phase 4 developer.

Output: ``<module>/build/course-spec.json`` and ``<module>/build/asset-map.json``.

    python3 elearning-course/scorm-plans/tools/build_course_spec.py 03_hr-employee-induction
"""
from __future__ import annotations

import base64
import html
import json
import re
import sys
from pathlib import Path

PLANS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_scorm_structure import blocks, table_rows  # noqa: E402

BRAND = PLANS / "00_program" / "brand" / "assets"
CHARS = PLANS / "00_program" / "characters"
MIME = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".svg": "image/svg+xml"}
PH = re.compile(r"^<([a-z0-9][a-z0-9-]*)>$")
CHAR_RE = re.compile(r"\bchar-(?:noor|omar)-[a-z]+(?:-[a-z]+)?\b")
STORYBOARD_ONLY = {"section_letter", "asset_status", "narration_script_id"}


def course_settings(p4: str) -> dict:
    m = re.search(r"```json\s*\n(\{.*?\})\s*```", p4, re.S)
    return json.loads(m.group(1)) if m else {}


def find_asset(aid: str, module_dir: Path) -> Path | None:
    cands = []
    for ext in (".svg", ".png", ".jpg"):
        cands.append(module_dir / "storyboard" / "assets" / f"{aid}{ext}")
    if aid.startswith("brand-"):
        cands.append(BRAND / f"{aid[len('brand-'):]}.png")
    if aid.startswith("char-"):
        cands += [CHARS / "assets" / f"{aid}.png", CHARS / "previews" / f"{aid}.jpg"]
    cands.append(BRAND / f"{aid}.png")
    return next((c for c in cands if c.exists()), None)


def pending_svg(aid: str, reason: str, w: int = 960, h: int = 540) -> bytes:
    a, r = html.escape(aid), html.escape(reason)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Pending asset {a}">
<rect width="{w}" height="{h}" fill="#F4F7FA"/>
<rect x="12" y="12" width="{w-24}" height="{h-24}" fill="none" stroke="#C0CED9" stroke-width="3" stroke-dasharray="14 10" rx="16"/>
<text x="{w/2}" y="{h/2-28}" text-anchor="middle" font-family="Montserrat, Arial, sans-serif" font-size="30" font-weight="700" fill="#003867">&#9888; PENDING ASSET</text>
<text x="{w/2}" y="{h/2+14}" text-anchor="middle" font-family="Montserrat, Arial, sans-serif" font-size="24" fill="#003867">{a}</text>
<text x="{w/2}" y="{h/2+52}" text-anchor="middle" font-family="Montserrat, Arial, sans-serif" font-size="18" fill="#5B6B7B">{r}</text>
</svg>""".encode()


def gate_for(aid: str) -> str:
    if "oracle" in aid:
        return "Test-account capture after B8"
    if aid.startswith("ehr-shot") or "ehr-shot" in aid:
        return "DPO-approved test-environment capture (B2/D6)"
    if "leaders" in aid:
        return "Client photo with consent, or role tile (D5/B6)"
    if aid.startswith("char-"):
        return "Full-size companion PNG from Canva (G6)"
    return "Still to produce and approve (visual-and-motion-agent-brief.md)"


def natural_size(src: str) -> tuple[int, int]:
    """Pixel size of a data-URI image (PNG/JPEG header or SVG width/height/viewBox)."""
    import struct
    head, b64 = src.split(",", 1)
    raw = base64.b64decode(b64)
    if "png" in head:
        return struct.unpack(">II", raw[16:24])
    if "svg" in head:
        t = raw[:600].decode("utf-8", "ignore")
        m = re.search(r'width="([\d.]+)"[^>]*height="([\d.]+)"', t)
        if m:
            return int(float(m.group(1))), int(float(m.group(2)))
        m = re.search(r'viewBox="[\d.]+ [\d.]+ ([\d.]+) ([\d.]+)"', t)
        if m:
            return int(float(m.group(1))), int(float(m.group(2)))
    if "jpeg" in head:
        i = 2
        while i < len(raw):
            if raw[i] != 0xFF:
                break
            marker, ln = raw[i + 1], struct.unpack(">H", raw[i + 2:i + 4])[0]
            if marker in (0xC0, 0xC2):
                h, w = struct.unpack(">HH", raw[i + 5:i + 9])
                return w, h
            i += 2 + ln
    return 960, 540


def explore_hotspot_css(screens: list[dict], assets: dict[str, dict]) -> str:
    """Position explore-mode hotspot regions with CSS percentages.

    Workaround for edumints 4bbf459: ``bindHotspot`` returns before ``place()`` for
    ``hs-explore`` hotspots, so their regions are never positioned at runtime (they stack in
    the corner). Percentages of the image's natural size give the same placement, scale with
    the stage, and need no script. Remove once the compiler places explore regions itself.
    """
    rules = []
    for s in screens:
        if s.get("type") != "hotspot" or s.get("mode") != "explore":
            continue
        aid = s.get("image_asset_id")
        if aid not in assets:
            continue
        w, h = natural_size(assets[aid]["source"])
        for r in s.get("regions", []):
            c = [float(x) for x in r.get("coords", [])]
            if r.get("shape") == "circle" and len(c) == 3:
                x, y, wd, ht = c[0] - c[2], c[1] - c[2], 2 * c[2], 2 * c[2]
                extra = "border-radius:50%;"
            elif len(c) == 4:
                x, y, wd, ht = c
                extra = ""
            else:
                continue
            sel = f'.screen[data-screen-id="{s["id"]}"] .hs-explore .hotspot-region[data-region="{r["id"]}"]'
            rules.append(f"{sel}{{left:{x / w * 100:.3f}%;top:{y / h * 100:.3f}%;"
                         f"width:{wd / w * 100:.3f}%;height:{ht / h * 100:.3f}%;{extra}}}")
    if rules:
        rules.insert(0, ".hs-explore .hotspot-stage .hotspot-img{display:block;width:100%;height:auto}")
    return "\n".join(rules)


def data_uri(path: Path) -> str:
    return f"data:{MIME[path.suffix.lower()]};base64," + base64.b64encode(path.read_bytes()).decode()


def build(module: str) -> dict:
    mdir = PLANS / module
    sb = (mdir / "storyboard" / "storyboard.md").read_text()
    p4 = (mdir / "phase-4-build.md").read_text()
    settings = course_settings(p4)
    screens = blocks(sb)
    if not screens:
        raise SystemExit(f"{module}: no build blocks")
    prod = mdir / "build" / "screens.json"
    if prod.exists():
        # Production screens authored from the cards (modules whose storyboard blocks carry
        # review metadata only). They must keep the storyboard's ids, order, types, node_ids,
        # points and objective_ids — the structure the client reviewed.
        authored = json.loads(prod.read_text())
        key = lambda j: (j["id"], j["type"], j.get("node_id"), j.get("points") or 0,
                         sorted(j.get("objective_ids") or []))
        diffs = [(a["id"], b["id"]) for a, b in zip(screens, authored) if key(a) != key(b)]
        if len(authored) != len(screens) or diffs:
            raise SystemExit(f"{module}: build/screens.json drifts from the storyboard: "
                             f"{len(authored)} vs {len(screens)} screens; first diffs {diffs[:5]}")
        screens = authored
    prefix = screens[0]["id"].split("-")[0]

    assets: dict[str, dict] = {}
    report: dict[str, dict] = {}

    def use(aid: str) -> str:
        if aid in assets:
            return aid
        f = find_asset(aid, mdir)
        if f is not None:
            assets[aid] = {"id": aid, "filename": f"{aid}{f.suffix.lower()}", "source": data_uri(f)}
            report[aid] = {"status": "file", "path": str(f.relative_to(PLANS)),
                           "interim": "previews" in f.parts or "assets" in f.parts and f.parent.parent.name == "characters"}
        else:
            reason = gate_for(aid)
            src = "data:image/svg+xml;base64," + base64.b64encode(pending_svg(aid, reason)).decode()
            assets[aid] = {"id": aid, "filename": f"{aid}.svg", "source": src}
            report[aid] = {"status": "PENDING", "gate": reason}
        return aid

    def walk(o, key=""):
        if isinstance(o, dict):
            out = {}
            for k, v in o.items():
                if k in STORYBOARD_ONLY:
                    continue
                if isinstance(v, str) and PH.match(v) and (k.endswith("asset_id") or k == "asset_id"):
                    aid = PH.match(v).group(1)
                    if "-aud-" in aid:
                        report.setdefault("_audio", {"status": "PENDING", "gate": "Voices D10", "count": 0})
                        report["_audio"]["count"] += 1
                        continue
                    out[k] = use(aid)
                else:
                    out[k] = walk(v, k)
            return out
        if isinstance(o, list):
            return [walk(x, key) for x in o]
        return o

    def who(pose: str) -> str:
        return "Noor" if "noor" in pose else "Dr. Omar"

    def host_html(pose: str) -> str:
        neutral = "char-noor-avatar-neutral" if "noor" in pose else "char-omar-avatar-neutral"
        avatar = pose if "avatar" in pose and find_asset(pose, mdir) else neutral
        role = "Noor · Safety liaison" if "noor" in pose else "Dr. Omar · Family physician"
        cls = "noor" if "noor" in pose else "omar"
        return f'<div class="mc-host {cls}">{{{{asset:{use(avatar)}}}}}<span>{role}</span></div>'

    built = []
    placed = 0
    for s in screens:
        s = walk(s)
        poses = list(dict.fromkeys(CHAR_RE.findall(s.get("notes") or "")))
        t = s["type"]
        if t == "title_slide":
            s.pop("background_asset_id", None)  # the skin draws the L1 navy title
            welcome = [p for p in poses if "welcome" in p] or poses[:2]
            if welcome:
                cards = "".join(
                    f'<div class="mc-guide {"noor" if "noor" in p else "omar"}">{{{{asset:{use(p)}}}}}<span>{who(p)}</span></div>'
                    for p in welcome[:2])
                s["body_html"] = (s.get("body_html") or "") + f'<div class="mc-guides">{cards}</div>'
                placed += 1
        elif poses and t == "content_slide" and not s.get("media_asset_id") and not s.get("blocks"):
            s["layout"] = "text_media"
            s["media_asset_id"] = use(poses[0])
            s["media_alt"] = f"{who(poses[0])}, the course guide."
            placed += 1
        elif poses and t in {"decision_scenario", "game", "escape_room"} and s.get("intro_html") is not None:
            s["intro_html"] = host_html(poses[0]) + s["intro_html"]
            placed += 1
        built.append(s)

    outline = []
    for cells in table_rows(sb, rf"{prefix}-s[A-Z0-9]+"):
        nid = cells[0].strip("`")
        if nid not in {n["id"] for n in outline}:
            outline.append({"id": nid, "kind": "section", "title": re.sub(r"^[A-Z0-9]+ · ", "", cells[1]) or nid,
                            "unlock_rule": "free"})
    used_nodes = {s.get("node_id") for s in built}
    outline = [n for n in outline if n["id"] in used_nodes]
    objectives = []
    for cells in table_rows(sb, rf"{prefix}-o\d+"):
        oid = cells[0].strip("`")
        if oid not in {o["id"] for o in objectives}:
            objectives.append({"id": oid, "description": cells[1]})

    readme = (mdir / "README.md").read_text()
    seat = re.search(r"Seat time \| ~?(\d+)", readme)
    use("brand-logo-horizontal-navy")
    fonts = PLANS / "00_program" / "brand" / "fonts"
    for w in (400, 600, 700):
        f = fonts / f"montserrat-latin-{w}-normal.woff2"
        assets[f"font-montserrat-{w}"] = {"id": f"font-montserrat-{w}", "filename": f.name,
                                          "source": "data:font/woff2;base64," + base64.b64encode(f.read_bytes()).decode()}
    spec = {
        "schema_version": "1.0",
        "title": settings.get("title"),
        "description": settings.get("description", ""),
        "scorm_version": settings.get("scorm_version", "1.2"),
        "language": "en",
        "theme": "__BRAND__",
        "theme_mode": "light",
        "tracking": settings.get("tracking", {"completion_rule": "viewed_all_and_passed", "passing_score": 80}),
        "layout_mode": settings.get("layout_mode", "stage"),
        "metadata": {"description": settings.get("description") or settings.get("title"),
                     "keywords": ["My Clinic", "induction", prefix],
                     "typical_learning_time": f"PT{seat.group(1)}M" if seat else None},
        "objectives": objectives,
        "outline": outline,
        "screens": built,
        "assets": list(assets.values()),
        "__extra_css": explore_hotspot_css(built, assets),
    }
    out = mdir / "build"
    out.mkdir(exist_ok=True)
    (out / "course-spec.json").write_text(json.dumps(spec, ensure_ascii=False, indent=1))
    (out / "asset-map.json").write_text(json.dumps({"companions_placed": placed, "assets": report},
                                                   ensure_ascii=False, indent=2))
    pend = sum(1 for k, v in report.items() if v.get("status") == "PENDING" and k != "_audio")
    print(f"{module}: {len(built)} screens · {len(assets)} assets ({pend} pending cards) · "
          f"{placed} companion poses placed · audio placeholders dropped: {report.get('_audio', {}).get('count', 0)}")
    return spec


if __name__ == "__main__":
    for m in sys.argv[1:] or ["03_hr-employee-induction"]:
        build(m)
