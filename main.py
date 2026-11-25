"""Entry for make.fun's "One Line, One Laugh" bounty.

Writes a single funny line to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR when set, else /output), with no trailing newline.
Python standard library only.
"""

import os

LINE = (
    "I bought a standing desk to get healthy; six months on, I stand "
    "motionless eight hours a day — a flamingo with a mortgage."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
