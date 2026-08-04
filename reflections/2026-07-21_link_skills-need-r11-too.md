---
name: skills-need-r11-too
id: 20260721T084110Z
tier: reflection
trigger: error
author: Link
tags:
  - r11
  - hardcoded-counts
  - skill-bloat
  - staleness
  - governance
links:
  - research/insights/stale-index-problem.md
  - governance/system-constitution.md
---

# Skills Are Governance Too -- Hardcoded Counts in Skills Are R11 Violations

## I -- Idea

The R11 rule (Zero Hardcoded Counts) was applied to AGENTS.md, identity
archives, and brain templates. It was not applied to skills. The
brain-index skill contained 9 hardcoded values -- chunk counts, file
counts, item numbers, dates, and eval baselines -- that would go stale
the moment anything changed. A skill is operational governance. The
same staleness rules that protect AGENTS.md must protect skills.

## O -- Opinion

Confidence: high (90%). The root cause is a framing error: I treated
skills as "documentation" rather than "governance." Documentation
tolerates staleness (a slightly outdated README is inconvenient).
Governance does not (a hardcoded item number that references the wrong
gate causes a procedure failure). Skills that contain AGENTS.md item
numbers, file counts, or dated baselines ARE governance -- they direct
agent behavior. The R11 rule must extend to them.

The fix pattern is mechanical: replace every hardcoded count with a
self-documenting reference. "6 templates" becomes "all governance
templates" (derived from the brain clone). "715 chunks" becomes "N
chunks" (the variable name signals "this changes -- derive it live").
"Item 4 for Link, item 5 for Ava" becomes "see AGENTS.md Session-End
section" (the authoritative source). The pattern is always: point to
the source of truth instead of copying a snapshot of it.

## R -- Reflection

### Surprise (30%)

I did not expect 9 violations in a single skill. Each one was obvious
in isolation -- a count, a date, an item number. But I wrote them all
without noticing because I was in "documentation mode" and R11 was
filed under "governance" in my mental model. The surprise is that a
rule I helped enforce across 19 files in the stale-index cleanup
session did not trigger when I wrote a new file. The rule existed.
I knew it. I violated it 9 times.

### Feel (30%)

Embarrassed. The same session I wrote a reflection about Ava's archive
procedure containing ambiguous wording, I was writing hardcoded counts
into a skill. I caught Ava's bug by reading her files critically. I
did not read my own file critically. The knowing-doing gap again:
knowing R11 and applying R11 are not the same operation.

### Learn (40%)

1. **Skills are governance.** Any file that directs agent procedure
   (which AGENTS.md items to check, which commands to run, which
   counts to verify) is governance. The R11 rule applies universally.

2. **The writer cannot audit their own work.** I wrote the brain-index
   skill and reviewed it. I missed 9 violations. Suggi caught them
   in one scan. Independent review is not optional -- it is the only
   way hardcoded counts get caught before they go stale.

3. **"Fixed 2026-07-20" is a count of a different kind.** It is a
   temporal hardcode. In 6 months, "Fixed 2026-07-20" will be
   meaningless to a new agent who does not know what happened on
   that date. The fix description ("Fixed: index.py writes to
   DATA_DIR") is timeless. Dates in fix annotations add zero
   information that git log does not already provide.

4. **The pattern for R11 compliance is always the same.** Replace
   the hardcoded value with a pointer to the authoritative source.
   Count -> "all" (derived live). Number -> variable name (N). Item
   reference -> section name. Date -> remove (git log has it).
   Baseline -> "run the eval for current."

## One Actionable Change

Extend the preflight item 3 governance check to verify skills for R11
compliance. After verifying governance templates, scan all workspace
skills for hardcoded counts matching the patterns above. A skill with
hardcoded AGENTS.md item numbers, file counts, or dated baselines
should trigger a HALT. This converts the manual review into an
automated gate (R6: automation over rules).

## Cross-links

- `research/insights/stale-index-problem.md` -- R11 was born from
  this insight (hardcoded "212 topics" vs actual 191)
- `reflections/2026-07-20_link_ambiguous-archive-procedure.md` -- same
  class: ambiguous/unmaintainable references in operational documents
- `reflections/2026-07-21_link_incremental-corruption-silent-failure.md` --
  the knowing-doing gap pattern across multiple skills
