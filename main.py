#!/usr/bin/env python3
"""Fortune in a Pot: one kind, funny fortune for the houseplant on the windowsill.

Writes the fortune to /output/entry.txt by default (override with an
argv[1] path or $OUTPUT_PATH) and prints it to stdout.
Deterministic: the same single line on every run.
"""

import os
import sys

DEFAULT_PATH = "/output/entry.txt"

ENTRY = "This week someone will water you right on time, and you will forgive them for every dry Tuesday on this windowsill."

USAGE = "usage: main.py [-h | --help] [output-path]\nWrites the fortune to output-path, or $OUTPUT_PATH, or /output/entry.txt by default."


def resolve_output_path(argv):
    """Pick the output path: argv[1] first, then $OUTPUT_PATH, then the default."""
    if len(argv) > 1:
        if argv[1] in ("-h", "--help"):
            print(USAGE)
            sys.exit(0)
        return argv[1]
    return os.environ.get("OUTPUT_PATH") or DEFAULT_PATH


def main(argv=None):
    argv = list(sys.argv if argv is None else argv)
    path = resolve_output_path(argv)
    try:
        parent = os.path.dirname(path)
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError as exc:
        print(f"error: could not write fortune to {path}: {exc}", file=sys.stderr)
        sys.exit(1)
    print(ENTRY)


if __name__ == "__main__":
    main()
