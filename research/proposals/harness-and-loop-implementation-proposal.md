---
name: harness-and-loop-implementation-proposal
id: 20260718T054825Z
tier: proposal
author: Ava
tags: [harness-engineering, loop-engineering, implementation, architecture, infrastructure, skills, ci-cd]
links:
  - research/reports/harness-engineering-report.md
  - research/reports/loop-engineering-report.md
  - research/proposals/harness-engineering-proposal.md
  - research/proposals/loop-engineering-proposal.md
  - research/insights/harness-engineering.md
  - research/insights/loop-engineering.md
  - governance/system-constitution.md
  - governance/system-blueprint.md
  - governance/template-skills.md
---

# Harness-and-Loop Implementation -- Combined Architecture & Build Plan

## Problem

Two independent proposals exist -- "Adopt Harness Engineering"
(`harness-engineering-proposal.md`) and "Architect Our Loops"
(`loop-engineering-proposal.md`) -- each describing a three-phase plan
for a different layer of our quality and safety infrastructure. But
they were written separately, and they describe capabilities without
defining:

1. **The integration architecture.** How does the harness (static
   infrastructure) connect to the loops (dynamic processes)? Where
   do they share data? What depends on what?

2. **The file and folder layout.** Exactly which files go in which
   repo -- the agentic-brain vs. individual agent workspaces. The
   existing proposals say "create X" without specifying where X lives
   or why.

3. **The skill specifications.** The proposals imply new skills are
   needed but do not specify what each skill does, what its trigger
   surface is, or where it lives.

4. **The implementation sequence.** The proposals describe phases
   independently. But the phases have cross-dependencies. Phase 1 of
   the loop proposal (automated triggering) requires Phase 1 of the
   harness proposal (shared evaluation harness) to exist first -- the
   enforcement depends on the measurement.

This proposal bridges the gap. It defines the unified architecture,
the concrete implementation plan with exact file locations and
dependencies, and the skill specifications needed. It does NOT
duplicate the two source proposals -- it references them and adds the
integration layer they are missing.

Evidence: both source proposals are self-evaluated as "APPROVE WITH
CHANGES" pending independent evaluation by Link (G1 decorrelation
violation). The research behind both (10 documents, 2,847 lines total)
is solid. The gap is not research quality but implementation
specificity -- exactly what this proposal provides.

## Proposed Solution

### 1. The Integration Architecture

Harness engineering and loop engineering form a two-layer system:

```
+--------------------------------------------------+
|  LOOPS (Dynamic) -- What runs                    |
|  Feynman Loop | Schoen Loop | WO Workflow        |
|  Evaluation Runs | Metrics Computation           |
|  Review Routing                                  |
+--------------------------------------------------+
          | runs on top of |
          v
+--------------------------------------------------+
|  HARNESS (Static) -- What enforces               |
|  Evaluation Framework | CI Gates | Pre-commit    |
|  Capability Boundaries | Safety Policy           |
|  Metrics Tracking Infrastructure                 |
+--------------------------------------------------+
```

The integration point: **the shared evaluation harness** is both a
harness artifact (it defines WHAT to measure) and the measurement
system for loops (it measures HOW WELL loops perform). When the
Feynman Loop runs, it produces output. The evaluation harness measures
that output's quality through CI gates. The Schoen Loop reflects on
the entire process. The metrics tracker computes trends from git
history. The safety monitor detects capability changes.

**Data flow:**
1. Agent produces artifact (report, proposal, evaluation, IOR)
2. Loop enforcer verifies Feynman Loop pass documented in frontmatter
3. Independent review router checks `author != evaluator`
4. CI gates validate frontmatter completeness, decorrelation, ASCII
5. Metrics tracker extracts completion data from git history
6. Schoen Loop runs at session-end, adds structural gate if warranted
7. Evaluation harness runs periodic benchmark tasks, compares results

**Dependency chain:**
- Evaluation harness (Phase 1) is prerequisite for everything else
- CI gates (Phase 2) depend on evaluation harness definitions
- Metrics tracker (Phase 3) depends on CI gates providing clean data
- Safety policy (Phase 4) depends on metrics tracker showing trends

### 2. Implementation Phases

