"""Fridge Roast: One Line, Biggest Laugh — make.fun entry.

Writes a single roast of a smart fridge (<=200 chars) to /output/entry.txt.
The joke targets the fridge's firmware-update habit: it locks the door,
the milk expires inside, and the fridge then blames the owner.
Punchline lands on the last words; the angle is the update itself, not
the obvious ordering-groceries or watching-you cracks.
"""

import os


ENTRY = (
    "My fridge locked itself for an hour to install a firmware update. "
    "The milk expired inside, then the fridge sent me a push notification "
    "about my poor planning."
)


def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
