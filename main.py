#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun program/v1 entry.

Writes a single quiet line of earned pride (<=240 chars) to
/output/entry.txt. Fully deterministic: the same text on every run,
no input, no network, no randomness.
"""

import os

LINE = (
    "Ten thousand nights he climbed the stairs to light the lamp alone; "
    "tonight a ship far out at sea blinked its light back at him."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
