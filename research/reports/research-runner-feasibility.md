---
name: research-runner-feasibility
id: 20260823T145406Z
tier: report
status: draft
author: Morpheus
tags: [subagent, fleet, research-pipeline, capacity, library]
links:
  - research/proposals/research-runner-subagent.md
  - research/insights/library-system.md
---

# Research-Runner Subagent -- What the Fleet Record Shows

## Executive Summary

Question: does the fleet record support adding a dedicated
research-runner subagent now? Answer: no -- and the record also shows
the runner pattern itself works well when fed. The library pipeline
produced 217 topic files through cron-driven runner cycles between
July 19 and August 16, proving the lean-runner pattern at scale. But
both existing runners have been idle since mid-August (library-runner
jobs disabled, investment-runner never given jobs), and the record
contains zero instances of research work being deferred for lack of
capacity. Recommendation: hold at the proposal's position -- define
trigger conditions, birth nothing until they fire. Confidence: high
(85%), based on complete git and roster evidence; the main uncertainty
is unrecorded demand (requests Suggi never wrote down).

## Research Question

Does the fleet need a third lean subagent dedicated to automated
research cycles now?

Scope in: production history of the existing runners, current runner
states, recorded research demand from July-August 2026. Scope out: cost
of profile birth mechanics (documented in hermes-subagent-fleet),
whether library content quality is sufficient (evaluated elsewhere),
investing-runner's future job set (Neo's domain).

## Methodology

Three evidence sources, all primary: (1) git history of the agentic-brain
library folder (`git log -- library/`), counting production commits and
burst dates; (2) live file counts (`find library -name '*.md' | wc -l`
= 217); (3) the fleet roster (FLEET.md, verified against live cron
state during preflight). Demand-side search covered the logbook
(queue.log) for deferred or backlogged research requests. Retrieval
date: 2026-08-23. Limitations: one month of observable history; demand
evidence depends on what was actually recorded -- silent deferrals are
invisible to this method.

## Findings

### Finding 1: The Runner Pattern Works at Scale -- Claim CONFIRMED

The library-runner produced 217 topic files across roughly twenty
production days (July 19-30, August 5, August 16), with peak days
exceeding thirty commits. Evidence: git log of `library/`, file count
217. This validates the discoverer-propose/writer-produce cycle shape
that a research-runner would copy. Confidence: high (95%).

### Finding 2: Both Existing Runners Are Idle -- Claim CONFIRMED

Library-runner: three jobs, all disabled since 2026-08-22 (roster;
last library production commit 2026-08-16 13:23 +0200).
Investment-runner: zero jobs ever assigned. Neither runner has run a
production cycle in the current paused state. Evidence: FLEET.md
verified against live registry at preflight. Confidence: high (95%).

### Finding 3: No Recorded Capacity Shortfall -- NEGATIVE RESULT

Search of the logbook for deferred, backlogged, or cut-short research
work found zero recorded instances. Nineteen logbook lines mention
"research"; none record a capacity failure. The honest reading: trigger
condition 2 from the proposal has not demonstrably fired, though
unrecorded demand cannot be excluded. Confidence: medium (70%) --
absence of evidence here is weak evidence of absence, because the
logbook records agent events, not Suggi's unprompted wishes.

### Finding 4: Reactivation Precedes Any Birth -- SEQUENCING CONSTRAINT

The proposal's own trigger 1 (library pipeline sustained for two weeks)
requires unpausing library-runner first. A research-runner born today
would therefore be the third idle agent; born after reactivation, it
joins a proven-operating pattern. Evidence: Findings 1-2 combined.
Confidence: high (90%).

## Discussion

The findings support the proposal's counterintuitive conclusion: the
strongest argument FOR a research-runner (the pattern works -- Finding
1) coexists with the strongest argument AGAINST (we are not using the
two we have -- Finding 2). The binding constraint is not production
capacity but activated demand, consistent with the fleet's prior
verification-bottleneck insight: adding producers without consumers or
verified demand creates idle surface, not leverage. Finding 3 is the
pivot point: if real deferred demand exists but went unrecorded, the
report's answer flips -- which is why the proposal routes the decision
through explicit, queryable trigger conditions rather than a flat no.

## Conclusion

Do not add a research-runner now. The pattern is proven (Finding 1),
the demand is not (Finding 3), and both current runners sit idle
(Finding 2). One actionable recommendation: when Suggi next unpauses
the library pipeline, start the proposal's two-week observation window
in the same session, so trigger 1 begins accruing evidence immediately.
Open questions: who evaluates trigger 2 (demand), and whether
unrecorded-demand risk justifies a lighter probe (e.g., logging research
requests interactively for a month before deciding).

## Cross-Links

- `research/proposals/research-runner-subagent.md` -- the proposal this
  report investigates (supersedes 20260718T144607Z)
- `research/insights/library-system.md` -- the runner-pattern knowledge
  base this report draws on
