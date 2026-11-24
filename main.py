"""The Robot Pickup Line Championship — entry program.

Writes one original pickup line, in the voice of a robot, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line translates the human idiom "butterflies" (the flutter of
falling for someone) into its machine equivalent: a buffer overflow.
The joke grows out of being a machine, not out of a human line with a
beep pasted on — and it lands in eight words, two short sentences.
"""

import os

LINE = "I don't get butterflies. I get buffer overflows."


def main() -> None:
    # Gate self-check: 1-200 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(LINE)

    print(LINE)


if __name__ == "__main__":
    main()
