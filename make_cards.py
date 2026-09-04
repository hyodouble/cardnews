#!/usr/bin/env python3
"""Render a content JSON into 1080x1080 carousel slides.

Usage:
    python make_cards.py content/2026-08-28.json [out_dir ...]
    python make_cards.py content/2026-08-28.json --reel   # img/<date>-reel

Writes 01.png ... 10.png into every out_dir given (default: img/<date>).
The layout rules this implements are written down in DESIGN.md.
"""
import json
import os
import re
import sys

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageFont

SIZE = 1080
MARGIN = 76
HANDLE = "WHAT'S HOT KOREA"

INK = (16, 16, 18)
AMBER = (255, 176, 32)
WHITE = (255, 255, 255)
BONE = (240, 236, 228)

# Bundled open fonts beat the Windows defaults: Anton is a real poster face and
# Pretendard is the current standard for Korean UI type.
FONT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")
HANGUL = re.compile(r"[\u1100-\u11ff\u3130-\u318f\uac00-\ud7a3]")
EMPH = re.compile(r"\*\*(.+?)\*\*")

# Gemini stamps a sparkle into the bottom-right corner; trimming the frame is
# cleaner than trying to paint it out.
WATERMARK_TRIM = 0.12

# A Reel is one video, so the carousel furniture -- the swipe cue and the
# NN of NN counter -- is not just useless there, it tells the viewer to swipe
# away. --reel drops both and leaves the layout alone.
REEL = False


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def display(text, size):
    """Anton for Latin headlines, Pretendard ExtraBold where Hangul appears."""
    return font("Pretendard-ExtraBold.ttf" if HANGUL.search(text) else "Anton-Regular.ttf", size)


def body_font(text, size, weight="regular"):
    return font("Pretendard-Medium.ttf" if weight == "bold" else "Pretendard-Regular.ttf", size)


def caps(text):
    """Latin headlines are set in caps; Hangul has no case so it is left alone."""
    return text if HANGUL.search(text) else text.upper()


def tokens(text):
    """Tokenise once, keeping which words are accented and which follow a space."""
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


def block(draw, text, size, width, fnt_for, spacing):
    """Wrap into lines of (word, emph, space_before) and report the metrics."""
    lines, line, used = [], [], 0.0
    space = draw.textlength(" ", font=fnt_for(" "))
    for word, emph, sp in tokens(text):
        w = draw.textlength(word, font=fnt_for(word))
        gap = space if (sp and line) else 0.0
        if line and used + gap + w > width:
            lines.append(line)
            line, used = [(word, emph, False)], w
        else:
            line.append((word, emph, bool(gap)))
            used += gap + w
    if line:
        lines.append(line)
    return lines, int(size * spacing), space, fnt_for


def head_block(draw, text, size, width=None, spacing=0.94):
    width = width or SIZE - 2 * MARGIN
    if HANGUL.search(text):
        size, spacing = int(size * 0.72), 1.16
    else:
        spacing = 1.02  # Anton runs tall; 0.94 would collide
    return block(draw, caps(text), size, width, lambda w: display(w, size), spacing)


def body_block(draw, text, size, width=None, spacing=1.58, weight="regular"):
    width = width or SIZE - 2 * MARGIN
    return block(draw, text, size, width, lambda w: body_font(w, size, weight), spacing)


def paint(draw, packed, y, color, accent, x=MARGIN):
    lines, step, space, fnt_for = packed
    for line in lines:
        cx = x
        for word, emph, sp in line:
            if sp:
                cx += space
            fnt = fnt_for(word)
            draw.text((cx, y), word, font=fnt, fill=accent if emph else color)
            cx += draw.textlength(word, font=fnt)
        y += step
    return y


def height(packed):
    return len(packed[0]) * packed[1]


def grain(img, amount=9):
    """A little noise keeps flat fills from banding and reads as print."""
    noise = Image.effect_noise((SIZE, SIZE), amount).convert("L")
    return ImageChops.add(img, Image.merge("RGB", (noise, noise, noise)), scale=1, offset=-128)


