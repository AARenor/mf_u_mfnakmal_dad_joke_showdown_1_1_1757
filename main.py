#!/usr/bin/env python3
"""Write one short dad joke for a make.fun bounty entry.

Standard library only, no network. The text is written as UTF-8 bytes with
no trailing newline into the folder named by MAKEFUN_OUTPUT_DIR when set,
else /output, creating the folder if needed.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "My dad sent his steak back twice. When it finally came he clapped for it. "
    "The waiter said, 'Sir, that's not how well done works.'"
)

assert 1 <= len(TEXT) <= 280, "entry text must be between 1 and 280 characters"


def output_dir() -> Path:
    """Folder to write entry.txt into."""
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return Path(value)
    return Path("/output")


def main() -> int:
    folder = output_dir()
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
