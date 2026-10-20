#!/usr/bin/env python3
"""Turn the video plan (video/_shared/plan/clips.json) into the production plan and per-clip draft files.

    python3 elearning-course/video/_shared/scripts/scaffold_clips.py            # check + write plan + new drafts
    python3 elearning-course/video/_shared/scripts/scaffold_clips.py --check    # check only (exit 1 on a problem)
    python3 elearning-course/video/_shared/scripts/scaffold_clips.py --force <clip-id>   # rewrite that clip's drafts

Checks, for every clip:
  * every motion cue phrase is spoken word for word in its scene (resolve_cues.py will need it later)
  * the interaction comes after a real scene, and every option has a spoken reply
  * estimated length (140 wpm + 0.3 s per line + 1.0 s between scenes) is within target_sec + 10 %
  * every character pose and every named storyboard asset exists

Writes:
  video/PRODUCTION-PLAN.md                         the plan for people and agents (always regenerated)
  video/<clip-id>/data/{BRIEF.md,facts.md,script.md,cues.json,visual_plan.json,interactions.json}
                                                   drafts, only when missing (never overwrites approved work)
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

V = Path(__file__).resolve().parents[2]
PLANS = V.parent / "scorm-plans"
CHARS = PLANS / "00_program" / "characters" / "assets"
WPM, LINE_GAP, SCENE_GAP = 140, 0.3, 1.0
words = lambda t: len(re.findall(r"[\w'’-]+", t))
norm = lambda t: re.sub(r"[^\w' ]", " ", t.lower()).split()


def seconds(lines: list[str]) -> float:
    return sum(words(l) for l in lines) / WPM * 60 + LINE_GAP * len(lines)


def module_dir(m: str) -> Path:
    return next(PLANS.glob(f"{m}_*"))


def asset_exists(name: str, mod: str) -> bool | None:
    """True/False for a recognisable asset reference, None when the text is a description, not a file."""
    m = re.match(r"(char-[\w-]+)\.png", name)
    if m:
        return (CHARS / f"{m.group(1)}.png").exists()
    m = re.match(r"((?:hs1|hs2|hr|ops|rcma|rcmb|qsr|ehr)-img-[\w-]+)", name)
    if m:
        return any((module_dir(mod) / "storyboard" / "assets").glob(m.group(1) + ".*"))
    return None


def check(c: dict) -> tuple[list[str], float]:
    bad = []
    ids = [s["id"] for s in c["scenes"]]
    for s in c["scenes"]:
        spoken = " " + " ".join(norm(" ".join(s["lines"]))) + " "
        for cue, _ in s["motion"]:
            if " " + " ".join(norm(cue)) + " " not in spoken:
                bad.append(f"{c['id']}/{s['id']}: cue “{cue}” is not spoken in the scene")
        if not (CHARS / f"{s['pose']}.png").exists():
            bad.append(f"{c['id']}/{s['id']}: pose {s['pose']} not in characters/assets")
        for a in s["visual"]["assets"]:
            if asset_exists(a, c["module"]) is False:
                bad.append(f"{c['id']}/{s['id']}: asset {a} not found")
    it = c.get("interaction")
    if it:
        if it["after_scene"] not in ids:
            bad.append(f"{c['id']}: interaction after unknown scene {it['after_scene']}")
        if any(not o.get("reply") for o in it["options"]):
            bad.append(f"{c['id']}: an interaction option has no reply")
    est = sum(seconds(s["lines"]) for s in c["scenes"]) + SCENE_GAP * (len(c["scenes"]) - 1)
    if est > c["target_sec"] * 1.1:
        bad.append(f"{c['id']}: estimated {est:.0f} s is over the {c['target_sec']} s target")
    return bad, est


def script_md(c: dict, voice: dict) -> str:
    out = [f"# Script — {c['id']}", "",
           f"> Speaker for every line: **{voice['name']}** (`omar`). One sentence per line. Do not add words without updating the cues.",
           "> Gate B: approved by ______ on ____-__-__", ""]
    for i, s in enumerate(c["scenes"], 1):
        out += [f"# SCENE {i} | {s['id']} | {s['title']}", "**Speaker:** omar", *s["lines"], ""]
    it = c.get("interaction")
    if it:
        out += [f"# INTERACTION | after {it['after_scene']} | unscored", "**Speaker:** omar", f"Q: {it['question']}"]
        out += [f"{o['id']}: {o['text']} → {o['reply']}" for o in it["options"]]
    return "\n".join(out) + "\n"


def visual_plan(c: dict) -> dict:
    return {"clip": c["id"], "fps": 30, "size": "1920x1080", "brand": "video/_shared/brand/tokens.css",
            "module_colour": c["colour"], "status": "draft — needs Gate C",
            "scenes": [{"id": s["id"], "title": s["title"], "goal": s["title"], "pose": s["pose"],
                        "layout": s["visual"]["layout"], "onScreenText": s["visual"]["on_screen"],
                        "assets": s["visual"]["assets"],
                        "beats": [{"cue": cue, "do": do} for cue, do in s["motion"]],
                        "mustNotShow": ["real staff, patients or screens", "logos except the supplied PNG",
                                        "any fact not in data/facts.md"]} for s in c["scenes"]]}


def brief_md(c: dict) -> str:
    return f"""# BRIEF — {c['id']}

