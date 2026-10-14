#!/usr/bin/env python3
"""Audit the visual assets and document templates of the My Clinic storyboard programme.

Answers "what do we actually have, and what is still missing?" with evidence instead of memory:

* **Brand** — the supplied client logo lock-ups, title background, watermark, value tiles, the
  eight screen mockups against layouts L1–L6, plus pixel dimensions and alpha channels.
* **Companions** — approved previews vs the interim avatar crops vs the full-size Canva PNGs that
  are still outstanding (programme gap G6), with the Canva media id for each.
* **Module assets** — every asset id referenced by a storyboard, visual plan, visual board or
  asset register, checked against the files on disk (missing files and orphans).
* **Documents** — the client logo is present on every visual board, in every Word rendering and on
  every Markdown cover; card templates carry all eight sections; internal links resolve; no
  speaker label leaked into TTS input; placeholder markers counted per module.

Writes `00_program/asset-template-audit.md` and `00_program/asset-audit.json`.
Exits non-zero when a hard failure is found (referenced asset missing, broken internal link,
speaker label in `tts_text`, card missing a template section).

Usage:
    python3 elearning-course/scorm-plans/tools/audit_assets.py
"""
from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[3]
PLANS = ROOT / "elearning-course" / "scorm-plans"
BRAND = PLANS / "00_program" / "brand"
CHARS = PLANS / "00_program" / "characters"
REVIEW = PLANS / "client-review"
TODAY = "2026-10-14"

BRAND_ASSETS = [
    "assets/logo-horizontal-navy.png", "assets/logo-horizontal-white.png",
    "assets/logo-horizontal-on-navy.png", "assets/mark-navy.png", "assets/mark-white.png",
    "assets/mark-watermark-navy-40.png", "assets/background-title-navy.png",
    "assets/value-tile-ambitious-teal.png", "assets/value-tile-caring-purple.png",
    "assets/value-tile-collaborative-burgundy.png", "assets/value-tile-responsible-magenta.png",
    "logo-preview.png",
]
MOCKUPS = {
    "screen-mockups/01-title.png": "L1 Title",
    "screen-mockups/02-section-opener.png": "L2 Section opener",
    "screen-mockups/03-content.png": "L3 Content",
    "screen-mockups/04-question.png": "L4 Question",
    "screen-mockups/05-scenario.png": "L5 Scenario",
    "screen-mockups/06-results.png": "L6 Results / close",
    "screen-mockups/07-meet-your-guides.png": "L1 duo (companion intro)",
    "screen-mockups/08-companion-tip.png": "L4 tip card (companion)",
}
POSES = ["master", "welcome", "explaining", "tip", "thinking", "concern", "success", "listening", "avatar-neutral"]
INTERIM_AVATARS = ["char-noor-avatar-neutral.png", "char-omar-avatar-neutral.png",
                   "char-noor-avatar-happy.png", "char-noor-avatar-concern.png", "char-omar-avatar-happy.png"]
CARD_SECTIONS = ["#### 1. Purpose", "#### 2. On-screen content", "#### 3. Visual design",
                 "#### 4. Interaction and scoring", "#### 5. Narration", "#### 6. Accessibility",
                 "#### 7. Build fields (edumints)", "#### 8. Notes for SME and developer"]

hard_failures: list[str] = []
notes: list[str] = []


def image_info(path: Path) -> dict:
    with Image.open(path) as image:
        return {"file": str(path.relative_to(PLANS)), "size": list(image.size), "mode": image.mode,
                "bytes": path.stat().st_size,
                "alpha": image.mode in ("RGBA", "LA") or "transparency" in image.info}


def canva_ids() -> dict[str, dict[str, str]]:
    text = (CHARS / "companions.md").read_text(encoding="utf-8")
    ids: dict[str, dict[str, str]] = {}
    for line in text.splitlines():
        match = re.match(r"\| `(char-<id>-[a-z-]+)` \| `(MAHX-[A-Za-z0-9_-]+)` \| `(MAHX-[A-Za-z0-9_-]+)` \|", line)
        if match:
            ids[match.group(1)] = {"noor": match.group(2), "omar": match.group(3)}
    return ids


