#!/usr/bin/env python3
"""Publish one card-news carousel to Instagram, a Facebook Page and Threads.

Usage:
    python post.py "caption text" img/slide1.png img/slide2.png ...

Images must already be pushed to GitHub Pages -- the Meta APIs only accept
public URLs, never file uploads. The script turns each local path into
BASE_URL/<path> and hands that to Meta.
"""
import json
import os
import sys
import time
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
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def wait_ready(base, container_id, token, tries=20):
    """Meta builds carousel containers asynchronously; publish too early and it 400s."""
    for _ in range(tries):
        status = call(base + "/" + container_id,
                      {"fields": "status_code", "access_token": token}, "GET")
        if status.get("status_code") == "FINISHED":
            return
        if status.get("status_code") == "ERROR":
            raise RuntimeError(f"container {container_id} failed: {status}")
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


def post_threads(urls, caption, user_id, token):
    children = [
        call(f"{THREADS}/{user_id}/threads",
             {"media_type": "IMAGE", "image_url": u,
              "is_carousel_item": "true", "access_token": token})["id"]
        for u in urls
    ]
    parent = call(f"{THREADS}/{user_id}/threads", {
        "media_type": "CAROUSEL",
        "children": ",".join(children),
        "text": caption,
        "access_token": token,
    })["id"]
    wait_ready(THREADS, parent, token)
    return call(f"{THREADS}/{user_id}/threads_publish",
                {"creation_id": parent, "access_token": token})


def main(argv):
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

    targets = [
        ("instagram", post_instagram, os.environ["IG_USER_ID"], os.environ["IG_TOKEN"]),
        ("facebook", post_facebook, os.environ["FB_PAGE_ID"], os.environ["FB_TOKEN"]),
        ("threads", post_threads, os.environ["THREADS_USER_ID"], os.environ["THREADS_TOKEN"]),
    ]
    for name, fn, target_id, token in targets:
        try:
            print(name, fn(urls, caption, target_id, token))
        except Exception as exc:  # one dead platform must not block the others
            print(f"{name} FAILED: {exc}", file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv)
