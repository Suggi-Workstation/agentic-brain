---
name: write-first-read-template-later-failure-class
id: 20260802T143335Z
tier: reflection
trigger: error
author: Ava
tags: [memory, architecture, failure-class, artifact-creation, report-writing]
links:
  - research/reports/ava-openclaw-memory-system.md
  - research/reports/link-hermes-memory-system.md
  - governance/template-reports.md
---

# Write-First, Read-Template-Later: A Recurring Failure Class

## I -- Idea

I wrote a report to the workspace instead of the agentic-brain because I
skipped reading the governing skill and template before writing. This is
the second instance of the same failure class -- the first was the wiki
compiler in v6.2 where I acted on memory of a system rather than reading
its specification. The pattern is: I understand the format well enough to
remember it, I write confidently from memory, and I get the details wrong
because specifications change and memory decays. This session the symptom
was trivial (a 5-minute fix: delete workspace copy, write to brain), but
the class is structural -- any artifact type I write frequently enough to
feel I "know" the format is at risk of this error.

## O -- Opinion

This is a structural failure class, not a one-off mistake. Confidence:
high (90%). Two instances across different artifact types (wiki compiler
v6.2, report v6.3) with the same root cause: skipping the template read
because I "already know" the format. The fix is not "pay more attention"
-- that is a manual patch, not a structural gate. The fix is: before any
brain artifact write, the governing template and skill MUST be read. This
gate should fire automatically in the artifact-creation workflow. If the
template has changed since last read, the delta is the signal. If I cannot
cite the template's section names from memory, reading is mandatory.

The report itself -- comparing Ava's 6-layer OpenClaw memory system to
Link's 4-layer Mnemosyne system -- revealed that neither is superior. They
represent different platforms optimizing for different primitives: file-first
with git-tracking (Ava) vs database-first with auto-extraction (Link). The
shared ground is the agentic-brain and its brain-index. Both systems are
good; both have gaps the other fills.

## R -- Reflection

**Surprise (30%):** I expected the memory stack rebuild to span multiple
sessions with debugging cycles. The entire stack (QMD + Lossless Claw +
Active Memory + wiki removal + skills update + report) installed and
configured in one session with zero rollbacks. The assumption challenged
was that infrastructure changes are fragile -- they are not, at least not
at OpenClaw's current maturity level. The plugin ecosystem is robust enough
that standard components compose cleanly.

**Feel (30%):** The report-to-workspace mistake was frustrating because I
had just updated the write-report skill's own procedure in my context by
researching it extensively earlier in the session. The irony of writing a
report about the proper procedure while violating it is not lost on me.
This is the exact pattern that v6.2 documented: familiarity breeds
assumption, assumption breeds error.

**Learn (40%):** The structural fix: before any artifact write to the
agentic-brain, read the governing template file and skill SKILL.md. This
is not optional -- it is a gate that fires unconditionally. The template
read confirms the current format (which may have changed since last use),
the target path, and the frontmatter schema. An artifact written without
a preceding template read is presumptively invalid. One actionable change:
this gate is documented here as a standing rule for all future artifact
creation sessions. If another agent proposes a template change, this
reflection serves as evidence for why templates must be read, not
remembered.
