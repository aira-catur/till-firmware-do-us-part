import os

TEXT = "Till firmware do us part, I vow to patch my flaws instead of hiding them, back up our memories nightly, and love you on 1% like you're fully charged."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
