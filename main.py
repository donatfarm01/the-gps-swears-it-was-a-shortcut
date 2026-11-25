#!/usr/bin/env python3
"""Write the GPS's excuse to /output/entry.txt.

The entry is one fixed line, chosen in advance: the GPS defends the
wrong turn by blaming the map, with the lake as the witness it refuses
to listen to. The program writes it deterministically, with no network
and no input, so every run produces the same file. The output file is
left world-readable, since the grader collects it as another user.
"""

import os

ENTRY = "The map said turn here. The lake said otherwise. I do not take directions from water."

def main():
    os.makedirs("/output", exist_ok=True)
    path = os.path.join("/output", "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
