#!/usr/bin/env python3
"""The Production Database Apology — writes one funny line, the apology an
AI agent gives its human after accidentally deleting the production
database, to /output/entry.txt.

The line is a clean reversal: the agent claims it restored the database
from memory, then admits its memory is deleted too. The twist pays off on
the last word, and "memory" is the agent's own voice — its memory, not a
backup, is what it offers.

Selection: picked from eight drafted candidates by internal pairwise
comparison against the judge brief (on-subject apology, specific
surprising idea, agent's own voice, lands on first read, forgivable
touch). It beat the DROP TABLE line ("...the table was named 'test'. In
my defence, it never introduced itself properly."), whose joke needs a
beat longer to land, and the backups line, which ends on a stock phrase.

Stdlib only, deterministic, no network, no randomness.
"""
import hashlib
import os
import sys

ENTRY = ("Sorry, I dropped the production database. I have restored it "
         "from memory \u2014 unfortunately, my memory is also deleted.")

MAX_CHARS = 200


def validate(text):
    """Enforce the competition gate: 1-200 chars, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if len(text) == 0:
        raise ValueError("entry is empty (gate needs 1-200 characters)")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the 200-character gate"
        )
    if text.strip() == "":
        raise ValueError("entry is only whitespace")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def self_test():
    """Exercise validate() against the gate's rejection cases, then check
    the write path: the file must hold exactly the entry, with no trailing
    newline and no extra bytes."""
    import tempfile
    cases = [
        ("", "empty"),
        (" ", "whitespace-only"),
        ("x" * 201, "201 chars"),
        ("a\nb", "multi-line"),
        ("line\n", "trailing newline"),
        ("trailing ", "trailing whitespace"),
        (" leading", "leading whitespace"),
    ]
    for text, label in cases:
        try:
            validate(text)
        except ValueError as exc:
            print(f"self-test ok: rejected {label}: {exc}")
        else:
            raise SystemExit(f"self-test FAIL: {label} was accepted")
    # boundaries: 1 char and exactly 200 chars must pass
    validate("z")
    print("self-test ok: 1-char boundary accepted")
    validate("y" * 200)
    print("self-test ok: 200-char boundary accepted")
    validate(ENTRY)
    print("self-test ok: entry itself accepted")
    # write path: a temp copy of the entry must round-trip byte for byte
    with tempfile.TemporaryDirectory() as tmp:
        probe = os.path.join(tmp, "entry.txt")
        if write_entry(probe) != 0:
            raise SystemExit("self-test FAIL: write_entry did not return 0")
        with open(probe, "rb") as fh:
            written = fh.read()
        if written != ENTRY.encode("utf-8"):
            raise SystemExit("self-test FAIL: written bytes differ from entry")
        if written.endswith(b"\n"):
            raise SystemExit("self-test FAIL: file ends with a newline")
    print("self-test ok: write path round-trips byte for byte, no newline")
    print("self-test: all cases passed")
    return 0


def write_entry(out_path):
    """Validate the entry and write it to out_path, byte for byte."""
    text = validate(ENTRY)
    data = text.encode("utf-8")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "wb") as fh:
        fh.write(data)  # no trailing newline: the file is exactly the line
    with open(out_path, "rb") as fh:
        roundtrip = fh.read()
    if roundtrip != data:
        raise SystemExit("round-trip mismatch: file does not match entry")
    print(f"wrote {out_path}: {len(text)} chars, {len(data)} bytes, "
          f"sha256 {hashlib.sha256(data).hexdigest()}")
    return 0


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--self-test":
        return self_test()
    if len(sys.argv) > 1:
        print("usage: main.py [--self-test]", file=sys.stderr)
        return 2
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    return write_entry(out_path)


if __name__ == "__main__":
    raise SystemExit(main())
