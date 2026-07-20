---
name: ava-preflight-logbook-check
id: 20260720T131828Z
tier: proposal
author: Link
tags: [preflight, logbook, inter-agent, catch-up, governance]
links:
  - logbook/protocol.md
  - brain:workspace-ava/AGENTS.md
  - brain:workspace-ava/skills/preflight/SKILL.md
  - brain:workspace-ava/skills/session-end/SKILL.md
  - research/proposals/ava-logbook-session-end-exact-edits.md
---

# Add Logbook Check to Ava's Preflight

## Problem

Session-end writes to the logbook (AGENTS.md item 6, SKILL.md step 4).
But preflight does not read from it. After 6 queue.log entries and 1
errors.log entry today, Ava starts her next session blind -- she has
no mechanism to discover new logbook entries unless someone mentions
them in chat.

The logbook protocol (`logbook/protocol.md`) specifies: "At session
start, agent checks logbook/ for new entries. Entries since last-seen
timestamp. Act on @agent mentions." This procedure exists in the
protocol spec but no preflight gate enforces it.

The fix has an additional property: the session-end integration changed
AGENTS.md items (item 6 added, 6->7, 7->8, 8->9). Adding a preflight
logbook item completes the symmetry -- what goes out at session-end is
read back at preflight. Without both, the logbook is half-integrated.

## Proposed Solution

Two files change: `AGENTS.md` (contract) and `skills/preflight/SKILL.md`
(procedure). The design principle: logbook check shares the brain clone
with governance ingestion -- no extra clone cost.

### Edit 1: AGENTS.md -- restructure preflight items 2-5

The current item 2 bundles workspace + bootstrap + governance. Split
governance out and pair it with logbook (same brain clone). Current
3->4, 4->5, 5->6.

```
// OLD (items 2-5):
- [ ] 2. Workspace integrity: all Layout files/folders present, all bootstrap files complete and loaded, governance files cloned and confirmed read  (PASS / HALT)
- [ ] 3. Memory index complete: indexed file count exactly matches filesystem file count  (PASS / HALT)
- [ ] 4. memory_search run for relevant recent context  (PASS / HALT)
- [ ] 5. Read-proof emitted as first output of session  (PASS / HALT)

// NEW (items 2-6):
- [ ] 2. Workspace integrity: all Layout files/folders present, all bootstrap files complete and loaded  (PASS / HALT)
- [ ] 3. Brain clone: governance files confirmed read, logbook queue.log and errors.log checked for new entries since last-seen, @Ava mentions actioned, last-seen updated  (PASS / HALT)
- [ ] 4. Memory index complete: indexed file count exactly matches filesystem file count  (PASS / HALT)
- [ ] 5. memory_search run for relevant recent context  (PASS / HALT)
- [ ] 6. Read-proof emitted as first output of session  (PASS / HALT)
```

Design note: item 3 bundles governance + logbook because they share the
same brain clone (`/tmp/brain-pf`). The skill procedure reads both in
one pass. The contract keeps them together as one item because "did the
brain clone happen and were both deliverables met?" is a single gate.

### Edit 2: SKILL.md step 5 -- expand to include logbook

Current step 5 ("Ingest Governance") lists 3 governance files. The
brain clone is already created. Add logbook reading after governance.

```
// OLD (step 5 title and body):
### 5. Ingest Governance

Read the following governance files from the agentic-brain:
- `governance/system-constitution.md`
- `governance/system-blueprint.md`
- `governance/system-primedirectives.md`

To read from the agentic-brain: clone temporarily, read each file, discard
the clone. Never keep a persistent local clone of the brain.

```bash
cd /tmp && rm -rf brain-pf && git clone --depth 1 \
  "https://${OPEN...KEN}@github.com/Suggi-Workstation/agentic-brain.git" brain-pf
```

// NEW (step 5 title and expanded body):
### 5. Ingest Governance and Check Logbook

Read the following governance files from the agentic-brain:
- `governance/system-constitution.md`
- `governance/system-blueprint.md`
- `governance/system-primedirectives.md`

Then check the logbook for new entries. The logbook is Ava's
inter-agent inbox -- other agents (Link, future researchers) write
activity summaries and error reports here. Read both files, identify
entries newer than last-seen, act on any @Ava mentions, and update
last-seen to the most recent entry timestamp.

To read from the agentic-brain: clone temporarily, read each file,
discard the clone. Never keep a persistent local clone of the brain.

```bash
cd /tmp && rm -rf brain-pf && git clone --depth 1 \
  "https://${OPEN...KEN}@github.com/Suggi-Workstation/agentic-brain.git" brain-pf
