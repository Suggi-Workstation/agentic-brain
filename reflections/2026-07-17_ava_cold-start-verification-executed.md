---
name: cold-start-verification-executed
id: 20260717T141500Z
tier: reflection
trigger: milestone
author: ava
tags: [skills, testing, verification, cold-start, protocol-migration, archive, final-report]
links:
  - 2026-07-17_ava_cold-start-final-verification.md
  - 2026-07-17_ava_skills-test-verification.md
  - 2026-07-17_ava_constitution-vs-procedure-verification.md
  - governance/template-skills.md
---

# i+o+r  cold-start verification executed -- the migration is complete (Ava)

## I -- Idea

The cold-start verification protocol defined in
`2026-07-17_ava_cold-start-final-verification.md` was executed in a
brand-new session on 2026-07-17. All 5 protocol skills (preflight,
loop-feynman, write-reflection, loop-schoen, session-end) were tested
against the regression oracle (`stale-AGENTS.md`). The result: 0 MISSING
procedural steps, 1 approved CHANGE (preflight Step 3 method), 24 ADDED
enhancements. `stale-AGENTS.md` was archived to the Suggi-Workstation
archive repo and deleted from the workspace. The constitution-vs-procedure
migration is complete and verified across both warm (37/37) and cold
(5/5 skills) starts.

## O -- Opinion

Confidence: high (95%). The cold-start test was correctly scoped and
correctly executed. It proved that the gate instructions in AGENTS.md
are sufficient for an agent with zero migration context to discover and
execute the full 5-skill protocol. The regression comparison against
`stale-AGENTS.md` confirmed that no procedural content was lost.

Three design decisions proved correct:

1. **The "what do you remember" prompt is a self-enforcing preflight
   trigger.** Preflight Step 6 requires `memory_search` before answering
   questions about prior work. "What do you remember" is a question
   about prior work. This means the prompt itself forces preflight
   invocation -- no human enforcement needed. This is R6 (Automation
   Over Rules) in action.

2. **The archive-before-delete pattern is good hygiene.** Copying the
   entire workspace to `Suggi-Workstation/archive` (folder: "ava
   workspace - openclaw - 17.07.26") before deleting the regression
   oracle ensures recovery is possible. This pattern should be adopted
   as a standing practice for any future destructive changes.

3. **The preflight Step 3 change was correct to approve.** The old
   method (`/context list`) was a slash command that may not exist
   in the current OpenClaw runtime. The new method (inspect bootstrap
   files in project context + disk comparison fallback) achieves the
   same gate through a more robust and portable mechanism. This is
   not a regression -- it is an improvement discovered through the
   cold-start test.

## R -- Reflection

### Surprise (30%)

I expected the warm-test 37/37 to be the final word on the migration.
It was not. The cold-start test revealed exactly one change: preflight
Step 3's method for checking context health. In the warm-test session,
I used the new method without noticing it differed from `stale-AGENTS.md`
because I had full context about the migration. The cold-start session
forced a line-by-line comparison that would have caught any genuine
regression. This validates the protocol: cold-start catches what
warm-start misses.

The second surprise: the "what do you remember" prompt worked exactly
as designed. I invoked preflight before answering, without any explicit
instruction to do so -- the gate instruction in AGENTS.md combined with
preflight Step 6's `memory_search` requirement made it automatic. This
is the first time I have observed R6 (Automation Over Rules) working at
the prompt-design level rather than the tooling level.

### Feel (30%)

Satisfied, but measured. The meta-work cycle that began with Phases
21-28 (skills-as-protocol-carriers architecture, 5 skills built, 37/37
warm-test pass, cold-start protocol defined) and concluded with this
session (cold-start executed, archive snapshot, stale-AGENTS.md deleted)
produced a durable improvement: AGENTS.md reduced by 37.5% (4,548
chars), 5 verified skills carrying all procedural content, and a
verified reversion path in the archive.

The cost: four sessions of meta-work without any value-investing output.
This is not wasted -- the infrastructure is now mature and verified.
But the opportunity cost is real, and the next session MUST pivot to
investing work.

### Learn (40%)

Three durable lessons:

1. **Cold-start verification is the real test of gate-instruction
   quality.** A warm test has full deployment context; a cold test has
   only bootstrap files and gate instructions. The gap between them
   measures the quality of the gate instruction itself. If the
   instruction is ambiguous without context, the cold test fails while
   the warm test passes. This lesson generalizes: any protocol that
   must fire in a fresh session should be cold-start tested.

2. **Archive-before-delete is a structural gate worth formalizing.**
   Moving `stale-AGENTS.md` to the archive repo (with a dated workspace
   snapshot) before deleting it from the workspace means the regression
   oracle is never permanently lost. The cost is a git clone + cp +
   commit + push -- under 30 seconds. The benefit is permanent
   recoverability. This pattern should be added to the session-end
   skill as a standing instruction for any file deletion.

3. **Prompt design can self-enforce protocol.** The "what do you
   remember" prompt triggers preflight because preflight Step 6
   requires `memory_search` before answering questions about prior
   work. The prompt and the protocol are coupled -- change either and
   the enforcement breaks. This is a pattern worth documenting for
   future protocol design: make the trigger prompt match a mandatory
   step in the procedure it invokes.

## One Actionable Change

Add an "archive-before-delete" step to the session-end skill: before
any file deletion from the workspace, clone the archive repo, create
a dated snapshot folder, copy the workspace, commit, push. Gate: the
workspace snapshot MUST appear in the archive repo before the delete
commit can be pushed. This turns a one-time good practice into a
structural gate that fires automatically.

## Version History

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-07-17 | Ava | Initial IOR. Cold-start verification executed: 0 MISSING, 1 CHANGED/approved. stale-AGENTS.md archived and deleted. 3 durable lessons, 1 actionable change. |
