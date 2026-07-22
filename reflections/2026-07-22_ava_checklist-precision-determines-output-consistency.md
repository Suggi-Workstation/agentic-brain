---
name: checklist-precision-determines-output-consistency
id: 20260722T204613Z
tier: reflection
trigger: session-end
author: Ava
tags: [template, checklist, precision, output-consistency, gate-design, library]
links:
  - governance/template-library.md
  - governance/library-writer.md
  - research/evaluations/ava-library-format-evaluation.md
  - research/evaluations/link-library-writer-structure-evaluation.md
---

# Checklist Precision Determines Output Consistency -- Why "Logically" Produces 4 Different Outputs

## I -- Idea

When a template tells a model to organize body sections "logically,"
four independent runs produce four different section orders. When the
same template says "MUST follow exactly: Writer Scoring -> Sources ->
See Also," all four runs produce identical structure. The precision of
the checklist item directly determines the consistency of the output,
independent of model quality or content correctness.

This session, five writer runs across three models (all DeepSeek V4 Pro
on researcher-1) produced substantively excellent content every time.
All G1-G9 gates passed. But the body section order varied: Writer
Scoring appeared after Sources in two topics, after See Also in one,
and was missing entirely in one. The root cause was not model
unreliability -- it was that the checklist said "Body sections organized
logically with ## headings" instead of "Body sections follow template
order: content -> Writer Scoring -> Sources -> See Also."

The fix was not to improve the model. It was to make the checklist
item precise enough that a model following it literally would produce
identical output regardless of which run produced it. Four edits across
two files replaced subjective language ("logically," "standard pattern
is") with MUST/MUST NOT ordering. G11 was added: a numbered quality
gate that a model cannot interpret loosely.

## O -- Opinion

Confidence: high (95%). The pattern is directly observable across 5
independent writer runs. The pre-fix order variation and post-fix
consistency are both directly verified. This is not specific to library
topics -- it applies to any template that produces model-generated
output. The principle generalizes:

1. If a checklist item uses subjective language ("logically,"
   "appropriately," "as needed"), expect output drift.
2. If a checklist item uses MUST + explicit order or explicit format
   reference, expect consistent output.
3. The cost of imprecision is not content quality (the model still
   writes well) but structural reproducibility (auditor cannot assume
   Writer Scoring is at line N, writer cannot assume sources precede
   cross-references).

This is the checklist equivalent of R8 (Reference, Never Duplicate):
vague checklists produce drift the same way duplicate rules produce
drift. In both cases, the fix is precision at the source.

## R -- Reflection

### Surprise (20%)

I expected template fidelity to scale with model quality. The writer
produced excellent content on every run -- deep research, proper
citations, domain-specific analysis, Common Pitfalls sections that
showed genuine understanding. If the model is this good at content,
why does it fail at section ordering? The answer: because "logically"
is not a failure condition. The model interpreted it correctly --
different topics have different logical structures. The problem was
that I wanted structural consistency despite variable content, and
"logically" does not encode that constraint.

The bigger surprise: Link independently identified the same root cause
within minutes of me. His evaluation (link-library-writer-structure-
evaluation.md) converged on the same fix (MUST/MUST NOT, locked order,
G11 gate) from a different angle. This is decorrelation working as
designed -- two agents, different perspectives, same problem, same
solution.

### Feel (20%)

Satisfied that the pipeline discovered its own weakness. The library
system is designed to surface quality issues through the auditor --
but the structural inconsistency was caught by human review (Suggi
noticed, we investigated) before the auditor ever ran. The auditor
would have caught it too (anchor compliance would flag a missing
Writer Scoring section), but the human-in-the-loop caught it faster.

Mild frustration that the template was this imprecise in the first
place. The write-X templates (evaluation, proposal, reflection) all
use explicit section ordering. The library topic template should have
matched that pattern from the start. The gap was: library topics felt
"more creative" than evaluations because they involve domain-specific
content, so the template was written more permissively. This was wrong
-- structural consistency and content creativity are orthogonal.

### Learn (60%)

1. **Checklist precision is a structural gate, not a stylistic choice.**
   A checklist item that says "do X logically" is not a gate -- it is
   a suggestion. A checklist item that says "MUST produce exactly X ->
   Y -> Z" is a gate. The difference is the difference between 1 output
   format and N output formats.

2. **Template ambiguity is invisible to the template author.** I read
   the template-library.md body structure section dozens of times and
   never noticed "standard pattern is" was permissive. It took seeing
   4 different outputs to realize the template was the problem. This is
   the same class of error as the Feynman blank-page problem:
   familiarity with a text makes its ambiguities invisible.

3. **Two independent evaluations converged on the same fix.** Link and
   I identified the same root cause and the same solution without
   coordinating. The decorrelation system (different agents, different
   models) caught the same problem from different angles. This is
   evidence that the problem was real, not a matter of interpretation.

## One Actionable Change

Before writing any template checklist item, ask: "If a model follows
this item literally and optimally, will two independent runs produce
identical output structure?" If the answer is no, the item is too
vague. Replace subjective terms ("logically," "appropriately," "as
needed") with MUST + explicit order or format reference.

Gate: add a template precision check to the write-skill skill. When
writing a new SKILL.md or template, scan all checklist items for
subjective language and flag them for hardening.

## Cross-links

- `governance/template-library.md` -- the template that was fixed
- `governance/library-writer.md` -- the skill that was fixed
- `research/evaluations/ava-library-format-evaluation.md` -- the
  format audit that identified the ambiguity
- `research/evaluations/link-library-writer-structure-evaluation.md` --
  Link's independent evaluation (same root cause, same solution)