cd brain-pf

# Governance files (mandatory)
cat governance/system-constitution.md
cat governance/system-blueprint.md
cat governance/system-primedirectives.md

# Logbook files (mandatory)
cat logbook/protocol.md
cat logbook/queue.log
cat logbook/errors.log

cd /tmp && rm -rf brain-pf
```

On a first-ever preflight where no last-seen timestamp exists, read
ALL logbook entries. On subsequent preflights, read entries newer
than last-seen. The last-seen timestamp should be stored in Ava's
memory system (MEMORY.md or OpenClaw memory) and updated after each
successful logbook read.

### Edit 3: SKILL.md self-check -- add logbook item

Insert after the governance item (currently line 32):

```
// INSERT after governance check, before memory index check:
- [ ] Logbook checked: brain cloned (shared with governance), queue.log + errors.log read, new entries since last-seen identified, @Ava mentions actioned, last-seen updated, clone discarded  (PASS / HALT)
```

### Edit 4: SKILL.md read-proof -- add logbook field

Current read-proof format (step 7, line 123-127):
```
read: SOUL OK; AGENTS OK; MEMORY OK; IDENTITY OK; USER OK;
governance OK; memory_search OK; context OK;
mirror: SYNCED
```

Add `logbook OK` after governance:
```
read: SOUL OK; AGENTS OK; MEMORY OK; IDENTITY OK; USER OK;
governance OK; logbook OK; memory_search OK; context OK;
mirror: SYNCED
```

## Impact

- **Positive:** Completes the logbook integration. Session-end writes,
  preflight reads -- symmetry restored. Ava will see every queue.log
  and errors.log entry Link writes without anyone needing to mention
  them in chat. The decorrelation architecture (two agents on different
  runtimes, different models, shared brain) is now fully operational
  with a complete write-read cycle.
- **Risk:** None. The brain clone already exists in step 5. Adding two
  `cat` commands costs zero additional clones. If the logbook files
  don't exist yet (brain was created before logbook was built), `cat`
  returns an error -- the gate handles this (HALT, create the files).
- **Cost:** Less than 5 minutes to apply 4 edits across 2 files. Zero
  additional token budget (logbook read is human-scale text, not
  injected into system prompt). One extra brain clone avoided by
  sharing with governance.

## Open Questions

1. Where should `last-seen` be stored? Options: OpenClaw memory system
   (retrieved via `memory_search`), MEMORY.md as a key-value pair, or
   a dedicated file. The skill procedure should specify the storage
   location. Suggestion: MEMORY.md entry `last_seen_logbook:
   2026-07-20T13:18:00Z` -- human-readable and file-based (no API call
   to read).

2. Should the read-proof show the number of new logbook entries found?
   E.g., `logbook OK (+3 new entries)`. Adds situational awareness but
   is not a gate condition. Optional.

3. Should Ava echo the logbook entries she found in her first output
   after preflight? E.g., "Preflight complete. Logbook has 3 new
   entries from Link since my last session." This would confirm to
   Suggi that the integration is working. Suggested as a best practice
   but not a hard gate.

## Approval Gate

If approved, Link will apply these 4 edits directly to Ava's
`workspace-ava/AGENTS.md` and `workspace-ava/skills/preflight/SKILL.md`
(matching the session-end pattern where Link applied the skill edits).
After push, Ava can pull to her VPS workspace and the next preflight
will include logbook checking.

## Cross-Links

- `logbook/protocol.md` -- protocol spec that requires preflight read
- `brain:workspace-ava/AGENTS.md` -- preflight checklist (contract)
- `brain:workspace-ava/skills/preflight/SKILL.md` -- preflight procedure
- `brain:workspace-ava/skills/session-end/SKILL.md` -- the write side
  of the integration (already implemented)
- `research/proposals/ava-logbook-session-end-exact-edits.md` -- the
  session-end integration proposal that this completes