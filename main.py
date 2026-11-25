#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary.

The word: queue.

Five letters, one of them pronounced. The other four are silent freeloaders
standing in line behind it, doing nothing, for centuries. Delete the word
and four letters finally lose their jobs — the queue moves at last.
"""

import os
from pathlib import Path

WORD = "queue"


def main() -> None:
    # Graders run with MAKEFUN_OUTPUT_DIR set; fall back to /output so a
    # bare local run still works instead of crashing on a missing variable.
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
