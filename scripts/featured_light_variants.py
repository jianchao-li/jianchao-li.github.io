"""Render light-mode variants of the "Blueprint Pixel" featured images.

Every post's and project's featured.jpg is pixel art in the 16-colour palette of
scripts/bogle_series/featured_images.py, drawn at 400x220 and upscaled 5x.
This script reads each featured.jpg back to its 400x220 palette grid, remaps
the palette onto a light "paper blueprint" background, and writes
light-mode.jpg next to it. The site shows light-mode.jpg in light mode and
featured.jpg in dark mode (see layouts/partials/featured-image-pair.html).

The file name must not contain "feature", "cover", "thumbnail" or
"background": the theme picks a post's featured image by those globs.

Pixels drawn straight onto the background (unoutlined text, chart lines,
sparkles) get darker colours so they stay readable on the light paper;
pixels inside outlined shapes keep their original colours.

Requires Pillow:  python3 -m venv /tmp/pxenv && /tmp/pxenv/bin/pip install pillow
Run from the repo root:  /tmp/pxenv/bin/python scripts/featured_light_variants.py [content/posts/<slug>/featured.jpg ...]
"""
import glob
import os
import sys
from collections import deque

from PIL import Image

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "bogle_series"))
from featured_images import P, SCALE  # noqa: E402

NAMES = list(P)
PAL = [P[n] for n in NAMES]

# Colour inside an outlined shape (or anywhere, for the structural colours).
LIGHT = {
    "bg": (244, 246, 250), "grid": (216, 222, 234), "out": (44, 56, 88),
    "dk": (198, 208, 226), "mid": (132, 148, 180), "lt": (92, 108, 144),
    "wh": (255, 255, 255), "pure": (255, 255, 255),
    "gold": (244, 180, 60), "orange": (236, 120, 56),
    "green": (76, 200, 116), "red": (228, 72, 76),
    "cyan": (56, 200, 228), "teal": (28, 140, 156),
    "purple": (140, 124, 244), "dpurple": (88, 72, 164),
}
# Colour when a same-coloured patch touches the background directly.
FLOATING = {
    "wh": (64, 78, 112), "pure": (214, 140, 20),
    "gold": (210, 138, 16), "orange": (212, 94, 34),
    "green": (32, 156, 80), "red": (206, 50, 56),
    "cyan": (16, 146, 180), "teal": (18, 116, 132),
    "purple": (112, 92, 226), "dpurple": (88, 72, 164),
}
BACKGROUND = {NAMES.index("bg"), NAMES.index("grid")}


def nearest(c):
    return min(range(len(PAL)), key=lambda i: sum((a - b) ** 2 for a, b in zip(c, PAL[i])))


def to_grid(path):
    im = Image.open(path).convert("RGB")
    w, h = im.size[0] // SCALE, im.size[1] // SCALE
    px = im.load()
    cache = {}
    grid = []
    for y in range(h):
        row = []
        for x in range(w):
            # average the inner 3x3 of each 5x5 block to shrug off JPEG noise
            cs = [px[x * SCALE + dx, y * SCALE + dy] for dx in (1, 2, 3) for dy in (1, 2, 3)]
            c = tuple(sum(ch) // len(cs) for ch in zip(*cs))
            if c not in cache:
                cache[c] = nearest(c)
            row.append(cache[c])
        grid.append(row)
    return grid


def floating_mask(grid):
    """True for pixels whose same-colour 4-connected patch touches the background."""
    h, w = len(grid), len(grid[0])
    seen = [[False] * w for _ in range(h)]
    out = [[False] * w for _ in range(h)]
    for sy in range(h):
        for sx in range(w):
            if seen[sy][sx] or grid[sy][sx] in BACKGROUND:
                continue
            col = grid[sy][sx]
            comp, touches = [], False
            q = deque([(sx, sy)])
            seen[sy][sx] = True
            while q:
                x, y = q.popleft()
                comp.append((x, y))
                for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= nx < w and 0 <= ny < h:
                        n = grid[ny][nx]
                        if n in BACKGROUND:
                            touches = True
                        elif n == col and not seen[ny][nx]:
                            seen[ny][nx] = True
                            q.append((nx, ny))
            if touches:
                for x, y in comp:
                    out[y][x] = True
    return out


def light_variant(path):
    grid = to_grid(path)
    flo = floating_mask(grid)
    h, w = len(grid), len(grid[0])
    im = Image.new("RGB", (w, h))
    data = []
    for y in range(h):
        for x in range(w):
            name = NAMES[grid[y][x]]
            data.append(FLOATING[name] if flo[y][x] and name in FLOATING else LIGHT[name])
    im.putdata(data)
    return im.resize((w * SCALE, h * SCALE), Image.NEAREST)


if __name__ == "__main__":
    paths = sys.argv[1:] or sorted(glob.glob("content/*/*/featured.jpg"))
    for path in paths:
        dst = os.path.join(os.path.dirname(path), "light-mode.jpg")
        light_variant(path).save(dst, "JPEG", quality=92, subsampling=0)
        print(dst)
