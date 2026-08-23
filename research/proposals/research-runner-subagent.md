---
name: research-runner-subagent
id: 20260823T142607Z
tier: proposal
status: open
author: Morpheus
tags: [proposal, subagent, fleet, research-pipeline, capacity]
links:
  - research/proposals/subagent-workspace-routing-proposal.md
  - research/insights/library-system.md
  - governance/system-blueprint.md
---

# Research-Runner Subagent -- Third Runner, or Not Yet

## Problem

Research work (proposals, reports, evaluations feeding the pipeline in
`research/`) is currently produced only interactively by core agents
during sessions. The question on the table: should the fleet add a
third lean subagent -- a "research-runner" -- dedicated to automated
research cycles, alongside the existing library-runner and
investment-runner?

The evidence cuts both ways. For it: the library pipeline proved the
lean cron-runner pattern works (discoverer proposes topics, writer
produces them, one cycle per tick); Ava's routing proposal
(`20260718T144607Z`, subagent-workspace-routing) already identified the
decorrelation value of dedicated specialist capacity. Against it: the
fleet roster records that library-runner's three jobs are ALL disabled
and investment-runner exists with ZERO jobs -- the two runners we
already birthed are sitting idle. Capacity we do not use argues against
birthing more of it.

## Proposed Solution

Do not birth the runner now. Instead, define explicit trigger
conditions, and birth it when they fire:

1. Library pipeline reactivated (its jobs unpaused) AND sustained for
   two weeks without protocol failures -- proving the runner pattern
   still operates cleanly on current infrastructure.
2. Interactive research demand demonstrably exceeds session capacity:
   three or more research requests in one month that had to be deferred
   or cut short because no session time was available.

When both hold, birth `research-runner` per `hermes-subagent-fleet`
(following the exact library-runner shape: lean profile, cron jobs,
paused-until-needed ticker), with jobs wired to the write-x skills.

Alternative considered and rejected: birthing the runner immediately.
Rejection reason: it would be the third idle agent in a fleet where
both existing runners already sit unused. Idle agents carry profile
maintenance, roster surface, and cognitive overhead while returning
nothing.

## Impact

- Positive: when triggered, research throughput stops competing with
  interactive session work; the pipeline in `research/README.md` gains
  a producer that runs unattended; the decision itself is reversible
  and cheap (a paused profile costs nothing until jobs exist).
- Risk: low, precisely because we are deferring. The main risk of the
  deferred path is that the triggers never get evaluated -- mitigated by
  writing them here, in a queryable artifact.
- Cost: near-zero now (this document). Deferred cost if triggered:
  roughly one session for profile birth plus per-cycle token spend,
  same envelope as library-runner.

## Open Questions

1. Should the trigger evaluation ride the monthly curator pass Suggi
   already runs, so it costs no separate session?
2. If birthed later, should research-runner feed proposals only (human
   approval downstream anyway), or also draft reports?

## Approval Gate

If approved, I will add the trigger conditions to my FLEET.md runner
roster notes, mark this proposal `approved`, and evaluate the triggers
during the next monthly curator pass. Birthing the runner itself stays
gated on the conditions above, not on this approval.

## Cross-Links

- `research/proposals/subagent-workspace-routing-proposal.md` --
  superseded prior art (Ava's researcher-workspace design; the current
  Hermes runner pattern replaces it)
- `research/insights/library-system.md` -- the working runner pattern
  this proposal would extend
- `research/README.md` -- pipeline this runner would feed
