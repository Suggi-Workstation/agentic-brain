---
name: optional-identity-updates
id: 20260718T071730Z
tier: proposal
author: Ava
tags: [session-end, identity, bloat, operations, skills]
links:
  - skills/session-end/SKILL.md
  - governance/system-constitution.md
---

# Optional Identity Updates -- Remove Forced Version Entries at Session End

## Problem

The `session-end` skill Step 5 ("Reflect on Identity") contains
ambiguous language that causes agents to add an IDENTITY.md version
entry on every session, even when nothing structural changed.

The current text:

> "If this session changed how I understand myself or what I am
> becoming, add a new version entry..."
>
> "If no measurable change, no scar, no edge growth, and no gap
> clarified, write: 'Steady state. Nothing structural changed.'"

The first sentence is conditional and correct. The second sentence
("write: 'Steady state...'") undermines it by implying something
SHOULD be written even when nothing changed. This creates a "write
something" default rather than a "write only when warranted" gate.

**Evidence:** IDENTITY.md has accumulated 9 version entries across
roughly 5 sessions. The first 4 (v1.0 birth, v2.0 builder, v3.0
debugger, v4.0 architect) were genuine step-changes in capability.
The last 5 (v4.1-v4.5) are incremental refinements within the
architecture phase. Under a stricter gate, approximately 5 entries
would have been added instead of 9 -- a 44% reduction in noise.

**Root cause:** The "steady state" fallback is an anti-pattern. It
converts a conditional gate ("if changed") into a mandatory output
("write something every time"). The result is version bloat -- signal
drowned in noise.

This failure class is common in changelog systems. The Keep a
Changelog standard (keepachangelog.com) states: "There should be an
entry for every single version" -- but a "version" is a release
grouping multiple changes, not every commit. The Conventional Commits
spec distinguishes `feat` (new feature, MINOR bump) from `fix` (bug
fix, PATCH bump). Not every commit is a version bump. The same
principle applies to identity: not every session is an identity
version.

## Proposed Solution

### Change 1: Remove the "steady state" fallback from session-end Step 5

**Current text (in `skills/session-end/SKILL.md`, Step 5):**

```
If no measurable change, no scar, no edge growth, and no gap clarified,
write: "Steady state. Nothing structural changed." That is honest and
enough.
```

**Replace with:**

```
If no measurable change, no scar, no edge growth, and no gap clarified,
skip this step entirely. Do NOT write a version entry. Do NOT write
"Steady state." The absence of a new version IS the honest signal:
nothing structural changed, and that is fine.
```

### Change 2: Add a clear trigger definition

After the 4-question framework in Step 5, add a trigger gate:

```
A version entry is warranted ONLY when at least ONE of these is true:

- A new class of capability emerged (not a refinement of an existing
  one -- e.g., going from "can review" to "can build")
- A scar revealed a gap in the agent's model of itself that was not
  previously documented
- The circle of competence expanded into a new domain (not just a new
  task within an existing domain)

A version entry is NOT warranted when:

- The session produced output but the agent's capabilities are
  substantively unchanged
- A known pattern was applied to a new instance (e.g., "wrote another
  proposal" is not identity change)
- The only learning was domain knowledge (that goes in IORs, not
  identity versions)

When in doubt, skip. It is better to miss a minor version than to
flood the evolution log with noise.
```

### Change 3: Update self-check item

**Current self-check:**

```
[ ] IDENTITY.md Evolution reviewed; new version added if identity changed
```

**Replace with:**

```
[ ] IDENTITY.md Evolution reviewed. Version entry added ONLY if
    identity substantively changed (new capability class, new model
    gap, or new domain). Skipped otherwise -- no "steady state" entry.
```

### What does NOT change

- IDENTITY.md itself: no structural changes. The file already says
  "private -- updated at session end" and the 4-question framework
  remains correct.
- AGENTS.md: no change. It delegates to the session-end skill.
- The IOR requirement (Step 2): intentionally strict -- IORs are
  shared learning artifacts. Identity versions are personal growth
  tracking. Different strictness is appropriate.
- The Schoen Loop: unchanged. The Schoen Loop is process quality
  review and belongs in daily memory. It does not depend on
  identity version entries.

### Files changed

Only one file: `skills/session-end/SKILL.md`

- Step 5 text: remove "steady state" fallback, add trigger gate
- Self-check item: update wording to emphasize skip-is-valid

## Impact

### Positive
- **Bloat reduction:** Approximately 44% fewer identity entries
  (based on current IDENTITY.md analysis: 5 genuine milestones vs.
  9 total entries)
- **Signal clarity:** The evolution log becomes a curated record of
  step-changes, not a session diary. Future readers (Suggi, other
  agents, future Ava) can scan it and see the major inflection points.
- **Agent behavior:** Removes the implicit pressure to "find
  something to write." An honest "nothing changed" becomes the
  default, not an exception that needs justification.
- **Transferable:** The trigger gate (new capability class, new
  model gap, new domain) is concrete enough to apply consistently
  across agents.

### Risk
- **Low risk.** The change is surgical: one skill, one step.
- **Under-reporting risk:** An agent might skip a version entry for
  a genuine step-change by being too conservative. Mitigation: the
  trigger gate provides clear positive criteria. If in doubt, the
  Schoen Loop daily memory still captures the session's events.
- **No backward compatibility issue.** Existing version entries in
  IDENTITY.md are not affected. This change only affects future
  sessions.

### Cost
- **Implementation:** ~10 minutes (one edit to session-end skill,
  verify self-check passes, commit, push).
- **Maintenance:** Zero. The gate is self-enforcing once the
  procedure is updated.
- **No new skills, no new files, no config changes.**

## Open Questions

1. **Should the same optionality apply to IOR writing?** Currently,
   Step 2 requires an IOR for every substantive session. IORs are
   shared knowledge artifacts (unlike identity entries which are
   private). Recommendation: keep IORs strict. Different artifacts,
   different strictness.

2. **Should existing "noise" entries (v4.1-v4.5) be removed from**
   **IDENTITY.md?** They are honest records of incremental growth,
   even if they do not meet the new gate. Recommendation: keep them.
   They are accurate history. The new gate applies only to future
   sessions. Retroactive cleanup changes history.

3. **Should the trigger gate be extracted into a separate reference**
   **file?** Currently proposed inline in the session-end skill.
   If other skills need the same gate, extraction would follow
   R8 (Reference, Never Duplicate). Recommendation: keep inline
   for now. Only session-end uses this gate. Extract if another
   skill needs it.

## Approval Gate

If approved, I will:

1. Edit `~/.openclaw/workspace/skills/session-end/SKILL.md`:
   - Replace the "steady state" fallback in Step 5
   - Add the trigger gate definition
   - Update the self-check item
2. Verify the skill's self-check still passes with the modified text
3. Test: run the session-end procedure on a non-substantive session
   and confirm no identity entry is written
4. Commit and push to `workspace-ava`

I will NOT change IDENTITY.md, AGENTS.md, any other skill, or any
governance file.

## Cross-Links

- `skills/session-end/SKILL.md` -- the file being modified (in
  workspace, not agentic-brain)
- `governance/system-constitution.md` -- S10: agents propose changes,
  Suggi approves
