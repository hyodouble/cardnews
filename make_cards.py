#!/usr/bin/env python3
"""Render a content JSON into 1080x1080 carousel slides.

Usage:
    python make_cards.py content/2026-08-28.json [out_dir ...]

Writes 01.png ... 10.png into every out_dir given (default: img/<date>).
The layout rules this implements are written down in DESIGN.md.
"""
import json
import os
import re
import sys

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

SIZE = 1080
MARGIN = 88
HANDLE = "WHAT'S HOT KOREA"

# Dark editorial base; the amber is the only accent and is rationed per slide.
INK = (18, 18, 20)
INK_SOFT = (28, 28, 32)
AMBER = (245, 166, 35)
WHITE = (255, 255, 255)
MUTED = (255, 255, 255, 150)
FAINT = (255, 255, 255, 70)

FONT_DIR = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts")
HANGUL = re.compile(r"[\u1100-\u11ff\u3130-\u318f\uac00-\ud7a3]")
# **bold** marks the one phrase per line that carries the accent.
EMPH = re.compile(r"\*\*(.+?)\*\*")


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def pick(text, size, weight="black"):
    """Malgun Gothic carries the Hangul; Arial carries the display weight."""
    if HANGUL.search(text):
        return font("malgunbd.ttf" if weight != "regular" else "malgun.ttf", size)
    return font({"black": "ariblk.ttf", "bold": "segoeuib.ttf"}.get(weight, "segoeui.ttf"), size)


def tokens(text):
    """Tokenise once, keeping which words are accented and which follow a space.

    Splitting on whitespace alone would detach punctuation from the word it
    belongs to, so ``**a crisis**, next`` rendered as ``a crisis , next``.
    """
    plain, spans, cursor = [], [], 0
    for m in EMPH.finditer(text):
        plain.append(text[cursor:m.start()])
        start = sum(len(p) for p in plain)
        plain.append(m.group(1))
        spans.append((start, start + len(m.group(1))))
        cursor = m.end()
    plain.append(text[cursor:])
    flat = "".join(plain)

    out = []
    for m in re.finditer(r"\S+", flat):
        emph = any(a <= m.start() < b for a, b in spans)
        out.append((m.group(), emph, m.start() > 0 and flat[m.start() - 1].isspace()))
    return out


def wrap_rich(draw, text, size, weight, width):
    """Wrap into lines of (word, emph, space_before) tuples."""
    lines, line, used = [], [], 0.0
    space = draw.textlength(" ", font=pick(" ", size, weight))
    for word, emph, sp in tokens(text):
        w = draw.textlength(word, font=pick(word, size, weight))
        gap = space if (sp and line) else 0.0
        if line and used + gap + w > width:
            lines.append(line)
            line, used = [(word, emph, False)], w
        else:
            line.append((word, emph, bool(gap)))
            used += gap + w
    if line:
        lines.append(line)
    return lines


def draw_rich(draw, text, y, size, color, accent=AMBER, weight="black",
              spacing=1.1, width=None, underline=False):
    """Draw wrapped text, painting the **marked** phrase in the accent colour."""
    width = width or SIZE - 2 * MARGIN
    step = int(size * spacing)
    space = draw.textlength(" ", font=pick(" ", size, weight))
    for line in wrap_rich(draw, text, size, weight, width):
        x = MARGIN
        for word, emph, sp in line:
            if sp:
                x += space
            fnt = pick(word, size, weight)
            draw.text((x, y), word, font=fnt, fill=accent if emph else color)
            w = draw.textlength(word, font=fnt)
            if emph and underline:
                base = y + size * 1.16
                draw.line([(x, base), (x + w, base)], fill=accent, width=5)
            x += w
        y += step
    return y


def rich_height(draw, text, size, weight="black", spacing=1.1, width=None):
    width = width or SIZE - 2 * MARGIN
    return len(wrap_rich(draw, text, size, weight, width)) * int(size * spacing)