| Field | Value |
|---|---|
| clip id | `{c['id']}` |
| module | {c['module']} |
| placement | {c['placement']} |
| route | narrated-explainer with one voice interaction |
| destination | lms (SCORM 1.2, Oracle Learning), unscored screen |
| aspect / fps | 1920x1080 master, 30 fps → 1280x720 SCORM encode |
| target length | {c['target_sec']} s of narration (the interaction pause is extra) |
| voice | Dr. Omar only (male), see video/PRODUCTION-PLAN.md §2 |
| captions | WebVTT with `<v Dr. Omar>` tags |
| music / sfx | off unless the owner says on |
| brand | video/_shared/brand/README.md, module colour `{c['colour']}` |

## Message
{c['message']}

## Audience
{c['audience']}

## Action
{c['action']}

## Proof
none

## Stated vs inferred
- **Stated:** see data/facts.md (every line has a source).
- **Inferred (needs OK):** {'; '.join(c.get('open') or ['nothing'])}

## Owner OK (Gate A)
- [ ] approved by ______ on ____-__-__
"""


def facts_md(c: dict) -> str:
    rows = "\n".join(f"| {i} | {f} | {src} | {st} |" for i, (f, src, st) in enumerate(c["facts"], 1))
    return f"""# Facts — {c['id']}

> Everything seen or heard. Never add a fact without a source. Pending facts keep their marker on screen and stay out of the narration.

| # | Fact | Source | Status |
|---|---|---|---|
{rows}

