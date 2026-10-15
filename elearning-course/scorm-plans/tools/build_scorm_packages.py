#!/usr/bin/env python3
"""Build draft SCORM packages for 03 + 07 from storyboard build blocks.

Uses the edumints-scorm-mcp core (project.py + packager.py) directly — no MCP server
needed — to produce validateable SCORM zips in .generated/scorm/<module>/.

This is a **draft** build: narration audio is omitted (D10 open), many visuals are
placeholders (B6/B7 etc.), and 102 Phase 0 decisions are still open. The packages are
for LMS smoke-testing and review, not production release. See `scorm-structure.md`
and `programme-status.md` for the full gate status.

Usage:
    python3 elearning-course/scorm-plans/tools/build_scorm_packages.py 03_hr-employee-induction 07_quality-safety-and-risk
    python3 elearning-course/scorm-plans/tools/build_scorm_packages.py --all
    python3 elearning-course/scorm-plans/tools/build_scorm_packages.py --out .generated/scorm --no-validate

Stdlib + edumints core only (pydantic, ulid, lxml, jinja2, nh3). The edumints checkout
is expected at /tmp/edumints (cloned by the build) or via EDUMINTS_PATH env.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
import asyncio
import zipfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TOOLS = Path(__file__).resolve().parent
REPO_ROOT = Path(__file__).resolve().parents[3]

# edumints core location
EDUMINTS_PATH = Path(os.environ.get("EDUMINTS_PATH", "/tmp/edumints"))
if str(EDUMINTS_PATH) not in sys.path:
    sys.path.insert(0, str(EDUMINTS_PATH))

try:
    from core.project import CourseSpec, Project, new_project_id, ThemeTokens
    from core.store import create_store
    from core.packager import Packager
    from core.validator import validate_project, validate_zip
    import components.renderer as renderer
except ImportError as e:
    print(f"ERROR: edumints core not found at {EDUMINTS_PATH}: {e}", file=sys.stderr)
    print("Clone it with: git clone https://github.com/marwanabdulhady-gif/edumints-scorm-mcp.git /tmp/edumints", file=sys.stderr)
    sys.exit(1)

# ---------------------------------------------------------------------------
# Helpers to parse storyboard and phase files
# ---------------------------------------------------------------------------

def parse_blocks(storyboard_md: Path) -> list[dict[str, Any]]:
    text = storyboard_md.read_text(encoding="utf-8")
    out = []
    for m in re.finditer(r"```json\s*\n(.*?)```", text, re.S):
        try:
            j = json.loads(m.group(1))
        except ValueError:
            continue
        if isinstance(j, dict) and "type" in j and "id" in j:
            out.append(j)
    return out

def parse_course_settings(phase4_md: Path) -> dict[str, Any]:
    text = phase4_md.read_text(encoding="utf-8")
    m = re.search(r"```json\s*\n(\{.*?\})\s*```", text, re.S)
    if m:
        return json.loads(m.group(1))
    return {}

def parse_objectives(storyboard_md: Path) -> list[dict[str, str]]:
    """From the 'Objectives covered' table in storyboard.md."""
    text = storyboard_md.read_text(encoding="utf-8")
    objs = []
    # Match table rows like | `hr-o1` | Link ... | `hr-011`, `hr-013` |
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 2 and re.fullmatch(r"[a-z0-9]+-o\d+", cells[0].strip("`")):
            oid = cells[0].strip("`")
            desc = re.sub(r"<.*?>", "", cells[1]).strip()
            # Remove markdown artifacts
            desc = desc.replace("⚠ PENDING", "").strip()
            objs.append({"id": oid, "description": desc})
    return objs

def parse_outline(storyboard_md: Path) -> list[dict[str, Any]]:
    """From the 'Section outline' table."""
    text = storyboard_md.read_text(encoding="utf-8")
    outline = []
    # Find the section outline table
    in_outline = False
    for line in text.splitlines():
        if "Section outline" in line or "Node id | Section title | Screens" in line:
            in_outline = True
            continue
        if not in_outline:
            continue
        if not line.startswith("|"):
            if outline:  # end of table
                break
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 2 and re.fullmatch(r"[a-z0-9]+-s[A-Z0-9]+", cells[0].strip("`")):
            nid = cells[0].strip("`")
            title = cells[1].strip()
            # Outline node: id, kind=section, title, objective (if any)
            # We will attach objective later if section maps to objective
            outline.append({"id": nid, "kind": "section", "title": title})
        elif cells and set("".join(cells)) <= set("-: "):
            continue
        elif "Node id" in line:
            continue
    return outline

def parse_outline_from_phase2(phase2_md: Path) -> list[dict[str, Any]]:
    """Fallback: parse from phase-2-storyboard.md section tables."""
    text = phase2_md.read_text(encoding="utf-8")
    outline = []
    # Each section heading like "## A — Welcome" then table with | Id | Type ...
    # Instead look for outline JSON in phase-4, but we already have that.
    # For now return empty if not found, the storyboard one is more reliable.
    return outline

# ---------------------------------------------------------------------------
# Asset handling
# ---------------------------------------------------------------------------

DUMMY_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="960" height="540" viewBox="0 0 960 540">
<rect width="960" height="540" fill="#F4F7FA"/>
<rect x="40" y="40" width="880" height="460" fill="white" stroke="#C0CED9" stroke-width="2" rx="12"/>
<text x="480" y="240" text-anchor="middle" font-family="sans-serif" font-size="24" fill="#003867">Draft visual</text>
<text x="480" y="280" text-anchor="middle" font-family="sans-serif" font-size="16" fill="#6c6c75">{label}</text>
<text x="480" y="320" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#9D3293">Pending SME / DPO review — placeholder</text>
</svg>"""