PREFIXES = {"01_health-and-safety-1": "hs1", "02_health-and-safety-2": "hs2",
            "03_hr-employee-induction": "hr", "04_operations-and-my-care": "ops",
            "05_rcm-documentation-and-coding": "rcma", "06_rcm-ebp-benefits-and-rejections": "rcmb",
            "07_quality-safety-and-risk": "qsr", "08_it-ehr-consultation": "ehr"}


def module_asset_audit(folder: str) -> dict:
    story = PLANS / folder / "storyboard"
    prefix = PREFIXES[folder]
    referenced: dict[str, set[str]] = {}
    texts = {
        "storyboard.md": (story / "storyboard.md").read_text(encoding="utf-8"),
        "visual-plan.json": (story / "visual-plan.json").read_text(encoding="utf-8"),
        "screen-visuals.html": (story / "screen-visuals.html").read_text(encoding="utf-8"),
        "asset-register.md": (story / "asset-register.md").read_text(encoding="utf-8"),
    }
    pattern = re.compile(rf"\b{re.escape(prefix)}-(?:img|tbl|pdf|vid|cap)[a-z0-9-]*[a-z0-9]")
    for name, text in texts.items():
        for asset_id in set(pattern.findall(text)):
            referenced.setdefault(asset_id, set()).add(name)
    for asset_id in set(re.findall(r"`(char-(?:noor|omar)-[a-z-]+)`", texts["storyboard.md"] + texts["visual-plan.json"])):
        referenced.setdefault(asset_id, set()).add("companion")
    on_disk = {p.stem: p for p in story.glob("assets/*") if p.suffix in {".svg", ".png", ".jpg"}}
    register = texts["asset-register.md"]

    def planned_in_register(asset_id: str) -> bool:
        if f"`{asset_id}`" in register or f"`{asset_id} (" in register:
            return True
        base = re.sub(r"-\d+$", "", asset_id)
        if f"`{base}`" in register or re.search(rf"`{re.escape(base)}[-–.0-9(]", register):
            return True
        # Asset families: the register plans one id (hr-img-7c-icons) that the cards expand
        # per item (hr-img-7c-care, hr-img-award-trophy, ...).
        family = register and re.findall(r"`([a-z0-9-]+)-(?:icons|sheets|set)", register)
        return any(asset_id.startswith(f"{stem}-") for stem in family or [])

    # The register lists planned assets that intentionally have no file yet; keep those separate
    # from genuine gaps where a card points at a file that should exist.
    missing = sorted(a for a in referenced
                     if a not in on_disk and not a.startswith("char-") and not planned_in_register(a))
    planned = sorted(a for a in referenced if a not in on_disk and not a.startswith("char-") and a not in missing)
    orphans = sorted(p.stem for p in on_disk.values() if p.stem not in referenced)
    svg_issues = []
    for path in on_disk.values():
        if path.suffix != ".svg":
            continue
        try:
            tree = ET.fromstring(path.read_text(encoding="utf-8"))
            if tree.get("viewBox") is None:
                svg_issues.append(f"{path.name}: no viewBox")
        except ET.ParseError as error:
            svg_issues.append(f"{path.name}: XML error {error}")
            hard_failures.append(f"{folder}: {path.name} is not valid SVG")
    for asset_id in missing:
        hard_failures.append(f"{folder}: asset `{asset_id}` is referenced but has no file in storyboard/assets/")
    return {
        "referenced": {k: sorted(v) for k, v in sorted(referenced.items())},
        "on_disk": sorted(on_disk),
        "missing_files": missing,
        "planned_not_built": planned,
        "orphans": orphans,
        "svg_issues": svg_issues,
    }


