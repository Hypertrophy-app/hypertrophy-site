#!/usr/bin/env python3
"""Fail the deploy if an internal link points at a file we do not publish."""

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"

errors: list[str] = []
checked = 0

for page in sorted(PUBLIC.rglob("*.html")):
    text = page.read_text(encoding="utf-8")
    for value in re.findall(r'(?:href|src)="([^"]+)"', text):
        parts = urlsplit(value)
        if parts.scheme or parts.netloc or not parts.path.startswith("/"):
            continue
        checked += 1
        target = unquote(parts.path).lstrip("/")
        if not target:
            target = "index.html"
        elif (PUBLIC / target).is_dir():
            target = target.rstrip("/") + "/index.html"
        if not (PUBLIC / target).is_file():
            rel = page.relative_to(PUBLIC)
            errors.append(f"{rel}: {value} -> missing public/{target}")

if errors:
    print("Broken internal links:")
    print("\n".join(f"  {error}" for error in errors))
    raise SystemExit(1)

print(f"Checked {checked} internal links across {len(list(PUBLIC.rglob('*.html')))} pages.")