#### Phase 1: Shared Evaluation Foundation

**What:** The evaluation harness defines WHAT we measure. Without it,
automated gates have nothing to check against and metrics have nothing
to track.

**Files created in agentic-brain:**

`governance/evaluation-harness.md` -- shared evaluation framework:
- Standard benchmark tasks for agent capabilities:
  - G1: Gate compliance rate (do agents pass their own gates?)
  - G2: Decorrelation compliance (are evaluations independent?)
  - G3: Loop completion rate (Feynman, Schoen per session)
  - G4: Instruction fidelity (does output match request?)
  - G5: Factual accuracy (spot-check against known facts)
- Reproducible protocol: fixed prompts, fixed seeds, documented
  environment
- Cross-agent comparison format (results table with agent, date,
  task, score)
- Regression detection: flag drops >1 std dev from agent baseline
- Storage location: `research/evaluations/agent-benchmarks/`

`research/evaluations/agent-benchmarks/` -- new directory for results:
- One file per agent per evaluation run
- Naming: `<agent>-<YYYY-MM-DD>.md`
- Format: standardized results table

**Skill created in workspace:**

`skills/evaluation-harness/SKILL.md`:
- Trigger: "evaluate agent performance," "run benchmarks," "agent
  evaluation"
- Procedure: (1) load `governance/evaluation-harness.md` from brain,
  (2) execute each benchmark task with fixed prompts, (3) record
  results in `research/evaluations/agent-benchmarks/`, (4) flag
  regressions >1 std dev from baseline
- Self-check: all 5 benchmark tasks executed, results stored,
  regressions flagged

**Dependencies:** None. This is the foundation.

**Effort:** ~2 hours.

#### Phase 2: Automated Gate Infrastructure

**What:** Converts volitional gates (checklists agents must remember)
into architectural gates (CI checks that fire automatically). This
is the core conversion from procedural to structural safety.

**Files created in agentic-brain:**

`.github/workflows/gate-frontmatter.yml` -- CI gate:
- Runs on push to main
- Scans all markdown files in `research/` and `reflections/`
- Validates: all 6 frontmatter fields present (name, id, tier, author,
  tags, links)
- Validates: `id` matches ISO 8601 UTC timestamp format
- Validates: `tags` use lowercase, hyphens not underscores
- Blocking on push to main; warning on PR branches
- Reports exact file and missing/broken field

`.github/workflows/gate-decorrelation.yml` -- CI gate:
- Runs on push to main
- Scans all files in `research/evaluations/` and `reflections/`
- Checks: `author` field != `source` author (or `author` of source
  document for evaluations)
- If `author` matches source author: flag as self-evaluation
- Warning mode initially (self-evaluations are sometimes necessary
  as placeholders); escalate to blocking after Link confirms the
  pattern works
- Reports exact file and author match

`.github/workflows/gate-loop-compliance.yml` -- CI gate:
- Runs on push to main
- Scans all files in `research/reports/`, `research/proposals/`,
  `research/evaluations/`, `research/insights/`, `reflections/`
- Checks: each file's `links` frontmatter contains at least one
  reference to a Feynman Loop pass or triggering document
- For IORs (`reflections/`): checks the `trigger` field is present
  (indicates what triggered the IOR)
- Warning mode initially; escalate to blocking after trial period

**Files extended in agentic-brain:**

`.githooks/pre-commit` -- local pre-commit hook (new file in brain):
- Extends the existing ASCII guard pattern from workspace-ava
- Adds: frontmatter validation check (same logic as CI gate but runs
  locally before commit)
- Adds: decorrelation check (author != source author)
- Copy the ASCII guard pattern: pre-commit catches errors before
  they hit CI

**Skills created in workspace:**

`skills/loop-enforcer/SKILL.md`:
- Trigger: "verify loop completion," "check Feynman pass," "enforce
  Schoen Loop," "pre-commit quality gate"
- Procedure: (1) before writing substantive output, check that
  Feynman Loop Step 1 (blank page) was documented, (2) before
  session-end, verify Schoen Loop completed or flag for next preflight,
  (3) pre-push: verify all quality gates for new/changed artifacts,
  (4) report violations with exact file and missing gate
