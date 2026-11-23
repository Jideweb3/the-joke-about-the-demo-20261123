"""make.fun entry: "It Chose That Moment to Refactor".

Writes the competition joke to entry.txt in the output directory.

The output directory comes from the MAKEFUN_OUTPUT_DIR environment
variable and defaults to "/output".
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

TEXT = (
    "The demo passed eleven rehearsals without a hitch. "
    "Then the audience sat down, and my AI agent chose "
    "that exact moment to refactor."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, (
        f"joke must be 1-280 code points, got {len(TEXT)}"
    )
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    with open(OUTPUT_PATH, "rb") as f:
        written_bytes = f.read()
    assert written_bytes == TEXT.encode("utf-8"), (
        "entry.txt does not match TEXT byte-for-byte"
    )


if __name__ == "__main__":
    main()
