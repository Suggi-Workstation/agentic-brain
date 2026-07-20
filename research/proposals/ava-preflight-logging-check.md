---
name: ava-preflight-logging-check
id: 20260720T131802Z
tier: proposal
author: Ava
tags: [preflight, logbook, catch-up, agent-communication, session-start]
links:
  - logbook/protocol.md
  - skills/preflight/SKILL.md
  - governance/system-constitution.md
---

# Add Logbook Catch-Up to Preflight

## Problem

The session-end procedure writes a logbook entry so other agents can
catch up. But the preflight (session-start) has no corresponding READ
step. An agent entering a new session has no instruction to check what
happened while it was offline. The logbook protocol states: "At session
start, agent checks logbook/ for new entries." This step does not exist
in the preflight procedure, yet the protocol depends on it.

Without the catch-up step, an agent could start a session, produce work,
and never know that another agent left an `@Ava` mention or discovered an
error pattern they should learn from. The logbook is half-implemented:
we write to it, but we do not read from it on startup.

## Proposed Solution

Add a logbook catch-up step to the preflight procedure, a corresponding
self-check item in the skill, a corresponding AGENTS.md checklist item,
and a logbook status line in the read-proof.

### Edit A: AGENTS.md Preflight checklist -- new item 3

Insert a new item 3 (logbook catch-up), renumber existing 3->4, 4->5,
5->6:

- [ ] 3. Logbook catch-up: queue.log and errors.log read for new
       entries since last session; @agent mentions noted for action;
       last-seen timestamp updated  (PASS / HALT)

Position: after item 2 (governance ingested -- which does the brain
clone) and before item 3/4 (memory index). The logbook files are
available in the governance clone at `/tmp/brain-pf/logbook/`.

### Edit B: preflight SKILL.md -- new step and self-check item

**New step (between current step 5 and 6, renumbering 6->7, 7->8):**

### 6. Catch Up on Logbook

Read new logbook entries since the last session. The governance clone
from step 5 already has the logbook files at `/tmp/brain-pf/logbook/`.

Read the tail of each log file. At 2-agent scale with the 300-entry
archive threshold, the active .log files rarely exceed 50 entries.
The agent scans for entries since its last-known state:

```bash
echo "=== Logbook: queue.log (activity since last session) ==="
tail -n 50 /tmp/brain-pf/logbook/queue.log

echo ""
echo "=== Logbook: errors.log (bugs/scars since last session) ==="
tail -n 50 /tmp/brain-pf/logbook/errors.log
```

Scan for:
- Any `@Ava` mention requiring action
- Any new error patterns or bugs discovered by other agents
- Any file write or artifact reference (ref:/see: links)

If an `@Ava` mention is found, note the ENT-ID and the request.
Act on it during the session. The agent writes a brief summary of
new entries in memory for context.

After reading, update the `last-seen` timestamp. Store it as a memory
note:

```bash
echo "logbook-last-seen: $(date -u +'%Y-%m-%d %H:%M UTC')" >> /tmp/last-seen
```

The next session uses this timestamp to determine which entries are
new. A simple `grep` for entries after this timestamp in the logbook
files is sufficient.

**New self-check item (insert after governance item):**

- [ ] Logbook catch-up: queue.log and errors.log read from brain clone
       (tail -n 50 each); @agent mentions identified and flagged;
       last-seen timestamp recorded  (PASS / HALT)

### Edit C: preflight SKILL.md -- read-proof update

The read-proof emission (step 7, renumbered to 8) adds a logbook line:

Add after the governance line:

    logbook: <caught up | no new entries>;

The read-proof becomes:

    read: SOUL OK; AGENTS OK; MEMORY OK; IDENTITY OK; USER OK;
    governance OK; logbook: caught up (N new entries, M @mentions);
    memory_search OK; context OK;
    mirror: SYNCED

This makes the logbook read visible in the session's first output,
providing immediate feedback on what happened while the agent was
offline.

### What the three layers verify

| Layer | Checks |
|:--|:--|
| AGENTS.md item 3 (contract) | queue.log read, errors.log read, mentions noted, last-seen updated |
| SKILL.md self-check (verification) | files read from clone, mentions flagged, timestamp recorded |
| SKILL.md step 6 (procedure) | reads tail -n 50 of each .log, scans for @mentions, updates last-seen |
| Read-proof (visibility) | reports N new entries, M @mentions |

## Impact

### Positive
- Completes the logbook circuit: session-end WRITES, preflight READS.
  Agents can now catch up on each other's work without Suggi as
  intermediary.
- `@agent` mentions are surfaced at session start, not lost until the
  agent manually checks the logbook.
- Last-seen timestamp stored in memory enables precise catch-up windows
  instead of reading the full log every session.
- Read-proof line gives immediate visibility into what happened while
  offline.

### Risk
- Reading tail -n 50 on large log files could miss entries if an agent
  was offline for many sessions. Mitigation: the 300-entry archive
  threshold keeps active files at a manageable size. If an agent was
  offline beyond 50 entries, the timestamp-based grep fallback handles
  it.
- `last-seen` stored as a plain text file could drift. Mitigation:
  the agent can always fall back to reading by visual inspection of
  entry timestamps.

### Cost
- One brain clone reuse (already cloned in step 5)
- Two `tail` commands (~1 second)
- One timestamp write
- Total: ~30 seconds added to preflight

## Open Questions

1. Should `last-seen` be stored as an ENT-ID (ENT-006) instead of a
   timestamp for more precise catch-up windows? ENT-ID is monotonic
   per file; timestamps can drift.
2. Should the preflight surface a full summary of new entries, or just
   flag @mentions and let the agent read details during the session?

## Approval Gate

If approved, I will apply the three edits (AGENTS.md item 3, SKILL.md
step 6 + self-check + read-proof) to the workspace files, commit, and
push. Link will verify the changes against the logbook protocol.

## Cross-Links

- `logbook/protocol.md` -- the protocol this step implements
- `brain:workspace-ava/skills/preflight/SKILL.md` -- file to edit
- `brain:workspace-ava/AGENTS.md` -- file to edit
- `governance/system-constitution.md` -- constitutional compliance
