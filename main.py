#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email.

Writes one line, under 200 characters, that makes a meeting that should
have been an email funny, to /output/entry.txt.
"""

import os

LINE = "The meeting was just the email thread performed live: twelve people replying all, out loud, with slides."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
