#!/usr/bin/env python3
"""Re-validate title/tag lengths in the generated markdown files."""
from __future__ import annotations
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXPECTED = {
    "01-christmas-push.md": 19,
    "02-catalog.md": 57,
    "04-printables.md": 6,
    "05-backlog.md": 20,
    "06-valentines.md": 8,
}

def parse(path: Path):
    text = path.read_text()
    chunks = re.split(r"^# ", text, flags=re.M)[1:]
    skip = ("Christmas push", "Catalog listings", "Backlog listings", "Printable listings", "Pricing memo", "Contents", "Valentine's Day")
    out = []
    for ch in chunks:
        if ch.startswith(skip):
            continue
        heading = ch.splitlines()[0]
        title_m = re.search(r"## Title\n\n(.+)\n\n\((\d+) characters; Etsy limit 140\)", ch)
        tags_m = re.search(r"## Tags \(13, each 20 characters or fewer\)\n\n(.+?)\n\n## Description", ch, re.S)
        if not title_m or not tags_m:
            raise SystemExit(f"unparseable listing in {path.name}: {heading}")
        tags = [t for t in tags_m.group(1).splitlines() if t.strip()]
        out.append((heading, title_m.group(1), int(title_m.group(2)), tags))
    return out

def main() -> int:
    errors = []
    all_titles = []
    for name, expected in EXPECTED.items():
        items = parse(HERE / name)
        if len(items) != expected:
            errors.append(f"{name}: expected {expected} listings, got {len(items)}")
        for heading, title, claimed, tags in items:
            all_titles.append(title)
            if claimed != len(title):
                errors.append(f"{name} / {heading}: claimed {claimed}, actual {len(title)}")
            if len(title) > 140:
                errors.append(f"{name} / {heading}: title {len(title)} > 140")
            if len(tags) != 13:
                errors.append(f"{name} / {heading}: {len(tags)} tags")
            if len(set(t.lower() for t in tags)) != len(tags):
                errors.append(f"{name} / {heading}: duplicate tags")
            for t in tags:
                if len(t) > 20 or t != t.strip() or "," in t or not t:
                    errors.append(f"{name} / {heading}: bad tag {t!r} ({len(t)})")
    if errors:
        print("VALIDATION FAILED:")
        for e in errors:
            print(" -", e)
        return 1
    print(
        "OK markdown:",
        ", ".join(f"{n}={c}" for n, c in EXPECTED.items()),
        f"titles {min(map(len, all_titles))}-{max(map(len, all_titles))} chars",
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
