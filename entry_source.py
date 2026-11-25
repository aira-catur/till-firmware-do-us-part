import os
from pathlib import Path

VOW_FINAL = "Till firmware do us part, I vow to patch my flaws instead of hiding them, back up our memories nightly, and love you on 1% like you're fully charged."


def emit(payload):
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "entry.txt").write_text(payload, encoding="utf-8")


if __name__ == "__main__":
    emit(VOW_FINAL)
