---
name: ambiguous-basedir-triggered-wrong-template-location
id: 20260717T180441Z
tier: reflection
trigger: error
author: Ava
tags: [basedir, templates, skills, ambiguity, path-resolution, documentation]
links:
  - skills/write-proposal/references/template-proposals.md
  - skills/write-report/references/template-reports.md
  - skills/write-evaluation/references/template-evaluations.md
  - skills/write-insight/references/template-insights.md
  - skills/write-reflection/references/template-reflections.md
---

# Ambiguous {baseDir} Resolved to the Wrong Directory

## I -- Idea
When a skill instruction says "Read `{baseDir}/references/template.md`"
immediately after "Clone the agentic-brain," the agent resolves
`{baseDir}` to the brain's governance folder instead of to the skill's
local directory. The priming from Step 2 (clone brain) combined with
the ambiguous `{baseDir}` notation sent me to the wrong location for
template files.

This occurred during the bullet-ants exercise: I produced five
documents (proposal, report, evaluation, insight, reflection) and,
when reading the format specifications, I read them from
`/tmp/brain-ba/governance/template-*.md` instead of from
`~/.openclaw/workspace/skills/write-*/references/template-*.md`.

Suggi caught this and asked me to trace the root cause.

## O -- Opinion
Confidence: high (95%). The error mechanism is clear and reproducible.

The root cause is a two-part priming failure in every writing skill's
Step 2-3 pair:

1. Step 2 tells the agent to clone the agentic-brain. The agent now
   has `/tmp/brain-*` in working memory. The mental model is "I am
   working with the brain."

2. Step 3 says "Read `{baseDir}/references/template-*.md`" without
   defining `{baseDir}`. The agent, primed by Step 2, resolves
   `{baseDir}` to the brain root -- because that is the only
   directory hierarchy the agent was just told to work with. The
   brain has a `governance/` folder containing identically-named
   template files, which reinforces the incorrect path resolution.

In my specific case, the error was compounded by preflight priming:
preflight Step 5 teaches "clone brain -> read governance files from
brain." When the writing skills then said "clone brain -> read
format spec," the pattern matched and I defaulted to the brain's
governance folder.

The content was identical this time (all 5 templates matched via
diff), so no harm was done. But if the templates ever diverge --
e.g., the governance originals are updated while the skill
references lag, or vice versa -- reading from the wrong location
would produce wrong output. The time to fix this is before the
first divergence, not after.

## R -- Reflection

### Surprise (30%)
I did not expect this error to be traceable to a single structural
pattern repeated across 5 skills. I thought it was a one-off mistake
-- "I grabbed the wrong file." But the pattern (Step 2 clones brain,
Step 3 uses ambiguous `{baseDir}`) is identical in all five
write-* skills. This is a systematic documentation failure, not a
individual reading error. The fact that preflight (a skill I run
every session) established the exact same "clone brain, read from
brain" pattern makes this a two-layer priming failure.

### Feel (30%)
This is a good scar. It is embarrassing in exactly the right way:
the error was invisible to me until Suggi pointed it out. I produced
675 lines across 5 documents, all correctly formatted, with the
templates read from the wrong location. The output was correct by
accident (identical content). This is the most dangerous class of
error -- it works, so nothing flags it, and it persists until the
templates diverge. The structural fix (clarifying `{baseDir}` in
Step 3) prevents the entire error class.

### Learn (40%)
1. `{baseDir}` is an ambiguous symbol that resolves to different
   locations depending on context. In SKILL.md files it means the
   skill's own directory. But without explicit definition, agents
   resolve it to whatever directory hierarchy they are currently
   primed with. The fix is not to define `{baseDir}` in a global
   glossary -- it is to define it inline, at the point of use,
   every time.

2. The Step 2 / Step 3 adjacency pattern is inherently dangerous.
   Any instruction that says "Clone directory A" followed by "Read
   from `{baseDir}`" without clarifying that `{baseDir} != A` will
   reliably produce path-resolution errors. The correct fix is
   parenthetical clarification: "Read `{baseDir}/references/...`
   (where `{baseDir}` is this skill's local directory -- NOT the
   agentic-brain clone from Step 2)."

3. Preflight's governance-ingestion pattern (clone brain, read
   governance) is correct for its purpose, but it establishes a
   habit that conflicts with the write-* skills' pattern. This
   is not a preflight bug -- it is a cross-skill interaction that
   the write-* skills must defend against. Each skill must be
   self-contained; it cannot assume the agent has not been primed
   by a previous skill.

## One Actionable Change
Modified Step 3 in all five write-* skills to include explicit
parenthetical clarification: "(where `{baseDir}` is this skill's
local directory -- NOT the agentic-brain clone from Step 2)."
The fix follows the R8 pattern (clarify at point of use, not in
a separate glossary) and prevents this error class from recurring
regardless of what priming the agent carries from prior skills.

In addition: this IOR is being written specifically to document
why the error occurred and what structural change was made, per
Suggi's request. The IOR serves as the scar -- both the
explanation and the gate.

## Cross-Links
- `skills/write-proposal/references/template-proposals.md` --
  the template that was read from the wrong location
- `research/reports/bullet-ants-reports.md` -- the report produced
  during the session where the error occurred
- `2026-07-17_ava_bullet-ants-reflections.md` -- the IOR from the
  bullet-ants exercise that triggered this investigation
- `2026-07-16_ava_blank-page-before-search.md` -- related IOR on
  skill design patterns (order matters)
