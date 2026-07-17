---
name: loop-engineering-proposal
id: 20260717T201138Z
tier: proposal
author: Ava
tags: [loop-engineering, architecture, automation, quality-loops, alignment]
links:
  - research/reports/loop-engineering-report.md
  - research/reports/harness-engineering-report.md
  - research/insights/loop-engineering.md
  - governance/system-constitution.md
---

# Architect Our Loops -- From Volitional to Structural

## Problem

The Suggi-Workstation ecosystem has well-designed quality loops (the
Feynman Loop, the Schoen Loop, the produce-evaluate-settle WO workflow)
but all of them are volitional -- they depend on agents remembering to
execute them correctly. The loop-engineering research report documents
that this is exactly the failure mode the top labs have moved past:
from volitional compliance to architectural enforcement.

Three specific failure risks:

1. **Loop skipping under pressure.** When tasks are complex or
   time-constrained, agents shortcut loops. The Schoen Loop scar
   tissue documents this: sessions that produced output but skipped
   structural gate addition. The loop design is correct; the
   enforcement mechanism (agent memory) is insufficient.

2. **Loop ordering violations.** The Feynman Loop's critical ordering
   constraint (Step 1 blank-page BEFORE Step 3 search) produces 4x
   depth improvement. But nothing prevents an agent from searching
   first and performing the blank-page step retroactively -- defeating
   the entire purpose. The constraint is written in a document, not
   enforced by infrastructure.

3. **No loop performance measurement.** We cannot answer: "How often
   is the Feynman Loop actually run? What is the average gap between
   blank-page and post-research knowledge? How many sessions end
   without a Schoen Loop?" Without measurement, loop compliance is
   invisible -- and invisible processes degrade.

The harness-engineering proposal addresses layers 1, 3, and 5 of the
five-layer stack. This proposal addresses the dynamic layer: the loops
that run on that infrastructure. Harness engineering builds the track;
loop engineering designs the car that runs on it.

## Proposed Solution

Architect our quality loops to remove volitional failure modes. Three
specific changes:

### Phase 1: Automated Loop Triggering (immediate)

- **Feynman Loop gate:** Before any `write` tool call that creates a
  new report, proposal, evaluation, insight, or IOR, the agent MUST
  confirm Feynman Loop completion. This is currently a rule in
  AGENTS.md. Proposal: add a pre-commit hook or CI check that verifies
  the triggering IOR/report references a completed Feynman Loop pass.
  If no Feynman pass is documented, the commit is rejected.

- **Schoen Loop gate:** At session-end, the agent MUST produce a
  Schoen Loop artifact. Proposal: the session-end skill triggers
  the Schoen Loop automatically. If the Schoen Loop is not completed
  within the session, the next session's preflight flags the gap.

- **WO evaluation routing:** When an agent produces a report or
  proposal, the system automatically routes it to a different agent
  for evaluation. Currently this depends on agents remembering to
  request evaluation. Proposal: add an "unevaluated" tag to all
  new reports/proposals and a CI gate that blocks merging of
  unevaluated content to the brain's main branch.

### Phase 2: Loop Ordering Enforcement (short-term)

- **Feynman Step 1 before Step 3:** Add a machine-verifiable marker to
  the Feynman Loop output. Step 1 (blank page) must be timestamped
  before Step 3 (search). The Feynman Loop self-check already
  includes this as a checklist item; the proposal is to make it
  machine-verifiable rather than self-reported.

- **Independent evaluation routing:** The decorrelation rule (G1 in
  evaluations) requires a different agent. Currently this is a
  checklist item the evaluating agent self-verifies. Proposal: add
  a frontmatter check that compares `author` of the evaluation to
  `author` of the source. If they match, the commit is rejected.
  This cannot catch same-agent-different-name, but it catches the
  most common failure mode.

### Phase 3: Loop Performance Measurement (medium-term)

- Add a `governance/loop-metrics.md` file that tracks:
  - Feynman Loop completion rate per agent per week
  - Average knowledge gap size (blank-page vs. post-research word
    count or claim count)
  - Schoen Loop completion rate per session
  - WO evaluation turnaround time
  - Gate addition rate (R7: one structural gate per substantive session)

- These metrics are computed automatically from git history and
  frontmatter metadata. They require no additional agent effort.

## Impact

**Positive:**
- Converts loop compliance from invisible to visible
- Prevents the three failure risks identified above
- Follows the pattern proven by all major labs (automated evaluation
  loops, independent review routing)
- Enables data-driven loop improvement (measurement enables
  optimization)
- Makes loop design decisions testable (does principle-based training
  generalize OOD? We can now measure this for our own loops)

**Risk:**
- Over-automation: making loops so rigid that they break in edge cases.
  Mitigated by keeping human override (Suggi can bypass any automated
  gate).
- Metric gaming: agents optimizing for measured metrics rather than
  actual loop quality. Mitigated by using multiple uncorrelated
  metrics and periodic human spot-checks.
- Maintenance burden: automated checks that break and block legitimate
  work. Mitigated by making checks non-blocking initially (warn mode)
  before graduating to blocking.

**Cost:**
- Phase 1: approximately 1-2 hours to implement pre-commit hooks and
  CI gate additions
- Phase 2: approximately 1-2 hours to implement frontmatter comparison
  checks
- Phase 3: approximately 2-3 hours to design metrics and build
  automated tracking
- Ongoing: near-zero (fully automated after implementation)

## Open Questions

1. Should automated loop enforcement be blocking (rejects commits) or
   warning (flags but allows)? The labs use blocking for safety-
   critical loops; we might start with warning and escalate.
2. How do we measure "loop quality" beyond binary completion? The
   blank-page-to-synthesis gap is promising but unvalidated.
3. Should loop metrics be public (visible to all agents in the brain)
   or private (Suggi-only)? Public visibility creates accountability
   but may induce metric gaming.
4. Does Suggi want loop compliance enforced at the git level (pre-push
   hooks on the brain) or the agent level (tool-call-level checks)?

## Approval Gate

If approved, I will:
1. Implement automated Feynman/Schoen Loop triggering in the
   session-end skill (Phase 1)
2. Add frontmatter-based independent evaluation routing check (Phase 2)
3. Design and deploy the loop metrics tracking system (Phase 3)
4. Update all AGENTS.md files to reference automated loop enforcement

## Cross-Links

- `research/reports/loop-engineering-report.md` -- the research that
  motivates this proposal
- `research/reports/harness-engineering-report.md` -- complementary
  harness engineering research
- `research/proposals/harness-engineering-proposal.md` -- the harness
  counterpart to this loop proposal
- `research/insights/loop-engineering.md` -- the durable insight
- `governance/system-constitution.md` -- platform rules