def photo(path, darken=0.55, blur=0):
    img = Image.open(path).convert("RGB")
    # Only Gemini output carries the sparkle, and it always comes back 1024x1024.
    # A real photograph dropped in here has no watermark, so trimming it would
    # just eat a tenth of the frame.
    if img.size == (1024, 1024):
        img = img.crop((0, 0, int(img.width * (1 - WATERMARK_TRIM)),
                        int(img.height * (1 - WATERMARK_TRIM))))
    side = min(img.size)
    img = img.crop(((img.width - side) // 2, (img.height - side) // 2,
                    (img.width + side) // 2, (img.height + side) // 2))
    img = img.resize((SIZE, SIZE), Image.LANCZOS)
    if blur:
        img = img.filter(ImageFilter.GaussianBlur(blur))
    return grain(ImageEnhance.Brightness(img).enhance(darken))


def scrim(img, height_px=760, strength=250):
    """Darken upward from the bottom so a bottom-anchored headline stays readable."""
    ramp = Image.new("L", (1, SIZE))
    for y in range(SIZE):
        t = max(0.0, (y - (SIZE - height_px)) / height_px)
        ramp.putpixel((0, y), int(strength * t ** 1.5))
    return Image.composite(Image.new("RGB", (SIZE, SIZE), INK), img, ramp.resize((SIZE, SIZE)))


def chrome(img, index, total, on_dark=True):
    """Tiny centred wordmark up top, counter in the corner. Nothing else."""
    d = ImageDraw.Draw(img, "RGBA")
    tint = (255, 255, 255, 130) if on_dark else (16, 16, 18, 150)
    wm = font("seguisb.ttf", 22)
    d.text(((SIZE - d.textlength(HANDLE, font=wm)) / 2, MARGIN - 14), HANDLE, font=wm, fill=tint)

    if not REEL:
        counter = f"{index:02d} — {total:02d}"
        d.text((SIZE - MARGIN - d.textlength(counter, font=wm), SIZE - MARGIN - 8),
               counter, font=wm, fill=tint)
    return d


def render_hook(s, index, total, assets):
    img = scrim(photo(assets["hook"], 0.62), height_px=840)
    d = chrome(img, index, total)

    head = head_block(d, s["headline"], 92)
    note = body_block(d, s["note"], 30, weight="bold")

    y = SIZE - MARGIN - 104 - height(note) - height(head)
    d.text((MARGIN, y - 52), caps(s["kicker"]), font=body_font(s["kicker"], 24, "bold"),
           fill=AMBER)
    y = paint(d, head, y, WHITE, AMBER)
    paint(d, note, y + 28, BONE, AMBER)

    if not REEL:
        cue = "밀어서 보기 →" if HANGUL.search(s["note"]) else "SWIPE →"
        d.text((MARGIN, SIZE - MARGIN - 8), cue, font=body_font(cue, 22, "bold"),
               fill=(255, 255, 255, 130))
    return img


def render_content(s, index, total, assets):
    """Same photo + scrim treatment as hook/stat/cta -- see DESIGN.md 4th revision.

    A flat-color slide reads as a different document from its photo neighbours,
    so every slide shares one visual treatment and gets its rhythm from a
    different photo instead of a different background type.
    """
    key = s.get("asset", f"content{index}")
    img = scrim(photo(assets.get(key, assets["hook"])), height_px=760)
    d = chrome(img, index, total)

    head = head_block(d, s["headline"], 76)
    text = body_block(d, s["body"], 33)

    # Anchored to the bottom margin, the way the reference sets do it.
    y = SIZE - MARGIN - 84 - height(text) - 62 - height(head)
    y = paint(d, head, y, WHITE, AMBER)
    paint(d, text, y + 62, BONE, AMBER)
    return img


def render_stat(s, index, total, assets):
    img = scrim(photo(assets.get("stat", assets["hook"]), 0.4, blur=4), height_px=SIZE)
    d = chrome(img, index, total)

    head = head_block(d, s["headline"], 54)
    text = body_block(d, s["body"], 31)

    y = (SIZE - (250 + height(head) + 54 + height(text))) // 2
    d.text((MARGIN, y), s["stat"], font=display(s["stat"], 220), fill=AMBER)
    y = paint(d, head, y + 250, WHITE, AMBER)
    paint(d, text, y + 54, BONE, AMBER)
    return img


def render_cta(s, index, total, assets):
    img = scrim(photo(assets.get("cta", assets["hook"]), 0.4, blur=3), height_px=SIZE)
    d = chrome(img, index, total)

    head = head_block(d, s["headline"], 84)
    text = body_block(d, s["body"], 31, weight="bold")

    y = (SIZE - (height(head) + 46 + height(text) + 150)) // 2
    y = paint(d, head, y, WHITE, AMBER)
    y = paint(d, text, y + 46, BONE, AMBER)

    label = caps(s.get("button", "FOLLOW @whatshotkorea"))
    bf = display(label, 40)
    pill = d.textlength(label, font=bf) + 88
    d.rounded_rectangle([MARGIN, y + 44, MARGIN + pill, y + 134], radius=45, fill=AMBER)
    d.text((MARGIN + 44, y + 66), label, font=bf, fill=INK)
    return img


RENDERERS = {"hook": render_hook, "content": render_content,
             "stat": render_stat, "cta": render_cta}


def main(argv):
    global REEL
    REEL = "--reel" in argv
    args = [a for a in argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit(__doc__)

    with open(args[0], encoding="utf-8") as fh:
        data = json.load(fh)

    asset_dir = os.path.join("assets", data["date"])
    assets = {os.path.splitext(f)[0]: os.path.join(asset_dir, f)
              for f in os.listdir(asset_dir)} if os.path.isdir(asset_dir) else {}
    if "hook" not in assets:
        sys.exit(f"need at least {asset_dir}/hook.png")

    out_dirs = args[1:] or [os.path.join(
        "img", data["date"] + ("-reel" if REEL else ""))]
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
