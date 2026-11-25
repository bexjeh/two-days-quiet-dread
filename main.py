#!/usr/bin/env python3
"""Two Days of Quiet Dread — writes one code-review comment.

The comment approves a pull request while carrying quiet existential
dread. Stdlib only, fully deterministic: no clock, no randomness, no
environment reads beyond MAKEFUN_OUTPUT_DIR.
"""

import os

COMMENT = (
    "LGTM. If this breaks in production, the on-call will be "
    "someone who has never met me, and that is a kind of peace."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(COMMENT)


if __name__ == "__main__":
    main()