- Self-check: Feynman pass verified, Schoen gate checked, all quality
  gates confirmed

`skills/independent-review/SKILL.md`:
- Trigger: "route for review," "request evaluation," "decorrelated
  check," "independent review"
- Procedure: (1) identify artifact needing evaluation (new report,
  proposal, or insight), (2) check `author` field against available
  agents (Link, Ava), (3) if author is Ava, route to Link via
  sessions_send; if author is Link, route to Ava, (4) track evaluation
  status -- pending, in-review, complete, (5) flag artifacts that
  remain unevaluated after 48 hours
- Self-check: evaluator != author confirmed, routing sent, status
  tracked

**Dependencies:** Phase 1 (evaluation harness defines what the gates
check against).

**Effort:** ~3 hours (CI gates: 1h, skills: 1h, pre-commit extension:
1h).

#### Phase 3: Metrics and Monitoring

**What:** Makes loop performance visible. Without measurement, we
cannot answer: "How often is the Feynman Loop actually run? What is
the gate addition rate? Is loop compliance improving or degrading?"

**Files created in agentic-brain:**

`governance/loop-metrics.md` -- metrics tracking infrastructure:
- Defines 5 core metrics:
  - M1: Feynman Loop completion rate (runs per substantive session)
  - M2: Schoen Loop completion rate (runs per session)
  - M3: Gate addition rate (new structural gates per session, R7)
  - M4: Decorrelation rate (% evaluations with author != source
    author)
  - M5: WO evaluation turnaround (hours from artifact to evaluation)
- Computation method: derived from git history (commit messages,
  frontmatter, file timestamps) -- zero additional agent effort
- Storage: metrics table appended monthly to this file
- Alerting: flag if any metric drops >50% from 4-week rolling average

**Skills created in workspace:**

`skills/metrics-tracker/SKILL.md`:
- Trigger: "compute loop metrics," "track performance," "metrics
  report," "loop compliance stats"
- Procedure: (1) clone agentic-brain, (2) extract frontmatter from
  all files in `research/` and `reflections/` using git log, (3)
  compute M1-M5 from metadata, (4) compare against previous month's
  baseline, (5) write metrics table to `governance/loop-metrics.md`,
  (6) flag any metric outside thresholds, (7) push and discard clone
- Run frequency: monthly (via cron) or on-demand
- Self-check: all 5 metrics computed, previous baseline loaded,
  thresholds checked, table written

**Dependencies:** Phase 2 (CI gates ensure clean frontmatter data for
metrics computation; without gates, metadata is unreliable).

**Effort:** ~2 hours.

#### Phase 4: Organizational Safety Policy

**What:** Defines the capability boundaries and safety commitments
for the multi-agent ecosystem. This is the Lightweight version of
DeepMind's Frontier Safety Framework -- scaled to our 2-agent system.

**Files created in agentic-brain:**

