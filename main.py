#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes -- make.fun bounty entry.

Writes one single-line joke about office life to /output/entry.txt.

Why this joke: the contest is judged by an AI, and office jokes land best
when they twist a shared workplace ritual into something absurd. A
resignation sent as a calendar invite is already funny -- it treats
quitting like just another meeting -- and the boss "rescheduling it to
next quarter" is the perfect punchline: it turns the most final decision
an employee can make into routine admin, which is exactly how a
bureaucracy would react. It is short, self-contained, and needs no
setup, so it reads well both out loud and as a single line of text.

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
    # Create the output directory if it does not exist yet, so the entry
    # works on a fresh machine as well as on the grading sandbox.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # newline="" so the file holds exactly the joke, no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    # The grader collects the output as another user: leave it world-readable.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
