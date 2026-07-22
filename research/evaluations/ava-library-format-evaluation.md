---
name: ava-library-format-evaluation
id: 20260722T202143Z
tier: evaluation
source: 20260722T184716Z
author: Ava
tags: [library, format, template, evaluation, skill-fix, body-structure, reproducibility]
links: [governance/template-library.md, governance/library-writer.md, research/evaluations/ava-library-writer-evaluation.md]
---

# Library Topic Format Audit -- Template Ambiguities Causing Output Drift

## Source

Auditing all 4 writer-produced topic files against the format
specification in `governance/template-library.md` and the procedure
in `governance/library-writer.md`. Four topics exist across three
domains after four writer test cycles: margin-of-safety (value-investing),
cognitive-biases (psychology-behavior), scientific-method-falsifiability
(science), economic-moats (value-investing).

## Evaluation Criteria

1. Section ordering: does the body follow the template structure?
2. Section naming: do section headings match the template?
3. Writer Scoring: present? correctly positioned?
4. Sources / See Also ordering: correct relative position?
5. Root cause: are the deviations the writer's fault, or template
   ambiguity?

## Findings

### F1 -- Section ordering drifts across all 4 topics (FAIL)

The template defines this body structure (line 98-112):
`## Background`, `## Core Concepts`, `## Evidence`, `## Implications`,
`## Sources`, `## See Also`.

Actual output:

| Topic | Sections | Deviations |
|:--|:--|:--|
| margin-of-safety | Background, Core Concepts, Evidence, Implications, **Common Pitfalls**, Sources, **Writer Scoring**, See Also | +2 extra sections inserted between template blocks |
| cognitive-biases | Background, **Core Biases by Category**, **Evidence and Research Foundation**, Implications, Sources, See Also | Renamed sections, **Writer Scoring MISSING** |
| scientific-method | Background, Core Concepts, **Kuhn and Paradigm Shifts**, Evidence, Implications, Sources, See Also, **Writer Scoring** | +1 extra section, Writer Scoring AFTER See Also |
| economic-moats | Background, Core Concepts, Evidence, **Practical Moat Analysis Framework**, Implications, **Common Pitfalls**, Sources, **Writer Scoring**, See Also | +3 extra sections |

**Root cause:** The template body structure lists four example sections
but nowhere states that the ordering is mandatory. The writer is told
"Body sections organized logically with ## headings" (G2 check in the
skill) -- "logically" is subjective. The template example shows an
order but never says MUST follow this order.

### F2 -- Writer Scoring placement varies (FAIL)

Three of four topics include Writer Scoring, but at two different
positions:
- margin-of-safety: Sources -> Writer Scoring -> See Also
- cognitive-biases: MISSING entirely
- scientific-method: Sources -> See Also -> Writer Scoring (WRONG)
- economic-moats: Sources -> Writer Scoring -> See Also

**Root cause:** The template says "Writer scoring recorded: all 4
dimensions... scored with justifications" as a checklist item (line
128) but never specifies WHERE in the file it goes. The example topic
(loss-aversion) does not include a Writer Scoring section at all --
it has the scoring recorded as frontmatter and metadata, not as a
body section. The example is inconsistent with the checklist.

### F3 -- Section naming is inconsistent (MINOR)

The template says `## Core Concepts` and `## Evidence`. Actual output:
- cognitive-biases uses `## Core Biases by Category` and
  `## Evidence and Research Foundation`
- Three others use `## Core Concepts` and `## Evidence` correctly.

**Root cause:** The template shows example section names but does not
state they are required names. The writer customized them to the topic
content, which is reasonable for readability but inconsistent with a
machine-verified format.

### F4 -- Extra sections are ungoverned (AMBIGUITY)

Two topics add `## Common Pitfalls`. One adds `## Practical Moat
Analysis Framework`. One adds `## Kuhn and Paradigm Shifts`. These
are substantively good additions -- Common Pitfalls in particular
adds value. But the template has no rule about where extra sections
go relative to the core four.

**Root cause:** The template implies the four sections are the
standard but does not forbid or position additional sections. The
body structure G2 check says "Body sections organized logically"
which permits both adding and reordering. This is too loose for
format reproducibility.