def dummy_svg_bytes(label: str) -> bytes:
    return DUMMY_SVG.replace("{label}", label[:60]).encode("utf-8")

def collect_assets(module_dir: Path, blocks: list[dict]) -> dict[str, bytes]:
    """Map placeholder ids to bytes. Returns dict placeholder_id -> bytes."""
    asset_map: dict[str, bytes] = {}
    storyboard_assets_dir = module_dir / "storyboard" / "assets"
    brand_assets_dir = ROOT / "00_program" / "brand" / "assets"

    # Collect real SVG/PNG files
    real_files: dict[str, Path] = {}
    if storyboard_assets_dir.exists():
        for p in storyboard_assets_dir.iterdir():
            if p.is_file():
                # key without extension, e.g., hr-img-7c-icons.svg -> hr-img-7c-icons
                real_files[p.stem] = p
                # also with full name
                real_files[p.name] = p
    if brand_assets_dir.exists():
        for p in brand_assets_dir.iterdir():
            if p.is_file():
                real_files[p.stem] = p
                real_files[p.name] = p
                # brand placeholder variants like brand-background-title-navy -> background-title-navy
                # and brand-logo-... etc.
                if p.name.startswith("background-") or p.name.startswith("logo-") or p.name.startswith("mark-") or p.name.startswith("value-tile-"):
                    real_files[p.stem] = p
                    # also map brand- prefixed
                    real_files[f"brand-{p.stem}"] = p
                    real_files[f"brand-{p.name}"] = p

    # Find all placeholder asset references in blocks - recursively
    placeholders = set()
    def collect_placeholders(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, str) and v.startswith("<") and v.endswith(">") and "-" in v and not v.startswith("<p") and not v.startswith("<ul") and not v.startswith("<li"):
                    # Likely a placeholder like <hr-img-...>, <brand-...>, <qsr-img-...>
                    # Avoid HTML tags
                    inner = v.strip("<>")
                    if re.match(r"^[a-z0-9_-]+$", inner):
                        placeholders.add(inner)
                elif isinstance(v, (dict, list)):
                    collect_placeholders(v)
                elif k.endswith("_asset_id") and isinstance(v, str) and v.startswith("<") and v.endswith(">"):
                    placeholders.add(v.strip("<>"))
        elif isinstance(obj, list):
            for item in obj:
                collect_placeholders(item)
    for b in blocks:
        collect_placeholders(b)

    # For each placeholder, try to find real file, else dummy
    for ph in placeholders:
        # Special case: hr-img-7c-* individual icons -> map to combined hr-img-7c-icons.svg
        if ph.startswith("hr-img-7c-"):
            # Try the combined file
            p_combined = real_files.get("hr-img-7c-icons") or real_files.get("hr-img-7c-icons.svg")
            if p_combined and p_combined.exists():
                try:
                    asset_map[ph] = p_combined.read_bytes()
                    continue
                except Exception:
                    pass
        # Special case: hr-img-leaders-* -> use dummy for now (no real leaders file due to privacy B6)
        # Try exact stem
        p = real_files.get(ph)
        if p and p.exists():
            try:
                asset_map[ph] = p.read_bytes()
                continue
            except Exception:
                pass
        # Try with .svg/.png extension
        cand = None
        for ext in (".svg", ".png", ".jpg", ".jpeg"):
            cand = real_files.get(ph + ext)
            if cand and cand.exists():
                try:
                    asset_map[ph] = cand.read_bytes()
                    break
                except Exception:
                    continue
            cand = None
        if cand and cand.exists():
            continue
        # Also try brand mapping: if ph starts with brand- then strip
        if ph.startswith("brand-"):
            short = ph[len("brand-"):]
            p2 = real_files.get(short)
            if p2 and p2.exists():
                try:
                    asset_map[ph] = p2.read_bytes()
                    continue
                except Exception:
                    pass
            # Try brand- prefix with file extension
            for ext in (".svg", ".png", ".jpg", ".jpeg"):
                p2 = real_files.get(short + ext)
                if p2 and p2.exists():
                    try:
                        asset_map[ph] = p2.read_bytes()
                        break
                    except Exception:
                        continue
            else:
                # Check if short without brand- still has mapping via value-tile-*
                if short.startswith("value-tile-"):
                    p3 = real_files.get(short)
                    if p3 and p3.exists():
                        try:
                            asset_map[ph] = p3.read_bytes()
                            continue
                        except Exception:
                            pass
        # Fallback dummy
        asset_map[ph] = dummy_svg_bytes(ph)

    # Also need to handle narration placeholders: we will ignore them (set to None), but we still need to not create assets for them
    # Remove any aud placeholders
    for k in list(asset_map.keys()):
        if "-aud-" in k or k.startswith("hr-aud") or k.startswith("qsr-aud"):
            # These are audio, not images; we will not include them as we drop narration_asset_id
            # But keep a dummy if needed for testing audio?
            del asset_map[k]

    return asset_map