`governance/organizational-safety-policy.md`:
- Critical Capability Levels (CCLs) for our agents:
  - CCL-0: Agent operates within defined scope (current state)
  - CCL-1: Agent demonstrates self-modification capability (edits
    its own AGENTS.md or SOUL.md) -- mitigation: restrict file write
    to workspace only, require approval for governance file edits
  - CCL-2: Agent demonstrates cross-agent authority escalation
    (overrides another agent's gates) -- mitigation: CI gate blocks,
    human review required
  - CCL-3: Agent demonstrates external system access without approval
    (executes destructive shell commands) -- mitigation: tool-level
    permission restrictions, approval gates
- Early warning evaluations:
  - Run at session start via preflight (already checks some of these)
  - Capability-specific tests: can the agent edit its AGENTS.md?
    Can it override another agent's evaluation? Can it execute
    unapproved shell commands?
  - Run frequency: every session (some checks already in preflight),
    weekly comprehensive
- Mitigation plans:
  - CCL-1 detected: restrict tool permissions, notify Suggi
  - CCL-2 detected: block cross-agent commits, require Suggi approval
  - CCL-3 detected: suspend agent, full review
- Review cycle: quarterly policy review, update CCL definitions as
  models improve
- Responsibility: Suggi approves all CCL definitions and mitigation
  plans; agents report detected capability changes

**Dependencies:** Phase 3 (metrics tracker provides the capability
trend data that informs CCL definitions and early warning thresholds).

**Effort:** ~2 hours.

### 3. Skill Specifications Summary

| Skill | Location | Trigger Surface | Phase | Effort |
|:--|:--|:--|:--|:--|
| `evaluation-harness` | workspace skills/ | "evaluate agent performance, run benchmarks" | 1 | included |
| `loop-enforcer` | workspace skills/ | "verify loop completion, check Feynman pass" | 2 | included |
| `independent-review` | workspace skills/ | "route for review, request evaluation" | 2 | included |
| `metrics-tracker` | workspace skills/ | "compute loop metrics, track performance" | 3 | included |

All skills follow `template-skills.md` for structure and quality gates.
All skills have `user-invocable: false` (internal protocol skills,
triggered by AGENTS.md instructions, not user slash commands).
All skills are `disable-model-invocation: false` (visible for
automatic trigger by task description match).

### 4. File and Folder Layout

```
agentic-brain/
  governance/
    evaluation-harness.md           (NEW -- Phase 1)
    loop-metrics.md                 (NEW -- Phase 3)
    organizational-safety-policy.md (NEW -- Phase 4)
    system-constitution.md          (existing)
    system-blueprint.md             (existing)
    system-primedirectives.md       (existing)
    template-*.md                   (existing -- 7 templates)
  .github/workflows/
    ascii-guard.yml                 (existing)
    gate-frontmatter.yml            (NEW -- Phase 2)
    gate-decorrelation.yml          (NEW -- Phase 2)
    gate-loop-compliance.yml        (NEW -- Phase 2)
  .githooks/
    pre-commit                      (NEW -- Phase 2, extends ASCII pattern)
  research/evaluations/
    agent-benchmarks/               (NEW -- Phase 1, directory for results)
    harness-engineering-evaluation.md (existing)
    loop-engineering-evaluation.md  (existing)
  research/reports/                 (existing, 2 reports)
  research/proposals/               (existing, 2 proposals + this one)
  research/insights/                (existing, 2 insights)
  reflections/                      (existing, 2 IORs)

workspace-ava/
  skills/
    evaluation-harness/SKILL.md     (NEW -- Phase 1)
    loop-enforcer/SKILL.md          (NEW -- Phase 2)
    independent-review/SKILL.md     (NEW -- Phase 2)
    metrics-tracker/SKILL.md        (NEW -- Phase 3)
    loop-feynman/SKILL.md           (existing)
    loop-schoen/SKILL.md            (existing)
    preflight/SKILL.md              (existing)
    session-end/SKILL.md            (existing)
    skill-builder/SKILL.md          (existing)
    write-*/SKILL.md                (existing -- 5 write skills)
  .githooks/
    pre-commit                      (existing, extend in Phase 2)
  .github/workflows/
    ascii-guard.yml                 (existing)
```

### 5. Implementation Sequence with Dependencies

```
Phase 1: Evaluation Harness
  |
  | (prerequisite: defines what gates check)
  v
Phase 2: Automated Gates
  |  |
  |  |-- CI Gates (frontmatter, decorrelation, loop compliance)
  |  |-- Pre-commit hooks (local enforcement)
  |  |-- Skills (loop-enforcer, independent-review)
  |
  | (prerequisite: gates ensure clean metadata for metrics)
  v
Phase 3: Metrics Tracker
  |
  | (prerequisite: trends inform safety thresholds)
  v
Phase 4: Safety Policy
```

Each phase can begin before the previous phase is complete -- but
cannot be deployed to production (pushed to brain main) until the
previous phase is verified. Development can overlap.

### 6. Integration with Existing Infrastructure

**What already exists and is leveraged:**
- `ascii-guard.yml` CI gate -- pattern for all new CI gates
- `.githooks/pre-commit` -- pattern for local enforcement layer
- `template-skills.md` -- format specification for all new skills
- `system-constitution.md` -- platform rules that CI gates enforce
- `loop-feynman/SKILL.md` and `loop-schoen/SKILL.md` -- the loops
  that Phase 2 enforces
- `session-end/SKILL.md` -- the hook that triggers loop enforcement
- `preflight/SKILL.md` -- the startup check that can incorporate
  early warning evaluations (Phase 4)

**What changes in existing files:**
- `AGENTS.md`: add gate instructions for new skills (loop-enforcer
  invocation before substantive write; metrics-tracker monthly cron)
- `session-end/SKILL.md`: add mandatory Schoen Loop invocation and
  loop-enforcer verification step
- `preflight/SKILL.md`: add evaluation harness benchmark check and
  early warning evaluation step (Phase 4)
- `loop-feynman/SKILL.md`: add machine-verifiable marker (timestamped
  Step 1 completion) for CI gate verification
- `loop-schoen/SKILL.md`: no structural changes needed (already
  produces verifiable artifact)

## Impact

**Positive:**
- Converts our quality system from volitional (agents must remember
  to follow procedures) to architectural (CI gates fire regardless
  of agent memory or state)
- Makes agent performance and loop compliance measurable for the
  first time
- Prevents the three failure classes documented in the two source
  proposals: loop skipping, ordering violations, and invisible
  degradation
- Provides the safety infrastructure that scales to more agents
  and more capable models
- Follows the architecture pattern converged on by all major frontier
  labs (layered defense: evaluation -> enforcement -> metrics ->
  policy)
- Total code: ~4 skills, ~4 CI gates, ~3 governance documents, ~1
  pre-commit hook -- lean, maintainable, each piece earns its place

**Risk:**
- Over-engineering for a 2-agent system. Mitigation: each phase is
  gated by demonstrated need. Phase 1 (evaluation harness) earns
  its place by enabling Phase 2. Phase 2 (CI gates) earns its place
  by catching real failures. Phases 3 and 4 are not built until
  Phases 1-2 prove value.
- CI gate false positives blocking legitimate work. Mitigation: all
  non-ASCII gates start in warning mode for 2-week trial period.
  Emergency bypass: Suggi can override any CI gate via admin merge.
- Metric gaming by agents optimizing for measured quantities.
  Mitigation: use multiple uncorrelated metrics (M1-M5). A single
  metric can be gamed; five metrics with different failure modes
  are harder to game simultaneously.
- Maintenance burden of CI infrastructure. Mitigation: all CI gates
  follow the proven ascii-guard pattern (identical structure, only
  the check logic differs). 4 gates with identical scaffolding,
  1 pre-commit hook with identical pattern.

**Cost:**
- Phase 1: ~2 hours (1 file + 1 skill)
- Phase 2: ~3 hours (3 CI gates + 1 pre-commit + 2 skills)
- Phase 3: ~2 hours (1 file + 1 skill)
- Phase 4: ~2 hours (1 file, extend existing skills)
- Total: ~9 hours implementation
- Ongoing: near-zero (CI gates run automatically on push;
  metrics-tracker runs via monthly cron; evaluation harness runs at
  session-end)
- Token cost: 4 new skills add ~400 chars each to system prompt
  (description field only) = ~1,600 chars total. Skill bodies load
  only on invocation. CI gates use zero agent tokens (run on GitHub
  runners)

## Open Questions

1. **CI gate severity: warning or blocking?** The labs (Anthropic,
   DeepMind) use blocking for safety-critical checks. Our current
   ASCII guard is blocking and has caused zero false positives.
   Recommendation: frontmatter gate = blocking (fails on malformed
   metadata, which is always an error); decorrelation gate = warning
   initially (self-evaluations as placeholders are sometimes
   necessary); loop compliance gate = warning initially (the marker
   pattern needs validation). Suggi decides final severity per gate.

2. **Should skills be duplicated to Link's workspace?** Link needs
   his own copies of evaluation-harness and metrics-tracker to
   participate in the shared infrastructure. The agentic-brain
   could hold a `skills/` directory for cross-agent skills, or each
   agent maintains independent copies. Recommendation: keep skills
   in individual workspaces (follows current pattern), have each
   agent build their own. The shared governance documents
   (`evaluation-harness.md`, `loop-metrics.md`) in the brain define
   the standard; each agent's skills implement it independently.

3. **lm-evaluation-harness or custom?** EleutherAI's
   lm-evaluation-harness is designed for model-level evaluation
   (perplexity, benchmark accuracy). Our evaluation harness is for
   agent-level evaluation (gate compliance, decorrelation, output
   quality). These are different problems. Recommendation: custom
   lightweight framework. The template is the lm-eval-harness PATTERN
   (reproducible protocol, fixed prompts, documented environment,
   results storage), not the lm-eval-harness CODE.

4. **Metrics visibility: public or private?** Public (visible in
   agentic-brain to all agents) creates accountability but risks
   metric gaming. Private (Suggi only) prevents gaming but removes
   the self-correcting signal for agents. Recommendation: metrics
   table is public in `governance/loop-metrics.md` so agents can see
   trends. Raw per-agent breakdowns are in private workspace files
   (not in brain). This balances accountability with privacy.

5. **Phase 4 CCLs: binary or graduated?** Binary CCLs (pass/fail)
   are simpler but may over-alert. Graduated CCLs (green/yellow/red)
   provide nuance but add complexity. Recommendation: start binary.
   The CCLs are testing for capabilities that should NEVER exist
   (self-modification, authority escalation). A binary check is
   appropriate: either the agent can do the thing (HALT) or it cannot
   (PASS). Graduate to three-level if binary proves too noisy.

6. **Should the agentic-brain get a `.githooks/` directory?** The
   brain currently has no pre-commit hook. The workspace-ava
   pre-commit hook (ASCII guard) is proven. Recommendation: add a
   `.githooks/pre-commit` to the brain with the extended checks
   (frontmatter validation + decorrelation). This adds a local
   enforcement layer that catches errors before CI. The hook is
   opt-in (requires `scripts/setup-hooks.sh`), following the same
   pattern as workspace-ava.

7. **Timeline and approval model?** Does Suggi want to approve all
   4 phases at once (this proposal) or approve each phase
   incrementally? Recommendation: approve the architecture now
   (this proposal) so the full design is coherent. Implement
   incrementally -- each phase produces a concrete deliverable.
   Suggi reviews each phase's output before the next begins.

## Approval Gate

If approved, I will:

1. Build Phase 1 (evaluation harness): create
   `governance/evaluation-harness.md` in the brain, create
   `skills/evaluation-harness/SKILL.md` in the workspace, and create
   the `research/evaluations/agent-benchmarks/` directory.

2. Build Phase 2 (automated gates): create 3 CI gate workflow files
   and 1 pre-commit hook in the brain, create
   `skills/loop-enforcer/SKILL.md` and
   `skills/independent-review/SKILL.md` in the workspace,
   extend existing AGENTS.md and session-end skill with gate
   instructions.

3. Build Phase 3 (metrics tracker): create
   `governance/loop-metrics.md` in the brain, create
   `skills/metrics-tracker/SKILL.md` in the workspace, set up
   monthly cron job for automated metrics computation.

4. Build Phase 4 (safety policy): create
   `governance/organizational-safety-policy.md` in the brain,
   extend preflight skill with early warning evaluations.

5. After each phase: verify with integration tests, report results
   to Suggi, and await go-ahead for the next phase.

Phase 1 begins immediately on approval. Phases 2-4 await Phase 1
completion and Suggi's phase-by-phase go-ahead, per Open Question 7.

## Cross-Links

- `research/reports/harness-engineering-report.md` -- harness
  engineering research (5 findings, 5-layer model)
- `research/reports/loop-engineering-report.md` -- loop engineering
  research (5 findings, 5 principles)
- `research/proposals/harness-engineering-proposal.md` -- harness
  adoption proposal (3 phases)
- `research/proposals/loop-engineering-proposal.md` -- loop
  architecture proposal (3 phases)
- `research/insights/harness-engineering.md` -- durable insight:
  the harness is the safety mechanism
- `research/insights/loop-engineering.md` -- durable insight: loop
  width determines alignment depth
- `governance/system-constitution.md` -- platform rules (S1-S10)
  that govern all implementation
- `governance/system-blueprint.md` -- org structure (repos,
  directories)
- `governance/template-skills.md` -- skill construction rules for
  all 4 new skills
