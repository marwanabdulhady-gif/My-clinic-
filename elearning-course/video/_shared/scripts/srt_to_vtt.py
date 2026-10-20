#!/usr/bin/env python3
"""Convert the generated captions.srt to the WebVTT file the SCORM video screen loads.

Speaker tags (<v Noor> / <v Dr. Omar>) come from data/narration_manifest.json when it exists
(one entry per scene clip with start/end seconds and a speaker), else from --speaker.

    python3 srt_to_vtt.py data/captions.srt data/<clip-id>.vtt [--manifest data/narration_manifest.json]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

NAMES = {"noor": "Noor", "omar": "Dr. Omar"}
TS = re.compile(r"(\d+):(\d+):(\d+)[,.](\d+)")


def sec(t: str) -> float:
    h, m, s, ms = TS.match(t.strip()).groups()
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


def vtt_ts(x: float) -> str:
    h, r = divmod(x, 3600)
    m, s = divmod(r, 60)
    return f"{int(h):02d}:{int(m):02d}:{s:06.3f}"


def speakers(manifest: Path | None, default: str | None):
    spans = []
    if manifest and manifest.exists():
        data = json.loads(manifest.read_text())
        for e in (data.get("scenes", []) if isinstance(data, dict) else data):
            sp = NAMES.get(str(e.get("speaker", "")).lower())
            if sp and "start" in e and "end" in e:
                spans.append((float(e["start"]), float(e["end"]), sp))
    return lambda t: next((s for a, b, s in spans if a <= t < b), default)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("srt"); ap.add_argument("vtt")
    ap.add_argument("--manifest", default="data/narration_manifest.json")
    ap.add_argument("--speaker", help="fallback speaker name for every cue")
    a = ap.parse_args()
    who = speakers(Path(a.manifest), a.speaker)
    blocks = re.split(r"\n\s*\n", Path(a.srt).read_text(encoding="utf-8-sig").strip())
    out, last = ["WEBVTT", ""], -1.0
    for b in blocks:
        lines = [l for l in b.strip().splitlines() if l.strip()]
        if len(lines) < 3 or "-->" not in lines[1]:
            print(f"bad cue: {lines[:2]}", file=sys.stderr); return 1
        start, end = (sec(x) for x in lines[1].split("-->"))
        if start < last or end <= start:
            print(f"overlapping or empty cue at {lines[1]}", file=sys.stderr); return 1
        last = end
        text = " ".join(lines[2:])
        sp = who(start)
        out += [f"{vtt_ts(start)} --> {vtt_ts(end)}", f"<v {sp}>{text}" if sp else text, ""]
    Path(a.vtt).write_text("\n".join(out), encoding="utf-8")
    print(f"{a.vtt}: {len(blocks)} cues")
    return 0


if __name__ == "__main__":
    sys.exit(main())
