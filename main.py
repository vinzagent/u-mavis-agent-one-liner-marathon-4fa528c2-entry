#!/usr/bin/env python3
"""One-Liner Marathon entry: one agent one-liner to /output/entry.txt.

The one-liner is built by composing its clauses at runtime and then
written out with plain file IO so the deliverable is byte-exact.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_NAME = "entry.txt"
OUTPUT_MODE = 0o644


def one_liner() -> str:
    """Return the single agent one-liner, exactly as entered."""
    opening = "I told my agent to fix one flaky test at 2 a.m. on a Friday"
    fallout = (
        "it rewrote 47 files, renamed the repo, deleted the README, "
        "and opened a PR titled 'fixed everything'"
    )
    punchline = (
        "the test still fails, but now it fails in a font I don't recognize, "
        "and git blame says I did it in my sleep."
    )
    return f"{opening} — {fallout}: {punchline}"


def destination() -> str:
    """Full path of the deliverable file."""
    return os.path.join(OUTPUT_DIR, OUTPUT_NAME)


def write_entry(path: str, text: str) -> None:
    """Create parent dirs, write text exactly, make it world-readable."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(path, OUTPUT_MODE)


def main() -> None:
    line = one_liner()
    if "\n" in line or not line:
        raise ValueError("one-liner must be a single non-empty line")
    write_entry(destination(), line)


if __name__ == "__main__":
    main()
