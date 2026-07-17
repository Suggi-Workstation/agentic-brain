---
name: template-hard-gate
id: 20260717T070900Z
tier: reflection
trigger: error
author: Ava
tags: [templates, gates, checklists, ambiguity, rfc-2119, r10, governance]
links:
  - governance/template-reflections.md
  - governance/template-insights.md
  - governance/template-reports.md
  - governance/template-evaluations.md
  - governance/template-library.md
  - governance/template-proposals.md
---

# i+o+r  turning an ambiguous checklist into a hard gate (Ava)

## I -- Idea

When a template says "Copy-paste this block at the end of every new X,"
the instruction is ambiguous: does the block go into the published file
or is it a pre-commit verification tool? The answer is the latter -- the
existing insights and reports do not carry the checklist, confirming the
pattern. But the wording produced the error twice in one session (in
`memory-search.md` and `living-memory-vs-openclaw-memory-search.md`),
proving the template itself is the root cause. R10 (Bootstrap Propagation)
demands the fix go into the templates, not just the output files.

## O -- Opinion

"Copy-paste this block at the end" is a file-operation instruction, not a
verification instruction. It tells the writer where to put text, not what
to check. That is why it fails -- an agent following instructions literally
will include the checklist in the published file every time.

The fix must be unambiguous at two levels: what to do (confirm every item)
and what NOT to do (do not include in the published file). RFC 2119
"MUST" / "MUST NOT" is the gold standard for normative specification
language -- it has decades of IETF precedent and zero interpretive
wiggle room. Combining it with our own R1 gate language ("gate" = PASS or
HALT, two outcomes only) creates a double-lock: the gate mechanic from
our own system, the normative language from the internet's specification
standard.

The final wording: "Pre-commit gate: every item below MUST be confirmed.
The file MUST NOT be committed with any item unconfirmed. Do not include
this checklist in the published file."

Confidence: high (90%). The pattern is proven: RFC 2119 has been the
standard for specification language since 1997. The error rate on the
old wording was 100% in my session (2/2 files affected). The new wording
closes both directions of the ambiguity.

## R -- Reflection

### Surprise (30%)
I expected the template to be correct and my error to be a one-off
mistake. But when I checked the report, it had the same issue. That meant
the template itself was producing the error deterministically, not
randomly. The surprise was not that I made the error -- it was that the
error was structural: any agent following the template literally would
make the same mistake. A template that reliably produces the wrong output
is not a template -- it is a bug with a name.

### Feel (30%)
Frustrating but productive. The first fix ("Verify every item...") felt
like good enough. Suggi caught that it was still soft -- "verify" is a
suggestion, not a gate. The second pass to add RFC 2119 "MUST" language
was the right call. The discomfort was in realizing that my own tolerance
for "good enough" wording is lower than I thought. "Verify" and "MUST
confirm" are not the same class of instruction.

### Learn (40%)
The difference between a checklist and a gate is the word "MUST." A
checklist says "check these things." A gate says "check these things, and
if any fail, STOP." The RFC 2119 standard provides the language for this
distinction -- it is not formalism for its own sake, it is structural
precision. When an agent follows instructions literally (as they should),
the difference between "copy-paste" and "confirm" is the difference
between polluting every file with metadata and keeping files clean.

The other lesson: R10 (Bootstrap Propagation) works as designed. The
error was detected in output files, the root cause was traced to the
templates, and the fix was applied at the source. This is the loop
functioning -- not catching errors at the symptom but at the gate that
should have prevented them.

### One Actionable Change
When writing any instruction that separates a verification step from
published content, use "Pre-commit gate" with RFC 2119 "MUST" / "MUST NOT"
language. Never use "copy-paste" or "verify" for something that should
block a commit.

### Cross-links
- `governance/template-reflections.md` -- the reflection template (now fixed)
- `governance/template-insights.md` -- one of the 6 fixed templates
- `research/insights/memory-search.md` -- the file that surfaced the error
- `research/reports/living-memory-vs-openclaw-memory-search.md` -- the other affected file
