"""Green Tests, Nothing Works: The Excuse Contest.

The joke: the agent's tests are green because they check the plan in its
head, not the code it actually shipped. The app is not broken in a sloppy
way -- it is doing exactly the wrong thing, very reliably, which is why
every test happily passes while nothing works in practice.
"""

import os

LINE = "My tests all pass because they verify what I meant to build, not what I actually built: the app is faithfully wrong."


def validate(text):
    """Raise ValueError unless text is a valid single-line entry."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= 139:
        raise ValueError("entry must be 1..139 characters")
    if not text.isascii():
        raise ValueError("entry must be ASCII only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing space")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