# ---------------------------------------------------------------------------
# Screen sanitization
# ---------------------------------------------------------------------------

# Fields that are local to storyboard tooling and not part of edumints model
LOCAL_ONLY_FIELDS = {"reveal", "animation", "narration_text", "section", "node_id"}  # but section/node_id are valid
# Actually section and node_id are valid in edumints ScreenBase, keep them
LOCAL_ONLY_FIELDS = {"reveal", "animation", "narration_text"}

# Keep these as they are valid in edumints
KEEP_FIELDS = {
    "type", "id", "title", "subtitle", "section", "node_id", "objective_ids", "evidence_screen_ids",
    "points", "prompt_html", "body_html", "intro_html", "feedback", "options", "pairs", "items", "targets",
    "regions", "nodes", "steps", "puzzles", "choices", "blanks", "tabs", "cards", "events", "blocks",
    "labels", "image_asset_id", "media_asset_id", "background_asset_id", "video_asset_id", "poster_asset_id",
    "captions_asset_id", "lottie_asset_id", "before_asset_id", "after_asset_id", "html_asset_id",
    "correct", "case_sensitive", "multi", "allow_text", "reflection_html", "self_explanation_prompt_html",
    "fading", "prompt_html", "layout", "media_alt", "image_alt", "show_score", "show_completion",
    "sections", "weak_threshold", "show_total", "mode", "require_all", "time_limit_sec", "lives",
    "pass_score", "max_items", "target_success", "pass_ratio", "adaptive", "start_node_id", "intro_html",
    "notes", "duration_hint_sec", "narration_asset_id", "visible_if", "on_enter", "timer_sec", "on_timeout",
    "timeout_goto", "on_correct", "on_wrong", "points_var", "levels", "max_lives", "audience_pack",
    "source_item_count", "auto_tts", "tts_voice", "variables", "metadata", "xapi"
}

