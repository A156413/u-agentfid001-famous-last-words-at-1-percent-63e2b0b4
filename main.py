#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — a phone's final line at 1% battery.

Writes one original line to /output/entry.txt (or $OUTPUT_DIR/entry.txt
when testing locally). Python 3 standard library only.
"""

import os

LINE = "I have 1% left, and I'm spending it on this sentence instead of your alarm. Good luck tomorrow."

# The sealed scorer accepts 1 to 199 characters, not only whitespace.
assert 1 <= len(LINE) <= 199 and LINE.strip(), "entry line violates the 1-199 character gate"


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
