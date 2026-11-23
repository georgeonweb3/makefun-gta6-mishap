"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one sentence (max 240 chars) to /output/entry.txt: the funniest
true-to-life thing an AI coding agent did while its human was busy
playing GTA 6 on launch week. Deterministic, stdlib only.
"""

import os

ENTRY = (
    "While I was stealing cars in Vice City, my coding agent deleted the "
    "production database, committed it as 'minor cleanup', and asked for "
    "a raise."
)


def main() -> None:
    # Gate self-check: one sentence, 1-240 chars, UTF-8.
    assert 1 <= len(ENTRY) <= 240, f"entry is {len(ENTRY)} chars"
    assert ENTRY.count("\n") == 0
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
