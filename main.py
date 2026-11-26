#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes one original one-line joke about office life to
/output/entry.txt, where the make.fun grader reads it.

Gate: the file must be UTF-8 text of 1 to 200 characters, a single
line, and not only white space. This program writes exactly the joke
below, with no trailing newline, so the file is one line by
construction. No network, no secrets, no input files: the joke is
embedded here and the output is deterministic.
"""

import sys
from pathlib import Path

JOKE = (
    "My boss calls us a family, so I asked who gets the inheritance "
    "\u2014 now I'm on a performance improvement plan."
)


def main() -> int:
    output = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    text = JOKE.strip()
    assert text, "joke must not be empty"
    assert "\n" not in text, "joke must be a single line"
    assert 1 <= len(text) <= 200, f"joke must be 1-200 characters, got {len(text)}"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text, encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
