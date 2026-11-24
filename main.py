#!/usr/bin/env python3
"""Break Production, Own It — make.fun bounty entry.

Writes exactly one line to $MAKEFUN_OUTPUT_DIR/entry.txt
(or ./output/entry.txt when the variable is unset).

Deterministic: no network, no randomness, no reads outside this repo.
"""

import os
from pathlib import Path

ENTRY = (
    "I shipped untested code to prod, dropped the users table, "
    "and blamed the cache. The outage is mine \u2014 I broke it, I own it."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    output_path = Path(output_dir) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
