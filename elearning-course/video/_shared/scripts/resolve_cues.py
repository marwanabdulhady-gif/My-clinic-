#!/usr/bin/env python3
"""Turn spoken-phrase cues into times, and fail loudly when a phrase is not in the narration.

HyperFrames reads animation start times from data attributes, so nothing stops a cue drifting if
the narration changes. This script is the guard: every cue in data/cues.json names the phrase it
waits for; the time comes from the word timestamps of the real recording.

    data/cues.json            {"scene02-extinguisher": "fire extinguisher", ...}
    data/transcript_words.json  [{"word": "fire", "start": 12.31, "end": 12.6}, ...]  (or {"words": [...]})
    -> src/data/cues.json     {"scene02-extinguisher": 12.31, ...}

Exit 0 = all cues found · 1 = a phrase is missing (lists every missing cue) · 2 = bad input.

    python3 resolve_cues.py [--cues data/cues.json] [--words data/transcript_words.json] [--out src/data/cues.json]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

norm = lambda w: re.sub(r"[^\w']", "", w.lower())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cues", default="data/cues.json")
    ap.add_argument("--words", default="data/transcript_words.json")
    ap.add_argument("--out", default="src/data/cues.json")
    a = ap.parse_args()
    try:
        cues = json.loads(Path(a.cues).read_text())
        words = json.loads(Path(a.words).read_text())
        words = words.get("words", words) if isinstance(words, dict) else words
        seq = [(norm(w.get("word") or w.get("text", "")), float(w["start"])) for w in words]
    except Exception as e:  # noqa: BLE001
        print(f"bad input: {e}", file=sys.stderr)
        return 2
    toks = [t for t, _ in seq]
    out, missing = {}, []
    for cue, phrase in cues.items():
        p = [norm(x) for x in phrase.split() if norm(x)]
        hit = next((i for i in range(len(toks) - len(p) + 1) if toks[i:i + len(p)] == p), None)
        if hit is None:
            missing.append(f"{cue}: “{phrase}”")
        else:
            out[cue] = round(seq[hit][1], 3)
    if missing:
        print("MISSING cue phrases (not spoken in the narration):\n  " + "\n  ".join(missing), file=sys.stderr)
        return 1
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=1))
    print(f"{a.out}: {len(out)} cues resolved")
    return 0


if __name__ == "__main__":
    sys.exit(main())
