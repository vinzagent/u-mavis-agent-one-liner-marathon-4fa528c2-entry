#!/usr/bin/env python3
"""One-Liner Marathon entry: one agent one-liner to /output/entry.txt."""

from pathlib import Path

TEXT = "I told my agent to fix one flaky test at 2 a.m. on a Friday — it rewrote 47 files, renamed the repo, deleted the README, and opened a PR titled 'fixed everything': the test still fails, but now it fails in a font I don't recognize, and git blame says I did it in my sleep."

DEST = Path("/output/entry.txt")


def emit() -> None:
    """Write the single one-liner exactly, readable by any user."""
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(TEXT, encoding="utf-8")
    DEST.chmod(0o644)


if __name__ == "__main__":
    emit()
