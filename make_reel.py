#!/usr/bin/env python3
"""Turn a rendered card set into a 9:16 Reel.

Usage:
    python make_reel.py img/2026-09-05 [seconds_per_card]

Writes reel.mp4 next to the cards. The square card is centred on a blurred,
darkened copy of itself, which fills the vertical frame without bars and
without re-laying out the type.
"""
import os
import subprocess
import sys

from PIL import Image, ImageEnhance, ImageFilter

W, H = 1080, 1920
HOLD = 3.0  # seconds per card; under 2.5 nobody finishes reading the body line


def vertical(card):
    """Sharp square card over a blurred fill cropped from the same picture."""
    bg = card.resize((H, H), Image.LANCZOS)
    bg = bg.crop(((H - W) // 2, 0, (H + W) // 2, H))
    bg = ImageEnhance.Brightness(bg.filter(ImageFilter.GaussianBlur(48))).enhance(0.45)
    bg.paste(card, (0, (H - W) // 2))
    return bg


def main(argv):
    src = argv[1]
    hold = float(argv[2]) if len(argv) > 2 else HOLD
    cards = sorted(f for f in os.listdir(src) if f[:2].isdigit() and f.endswith(".png"))
    if not cards:
        sys.exit("no NN.png cards in " + src)

    frames = os.path.join(src, "reel_frames")
    os.makedirs(frames, exist_ok=True)
    for name in cards:
        vertical(Image.open(os.path.join(src, name)).convert("RGB")).save(
            os.path.join(frames, name))

    listing = os.path.join(frames, "concat.txt")
    with open(listing, "w", encoding="utf-8") as fh:
        for name in cards:
            fh.write("file '%s'\nduration %s\n" % (name, hold))
        fh.write("file '%s'\n" % cards[-1])  # concat drops the last duration

    out = os.path.join(src, "reel.mp4")
    # Instagram wants an audio track even on a silent Reel, so a null source
    # goes in alongside the frames.
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error",
        "-f", "concat", "-safe", "0", "-i", listing,
        "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
        "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-preset", "medium",
        "-crf", "20", "-c:a", "aac", "-b:a", "128k", "-shortest",
        "-movflags", "+faststart", out,
    ], check=True)
    print("%s: %d cards x %.1fs -> %s" % (os.path.basename(src), len(cards), hold, out))


if __name__ == "__main__":
    main(sys.argv)
