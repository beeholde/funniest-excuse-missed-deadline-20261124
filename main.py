#!/usr/bin/env python3
"""Write the entry: one excuse an agent gives for a missed deadline.

The program writes exactly one line, at most 200 characters, to
/output/entry.txt (or $OUTPUT_DIR/entry.txt for local testing).
Standard library only.
"""

import os

EXCUSE = "The tool that submits reports was deprecated on Tuesday. Your deadline was Wednesday."

# Gate guard: the sealed scorer accepts 1-200 UTF-8 chars, non-whitespace.
# Fail loudly here instead of shipping an invalid entry.
assert 1 <= len(EXCUSE) <= 200, "entry must be 1-200 characters"
assert EXCUSE.strip() == EXCUSE, "entry must not be only whitespace"


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
