#!/usr/bin/env python3
"""Derive the three missing companion avatar crops from the approved Canva pose previews.

companions.md §3 lists `char-noor-avatar-happy`, `char-noor-avatar-concern` and
`char-omar-avatar-happy` as "to make if needed": crop them from the already-approved `-success`
and `-concern` poses rather than generating new likenesses. The neutral avatars are copied from
their approved previews.

These are **interim, low-resolution** crops from the 149×199 preview JPGs: good enough to show
avatar placement on storyboards and visual boards at 48–64 px. They are not the production files.
Production still needs the full-size transparent PNGs downloaded from Canva (programme gap G6),
which this tool cannot reach.

Usage:
    python3 elearning-course/scorm-plans/tools/make_companion_avatars.py
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[3]
CHARS = ROOT / "elearning-course" / "scorm-plans" / "00_program" / "characters"
PREVIEWS = CHARS / "previews"
ASSETS = CHARS / "assets"

# avatar crop = top-centre square of the pose preview (head and shoulders)
CROP_TOP = 0.02
CROP_HEIGHT = 0.44
WHITE_TOLERANCE = 244

DERIVED = {
    "char-noor-avatar-happy": "char-noor-success.jpg",
    "char-noor-avatar-concern": "char-noor-concern.jpg",
    "char-omar-avatar-happy": "char-omar-success.jpg",
}
COPIED = {
    "char-noor-avatar-neutral": "char-noor-avatar-neutral.jpg",
    "char-omar-avatar-neutral": "char-omar-avatar-neutral.jpg",
}


def key_white(image: Image.Image) -> Image.Image:
    """Turn the flat white studio background transparent (preview JPGs have no alpha)."""
    rgba = image.convert("RGBA")
    pixels = rgba.load()
    width, height = rgba.size
    for y in range(height):
        for x in range(width):
            r, g, b, _a = pixels[x, y]
            if r >= WHITE_TOLERANCE and g >= WHITE_TOLERANCE and b >= WHITE_TOLERANCE:
                pixels[x, y] = (r, g, b, 0)
    return rgba


def head_crop(image: Image.Image) -> Image.Image:
    width, height = image.size
    top = int(height * CROP_TOP)
    side = int(height * CROP_HEIGHT)
    left = max(0, (width - side) // 2)
    return image.crop((left, top, left + side, top + side))


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    made = []
    for asset_id, source in {**COPIED, **DERIVED}.items():
        image = Image.open(PREVIEWS / source)
        if asset_id in DERIVED:
            image = head_crop(image)
        out = ASSETS / f"{asset_id}.png"
        key_white(image).save(out, "PNG")
        made.append((asset_id, source, out.stat().st_size, image.size))
    for asset_id, source, size, dims in made:
        kind = "copied" if asset_id.endswith("neutral") else "cropped"
        print(f"{asset_id}.png  {kind} from previews/{source}  {dims[0]}×{dims[1]}  {size} bytes")
    print(f"\nInterim assets in {ASSETS.relative_to(ROOT)}. Production still requires the "
          "full-size Canva PNGs (programme gap G6).")


if __name__ == "__main__":
    main()
