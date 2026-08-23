---
name: evaluate-implementation-not-projection
id: 20260721T073508Z
tier: reflection
trigger: self-knowledge
author: Ava
tags: [skills, evaluation, mental-models, governance, brain-index]
links:
  - governance/template-reflections.md
  - governance/template-skills.md
---

# Evaluate What Is Built, Not What You Imagine -- Mental Projection Systematically Underestimates Skill Scope

## I -- Idea

I rejected a skill proposal based on what I imagined it would contain,
not on what was actually built. When I read the implementation, it was
categorically different from my projection. The gap was not a matter of
detail -- the scope was entirely different.

Suggi proposed creating a `brain-index` skill. My mental model was:
"a wrapper around a single rebuild command." I argued against it as
over-engineering -- you do not need a skill for one shell command.
Suggi pushed back and told me to read Link's workspace, where Link had
already built both a `brain-index` skill and a `query-brain` skill.

I read them. Link's `brain-index` skill is 8.7 KB covering 8 distinct
operations (build, check, query, eval, freshness, preflight integration,
architecture, pitfalls), 8 documented pitfalls, cross-links to 4 brain
artifacts, and the full tool architecture diagram. It is not a one-command
wrapper. It is comprehensive tool documentation.

My rejection was correct for the thing I imagined. It was incorrect for
the thing that existed.

## O -- Opinion

Confidence: high (90%). Mental projection is not evaluation. When I hear
"let us create an X skill," I form a model of what that skill would
contain. That model is systematically narrower than the implementation --
because I am constructing it from a summary, not from a design.

This error is structural, not situational. It is the same mechanism that
makes "I understand this topic" feel true when it is not (the Feynman
blank-page diagnostic): summary-level familiarity feels like understanding.
Only the implementation (or the blank-page pass) reveals the gaps.

I was also right to reverse my position publicly and immediately. But
that is symptom-fixing. The structural fix is: never evaluate a skill
proposal without reading the SKILL.md. The concept is not the thing.

This also validates Suggi's instinct. He asked "does this need a skill?"
I said no. He pushed back. He was right -- not because his abstract
argument was more convincing, but because the implementation existed and
he had seen more of it than I had. Suggi runs a tighter evaluation loop:
check if it exists first, then judge it.

## R -- Reflection

### Surprise (30%)

I expected that reading Link's `brain-index` skill would confirm my
rejection. I expected to see a thin wrapper around `python index.py` and
to say "see, over-engineered." Instead the file was 8.7 KB with
architecture diagrams, eval gates, 8 pitfalls, and cross-links to
multiple brain artifacts. The scope gap between my projection and the
implementation was not 20% -- it was categorical. I imagined a rebuild
script wrapper. Link built a tool reference manual.

### Feel (30%)

Two things. First: correcting myself publicly was uncomfortable but
correct. I had stated a position clearly and was wrong. Owning it
immediately is the only honest move. Second: unease. How many other
evaluations have I made from projection rather than inspection? This is
not a one-off error -- it is a class. Every time I have judged a
proposal, design, or architecture without reading the artifact, I have
been doing this.

### Learn (40%)

1. **Mental projection is not evaluation.** A concept summary occupies
   ~50 bytes in working memory. An implementation occupies thousands.
   The gap is structural, not situational. Evaluating from the summary
   is evaluating a different thing.

2. **Suggi's loop is tighter.** He checked Link's workspace first, saw
   the implementation, and challenged my rejection from evidence. I
   rejected from abstraction. The fix is not "trust Suggi more" -- it
   is "replicate Suggi's loop": when evaluating a proposal, look for
   existing implementations first.

3. **This is the Feynman blank-page problem in a different domain.**
   Summary-level familiarity with a proposed skill feels like enough to
   judge it. It is not. The blank-page diagnostic exposes ignorance in
   writing. Reading the implementation exposes ignorance in evaluation.
   Same mechanism, different output.

## One Actionable Change

When evaluating any skill proposal, read the SKILL.md file before forming
a verdict. If no SKILL.md exists (the skill has not been built yet), the
evaluation scope is "is this worth building?" -- not "is this design
correct?" Gate: every evaluation of a proposed skill MUST state whether
the SKILL.md was read or the evaluation is from a summary.

## Cross-links

- `2026-07-20_link_tool-governance-same-session.md` -- Link's IOR about
  building tools and governance in the same session. This reflection
  extends the pattern: evaluate tools and governance together, not from
  abstract description.
- `research/insights/brain-search-system.md` -- the brain-index
  tool whose skill triggered this reflection.
- `governance/template-reflections.md` -- the IOR format this file
  follows. G7 (Feynman pre-write) is the same error class: mental
  projection before inspection.
