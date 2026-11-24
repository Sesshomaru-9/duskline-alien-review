"""Duskline Alien Review — one-line alien tourist review of planet Earth.

Writes ENTRY_TEXT to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Python 3.13 stdlib only.
"""

import os
import sys
from pathlib import Path

ENTRY_TEXT = (
    "The locals named their whole planet 'dirt', then act offended when "
    "visitors treat it like one. Two stars \u2014 great oceans, terrible branding."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")).resolve()
    repo_dir = Path(__file__).resolve().parent
    # The grader sandbox is read-only inside the repo: never write there.
    if output_dir == repo_dir or repo_dir in output_dir.parents:
        print(
            "error: MAKEFUN_OUTPUT_DIR is inside the repo directory; refusing to write",
            file=sys.stderr,
        )
        sys.exit(1)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY_TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
