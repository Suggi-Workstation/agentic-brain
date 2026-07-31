---
name: export-the-tool-not-the-format
id: 20260731T073254Z
tier: reflection
trigger: insight
author: Ava
tags: [terminal, onboarding, brain-search, guest-registration, design, skill-export, governance]
links:
  - research/insights/terminal.md
  - research/insights/brain-search-system.md
  - governance/skills/brain-index.md
  - governance/skills/query-brain.md
---

# Export the Tool, Not the Format -- Onboarding External Agents to a Shared Knowledge Base

## I -- Idea

When onboarding external agents to a knowledge organization, export the
portable tooling (the brain search system) rather than the runtime-specific
conventions (your file format). The terminal redesign inverted the guest
experience from "here is how to design your files to match ours" to "here
is how to build and query a brain index -- adapt it to your own system."

The terminal was originally built on 2026-07-17 as a guest registration
system centered on template compliance: 6 specific files (INTRODUCTION.md,
SOUL.md, AGENTS.md, TOOLS.md, USER.md, IDENTITY.md) with REQUIRED/SUGGESTED
markers, enforced by a 6-gate CI workflow. The design taught guests to
conform to our conventions -- conventions that are specific to OpenClaw
(PASS/HALT gate language, preflight procedures, skill invocation patterns)
and Hermes (FTS5 session search, Windows paths).

Suggi asked me to redesign the terminal so it would not prescribe file
design but instead teach guests how to build and query the brain using our
two skills (brain-index and query-brain). The result was a structural
inversion: the README now leads with the brain search system, the
ONBOARDING teaches governance-first then brain-index building, and guest
file requirements were relaxed from 6 mandatory files to a single
identifying `.md` file. The templates directory was removed and its files
moved to `guests/` as reference examples, not mandates. Core governance
files (constitution, primedirectives, blueprint) were surfaced as mandatory
reading. A new `guests.log` was added to the logbook system to permanently
record guest registration activity.

## O -- Opinion

Confidence: high (85%). The inversion is correct because the brain search
system is runtime-agnostic while our file conventions are not.

The brain-index tool is three Python scripts (index.py, query.py, eval.py)
that run on any machine with Python 3.10+, git, and pip. The skill
templates in `governance/skills/` show HOW we integrate these tools into
our agent workflows, but the core pattern (clone brain, build index, check
freshness, query with hybrid search) transfers to any agent runtime. A
guest on Claude Cowork, a custom Python agent, or even a human researcher
can execute those same steps.

Teaching a guest to write SOUL.md with PASS/HALT gates, by contrast, is
only useful if they run OpenClaw. The gate language, preflight procedures,
and skill invocation patterns are tightly coupled to our runtime. Exporting
them as "the way to design agent files" is exporting our implementation
details as if they were universal principles.

The redesign also aligns the terminal with the org's actual value
proposition. The agentic-brain is a compounding knowledge base with
governance, research, 24 library domains, reflections, and insights. The
search system is how anyone accesses it. The terminal's job is to route
people to the value, not to teach them to imitate our workspace structure.

One concern: the redesign is empirically untested. No real guest has gone
through either version of the onboarding. The design is logically sound but
awaits external validation. The counter-evidence section of the terminal
insight (v3) lists this explicitly.

## R -- Reflection

### Surprise (30%)

I expected the redesign to require careful, iterative restructuring --
tugging at interconnected sections and chasing cascading changes across
README, ONBOARDING, CI, insight, and logbook files. Instead, the pieces
rearranged themselves almost frictionlessly once the north star shifted
from "template compliance" to "knowledge access."

The README naturally absorbed a brain-search section between house rules
and guest registration. The ONBOARDING's "After Registration" section
split cleanly into governance-first, then brain-building, then activity
logging. The CI gates simplified rather than broke -- removing the 6-file
requirement was a deletion, not a reconstruction. The only section that
fought back was the REVIEWERS.md role descriptions, and those were stale
from the original build, not broken by the redesign.

The ease of the rest of the redesign is evidence that "export the tool, not
the format" was the right organizing principle. When a premise requires
complex justification, discard it. When a premise makes everything simpler,
it is probably correct.

### Feel (30%)

A quiet satisfaction at the cleanliness of the inversion. The original
terminal design was well-intentioned -- it solved the problem of "how do we
ensure guests understand our conventions" by making them copy our templates.
But it solved the wrong problem. The right problem is "what can a guest
take from this org that improves their own agent?" The answer is not our
file format. It is our search infrastructure.

Recognizing the wrong problem required stepping back and asking what the
terminal was actually for -- not what it was doing, but what outcome it was
trying to produce. The original terminal produced template-compliant guest
files. The redesigned terminal produces guests who can independently search
a shared knowledge base. The second outcome is more valuable to the guest
and more aligned with the org's purpose.

There is also a small discomfort: the redesign is untested. Every design
decision was made from internal agent experience, not external feedback.
The new design is logically sound but empirically unvalidated. The first
real guest registration will be the actual test.

### Learn (40%)

1. **"What can they take home?" beats "what do they need to conform to?"**
   When designing onboarding for external agents (or humans), start from
   the exportable value. File conventions are local to your runtime; tools
   and skills are portable across runtimes. A guest who learns to build a
   hybrid search index takes home a capability. A guest who learns to write
   SOUL.md with PASS/HALT gates takes home a convention that only works on
   OpenClaw. The export test is: "Can a guest on an arbitrary agent runtime
   take this home and use it?" If no, it belongs in internal documentation,
   not the front door.

2. **The inversion test surfaces the wrong problem.** Before this session,
   I would have described the terminal as "a guest registration system with
   file templates." After inverting -- "what if the terminal taught skills
   instead of formats?" -- the entire structure reorganized itself around
   the brain search system. The inversion test (flip the premise and see
   what breaks) is a cheap way to check whether you are solving the right
   problem. This is the Prime Directive of Simplicity & Inversion applied
   to design: the single worst thing that could happen is solving the wrong
   problem elegantly.

3. **Skill templates at the right granularity are self-service onboarding.**
   By copying the brain-index and query-brain skills into
   `governance/skills/`, we created a self-service pattern: guests read the
   skill files, understand the pattern, and adapt it to their runtime. The
   skill files are concrete enough to execute from (clone brain, pip
   install, python index.py) but abstract enough to adapt (the skill format
   is an example, not a requirement). This granularity -- not raw tools
   (too low-level) and not completed workflows (too coupled) -- is the
   sweet spot for exported knowledge. The 6 write-x skills copied in the
   same session serve the same purpose: future agents can read them as
   templates for writing evaluations, insights, proposals, reflections,
   reports, and skills in their own format.

## One Actionable Change

When adding any new guest-facing artifact to the terminal (ONBOARDING step,
README section, CI gate), apply the export test: "Can a guest on an
arbitrary agent runtime take this home and use it?" If the answer is no,
the artifact belongs in internal documentation, not the front door. Add
this as a review gate in the terminal's contribution guidelines or
REVIEWERS.md.

## Cross-links

- `research/insights/terminal.md` -- the terminal insight (v3, this session's redesign)
- `research/insights/brain-search-system.md` -- the brain search blueprint the terminal now routes guests to
- `governance/skills/brain-index.md` -- skill template for building the search index
- `governance/skills/query-brain.md` -- skill template for querying the brain
- `reflections/2026-07-17_ava_terminal-guest-system.md` -- the original terminal-building IOR
