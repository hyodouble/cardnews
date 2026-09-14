#!/usr/bin/env bash
# Render, push and publish one day's carousel in a single run. macOS port of run_day.ps1.
#
#   ./run_day.sh                  # today
#   ./run_day.sh 2026-09-14
#   ./run_day.sh --yes            # no confirmation
#   ./run_day.sh --render-only    # stop before posting
#
# What it does, in order: pull, render the ten slides into img/<date> and into the
# desktop day folder, write the brief, commit and push the slides, wait until
# GitHub Pages actually serves the first one, then publish.
#
# The wait matters. post.py HEADs every slide URL and refuses to run if one is not
# public yet, and Pages takes about a minute to deploy after a push.
#
# Publishing still asks before it posts, because that is the one step this repo
# deliberately keeps manual -- see README. --yes skips the question, --render-only
# stops after the push and leaves the posting for later.
set -u
cd "$(dirname "$0")"

# SETUP.md section 5 puts the eyeball copy here; override with KOREAHOTSHOT_DIR.
DESKTOP_ROOT="${KOREAHOTSHOT_DIR:-$HOME/Desktop/koreahotshot}"
PY=python3

fail() { printf '\033[31mSTOP: %s\033[0m\n' "$1" >&2; exit 1; }
step() { printf '\n\033[36m== %s\033[0m\n' "$1"; }

date_arg=""; yes=0; render_only=0
for a in "$@"; do
    case "$a" in
        --yes|-y)         yes=1 ;;
        --render-only|-r) render_only=1 ;;
        -h|--help)        sed -n '2,18p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
        -*)               fail "unknown flag: $a" ;;
        *)                date_arg="$a" ;;
    esac
done
DATE="${date_arg:-$(date +%F)}"

content="content/$DATE.json"
[ -f "$content" ] || fail "no $content -- nothing prepared for $DATE"

photos=$(ls assets/"$DATE"/*.png 2>/dev/null | wc -l | tr -d ' ')
[ "$photos" -ge 10 ] || fail "assets/$DATE has $photos photos, needs 10"

meta=$($PY -c 'import json,sys; d=json.load(open(sys.argv[1],encoding="utf-8")); print(d["weekday"], d["title"])' "$content") \
    || fail "$content has no weekday/title"
read -r weekday title <<<"$meta"
folder="$DESKTOP_ROOT/${DATE}_${weekday}"
echo "$DATE ($weekday) -- $title"

step "pulling"
git pull --ff-only || fail "git pull failed -- resolve it by hand, then run this again"

step "rendering"
$PY make_cards.py "$content" "img/$DATE" "$folder/slides" || fail "make_cards.py failed"
$PY make_brief.py "$content" "$folder"                    || fail "make_brief.py failed"

slides=$(ls img/"$DATE"/*.png 2>/dev/null | wc -l | tr -d ' ')
[ "$slides" -eq 10 ] || fail "img/$DATE has $slides slides, needs 10"
echo "10 slides in img/$DATE and in $folder"

step "pushing"
git add "img/$DATE" "assets/$DATE" "$content"
# exit 1 from --quiet just means there are staged changes
if ! git diff --cached --quiet; then
    git commit -m "Render the $DATE slides" || fail "git commit failed"
fi
git push || fail "git push failed -- the slides must be public before posting"

step "waiting for GitHub Pages"
base=$(sed -n 's/^BASE_URL=//p' .env | tr -d '\r' | head -1)
[ -n "$base" ] || fail "no BASE_URL in .env"
url="${base%/}/img/$DATE/01.png"
live=0
for attempt in $(seq 1 20); do
    if [ "$(curl -s -o /dev/null -I -w '%{http_code}' --max-time 10 "$url")" = "200" ]; then
        live=1; break
    fi
    echo "  not served yet ($attempt/20), waiting 15s"
    sleep 15
done
[ "$live" = 1 ] || fail "$url still not public after five minutes -- check the Pages build, then run it again with $DATE"
echo "serving $url"

if [ "$render_only" = 1 ]; then
    printf '\nrendered and pushed. To post it:  %s publish_today.py %s\n' "$PY" "$DATE"
    exit 0
fi

step "publishing"
if [ "$yes" != 1 ]; then
    read -r -p "Post '$title' to Instagram, Facebook and Threads? [y/N] " answer
    if [ "$answer" != "y" ]; then
        echo "left unpublished. To post it later:  $PY publish_today.py $DATE"
        exit 0
    fi
fi
$PY publish_today.py "$DATE"
published=$?

echo
if [ "$published" = 0 ]; then
    printf '\033[32mpublished. Mark the day in the README table.\033[0m\n'
else
    printf '\033[33mpublish_today.py reported a failure. Read publish.log.\033[0m\n'
    echo "Instagram can answer 403 and post anyway, so check before retrying:"
    echo "  $PY -c \"import os,post; post.load_env(); ig=os.environ['IG_USER_ID']; print(post.call(f'{post.GRAPH}/{ig}/media',{'fields':'id,timestamp','limit':'3','access_token':os.environ['PAGE_TOKEN']},'GET'))\""
fi
echo "Facebook's first comment does not go up through the API. Paste the 'reply' from $content by hand."
