#!/usr/bin/env python3
"""Rewrite narration safely: export a worksheet, fill it in, apply it (gap G11).

Six packs (01, 02, 04, 05, 06, 08) carry generic filler sentences in their narration. Rewriting
them by hand means keeping three files in step; this tool does it:

  export <module>   write <module>/production/narration-rewrite.csv — one row per segment that
                    still contains filler: the screen, what the learner sees, the current text,
                    the filler found, the text with the filler removed (a starting point), the
                    target length, and an empty ``new_text`` column
  apply  <module>   read the worksheet and, for every row with ``new_text``:
                    check it (speaker label, no filler, length, no "correct answer" wording on
                    scored screens), then write it to storyboard/narration-script.json, the
                    screen's narration_text (captions) in build/screens.json, and regenerate
                    audio-script-export.json + voice_talent.md
  check  <module>   list the segments that still contain filler

    python3 elearning-course/scorm-plans/tools/narration_rewrite.py export 04_operations-and-my-care
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audio_export  # noqa: E402
from narration_filler import filler_in  # noqa: E402

PLANS = Path(__file__).resolve().parents[1]
FIELDS = ["screen_id", "part", "speaker", "screen_type", "scored", "screen_title", "on_screen_text",
          "target_sec", "target_words", "current_text", "filler_found", "without_filler", "new_text"]
CAPTION_NAME = {"NOOR": "Noor", "OMAR": "Dr. Omar"}
ANSWER_WORDS = re.compile(r"\b(the (correct|right) answer|answer is|choose option|pick option)\b", re.I)


def screens_of(mdir: Path) -> dict[str, dict]:
    p = mdir / "build" / "screens.json"
    return {s["id"]: s for s in json.loads(p.read_text())} if p.exists() else {}


def export(module: str) -> Path:
    mdir = PLANS / module
    script = audio_export.load_script(mdir)
    screens = screens_of(mdir)
    out = mdir / "production" / "narration-rewrite.csv"
    out.parent.mkdir(exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        for seg in script["segments"]:
            found = filler_in(seg["narration"])
            if not found:
                continue
            kept = seg["narration"]
            for line in found:
                kept = kept.replace(line, "")
            kept = re.sub(r"\s{2,}", " ", kept).strip()
            s = screens.get(seg["screen_id"], {})
            w.writerow({
                "screen_id": seg["screen_id"], "part": seg.get("part", ""), "speaker": seg.get("speaker", ""),
                "screen_type": s.get("type", ""), "scored": "yes" if s.get("points") else "no",
                "screen_title": s.get("title", ""), "on_screen_text": seg.get("on_screen_text", ""),
                "target_sec": seg.get("target_sec", ""),
                "target_words": round(float(seg.get("target_sec") or 0) * audio_export.WPM / 60),
                "current_text": seg["narration"], "filler_found": " | ".join(found),
                "without_filler": kept, "new_text": ""})
    return out


def problems(row: dict) -> list[str]:
    text = row["new_text"].strip()
    label = text.split(":", 1)[0]
    errs = []
    if label not in CAPTION_NAME:
        errs.append("must start with NOOR: or OMAR:")
    elif label.lower() != (row["speaker"] or label).lower():
        errs.append(f"speaker changed ({row['speaker']} → {label.lower()}); keep the same voice")
    if filler_in(text):
        errs.append(f"still contains filler: {filler_in(text)}")
    words = len(text.split(":", 1)[-1].split())
    target = int(float(row["target_words"] or 0))
    if target and not (0.6 * target <= words <= 1.15 * target):
        errs.append(f"{words} words; aim for {int(0.6 * target)}–{int(1.15 * target)}")
    if row["scored"] == "yes" and ANSWER_WORDS.search(text):
        errs.append("scored screen: the narration must not give the answer")
    if "⚠" in text or "PENDING" in text.upper():
        errs.append("no pending markers in spoken text; leave open facts out of the narration")
    return errs


def apply(module: str) -> int:
    mdir = PLANS / module
    rows = list(csv.DictReader((mdir / "production" / "narration-rewrite.csv").open(encoding="utf-8")))
    todo = [r for r in rows if r["new_text"].strip()]
    bad = {f"{r['screen_id']}/{r['part']}": problems(r) for r in todo}
    bad = {k: v for k, v in bad.items() if v}
    if bad:
        for k, v in bad.items():
            print(f"REFUSED {k}: " + "; ".join(v))
        print(f"{len(bad)} row(s) refused — nothing written. Fix them and run apply again.")
        return 1
    script = audio_export.load_script(mdir)
    by_key = {(r["screen_id"], r["part"]): r["new_text"].strip() for r in todo}
    for seg in script["segments"]:
        new = by_key.get((seg["screen_id"], seg.get("part", "")))
        if new:
            seg["narration"] = new
    audio_export.write_outputs(mdir, script)
    sp = mdir / "build" / "screens.json"
    if sp.exists():
        screens = json.loads(sp.read_text())
        changed = {r["screen_id"] for r in todo}
        for s in screens:
            if s["id"] in changed:
                parts = [g["narration"] for g in script["segments"] if g["screen_id"] == s["id"]]
                s["narration_text"] = " ".join(
                    CAPTION_NAME[p.split(":", 1)[0]] + ":" + p.split(":", 1)[1] if p.split(":", 1)[0] in CAPTION_NAME else p
                    for p in parts)
        sp.write_text(json.dumps(screens, ensure_ascii=False, indent=1))
    print(f"{module}: {len(todo)} segment(s) rewritten; {check(module, quiet=True)} still contain filler")
    return 0


def check(module: str, quiet: bool = False) -> int:
    script = audio_export.load_script(PLANS / module)
    left = [s for s in script["segments"] if filler_in(s["narration"])]
    if not quiet:
        for s in left:
            print(f"{s['screen_id']}/{s.get('part', '')}: {filler_in(s['narration'])}")
        print(f"{module}: {len(left)} of {len(script['segments'])} segments still contain filler")
    return len(left)


if __name__ == "__main__":
    cmd, module = sys.argv[1], sys.argv[2]
    if cmd == "export":
        print(export(module))
    elif cmd == "apply":
        sys.exit(apply(module))
    else:
        check(module)
