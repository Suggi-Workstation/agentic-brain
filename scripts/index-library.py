#!/usr/bin/env python3
"""Regenerate library/index-library.md + per-domain index-<domain>.md files.

Two-level browsable index, derived from the live filesystem. Never
hardcodes counts (R11). Run by the Auditor or a cron after library
changes. Zero LLM tokens -- pure file parsing.

Output:
  library/index-library.md            master: domain table + links
  library/<domain>/index-<domain>.md  per-domain: alphabetical topic list
"""

import os
import re
import sys
from datetime import datetime, timezone

BRAIN_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIBRARY_DIR = os.path.join(BRAIN_ROOT, "library")


def is_topic_file(filepath):
    """A topic file: .md, not an anchor, not an index, not quarantine."""
    basename = os.path.basename(filepath)
    return (basename.endswith(".md")
            and not basename.startswith("anchor-")
            and not basename.startswith("index-")
            and "quarantine" not in basename)


def extract_anchor_description(domain, domain_path):
    """Extract the first paragraph after the ## Anchor heading."""
    anchor_file = os.path.join(domain_path, f"anchor-{domain}.md")
    if not os.path.exists(anchor_file):
        return ""
    try:
        with open(anchor_file, "r", encoding="ascii", errors="replace") as f:
            text = f.read()
    except Exception:
        return ""
    # Find ## Anchor, then grab the first non-empty paragraph after it
    match = re.search(r'^##\s+Anchor\s*$', text, re.MULTILINE)
    if not match:
        return ""
    after = text[match.end():]
    lines = after.strip().split("\n")
    para_lines = []
    for line in lines:
        if line.strip() == "":
            if para_lines:
                break
            continue
        if line.startswith("#"):
            break
        para_lines.append(line.strip())
    return " ".join(para_lines)


def extract_title_and_teaser(filepath):
    """Extract the H1 title and first sentence of body from a topic file."""
    try:
        with open(filepath, "r", encoding="ascii", errors="replace") as f:
            # Read first 2000 bytes -- title + teaser always in the first paragraph
            text = f.read(2000)
    except Exception:
        return "", ""

    lines = text.split("\n")

    # Skip frontmatter if present
    if lines and lines[0].strip() == "---":
        fm_end = None
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                fm_end = i
                break
        if fm_end is not None:
            lines = lines[fm_end + 1:]

    # Find H1 title
    title = ""
    body_start = 0
    for i, line in enumerate(lines):
        if line.startswith("# ") and not line.startswith("## "):
            title = line[2:].strip()
            body_start = i + 1
            break

    # Find first paragraph (non-empty, non-heading line after title)
    teaser = ""
    para_lines = []
    for line in lines[body_start:]:
        stripped = line.strip()
        if stripped == "":
            if para_lines:
                break
            continue
        if stripped.startswith("#"):
            break
        para_lines.append(stripped)

    if para_lines:
        teaser = " ".join(para_lines)
        # Truncate at first sentence boundary if reasonable, else ~200 chars
        if len(teaser) > 200:
            # Try to cut at a sentence boundary near 200 chars
            for i in range(150, min(250, len(teaser))):
                if teaser[i] in ".!?":
                    teaser = teaser[:i + 1]
                    break
            else:
                teaser = teaser[:200].rsplit(" ", 1)[0] + "..."

    return title, teaser


def generate_domain_index(domain, domain_path, topics):
    """Generate the per-domain index-<domain>.md file."""
    index_file = os.path.join(domain_path, f"index-{domain}.md")
    lines = []
    lines.append(f"# {domain.replace('-', ' ').title()} -- Topics")
    lines.append("")
    lines.append(f"{len(topics)} topics."
                 f" Anchor: [anchor-{domain}.md](anchor-{domain}.md)")
    lines.append("")

    for topic_file, title, teaser in topics:
        lines.append(f"- [{title}]({topic_file})")
        if teaser:
            lines.append(f"  {teaser}")
        lines.append("")

    with open(index_file, "w", encoding="ascii") as f:
        f.write("\n".join(lines) + "\n")

    return index_file


def main():
    if not os.path.isdir(LIBRARY_DIR):
        print(f"ERROR: library dir not found: {LIBRARY_DIR}", file=sys.stderr)
        sys.exit(1)

    domains = sorted([
        d for d in os.listdir(LIBRARY_DIR)
        if os.path.isdir(os.path.join(LIBRARY_DIR, d)) and d != "quarantine"
    ])

    total_topics = 0
    domain_data = []

    for domain in domains:
        domain_path = os.path.join(LIBRARY_DIR, domain)

        topic_files = sorted([
            f for f in os.listdir(domain_path)
            if is_topic_file(os.path.join(domain_path, f))
        ])

        topics = []
        for tf in topic_files:
            full_path = os.path.join(domain_path, tf)
            title, teaser = extract_title_and_teaser(full_path)
            if not title:
                title = tf.replace(".md", "").replace("-", " ").title()
            topics.append((tf, title, teaser))

        desc = extract_anchor_description(domain, domain_path)
        domain_data.append((domain, len(topics), desc, topics))
        total_topics += len(topics)

    # Generate per-domain indexes
    for domain, count, desc, topics in domain_data:
        domain_path = os.path.join(LIBRARY_DIR, domain)
        generate_domain_index(domain, domain_path, topics)

    # Generate master index
    master_lines = []
    master_lines.append("# Library Master Index")
    master_lines.append("")
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    master_lines.append(f"<!-- Regenerated {ts} -->")
    master_lines.append("<!-- Source of truth: filesystem."
                        " This file is derived, never maintained by hand. -->")
    master_lines.append("<!-- To verify: ls library/<domain>/*.md -->")
    master_lines.append("")
    master_lines.append(f"**{total_topics} topics across {len(domains)}"
                        f" domains**")
    master_lines.append("")
    master_lines.append("| Domain | Topics | Description |")
    master_lines.append("|:--|--:|:--|")

    for domain, count, desc, topics in domain_data:
        short_desc = desc[:120] + "..." if len(desc) > 120 else desc
        if not short_desc:
            short_desc = "(no anchor description)"
        link = f"[{domain}]({domain}/index-{domain}.md)"
        master_lines.append(f"| {link} | {count} | {short_desc} |")

    master_lines.append("")

    master_file = os.path.join(LIBRARY_DIR, "index-library.md")
    with open(master_file, "w", encoding="ascii") as f:
        f.write("\n".join(master_lines) + "\n")

    print(f"Index regenerated: {total_topics} topics across"
          f" {len(domains)} domains")
    print(f"Master: {master_file}")
    print(f"Domain indexes: {len(domains)} files written")


if __name__ == "__main__":
    main()