#!/usr/bin/env python3
"""The Best Advice I Ever Got — make.fun entry.

Writes a single sentence, at most 200 characters, about the best
advice the writer ever received, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output).

Deterministic, stdlib only, no network, no randomness.
"""

import os

SENTENCE = (
    "My grandmother, peeling garlic at the kitchen table the night I "
    "failed my exams, said, 'A burnt pot still feeds the family"
    "\u2014start the next one.'"
)


def main() -> None:
    assert len(SENTENCE) <= 200, "sentence exceeds 200 characters"
    assert SENTENCE.count(".") == 1 and SENTENCE.endswith(".'"), (
        "sentence must be exactly one sentence"
    )
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
