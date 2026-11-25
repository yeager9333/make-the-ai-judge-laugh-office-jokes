"""One-line office joke entry for make.fun.

Writes the joke to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only, no network.
"""
import os

JOKE = "My calendar is so full I had to book a meeting with myself just to eat lunch \u2014 and I still showed up late."

# The gate requires 1 to 199 characters of UTF-8 text, not only whitespace.
assert 1 <= len(JOKE) <= 199 and JOKE.strip(), "joke must be 1-199 characters"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
