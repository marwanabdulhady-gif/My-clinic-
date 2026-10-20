#!/usr/bin/env python3
"""Write one machine-readable media job list per module for the image, audio and video agents.

Every asset a package still needs becomes one job with everything an agent needs to make it and
a reviewer needs to accept it: route, target file, size, prompt or script, the screens that use
it, the hotspot regions the picture must show, the gate that blocks it and the acceptance checks.
Nothing here generates media; agents read the job list, produce the file, and set ``status``.

Inputs (all already in the repo):
  * ``<module>/build/asset-map.json``             which ids are files and which are PENDING
  * ``<module>/build/course-spec.json``           where each asset is used, hotspot regions
  * ``<module>/storyboard/asset-register.md``     brief, kind, route, alt text, gate
  * ``<module>/storyboard/narration-script.json`` narration segments (audio jobs)
  * ``00_program/visual-generation-prompts.md``   approved prompts + shared style suffix
  * ``00_program/media-video-plan.json``          the optional motion-graphics clips

Outputs:
  * ``<module>/production/media-jobs.json``
  * ``00_program/media-jobs-summary.md`` (programme roll-up)

    python3 elearning-course/scorm-plans/tools/build_media_jobs.py
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

PLANS = Path(__file__).resolve().parents[1]
PROG = PLANS / "00_program"
MODULES = sorted(p.name for p in PLANS.glob("0[1-8]_*") if p.is_dir())
PAD_LINES = (  # generic filler the storyboard assembler adds to reach target length (gap G11)
    "Pause and connect this to your role.", "Use the principle in context.", "Keep the next action clear.",
    "Think of the first detail you would check.", "Apply the point to a familiar task.",
    "Carry the idea into your next decision.", "Notice which part of this you would use first on shift.",
    "Link it to the task waiting for you tomorrow.", "Use the rule you practised.",
    "Focus on the action that fits.", "Choose the option you would defend to a colleague.",
)
VOICES = {"noor": "Noor — female, early-to-mid 30s, warm, calm, clear",
          "omar": "Dr. Omar — male, late 30s, friendly, confident, medium-low pitch"}


def prompts() -> tuple[str, dict[str, str]]:
    text = (PROG / "visual-generation-prompts.md").read_text()
    m = re.search(r"## Shared style suffix.*?```text\n(.*?)```", text, re.S)
    suffix = m.group(1).strip() if m else ""
    out = {}
    for aid, body in re.findall(r"### `([a-z0-9-]+)`[^\n]*\n.*?```text\n(.*?)```", text, re.S):
        out[aid] = body.strip()
    return suffix, out


def register(mdir: Path) -> dict[str, dict]:
    rows = {}
    for line in (mdir / "storyboard" / "asset-register.md").read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 6 and re.fullmatch(r"`[a-z0-9-]+`", cells[0]) and not cells[1].startswith("["):
            aid = cells[0].strip("`")
            if len(cells) >= 8 or aid not in rows:
                rows[aid] = {"kind": cells[1], "screens": cells[2], "brief": cells[3], "route": cells[4],
                             "alt": cells[5].strip('"“” '), "gate": cells[7] if len(cells) >= 8 else ""}
    return rows


def route_for(aid: str, reg: dict) -> str:
    r, k = reg.get("route", "").lower(), reg.get("kind", "").lower()
    if "mp4" in k or "vtt" in k or "video" in k or "mp4" in r or "vtt" in r:
        return "blocked-mp4-vtt"
    if "oracle" in aid or "ehr-shot" in aid:
        return "capture"          # test-environment screenshot, never generated
    if "leaders" in aid:
        return "client-photo-or-role-tile"
    if "photo" in k or "with permission" in r:
        return "client-photo"
    if "pdf" in aid:
        return "own-pdf"
    if "svg" in k or r.startswith("own") or "diagram" in k or "pictogram" in k or "icon" in k:
        return "own-svg"
    return "ai-image"


def usage(spec: dict) -> dict[str, list[dict]]:
    """asset id -> the screens that use it, with the regions a hotspot picture must show."""
    out: dict[str, list[dict]] = {}

    def walk(o, screen):
        if isinstance(o, dict):
            for k, v in o.items():
                if isinstance(v, str) and k.endswith("asset_id"):
                    u = {"screen_id": screen["id"], "type": screen["type"], "field": k,
                         "scored": bool(screen.get("points"))}
                    if screen["type"] in {"hotspot", "labeled_diagram"} and screen.get("regions"):
                        u["mode"] = screen.get("mode", "find")
                        u["regions"] = [{"id": r["id"], "label": re.sub("<[^>]+>", "", r.get("label_html") or r.get("label") or r["id"]),
                                         "correct": r.get("correct"), "coords": r.get("coords")}
                                        for r in screen["regions"]]
                    out.setdefault(v, []).append(u)
                else:
                    walk(v, screen)
        elif isinstance(o, list):
            for x in o:
                walk(x, screen)
    for s in spec["screens"]:
        walk(s, s)
    return out


def image_job(aid: str, mdir: Path, reg: dict, uses: list[dict], amap: dict, suffix: str, pr: dict, colour: str) -> dict:
    route = route_for(aid, reg)
    hotspot = [u for u in uses if u.get("regions")]
    exists = any((mdir / "storyboard" / "assets" / f"{aid}{e}").exists() for e in (".svg", ".png", ".jpg"))
    blocked = route == "blocked-mp4-vtt"
    job = {
        "id": aid, "media": "video" if blocked else "image", "route": route,
        "status": "blocked" if blocked else (
            "done" if (amap.get("status") == "file" and not amap.get("interim")) or exists else "todo"
        ),
        "target_file": (f"{mdir.name}/storyboard/assets/{aid}.mp4" if blocked
                        else f"{mdir.name}/storyboard/assets/{aid}{'.svg' if route == 'own-svg' else '.png'}"),
        "size_px": None if blocked or route == "own-svg" else [1920, 1080],
        "screens": sorted({u["screen_id"] for u in uses}) or [s.strip("` ") for s in reg.get("screens", "").split(",") if s.strip()],
        "brief": reg.get("brief", ""), "alt_text": reg.get("alt", ""),
        "gate": reg.get("gate") or amap.get("gate", ""),
    }
    if route == "ai-image":
        body = pr.get(aid) or f"{reg.get('brief', aid)}. Module highlight colour {colour}."
        job["prompt"] = body + ("\n\n" + suffix if suffix and "shared style suffix" not in body.lower() else "")
        if "shared style suffix" in body.lower():
            job["prompt"] = body + "\n\n" + suffix
    if hotspot:
        job["hotspots"] = {
            "rule": "Every listed item must be clearly visible, separate and at least 48 px at 960×540. "
                    "After generating, map one box per region into production/hotspots/<asset-id>.json "
                    "(tools/map_hotspots.py) — coordinates are not guessed in the storyboard.",
            "screens": [{"screen_id": u["screen_id"], "mode": u["mode"], "scored": u["scored"],
                         "regions": u["regions"]} for u in hotspot],
            "extra_regions_allowed": all(not u["scored"] or u["mode"] == "explore" for u in hotspot),
        }
    job["acceptance"] = [
        "Matches the brief; nothing beyond it (no extra hazards, people or objects).",
        "No text, numbers, logos, identifiers or real likenesses in the pixels; labels stay in HTML.",
        "Brand palette: navy #003867 outlines, light surfaces, one module highlight.",
        "Provenance recorded (generator, model, date, prompt) in PROVENANCE.json via add_asset.",
    ] + (["Hotspot boxes mapped and checked on the overlay preview."] if hotspot else [])
    return job


def layer_image_jobs(mdir: Path, colour: str, suffix: str, have: set[str]) -> list[dict]:
    """Pictures a staged personalisation step waits for (new explore hotspots on new pictures)."""
    p = mdir / "production" / "personalisation.json"
    if not p.exists():
        return []
    out = []
    for sid, step in json.loads(p.read_text()).get("convert", {}).items():
        aid = step.get("requires_asset")
        if not aid or aid in have:
            continue
        done = any((mdir / "storyboard" / "assets" / f"{aid}{e}").exists() for e in (".png", ".jpg", ".svg"))
        out.append({
            "id": aid, "media": "image", "route": "ai-image", "status": "done" if done else "todo",
            "target_file": f"{mdir.name}/storyboard/assets/{aid}.png", "size_px": [1920, 1080], "screens": [sid],
            "brief": step.get("brief", ""), "alt_text": step.get("image_alt", ""),
            "prompt": f"{step.get('brief', '')} Module highlight colour {colour}.\n\n{suffix}",
            "gate": "Unscored explore screen (personalisation layer); SME confirms the items",
            "hotspots": {"rule": "Every listed item must be clearly visible, separate and at least 48 px at 960×540. "
                                  "Map the boxes with tools/map_hotspots.py init/preview after generating.",
                         "screens": [{"screen_id": sid, "mode": "explore", "scored": False,
                                      "regions": [{"id": r["id"], "label": re.sub("<[^>]+>", "", r["label_html"])} for r in step["regions"]]}],
                         "extra_regions_allowed": True},
            "acceptance": ["Matches the brief; nothing beyond it.", "No text, numbers or logos in the pixels.",
                           "Hotspot boxes mapped and checked on the overlay preview.", "Provenance recorded."],
            "unlocks": f"{sid} becomes an explore hotspot when this file exists"})
    return out


def audio_jobs(mdir: Path, prefix: str) -> list[dict]:
    p = mdir / "storyboard" / "narration-script.json"
    if not p.exists():
        return []
    n = json.loads(p.read_text())
    jobs = []
    for seg in n["segments"]:
        text = seg.get("narration", "")
        pads = [l for l in PAD_LINES if l in text]
        speakers = sorted(set(re.findall(r"^(NOOR|OMAR):", text, re.M))) or [seg.get("speaker", "").upper()]
        jobs.append({
            "id": f"{prefix}-aud-{seg['screen_id'].split('-', 1)[1]}", "media": "audio", "route": "tts",
            "status": "blocked-rewrite" if pads else (
                "done" if (mdir / "storyboard" / "audio" / f"{prefix}-aud-{seg['screen_id'].split('-', 1)[1]}.mp3").exists() else "todo"),
            "target_file": f"{mdir.name}/storyboard/audio/{prefix}-aud-{seg['screen_id'].split('-', 1)[1]}.mp3",
            "screens": [seg["screen_id"]], "speakers": [s.title() for s in speakers if s],
            "voices": [VOICES[s.lower()] for s in speakers if s and s.lower() in VOICES],
            "script": text, "target_sec": seg.get("target_sec"), "tone": seg.get("tone"),
            "filler_lines": pads,
            "format": "MP3 44.1 kHz mono 96 kbps, −16 LUFS integrated, −1 dBTP, 300 ms head/tail",
            "captions": "WebVTT from the final audio (forced alignment), speaker names as <v Noor>/<v Dr. Omar>",
            "lexicon": "storyboard/voice_talent.md + 00_program/narration-and-lexicon.md",
            "gate": "D10 voices approved; filler lines rewritten from the source first" if pads else "D10 voices approved",
        })
    return jobs


def video_jobs(module: str) -> list[dict]:
    p = PROG / "media-video-plan.json"
    if not p.exists():
        return []
    return [dict(v, media="video") for v in json.loads(p.read_text())["clips"] if v["module"] == module[:2]]


def main() -> None:
    suffix, pr = prompts()
    summary = []
    for module in MODULES:
        mdir = PLANS / module
        spec_p = mdir / "build" / "course-spec.json"
        if not spec_p.exists():
            continue
        spec = json.loads(spec_p.read_text())
        amap = json.loads((mdir / "build" / "asset-map.json").read_text())["assets"]
        reg = register(mdir)
        uses = usage(spec)
        prefix = spec["screens"][0]["id"].split("-")[0]
        colour = (re.search(r"module colour \*\*[^#*]*(#[0-9A-Fa-f]{6})", (mdir / "README.md").read_text()) or [None, ""])[1]
        ids = [a for a in dict.fromkeys(list(amap) + list(reg)) if not a.startswith(("_", "char-", "brand-", "font-"))]
        def row(a: str) -> dict:  # unregistered parts of a set (hr-img-7c-cure) inherit the set's row
            if a in reg:
                return reg[a]
            return next((dict(v, brief=f"Part of {k}: {v['brief']}") for k, v in reg.items()
                         if k.endswith("-icons") and a.startswith(k[:-len("icons")])), {})
        images = [image_job(a, mdir, row(a), uses.get(a, []), amap.get(a, {}), suffix, pr, colour) for a in ids]
        images += layer_image_jobs(mdir, colour, suffix, {j["id"] for j in images})
        jobs = images + audio_jobs(mdir, prefix) + video_jobs(module)
        out = mdir / "production"
        out.mkdir(exist_ok=True)
        prev = out / "media-jobs.json"
        if prev.exists():  # keep what agents and reviewers recorded on earlier runs
            kept = {j["id"]: j for j in json.loads(prev.read_text())["jobs"]}
            for j in jobs:
                old = kept.get(j["id"], {})
                for k in ("made_by", "tool", "model", "date", "prompt_used", "reviewed_by", "notes"):
                    if k in old:
                        j[k] = old[k]
                # a review/approval survives only while the file it was given for is still there
                if old.get("status") in {"review", "approved"} and (j["media"] != "image" or j["status"] == "done"):
                    j["status"] = old["status"]
        (out / "hotspots").mkdir(exist_ok=True)
        (out / "media-jobs.json").write_text(json.dumps(
            {"module": module, "module_colour": colour, "generated_by": "tools/build_media_jobs.py",
             "agent_runbook": "00_program/media-production-runbook.md", "jobs": jobs},
            ensure_ascii=False, indent=1))
        c = Counter((j["media"], j["route"], j["status"]) for j in jobs)
        summary.append((module, c, sum(1 for j in images if j.get("hotspots"))))
        print(f"{module}: {len(jobs)} jobs")

    lines = ["# Media jobs — programme roll-up", "",
             "Generated by `tools/build_media_jobs.py` from the asset maps, registers, narration scripts and the video plan. "
             "Each module's full list is `<module>/production/media-jobs.json`; agents follow [`media-production-runbook.md`](media-production-runbook.md).", "",
             "| Module | Images to make (AI) | Own SVG/PDF to draw | Client photos / captures | Pictures needing hotspot mapping | Audio clips | Audio blocked by filler text | Optional videos | Done |",
             "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    tot = Counter()
    for module, c, hs in summary:
        def n(media=None, route=None, status=None, not_status=None):
            return sum(v for (m, r, s), v in c.items() if (media is None or m == media) and (route is None or r in route)
                       and (status is None or s == status) and (not_status is None or s != not_status))
        row = [n("image", ("ai-image",), not_status="done"), n("image", ("own-svg", "own-pdf"), not_status="done"),
               n("image", ("client-photo", "capture", "client-photo-or-role-tile"), not_status="done"), hs,
               n("audio"), n("audio", status="blocked-rewrite"), n("video"), n(status="done")]
        tot.update(dict(enumerate(row)))
        lines.append(f"| {module} | " + " | ".join(map(str, row)) + " |")
    lines.append("| **Total** | " + " | ".join(f"**{tot[i]}**" for i in range(8)) + " |")
    lines += ["", "Audio *blocked by filler text*: the storyboard assembler padded these segments with generic lines "
              "(\"Keep the next action clear.\") to reach the target length. Rewrite them from the source before any TTS run "
              "(programme status G11)."]
    (PROG / "media-jobs-summary.md").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
