#!/usr/bin/env python3
"""Package one module as a SCORM 1.2 zip for Oracle Learning, using our own player.

    python3 tools/build_package.py <module>        e.g. 04_operations-and-my-care

Reads   <module>/build/course-spec.json   (made by build_course_spec.py; nothing scored changes here)
Writes  <module>/build/package/           index.html, course.js, player.js, player.css, assets/, imsmanifest.xml
        <module>/build/<zip name>.zip      the file to upload to Oracle (name kept from the old build)
        <module>/build/preview.html        opens the package in a browser (progress saved in that browser)

The player (tools/player/) has no dependencies and talks to the LMS through the SCORM 1.2 API
(window.API in a parent frame or the opener). The edumints compiler is no longer used.
"""
from __future__ import annotations

import base64
import json
import re
import shutil
import sys
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

PLANS = Path(__file__).resolve().parents[1]
PLAYER = Path(__file__).resolve().parent / "player"
BRAND = PLANS / "00_program" / "brand"
FONTS = ["montserrat-latin-400-normal.woff2", "montserrat-latin-600-normal.woff2", "montserrat-latin-700-normal.woff2"]
DROP = {"notes", "narration_text", "reveal", "animation", "duration_hint_sec", "node_id", "evidence_screen_ids"}
TEAL_INK = {"#008C99": "#006E78"}   # brand-identity.md: teal is for large text only; small text uses the dark teal


def module_colour(mdir: Path) -> str:
    m = re.search(r"module colour \*\*[^#*]*(#[0-9A-Fa-f]{6})", (mdir / "README.md").read_text())
    return m.group(1).upper() if m else "#003867"


def zip_name(mdir: Path, spec: dict) -> str:
    old = sorted((mdir / "build").glob("MC_*1.2.zip")) or sorted((mdir / "build").glob("MC_*.zip"))
    if old:
        return old[-1].name
    return f"MC_{mdir.name[:2]}_{spec['screens'][0]['id'].split('-')[0]}_v0.1-draft_1.2.zip"


def manifest(spec: dict, files: list[str], ident: str) -> str:
    t = escape(spec["title"])
    d = escape((spec.get("metadata") or {}).get("description") or spec.get("description") or spec["title"])
    tlt = (spec.get("metadata") or {}).get("typical_learning_time") or "PT15M"
    kw = "".join(f"<imsmd:keyword><imsmd:langstring xml:lang=\"en\">{escape(k)}</imsmd:langstring></imsmd:keyword>"
                 for k in (spec.get("metadata") or {}).get("keywords", []))
    fl = "\n      ".join(f'<file href="{escape(f)}"/>' for f in files)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<manifest xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2" xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2" xmlns:imsmd="http://www.imsglobal.org/xsd/imsmd_v1p2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" identifier="MANIFEST-{ident}" version="1.2" xsi:schemaLocation="http://www.imsproject.org/xsd/imscp_rootv1p1p2 imscp_rootv1p1p2.xsd http://www.imsglobal.org/xsd/imsmd_v1p2 imsmd_v1p2p4.xsd http://www.adlnet.org/xsd/adlcp_rootv1p2 adlcp_rootv1p2.xsd">
  <metadata>
    <schema>ADL SCORM</schema>
    <schemaversion>1.2</schemaversion>
    <imsmd:lom><imsmd:general><imsmd:title><imsmd:langstring xml:lang="en">{t}</imsmd:langstring></imsmd:title><imsmd:language>en</imsmd:language><imsmd:description><imsmd:langstring xml:lang="en">{d}</imsmd:langstring></imsmd:description>{kw}</imsmd:general><imsmd:educational><imsmd:typicallearningtime><imsmd:datetime>{tlt}</imsmd:datetime></imsmd:typicallearningtime></imsmd:educational></imsmd:lom>
  </metadata>
  <organizations default="ORG-1">
    <organization identifier="ORG-1">
      <title>{t}</title>
      <item identifier="ITEM-1" identifierref="RES-1">
        <title>{t}</title>
        <adlcp:masteryscore>{spec['tracking']['passing_score']}</adlcp:masteryscore>
      </item>
    </organization>
  </organizations>
  <resources>
    <resource identifier="RES-1" type="webcontent" adlcp:scormtype="sco" href="index.html">
      {fl}
    </resource>
  </resources>
</manifest>
"""


TYPES = {"title_slide", "content_slide", "summary", "results_breakdown", "branching", "mcq", "true_false", "fill_blank",
         "drag_drop", "matching", "sorting", "accordion", "timeline", "tabs", "flashcards", "hotspot", "labeled_diagram",
         "simulation", "decision_scenario", "game", "escape_room", "adaptive_practice", "poll", "exploration",
         "worked_example", "image_compare", "video"}


def validate(out: Path, course: dict, spec: dict) -> list[str]:
    """Structural checks Oracle cares about plus the player's own needs. Empty list = ok."""
    bad = []
    try:
        import xml.etree.ElementTree as ET
        root = ET.parse(out / "imsmanifest.xml").getroot()
        ns = {"c": "http://www.imsproject.org/xsd/imscp_rootv1p1p2"}
        listed = {f.get("href") for f in root.iterfind(".//c:file", ns)}
        for f in listed:
            if not (out / f).is_file():
                bad.append(f"manifest lists a missing file: {f}")
        res = root.find(".//c:resource", ns)
        if res is None or res.get("href") != "index.html":
            bad.append("manifest resource must launch index.html")
    except Exception as e:  # noqa: BLE001
        bad.append(f"manifest does not parse: {e}")
    ids = [x["id"] for x in course["screens"]]
    if len(ids) != len(set(ids)):
        bad.append("duplicate screen ids")
    for x in course["screens"]:
        if x["type"] not in TYPES:
            bad.append(f"{x['id']}: screen type {x['type']} has no renderer")
        for c in x.get("choices", []) if x["type"] == "branching" else []:
            if c.get("goto_screen_id") and c["goto_screen_id"] not in ids:
                bad.append(f"{x['id']}: goto {c['goto_screen_id']} does not exist")
        blob = json.dumps(x)
        for aid in set(re.findall(r'"(?:image_asset_id|media_asset_id|before_asset_id|after_asset_id|artifact_asset_id)": "([^"]+)"', blob)) | set(re.findall(r"\{\{asset:([\w-]+)\}\}", blob)):
            if aid not in course["assets"]:
                bad.append(f"{x['id']}: picture {aid} is not in the package")
    if sum(x.get("points") or 0 for x in course["screens"]) != sum(x.get("points") or 0 for x in spec["screens"]):
        bad.append("total points differ from course-spec.json")
    if len(json.dumps({"c": ids[-1], "v": {i: 1 for i in ids}})) > 3000:
        bad.append("resume data could exceed the SCORM 1.2 limit of 4096 characters")
    return bad