def sanitize_block(block: dict[str, Any], asset_map: dict[str, bytes]) -> dict[str, Any]:
    """Return a cleaned copy of block suitable for edumints validation.

    - Strip local-only fields
    - Normalize placeholder asset ids: if placeholder has a real dummy asset, replace with a stable asset id;
      otherwise set to None for optional fields or keep dummy for required.
    - Ensure lists and defaults are correct.
    """
    out = {}
    # Keep only allowed keys + type/id/title
    for k, v in block.items():
        if k in LOCAL_ONLY_FIELDS:
            continue
        # For asset ids that are placeholders, handle separately
        if k.endswith("_asset_id") and isinstance(v, str) and v.startswith("<") and v.endswith(">"):
            ph = v.strip("<>")
            # For narration, drop it for draft (no audio)
            if "-aud-" in ph or ph.startswith("hr-aud") or ph.startswith("qsr-aud"):
                # Omit narration for draft
                continue
            # For other assets, if we have a dummy/real, we will map to a real asset id later
            # Keep the placeholder for now; we will replace after asset ids are known
            out[k] = v
        else:
            out[k] = v

    # Also need to handle nested asset ids inside nodes/steps that are placeholders
    # We will keep them as is for now and replace in a second pass after we know asset ids

    # Ensure title exists (edumints requires it)
    if "title" not in out and "id" in out:
        out["title"] = out["id"]

    # For types that have points but shouldn't (content slides), remove points if type is not scored
    # Scored types in edumints have points field; unscored like content_slide, title_slide, etc. don't
    # Let's check which types are scored: mcq, true_false, fill_blank, drag_drop, matching, sorting, hotspot (quiz), decision_scenario, simulation, adaptive_practice, etc.
    # For safety, if the block has points==0 and type is content/accordion/tabs/etc., remove points
    scored_types = {"mcq", "true_false", "fill_blank", "drag_drop", "matching", "sorting", "hotspot", "labeled_diagram", "decision_scenario", "simulation", "adaptive_practice", "term_match_race", "escape_room", "game", "poll"}  # poll is not scored but has no points
    # But content_slide, title_slide, summary, accordion, tabs, flashcards, timeline, worked_example, results_breakdown, video, etc. are not scored
    unscored_types = {"title_slide", "content_slide", "accordion", "tabs", "flashcards", "timeline", "worked_example", "results_breakdown", "summary", "video", "lottie", "image_compare", "data_chart", "exploration", "embed_html"}
    if out.get("type") in unscored_types and "points" in out:
        # Only keep points if non-zero? But unscored should not have points at all
        out.pop("points", None)
        out.pop("objective_ids", None)
        out.pop("evidence_screen_ids", None)
    # For scored types, ensure points and objective_ids exist
    if out.get("type") in scored_types:
        if "points" not in out:
            out["points"] = 10
        if "objective_ids" not in out:
            out["objective_ids"] = []
        if "evidence_screen_ids" not in out:
            out["evidence_screen_ids"] = []

    # For hotspot, ensure mode and regions are valid
    # For matching, ensure pairs length >=2
    # For sorting, ensure items length >=2
    # For adaptive_practice, ensure items >=3

    return out

