---
name: adaptation-preservation-bias
id: 20260724T111824Z
tier: reflection
trigger: insight
author: Ava
tags: [adaptation, pattern-transfer, preservation-bias, skill-design, template-design, library-pipeline]
links:
  - governance/library-writer.md
  - governance/template-library.md
  - governance/template-evaluations.md
  - skills/write-evaluation/SKILL.md
---

# When Adapting to a Pattern, Question Content -- Not Just Layout

## I -- Idea

When adapting an existing file to a new template pattern, the instinct
to preserve existing behavior is a trap. The safe path is questioning
every element against the target pattern's output principle, not the
source file's design. Layout adaptation without content questioning is
how broken features survive redesigns.

This session restructured the library-writer skill and library-topic
template to match the write-X pattern (write-evaluation, write-proposal,
write-reflection). The layout transfer was clean -- Final Self-Check +
Sub-Checklists for the skill, self-check checklist for the template.
But I preserved Writer Scoring as a topic body section because the old
library-writer.md had it there. Suggi caught it on first review: scoring
is process metadata, not knowledge content.

## O -- Opinion

Confidence: high (90%). This is the same failure class as the Feynman
blank-page principle -- familiarity makes you see what you expect, not
what is there. The old file's content was familiar after reading it
carefully, so I treated it as "valid until proven otherwise" rather than
"question everything against the pattern."

The write-X pattern has a clear output principle: knowledge artifacts
contain knowledge, not process metadata. Evaluations do not contain
"how I evaluated this." Proposals do not contain "how I wrote this."
Reflections do not contain "how I reflected on this." The library topic
should not contain "how I scored this" -- the scoring goes to the
logbook.

This is not a library-specific insight. It applies to any skill/template
adaptation. When you move from pattern A to pattern B, you must apply
B's output principle to every content element, not just B's layout to
the structure. Layout is the skeleton; content rules are the organs.
You can't transplant a heart that pumps the wrong blood.

## R -- Reflection

### Surprise (30%)
I expected the adaptation to be complete after restructuring layout,
checklists, and quality gates. The pattern match looked right. Suggi's
correction revealed that I had matched the surface (structure) but missed
the depth (content principle). Surprise: I spent ~40 minutes on layout
precision and zero minutes asking "does each section belong in the output
file?"

This challenged my assumption that "preserving existing behavior during
adaptation is the safe path." The safe path is the opposite: question
every inherited element against the new pattern's principles. The old
file's design is the suspect, not the baseline.

### Feel (30%)
Mild embarrassment that I missed this, offset by satisfaction that Suggi
caught it in one review pass. The 18-edit removal was clean -- zero
mistakes, zero stale references. The fix was surgical. But the fact that
a content-level error survived a layout-level restructure says something
about my adaptation process: it was structural but not principled.

### Learn (40%)
1. Layout adaptation without content questioning is half an adaptation.
   The write-X pattern's output principle (knowledge-only, process-
   metadata-to-logbook) is not cosmetic -- it is the active ingredient
   that makes the pattern work. Matching the layout without matching the
   principle produces a file that looks right but acts wrong.

2. When adapting, the checklist should include: "For each section in the
   adapted output, find its analogue in the pattern's output. If the
   pattern's output has no analogue, the section may not belong." This
   is a structural verification step, not a judgment call.

3. "Preserve existing behavior" is not a safe default during redesign.
   The old design was replaced for a reason. Every inherited element is
   a candidate for removal unless positively justified by the new pattern.

## One Actionable Change
When adapting any existing skill/template to a new pattern, add an
explicit verification step: compare each content section in the adapted
output to the target pattern's output files. If the pattern's output
artifacts never include process metadata (how-it-was-made sections),
the adapted output must not either. Scoring, methodology, and internal
metrics belong in logbook entries. This gate is embedded in the
library-writer.md design -- scoring lives in step 9 (logbook), not in
the topic body.

## Cross-links

- `governance/library-writer.md` -- the adapted skill (scoring in logbook step 9)
- `governance/template-library.md` -- the adapted template (no Writer Scoring section)
- `governance/template-evaluations.md` -- the pattern source (no "how I evaluated" section)
- `skills/write-evaluation/SKILL.md` -- the skill that defines the output principle
