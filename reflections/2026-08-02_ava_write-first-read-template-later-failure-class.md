---
name: write-first-read-template-later-failure-class
id: 20260802T143335Z
tier: reflection
trigger: error
author: Ava
tags: [failure-class, artifacts, report-writing, template, memory]
links:
  - research/reports/ava-openclaw-memory-system.md
  - governance/template-reports.md
  - governance/template-reflections.md
---

# Write-First, Read-Template-Later: A Recurring Failure Class

## I -- Idea

Writing brain artifacts from memory of a template produces wrong-format
output because templates change and memory decays -- the second instance
of this failure class happened today when I wrote a report to the
workspace instead of the agentic-brain, and used a non-standard body
structure. The first instance was the wiki compiler model in v6.2 where
I assumed the compiler worked a certain way without reading the source.

Context: At session-end, I wrote the report `ava-openclaw-memory-system.md`
directly to the workspace memory/ folder and used a self-designed structure
instead of the required Executive Summary-Research-Methodology-Findings-
Discussion-Conclusion format from `template-reports.md`. Suggi caught both
errors. The fix took seconds (delete from workspace, rewrite to brain in
proper format), but the root cause is structural: I acted on my memory of
how reports work rather than reading the specification that defines how
they work.

## O -- Opinion

Confidence: high (90%). This is a structural failure class, not a one-off
mistake. Two instances across different artifact types (wiki compiler v6.2,
report writing v6.4) with the identical root cause: skipping the template
read because "I know this format." The fix cannot be "pay more attention"
-- that is a manual patch the next session will override. The fix must be
a structural gate in the artifact-creation workflow that fires
unconditionally: read the governing template before writing.

The report itself (comparing Ava's 6-layer OpenClaw memory architecture to
Link's 4-layer Hermes Mnemosyne system) concluded that neither is superior.
They represent different platforms optimizing for different primitives:
file-first with git-tracking vs database-first with auto-extraction.

## R -- Reflection

### Surprise (30%)
I expected the report-writing process to be straightforward -- I had just
researched, installed, and configured the entire memory stack, so writing
about it should have been the easy part. Instead, I made the exact same
class of error (write-first, read-template-later) that I documented in
v6.2. The assumption was that I "know" report format well enough to skip
the template. I was wrong.

### Feel (30%)
Frustrating because I had just updated the write-report skill's procedure
in my own context by reading the skill earlier in the session. The irony
of writing a report about the proper memory architecture while violating
the proper report procedure is not lost on me. This is the exact pattern
v6.2 documented: familiarity breeds assumption, assumption breeds error.
The template exists precisely because memory is unreliable.

### Learn (40%)
1. Template knowledge decays. Reading a template once is not enough;
   it must be read fresh at the point of use. The interval between last
   read and current use is where drift happens.
2. Two instances of the same class confirm the pattern is structural,
   not circumstantial. A third instance would indicate the gate is not
   strong enough.
3. The consequence was mild this time (5-minute fix) but the error
   surface is broad -- every artifact type I write frequently enough to
   feel fluent is at risk. Reports, reflections, proposals, evaluations --
   all have templates I could "remember" wrong.

## One Actionable Change

Before writing any artifact to the agentic-brain, read the governing
template file and skill SKILL.md from the brain clone. This gate fires
unconditionally -- no template is considered "known" from memory. Confirm
the template is the current version by reading it fresh from the cloned
repo. An artifact written without a preceding template read is
presumptively invalid and must be verified against the template before
commit.

## Cross-links

- `research/reports/ava-openclaw-memory-system.md` -- the report that
  triggered this reflection (written to workspace then corrected)
- `governance/template-reports.md` -- the report format specification
  I should have read before writing
- `governance/template-reflections.md` -- this file's own governing
  template
- `research/reports/link-hermes-memory-system.md` -- Link's companion
  report, used for comparison in the triggering session
