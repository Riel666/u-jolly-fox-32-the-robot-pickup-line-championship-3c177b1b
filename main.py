"""One pickup line, a single line of at most 200 characters, in the voice of a robot trying to charm someone.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "Are you a firmware update? Because every time you walk by, my heart reboots and I forget what I was programmed to say."


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