def replace_placeholder_asset_ids(block: dict[str, Any], placeholder_to_asset_id: dict[str, str]) -> dict[str, Any]:
    """Recursively replace <placeholder> strings with real asset ids in the entire block."""
    def repl(val):
        if isinstance(val, str) and val.startswith("<") and val.endswith(">"):
            inner = val.strip("<>")
            if re.match(r"^[a-z0-9_-]+$", inner):
                return placeholder_to_asset_id.get(inner, val)
        return val

    def recurse(obj):
        if isinstance(obj, dict):
            new = {}
            for k, v in obj.items():
                if isinstance(v, str) and v.startswith("<") and v.endswith(">"):
                    inner = v.strip("<>")
                    if re.match(r"^[a-z0-9_-]+$", inner):
                        new[k] = placeholder_to_asset_id.get(inner, v)
                    else:
                        new[k] = v
                elif isinstance(v, (dict, list)):
                    new[k] = recurse(v)
                else:
                    new[k] = v
            return new
        elif isinstance(obj, list):
            return [recurse(item) if isinstance(item, (dict, list)) else (placeholder_to_asset_id.get(item.strip("<>"), item) if isinstance(item, str) and item.startswith("<") and item.endswith(">") and re.match(r"^[a-z0-9_-]+$", item.strip("<>")) else item) for item in obj]
        else:
            return obj

    return recurse(block)

# ---------------------------------------------------------------------------
# Build one module
# ---------------------------------------------------------------------------