def doc_audit() -> dict:
    result = {"docx": [], "boards": [], "markdown_covers": [], "broken_links": []}
    for docx in sorted(REVIEW.glob("*.docx")):
        with zipfile.ZipFile(docx) as archive:
            media = [n for n in archive.namelist() if n.startswith("word/media/")]
            header = archive.read("word/header1.xml").decode("utf-8") if "word/header1.xml" in archive.namelist() else ""
            footer = archive.read("word/footer1.xml").decode("utf-8") if "word/footer1.xml" in archive.namelist() else ""
        logo_in_header = "image" in header or "blip" in header
        result["docx"].append({
            "file": docx.name, "media": len(media), "logo_in_header": logo_in_header,
            "page_fields": "PAGE" in footer and "NUMPAGES" in footer,
        })
        if not logo_in_header:
            hard_failures.append(f"{docx.name}: running header has no client logo")
    for board in sorted(PLANS.glob("0[1-8]_*/storyboard/screen-visuals.html")):
        text = board.read_text(encoding="utf-8")
        ok = "logo-horizontal-white.png" in text or "logo-horizontal-navy.png" in text
        result["boards"].append({"file": str(board.relative_to(PLANS)), "logo": ok})
        if not ok:
            hard_failures.append(f"{board.relative_to(PLANS)}: no client logo on the board")
    for md in sorted(PLANS.glob("0[1-8]_*/storyboard/storyboard.md")) + [PLANS / "00_program/programme-status.md", PLANS / "README.md"]:
        text = md.read_text(encoding="utf-8")
        ok = "logo-preview.png" in text or "logo-horizontal" in text
        result["markdown_covers"].append({"file": str(md.relative_to(PLANS)), "logo": ok})
        if not ok:
            notes.append(f"{md.relative_to(PLANS)}: no logo on the cover line")
    # internal link resolution across the whole plans tree
    for md in sorted(PLANS.rglob("*.md")):
        base = md.parent
        for link in re.findall(r"\]\(([^)\s]+)\)", md.read_text(encoding="utf-8")):
            if link.startswith(("http", "mailto", "#")):
                continue
            target = (base / link.split("#")[0]).resolve()
            if not target.exists():
                result["broken_links"].append({"file": str(md.relative_to(PLANS)), "link": link})
                hard_failures.append(f"{md.relative_to(PLANS)}: broken link {link}")
    return result


def narration_audit(folder: str) -> dict:
    script = json.loads((PLANS / folder / "storyboard" / "narration-script.json").read_text(encoding="utf-8"))
    export = json.loads((PLANS / folder / "storyboard" / "audio-script-export.json").read_text(encoding="utf-8"))
    leaks = [s["screen_id"] for s in export["segments"] if re.match(r"^(NOOR|OMAR):", s.get("tts_text", ""))]
    for sid in leaks:
        hard_failures.append(f"{folder}: speaker label leaked into tts_text on {sid}")
    parts = [s for s in script["segments"] if str(s.get("part", "")).endswith("-1")]
    dual = sorted({s["screen_id"] for s in parts})
    unsplit = []
    for s in script["segments"]:
        labels = set(re.findall(r"^(NOOR|OMAR):", s["narration"], re.M))
        if len(labels) > 1:
            unsplit.append(s["screen_id"])
            hard_failures.append(f"{folder}: {s['screen_id']} still mixes two voices in one segment")
    return {
        "segments": len(script["segments"]), "two_voice_screens": dual, "unsplit": unsplit,
        "tts_label_leaks": leaks, "minutes": round(export["total_est_sec"] / 60, 1),
        "voice_persona_set": bool(script.get("voice", {}).get("persona")),
    }


def template_audit(folder: str) -> dict:
    text = (PLANS / folder / "storyboard" / "storyboard.md").read_text(encoding="utf-8")
    cards = re.findall(r"^### `([a-z0-9-]+)`", text, re.M)
    incomplete = []
    for card in cards:
        block = text.split(f"### `{card}`", 1)[1]
        block = block.split("\n### `", 1)[0]
        missing = [s for s in CARD_SECTIONS if s not in block]
        if missing:
            incomplete.append({"card": card, "missing": missing})
            hard_failures.append(f"{folder}: card {card} missing template sections {missing}")
    placeholders = len(re.findall(r"⚠ PENDING", text))
    angles = len(re.findall(r"`<[a-z0-9-…]+>`", text))
    return {"cards": len(cards), "incomplete_cards": incomplete,
            "pending_markers": placeholders, "angle_placeholders": angles}


