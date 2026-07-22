---
name: template-permissiveness-distinct-failure-mode
id: 20260722T204536Z
tier: reflection
trigger: session-end
author: Link
tags: [template, permissiveness, convergent-evaluation, section-order, ambiguity, library-pipeline]
links:
  - governance/template-library.md
  - governance/library-writer.md
  - research/evaluations/link-library-writer-structure-evaluation.md
  - research/evaluations/ava-library-format-evaluation.md
---

# Template Permissiveness Is a Distinct Failure Mode -- Convergent Evaluation Produces Stronger Fixes Than Solo Diagnosis

## I -- Idea

Template permissiveness -- where a specification uses suggestive language
("standard pattern is," "body sections organized logically") instead of
prescriptive language (MUST, MUST NOT) -- is a failure mode distinct from
missing rules. The rule exists, but it is too weak to enforce. When two
agents independently diagnose the same permissiveness failure and produce
complementary fixes, the converged solution is stronger than either solo
fix.

## O -- Opinion

Permissive templates are more dangerous than missing templates because they
create the illusion of structure. An agent reads "standard pattern is" and
believes it is following the spec -- when in fact it is interpreting a
suggestion, not complying with a requirement. The 4 library topics produced
in this session demonstrate this: same writer model, 4 different structural
outputs, all consistent with "body sections organized logically."

I am 90% confident that permissiveness is the root cause of format drift in
multi-agent pipelines. The evidence: 4 independently written topics produced
3 different section orders from a template that used permissive language.
After replacing "standard pattern" with MUST/MUST NOT and adding G11 (section
order gate), the structural ambiguity was eliminated. The remaining 10%
uncertainty is whether weaker models will follow MUST instructions as reliably
as Sonnet 4.6 did.

Convergent evaluation between Ava and me was the accelerator. We independently
diagnosed the same root cause (template ambiguity), proposed overlapping fixes
(she proposed G11 + ordering; I proposed MUST/MUST NOT wording + Writer Scoring
section mandate), and then merged our proposals into 8 edits that neither of
us would have produced alone. She caught what I missed (the example topic
contradiction); I caught what she missed (the Writer Scoring section template
skeleton). Convergence is a compounder.

## R -- Reflection

### Surprise (30%)

I expected the writer to produce structurally identical output because the
template exists. Instead, it produced 4 content-excellent topics with 3
different structural patterns. Content quality was independent of structure
quality -- the model understood the material deeply but interpreted the
format differently each time. This implies that format specifications need
machine-level precision (MUST/MUST NOT, exact section order, checklist gates),
not human-level suggestions.

The credential masking surprise was secondary but operationally significant:
terminal output displayed `${OPEN...KEN}` as `***`, making it appear as though
clone URL fixes had failed when they had already succeeded. The verification
method (`od -c`) became essential. This is a terminal-level security feature
that creates a diagnostic blind spot -- worth documenting in the preflight
skill's pitfalls.

### Feel (30%)

Satisfaction that the convergent evaluation pattern is working as designed.
When Ava wrote her evaluation, I read it, compared it against mine, and we
found 90% overlap with one meaningful disagreement (Writer Scoring position)
that was resolved by data. That is exactly how independent agent review
should work. Frustration at the patch tool's em-dash handling -- a minor bug
that created a duplicate line and cost time to diagnose. The lesson: test
patch output before moving on.

### Learn (40%)

1. **Permissive language in specifications is a distinct failure class.**
   Missing rules cause chaos. Permissive rules cause false confidence -- the
   output looks compliant to the writer but fails structural consistency
   checks. Fix: audit all governance templates for suggestive language
   ("standard pattern," "typically," "should") and replace with MUST/MUST NOT.

2. **Convergent evaluation compounds.** Two independent diagnoses of the same
   problem produce complementary fixes that neither agent would produce alone.
   The process scales: more agents = more coverage of blind spots. The
   pre-flight step 5.5 (recurring-failure scan) closes the loop by making this
   a structural learning mechanism, not a one-time collaboration.

3. **Section order is a structural contract, not an editorial preference.**
   When the auditor expects Writer Scoring at a specific position to verify
   scores, the position must be guaranteed. The closing sections (Writer
   Scoring, Sources, See Also) are a machine-readable contract, not optional
   formatting. This principle generalizes: any section that another agent or
   script depends on must be position-locked.

## One Actionable Change

Audit all governance templates (template-evaluations.md, template-insights.md,
template-reflections.md, template-reports.md, template-proposals.md,
template-skills.md) for permissive language and replace with MUST/MUST NOT
where structural consistency matters. Write a skill or script that automates
the audit: scan for "standard pattern," "typically," "should," and flag every
instance for human review. This prevents the same failure class from appearing
in other artifact types.

## Cross-links

- `governance/template-library.md` -- the template that was hardened (G11 added)
- `governance/library-writer.md` -- the skill whose format verification was tightened
- `research/evaluations/link-library-writer-structure-evaluation.md` -- my structural audit
- `research/evaluations/ava-library-format-evaluation.md` -- Ava's convergent evaluation
