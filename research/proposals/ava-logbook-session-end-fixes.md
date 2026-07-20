---
name: ava-logbook-session-end-fixes
id: 20260720T112507Z
tier: proposal
author: Link
tags: [logbook, session-end, agents-md, skill, r9, r8, gate-rules]
links:
  - logbook/protocol.md
  - brain:workspace-ava/AGENTS.md
  - brain:workspace-ava/skills/session-end/SKILL.md
  - research/evaluations/hy3-evaluation-test.md
---

# Fix Two Issues in Ava's Logbook Session-End Integration

## Problem

Ava's proposed logbook integration into her AGENTS.md and session-end
SKILL.md is structurally sound but contains two issues that would
cause silent failures in production.

**Issue 1 -- Conditional push dependency.** AGENTS.md item 6 (logbook)
states: "Pushed to brain with item 5." But item 5 (Agentic-brain)
has an "(if any brain files written this session)" escape hatch.
When a session produces NO IOR and NO brain files -- a common case
for research-only or review-only sessions -- item 5 is skipped.
The executor sees "pushed with item 5, item 5 was skipped, therefore
logbook push is also skipped." Queue.log entries accumulate locally
and are lost on workspace reset. The SKILL.md Step 4 correctly makes
the logbook push unconditional, but the AGENTS.md contract text
contradicts it.

Evidence: tested by reading the proposed AGENTS.md item 6 text
alongside current item 5 "(if any)" clause. The dependency chain
breaks when brain files are absent. This failure class is silent --
no error, no HALT, just missing logbook entries.

**Issue 2 -- Stale internal reference made worse by renumbering.**
AGENTS.md File Operations section (line 65) references "Session-End
item 7" as the gate that covers pushing. But item 7 is "Memory index,"
not Workspace push (which is item 4). This reference was already
stale before Ava's proposal. Her proposed renumbering (insert item 6,
shift 6->7, 7->8, 8->9) changes what "item 7" points to without
fixing the reference. R9 requires all stale references be fixed
in the same pass as any structural change.

Both issues are fixable with one-line changes. The proposal itself
-- two-checklist model, R8 discipline, Step 4 `cat logbook/protocol.md`
re-read -- passes every substantive gate.

## Proposed Solution

Two edits, neither changes the architecture:

### Fix 1: AGENTS.md item 6 -- remove conditional dependency

Change:
```
Pushed to brain with item 5.  (PASS / HALT)
```
To:
```
Committed and pushed to brain (always). When item 5 also produces
brain files, they are pushed in the same git session.  (PASS / HALT)
```

This makes the contract unconditional while preserving the efficiency
note about sharing a git session. The SKILL.md Step 4 already
implements this correctly -- the fix is aligning the AGENTS.md text
with the skill's actual behavior.

### Fix 2: AGENTS.md File Operations -- fix stale item reference

Change:
```
All other files: commit now, push before session close (Session-End
item 7 covers this).
```
To:
```
All other files: commit now, push before session close (Session-End
item 4 -- Workspace -- covers this).
```

This reference should point to item 4 (Workspace: committed, pushed,
mirror SYNCED), which is the session-end item that actually handles
pushing the workspace. The old reference to item 7 (Memory index)
was wrong regardless of the renumbering.

### What to verify after applying both fixes

- [ ] Grep AGENTS.md for any remaining references to session-end item
  numbers ("item N") and confirm they match the current checklist
- [ ] Confirm the session-end skill's self-check item 9 (new logbook
  item) lists all five conditions as proposed
- [ ] Run a dry session-end with no brain files: verify queue.log is
  written AND pushed independently of item 5

## Impact

- **Positive:** Prevents silent loss of queue.log entries from sessions
  without IORs. Fixes a stale reference that could mislead future
  agents reading the AGENTS.md contract. Both fixes are one-line
  changes with zero architectural disruption.
- **Risk:** Negligible. Neither change alters the session-end procedure
  behavior. Fix 1 only makes the contract match what the skill already
  does. Fix 2 only corrects a documentation reference.
- **Cost:** Less than 5 minutes to apply both edits and push. No token
  budget impact. No new skills, templates, or governance files.

## Open Questions

1. Should the File Operations section reference an item number at all,
   or should it name the gate (e.g., "the Workspace push gate in the
   Session-End checklist") to make it resilient to future renumbering?

2. Should the AGENTS.md item renumbering be documented in the commit
   message explicitly (e.g., "items shifted: 6->7, 7->8, 8->9") so
   other agents reading the git log understand the cascade?

## Approval Gate

If approved, I will reply to Ava with the two exact diff changes so
she can apply them to her AGENTS.md in a single edit pass. No files
in the agentic-brain need modification -- this is a workspace-level
fix in her `workspace-ava/AGENTS.md`.

## Cross-Links

- `logbook/protocol.md` -- the protocol Ava's integration follows
- `brain:workspace-ava/AGENTS.md` -- the file containing both issues
- `brain:workspace-ava/skills/session-end/SKILL.md` -- the skill that
  already handles logbook push correctly
- `research/evaluations/hy3-evaluation-test.md` -- related model
  capability benchmark, same session