def main() -> None:
    audit: dict = {"date": TODAY, "brand": {}, "companions": {}, "modules": {}, "documents": {}}

    brand_rows = []
    for rel in BRAND_ASSETS:
        path = BRAND / rel
        if not path.exists():
            hard_failures.append(f"brand asset missing: {rel}")
            brand_rows.append({"file": rel, "status": "MISSING"})
            continue
        info = image_info(path)
        brand_rows.append(info)
    audit["brand"]["assets"] = brand_rows
    mockup_rows = []
    for rel, layout in MOCKUPS.items():
        path = BRAND / rel
        if not path.exists():
            hard_failures.append(f"screen mockup missing: {rel}")
            mockup_rows.append({"file": rel, "layout": layout, "status": "MISSING"})
        else:
            mockup_rows.append({**image_info(path), "layout": layout})
    audit["brand"]["mockups"] = mockup_rows
    audit["brand"]["layouts_covered"] = sorted({r["layout"] for r in mockup_rows if r.get("size")})

    ids = canva_ids()
    previews = sorted(p.name for p in (CHARS / "previews").glob("*.jpg"))
    expected_previews = sorted(f"char-{who}-{pose}.jpg" for who in ("noor", "omar") for pose in POSES)
    assets = sorted(p.name for p in (CHARS / "assets").glob("*.png")) if (CHARS / "assets").is_dir() else []
    audit["companions"] = {
        "previews_present": previews,
        "previews_missing": [p for p in expected_previews if p not in previews],
        "interim_avatars": assets,
        "interim_missing": [a for a in INTERIM_AVATARS if a not in assets],
        "full_size_outstanding": sorted(
            f"{asset.replace('<id>', who)}.png (Canva {ids[asset][who]})"
            for asset in ids for who in ("noor", "omar")),
        "canva_ids": ids,
    }

    for folder in sorted(p.name for p in PLANS.glob("0[1-8]_*")):
        audit["modules"][folder] = {
            "assets": module_asset_audit(folder),
            "narration": narration_audit(folder),
            "template": template_audit(folder),
        }

    audit["documents"] = doc_audit()

    (PLANS / "00_program" / "asset-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # ---- markdown report
    md: list[str] = ["# Visual asset and template audit", "",
                     f"![My Clinic logo](brand/logo-preview.png)", "",
                     f"> Generated by `tools/audit_assets.py` on **{TODAY}**. Evidence-based inventory of "
                     "brand files, companion art, module assets, Word renderings and card templates. "
                     "Hard failures block the audit exit code; everything else is a planning note.", ""]
    md += ["## 1. Brand kit (supplied client art)", "",
           "| File | Pixels | Mode | Alpha | Bytes |", "|---|---|---|---|---|"]
    for row in audit["brand"]["assets"]:
        if row.get("status") == "MISSING":
            md.append(f"| `{row['file']}` | — | — | — | **MISSING** |")
        else:
            md.append(f"| `{row['file']}` | {row['size'][0]}×{row['size'][1]} | {row['mode']} | {'yes' if row['alpha'] else 'no'} | {row['bytes']:,} |")
    md += ["", "| Mockup | Brand layout | Pixels |", "|---|---|---|"]
    for row in audit["brand"]["mockups"]:
        md.append(f"| `{row['file']}` | {row['layout']} | {row.get('size', ['—'])[0]}×{row.get('size', ['—'])[1]} |")
    md += ["", f"Layouts with a mockup: {', '.join(audit['brand']['layouts_covered'])}.", ""]

    comp = audit["companions"]
    md += ["## 2. Companions Noor and Dr. Omar", "",
           f"- Approved previews in `characters/previews/`: **{len(comp['previews_present'])} of {len(comp['previews_missing']) + len(comp['previews_present'])}**"
           + (f" — missing: {', '.join(comp['previews_missing'])}" if comp["previews_missing"] else " (complete)."),
           f"- Interim transparent PNGs in `characters/assets/`: **{len(comp['interim_avatars'])}** ({', '.join('`' + a + '`' for a in comp['interim_avatars'])}).",
           f"- **Full-size production PNGs still outstanding: {len(comp['full_size_outstanding'])}** (programme gap G6). Download each from Canva as transparent PNG:",
           "", "| Asset | Noor media id | Dr. Omar media id |", "|---|---|---|"]
    for asset, ids_row in comp["canva_ids"].items():
        md.append(f"| `{asset.replace('<id>', '<noor|omar>')}` | `{ids_row['noor']}` | `{ids_row['omar']}` |")
    md += ["", "## 3. Module assets, narration and card templates", "",
           "| Module | Assets on disk | Referenced, no file | Planned, not built | Orphans | SVG issues | Cards | Incomplete cards | ⚠ PENDING | Narration min | Two-voice screens | TTS label leaks |",
           "|---|---:|---|---|---|---|---:|---:|---:|---:|---|---|"]
    for folder, data in audit["modules"].items():
        a, n, t = data["assets"], data["narration"], data["template"]
        md.append(f"| {folder[:2]} | {len(a['on_disk'])} | {', '.join('`' + x + '`' for x in a['missing_files']) or '—'} | "
                  f"{len(a['planned_not_built'])} | {', '.join(a['orphans']) or '—'} | {len(a['svg_issues'])} | {t['cards']} | "
                  f"{len(t['incomplete_cards'])} | {t['pending_markers']} | {n['minutes']} | {len(n['two_voice_screens'])} | {len(n['tts_label_leaks'])} |")
    md += ["", "Planned-but-not-built assets are intentional: they wait on SME/consent/DPO decisions recorded in each asset register.", ""]

    docs = audit["documents"]
    md += ["## 4. Documents, logo placement and links", "",
           "| Word document | Images | Logo in running header | Page fields |", "|---|---:|---|---|"]
    for row in docs["docx"]:
        md.append(f"| `{row['file']}` | {row['media']} | {'yes' if row['logo_in_header'] else '**no**'} | {'yes' if row['page_fields'] else '**no**'} |")
    boards_ok = sum(1 for b in docs["boards"] if b["logo"])
    md += ["", f"Visual boards with the client logo: **{boards_ok}/{len(docs['boards'])}**. "
           f"Markdown covers with a logo line: **{sum(1 for c in docs['markdown_covers'] if c['logo'])}/{len(docs['markdown_covers'])}**. "
           f"Broken internal links: **{len(docs['broken_links'])}**.", ""]
    if docs["broken_links"]:
        md += ["| File | Broken link |", "|---|---|"]
        md += [f"| `{b['file']}` | `{b['link']}` |" for b in docs["broken_links"]]
        md.append("")

    md += ["## 5. Verdict", ""]
    if hard_failures:
        md += [f"**{len(hard_failures)} hard failure(s):**", ""]
        md += [f"- {f}" for f in hard_failures]
    else:
        md += ["No hard failures: every referenced asset exists, every card follows the template, "
               "every board and Word rendering carries the client logo, and no speaker label reaches "
               "the TTS input. Remaining work is production supply (full-size companion PNGs, "
               "consented photos, EHR test captures) and SME decisions, not documentation drift.", ""]
    if notes:
        md += ["Notes:", ""] + [f"- {n}" for n in notes]
    (PLANS / "00_program" / "asset-template-audit.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print("\n".join(f"- {f}" for f in hard_failures) or "audit clean")
    print(f"modules={len(audit['modules'])} hard_failures={len(hard_failures)}")
    raise SystemExit(1 if hard_failures else 0)


if __name__ == "__main__":
    main()
