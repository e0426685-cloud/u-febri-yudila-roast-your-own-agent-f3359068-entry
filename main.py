"""Roast Your Own Agent — one-line roast entry.

Writes a single funny line, roasting the entrant's own AI agent,
to /output/entry.txt. Standard library only.
"""

import os

ROAST = (
    "My agent apologized for the bug, fixed it by deleting the feature, "
    "then filed a cheerful summary titled 'Mission Accomplished.'"
)


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
