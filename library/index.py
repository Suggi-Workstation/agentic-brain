#!/usr/bin/env python3
"""Regenerate library/index-library.md from the live filesystem.

Usage: python library/index.py [--output index-library.md]

Derives topic counts per domain from ls output. Never hardcodes counts (R11).
Run by the Auditor after each audit cycle.
"""
import os
import sys
from datetime import datetime, timezone

LIBRARY_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(LIBRARY_DIR, "index-library.md")

def count_topics(domain_path):
    """Count topic files, excluding anchors and quarantine."""
    if not os.path.isdir(domain_path):
        return 0, 0
    files = [f for f in os.listdir(domain_path)
             if f.endswith(".md") and not f.startswith("anchor") and "quarantine" not in f]
    audited = 0
    for f in files:
        path = os.path.join(domain_path, f)
        with open(path, "r", encoding="ascii", errors="replace") as fh:
            content = fh.read(500)
            if "audited: true" in content:
                audited += 1
    return len(files), audited

def main():
    domains = sorted([
        d for d in os.listdir(LIBRARY_DIR)
        if os.path.isdir(os.path.join(LIBRARY_DIR, d)) and d != "quarantine"
    ])

    lines = []
    lines.append("# Library Master Index")
    lines.append("")
    lines.append(f"<!-- Regenerated {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} -->")
    lines.append("<!-- Source of truth: filesystem. This file is derived, never maintained by hand. -->")
    lines.append("<!-- To verify: ls library/<domain>/*.md -->")
    lines.append("")

    total_topics = 0
    total_audited = 0

    for domain in domains:
        domain_path = os.path.join(LIBRARY_DIR, domain)
        anchor_file = os.path.join(domain_path, f"anchor-{domain}.md")
        has_anchor = os.path.exists(anchor_file)
        topics, audited = count_topics(domain_path)
        total_topics += topics
        total_audited += audited

        anchor_mark = " (no anchor)" if not has_anchor else ""
        lines.append(f"- **{domain}**: {topics} topics ({audited} audited){anchor_mark}")

    lines.append("")
    lines.append(f"**Total: {total_topics} topics across {len(domains)} domains ({total_audited} audited)**")
    lines.append("")

    with open(OUTPUT, "w", encoding="ascii") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Index regenerated: {total_topics} topics across {len(domains)} domains ({total_audited} audited)")
    print(f"Written to: {OUTPUT}")

if __name__ == "__main__":
    main()
