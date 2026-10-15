#!/usr/bin/env python3
"""Import the full-size companion artwork (programme gap G6, roadmap item C7).

The course owner delivered the 18 full-size Canva exports of Noor and Dr. Omar on
2026-10-15 (1088 × 1456 px poses, 1264 × 1264 px avatar headshots, white studio
background, JPEG). Each file was matched pixel-wise against the approved previews in
`characters/previews/` before being renamed to its asset id, so the mapping is verified,
not assumed. One upload (Dr. Omar `-listening`) arrived twice; the duplicate is dropped.

This tool turns those originals into the production files companions.md §3 expects:

1. `characters/assets/originals/<asset id>.jpg` → `characters/assets/<asset id>.png`
   with the flat white studio background keyed to transparency. Only white connected to
   the image border is removed, so interior whites (lab coats, shirts, ID badges) survive
   — a plain white-threshold key would eat the coats.
2. Expression avatars from the full-size poses (replaces the interim preview crops):
   `char-<id>-avatar-happy`   = head-and-shoulders crop of `-success`
   `char-<id>-avatar-concern` = head-and-shoulders crop of `-concern`
   The `-avatar-neutral` headshots are imported like any other pose (rule 1).

Provenance: ai-generated (Canva AI, 14 Oct 2026; media ids in companions.md §3),
delivered and approved for import 2026-10-15. Regenerate the PNGs from the originals
with this tool at any time; it is deterministic.

Usage:
    python3 elearning-course/scorm-plans/tools/import_companion_art.py
"""
from __future__ import annotations

from collections import deque
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[3]
CHARS = ROOT / "elearning-course" / "scorm-plans" / "00_program" / "characters"
ORIGINALS = CHARS / "assets" / "originals"
ASSETS = CHARS / "assets"

WHO = ("noor", "omar")
POSES = ("master", "welcome", "explaining", "tip", "thinking", "concern", "success",
         "listening", "avatar-neutral")

# head-and-shoulders crop for expression avatars, as a fraction of the pose image
# (same geometry as the interim tool used on previews; verified on the full-size art)
CROP_TOP = 0.02
CROP_HEIGHT = 0.44

# background keying: near-white and neutral, and connected to the image border
BG_MIN = 235          # every channel at or above this
BG_SPREAD = 12        # max-min between channels at or below this

# edge tidy: drop light anti-alias fringes and stray speckles left next to the keyed
# background (looser than BG_*, but only for pixels that are mostly surrounded by
# transparency, so the figure itself is never eaten)
TIDY_MIN = 228
TIDY_SPREAD = 16
TIDY_TRANSPARENT_NEIGHBOURS = 4
TIDY_PASSES = 2


def key_border_white(image: Image.Image) -> Image.Image:
    """Make the border-connected white studio background transparent."""
    rgba = image.convert("RGBA")
    width, height = rgba.size
    pixels = rgba.load()
    is_bg = bytearray(width * height)
    seen = bytearray(width * height)
    queue: deque[tuple[int, int]] = deque()

    def background_like(x: int, y: int) -> bool:
        r, g, b, _a = pixels[x, y]
        return min(r, g, b) >= BG_MIN and max(r, g, b) - min(r, g, b) <= BG_SPREAD

    for x in range(width):
        for y in (0, height - 1):
            if background_like(x, y) and not seen[y * width + x]:
                seen[y * width + x] = 1
                queue.append((x, y))
    for y in range(height):
        for x in (0, width - 1):
            if background_like(x, y) and not seen[y * width + x]:
                seen[y * width + x] = 1
                queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        is_bg[y * width + x] = 1
        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= nx < width and 0 <= ny < height and not seen[ny * width + nx]:
                seen[ny * width + nx] = 1
                if background_like(nx, ny):
                    queue.append((nx, ny))

    for y in range(height):
        row = y * width
        for x in range(width):
            if is_bg[row + x]:
                r, g, b, _a = pixels[x, y]
                pixels[x, y] = (r, g, b, 0)
    return tidy_edges(rgba)


def tidy_edges(rgba: Image.Image) -> Image.Image:
    """Clear light fringe pixels that are mostly surrounded by keyed transparency."""
    width, height = rgba.size
    pixels = rgba.load()
    for _pass in range(TIDY_PASSES):
        drop = []
        for y in range(height):
            for x in range(width):
                r, g, b, a = pixels[x, y]
                if a == 0 or min(r, g, b) < TIDY_MIN or max(r, g, b) - min(r, g, b) > TIDY_SPREAD:
                    continue
                clear = 0
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1),
                               (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x + 1, y + 1)):
                    if 0 <= nx < width and 0 <= ny < height and pixels[nx, ny][3] == 0:
                        clear += 1
                if clear >= TIDY_TRANSPARENT_NEIGHBOURS:
                    drop.append((x, y))
        if not drop:
            break
        for x, y in drop:
            r, g, b, _a = pixels[x, y]
            pixels[x, y] = (r, g, b, 0)
    return rgba


def head_crop(image: Image.Image) -> Image.Image:
    """Square head-and-shoulders crop, centred horizontally on the frame."""
    width, height = image.size
    top = int(height * CROP_TOP)
    side = int(height * CROP_HEIGHT)
    left = max(0, (width - side) // 2)
    return image.crop((left, top, left + side, top + side))


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    missing = [f"char-{who}-{pose}.jpg" for who in WHO for pose in POSES
               if not (ORIGINALS / f"char-{who}-{pose}.jpg").exists()]
    if missing:
        raise SystemExit(f"missing originals in {ORIGINALS.relative_to(ROOT)}: {', '.join(missing)}")

    made = []
    for who in WHO:
        for pose in POSES:
            asset_id = f"char-{who}-{pose}"
            source = ORIGINALS / f"{asset_id}.jpg"
            out = ASSETS / f"{asset_id}.png"
            image = Image.open(source)
            keyed = key_border_white(image)
            keyed.save(out, "PNG")
            transparent = keyed.getchannel("A").tobytes().count(0)
            share = transparent / (keyed.size[0] * keyed.size[1])
            made.append((asset_id, keyed.size, out.stat().st_size, share))

        for pose, source_pose in (("avatar-happy", "success"), ("avatar-concern", "concern")):
            asset_id = f"char-{who}-{pose}"
            out = ASSETS / f"{asset_id}.png"
            crop = head_crop(Image.open(ASSETS / f"char-{who}-{source_pose}.png"))
            crop.save(out, "PNG")
            made.append((asset_id, crop.size, out.stat().st_size, None))

    for asset_id, size, nbytes, share in made:
        extra = f"  bg keyed {share:5.1%}" if share is not None else "  (avatar crop)"
        print(f"{asset_id}.png  {size[0]}×{size[1]}  {nbytes:,} bytes{extra}")
    print(f"\n{len(made)} production PNGs in {ASSETS.relative_to(ROOT)}.")


if __name__ == "__main__":
    main()