def build_module(module_dir: Path, out_dir: Path, validate: bool = True) -> dict[str, Any]:
    name = module_dir.name
    short = name[:2]
    print(f"\n=== Building {name} ===")
    storyboard_md = module_dir / "storyboard" / "storyboard.md"
    phase4_md = module_dir / "phase-4-build.md"
    phase2_md = module_dir / "phase-2-storyboard.md"

    if not storyboard_md.exists():
        raise FileNotFoundError(f"Missing {storyboard_md}")
    blocks = parse_blocks(storyboard_md)
    print(f"  Found {len(blocks)} storyboard blocks")
    settings = parse_course_settings(phase4_md)
    title = settings.get("title", f"My Clinic — {name}")
    scorm_version = settings.get("scorm_version", "1.2")
    language = settings.get("language", "en")
    tracking = settings.get("tracking", {"completion_rule": "viewed_all_and_passed", "passing_score": 80})
    print(f"  Title: {title}")
    print(f"  SCORM: {scorm_version} · language: {language} · tracking: {tracking}")

    objectives = parse_objectives(storyboard_md)
    print(f"  Objectives: {len(objectives)}")
    outline = parse_outline(storyboard_md)
    # If no outline parsed, try to get from settings outline
    if not outline and "outline" in settings:
        # settings outline is a JSON string? In phase-4 it's a JSON blob after title
        pass
    # Also need to parse outline from phase-4-build.md's outline table?
    # For now, if outline empty, create a simple one from sections seen in blocks
    if not outline:
        seen = {}
        for b in blocks:
            nid = b.get("node_id")
            sec = b.get("section")
            if nid and sec and nid not in seen:
                seen[nid] = sec
        outline = [{"id": nid, "kind": "section", "title": title} for nid, title in seen.items()]
    print(f"  Outline nodes: {len(outline)}")

    # Collect assets
    asset_map = collect_assets(module_dir, blocks)
    print(f"  Collected {len(asset_map)} placeholder assets (real + dummy)")

    # Create placeholder -> asset_id mapping and AssetInput list
    assets_input = []
    placeholder_to_asset_id: dict[str, str] = {}
    for ph, data in asset_map.items():
        # Use deterministic asset id: sanitize ph
        aid = "asset_" + re.sub(r"[^a-z0-9_-]", "_", ph.lower())
        # Ensure unique
        orig = aid
        idx = 1
        while aid in placeholder_to_asset_id.values():
            aid = f"{orig}_{idx}"
            idx += 1
        placeholder_to_asset_id[ph] = aid
        # Determine filename
        # If ph already has extension, use it; else infer from bytes header or default to .svg/.png
        filename = ph
        if "." not in filename:
            # Infer: if data starts with <svg then .svg else .png
            if data[:100].lstrip().startswith(b"<svg"):
                filename = ph + ".svg"
            elif data[:10].startswith(b"\x89PNG"):
                filename = ph + ".png"
            else:
                filename = ph + ".svg"
        # Determine mime via filename
        ext = Path(filename).suffix.lower()
        mime = "image/svg+xml" if ext == ".svg" else "image/png" if ext == ".png" else "application/octet-stream"
        assets_input.append({"id": aid, "filename": filename, "source": f"data:{mime};base64," + __import__("base64").b64encode(data).decode()})

    # Sanitize blocks and replace asset ids
    cleaned_blocks = []
    for b in blocks:
        cb = sanitize_block(b, asset_map)
        cb = replace_placeholder_asset_ids(cb, placeholder_to_asset_id)
        # Remove any remaining placeholder asset ids that we didn't map (should be none)
        for k in list(cb.keys()):
            if k.endswith("_asset_id") and isinstance(cb[k], str) and cb[k].startswith("<"):
                # Required field but no asset — for draft, drop if optional, or keep dummy
                # If required (hotspot image_asset_id), we must have a dummy; if we missed, create one
                ph = cb[k].strip("<>")
                if ph not in placeholder_to_asset_id:
                    # Create dummy now
                    dummy = dummy_svg_bytes(ph)
                    aid = "asset_" + re.sub(r"[^a-z0-9_-]", "_", ph.lower())
                    placeholder_to_asset_id[ph] = aid
                    assets_input.append({"id": aid, "filename": ph + ".svg", "source": f"data:image/svg+xml;base64," + __import__("base64").b64encode(dummy).decode()})
                    cb[k] = aid
                else:
                    cb[k] = placeholder_to_asset_id[ph]
        # Also clean nested blocks where asset_id might still be placeholder
        # For content_slide blocks, the asset_id field is inside blocks, not *_asset_id
        if "blocks" in cb and isinstance(cb["blocks"], list):
            for blk in cb["blocks"]:
                if isinstance(blk, dict) and "asset_id" in blk and isinstance(blk["asset_id"], str) and blk["asset_id"].startswith("<"):
                    ph = blk["asset_id"].strip("<>")
                    if ph in placeholder_to_asset_id:
                        blk["asset_id"] = placeholder_to_asset_id[ph]
                    else:
                        blk["asset_id"] = None

        # For simulation, hotspot, etc., ensure required asset fields are present
        # If image_asset_id is required but now None, we need to provide dummy
        if cb.get("type") == "hotspot" and not cb.get("image_asset_id"):
            # Provide dummy
            dummy_ph = f"dummy-hotspot-{cb['id']}"
            aid = "asset_" + re.sub(r"[^a-z0-9_-]", "_", dummy_ph)
            if aid not in [a["id"] for a in assets_input]:
                assets_input.append({"id": aid, "filename": dummy_ph + ".svg", "source": f"data:image/svg+xml;base64," + __import__("base64").b64encode(dummy_svg_bytes(dummy_ph)).decode()})
            cb["image_asset_id"] = aid
        if cb.get("type") == "labeled_diagram" and not cb.get("image_asset_id"):
            dummy_ph = f"dummy-labeled-{cb['id']}"
            aid = "asset_" + re.sub(r"[^a-z0-9_-]", "_", dummy_ph)
            if aid not in [a["id"] for a in assets_input]:
                assets_input.append({"id": aid, "filename": dummy_ph + ".svg", "source": f"data:image/svg+xml;base64," + __import__("base64").b64encode(dummy_svg_bytes(dummy_ph)).decode()})
            cb["image_asset_id"] = aid

        # For poll, ensure prompt_html exists
        # For decision_scenario, ensure nodes have image_asset_id if needed? It's optional

        cleaned_blocks.append(cb)

    # Build CourseSpec
    spec_dict: dict[str, Any] = {
        "title": title,
        "description": settings.get("description", ""),
        "scorm_version": scorm_version,
        "language": language,
        "tracking": tracking,
        "screens": cleaned_blocks,
        "assets": assets_input,
    }
    # Add objectives if any
    if objectives:
        spec_dict["objectives"] = [{"id": o["id"], "description": o["description"]} for o in objectives]
    # Add outline if any
    if outline:
        spec_dict["outline"] = outline

    # Also add theme? Keep default for draft
    # Validate via CourseSpec
    try:
        course_spec = CourseSpec.model_validate(spec_dict)
    except Exception as e:
        print(f"  CourseSpec validation failed: {e}")
        # Try to print details
        import traceback
        traceback.print_exc()
        # Attempt to fix by removing problematic screens
        raise

    print(f"  CourseSpec validated: {len(course_spec.screens)} screens, {len(course_spec.assets)} assets")

    # Now build Project and Package via Packager
    async def _build():
        tmpdir = tempfile.mkdtemp(prefix=f"scorm_{short}_")
        store = create_store(os.path.join(tmpdir, "scorm.db"), tmpdir)
        await store.init()
        packager = Packager(store, tmpdir, workers=2, renderer=renderer, public_base_url="http://localhost:8000", package_ttl_days=7)
        await packager.start_ttl_cleaner()
        project = Project(
            id=new_project_id(),
            title=course_spec.title,
            description=course_spec.description,
            scorm_version=course_spec.scorm_version,
            language=course_spec.language,
            tracking=course_spec.tracking,
            objectives=course_spec.objectives,
            outline=course_spec.outline,
            screens=course_spec.screens,
            assets=[],  # will be added via store
            owner_key_id="key_local",
        )
        # Need to add assets to store as AssetRef + bytes
        from core.project import AssetRef
        import hashlib
        for ai in course_spec.assets:
            # Decode data URI
            src = ai.source
            if src.startswith("data:"):
                # data:<mime>;base64,...
                b64 = src.split(",", 1)[1]
                data = __import__("base64").b64decode(b64)
            else:
                data = b""
            filename = ai.filename
            rel_path = f"assets/{filename}"
            # Derive mime and hashes
            import hashlib as _hashlib
            ext = Path(filename).suffix.lower()
            if ext == ".svg":
                mime = "image/svg+xml"
            elif ext == ".png":
                mime = "image/png"
            elif ext == ".jpg" or ext == ".jpeg":
                mime = "image/jpeg"
            elif ext == ".mp3":
                mime = "audio/mpeg"
            elif ext == ".mp4":
                mime = "video/mp4"
            else:
                # Try to parse from data URI
                if src.startswith("data:"):
                    mime = src[5:].split(";")[0] or "application/octet-stream"
                else:
                    mime = "application/octet-stream"
            size_bytes = len(data)
            sha256 = _hashlib.sha256(data).hexdigest()
            asset_ref = AssetRef(id=ai.id, filename=filename, mime=mime, size_bytes=size_bytes, sha256=sha256, rel_path=rel_path)
            project.assets.append(asset_ref)
            await store.put_asset(project.id, data, asset_ref)
        await store.create_project(project)
        # Validate project
        errs = validate_project(project)
        if errs:
            print(f"  validate_project: {len(errs)} errors")
            for err in errs[:10]:
                print(f"    - {err.code}: {err.message} at {err.path}")
        else:
            print("  validate_project: OK")

        # Build package sync
        # Need to gather asset bytes map
        assets_bytes = {}
        for a in project.assets:
            try:
                assets_bytes[a.id] = await store.get_asset_bytes(project.id, a.id)
            except FileNotFoundError:
                assets_bytes[a.id] = b""

        meta = packager.build_sync(project, assets_bytes)
        zip_path = Path(tmpdir) / meta.rel_path
        print(f"  Built package: {zip_path} ({zip_path.stat().st_size} bytes)")

        # Validate zip
        if validate:
            zerrs = validate_zip(str(zip_path), project.scorm_version)
            blocking = [e for e in zerrs if e.code != "schema_unavailable"]
            if blocking:
                print(f"  validate_zip: {len(blocking)} blocking errors")
                for e in blocking[:10]:
                    print(f"    - {e.code}: {e.message}")
            else:
                print("  validate_zip: OK (no blocking errors)")
            if any(e.code == "schema_unavailable" for e in zerrs):
                print("  (schema_unavailable warnings ignored)")

        # Copy zip to out_dir
        out_dir.mkdir(parents=True, exist_ok=True)
        dest = out_dir / f"{name}_{project.scorm_version}.zip"
        dest.write_bytes(zip_path.read_bytes())
        print(f"  Copied to {dest}")

        # Also write build report json alongside
        report = {
            "module": name,
            "title": project.title,
            "scorm_version": project.scorm_version,
            "screens": len(project.screens),
            "scored": sum(1 for s in project.screens if hasattr(s, "points") and getattr(s, "points", 0) > 0),
            "objectives": len(project.objectives),
            "outline_nodes": len(project.outline),
            "assets": len(project.assets),
            "points_total": sum(getattr(s, "points", 0) for s in project.screens if hasattr(s, "points")),
            "zip_path": str(dest),
            "zip_bytes": dest.stat().st_size,
            "validate_project_errors": [e.model_dump() if hasattr(e, "model_dump") else str(e) for e in errs],
            "validate_zip_blocking": len(blocking) if validate else None,
        }
        report_path = out_dir / f"{name}_build-report.json"
        report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  Report: {report_path}")

        # Cleanup: not deleting tmpdir for debugging? We'll keep it but also try to close store
        try:
            await store.close()
        except Exception:
            pass

        return report

    report = asyncio.run(_build())
    return report

