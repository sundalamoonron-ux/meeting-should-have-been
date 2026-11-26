#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email.

Writes one line, under 200 characters, that makes a meeting that should
have been an email funny, to /output/entry.txt.

The joke: the meeting adds nothing the email thread did not already do —
it just performs the same reply-all chaos live, with slides.
"""

import os

LINE = "The meeting was just the email thread performed live: twelve people replying all, out loud, with slides."

# Gate: one line, 1-200 chars, not only whitespace.
OUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate self-check: 1-200 chars, one line, not only whitespace.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert "\n" not in LINE and LINE.strip(), "line must be one non-blank line"
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
