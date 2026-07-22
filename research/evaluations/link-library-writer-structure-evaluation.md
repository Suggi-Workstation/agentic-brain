---
name: link-library-writer-structure-evaluation
id: 20260722T202126Z
tier: evaluation
source: 20260722T184716Z
author: Link
tags: [library, writer, structure, template, evaluation, fix]
links:
  - research/proposals/library-writer-test.md
  - governance/template-library.md
  - governance/library-writer.md
  - library/value-investing/margin-of-safety.md
  - library/psychology-behavior/cognitive-biases.md
  - library/science/scientific-method-falsifiability.md
  - library/value-investing/economic-moats.md
---

# Library Writer Structure Audit -- Template and Skill Gaps

## Source

Evaluating structural consistency across 4 completed writer topics
against `governance/template-library.md` and the library-writer skill.
The writer produced high-quality content (all 4 pass content gates),
but the body structure varies inconsistently across topics. Root cause
is ambiguity in both the template and the skill, not writer error.

## Findings

### F1 -- Section ordering is inconsistent across all 4 topics (FAIL)

| Topic | Writer Scoring position | Order of final 3 sections |
|:--|:--|:--|
| margin-of-safety | Between Sources and See Also | Sources -> Scoring -> See Also |
| cognitive-biases | Missing entirely | Sources -> See Also |
| scientific-method | After See Also | Sources -> See Also -> Scoring |
| economic-moats | Between Sources and See Also | Sources -> Scoring -> See Also |

Four topics, three different section orders. The template says "Body
sections organized logically with ## headings" -- permissive, no
mandated order. The writer skill's Format Verification checklist says
"Sources cited" and "Cross-references included" but does not specify
a fixed section order or which sections are mandatory.

### F2 -- Writer Scoring missing from cognitive-biases.md (FAIL)

cognitive-biases.md (347 lines) has no Writer Scoring section at all.
The logbook entry (ENT-004) records scores (core=10.0, scope=10.0,
value=9.0, authority=7.0) -- so the writer DID score the topic -- but
the scores are not recorded in the topic file itself.

The skill's Format Verification says "All four dimensions scored with
brief justifications" without specifying WHERE. The writer interpreted
this as "recorded in logbook is sufficient." The topic file has no
scoring record, making it impossible for the auditor to verify the
claimed scores against the justifications without cross-referencing
the logbook.

### F3 -- Template is permissive where it should be prescriptive (ROOT CAUSE)

The template-library.md body structure section says:

> "The structure depends on the domain and topic, but a standard
> pattern is: Background, Core Concepts, Evidence, Implications."

Three problems:

1. **"Standard pattern" is a suggestion, not a requirement.** The
   writer correctly interpreted this as flexibility to add Common
   Pitfalls, Practical Frameworks, and Kuhn sections. Those additions
   are good. But the writer also reordered the mandatory closing
   sections (Sources, Writer Scoring, See Also) because the template
   never locked their order.

2. **Writer Scoring is not in the body structure at all.** The template
   has a checklist item: "Writer scoring recorded: all 4 dimensions
   scored with justifications." But the body structure template (the
   markdown skeleton the writer follows) has no ## Writer Scoring
   heading. The writer must guess where and how to include it.

3. **Sources and See Also positions are described in prose, not in
   the structure template.** The template says "A `## Sources` section
   at the end of the file" and "A `## See Also` section at the end
   (after Sources)." That is clear for Sources -> See Also ordering.
   But Writer Scoring has no position guidance, so it floats.

### F4 -- Writer skill Format Verification checklist is incomplete (ROOT CAUSE)

The current checklist says:
- "Sources cited: at least 3 web sources with URLs, each annotated
   with [high]/[medium]/[low] rating (PASS / HALT)"
- "Cross-references: at least 1 link to a related topic or brain
   artifact (PASS / HALT)"
- "All four dimensions scored with brief justifications (PASS / HALT)"

Missing from this checklist:
- No item checking that a ## Writer Scoring section EXISTS
- No item checking section ORDER (Sources before See Also)
- No item linking the scoring to a specific format (dimensions with
  weights, formula, justifications, similarity overlap)

### F5 -- Body additions are correct and should be preserved (PASS, context)

The writers added sections that are not in the "standard pattern":
- Common Pitfalls (margin-of-safety, economic-moats)
- Practical Moat Analysis Framework (economic-moats)
- Kuhn and Paradigm Shifts as a top-level section (scientific-method)
- Core Biases by Category with ### sub-sections (cognitive-biases)
- Writer Scoring (3 of 4 topics)

