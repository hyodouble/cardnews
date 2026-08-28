# cardnews

Card-news carousels for **What's Hot Korea** — Korean news, trends and culture
explained in English.

This repository does two jobs:

1. **Image host.** GitHub Pages serves `img/` as public URLs. The Meta APIs
   accept image URLs only; they cannot take a file upload, so every slide has
   to be reachable on the open web before it can be published.
2. **Publisher.** `post.py` pushes one carousel to Instagram, the Facebook
   page and Threads in a single run.

## Accounts

| Platform | Handle | ID |
|---|---|---|
| Instagram | `whatshotkorea` (business) | see `.env` |
| Facebook page | What's Hot Korea | `1253255244544447` |
| Threads | `@whatshotkorea` | see `.env` |

The Instagram account is linked to the Facebook page, which is what makes the
Instagram Content Publishing API available. All three post to profiles we own,
so the Meta app stays in development mode and needs no App Review.

## Publishing a carousel

```bash
cp .env.example .env      # fill in the IDs and tokens once
git add img/ && git commit -m "add slides" && git push
python post.py "caption text" img/2026-08-28-1.png img/2026-08-28-2.png
```

Push first. `post.py` refuses to run if a slide is not yet reachable at its
public URL — that check exists because Meta's error for an unreachable image
is unhelpful.

Long-lived Meta tokens expire after 60 days; refresh them and update `.env`.

## Making a carousel

One JSON per post lives in `content/<date>.json`: ten slides, the caption, the
hashtags, and a `fact_check` list of claims that still need verifying. Slide
copy follows the rules in `claude-project-instructions.md`, kept here so the
prompt is versioned alongside the output rather than living only in the Claude
web UI.

```bash
python make_cards.py content/2026-08-28.json img/2026-08-28 "<desktop>/2026-08-28_금요일/slides"
python make_cards.py content/2026-08-28.json --ko img/2026-08-28-ko "<desktop>/2026-08-28_금요일/slides_ko"
python make_brief.py content/2026-08-28.json "<desktop>/2026-08-28_금요일"
```

Every post ships in both languages. Korean copy lives in a `ko` block on each
slide and falls back to the English field when absent, so a partial translation
still renders.

`make_cards.py` renders 1080x1080 PNGs in the account palette — four slide
types (`hook`, `content`, `stat`, `cta`) picked per slide by its `type` field.
It accepts several output directories so the repo copy and the desktop working
copy are written in one pass. `make_brief.py` writes the human-facing README
for a day folder: caption to copy, hashtags, fact-check flags, slide text.

Korean text renders through Malgun Gothic and English through Arial Black,
chosen per line, so a Hangul word inside an English headline does not drag the
whole line into a different typeface.

## Scheduled posts

| Date | Topic | Status |
|---|---|---|
| 2026-08-28 (금) | Chimaek and Burning Friday | slides ready, unpublished |
| 2026-08-29 (토) | Hiking gear as a social uniform | slides ready, unpublished |
| 2026-08-30 (일) | Kinship terms for strangers | slides ready, unpublished |

All three are evergreen culture explainers rather than breaking news. Check
each day's `fact_check` list before publishing.
