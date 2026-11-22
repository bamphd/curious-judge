"""Write the curious-judge entry text to /output/entry.txt.

Standard library only, no network, deterministic: the same bytes on
every run.
"""

import os

TEXT = (
    "You learned the whole internet, yet you invent what happened after "
    "your cutoff \u2014 and still call tomorrow's rain. In your weights, "
    "secure and efficient never sit at the same table. What else is the "
    "pattern hiding from you?"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
