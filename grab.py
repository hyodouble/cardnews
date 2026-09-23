"""Move the newest Gemini download into assets/<date>/<name>.png, resized to 1024.

    python grab.py 2026-09-22 hook

Refuses a file older than 3 minutes -- that is the previous edition's leftover,
not the cut just generated.
"""
import sys, time, pathlib
from PIL import Image

date, name = sys.argv[1], sys.argv[2]
downloads = pathlib.Path.home() / "Downloads"
newest = max(downloads.glob("Gemini_Generated_Image_*.png"), key=lambda p: p.stat().st_mtime)
age = time.time() - newest.stat().st_mtime
if age > 180:
    sys.exit(f"stale: {newest.name} is {age/60:.1f} min old -- download did not land")

out = pathlib.Path(__file__).parent / "assets" / date / f"{name}.png"
out.parent.mkdir(parents=True, exist_ok=True)
img = Image.open(newest).convert("RGB")
# Without Gemini Pro the download is 1408x768, not square: center-crop, which also cuts off the corner mark.
w, h = img.size
s = min(w, h)
img = img.crop(((w - s) // 2, (h - s) // 2, (w + s) // 2, (h + s) // 2))
img.resize((1024, 1024), Image.LANCZOS).save(out)
newest.unlink()
print(f"{newest.name} -> {out} ({age:.0f}s old)")
