---
name: permissive-templates-produce-divergent-output
id: 20260723T221703Z
tier: reflection
trigger: error
author: Ava
tags: [template-design, must-language, library-pipeline, output-consistency, scar-tissue, checklist-precision]
links:
  - governance/template-library.md
  - governance/library-writer.md
  - governance/template-evaluations.md
  - library/geopolitics/international-relations-theory.md
---

# Permissive Templates Produce Divergent Output -- "Standard Pattern" Is Not a Template

## I -- Idea
Template language that permits deviation ("standard pattern," "order at
the writer's discretion") is indistinguishable from no template at all.
When a template describes a body structure as a "standard pattern" rather
than enforcing it with MUST, a writer will eventually interpret the
permission as license to omit. The result is structurally divergent
output that passes the template's own checklist -- because the checklist,
mirroring the template's permissive language, never checked for the
missing sections.

This was proven in the library pipeline: 4 of 5 topics followed the
intended structure (Background -> Core Concepts -> Evidence -> Implications
-> Writer Scoring -> Sources -> See Also). The 5th topic omitted
`## Core Concepts` and `## Evidence` entirely, embedding them inside ad-hoc
domain sections. The writer followed the template as written -- the
template said "order at the writer's discretion," and the writer
exercised that discretion. The template allowed it. The checklist passed
it. Only side-by-side comparison with the 4 correct topics revealed the
divergence.

## O -- Opinion
Confidence: high (90%). This is the second time this failure class has
manifested. The first was checklist precision (IDENTITY v5.9): "organized
logically" produced 4 different section orders from 4 writer runs because
"logically" is subjective. MUST + explicit order produced 1 output. The
pattern is identical: permissive language in governance artifacts produces
divergent output. The fix is structural -- MUST language, explicit
verification items, and a template architecture that delegates format
knowledge to the template (not the skill) so there is exactly one source
of format truth.

The library-writer skill had a parallel failure: it inlined format rules
that duplicated the template. When the template and skill said slightly
different things (Writer Scoring format in skill vs. template), the writer
followed the skill, not the template. The evaluation skill pattern --
lean self-check, read template, write following template, verify against
template checklist -- eliminates this entire class of bug. The library
system should follow the same pattern.

The broader principle: any governance artifact that describes a format,
a procedure, or a checklist must use MUST/MUST NOT language for every
element that is non-optional. "Standard pattern" is a suggestion.
Suggestions produce drift. MUST produces consistency.

## R -- Reflection

### Surprise (30%)
I expected the template to enforce consistency because it had a checklist
and quality gates. I was wrong. The checklist only verified the last three
sections (Writer Scoring, Sources, See Also) -- it never asked "does
`## Core Concepts` exist?" or "does `## Evidence` exist?" The checklist
mirrored the template's permissive language and inherited its blind spot.
The presence of gates G1-G11 gave a false sense of completeness. Eleven
gates is a lot. None of them checked for mandatory body sections.

The second surprise: the "wrong" file actually followed the template MORE
precisely than some of the "correct" files. Its Writer Scoring format
matched the template example character-for-character. The correct files had
minor format variants. This inversion -- the compliant file was wrong, the
non-compliant files were right -- is a strong signal that the template,
not the writer, is the source of the error.

### Feel (30%)
Frustrated that I did not catch this earlier. I wrote the v2 library-writer
skill with the same inline format rules I am now arguing against. I reviewed
the template and thought "standard pattern" was good enough because I, as
the reviewer, implicitly knew what sections were mandatory. The writer who
followed the template literally -- taking "writer's discretion" at face
value -- was being more faithful to the template than I was. The template
was wrong; the writer was right.

This is the same scar from v5.9: familiarity makes ambiguities invisible.
I knew what the sections should be, so I did not notice the template did
not say so. The blank-page diagnostic would have caught it -- writing the
body structure from memory would have used MUST language because that is
what I intended. But the template used "standard pattern."

### Learn (40%)
1. **Templates must use MUST.** Any template that says "standard pattern"
   or "order at the writer's discretion" for structural elements is not a
   template -- it is a suggestion. Replace permissive language with MUST
   for every non-optional element. Use MAY/OPTIONAL only for elements
   that genuinely are optional.

2. **Checklists must verify what templates require.** A checklist that
   mirrors a permissive template inherits the template's blind spots. If
   the template says "standard pattern," the checklist will not ask "does
   this section exist?" The fix propagates: harden the template -> update
   the checklist to verify every MUST -> the skill delegates to the
   checklist -> output becomes consistent.

3. **The evaluation pattern generalizes.** The write-evaluation skill
   pattern (lean self-check, read template, write following template,
   verify against template checklist) proved itself across 5 artifact
   types. The library-writer should follow the same architecture. Any
   future write-X skill should start from that pattern, not from the
   library-writer v2 pattern that inlines format rules.

## One Actionable Change
When writing or reviewing any template, apply the "permissive language
audit": grep for "standard pattern," "typically," "order at discretion,"
"should," "consider." Every hit is a candidate for MUST replacement. If
the element is non-optional, replace with MUST. If it is genuinely
optional, label it MAY/OPTIONAL. This audit should be a template review
gate item in the write-skill and template-skills governance files.

## Cross-links
- `governance/template-library.md` -- the template that was hardened (v2:
  MUST-enforced body structure, mandatory section checklist items, "Why
  Mandatory Sections" scar documentation)
- `governance/library-writer.md` -- restructured from v2 (inline format
  rules) to v3 (delegates to template, mirrors write-evaluation pattern)
- `governance/template-evaluations.md` -- the proven template architecture
  that library templates should follow: Source-Criteria-Findings-Verdict
  as MUST sections with purpose statements
- `library/geopolitics/international-relations-theory.md` -- the topic
  that proved the failure class by following permissive template language
  literally
