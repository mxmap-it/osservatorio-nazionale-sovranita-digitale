"""Generate PNG brand assets for the Osservatorio (Concept B — radar).
Pillow only (no SVG rasterizer available). Supersampled for smooth arcs.
Outputs into static/brand/."""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(__file__), "..", "static", "brand")
os.makedirs(OUT, exist_ok=True)

BLUE = (0, 102, 204)
INK = (23, 50, 77)
GREEN = (0, 135, 88)
GRAY = (154, 166, 178)
RED = (206, 43, 55)
WHITE = (255, 255, 255)
SS = 4  # supersample factor

ARIAL = r"C:\Windows\Fonts\arial.ttf"
ARIALBD = r"C:\Windows\Fonts\arialbd.ttf"


def mix(fg, bg, t):
    return tuple(round(fg[i] * t + bg[i] * (1 - t)) for i in range(3))


def radar(draw, cx, cy, R, base, bg, ticks=True, n_arcs=3):
    """Draw a radar mark: dot + top semicircle arcs + tricolor ticks.
    base = arc/dot color, bg = solid background (for opacity emulation)."""
    w = max(2, round(0.12 * R))
    alphas = [1.0, 0.6, 0.3][:n_arcs]
    radii = [0.45 * R, 0.72 * R, 1.0 * R][:n_arcs]
    for rad, a in zip(radii, alphas):
        col = mix(base, bg, a)
        draw.arc([cx - rad, cy - rad, cx + rad, cy + rad], 180, 360, fill=col, width=w)
    dr = 0.17 * R
    draw.ellipse([cx - dr, cy - dr, cx + dr, cy + dr], fill=base)
    if ticks:
        tw = 0.27 * R
        th = max(2, round(0.09 * R))
        ty = cy + 0.42 * R
        cols = [GREEN, GRAY, RED] if base != WHITE else [(70, 208, 138), WHITE, (255, 107, 116)]
        gap = tw * 0.12
        x0 = cx - (3 * tw + 2 * gap) / 2
        for i, c in enumerate(cols):
            x = x0 + i * (tw + gap)
            draw.rectangle([x, ty, x + tw, ty + th], fill=c)


def icon(size, fname, n_arcs=2, ticks=False, radius_ratio=0.19):
    s = size * SS
    img = Image.new("RGB", (s, s), BLUE)
    d = ImageDraw.Draw(img)
    # rounded mask
    mask = Image.new("L", (s, s), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, s, s], radius=round(s * radius_ratio), fill=255)
    radar(d, s / 2, s * 0.56, s * 0.34, WHITE, BLUE, ticks=ticks, n_arcs=n_arcs)
    out = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    out.paste(img, (0, 0), mask)
    out = out.resize((size, size), Image.LANCZOS)
    out.save(os.path.join(OUT, fname))
    print("wrote", fname, size)


def og_image():
    W, H = 1200 * 1, 630 * 1
    s = 2  # supersample for og
    img = Image.new("RGB", (W * s, H * s), WHITE)
    d = ImageDraw.Draw(img)
    # symbol left-center
    radar(d, 250 * s, 300 * s, 150 * s, BLUE, WHITE, ticks=True, n_arcs=3)
    fb = ImageFont.truetype(ARIALBD, 64 * s)
    fb2 = ImageFont.truetype(ARIALBD, 64 * s)
    fsub = ImageFont.truetype(ARIAL, 26 * s)
    d.text((430 * s, 232 * s), "Osservatorio Nazionale", font=fb, fill=INK)
    d.text((430 * s, 310 * s), "Sovranità Digitale", font=fb2, fill=BLUE)
    d.text((432 * s, 402 * s), "MONITORAGGIO CIVICO · PA ITALIANA",
           font=fsub, fill=(90, 103, 114))
    d.rectangle([0, (H - 12) * s, W * s, H * s], fill=BLUE)
    # tricolor accent on bottom bar
    seg = W * s / 3
    d.rectangle([0, (H - 12) * s, seg, H * s], fill=GREEN)
    d.rectangle([2 * seg, (H - 12) * s, W * s, H * s], fill=RED)
    img = img.resize((W, H), Image.LANCZOS)
    img.save(os.path.join(OUT, "og-image.png"))
    print("wrote og-image.png", W, H)


def avatar():
    size = 400
    s = size * SS
    img = Image.new("RGB", (s, s), BLUE)
    d = ImageDraw.Draw(img)
    mask = Image.new("L", (s, s), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, s, s], radius=round(s * 0.22), fill=255)
    radar(d, s / 2, s * 0.54, s * 0.36, WHITE, BLUE, ticks=True, n_arcs=3)
    out = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    out.paste(img, (0, 0), mask)
    out.resize((size, size), Image.LANCZOS).save(os.path.join(OUT, "social-avatar.png"))
    print("wrote social-avatar.png", size)


if __name__ == "__main__":
    icon(16, "favicon-16.png", n_arcs=2)
    icon(32, "favicon-32.png", n_arcs=2)
    icon(180, "apple-touch-icon.png", n_arcs=2)
    icon(512, "icon-512.png", n_arcs=3, ticks=True)
    avatar()
    og_image()
    print("done")
