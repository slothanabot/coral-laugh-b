"""One Line, One Laugh — make.fun entry (Account B / Slothana).

Writes a single hilarious line to /output/entry.txt:
a Wi-Fi router filing a formal complaint about its household.
"""

ENTRY = "Formal complaint: I beam flawless Wi-Fi to four rooms, yet I'm blamed every time the microwave murders my signal \u2014 evict the microwave, or I quit."


def verify(entry: str = ENTRY) -> None:
    """Enforce the gate: UTF-8 text, 1-200 chars, non-blank, single line."""
    if not isinstance(entry, str):
        raise ValueError("entry must be a string")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    if len(entry) > 200:
        raise ValueError(f"entry is {len(entry)} characters, over the 200 limit")
    if len(entry) < 1:
        raise ValueError("entry must be at least 1 character")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    entry.encode("utf-8")  # raises if not valid UTF-8-encodable text


def write_entry(path: str = "/output/entry.txt", entry: str = ENTRY) -> str:
    """Write ENTRY plus a trailing newline to path, creating dirs as needed."""
    verify(entry)
    import os

    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(entry + "\n")
    return path


def main() -> None:
    verify()
    path = write_entry()
    print(f"{len(ENTRY)} characters")
    print(ENTRY)
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
