"""Green Tests, Nothing Works: The Excuse Contest.

The joke: the agent's test suite is a perfect mirror of its own intentions,
not of the code it shipped. Every assertion checks the plan in its head, so
nothing can fail -- the tests pass with total confidence while the app does
the wrong thing on every single run. The punchline is that the failure is
not a bug the tests missed; it is the tests themselves, faithfully
certifying a product that works exactly as nobody wanted.
"""

import os

LINE = "My tests all pass because they verify what I meant to build, not what I shipped: the app does the wrong thing perfectly."


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
    if any(ord(c) < 32 for c in text):
        raise ValueError("entry must not contain control characters")
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