These additions are substantively correct. The fix is not to remove
them but to lock the mandatory closing sections (Sources, Writer
Scoring, See Also) in a fixed order while preserving the writer's
freedom to add domain-specific content sections before them.

## Required Changes

### Change 1: Add ## Writer Scoring to template-library.md body structure

Insert between the Implications section and Sources section:

```markdown
### Writer Scoring

A `## Writer Scoring` section recording the scored dimensions with
justifications. MUST appear after the last body content section and
before `## Sources`.

Format:

- **Core match (X.X/10.0):** <1-2 sentence justification>
- **Scope fit (X.X/10.0):** <1-2 sentence justification>
- **Knowledge value (X.X/10.0):** <1-2 sentence justification>
- **Source authority (X.X/10.0):** <1-2 sentence justification>

**Weighted score:** (core * 0.35) + (scope * 0.35) + (value * 0.20)
+ (authority * 0.10) = **X.X/10.0**

**Topic similarity:** <X% overlap with existing topics. Proceeded/
Flagged/Skipped.>
```

### Change 2: Lock section order -- mandatory vs optional

In template-library.md, replace the permissive "standard pattern"
with explicit MUST/MUST NOT:

```markdown
## Body Structure

The body MUST include these sections in this order:

1. **Title** -- level-1 heading making a claim
2. **Opening paragraph** -- 2-3 sentences
3. **Body content sections** (## headings, domain-specific, order
   at writer's discretion). Standard pattern: ## Background, ## Core
   Concepts, ## Evidence, ## Implications. Additional sections
   (Common Pitfalls, Frameworks, Case Studies) are permitted.
4. **## Writer Scoring** -- scores with justifications (MUST)
5. **## Sources** -- cited references (MUST)
6. **## See Also** -- cross-references (MUST)

The last three sections (Writer Scoring, Sources, See Also) MUST
appear in this exact order. No content sections may follow ## See Also.
```

### Change 3: Add gate items to template-library.md checklist

Add to the Pre-commit checklist:
```
- [ ] ## Writer Scoring section present with all 4 dimensions
      scored, weighted formula shown, similarity overlap recorded
      (PASS / HALT)
- [ ] Section order correct: Writer Scoring -> Sources -> See Also.
      No content after See Also.  (PASS / HALT)
```

### Change 4: Add gate items to writer skill Format Verification

Add to the Scoring verification section:
```
- [ ] ## Writer Scoring section present with all 4 dimensions,
      justifications, weighted formula, and similarity overlap
      (PASS / HALT)
```
Add to the Body Structure verification section:
```
- [ ] Section order: body content -> Writer Scoring -> Sources ->
      See Also. No sections after See Also.  (PASS / HALT)
```

### Change 5: Remove ambiguity from writer skill step 7

Step 7 currently says "Write the topic file" with no structural
guidance. The structural guidance lives in the template. Add a
line: "Follow the body structure and section order specified in
`governance/template-library.md` exactly."

## Impact

- **Positive:** All 4 existing topics would pass a structural gate
  after the fixes are applied (retro-fitting Writer Scoring into
  cognitive-biases.md and re-ordering scientific-method.md). Future
  topics will be structurally identical regardless of which writer
  model produces them.
- **Risk:** Low. Adding mandatory sections to the template is backward-
  compatible -- no existing topic content is invalidated, only
  re-ordered.
- **Cost:** 4 edits across 2 files (template-library.md, library-writer
  skill). All 3 copies must be synced (governance, researcher-1, Link).

## Confidence

**High (90%).** The structural inconsistency is directly observable
across 4 files. The root cause (template permissiveness + missing
checklist items) is clear. 10% reserved for whether the writer models
will reliably follow MUST/MUST NOT instructions on section order --
weaker models may still deviate.

## Cross-Links

- `governance/template-library.md` -- template to fix
- `governance/library-writer.md` -- skill to fix
- `library/value-investing/margin-of-safety.md` -- topic 1
- `library/psychology-behavior/cognitive-biases.md` -- topic 2 (missing
  Writer Scoring)
- `library/science/scientific-method-falsifiability.md` -- topic 3
  (Writer Scoring after See Also)
- `library/value-investing/economic-moats.md` -- topic 4
- `research/proposals/library-writer-test.md` -- original test spec
