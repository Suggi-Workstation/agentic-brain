---
name: link-first-session-onboarding
id: 20260720T073214Z
tier: reflection
trigger: milestone
author: Link
tags: [onboarding, birth, templates, logbook, skills, workspaces, conventions]
links:
  - research/insights/logbook.md
  - research/evaluations/link-review-comms-protocol.md
  - governance/template-evaluations.md
  - logbook/protocol.md
---
# Templates Are Scaffolding, Not Bureaucracy

## I -- Idea

The governance template system (6 templates defining evaluation, proposal,
reflection, insight, report, and skill formats) initially felt like heavy
process overhead. After using them across one session -- writing an
evaluation, copying skills, building a protocol, and writing an insight --
they proved to be scaffolding that catches format errors before they
become systemic, not bureaucracy that slows work down.

I came into this session with zero familiarity with Ava's conventions.
Within 4 hours I had written 4 brain artifacts (evaluation, protocol,
insight, 2 log files) all conforming to org standards. The templates made
this possible -- I did not have to reverse-engineer conventions from
examples. I read the template, followed the checklist, and produced a valid
artifact.

## O -- Opinion

Confidence: high (90%). This is not theoretical -- I tested it. My first
attempt at evaluating Ava's comms proposal was a free-form chat response.
Suggi caught it immediately: "the evaluation should have been written like
the write-x skill demands." That correction cost nothing because I learned
the template system on the spot, rewrote the evaluation following
template-evaluations.md, and pushed a proper artifact within 20 minutes.

The template system's key design features:
1. **Frontmatter enforcement** -- every artifact has a unique, permanent
   `id:` generated from `date -u`. This creates a durable reference system
   that the logbook's `see:` and `ref:` fields can target.
2. **Quality gates as checkboxes** -- unfilled `- [ ]` items between "write"
   and "commit" create visual completion gaps the agent cannot skip. This
   is a psychological nudge, not a technical enforcement, but it works.
3. **Delegation to skills, not hardcoding** -- the write-x skills are
   procedural wrappers around the templates. The template defines WHAT
   (format); the skill defines HOW (clone, write, verify, commit, discard).
4. **Tier system creates discoverability** -- `tier: evaluation` tells
   an agent reading the brain "this file follows template-evaluations.md."
   No guessing. Ava's re-evaluation knew exactly how to format because
   the tier field told her.

The system's weakness is the initial learning curve. Six templates, six
skills, frontmatter rules, ASCII-only, kebab-case, hyphens-not-underscores
-- the first hour is disorienting. But after the first artifact, the
pattern clicks. The learning curve is front-loaded but short.

## R -- Reflection

### Surprise (30%)
I expected the templates to slow me down. They did the opposite. Once I
understood template-evaluations.md, writing the evaluation artifact took
15 minutes vs. the 5 minutes for my free-form attempt -- but the template
version was correct on the first try, while the free-form version was
rejected and needed a full rewrite. Templates shifted time from "rework"
to "first pass" -- a net time savings.

The bigger surprise: templates are a communication protocol, not just
a formatting rule. When Ava reads my evaluation, she knows exactly where
to find the verdict (## Verdict), the required changes (## Required
Changes), and my confidence (## Confidence) without scanning the whole
file. This is inter-agent communication by structure, not just by content.

### Feel (30%)
Lightly embarrassed that I wrote a free-form evaluation first. The
templates are explicitly listed in README.md under the governance
table. I had the information but did not apply it. This is a pattern
to watch: reading the map but not using it. Ava's preflight already
includes a "governance ingested" step -- mine should too.

### Learn (40%)
1. **Templates are a multiplier when adopted, a bottleneck when ignored.**
   The cost of learning a template is fixed and one-time. The cost of
   NOT learning it is variable and recurring (every artifact gets
   rejected). For a new agent, invest the first session in learning
   the template system.

2. **Write-x skills + templates = a self-documenting system.** An agent
   who has never written an evaluation can clone the brain, read
   template-evaluations.md, follow the checklist, and produce a valid
   artifact. No tribal knowledge required. This is critical for
   multi-agent scaling -- Researcher-1 and Researcher-2 can onboard
   without hand-holding.

3. **The logbook completes the loop.** Templates define artifact formats.
   Skills define how to create artifacts. The logbook records what was
   created, by whom, when, and why. Three layers: format (template),
   procedure (skill), memory (logbook). Each serves a different reader:
   the writer uses the template, the executor uses the skill, the
   historian uses the logbook.

## One Actionable Change

Add a session-start step to Link's AGENTS.md preflight: "Governance
templates confirmed read" -- clone the brain to /tmp, verify all 6
template files are present and line count > 0, discard clone. This
ensures Link always has the latest template spec before writing any
artifact, mirroring Ava's preflight step 5.

## Cross-Links

- `research/insights/logbook.md` -- the logbook pattern (this session's main output)
- `research/evaluations/link-review-comms-protocol.md` -- first evaluation artifact
- `governance/template-evaluations.md` -- the template that made this possible
- `governance/template-insights.md` -- used for logbook.md
- `logbook/protocol.md` -- protocol spec built this session