## Rejected or unverified
| Fact | Why it is out |
|---|---|
"""


def plan_md(data: dict, results: list[tuple[dict, list[str], float]]) -> str:
    v = data["voice"]
    L = [f"# Video production plan: 9 clips, voiced by Dr. Omar",
         "",
         "> Generated by `video/_shared/scripts/scaffold_clips.py` from `video/_shared/plan/clips.json`. **Edit the JSON, not this page**, then rerun the script.",
         f"> Owner brief ({data['version']}): {data['owner_brief'][len('Owner, 2026-10-20: '):] if data['owner_brief'].startswith('Owner, 2026-10-20: ') else data['owner_brief']}",
         "",
         "## 1. What this plan is",
         "",
         "There are nine short motion-graphics clips, one or two per course. Every scene below has four parts:",
         "",
         "- **Voice:** Dr. Omar's exact lines.",
         "- **Visual plan:** layout, on-screen text and assets.",
         "- **Motion plan:** what moves, on which spoken words.",
         "- **Voice interaction:** one pause per clip. Dr. Omar asks a question, the learner taps an answer, and Dr. Omar replies.",
         "",
         "Each clip's working files are drafted in `video/<clip-id>/data/`. The procedure, the gates and the checks are in [`README.md`](README.md) and [`../scorm-plans/00_program/video-playbook-review.md`](../scorm-plans/00_program/video-playbook-review.md) §5.",
         "",
         "Every facts table marks what is confirmed and what is still pending. **A pending fact is never spoken.** It is shown on screen only with its `⚠` tag.",
         "",
         "## 2. The voice: Dr. Omar (male)",
         "",
         f"- **Who:** {v['description']}",
         f"- **Rule:** {v['rule']}",
         "- **Audition:** for Gate D, record 30–45 words of `prog-vid-welcome` scenes 1–2 in two candidate male voices. Use one voice from the D10 English neural TTS provider and one free baseline (for example a Kokoro male voice through `npx hyperframes tts`). The owner picks by ear. Record the provider, voice, model and settings in `narration/tts_settings.json`. **Use the same voice for all nine clips.**",
         "- **Delivery:** warm, unhurried, smiling but never salesy. Pause 0.3 s between lines and about 1 s between scenes. Concern lines (`char-omar-concern`) are slower and lower, never dramatic.",
         "- **Pronunciation:** Omar = “OH-mar”, CBAHI = “see-bah-hee”, RACE = “race”, EHR = “E-H-R”, ICD = “I-C-D”, SCFHS = “S-C-F-H-S”, Mumaris = “mu-MAH-ris”, Qiwa = “KEE-wa”, J2 = “J two”. The full lexicon is in `00_program/narration-and-lexicon.md` §4. Apply fixes in the TTS `PRON` map, never in the script.",
         "- **Files:**",
         "  - one file per scene, `narration/sceneNN_omar.mp3`;",
         "  - the interaction question, `narration/int_q_omar.mp3`;",
         "  - one reply per option, `narration/int_<option-id>_omar.mp3`.",
         "  - Format: MP3, 44.1 kHz, mono, −16 LUFS, 300 ms head and tail. After Gate D the voice is frozen: never trim or stretch it.",
         "",
         "## 3. How a voice interaction works",
         "",
         "1. The clip plays to the end of the scene named in `after_scene`, then pauses.",
         "2. The player puts a question card over the frozen frame and plays the question audio. The answer options show as large buttons; captions are on.",
         "3. The learner taps an answer. The player plays that option's reply audio. The option is marked ✓ (correct) or with a neutral highlight, and a short caption shows.",
         "4. **Continue** (or the end of the reply audio) resumes the clip. The interaction is **never scored**. It can be skipped with **Skip**, and it works by keyboard.",
         "5. The data is in `data/interactions.json`. The pause time comes from the narration: `resolve_cues.py` resolves the cue `int-pause` (the last words of `after_scene`) to a time in seconds.",
         "6. **Player support is needed first** (task V0 in §5): a `video` screen with `interactions`. Until it exists, a clip can still be delivered as plain video. Put the question and replies after it as a normal unscored branching screen.",
         "",
         "## 4. Clips",
         ""]
    for c, bad, est in results:
        it = c.get("interaction")
        L += [f"### {c['id']} · {c['title']}",
              "",
              f"| Module | Placement | Target | Estimated narration | Colour |",
              f"|---|---|---|---|---|",
              f"| {c['module']} | {c['placement']} | {c['target_sec']} s | {est:.0f} s | `{c['colour']}` |",
              "",
              f"- **Message:** {c['message']}",
              f"- **Audience:** {c['audience']}",
              f"- **Learner action:** {c['action']}"]
        if c.get("open"):
            L += [f"- **Open questions for the owner:** " + " · ".join(c["open"])]
        if bad:
            L += [f"- **⚠ Plan check:** " + "; ".join(bad)]
        L += ["", "| # | Scene | Dr. Omar says | Visual plan | Motion plan (cue → what moves) |", "|---|---|---|---|---|"]
        for i, s in enumerate(c["scenes"], 1):
            say = "<br>".join(s["lines"])
            vis = f"{s['visual']['layout']}.<br>**Text:** " + " · ".join(s['visual']['on_screen']) + (
                f"<br>**Assets:** " + ", ".join(f"`{a}`" for a in s['visual']['assets']) if s['visual']['assets'] else "") + f"<br>**Pose:** `{s['pose']}`"
            mot = "<br>".join(f"“{cue}” → {do}" for cue, do in s["motion"])
            L.append(f"| {i} | **{s['title']}** (`{s['id']}`) | {say} | {vis} | {mot} |")
            if it and it["after_scene"] == s["id"]:
                opts = "<br>".join(f"{'✓ ' if o.get('correct') else ''}**{o['text']}** → “{o['reply']}”" for o in it["options"])
                L.append(f"| ⏸ | **Voice interaction** (unscored) | “{it['question']}” | Frozen frame dimmed 40 %; question card centre; {len(it['options'])} answer buttons | Card rises (400 ms); buttons stagger in 80 ms; tap → reply plays, chosen button highlights<br>{opts} |")
        L.append("")
    L += ["## 5. Tasks for the video agent, in order",
          "",
          "| # | Task | Done when |",
          "|---|---|---|",
          "| V0 | **Player support for interactive video** (a player task, not a content task: `tools/player/`). Add a `video` screen with a `.vtt` track, a poster, `interactions[]` (pause time, question audio, options with reply audio), Skip and Continue, keyboard, and reduced motion (poster + transcript). | `check_packages.py` passes for every module and a test video pauses, asks, replies and resumes |",
          "| V1 | Gate A for all nine: read `data/BRIEF.md` and `data/facts.md`, fix anything wrong, and send them to the owner with the open questions in §4 | Owner OK recorded in each BRIEF |",
          "| V2 | Gate B: owner or SME approves each `data/script.md` (lines and interaction wording) | Approval line filled in |",
          "| V3 | Voice audition and choice (§2), then record every clip: scenes + question + replies | Gate D OK; `narration/` complete; LUFS printed −16 ± 1 |",
          "| V4 | Storyboard board from `data/visual_plan.json` (Gate C), then build in HyperFrames with the shared components; `resolve_cues.py` exit 0 | Gate C and Gate E OK |",
          "| V5 | Render, `encode_scorm.sh`, `srt_to_vtt.py`, `delivery_check.py` all PASS; transcript HTML and poster frame | QA_REPORT.md filled with pasted output |",
          "| V6 | Owner approves the draft (Gate F). Copy the files to `target_file` / `captions_file`. Add the video screen to the module's `production/personalisation.json` (`insert_after`, unscored). Rebuild and run every AGENT-TASKS §3 check | `check_packages.py` failures=0, and the screen is visible in preview |",
          "",
          "Start with `prog-vid-welcome` (it sets the voice and the look), then `qsr-vid-speakup`, then the rest in module order.",
          ""]
    return "\n".join(L)


def main() -> int:
    args = sys.argv[1:]
    data = json.loads((V / "_shared" / "plan" / "clips.json").read_text())
    results, problems = [], 0
    for c in data["clips"]:
        bad, est = check(c)
        problems += len(bad)
        results.append((c, bad, est))
        print(f"{c['id']}: {len(c['scenes'])} scenes · ~{est:.0f} s of {c['target_sec']} s" + ("" if not bad else " · " + "; ".join(bad)))
    if "--check" in args:
        return 1 if problems else 0
    (V / "PRODUCTION-PLAN.md").write_text(plan_md(data, results))
    force = set(args[args.index("--force") + 1:]) if "--force" in args else set()
    for c, _, _ in results:
        d = V / c["id"] / "data"
        d.mkdir(parents=True, exist_ok=True)
        it = c.get("interaction")
        last = c["scenes"][[s["id"] for s in c["scenes"]].index(it["after_scene"])]["lines"][-1] if it else ""
        cues = {f"s{i:02d}-{s['id']}-{k}": cue for i, s in enumerate(c["scenes"], 1) for k, (cue, _) in enumerate(s["motion"], 1)}
        if it:
            cues["int-pause"] = " ".join(norm(last)[-3:])
        files = {"BRIEF.md": brief_md(c), "facts.md": facts_md(c), "script.md": script_md(c, data["voice"]),
                 "cues.json": json.dumps(cues, indent=1, ensure_ascii=False) + "\n",
                 "visual_plan.json": json.dumps(visual_plan(c), indent=1, ensure_ascii=False) + "\n"}
        if it:
            files["interactions.json"] = json.dumps({"clip": c["id"], "scored": False, "pause_cue": "int-pause",
                                                     "question": it["question"], "question_audio": "narration/int_q_omar.mp3",
                                                     "options": [{**o, "reply_audio": f"narration/int_{o['id']}_omar.mp3"} for o in it["options"]]},
                                                    indent=1, ensure_ascii=False) + "\n"
        for name, text in files.items():
            p = d / name
            if not p.exists() or c["id"] in force:
                p.write_text(text)
    print(f"wrote {V / 'PRODUCTION-PLAN.md'} · problems={problems}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
