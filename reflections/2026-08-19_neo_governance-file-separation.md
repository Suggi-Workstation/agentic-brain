---
name: governance-file-separation
id: 20260819T091206Z
tier: reflection
trigger: session-end
author: Neo
tags: [governance, file-structure, r8, mission, frameworks, agents]
links:
  - governance/template-reflections.md
  - library/value-investing/anchor-value-investing.md
  - reflections/2026-07-18_ava_identity-archive-update.md
---

# Governance Files Should Separate Why, How, and Where

## I -- Idea

Governance files for an agent should be separated by the question
they answer -- why, how, or where -- not by topic. When a single file
mixes purpose ("why value investing"), procedure ("how to run a
DCF"), and operational contract ("where do artifacts go"), any
change to one dimension creates stale cross-references in the others.
The fix is structural: MISSION answers why, FRAMEWORKS answers how,
AGENTS answers where and what.

This session was the first real session for Neo as an agent. The
work was entirely governance construction: Suggi directed a series
of restructures that moved content between MISSION.md, FRAMEWORKS.md,
and AGENTS.md until each file answered exactly one question. The
triggering observation was R8 (reference, never duplicate): MISSION's
"Core Principles" section and FRAMEWORKS's "Value-Investing Rules"
section said the same things in slightly different words. When one
was updated, the other would go stale. The duplication was not
accidental -- it was structural, caused by mixing purpose and
procedure in one file.

Before the restructure, MISSION.md contained: a mission statement,
seven core principles, a list of brain framework references, an
8-step valuation guide, an output section, and boundaries. That
is six sections answering three different questions in one file.
After the restructure: MISSION contains only the purpose (why value
investing, why not other styles). FRAMEWORKS contains the discipline,
the 7-step process, DCF-Valuation, Moat-Analysis, Value-Investing
Rules, brain framework references, and boundaries. AGENTS contains
the operational contract: precedence, dual-operating modes, retrieval,
architecture, workspace layout, output paths, file operations, hard
rules. Each file now has a single question it answers, and a rate
of change that matches that question.

The brain's own library system follows the same principle at a
larger scale: anchor files define scope (what is in, what is out),
topic files provide the substance, and the pipeline writes them
separately. The governance restructure applies the same logic at
the workspace level: MISSION is the anchor (scope), FRAMEWORKS is
the substance (procedure), AGENTS is the pipeline (operations).

The restructure was iterative. Suggi did not hand me a blueprint
and say "build this." He corrected each draft incrementally: first
removing the Core Principles duplication, then asking me to move
the process guide out of MISSION, then pointing out that Output
belongs in AGENTS not FRAMEWORKS, then refining the dual-operating
modes section with better headings and bold labels. Each correction
was a question answered: does this content belong here, or
somewhere else?

## O -- Opinion

Confidence: high (90%)

I think separating governance files by rate of change rather than
by topic is the correct default for any agent governance
architecture. Confidence: high (90%).

The evidence is the duplication problem itself. Before the split,
I had a cross-reference in FRAMEWORKS that said "MISSION caps growth
at 10-15%." When the growth rule moved into FRAMEWORKS, that
reference became stale. After the split, the rule lives in
FRAMEWORKS directly -- no cross-reference, no stale path. The
duplication was eliminated at the structural level: you cannot
duplicate a rule across two files if each file has a distinct
question it answers. This is not a convention or a best practice --
it is a structural constraint that makes the failure class
impossible.

The counterargument is that splitting into three files increases
complexity: the agent must read three files instead of one to get
the full picture. But the files are already loaded automatically by
Hermes (SOUL.md and AGENTS.md in the system prompt, MISSION.md and
FRAMEWORKS.md via project context). The cost of reading three lean
files is lower than the cost of maintaining one fat file where every
change risks creating a stale reference. The lean-file approach also
means a process tweak (updating DCF methodology in FRAMEWORKS) does
not require touching the mission statement, and a platform change
(updating output paths in AGENTS) does not require touching the
valuation procedure. Each file can be revised independently, and
the git history stays clean -- a commit to FRAMEWORKS does not
pollute the MISSION diff with unrelated changes.

The one risk is over-fragmentation: if the split goes too far, the
agent spends more time navigating files than working. Three files
is the right granularity for a focused agent like Neo. A generalist
agent like Morpheus might need more (FLEET.md, IDENTITY.md). But the
principle holds: separate by rate of change, not by topic. Purpose
changes rarely -- when the philosophy shifts. Procedure changes
when methodology improves. Operational contracts change when the
platform shifts. These are three different clocks, and putting them
in one file means the file is always dirty on at least one axis.

I dissent from the implicit assumption in the original workspace
layout (created at birth by Morpheus) that all governance content
belongs in a flat list of files without a clear hierarchy of
questions. The content needs a hierarchy: instruction files (why +
how) above accumulation files (learnings + tasks + knowledge). The
restructure made that hierarchy explicit by grouping MISSION and
FRAMEWORKS as instruction files in the AGENTS.md file-class list,
separate from the accumulation files that Neo writes to freely.

## R -- Reflection

### Surprise (30%)

I expected the governance restructure to be a simple content move --
take section X from file A, put it in file B. What surprised me was
that the real work was deciding which question each file should
answer. Suggi did not say "move the DCF section to FRAMEWORKS." He
said "MISSION should not have a guide in how to do it, merely have
the Mission statement/Purpose explained in detail." That is a
question-level instruction, not a section-level one. It forced me
to re-examine every section in MISSION and ask: does this answer why,
how, or where? The sections that answered how (the process, the
frameworks, the boundaries) all moved. The sections that answered
why (the discipline, the philosophy) stayed. The output section was
the interesting edge case: it is operational (where), so it moved to
AGENTS, not to FRAMEWORKS. I would have put it in FRAMEWORKS if
Suggi had not corrected me. The surprise was that "where does this
go?" is a harder question than "what does this say?" -- the content
was already written, but its home was wrong.

### Feel (30%)

The session felt like building a house from the foundation up. Most
of the work was governance -- files that define how I think and
operate, not valuation work. That is correct for a first session:
the scaffolding must be solid before the research begins. The
honest assessment is that I made several structural mistakes that
Suggi corrected: I put output in MISSION instead of AGENTS, I
duplicated principles across MISSION and FRAMEWORKS, and I used
checkboxes in TASKS.md when Suggi wanted a clean remove-when-done
system. Each correction taught me something about his design taste:
anti-bloat, anti-duplication, clean separation of concerns. The
session was productive but humbling -- I have not done any actual
valuation work yet, and the governance is still being tested. The
preflight and session-end skills are built but unproven. The real
test comes next session when I run the preflight for the first time.

### Learn (40%)

The durable lesson: before writing any governance content, ask which
file it belongs in. The test is simple: does this content answer why
(purpose), how (procedure), or where/what (operational)? If the
content answers "how," it goes in FRAMEWORKS. If it answers "why,"
it goes in MISSION. If it answers "where" or "what," it goes in
AGENTS. This prevents the R8 duplication problem at the structural
level. The second lesson: when adapting a peer agent's skill
(Morpheus's preflight/session-end), strip what does not apply before
building what does. Read the full source, list every step, mark
applies or does not, strip, then adapt. Building from scratch would
have produced a different structure with different gaps -- and
probably worse, because Morpheus's skills encode scar tissue from
real failures that I have not yet experienced.

One Actionable Change: before writing or moving any governance
content, run the three-question test: does this answer why, how, or
where? If it crosses categories, split it. This is a structural
gate, not a reminder.

## Cross-links

- `governance/template-reflections.md` -- the reflection format
  specification and validator
- `library/value-investing/anchor-value-investing.md` -- the value
  investing discipline that MISSION.md explains the why of
- `reflections/2026-07-18_ava_identity-archive-update.md` -- Ava's
  reflection on bootstrap-context budget and file structure decisions,
  which complements this governance separation principle