def build(module: str) -> Path:
    mdir = PLANS / module
    spec = json.loads((mdir / "build" / "course-spec.json").read_text())
    out = mdir / "build" / "package"
    if out.exists():
        shutil.rmtree(out)
    (out / "assets").mkdir(parents=True)

    assets = {}
    for a in spec.get("assets", []):
        srcv, fn = a.get("source", ""), a.get("filename") or a["id"]
        if srcv.startswith("data:"):
            (out / "assets" / fn).write_bytes(base64.b64decode(srcv.split(",", 1)[1]))
        elif Path(srcv).exists():
            shutil.copy(srcv, out / "assets" / fn)
        else:
            continue
        assets[a["id"]] = f"assets/{fn}"
    for f in FONTS:
        shutil.copy(BRAND / "fonts" / f, out / "assets" / f)
    shutil.copy(BRAND / "assets" / "mark-white.png", out / "assets" / "mark-white.png")
    logo = assets.get("brand-logo-horizontal-navy")
    if not logo:
        shutil.copy(BRAND / "assets" / "logo-horizontal-navy.png", out / "assets" / "logo-horizontal-navy.png")
        logo = "assets/logo-horizontal-navy.png"

    # mission titles for the menu and the top bar: section name -> outline title (via node_id)
    otitle = {o["id"]: o["title"] for o in spec.get("outline", [])}
    titles = {}
    for s in spec["screens"]:
        if s.get("section") and s.get("node_id") in otitle:
            titles.setdefault(s["section"], otitle[s["node_id"]])
    screens = [{k: v for k, v in s.items() if k not in DROP} for s in spec["screens"]]
    meter = re.search(r'#livesHud::before\{content:"([^"]+) "', spec.get("__extra_css", ""))
    tlt = re.search(r"PT(\d+)M", (spec.get("metadata") or {}).get("typical_learning_time") or "")
    colour = module_colour(mdir)
    course = {
        "title": spec["title"], "short_title": re.sub(r"^My Clinic\s*[—-]\s*", "", spec["title"]),
        "prefix": spec["screens"][0]["id"].split("-")[0], "module": mdir.name[:2], "colour": colour, "colour_ink": TEAL_INK.get(colour),
        "duration": int(tlt.group(1)) if tlt else None, "tracking": spec["tracking"],
        "objectives": spec.get("objectives", []), "variables": spec.get("variables", []),
        "points_var": spec.get("points_var"), "levels": spec.get("levels"), "lives_var": spec.get("lives_var"),
        "max_lives": spec.get("max_lives"), "meter_label": meter.group(1) if meter else "Patient safety",
        "titles": titles, "assets": assets, "logo": logo, "petal": "assets/mark-white.png", "screens": screens,
    }
    (out / "course.js").write_text("window.COURSE=" + json.dumps(course, ensure_ascii=False, separators=(",", ":")) + ";\n")
    shutil.copy(PLAYER / "player.js", out / "player.js")
    shutil.copy(PLAYER / "player.css", out / "player.css")
    t = escape(spec["title"])
    (out / "index.html").write_text(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><link rel="stylesheet" href="player.css"></head>
<body><noscript>This course needs JavaScript.</noscript>
<script src="course.js"></script><script src="player.js"></script></body></html>
""")
    files = sorted(str(p.relative_to(out)) for p in out.rglob("*") if p.is_file())
    (out / "imsmanifest.xml").write_text(manifest(spec, files, f"MC-{course['prefix']}"))
    files.append("imsmanifest.xml")

    zp = mdir / "build" / zip_name(mdir, spec)
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(files):
            z.write(out / f, f)
    (mdir / "build" / "preview.html").write_text(
        '<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=package/index.html">'
        '<a href="package/index.html">Open the course preview</a>\n')
    issues = validate(out, course, spec)
    (mdir / "build" / "build-report.json").write_text(json.dumps({
        "builder": "tools/build_package.py (My Clinic player, SCORM 1.2)",
        "validate_package": {"ok": not issues, "issues": issues},
        "lint_course": {"error_count": len(issues), "issues": [{"code": "package", "message": i} for i in issues]},
        "package": {"file": zp.name, "bytes": zp.stat().st_size},
        "screens": len(screens), "total_points": sum(x.get("points") or 0 for x in screens),
    }, indent=1))
    size = zp.stat().st_size / 1e6
    print(f"{module}: {len(screens)} screens · {len(assets)} assets · {zp.name} {size:.1f} MB · "
          + ("validate ok" if not issues else f"{len(issues)} PROBLEMS: " + "; ".join(issues[:5])))
    if issues:
        sys.exit(1)
    return zp


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    build(sys.argv[1])
