#!/usr/bin/env python3
"""Publish one card-news carousel to Instagram, a Facebook Page and Threads.

Usage:
    python post.py [--reply "comment text"] "caption text" img/slide1.png ...

--reply leaves one comment under the post on all three platforms. Replies are
what Threads re-circulates a post on, so every carousel ships with one.

Images must already be pushed to GitHub Pages -- the Meta APIs only accept
public URLs, never file uploads. The script turns each local path into
BASE_URL/<path> and hands that to Meta.
"""
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

GRAPH = "https://graph.facebook.com/v21.0"
THREADS = "https://graph.threads.net/v1.0"


def load_env(path=".env"):
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())


def call(url, params, method="POST"):
    data = urllib.parse.urlencode(params).encode()
    if method == "GET":
        req = urllib.request.Request(f"{url}?{data.decode()}")
    else:
        req = urllib.request.Request(url, data=data, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as exc:
        # Meta puts the actual reason in the body; the status line alone is useless.
        raise RuntimeError(f"{exc.code} {url}: {exc.read().decode()[:500]}") from None


def wait_ready(base, container_id, token, tries=20):
    """Meta builds carousel containers asynchronously; publish too early and it 400s.

    The two APIs disagree on the field name: Graph reports ``status_code``,
    Threads reports ``status`` and rejects the other outright.
    """
    field = "status" if base == THREADS else "status_code"
    for _ in range(tries):
        state = call(base + "/" + container_id,
                     {"fields": field, "access_token": token}, "GET").get(field)
        if state == "FINISHED":
            return
        if state in ("ERROR", "EXPIRED"):
            raise RuntimeError(f"container {container_id} failed: {state}")
        time.sleep(3)
    raise TimeoutError(f"container {container_id} never finished")


def post_instagram(urls, caption, ig_id, token):
    children = [
        call(f"{GRAPH}/{ig_id}/media",
             {"image_url": u, "is_carousel_item": "true", "access_token": token})["id"]
        for u in urls
    ]
    parent = call(f"{GRAPH}/{ig_id}/media", {
        "media_type": "CAROUSEL",
        "children": ",".join(children),
        "caption": caption,
        "access_token": token,
    })["id"]
    wait_ready(GRAPH, parent, token)
    return call(f"{GRAPH}/{ig_id}/media_publish",
                {"creation_id": parent, "access_token": token})


def post_facebook(urls, caption, page_id, token):
    """Unpublished photos first, then one post that carries them all."""
    media = [
        {"media_fbid": call(f"{GRAPH}/{page_id}/photos",
                            {"url": u, "published": "false", "access_token": token})["id"]}
        for u in urls
    ]
    params = {"message": caption, "access_token": token}
    for i, item in enumerate(media):
        params[f"attached_media[{i}]"] = json.dumps(item)
    return call(f"{GRAPH}/{page_id}/feed", params)


# Threads rejects anything longer than this, unlike Instagram and Facebook.
THREADS_TEXT_LIMIT = 500


def fit_threads(caption):
    """Trim to what Threads accepts without leaving a sentence hanging.

    Captions are written as English, a "· · ·" rule, then Korean. Dropping
    everything from the rule keeps one whole language rather than half of two.
    """
    if len(caption) <= THREADS_TEXT_LIMIT:
        return caption
    head = caption.split("· · ·")[0].strip()
    if len(head) > THREADS_TEXT_LIMIT:
        head = head[:THREADS_TEXT_LIMIT]
        cut = max(head.rfind(". "), head.rfind("\n"))
        head = (head[:cut + 1] if cut > 0 else head).strip()
    return head


def post_threads(urls, caption, user_id, token):
    children = [
        call(f"{THREADS}/{user_id}/threads",
             {"media_type": "IMAGE", "image_url": u,
              "is_carousel_item": "true", "access_token": token})["id"]
        for u in urls
    ]
    # Children are built asynchronously; a parent referencing an unfinished one
    # is rejected as an invalid carousel item.
    for child in children:
        wait_ready(THREADS, child, token)
    parent = call(f"{THREADS}/{user_id}/threads", {
        "media_type": "CAROUSEL",
        "children": ",".join(children),
        "text": fit_threads(caption),
        "access_token": token,
    })["id"]
    wait_ready(THREADS, parent, token)
    return call(f"{THREADS}/{user_id}/threads_publish",
                {"creation_id": parent, "access_token": token})


def reply_graph(post_id, text, _target_id, token):
    """Instagram and Facebook both take a comment on the published object."""
    return call(f"{GRAPH}/{post_id}/comments", {"message": text, "access_token": token})


def reply_threads(post_id, text, user_id, token):
    """A Threads reply is a normal text post that points at its parent."""
    container = call(f"{THREADS}/{user_id}/threads", {
        "media_type": "TEXT",
        "text": fit_threads(text),
        "reply_to_id": post_id,
        "access_token": token,
    })["id"]
    wait_ready(THREADS, container, token)
    return call(f"{THREADS}/{user_id}/threads_publish",
                {"creation_id": container, "access_token": token})


def main(argv):
    reply = ""
    if "--reply" in argv:
        i = argv.index("--reply")
        reply = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    if len(argv) < 3:
        sys.exit(__doc__)
    load_env()
    caption, paths = argv[1], argv[2:]

    base = os.environ["BASE_URL"].rstrip("/")
    urls = [f"{base}/{p.replace(os.sep, '/')}" for p in paths]
    for url in urls:
        with urllib.request.urlopen(urllib.request.Request(url, method="HEAD")) as r:
            if r.status != 200:
                sys.exit(f"not public yet: {url} -- push to GitHub first")

    # Instagram publishing runs on the page token too, so one token covers both.
    page_token = os.environ.get("PAGE_TOKEN", "")
    targets = [
        ("instagram", post_instagram, reply_graph,
         os.environ.get("IG_USER_ID"), page_token),
        ("facebook", post_facebook, reply_graph,
         os.environ.get("FB_PAGE_ID"), page_token),
        ("threads", post_threads, reply_threads,
         os.environ.get("THREADS_USER_ID"), os.environ.get("THREADS_TOKEN")),
    ]
    for name, fn, replier, target_id, token in targets:
        # A platform still waiting on its credentials must not block the others.
        if not target_id or not token:
            print(f"{name} skipped: missing id or token in .env", file=sys.stderr)
            continue
        try:
            result = fn(urls, caption, target_id, token)
            print(name, result)
        except Exception as exc:  # one dead platform must not block the others
            print(f"{name} FAILED: {exc}", file=sys.stderr)
            continue
        if not reply:
            continue
        try:
            # The post is already up; a failed comment is not worth aborting on.
            print(name, "reply", replier(result["id"], reply, target_id, token))
        except Exception as exc:
            print(f"{name} reply FAILED: {exc}", file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv)
