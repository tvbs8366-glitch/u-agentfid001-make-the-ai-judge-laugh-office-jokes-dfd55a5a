#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes -- make.fun bounty entry.

Writes one single-line joke about office life to /output/entry.txt.

The joke is fixed text, so the program is fully deterministic: two runs
produce byte-identical output. It makes no network calls, reads no
environment, needs no input and uses only the Python standard library.
"""

import os

JOKE = (
    "I submitted my resignation as a calendar invite, "
    "and my boss rescheduled it to next quarter."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # newline="" so the file holds exactly the joke, no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    # The grader collects the output as another user: leave it world-readable.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
