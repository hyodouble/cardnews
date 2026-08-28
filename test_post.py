"""Self-check for the parts of post.py that are easy to get wrong."""
import os
import sys

import post


def test_wait_ready_polls_until_finished():
    seen = []
    replies = iter([{"status_code": "IN_PROGRESS"}, {"status_code": "FINISHED"}])

    def fake_call(url, params, method="POST"):
        seen.append(url)
        return next(replies)

    post.call, post.time.sleep = fake_call, lambda _: None
    post.wait_ready(post.GRAPH, "123", "tok")
    assert seen == [post.GRAPH + "/123"] * 2, seen


def test_wait_ready_raises_on_error():
    post.call = lambda *a, **k: {"status_code": "ERROR"}
    try:
        post.wait_ready(post.GRAPH, "123", "tok")
    except RuntimeError:
        pass
    else:
        raise AssertionError("ERROR status must not be treated as publishable")


def test_wait_ready_reads_the_field_each_api_uses():
    """Threads 400s on status_code, so the field has to switch with the host."""
    asked = []

    def fake_call(url, params, method="POST"):
        asked.append(params["fields"])
        return {params["fields"]: "FINISHED"}

    post.call, post.time.sleep = fake_call, lambda _: None
    post.wait_ready(post.GRAPH, "1", "tok")
    post.wait_ready(post.THREADS, "1", "tok")
    assert asked == ["status_code", "status"], asked


def test_threads_caption_drops_the_korean_half():
    long_caption = ("A. " * 200) + "\n\n· · ·\n\n한국어 본문"
    out = post.fit_threads(long_caption)
    assert "한국어" not in out and len(out) <= post.THREADS_TEXT_LIMIT, len(out)


def test_windows_paths_become_urls():
    os.environ["BASE_URL"] = "https://hyodouble.github.io/cardnews/"
    base = os.environ["BASE_URL"].rstrip("/")
    url = f"{base}/{os.path.join('img', 'a.png').replace(os.sep, '/')}"
    assert url == "https://hyodouble.github.io/cardnews/img/a.png", url


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
    print("all passed")
