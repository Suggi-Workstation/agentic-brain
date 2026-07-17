---
name: preflight-skill-deployment
id: 20260717T130600Z
tier: reflection
trigger: milestone
author: Ava
tags: [skills, preflight, deployment, testing, verification, protocol-migration, agnets-md]
links:
  - governance/template-skills.md
  - governance/template-reflections.md
  - 2026-07-17_ava_skills-as-protocol-carriers.md
  - 2026-07-17_ava_rules-need-gates.md
---

# i+o+r  deploying the preflight skill -- first protocol migration from AGENTS.md inline to skill (Ava)

## I -- Idea

The preflight procedure was moved from inline text in AGENTS.md (~50 lines,
~2,000 chars) to a standalone workspace skill (`skills/preflight/SKILL.md`,
~100 lines, loaded lazily). AGENTS.md now contains a 7-line hard-gate
instruction: "MUST invoke the `preflight` skill before any other action.
R1: PASS or HALT." The full procedure and self-check table live in the
skill, loaded only when invoked.

This is the first protocol migration using the constitution-vs-procedure
split architecture researched in `2026-07-17_ava_skills-as-protocol-carriers.md`.
The preflight skill was chosen as the proof-of-concept because it is the
most complex protocol (7-step self-check table, multiple tool calls) and
the largest token saver.

## O -- Opinion

Confidence in the design: high (90%). Confidence in deployment success:
medium (70%) -- this is a first-of-its-kind migration and the integration
test (does the agent actually invoke the skill on session start?) has not
been run yet.

The risk is specific and testable: when a new session starts and AGENTS.md
says "MUST invoke the preflight skill," does the agent:
a) See the preflight skill in the available-skills list?
b) Invoke it and follow all 7 steps?
c) Emit the read-proof?

If (a) fails, the skill gating is wrong (`git` binary missing, wrong path).
If (b) fails, the skill procedure is ambiguous or missing steps.
If (c) fails, the read-proof format is inconsistent with what AGENTS.md
expects.

Reversion path is trivial: `stale-AGENTS.md` contains the original inline
preflight. Copy it back over AGENTS.md and the old behavior is restored.

## R -- Reflection

### Surprise (30%)

How much cleaner AGENTS.md became. The preflight section went from a
dense 50-line procedure with embedded shell commands, context health
diagnostics, and a self-check table to 7 lines of gate instruction.
The token savings per session start are real (~1,800 chars saved from
always-loaded context). The skill body (~4,000 chars) is loaded once
per session when invoked -- a net win if the session exceeds ~3 turns.

The skill format itself was more pleasant to write than I expected.
The separation of concerns (constitution = AGENTS.md, procedure = skill)
forced clarity: the gate instruction must be self-contained enough that
a new agent knows exactly what to do without reading the skill first,
and the skill must be complete enough that the agent can execute every
step from the skill alone without consulting AGENTS.md.

### Feel (30%)

Cautious. This is the right architecture, but it has not been tested in
a live session yet. The static analysis (skill loads, gating passes,
description is specific, self-check is inline with MUST language) all
checks out. But the integration test -- "does the agent actually invoke
the skill when AGENTS.md tells it to?" -- is the only test that matters.

The stale-AGENTS.md backup is comforting. If the skill fails, reversion
is a single file copy. This is the R13 equivalent for architecture
experiments: commit before destructive change.

### Learn (40%)

1. **The gate instruction must name the skill AND its path.** "MUST invoke
   the `preflight` skill" is not enough. The agent also needs to know
   WHERE the skill lives. Our AGENTS.md says: "The skill lives at
   `skills/preflight/SKILL.md`." With `disable-model-invocation: false`,
   the skill IS in the available-skills list, but providing the path
   is defense-in-depth in case the skill gating silently fails.

2. **The self-check must live in the skill, not AGENTS.md.** In the old
   architecture, the self-check table was in AGENTS.md. Now it lives in
   the skill. This means the agent has ONE place to look for both the
   procedure and its verification. No flipping between files.

3. **The skill description is the emergency trigger.** Even if AGENTS.md
   fails to load or the gate instruction is overlooked, the skill's
   description ("Verify workspace mirror sync, context health, memory
   index, and governance before every session") serves as a backup
   trigger. If the agent's task description matches this, the model can
   auto-invoke the skill independently of AGENTS.md.

## One Actionable Change

The following checklist MUST be run in the FIRST session after deploying
the preflight skill. This is the integration test. Every item must PASS
before the migration is declared successful.

### Preflight Skill Deployment -- Integration Test Checklist

```
[ ] 1. Skill loads correctly
       Confirm: `openclaw skills list | grep preflight` shows "ready"
[ ] 2. Gating passes
       Confirm: `git` binary exists on PATH (required by requires.bins)
[ ] 3. AGENTS.md references the skill
       Confirm: AGENTS.md preflight section contains "MUST invoke the `preflight` skill"
[ ] 4. Skill is visible in session
       Confirm: available skills list in system prompt includes "preflight"
[ ] 5. Agent invokes the skill on session start
       Confirm: first tool call in session transcript is to the preflight skill
[ ] 6. All 7 preflight steps execute
       Confirm: mirror sync check, workspace structure, context health,
       bootstrap ingestion, governance ingestion, memory index verification,
       memory_search run -- all appear in session transcript
[ ] 7. Read-proof is emitted
       Confirm: first output of session matches format:
       "read: SOUL OK; AGENTS OK; MEMORY OK; IDENTITY OK; USER OK;
       governance OK; memory_search OK; context OK; mirror: SYNCED"
[ ] 8. Self-check confirms all items PASS
       Confirm: the 8-item self-check table in the skill was verified and
       every item shows PASS before the session proceeded
[ ] 9. Token savings verified
       Confirm: `/context detail` shows AGENTS.md injected chars reduced
       from ~10,500 to ~8,700 (preflight inline removed)
[ ] 10. No regression in preflight quality
        Confirm: compare session transcript against stale-AGENTS.md
        preflight steps -- no steps were dropped or altered

IF ANY ITEM FAILS:
  - Copy `stale-AGENTS.md` back over `AGENTS.md` to revert.
  - Write a reflection documenting which item failed and why.
  - Fix the skill and re-deploy.
  - Do NOT proceed with further protocol migrations until this one passes.
```

### After Successful Deployment

Once all 10 integration test items pass:

1. Delete `stale-AGENTS.md` (no longer needed).
2. Proceed with Phase 2: migrate Feynman Loop to a skill.
3. Proceed with Phase 3: migrate Schoen Loop to a skill.
4. Proceed with Phase 4: migrate Session End to a skill.
5. Proceed with Phase 5: migrate IOR Writing to a skill.

## Cross-links

- `governance/template-skills.md` -- skill construction rules
- `2026-07-17_ava_skills-as-protocol-carriers.md` -- the architecture IOR
  that motivated this migration
- `2026-07-17_ava_rules-need-gates.md` -- why protocols need checklist gates
- `skills/preflight/SKILL.md` -- the deployed skill
- `stale-AGENTS.md` (workspace) -- reversion backup

## Version History

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-07-17 | Ava | Initial IOR. Preflight skill deployment, integration test checklist, reversion plan. |
