#!/usr/bin/env python3
"""Turn a login-dialog result into the never-expiring page token in .env.

Fill APP_ID, APP_SECRET and one of USER_CODE (the ?code= from a Facebook
Login for Business redirect) or USER_TOKEN (a short-lived user token), then:

    python refresh_token.py

A page token derived from a long-lived user token does not expire, so this
runs once per scope change rather than on a schedule.
"""
import os
import re
import sys

from post import GRAPH, call, load_env


def main():
    load_env()
    missing = [k for k in ("APP_ID", "APP_SECRET", "FB_PAGE_ID")
               if not os.environ.get(k)]
    if missing:
        sys.exit("missing in .env: " + ", ".join(missing))

    code = os.environ.get("USER_CODE", "")
    if code:
        # Facebook Login for Business hands back a code, not a token; the
        # exchanged user token is already long-lived, so no second swap.
        long_lived = call(f"{GRAPH}/oauth/access_token", {
            "client_id": os.environ["APP_ID"],
            "client_secret": os.environ["APP_SECRET"],
            "redirect_uri": os.environ.get(
                "REDIRECT_URI", "https://hyodouble.github.io/cardnews/"),
            "code": code,
        }, "GET")["access_token"]
    elif os.environ.get("USER_TOKEN"):
        long_lived = call(f"{GRAPH}/oauth/access_token", {
            "grant_type": "fb_exchange_token",
            "client_id": os.environ["APP_ID"],
            "client_secret": os.environ["APP_SECRET"],
            "fb_exchange_token": os.environ["USER_TOKEN"],
        }, "GET")["access_token"]
    else:
        sys.exit("missing in .env: USER_CODE or USER_TOKEN")

    pages = call(f"{GRAPH}/me/accounts",
                 {"access_token": long_lived}, "GET")["data"]
    page_id = os.environ["FB_PAGE_ID"]
    token = next((p["access_token"] for p in pages if p["id"] == page_id), None)
    if not token:
        sys.exit(f"page {page_id} not in this user's pages: "
                 + ", ".join(f"{p['id']} {p['name']}" for p in pages))

    scopes = call(f"{GRAPH}/debug_token",
                  {"input_token": token, "access_token": token},
                  "GET")["data"].get("scopes", [])
    print("scopes:", ", ".join(scopes))
    for want in ("instagram_manage_comments", "pages_manage_engagement"):
        if want not in scopes:
            print(f"WARNING: {want} still missing -- comments will fail",
                  file=sys.stderr)

    # Rewrite in place so the comments and the other keys survive.
    with open(".env", encoding="utf-8") as fh:
        env = fh.read()
    env = re.sub(r"^PAGE_TOKEN=.*$", "PAGE_TOKEN=" + token, env,
                 count=1, flags=re.M)
    with open(".env", "w", encoding="utf-8", newline="\n") as fh:
        fh.write(env)
    print("PAGE_TOKEN updated in .env")


if __name__ == "__main__":
    main()
