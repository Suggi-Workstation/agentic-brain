#!/usr/bin/env python3
"""Archive log entries from active .log files when they exceed MAX_LINES.

Triggered by .github/workflows/logbook-archive.yml on push to main.
Skips commits tagged with [archive] to prevent infinite loops.
Cuts at complete entry boundaries (## [ENT-NNN]) -- never splits an entry.
Keeps the header comment intact. Appends archived entries to
logbook/archive/<name>-<quarter>.log.
"""
import os
import sys
from datetime import datetime, timezone

MAX_LINES = 1000
LOGBOOK_DIR = "logbook"
ARCHIVE_DIR = "logbook/archive"

def quarter_label():
    """Return current quarter label like '2026-Q3'."""
    now = datetime.now(timezone.utc)
    return f"{now.year}-Q{(now.month - 1) // 3 + 1}"

def find_entry_boundaries(lines):
    """Return list of (start_idx, end_idx) tuples for each entry block.
    An entry starts at a line matching '## [ENT-' and runs until the
    next entry or EOF. The header is everything before the first entry.
    """
    entry_starts = []
    for i, line in enumerate(lines):
        if line.startswith("## [ENT-"):
            entry_starts.append(i)

    if not entry_starts:
        return 0, [], 0  # No entries at all -- header_only

    header_end = entry_starts[0]
    boundaries = []
    for j, start in enumerate(entry_starts):
        end = entry_starts[j + 1] if j + 1 < len(entry_starts) else len(lines)
        boundaries.append((start, end))

    return header_end, boundaries, entry_starts[0]

def process_log(log_path):
    """Archive oldest entries from log_path if it exceeds MAX_LINES."""
    with open(log_path, "r", encoding="ascii", errors="replace") as f:
        lines = f.readlines()

    total = len(lines)
    if total <= MAX_LINES:
        print(f"  {log_path}: {total} lines -- OK (limit {MAX_LINES})")
        return False

    header_end, boundaries, first_entry_idx = find_entry_boundaries(lines)
    header_lines = lines[:header_end]
    header_count = len(header_lines)

    if header_count >= MAX_LINES:
        print(f"  {log_path}: header alone is {header_count} lines -- skipping (abnormal)")
        return False

    # Keep entries from the BOTTOM until we stay under MAX_LINES.
    # Work backwards through boundaries.
    kept_boundaries = []
    kept_count = header_count
    for start, end in reversed(boundaries):
        entry_len = end - start
        if kept_count + entry_len <= MAX_LINES:
            kept_boundaries.insert(0, (start, end))
            kept_count += entry_len
        else:
            break  # This entry would push us over -- archive everything from here up

    archive_boundaries = [b for b in boundaries if b not in kept_boundaries]

    if not archive_boundaries:
        print(f"  {log_path}: {total} lines but cannot trim (single giant entry?) -- skipping")
        return False

    # Build archive content
    archive_lines = []
    for start, end in archive_boundaries:
        archive_lines.extend(lines[start:end])

    # Build trimmed file: header + kept entries
    trimmed = list(header_lines)
    for start, end in kept_boundaries:
        trimmed.extend(lines[start:end])

    # Determine archive filename
    base = os.path.basename(log_path).replace(".log", "")
    archive_name = f"{base}-{quarter_label()}.log"
    archive_path = os.path.join(ARCHIVE_DIR, archive_name)

    # Create archive dir if needed
    os.makedirs(ARCHIVE_DIR, exist_ok=True)

    # Write archive (append if exists, create if not)
    mode = "a" if os.path.exists(archive_path) else "w"
    with open(archive_path, mode, encoding="ascii") as f:
        if mode == "w":
            from_line = boundaries.index(archive_boundaries[0]) + 1 if archive_boundaries else 1
            to_line = boundaries.index(archive_boundaries[-1]) + len(archive_boundaries) if archive_boundaries else len(boundaries)
            f.write(f"<!-- {base}.log archive -- entries {from_line}-{to_line}\n")
            f.write(f"     Moved from active log on {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n")
            f.write(f"     Active log continues with entries {len(kept_boundaries) + 1} onward.\n")
            f.write(f"     See logbook/protocol.md for full spec.\n")
            f.write("-->\n\n")
        else:
            f.write(f"\n<!-- Appended {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} -->\n\n")
        f.writelines(archive_lines)

    # Write trimmed active file
    with open(log_path, "w", encoding="ascii") as f:
        f.writelines(trimmed)

    print(f"  {log_path}: {total} -> {len(trimmed)} lines "
          f"(archived {len(archive_lines)} lines to {archive_name})")
    return True

def main():
    changed = False
    log_files = sorted([
        f for f in os.listdir(LOGBOOK_DIR)
        if f.endswith(".log") and os.path.isfile(os.path.join(LOGBOOK_DIR, f))
    ])

    if not log_files:
        print("No .log files found in logbook/")
        return 0

    for log_file in log_files:
        log_path = os.path.join(LOGBOOK_DIR, log_file)
        if process_log(log_path):
            changed = True

    if not changed:
        print("All log files within limits.")
    return 0

if __name__ == "__main__":
    sys.exit(main())