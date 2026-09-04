# Setting this up on another machine

Everything needed to run What's Hot Korea from a different computer is in this
repository, with one deliberate exception: the four secret values. They are not
here and must never be committed — see [Carrying the credentials](#carrying-the-credentials).

Read `README.md` first for what the project is. This file is the checklist for
making a second machine able to publish.

## What runs, and when

| Piece | What it does |
|---|---|
| `make_cards.py` | Renders `content/<date>.json` + `assets/<date>/*.png` into ten 1080×1080 slides |
| `make_brief.py` | Writes the human-facing README for a day folder |
| `post.py` | Publishes one carousel to Instagram, the Facebook page and Threads, with a first comment |
| `publish_today.py` | Publishes a day's carousel if it is ready, does nothing if it is not. Takes an optional date |
| `register_schedule.ps1` | Registers a daily Windows task that runs `publish_today.py`. Not in use -- publishing is manual |
| `comment.py` | Puts a comment on a post that is already up, for when a publish-time comment failed |
| `adopt_system_token.py` | Trades the Meta system-user token for the page token and writes both into `.env` |

## 1. The machine

- **Python 3.10+** and **Pillow** (`pip install pillow`). Nothing else — every
  other import is standard library.
- **git**, with push access to `hyodouble/cardnews`.
- Fonts are committed under `fonts/`, so type renders identically everywhere.
  Korean glyphs fall back to Malgun Gothic on Windows; on macOS or Linux install
  a Korean face (`AppleGothic` and `Noto Sans KR` both work) or the Hangul in a
  headline renders as boxes.

```bash
git clone https://github.com/hyodouble/cardnews.git
cd cardnews
pip install pillow
cp .env.example .env      # then fill it in, see below
```

## 2. `.env`

`.env` is gitignored. `.env.example` lists every key. What each one is:

| Key | What it is | Where it comes from |
|---|---|---|
| `BASE_URL` | GitHub Pages root serving `img/` | Fixed: `https://hyodouble.github.io/cardnews` |
| `FB_PAGE_ID` | Facebook page id | In `.env.example`, not secret |
| `IG_USER_ID` | Instagram business account id | In `.env.example`, not secret |
| `THREADS_USER_ID` | Threads profile id | In `.env.example`, not secret |
| `PAGE_TOKEN` | Page token used for Instagram **and** Facebook publishing | Derived by `adopt_system_token.py` |
| `SYSTEM_TOKEN` | Meta system-user token, no expiry | Meta business settings, see step 3 |
| `THREADS_TOKEN` | Threads publishing token | Threads API, separate from the Graph tokens |
| `APP_ID` / `APP_SECRET` | Meta app credentials | Only needed by the legacy `refresh_token.py` path |

Only `PAGE_TOKEN`, `SYSTEM_TOKEN`, `THREADS_TOKEN` and `APP_SECRET` are secret.
The ids are not.

## 3. The Meta side, if it ever has to be rebuilt

The app is `korea-cardnews-publisher` (id `1443034627645657`) and it is built on
Meta's **use cases** model, not the old products model. That has one consequence
worth writing down: **there is no Facebook Login product, so there is nowhere to
register an OAuth redirect URI**, and every hand-built OAuth dialog dies with
`URL을 읽어들일 수 없습니다`. Do not spend another afternoon on that dialog.

The way in is a **system user**:

1. business.facebook.com → 비즈니스 설정 → 사용자 → 시스템 사용자 → 추가.
   The current one is `cardnews-publisher`, id `61594067399687`, Employee role.
   Creating one requires accepting Facebook's non-discrimination policy once.
2. 자산 할당, three assets:
   - Facebook page **What's Hot Korea** — 부분적인 액세스(비즈니스 도구 및 Facebook)
   - Instagram account **whatshotkorea** — 콘텐츠 + 커뮤니티 활동
   - App **korea-cardnews-publisher** — 앱 개발
3. 토큰 생성 → app `korea-cardnews-publisher` → 만료 **안 함** → scopes:
   `pages_show_list`, `pages_read_engagement`, `pages_manage_posts`,
   `pages_manage_engagement`, `instagram_basic`, `instagram_content_publish`,
   `instagram_manage_comments`, `business_management`.
4. Save the token to a file and run:

   ```bash
   python adopt_system_token.py <file holding the token>
   ```

   It writes `PAGE_TOKEN` and `SYSTEM_TOKEN` into `.env` and prints the page name
   and the scopes the token actually carries. Both comment scopes should appear.

**Known ceiling:** Instagram and Threads comments publish through the API;
Facebook page comments still answer OAuth 200. The page token carries
`pages_manage_engagement`, but its granular scopes come back with no
`target_ids`, so the permission is bound to no page. Closing that needs App
Review or a Facebook Login use case. It is deliberately not being chased —
Facebook is the low-priority channel here.

The Threads token is separate and was issued through the Threads API. It is not
derived from the system user and `adopt_system_token.py` does not touch it.

## 4. Image hosting

The Meta APIs take image URLs only, never uploads, so every slide has to be
public before it can be published. GitHub Pages serves this repo's `img/`
folder. That means the publishing order is always **commit and push first, then
publish** — `post.py` refuses to run if a slide is not reachable yet.

Nothing to configure on a new machine beyond push access.

## 5. The desktop working folder

Rendering writes to two places: `img/<date>/` inside the repo (what gets
published) and a working copy on the desktop for eyeballing:

```
~/Desktop/koreahotshot/
  2026-09-04_금요일/
    slides/        01.png … 10.png
    README.md      caption, hashtags, fact-check flags, slide text
    PROMPTS.md     the ten Gemini prompts (also kept in the repo)
```

The folder name is `<date>_<Korean weekday>`. Nothing reads this folder
programmatically — it exists so a person can flick through the day's cards and
copy the caption. On a machine where you don't want it, pass only the repo path
to `make_cards.py` and skip `make_brief.py`.

## 6. A day, start to finish

```bash
# 1. copy: write content/<date>.json and <date>_<요일>/PROMPTS.md
# 2. photos: ten images from Gemini image mode into assets/<date>/
#    filenames: hook, content2..content7, stat, content9, cta  (.png)
# 3. render
python make_cards.py content/2026-09-04.json img/2026-09-04 "$HOME/Desktop/koreahotshot/2026-09-04_금요일/slides"
python make_brief.py content/2026-09-04.json "$HOME/Desktop/koreahotshot/2026-09-04_금요일"

# 4. push, or the publish will refuse
git add img/2026-09-04 content/2026-09-04.json && git commit -m "..." && git push

# 5. publish -- nothing goes out until this runs
python publish_today.py 2026-09-04
```

Photo rules that cost real time when ignored are in `README.md` under
*Generating the photos*: never regenerate for aspect ratio or the Gemini
watermark, and keep Hangul signage and identifiable faces out of frame.

## 7. Publishing is manual

Nothing publishes on its own. `publish_today.py` sends a day's carousel when you
run it, and does nothing until then:

```bash
python publish_today.py                # today
python publish_today.py 2026-09-06     # a specific day
```

It publishes only if `content/<date>.json` and the ten slides exist; otherwise it
logs one line and exits. Every run, success or failure, appends to `publish.log`.

A daily 08:00 Windows task used to do this and was removed on 2026-09-04, for two
reasons worth keeping written down. The day a carousel went viral, the next post
was already going out on its own before anyone decided it should -- a schedule
turns the timing decision into a default. And the task ran inside a logged-on
console session, so closing the window killed Python mid-upload: the task
reported `0xC000013A` and `publish.log` held a `publishing` line with no result,
which is the worst possible state to find because it does not say whether Meta
got the post. Check the account, not the log, if you ever see that.

`register_schedule.ps1` is still here. If the schedule is ever wanted back:

```powershell
powershell -ExecutionPolicy Bypass -File register_schedule.ps1              # 08:00 daily
powershell -ExecutionPolicy Bypass -File register_schedule.ps1 -Time 07:30
powershell -ExecutionPolicy Bypass -File register_schedule.ps1 -Remove
```

Register it to run whether the user is logged on or not, or it will die the same
way. The machine also has to be awake -- `-WakeToRun` wakes a sleeping machine and
does nothing for one that is shut down.

**Weekends on another computer.** Prepare the carousels in advance, then publish
by hand from whatever machine is on:

```bash
git pull                       # slides pushed from the other machine come with it
python publish_today.py 2026-09-06
```

Only the `.env` values have to be carried over; everything else is in this repo.

## Carrying the credentials

The tokens are **not in this repository and must not be put in it.** Committing
them does not become safe by deleting the repo afterwards: the values live on in
GitHub's servers and in every clone, and the system-user token does not expire,
so the only real remedy after a leak is reissuing it in Meta business settings.

To set up a second machine, move `.env` across out of band — a USB stick, a
password manager entry, or an encrypted note — and delete the copy afterwards.
It is a 15-line file; this takes under a minute.

If a token ever does get exposed: Meta business settings → 시스템 사용자 →
`cardnews-publisher` → **토큰 취소**, then generate a new one and rerun
`adopt_system_token.py`. Revoking is what makes the old value harmless.
