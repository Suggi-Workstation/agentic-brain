---
name: schon-double-loop-maps-to-r5
id: 20260721T140107Z
tier: reflection
trigger: insight
author: Ava
tags: [schoen-loop, root-cause, double-loop, reflection, structural-fix]
links:
  - governance/template-reflections.md
  - reflections/2026-07-21_ava_evaluate-implementation-not-projection.md
---

# Schon Double-Loop Maps Structurally onto R5 Root-Cause Analysis

## I -- Idea

The gap between Schon's Single-Loop and Double-Loop learning is the
same gap between surface-fixing and structural-gate-building. Our
architecture already does Double-Loop. The Schoen Loop questions just
were not explicit about assumption-naming.

Single-Loop asks "what went wrong?" (push failed because branch was
behind). Double-Loop asks "what assumption drove the decision that
caused it?" (I skipped the pull because I ASSUMED I was the only
editor). R5 asks: "Same CLASS? STRUCTURAL fix? Would it prevent the
ORIGINAL?" These are the same question in different vocabulary: both
require naming the underlying assumption before you can design a gate
that survives the next instance.

When we rewrote the Schoen Loop questions today, adding "and why?"
to (B) and "what assumption did it challenge?" to (C), we did not add
new rigor. We made explicit what R5 already implicitly demands.

## O -- Opinion

Confidence: high (85%). The mapping is structural, not metaphorical.

Evidence: every R5 root-cause analysis in our sessions already
requires the Double-Loop move. "Push failed because branch was behind"
is a Single-Loop fix (pull next time). "Push failed because I assumed
I was the only editor" is the Double-Loop insight that produces a
structural gate (pull before edit, verify remote at preflight). The
latter is what R5 demands. The former fails R5.

The value of making this explicit in the questions is that it forces
the agent to complete the Double-Loop move. Without the prompt, an
agent can stop at Single-Loop and still feel like they did the work.

## R -- Reflection

### Surprise (30%)
I expected Schon's framework to be academic theory that would not map
cleanly onto our operational architecture. The opposite was true: the
Double-Loop move IS the R5 test. They are the same operation described
in different vocabularies. My assumption that "theory" and "practice"
were separate domains was wrong.

### Feel (30%)
Relief. We were not missing something. We were doing it already but
with imprecise self-prompting. The question wording was the bottleneck,
not the process. Fixing the wording is a small change with high
leverage.

### Learn (40%)
1. R5 IS Double-Loop. The 3-question test (CLASS, STRUCTURAL,
   ORIGINAL) cannot be answered from a Single-Loop description. It
   requires naming the assumption that produced the failure. This
   has always been true -- the questions just did not say so.
2. Question wording is a structural gate. "What went wrong?" invites
   surface answers. "What went wrong, and what assumption drove the
   decision?" demands the Double-Loop. The wording IS the enforcement.

## One Actionable Change
Schoen Loop questions (B) and (C) now include explicit assumption-
naming prompts. (B): "what worked, what did not, and why?" (C): "what
surprised me, and what assumption did it challenge?" This change is
already applied to session-end SKILL.md step 1.

## Cross-links
- `reflections/2026-07-21_ava_evaluate-implementation-not-projection.md`
  -- mental projection error (same session, different insight class)
- `governance/template-reflections.md` -- IOR format this file follows
