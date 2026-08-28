#!/usr/bin/env python3
"""Write the human-facing brief (caption, hashtags, slide copy) for one content JSON.

Usage:
    python make_brief.py content/2026-08-28.json out_dir
"""
import json
import sys


def main(argv):
    if len(argv) < 3:
        sys.exit(__doc__)
    with open(argv[1], encoding="utf-8") as fh:
        data = json.load(fh)
    ko = data.get("ko", {})

    out = [f"# {data['title']}",
           "",
           f"- 발행 예정: {data['date']} ({data['weekday']})",
           f"- 슬라이드: {len(data['slides'])}장",
           "- 영어판 `slides/`, 한국어판 `slides_ko/`",
           "",
           "## 캡션 — 영어판 (그대로 복사)",
           "",
           "```",
           data["caption"],
           "",
           " ".join(data["hashtags"]),
           "```",
           "",
           "## 캡션 — 한국어판 (그대로 복사)",
           "",
           "```",
           ko.get("caption", "(없음)"),
           "",
           " ".join(ko.get("hashtags", [])),
           "```",
           "",
           "## 확인이 필요한 사실",
           ""]
    out += [f"{i}. {flag}" for i, flag in enumerate(data["fact_check"], start=1)]
    out += ["", "## 슬라이드 문구", ""]

    for i, slide in enumerate(data["slides"], start=1):
        head = slide.get("headline", "")
        if slide["type"] == "stat":
            head = f"{slide['stat']} — {head}"
        out.append(f"**{i:02d}. {head}**")
        for key in ("kicker", "note", "body"):
            if slide.get(key):
                out.append(f"  EN  {slide[key]}")
        for key in ("kicker", "note", "body"):
            if slide.get("ko", {}).get(key):
                out.append(f"  KO  {slide['ko'][key]}")
        out.append("")

    with open(f"{argv[2]}/README.md", "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
    print(f"{argv[2]}/README.md")


if __name__ == "__main__":
    main(sys.argv)
