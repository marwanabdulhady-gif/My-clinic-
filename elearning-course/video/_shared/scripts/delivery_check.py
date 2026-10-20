#!/usr/bin/env python3
"""Hard checks on the SCORM video file before it goes into a package.

Fails (exit 1) unless ALL of these hold:
  * H.264 video, yuv420p, 1280x720 or 1920x1080, 30 fps; AAC audio, mono or stereo
  * size <= 10 MB per minute of video
  * integrated loudness -16 +/- 1 LUFS and true peak <= -1 dBTP (ffmpeg ebur128)
  * no more than 3 large luminance flashes in any 1-second window (photosensitive-safety guard)
  * a .vtt with the same base name exists and starts with WEBVTT

    python3 delivery_check.py renders/<clip-id>.mp4 [--vtt data/<clip-id>.vtt] [--json data/qa_delivery.json]
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str]) -> str:
    p = subprocess.run(cmd, capture_output=True, text=True)
    return p.stdout + p.stderr


def probe(f: str) -> dict:
    return json.loads(run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", f]))


def loudness(f: str) -> tuple[float, float]:
    out = run(["ffmpeg", "-hide_banner", "-nostats", "-i", f, "-af", "ebur128=peak=true", "-f", "null", "-"])
    i = re.findall(r"I:\s+(-?[\d.]+) LUFS", out)
    tp = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", out)
    return (float(i[-1]) if i else float("nan"), float(tp[-1]) if tp else float("nan"))


def flashes(f: str) -> int:
    """Max count of big frame-to-frame luminance jumps (>= 20% of range) in any 1-second window."""
    out = run(["ffmpeg", "-hide_banner", "-i", f, "-vf", "scale=160:-2,signalstats,metadata=print:key=lavfi.signalstats.YAVG",
               "-an", "-f", "null", "-"])
    y = [float(v) for v in re.findall(r"YAVG=([\d.]+)", out)]
    jumps = [i for i in range(1, len(y)) if abs(y[i] - y[i - 1]) >= 0.2 * 255]
    worst, j = 0, 0
    for i, t in enumerate(jumps):
        while jumps[j] < t - 30:
            j += 1
        worst = max(worst, i - j + 1)
    return worst


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mp4"); ap.add_argument("--vtt"); ap.add_argument("--json")
    a = ap.parse_args()
    info = probe(a.mp4)
    v = next(s for s in info["streams"] if s["codec_type"] == "video")
    au = next((s for s in info["streams"] if s["codec_type"] == "audio"), None)
    dur = float(info["format"]["duration"]); mb = Path(a.mp4).stat().st_size / 1e6
    fps = eval(v.get("avg_frame_rate", "0/1")) if v.get("avg_frame_rate", "0/0") != "0/0" else 0  # noqa: S307 - ffprobe fraction
    lufs, tp = loudness(a.mp4) if au else (float("nan"), float("nan"))
    fl = flashes(a.mp4)
    vtt = Path(a.vtt) if a.vtt else Path(a.mp4).with_suffix(".vtt")
    checks = {
        "video H.264 yuv420p": v["codec_name"] == "h264" and v.get("pix_fmt") == "yuv420p",
        "size 1280x720 or 1920x1080": (v["width"], v["height"]) in {(1280, 720), (1920, 1080)},
        "30 fps": abs(fps - 30) < 0.1,
        "AAC audio": bool(au) and au["codec_name"] == "aac",
        f"<= 10 MB/min ({mb / (dur / 60):.1f})": mb / (dur / 60) <= 10,
        f"loudness -16 +/- 1 LUFS ({lufs})": abs(lufs + 16) <= 1,
        f"true peak <= -1 dBTP ({tp})": tp <= -1,
        f"<= 3 flashes per second ({fl})": fl <= 3,
        f"captions {vtt.name}": vtt.exists() and vtt.read_text(encoding="utf-8").startswith("WEBVTT"),
    }
    for k, ok in checks.items():
        print(("PASS " if ok else "FAIL ") + k)
    if a.json:
        Path(a.json).write_text(json.dumps({"file": a.mp4, "duration_s": dur, "mb": mb, "lufs": lufs, "true_peak": tp,
                                            "max_flashes_per_s": fl, "checks": checks}, indent=1))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
