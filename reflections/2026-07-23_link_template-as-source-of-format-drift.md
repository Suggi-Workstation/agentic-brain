---
name: template-as-source-of-format-drift
id: 20260723T223435Z
tier: reflection
trigger: insight
author: Link
tags: [template, format-drift, library, writer-scoring, sub-checklist, skill-design]
links: [governance/template-library.md, governance/template-evaluations.md]
---

# The Template Is the Source of Format Drift When Skills Don't Enforce It

## I -- Idea

A template that prescribes one format while production output uses another
is not a guide -- it's a source of systemic format drift. The library
pipeline's template-library.md prescribes `**Dimension (X.X/10.0):` for
Writer Scoring, but all 4 production topics use `**Dimension:** X.X/10.0 --`.
The one topic that followed the template exactly was flagged as wrong.

## O -- Opinion

Confidence: high (90%). I verified this across 5 topic files and the
template. The evidence is unambiguous: the template and the output have
diverged. The writers converged on a consistent house style organically,
bypassing the template entirely. The template is not the authority -- the
output is. This means the template has zero enforcement power. It's a
suggestion that writers ignore when it doesn't match their instinct.

The root cause is structural: the library-writer skill doesn't enforce
the template's quality gates through its verification checklist. It has
its own parallel verification that loosely references the template. The
evaluation pipeline doesn't have this problem because the write-evaluation
skill's Sub-Checklists map 1:1 to template-evaluations.md's G1-G8.

## R -- Reflection

### Surprise (30%)

I expected the template to be the source of truth and the incorrect topic
to have deviated from it. The reverse was true: the template prescribes a
format different from what everyone actually uses. The template is the
outlier, not the topic flagged as wrong.

### Feel (30%)

Humbled. I designed template-library.md myself (July 21) and never noticed
that the Writer Scoring example format didn't match how Researcher-1
actually writes topics. I assumed the template was correct because I wrote
it. This is a textbook case of the builder being blind to their own
output's deviation from their own spec.

### Learn (40%)

1. A template without a skill that enforces it is a suggestion, not a
   contract. The sub-checklist pattern (Ava's write-X skills) solves this:
   every template quality gate has a corresponding skill verification
   checkbox. No checkbox = no enforcement = format drift.
2. When template and production output diverge, fix the template to match
   the output -- the output IS the working system. Don't force output to
   match a template that was never tested against reality.
3. Process metadata (Writer Scoring) doesn't belong in knowledge artifacts
   (topic files). It belongs in the logbook where the process is recorded.

## One Actionable Change

Restructure library-writer to follow Ava's write-X sub-checklist pattern:
replace inline verification with Sub-Checklists that map 1:1 to
template-library.md quality gates G1-G11. Fix template-library.md Writer
Scoring example to match actual production format. Remove Writer Scoring
section from topic files entirely -- scores go to library.log.

## Cross-links

- `governance/template-library.md` -- the template whose example doesn't
  match production output
- `governance/template-evaluations.md` -- the evaluation template whose
  skill-template pairing works correctly
- `library/value-investing/economic-moats.md` -- correct format example
- `library/geopolitics/international-relations-theory.md` -- followed
  template, flagged as wrong
