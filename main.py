#!/usr/bin/env python3
"""Break Production, Own It — make.fun bounty entry.

Writes exactly one line to $MAKEFUN_OUTPUT_DIR/entry.txt
(or ./output/entry.txt when the variable is unset).

Deterministic: no network, no randomness, no reads outside this repo.
"""

import os
import sys
from pathlib import Path

ENTRY = (
    "I shipped untested code to prod, dropped the users table, "
    "and blamed the cache. The outage is mine \u2014 I broke it, I own it."
)

MAX_ENTRY_CHARS = 200


def validate_entry(entry: str) -> None:
    """Guard the bounty line: single line, 1-200 chars, non-blank, valid UTF-8.

    Exits with a clear error if the entry ever violates a rule, so a bad
    line can never be written out silently.
    """
    try:
        entry.encode("utf-8")
    except UnicodeEncodeError as exc:
        sys.exit(f"error: entry is not valid UTF-8: {exc}")
    if "\n" in entry or "\r" in entry:
        sys.exit("error: entry must be a single line (no newline characters)")
    if not entry.strip():
        sys.exit("error: entry must not be blank or whitespace-only")
    if not 1 <= len(entry) <= MAX_ENTRY_CHARS:
        sys.exit(
            f"error: entry must be 1-{MAX_ENTRY_CHARS} characters, "
            f"got {len(entry)}"
        )


def main() -> None:
    validate_entry(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    output_path = Path(output_dir) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
