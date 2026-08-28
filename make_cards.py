#!/usr/bin/env python3
"""Render a content JSON into 1080x1080 carousel slides.

Usage:
    python make_cards.py content/2026-08-28.json [out_dir ...]

Writes 01.png ... 10.png into every out_dir given (default: img/<date>).
"""
import json
import os
import re
import sys

from PIL import Image, ImageDraw, ImageFont

SIZE = 1080
MARGIN = 96
HANDLE = "@whatshotkorea"

# Palette lifted from the account's profile artwork.
ORANGE_TOP = (247, 164, 43)
ORANGE_BOTTOM = (232, 86, 29)
CREAM = (255, 247, 236)
NAVY = (22, 36, 61)
SLATE = (74, 90, 115)
WHITE = (255, 255, 255)

FONT_DIR = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts")
HANGUL = re.compile(r"[\u1100-\u11ff\u3130-\u318f\uac00-\ud7a3]")


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def pick(text, size, weight="black"):
    """Malgun Gothic carries the Hangul; Arial carries the display weight."""
    if HANGUL.search(text):
        return font("malgunbd.ttf", size)
    return font({"black": "ariblk.ttf", "bold": "segoeuib.ttf"}.get(weight, "segoeui.ttf"), size)


def wrap(draw, text, fnt, width):
    lines, line = [], ""
    for word in text.split():
        probe = f"{line} {word}".strip()
        if draw.textlength(probe, font=fnt) <= width or not line:
            line = probe
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def block_height(draw, text, size, weight="black", spacing=1.22, width=None):
    width = width or SIZE - 2 * MARGIN
    return len(wrap(draw, text, pick(text, size, weight), width)) * int(size * spacing)


def draw_block(draw, text, y, size, color, weight="black", spacing=1.22, width=None):
    """Draw wrapped text from y downward, return the y just past the last line."""
    width = width or SIZE - 2 * MARGIN
    fnt = pick(text, size, weight)
    step = int(size * spacing)
    for line in wrap(draw, text, fnt, width):
        # Re-pick per line so a Hangul word does not force the whole block to Malgun.
        draw.text((MARGIN, y), line, font=pick(line, size, weight), fill=color)
        y += step
    return y


def gradient():
    img = Image.new("RGB", (SIZE, SIZE))
    d = ImageDraw.Draw(img)
    for y in range(SIZE):
        t = y / (SIZE - 1)
        d.line([(0, y), (SIZE, y)],
               fill=tuple(round(a + (b - a) * t) for a, b in zip(ORANGE_TOP, ORANGE_BOTTOM)))
    return img


def footer(draw, color, index, total):
    small = font("segoeuib.ttf", 30)
    draw.text((MARGIN, SIZE - MARGIN - 10), HANDLE, font=small, fill=color)
    counter = f"{index:02d} / {total:02d}"
    draw.text((SIZE - MARGIN - draw.textlength(counter, font=small), SIZE - MARGIN - 10),
              counter, font=small, fill=color)


def render_hook(slide, index, total):
    img = gradient()
    d = ImageDraw.Draw(img)
    kicker = font("segoeuib.ttf", 30)
    d.text((MARGIN, MARGIN), slide["kicker"], font=kicker, fill=(255, 235, 205))
    d.line([(MARGIN, MARGIN + 54), (MARGIN + 84, MARGIN + 54)], fill=WHITE, width=5)

    fnt = pick(slide["headline"], 82)
    lines = wrap(d, slide["headline"], fnt, SIZE - 2 * MARGIN)
    block = len(lines) * int(82 * 1.14)
    y = (SIZE - block) // 2 - 40
    for line in lines:
        d.text((MARGIN, y), line, font=pick(line, 82), fill=WHITE)
        y += int(82 * 1.14)
    draw_block(d, slide["note"], y + 26, 36, (255, 226, 195), weight="bold")
    footer(d, (255, 226, 195), index, total)
    return img


def render_content(slide, index, total):
    img = Image.new("RGB", (SIZE, SIZE), CREAM)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, SIZE, 14], fill=ORANGE_BOTTOM)

    chip = f"{index:02d}"
    d.rounded_rectangle([MARGIN, MARGIN, MARGIN + 92, MARGIN + 62], radius=18, fill=ORANGE_BOTTOM)
    cf = font("ariblk.ttf", 32)
    d.text((MARGIN + 46 - d.textlength(chip, font=cf) / 2, MARGIN + 12), chip, font=cf, fill=WHITE)

    head_h = block_height(d, slide["headline"], 62, spacing=1.18)
    body_h = block_height(d, slide["body"], 38, "regular", 1.42)
    start = max(MARGIN + 118, (SIZE - (head_h + 98 + body_h)) // 2)

    y = draw_block(d, slide["headline"], start, 62, NAVY, spacing=1.18)
    d.line([(MARGIN, y + 24), (MARGIN + 110, y + 24)], fill=ORANGE_BOTTOM, width=6)
    draw_block(d, slide["body"], y + 74, 38, SLATE, weight="regular", spacing=1.42)
    footer(d, (176, 158, 138), index, total)
    return img


def render_stat(slide, index, total):
    img = Image.new("RGB", (SIZE, SIZE), CREAM)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, SIZE, 14], fill=ORANGE_BOTTOM)

    head_h = block_height(d, slide["headline"], 50, spacing=1.2)
    body_h = block_height(d, slide["body"], 36, "regular", 1.42)
    start = (SIZE - (250 + head_h + 98 + body_h)) // 2

    d.text((MARGIN, start), slide["stat"], font=pick(slide["stat"], 176), fill=ORANGE_BOTTOM)
    y = draw_block(d, slide["headline"], start + 250, 50, NAVY, spacing=1.2)
    d.line([(MARGIN, y + 24), (MARGIN + 110, y + 24)], fill=ORANGE_BOTTOM, width=6)
    draw_block(d, slide["body"], y + 74, 36, SLATE, weight="regular", spacing=1.42)
    footer(d, (176, 158, 138), index, total)
    return img


def render_cta(slide, index, total):
    img = gradient()
    d = ImageDraw.Draw(img)
    y = draw_block(d, slide["headline"], 320, 76, WHITE, spacing=1.16)
    y = draw_block(d, slide["body"], y + 40, 40, (255, 232, 204), weight="bold", spacing=1.35)
    label = f"FOLLOW {HANDLE}"
    hf = font("ariblk.ttf", 38)
    pill_w = d.textlength(label, font=hf) + 92
    d.rounded_rectangle([MARGIN, y + 56, MARGIN + pill_w, y + 148], radius=46, fill=WHITE)
    d.text((MARGIN + 46, y + 80), label, font=hf, fill=ORANGE_BOTTOM)
    draw_block(d, slide["next"], y + 190, 32, (255, 226, 195), weight="bold")
    footer(d, (255, 226, 195), index, total)
    return img


RENDERERS = {"hook": render_hook, "content": render_content,
             "stat": render_stat, "cta": render_cta}


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    with open(argv[1], encoding="utf-8") as fh:
        data = json.load(fh)

    out_dirs = argv[2:] or [os.path.join("img", data["date"])]
    for out in out_dirs:
        os.makedirs(out, exist_ok=True)

    total = len(data["slides"])
    for i, slide in enumerate(data["slides"], start=1):
        img = RENDERERS[slide["type"]](slide, i, total)
        for out in out_dirs:
            img.save(os.path.join(out, f"{i:02d}.png"))
    print(f"{data['date']}: {total} slides -> {', '.join(out_dirs)}")


if __name__ == "__main__":
    main(sys.argv)
