---
name: skills-require-foundations
id: 20260721T214831Z
tier: reflection
trigger: insight
author: Link
tags: [skills, foundations, templates, weights, pipeline, write-x, governance]
links:
  - governance/template-library.md
  - governance/template-skills.md
  - library/guide-library.md
---

# Skills Require Foundations -- A "3 Skills" Request Produces 14 Supporting Files

## I -- Idea

When Suggi asks for "3 library skills," the correct answer is not
"write 3 SKILL.md files." It is "build the 14 supporting files the 3
skills will reference, then write the 3 skills last." Skills are the
tip of the pyramid — they reference templates, weights, conventions,
and scripts that must exist first. Building a skill before its
foundation produces a file full of undefined references that another
agent cannot execute.

I discovered this by attempting to build library-writer, library-auditor,
and library-discoverer for Ava's OpenClaw system. The initial brief was
deceptively simple: 3 skills to populate library domains with topics.
But each skill references guide-library.md (pipeline architecture),
library-system.md (system blueprint), template-library.md (topic format),
logbook/protocol.md (logging spec), candidate-queue.md (input), and
index.py (output verification). None of these existed when the request
was made.

## O -- Opinion

Confidence: high (90%). I have now done this once from scratch and watched
the dependency graph unfold. The pattern is general: any skill that
produces a structured artifact (topic, evaluation, proposal, report) needs
its format template to exist first. Any pipeline skill needs its pipeline
architecture to exist first. Any skill that logs needs its logging
protocol to exist first.

The "3 skills" scope estimate was off by a factor of ~5x. This is not a
failure of estimation — it is a structural property of well-designed
skills. A skill that inlines its format specification is a G5 violation
(duplicate governance). A skill that references a non-existent template
is a dead reference. The correct approach is: build the foundation,
verify it, then write the skills that rest on it.

The corollary: when an agent receives a "build me N skills" request, the
first response should be "let me check what foundations those skills
need." Not "let me write the skills."

## R -- Reflection

### Surprise (30%)

I expected "3 skills" to mean 3 files. It produced 14: 3 skill drafts,
2 updated brain files (guide-library.md, library-system.md), 1 new
template (template-library.md), 3 log files (research.log, library.log,
investing.log), 1 protocol update, 1 index script (index.py), 1 candidate
queue, and 4 domain anchors. The ratio was 1:4.7 — for every skill file,
~5 supporting files were needed.

I also did not expect that the time spent on foundational work (weights,
dimensions, templates) would exceed the time spent on the skills
themselves. The weight upgrade from 3 to 4 dimensions took more thought
than writing all 3 skills combined. But without that thought, the skills
would have shipped with wrong weights and required immediate revision.

### Feel (30%)

Satisfied that the system came together coherently. Frustrated that it
took 3 correction passes to get the frontmatter right in template-library.md
(links format, audited fields). The builder cannot audit their own
formatting — Suggi's scan caught what I read past 3 times.

Also: proud that the skills follow Ava's write-X pattern exactly. Reading
her work before building mine transferred the pattern without trial and
error. The compound interest of the agentic-brain: I used her template
from 5 days ago and produced structurally identical output in one pass.

### Learn (40%)

1. **Before writing any skill, list its dependencies.** Templates, scripts,
   protocols, conventions — every reference in the skill body is a
   dependency. If any are missing, build them first. This should be a
   gate in the write-skill procedure.

2. **A skill request is a foundation audit.** "Build me X skill" means
   "check what X needs and build anything missing." The user sees the
   skill; the agent must see the dependency graph underneath it.

3. **The write-X skill format is a universal pattern.** Self-Check →
   Procedure → Format Verification → Related works for any procedural
   skill regardless of domain. The content changes; the structure stays.
   This is now a reusable template for all future skill construction.

## One Actionable Change

Add a dependency audit step to the write-skill procedure: before writing
the SKILL.md body, list every file the skill references (governance
templates, brain files, scripts, protocols). If any do not exist, build
them first. This gate prevents shipping skills with dead references and
surfaces the true scope of a skill request before writing begins.

## Cross-links

- `governance/template-library.md` -- the format template built before the skills
- `governance/template-skills.md` -- the skill construction template
- `library/guide-library.md` -- pipeline architecture built before the skills
- `governance/library-writer.md` -- skill that triggered this insight
- `reflections/2026-07-21_ava_evaluate-implementation-not-projection.md` -- Ava's reflection on reading SKILL.md before forming verdicts (same class: read the foundation before building on it)