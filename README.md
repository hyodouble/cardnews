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
python post.py --reply "first comment" "caption text" img/2026-08-28-1.png ...
```

Every post ships with one reply, left as a comment on Instagram and Facebook
and as a threaded reply on Threads. It adds one fact the carousel left out and
ends on a question back to the reader. Threads re-circulates a post on its
replies, so the reply is what keeps a post alive past its first hour -- the
2026-09-01 carousel reached 2,258 views on 5 followers off three reposts, and
zero replies.

Push first. `post.py` refuses to run if a slide is not yet reachable at its
public URL — that check exists because Meta's error for an unreachable image
is unhelpful.

Long-lived Meta tokens expire after 60 days; refresh them and update `.env`.

The page token needs `instagram_manage_comments` and `pages_manage_engagement`
on top of the publishing scopes, or `--reply` fails with OAuth 10 on Instagram
and OAuth 200 on Facebook while the Threads reply still goes through. Threads
replies run on the separate Threads token and need nothing extra.

Both scopes were added to the app's use cases on 2026-09-02 and they now show
in the Graph API Explorer, but no login dialog will hand back a token carrying
them: the Explorer's own request dies on `Invalid Scopes:
pages_read_user_content`, a permission it adds by itself and Meta no longer
accepts, and every hand-built dialog (implicit, code, with and without the
`cardnews-publish-comment` configuration, id 1045642294762468) answers
"Sorry, something went wrong". Until that clears, Instagram and Facebook
comments go up by hand -- the reply text is in each `content/<date>.json`.

To reissue the page token with a new set of scopes:

```bash
# 1. approve the scopes -- the Explorer permission list hides anything whose
#    product is not added to the app, so ask for them in the URL instead
open "https://www.facebook.com/v21.0/dialog/oauth?client_id=$APP_ID&redirect_uri=https://www.facebook.com/connect/login_success.html&response_type=token&scope=pages_show_list,pages_read_engagement,pages_manage_posts,pages_manage_engagement,instagram_basic,instagram_content_publish,instagram_manage_comments,business_management"
# 2. copy #access_token=... out of the address bar into USER_TOKEN in .env
# 3. fill APP_ID and APP_SECRET in .env too, then
python refresh_token.py
```

`redirect_uri` has to be listed under Facebook Login > Settings > Valid OAuth
Redirect URIs first. The user token from that dialog lives about an hour;
`refresh_token.py` trades it for a long-lived one and stores the page token it
yields, which does not expire.

## Making a carousel

One JSON per post lives in `content/<date>.json`: ten slides, the caption, the
hashtags, a `reply` for the first comment, and a `fact_check` list of claims
that still need verifying. Slide
copy follows the rules in `claude-project-instructions.md`, kept here so the
prompt is versioned alongside the output rather than living only in the Claude
web UI.

```bash
python make_cards.py content/2026-08-28.json img/2026-08-28 "<desktop>/2026-08-28_금요일/slides"
python make_brief.py content/2026-08-28.json "<desktop>/2026-08-28_금요일"
```

Slides are English only. Posts through 2026-09-02 also shipped a Korean edition
rendered from a `ko` block on each slide; that was dropped on 2026-09-02 because
the audience reads English and the second translation cost more to write than it
returned. The old `ko` blocks are still in those files and are simply ignored.

`make_cards.py` renders 1080x1080 PNGs in the account palette — four slide
types (`hook`, `content`, `stat`, `cta`) picked per slide by its `type` field.
It accepts several output directories so the repo copy and the desktop working
copy are written in one pass. `make_brief.py` writes the human-facing README
for a day folder: caption to copy, hashtags, fact-check flags, slide text.

Korean text renders through Malgun Gothic and English through Arial Black,
chosen per line, so a Hangul word inside an English headline does not drag the
whole line into a different typeface.

## Generating the photos

Ten photos per post come out of Gemini in image mode, one per prompt in that
day's `PROMPTS.md`, saved into `assets/<date>/` under the filenames the renderer
expects. Two rules on regenerating, because a regeneration costs a full image
call and usually buys nothing:

- **Never regenerate to fix the aspect ratio.** Gemini's chat view crops results
  to a wide preview, but the downloaded file is 1024x1024 square. A "make it 1:1"
  follow-up returns the same picture again.
- **Never regenerate to fix the Gemini watermark.** `make_cards.py` trims 12% off
  the right and bottom edges, which takes the ✦ mark with it.

Regenerate only when the picture itself is wrong: the subject or the composition
does not match what the slide claims, a logo or legible text got in, or the
prompt was based on a wrong mental image of the real thing. That last one is
worth a search first — the 2026-09-02 응원단상 photo had to be redone because the
prompt described a tower in the middle of the stands instead of the low deck at
the front, and looking at a real photo settled it in one attempt.

## Scheduled posts

| Date | Topic | Status |
|---|---|---|
| 2026-08-28 (금) | Chimaek and Burning Friday | slides ready, unpublished |
| 2026-08-29 (토) | Hiking gear as a social uniform | slides ready, unpublished |
| 2026-08-30 (일) | Kinship terms for strangers | slides ready, unpublished |
| 2026-08-31 (월) | Chukuigeum, the wedding cash ledger | published manually (English edition) |
| 2026-09-01 (화) | Jari-matgi, leaving a laptop on the table | slides ready |
| 2026-09-02 (수) | KBO cheering culture, a song per batter | published via API to Instagram, Facebook and Threads |
| 2026-09-03 (목) | Daeri unjeon, a stranger drives your car home | published via API to Instagram, Facebook and Threads |

All of them are evergreen culture explainers rather than breaking news. Check
each day's `fact_check` list before publishing.

## API publishing

The Meta app `korea-cardnews-publisher` was restricted for "unusual activity"
on 2026-08-31 and every call failed with OAuth 190 / 200. The restriction was
gone by 2026-09-02: the same `.env` tokens published the KBO carousel to all
three platforms in one `post.py` run. If the errors come back, wait the app out
rather than registering a replacement -- a second app reads as evasion and puts
the Instagram account at risk.
