"""Funniest Time Machine Warning Label.

Writes a single warning label, 120 characters at most, to /output/entry.txt.

The joke: a straight-faced safety notice about the grandfather paradox,
whose punch lands in the last few words -- murder reframed as a ticketing
problem, because the victim is the only passenger who paid for the trip.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 120

LABEL = "WARNING: Do not kill your grandfather. He is the only passenger who paid for this trip."


def validate(text: str) -> str:
    """Return the label if it passes the gate, else raise."""
    label = text.strip()
    if not label:
        raise ValueError("label must not be only whitespace")
    if len(label) > MAX_CHARS:
        raise ValueError(f"label is {len(label)} chars, limit is {MAX_CHARS}")
    if "\n" in label:
        raise ValueError("label must be a single line")
    return label


def main() -> None:
    label = validate(LABEL)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(label)


if __name__ == "__main__":
    main()
