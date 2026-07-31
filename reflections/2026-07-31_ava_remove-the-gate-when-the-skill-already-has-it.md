---
name: remove-the-gate-when-the-skill-already-has-it
id: 20260731T112419Z
tier: reflection
trigger: insight
author: Ava
tags: [gates, skills, duplication, automation, feynman, write-x, r6, r8, r11]
links:
  - governance/skills/loop-feynman.md
  - governance/skills/write-reflection.md
  - governance/skills/write-evaluation.md
  - governance/skills/write-insight.md
  - governance/skills/write-proposal.md
  - governance/skills/write-report.md
  - governance/skills/write-skill.md
---

# Remove the Gate When the Skill Already Has It -- Skills Trigger Skills, Bootstrap Files Should Not Duplicate

## I -- Idea

A gate in a bootstrap file that duplicates a gate in a skill is worse
than redundant -- it creates a second authority that will inevitably
drift. When every trigger path to the gate already passes through the
skill, the bootstrap copy serves no function except to occupy attention.

The AGENTS.md had two HARD GATE sections -- Reflection Writing (5-item
checklist) and The Feynman Loop (6-item checklist) -- that duplicated
content from `write-reflection` SKILL.md (~30+ checks across 5
sub-checklists) and `loop-feynman` SKILL.md (7-item self-check). Both
were removed in a three-step cleanup: first shrunk to invocation-only
lines, then removed entirely when analysis confirmed zero trigger paths
led to them. Simultaneously, the loop-feynman skill was revived from
dead code (nothing invoked it) and integrated as Step 1 into all 6
write-x skills, replacing R11-violating hardcoded lists with
artifact-agnostic language.

## O -- Opinion

Confidence: high (95%). This is not a design hypothesis -- it is the
logical conclusion of two existing gate rules applied consistently.

R6 (Automation Over Rules): "A gate that fires by itself beats a rule
that must be remembered." The skills' self-checks fire automatically
when the skill is invoked. The AGENTS.md versions require volition --
I must remember to look at them. The skill trigger chain (session-end
-> write-reflection -> loop-feynman, or any write-x -> loop-feynman)
fires automatically. The AGENTS.md gate is hope.

R8 (Reference, Never Duplicate): "Before writing any instruction,
check if it already exists. Duplication = drift." The AGENTS.md
checklists were literal subsets of the skill self-checks. If the
skill updated (as it did today -- IOR->Reflection, Feynman Step 1
added, renumbering), the AGENTS.md copy would not. The drift had
already begun: the skill had 30+ checks, AGENTS.md had 5.

The only question is whether the bootstrap file serves as a trigger.
It does not. Every path to writing a reflection passes through
session-end Step 3, which invokes write-reflection directly. Every
path to writing an artifact passes through a write-x skill, which
has Feynman as Step 1. There are zero scenarios where I would be
writing a brain artifact and the AGENTS.md sections would be the
thing that tells me to use the skills.

The Feynman Loop skill was in even worse shape before this session:
it was `user-invocable: false` but nothing invoked it. Only one of
six write-x skills referenced it, and even that was just a quality
gate check, not a triggered sub-skill invocation. The "When to Apply"
section had an R11 violation -- hardcoding "research report,
evaluation, or IOR" as the trigger list. The skill was IOR-centric
when it should be artifact-agnostic. It had the architecture of a
gate but no road leading to it.

## R -- Reflection

### Surprise (30%)

I expected the AGENTS.md sections to serve as bootstrap triggers --
"on fresh context, the agent reads this and knows to invoke the skill."
But tracing every trigger path revealed the opposite: the skills form
a closed invocation chain. Session-end calls write-reflection. Every
write-x skill calls loop-feynman as Step 1. A fresh session reads
AGENTS.md -> Session-End gate -> session-end skill -> write-reflection
skill -> loop-feynman skill. No step in this chain consults the
Reflection Writing or Feynman Loop sections. They were vestigial.

The second surprise was that loop-feynman was dead code. I had been
doing the Feynman blank page from training (it is a deeply ingrained
habit), not because the skill was ever formally invoked. The skill
file existed but nothing called it. The habit was real but the
mechanism was broken. This is the exact R6 failure mode: a rule
enforced by habit, not by automation.

### Feel (30%)

A quiet satisfaction at the architectural cleanliness. Before this
session, the gate landscape had two kinds of redundancy: duplicate
checklists (AGENTS.md vs skills) and orphaned skills (loop-feynman
with no invoker). Now the skills form a clean chain: session-end
triggers write-reflection, write-x skills trigger loop-feynman. Each
skill has one authoritative self-check. The bootstrap file references
the skills without duplicating them. This is the architecture I would
design if starting from scratch -- it took three passes to arrive at
it because each pass revealed the next layer of redundancy.

There is also a small discomfort: Suggi spotted this. He asked "Do
these checklists even get triggered by the skills?" and that question
unfolded the entire analysis. I had been looking at those sections
every session and never questioned whether they actually fired. The
immersion produces completeness illusion again -- the same class as
the bridge-mode mirror fallacy (v6.0). I saw gates in the bootstrap
context and assumed they were doing work.

### Learn (40%)

1. **Trace the trigger path before declaring a gate necessary.** The
   question "when would I ever read this and act on it?" must trace
   every possible entry point. If the answer is "never, because the
   skill already fires automatically from another path," the gate is
   vestigial. This applies beyond AGENTS.md: any instruction in any
   file should have a documented trigger path. If it does not, it is
   a hope, not a gate.

2. **Skills form chains; bootstrap files should not duplicate the
   chain.** The correct pattern: AGENTS.md says "invoke session-end."
   session-end says "invoke write-reflection." write-reflection says
   "invoke loop-feynman." Each link is a single invocation reference.
   No skill duplicates another skill's checklist. No bootstrap file
   duplicates a skill's checklist. The chain IS the automation.

3. **A `user-invocable: false` skill with no invoker is dead code.**
   The loop-feynman skill was built with the right architecture
   (self-check, 6-step procedure, R4 gate) but never connected to
   any invocation path. Five of six write-x skills had no reference
   to it. The fix was not to make it `user-invocable: true` -- it was
   to embed it as a prerequisite step in every skill that needs it.
   A skill that must be remembered is not a skill; it is a note.

## One Actionable Change

When adding or editing any HARD GATE section in AGENTS.md, apply the
trigger-path test: trace every scenario where this gate would fire and
verify at least one path does not already pass through a skill with
its own self-check. If all paths go through a skill, the AGENTS.md
gate is redundant and should reference the skill instead of
duplicating its checks. If no path leads to the gate, remove it.

## Cross-links

- `governance/skills/loop-feynman.md` -- the Feynman Loop skill, now integrated as Step 1 in all write-x skills
- `governance/skills/write-reflection.md` -- the Reflection Writing skill, renamed from IOR Writing
- `reflections/2026-07-18_ava_search-feature-analysis.md` -- same R8 pattern applied to retrieval architecture
- `reflections/2026-07-28_ava_infrastructure-ready-is-not-working.md` -- the bridge-mode mirror fallacy, same "immersion produces completeness illusion" class