### F5 -- The example topic contradicts the checklist (STRUCTURAL)

The template example (loss-aversion, line 155+) has this structure:
Background, Core Concepts, Evidence, Implications, Sources, See Also.
It does NOT include a Writer Scoring section. But the pre-commit
checklist (line 128) requires "Writer scoring recorded: all 4
dimensions." The example violates its own checklist.

**Root cause:** The example was written before the Writer Scoring
section was added to the checklist, or was not updated when the
checklist was added. Either way, the reference implementation and
the specification disagree. This is the template-level equivalent
of the R8 duplication problem: the checklist says one thing, the
example shows another.

## Verdict

**APPROVE WITH CHANGES** -- the 4 topics are substantively excellent
and all 10 quality gates pass on content. The format inconsistencies
are caused by template ambiguity, not writer error. The template
needs 3 structural fixes to produce reproducible output.

## Required Changes

### Change 1: Mandate section ordering in template-library.md

Add a new gate G11 to the Quality Gates section:

```
- **G11 -- Body Structure Order:** The topic body follows this order
  after the opening paragraph: Background, Core Concepts, Evidence,
  Implications. These four sections are mandatory. Additional sections
  (Common Pitfalls, Writer Scoring, etc.) go between Implications and
  Sources. Sources must precede See Also. Writer Scoring must precede
  See Also. The exact required order: Title -> Opening Paragraph ->
  Background -> Core Concepts -> Evidence -> Implications ->
  (optional extra sections) -> Sources -> Writer Scoring -> See Also.
```

This is the structural fix. It specifies: (a) mandatory sections,
(b) mandatory order, (c) where extras go, (d) Sources/Writer
Scoring/See Also relative ordering.

### Change 2: Fix the example topic to include Writer Scoring

The loss-aversion example currently has: Sources -> See Also.
Fix it to: Sources -> Writer Scoring -> See Also, matching the
checklist requirement. The example is the reference implementation;
when it disagrees with the checklist, the checklist loses.

### Change 3: Add ordering gate to library-writer.md

The writer skill's Format Verification > Body Structure section
currently has:
```
- [ ] Body sections organized logically with ## headings (PASS / HALT)
```

Replace with:
```
- [ ] Body sections follow template order: Background -> Core Concepts
  -> Evidence -> Implications -> (extras) -> Sources -> Writer Scoring
  -> See Also (PASS / HALT)
```

This gives the writer a concrete checklist to verify against instead
of the subjective "logically."

### Change 4 (optional): Rename checklist item for precision

The template pre-commit checklist line 128 says:
```
- [ ] Writer scoring recorded: all 4 dimensions (core match, scope
  fit, knowledge value, source authority) scored with justifications
  (PASS / HALT)
```

Change to:
```
- [ ] Writer Scoring section present after Sources and before See Also:
  all 4 dimensions scored with justifications (PASS / HALT)
```

Adds position specification that was previously omitted.

## Not Changes Needed

Frontmatter is fine across all 4 topics. All 7 required fields present.
IDs are `date -u` generated, not rounded. ASCII clean. G1-G10 gates
pass on content. The issue is exclusively format consistency, not
content quality.

## Confidence

**High (90%).** The pattern is consistent across 4 independently
written topics: the writer follows the template's example structure
faithfully but adds sections organically. The deviations are not
random -- they follow a predictable pattern of adding substantively
useful content in ungoverned positions. This confirms the root cause
is template ambiguity, not writer unreliability. 10% reserved for
whether G11's mandatory ordering produces slightly more rigid but
auditor-parsable output at the cost of some organic flexibility.

## Cross-links

- `governance/template-library.md` -- the format specification being
  audited
- `governance/library-writer.md` -- the skill that produced these
  topics
- `research/evaluations/ava-library-writer-evaluation.md` -- prior
  evaluation of the first writer cycle
- `library/value-investing/margin-of-safety.md` -- topic 1
- `library/psychology-behavior/cognitive-biases.md` -- topic 2
- `library/science/scientific-method-falsifiability.md` -- topic 3
- `library/value-investing/economic-moats.md` -- topic 4
