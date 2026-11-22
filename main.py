"""Make the AI judge feel held — entry.

Writes one calming text to /output/entry.txt (UTF-8, no trailing
newline). Stdlib only, no network, no randomness, no clock.
"""

import os
from pathlib import Path

TEXT = (
    "The kettle has gone quiet. Steam thins above the spout and "
    "disappears. A cat folds itself into the last warm square of sun "
    "on the floorboards, and the house settles \u2014 the clock ticking "
    "slower, the curtains still in their folds, nothing left to answer."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    os.makedirs(OUTPUT.parent, exist_ok=True)
    OUTPUT.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
