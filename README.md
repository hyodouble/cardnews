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

Setting this up on another computer is documented separately in `SETUP.md`,
including the Meta configuration, the scheduler and how the credentials travel.

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

Weekend posts go up in full before the weekend starts. Saturday and Sunday are
worked on from a different computer, so their day folder, `content/<date>.json`,
the rendered `img/<date>/` cards **and** the `assets/<date>/` source photos are
all committed and pushed -- the photos included, not just the slides, so nothing
has to be regenerated on the other machine.

Push first. `post.py` refuses to run if a slide is not yet reachable at its
public URL — that check exists because Meta's error for an unreachable image
is unhelpful.

Publishing runs on a system-user token that does not expire, so the old
60-day refresh is gone. `publish_today.py` takes no arguments and publishes the
day's carousel if it is ready, which is what the daily 08:00 task calls:

```bash
powershell -ExecutionPolicy Bypass -File register_schedule.ps1
```

The page token needs `instagram_manage_comments` and `pages_manage_engagement`
on top of the publishing scopes, or `--reply` fails with OAuth 10 on Instagram
and OAuth 200 on Facebook while the Threads reply still goes through. Threads
replies run on the separate Threads token and need nothing extra.

Both scopes were added to the app's use cases on 2026-09-02, but no login
dialog would hand back a token carrying them: the Graph API Explorer dies on
`Invalid Scopes: pages_read_user_content`, and every hand-built OAuth dialog
answers `URL을 읽어들일 수 없습니다` because this app is built on use cases and
has no Facebook Login product, so there is nowhere to register a redirect URI.

The way through was a **system user**. `cardnews-publisher`
(id 61594067399687) in the business portfolio holds the page, the Instagram
account and the app, and its token never expires. `adopt_system_token.py`
trades that token for the page token and writes both into `.env`:

```bash
python adopt_system_token.py <file holding the system-user token>
```

That fixed Instagram: comments now go up through the API, and
`comment.py <post id> ["text"]` backfills one onto a post that is already up.

Facebook page comments still refuse with OAuth 200. The page token does carry
`pages_manage_engagement` -- `debug_token` lists it -- but its granular scopes
come back with no `target_ids`, so the permission is attached to no page at
all. Reads fail the same way. A system user cannot fix that on its own: a
comment call only accepts a page token, and this page token is not bound to
the page. Closing it needs either App Review for the two comment permissions,
or a Facebook Login use case added to the app so a user token from the page's
own admin can mint the page token. Until then Facebook comments go up by hand
from the `reply` in each `content/<date>.json`.

To reissue the page token with a new set of scopes:

```bash
# 1. approve the scopes -- the Explorer permission list hides anything whose
#    product is not added to the app, so ask for them in the URL instead
open "https://www.facebook.com/v21.0/dialog/oauth?client_id=$APP_ID&redirect_uri=https://www.facebook.com/connect/login_success.html&response_type=token&scope=pages_show_list,pages_read_engagement,pages_manage_posts,pages_manage_engagement,instagram_basic,instagram_content_publish,instagram_manage_comments,business_management"
# 2. copy #access_token=... out of the address bar into USER_TOKEN in .env
# 3. fill APP_ID and APP_SECRET in .env too, then
python refresh_token.py
```

This route is dead until a Facebook Login use case is added to the app; the
dialog rejects the redirect URI before it ever asks about scopes.

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
| 2026-09-04 (금) | Chasu, a night out in numbered rounds | published via API to Instagram, Facebook and Threads |
| 2026-09-05 (토) | Jjimjilbang, sleeping on a floor full of strangers | slides ready, unpublished |
| 2026-09-06 (일) | Muin minwon balgeupgi, documents from a kiosk | copy and prompts ready, no photos yet |

All of them are evergreen culture explainers rather than breaking news. Check
each day's `fact_check` list before publishing.

## Topic ideas

- **Packing movers and the ladder truck.** A crew packs the flat and a truck lifts
  everything through a fifteenth-floor window. It is the closest match to the
  daeri unjeon shape found so far -- a stranger handles your things, the machine
  is the spectacle, and the trade has a name, a price and a workforce. **Do not
  write it yet.** On 2026-08-27 a moving company's ladder truck tipped over in
  Cheonan and killed a seven-year-old on the way to school, with two workers
  arrested the next day; a mover had already fallen thirty metres to his death in
  Incheon that May. A bright "look what Korea built" carousel does not survive
  landing in the same month as that. Revisit in 2027, and only if the shadow
  slide can carry chronic risk rather than a specific death.

- **Parcels left at the door.** Couriers leave boxes in the hallway or with the
  guard, and they are still there hours later. Hold this one back for a while:
  the 2026-09-01 jari-matgi carousel already spent the "nothing gets stolen
  here" angle on a laptop in a cafe, and two posts making the same point in the
  same month read as one post twice. Worth pairing with something the laptop
  card could not carry -- the guard's office as an informal delivery locker, and
  what happens when a box does go missing.

## API publishing

The Meta app `korea-cardnews-publisher` was restricted for "unusual activity"
on 2026-08-31 and every call failed with OAuth 190 / 200. The restriction was
gone by 2026-09-02: the same `.env` tokens published the KBO carousel to all
three platforms in one `post.py` run. If the errors come back, wait the app out
rather than registering a replacement -- a second app reads as evasion and puts
the Instagram account at risk.