def photo(path, darken=0.42, blur=0):
    """Fill the square with the asset, dimmed enough that white type stays readable."""
    img = Image.open(path).convert("RGB")
    side = min(img.size)
    img = img.crop(((img.width - side) // 2, (img.height - side) // 2,
                    (img.width + side) // 2, (img.height + side) // 2))
    img = img.resize((SIZE, SIZE), Image.LANCZOS)
    if blur:
        img = img.filter(ImageFilter.GaussianBlur(blur))
    return ImageEnhance.Brightness(img).enhance(darken)


def top_shade(img, height=620, strength=236):
    """Darken the top so the headline never fights the photo underneath it."""
    shade = Image.new("L", (1, SIZE), 0)
    for y in range(SIZE):
        shade.putpixel((0, y), int(strength * max(0.0, 1 - y / height)))
    mask = shade.resize((SIZE, SIZE))
    return Image.composite(Image.new("RGB", (SIZE, SIZE), INK), img, mask)


def frame(img, index, total):
    """The fixed furniture every slide shares: brand top-left, counter top-right."""
    d = ImageDraw.Draw(img, "RGBA")
    small = font("segoeuib.ttf", 26)
    d.ellipse([MARGIN, MARGIN + 6, MARGIN + 13, MARGIN + 19], fill=AMBER)
    d.text((MARGIN + 26, MARGIN), HANDLE, font=small, fill=MUTED)

    cur, rest = f"{index:02d}", f"/ {total:02d}"
    cf = font("ariblk.ttf", 28)
    rw = d.textlength(rest, font=small)
    cw = d.textlength(cur, font=cf)
    d.text((SIZE - MARGIN - rw, MARGIN + 1), rest, font=small, fill=FAINT)
    d.text((SIZE - MARGIN - rw - cw - 4, MARGIN - 2), cur, font=cf, fill=WHITE)
    return d


def render_hook(slide, index, total, assets):
    img = top_shade(photo(assets["hook"], 0.46), height=880, strength=246)
    d = frame(img, index, total)

    d.text((MARGIN, 232), slide["kicker"], font=font("segoeuib.ttf", 28), fill=AMBER)
    y = draw_rich(d, slide["headline"], 286, 72, WHITE, spacing=1.26, underline=True)
    draw_rich(d, slide["note"], y + 24, 32, MUTED, weight="bold", spacing=1.35)

    cue = "밀어서 보기  →" if HANGUL.search(slide["note"]) else "SWIPE  →"
    cf = font("segoeuib.ttf", 28)
    d.text((SIZE - MARGIN - d.textlength(cue, font=cf), SIZE - MARGIN - 20), cue,
           font=cf, fill=MUTED)
    return img


def render_content(slide, index, total, assets):
    img = Image.new("RGB", (SIZE, SIZE), INK)

    # A ghosted index numeral gives an all-text slide something to look at.
    layer = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    gd = ImageDraw.Draw(layer)
    ghost = font("ariblk.ttf", 460)
    gd.text((SIZE - MARGIN - gd.textlength(f"{index:02d}", font=ghost) + 90, 560),
            f"{index:02d}", font=ghost, fill=(255, 255, 255, 20))
    img = Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB")

    d = ImageDraw.Draw(img, "RGBA")
    d.rectangle([0, 0, SIZE, 6], fill=AMBER)

    head_h = rich_height(d, slide["headline"], 56, spacing=1.14)
    body_h = rich_height(d, slide["body"], 34, "regular", 1.62)
    y = max(300, (SIZE - (head_h + 96 + body_h)) // 2)

    y = draw_rich(d, slide["headline"], y, 56, WHITE, spacing=1.14)
    d.line([(MARGIN, y + 30), (MARGIN + 92, y + 30)], fill=AMBER, width=5)
    draw_rich(d, slide["body"], y + 76, 34, MUTED, weight="regular", spacing=1.62)

    frame(img, index, total)
    return img


def render_stat(slide, index, total, assets):
    img = top_shade(photo(assets.get("stat", assets["hook"]), 0.3, blur=3), height=SIZE)
    d = frame(img, index, total)

    stat_font = pick(slide["stat"], 168)
    body_h = rich_height(d, slide["body"], 32, "regular", 1.6)
    head_h = rich_height(d, slide["headline"], 46, spacing=1.16)
    y = (SIZE - (230 + head_h + 92 + body_h)) // 2

    d.text((MARGIN, y), slide["stat"], font=stat_font, fill=AMBER)
    y = draw_rich(d, slide["headline"], y + 230, 46, WHITE, spacing=1.16)
    d.line([(MARGIN, y + 28), (MARGIN + 92, y + 28)], fill=AMBER, width=5)
    draw_rich(d, slide["body"], y + 72, 32, MUTED, weight="regular", spacing=1.6)
    return img


def render_cta(slide, index, total, assets):
    img = top_shade(photo(assets.get("cta", assets["hook"]), 0.32, blur=2), height=SIZE)
    d = frame(img, index, total)

    y = draw_rich(d, slide["headline"], 300, 66, WHITE, spacing=1.14)
    y = draw_rich(d, slide["body"], y + 34, 34, MUTED, weight="bold", spacing=1.45)

    label = slide.get("button", "FOLLOW @whatshotkorea")
    bf = pick(label, 34, "black")
    pill_w = d.textlength(label, font=bf) + 84
    d.rounded_rectangle([MARGIN, y + 54, MARGIN + pill_w, y + 138], radius=42, fill=AMBER)
    d.text((MARGIN + 42, y + 76), label, font=bf, fill=INK_SOFT)
    return img


RENDERERS = {"hook": render_hook, "content": render_content,
             "stat": render_stat, "cta": render_cta}


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    with open(argv[1], encoding="utf-8") as fh:
        data = json.load(fh)

    asset_dir = os.path.join("assets", data["date"])
    assets = {os.path.splitext(f)[0]: os.path.join(asset_dir, f)
              for f in os.listdir(asset_dir)} if os.path.isdir(asset_dir) else {}
    if "hook" not in assets:
        sys.exit(f"need at least {asset_dir}/hook.png")

    out_dirs = argv[2:] or [os.path.join("img", data["date"])]
    for out in out_dirs:
        os.makedirs(out, exist_ok=True)

    total = len(data["slides"])
    for i, slide in enumerate(data["slides"], start=1):
        img = RENDERERS[slide["type"]](slide, i, total, assets)
        for out in out_dirs:
            img.save(os.path.join(out, f"{i:02d}.png"))
    print(f"{data['date']}: {total} slides -> {', '.join(out_dirs)}")


if __name__ == "__main__":
    main(sys.argv)
