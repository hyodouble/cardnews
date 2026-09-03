#!/usr/bin/env python3
"""Leave a comment on a post that is already up.

Usage:
    python comment.py <post id> ["comment text"]

With no text, the reply from content/<today>.json is used. Post ids come out
of post.py's own output: an Instagram media id, or a Facebook
<page>_<post> id. This exists for the days a publish went through but its
comment did not.
"""
import json
import os
import sys
import datetime

from post import GRAPH, call, load_env


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    post_id = argv[1]
    if len(argv) > 2:
        text = argv[2]
    else:
        today = datetime.date.today().isoformat()
        with open(f"content/{today}.json", encoding="utf-8") as fh:
            text = json.load(fh)["reply"]

    load_env()
    # The page token derived from the system user does not carry its scopes,
    # so fall back to the system-user token when Facebook refuses.
    tokens = [os.environ[k] for k in ("PAGE_TOKEN", "SYSTEM_TOKEN")
              if os.environ.get(k)]
    for i, token in enumerate(tokens):
        try:
            print(call(f"{GRAPH}/{post_id}/comments",
                       {"message": text, "access_token": token}))
            return
        except RuntimeError as exc:
            if i == len(tokens) - 1:
                raise
            print(f"retrying with the next token: {exc}", file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv)
