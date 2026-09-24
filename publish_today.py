#!/usr/bin/env python3
"""Publish one day's carousel without arguments, for the scheduler to call.

Usage:
    python publish_today.py [YYYY-MM-DD]

Reads content/<date>.json for the caption, hashtags and first comment, takes
the images from img/<date>/ -- ten slides, or one greeting card -- and hands
the lot to post.py. Defaults to today, which is what the 08:00 task runs.

Every run appends to publish.log, because a scheduled run has nobody watching
it. A run that finds no content file or no slides exits without calling Meta.
"""
import datetime
import glob
import json
import os
import sys

import post

SLIDES = 10


def log(message):
    line = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S} {message}"
    print(line)
    with open("publish.log", "a", encoding="utf-8") as fh:
        fh.write(line + "\n")


def main(argv):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    date = argv[1] if len(argv) > 1 else datetime.date.today().isoformat()

    content = f"content/{date}.json"
    if not os.path.exists(content):
        log(f"{date}: no {content}, nothing to publish")
        return 0

    with open(content, encoding="utf-8") as fh:
        day = json.load(fh)

    # A greeting day is one image; a carousel day is ten. Anything in between is
    # a half-rendered day and must not go up.
    paths = sorted(glob.glob(f"img/{date}/*.png"))
    if len(paths) not in (1, SLIDES):
        log(f"{date}: img/{date} has {len(paths)} images, needs 1 or {SLIDES}")
        return 1

    caption = day["caption"] + "\n\n" + " ".join(day["hashtags"])
    argv = ["post.py"]
    if day.get("reply"):
        argv += ["--reply", day["reply"]]
    argv += [caption] + paths

    log(f"{date}: publishing {day['title']}")
    try:
        posted = post.main(argv)
    except SystemExit as exc:  # post.py exits on unreachable images
        log(f"{date}: post.py stopped -- {exc}")
        return 1
    except Exception as exc:
        log(f"{date}: FAILED -- {exc}")
        return 1
    if not posted:
        log(f"{date}: FAILED -- every platform refused, nothing went up")
        return 1
    log(f"{date}: done")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