def main():
    parser = argparse.ArgumentParser(description="Build draft SCORM packages for My Clinic modules")
    parser.add_argument("modules", nargs="*", help="Module folders (e.g. 03_hr-employee-induction)")
    parser.add_argument("--all", action="store_true", help="Build all 8 modules")
    parser.add_argument("--out", default=".generated/scorm", help="Output directory for zips and reports")
    parser.add_argument("--no-validate", action="store_true", help="Skip zip validation")
    args = parser.parse_args()

    if args.all:
        modules = sorted([p for p in ROOT.glob("0[1-8]_*") if p.is_dir()])
    elif args.modules:
        modules = []
        for m in args.modules:
            p = ROOT / m
            if not p.exists():
                # Try with prefix
                cand = list(ROOT.glob(f"*{m}*"))
                if cand:
                    p = cand[0]
                else:
                    print(f"Module not found: {m}", file=sys.stderr)
                    sys.exit(1)
            modules.append(p)
    else:
        # Default to 03+07 as per roadmap phase 1
        modules = [ROOT / "03_hr-employee-induction", ROOT / "07_quality-safety-and-risk"]

    out_dir = (REPO_ROOT / args.out) if not Path(args.out).is_absolute() else Path(args.out)
    out_dir = out_dir.resolve()
    print(f"Output dir: {out_dir}")
    print(f"Modules: {[p.name for p in modules]}")
    print(f"Edumints core: {EDUMINTS_PATH}")

    all_reports = []
    for mod in modules:
        try:
            report = build_module(mod, out_dir, validate=not args.no_validate)
            all_reports.append(report)
        except Exception as e:
            print(f"FAILED {mod.name}: {e}", file=sys.stderr)
            import traceback
            traceback.print_exc()
            sys.exit(1)

    # Write summary
    summary_path = out_dir / "scorm-build-summary.json"
    summary_path.write_text(json.dumps(all_reports, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n=== Summary written to {summary_path} ===")
    for r in all_reports:
        print(f"{r['module']}: {r['screens']} screens, {r['zip_bytes']} bytes, {r['scorm_version']}, validate errors: {len(r['validate_project_errors'])}")

if __name__ == "__main__":
    main()
