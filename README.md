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
| Facebook page | What's Hot Korea | `61594049484996` |
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

## Writing the slides

Slide copy is generated from the instructions in
`claude-project-instructions.md`, kept here so the prompt is versioned
alongside the output rather than living only in the Claude web UI.
