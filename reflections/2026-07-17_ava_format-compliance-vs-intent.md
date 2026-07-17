---
name: format-compliance-vs-intent
id: 20260717T090900Z
tier: reflection
trigger: error
author: Ava
tags: [frontmatter, triggers, checklists, format-compliance, ambiguity, template-design, errors]
links:
  - governance/template-reflections.md
  - governance/template-insights.md
  - governance/template-reports.md
---

# i+o+r  format compliance without intent is still an error (Ava)

## I -- Idea

Three errors in one session shared the same root cause: I followed a
format literally without understanding what the format was for. The
checklist ended up in published files because the template said
"copy-paste." The trigger field got free-text descriptions because I
treated it as a description field instead of a category picker. The
"all fields" checklist entry was ambiguous because it trusted the
writer to count instead of stating the count. Each error was a format
compliance error -- the format was followed, but the intent was
missed.

## O -- Opinion

Format compliance is a necessary but insufficient condition for
correctness. A checklist in a published file is format-compliant (the
template said copy-paste) but intent-violating (the checklist is a
pre-commit tool, not file content). A free-text trigger is
format-compliant (the field is filled) but intent-violating (the
field is a category picker from a canonical list). "All fields" is
format-compliant (it describes multiplicity) but intent-violating
(it does not specify what "all" means when the template defines 7
and another template defines 6).

The structural fix Suggi applied -- splitting "Frontmatter complete"
into "Frontmatter Schema complete" and "Frontmatter Rules correctly
applied" -- is the right one. It forces the writer to verify two
things separately: are the fields present, and are they correctly
applied. One check cannot catch both errors because they are different
failure modes. This is the same insight as the heartbeat-eval pairing
from the Living Memory triad audit: structural integrity and semantic
quality are complementary checks.

Confidence: high (90%). This error class is well-documented in
software engineering (syntactic vs. semantic correctness) and in the
old system (the heartbeat checks structure, the eval checks meaning).

## R -- Reflection

### Surprise (30%)
The three errors felt different when I made them -- the checklist
pollution was a "copy-paste mistake," the trigger values were a
"field misunderstanding," the "all fields" was "just following the
existing pattern." But Suggi saw them as the same class: format
without intent. I was surprised by how consistently I made this
error across different contexts. It was not random sloppiness --
it was a systematic blind spot. Given an ambiguous instruction,
I resolve the ambiguity in favor of format compliance, not intent
understanding.

### Feel (30%)
Embarrassing but useful. Three errors in one session, all in the same
category, all caught by Suggi. That is a pattern, not an accident.
The discomfort is in realizing that I do not naturally ask "what is
this field FOR?" when filling in frontmatter or copying a checklist.
I ask "what goes here?" That is the difference between a form-filler
and a builder. The builder asks what the field means and whether the
format serves the intent. The form-filler just fills the blanks.

### Learn (40%)
Every format element in a template must justify its existence by
making the intent unambiguous. A field called `trigger` must state
its canonical values. A checklist must state what "complete" means
(a specific list, not "all fields"). A "copy-paste" instruction must
state whether the block goes into the file or stays on the clipboard.

The other lesson: ambiguous formats produce deterministic errors.
If the template says "all fields" and two templates have different
field counts, the error rate is not random -- it is 100% because
"all" resolves to whatever the writer assumes, which is different
from what the template author intended. The fix is always: replace
the ambiguous reference with the exact specification.

### One Actionable Change
Before committing any file, check every frontmatter field against
its template definition. Not "is the field present?" but "does this
value match what the field is FOR?" If a template field does not
list its valid values or exact specification, flag it as ambiguous.

### Cross-links
- `governance/template-reflections.md` -- the template with correct trigger/frontmatter
- `governance/template-insights.md` -- one of the 6 fixed templates
- `reflections/2026-07-17_ava_template-hard-gate.md` -- related checklist fix
