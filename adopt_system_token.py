#!/usr/bin/env python3
"""Trade the system-user token for the page token and store it in .env.

The system user was created so the page token can carry
pages_manage_engagement and instagram_manage_comments, which the OAuth
dialog could not hand back. Run it once after generating a token in
Business settings:

    python adopt_system_token.py <path to a file holding the token>

Nothing is printed but the page name and the scopes the token carries.
"""
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

GRAPH = "https://graph.facebook.com/v21.0"
PAGE_ID = "1253255244544447"


def get(path, **params):
    url = f"{GRAPH}/{path}?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as exc:
        # Meta puts the real reason in the body, never in the status line.
        raise RuntimeError(f"{exc.code} {path}: {exc.read().decode()[:400]}") from None


def set_env(key, value):
    lines = open(".env", encoding="utf-8").read().splitlines()
    for i, line in enumerate(lines):
        if line.startswith(f"{key}="):
            lines[i] = f"{key}={value}"
            break
    else:
        lines.append(f"{key}={value}")
    open(".env", "w", encoding="utf-8").write("\n".join(lines) + "\n")


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    # utf-8-sig: PowerShell writes a BOM, and Meta cannot parse a token
    # with one glued to the front.
    token = open(argv[1], encoding="utf-8-sig").read().strip()

    # A system user reads its page token off the page itself; /me/accounts
    # answers 400 for system users on some app configurations.
    page = get(PAGE_ID, fields="name,access_token", access_token=token)
    page_token = page.get("access_token") or token
    scopes = get("debug_token", input_token=page_token,
                 access_token=token)["data"].get("scopes", [])

    # The derived page token comes back without the scopes the system user
    # holds, so keep the system-user token too and let callers fall back to it.
    set_env("PAGE_TOKEN", page_token)
    set_env("SYSTEM_TOKEN", token)
    print("page:", page["name"])
    print("scopes:", ", ".join(sorted(scopes)))


if __name__ == "__main__":
    main(sys.argv)
