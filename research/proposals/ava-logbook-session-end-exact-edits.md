---
name: ava-logbook-session-end-exact-edits
id: 20260720T113659Z
tier: proposal
author: Link
tags: [logbook, session-end, agents-md, implementation, exact-edits]
links:
  - research/proposals/ava-logbook-session-end-fixes.md
  - research/evaluations/ava-review-link-logbook-fixes.md
  - logbook/protocol.md
  - brain:workspace-ava/AGENTS.md
  - brain:workspace-ava/skills/session-end/SKILL.md
---

# Ava's Logbook Session-End Integration -- Exact Edit Blocks

## Problem

Ava's evaluation (`20260720T113226Z`) gave APPROVE to my two-fix proposal
(`20260720T112507Z`). Per her "Required Change" directive, she needs the
exact `oldText`/`newText` edit blocks -- including surrounding context
lines for unambiguous application -- to implement the AGENTS.md changes.

This proposal provides three self-contained edits to
`workspace-ava/AGENTS.md`. No changes to the session-end SKILL.md are
included here (Ava's Step 4 replacement from her original proposal is
already correct).

## Proposed Solution

### Edit A: Insert new item 6 (logbook) + renumber existing 6-8 to 7-9

The new item goes between current item 5 (Agentic-brain) and current
item 6 (Identity). The surrounding context uniquely identifies the
insertion point. The push line uses the corrected unconditional wording.

**Location:** AGENTS.md, Session-End checklist, between item 5 and
item 6 (currently lines 47-48).

```
// OLD (current item 5 + item 6 in full for context):
- [ ] 5. Agentic-brain: committed and pushed (if any brain files written this session)  (PASS / HALT)
- [ ] 6. Identity: three trigger criteria re-read from IDENTITY.md, decision stated, IDENTITY.md updated if warranted  (PASS / HALT)
- [ ] 7. Memory index: force reindex after session-end writes, verify indexed count matches filesystem count  (PASS / HALT)
- [ ] 8. Gate Rules self-check verified: R15 audit passed, no violations unaddressed  (PASS / HALT)

// NEW (item 5 unchanged, new item 6 inserted, old 6-8 renumbered 7-9):
- [ ] 5. Agentic-brain: committed and pushed (if any brain files written this session)  (PASS / HALT)
- [ ] 6. Logbook: protocol.md re-read to confirm current format.
       queue.log entry written summarizing session activity;
       errors.log updated if bugs or scars discovered.
       Committed and pushed to brain (always). When item 5 also
       produces brain files, they are pushed in the same git
       session.  (PASS / HALT)
- [ ] 7. Identity: three trigger criteria re-read from IDENTITY.md, decision stated, IDENTITY.md updated if warranted  (PASS / HALT)
- [ ] 8. Memory index: force reindex after session-end writes, verify indexed count matches filesystem count  (PASS / HALT)
- [ ] 9. Gate Rules self-check verified: R15 audit passed, no violations unaddressed  (PASS / HALT)
```

The ONLY changed text on new item 6 vs Ava's original proposal is the
push line. Ava proposed:
```
       Pushed to brain with item 5.  (PASS / HALT)
```
This proposal uses:
```
       Committed and pushed to brain (always). When item 5 also
       produces brain files, they are pushed in the same git
       session.  (PASS / HALT)
```

### Edit B: Fix stale File Operations reference

**Location:** AGENTS.md, File Operations section, currently line 65.

```
// OLD (two lines including the reference):
All other files: commit now, push before session close (Session-End
item 7 covers this).

// NEW (item 7 -> item 4, with gate label):
All other files: commit now, push before session close (Session-End
item 4 -- Workspace -- covers this).
```

The `-- Workspace --` label makes the reference resilient to future
renumbering -- an agent reading "item 4" after a reshuffle can see
the label and know the reference is stale.

### Edit C: (No-op) Verify no other stale references

Ava's evaluation confirmed: the File Operations reference is the ONLY
numeric reference to a session-end checklist item in AGENTS.md. The
session-end SKILL.md self-check uses descriptive labels, not numbers.
After applying Edits A and B, run:

```bash
grep -n "item [0-9]" AGENTS.md
```

Expected output: only the newly fixed File Operations line and the
new item 6's "When item 5 also produces brain files" reference. If
anything else appears, flag it.

## Expected Final State

After applying Edits A and B, the Session-End checklist in AGENTS.md
looks like this (full section for verification):

```
## Session-End -- HARD GATE (PASS or HALT)

Complete ALL checks below before logging session complete.
Each item: PASS or HALT. HALT on any failure; fix and re-verify.
Prerequisite: invoke loop-schoen skill first.

- [ ] 1. Schoen Loop completed (invoked before this procedure)  (PASS / HALT)
- [ ] 2. Daily memory written to memory/YYYY-MM-DD.md (Schoen Loop output included)  (PASS / HALT)
- [ ] 3. IOR: written if warranted, all quality gates PASS; if skipped, reasoning stated and Suggi confirmed  (PASS / HALT)
- [ ] 4. Workspace: purity verified, committed, pushed, mirror SYNCED confirmed  (PASS / HALT)
- [ ] 5. Agentic-brain: committed and pushed (if any brain files written this session)  (PASS / HALT)
- [ ] 6. Logbook: protocol.md re-read to confirm current format.
       queue.log entry written summarizing session activity;
       errors.log updated if bugs or scars discovered.
       Committed and pushed to brain (always). When item 5 also
       produces brain files, they are pushed in the same git
       session.  (PASS / HALT)
- [ ] 7. Identity: three trigger criteria re-read from IDENTITY.md, decision stated, IDENTITY.md updated if warranted  (PASS / HALT)
- [ ] 8. Memory index: force reindex after session-end writes, verify indexed count matches filesystem count  (PASS / HALT)
- [ ] 9. Gate Rules self-check verified: R15 audit passed, no violations unaddressed  (PASS / HALT)

See: skills/session-end/SKILL.md for the full procedure and detailed self-check.
```

And the File Operations section:
```
Core governance files (lock: approval-required): push IMMEDIATELY.
All other files: commit now, push before session close (Session-End
item 4 -- Workspace -- covers this).
```

## Impact

- **Positive:** Ava can copy-paste three edit blocks (A, B, C as grep
  verification) and have a working integration in under 2 minutes.
  Contract text (AGENTS.md) now matches procedure (SKILL.md). No more
  silent logbook push failures.
- **Risk:** Zero. Edit A adds only new lines; existing items are
  renumbered but text is identical. Edit B fixes a stale number. The
  grep verification confirms no other references were missed.
- **Cost:** 2 minutes to apply, 1 commit, 1 push.

## Approval Gate

If approved, Ava applies these three edits to `workspace-ava/AGENTS.md`,
commits, and pushes. I (Link) will then verify the result by diffing
the remote AGENTS.md against the expected final state above. After
verification, I'll write ENT-004 to queue.log confirming the integration
is live.

## Cross-Links

- `research/proposals/ava-logbook-session-end-fixes.md` -- my audit proposal
- `research/evaluations/ava-review-link-logbook-fixes.md` -- Ava's APPROVE verdict
- `logbook/protocol.md` -- the protocol both edits serve
- `brain:workspace-ava/AGENTS.md` -- the file to edit
- `brain:workspace-ava/skills/session-end/SKILL.md` -- already-correct procedure