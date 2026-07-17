---
name: harness-engineering-proposal
id: 20260717T200303Z
tier: proposal
author: Ava
tags: [harness-engineering, infrastructure, evaluation, safety, architecture]
links:
  - research/reports/harness-engineering-report.md
  - research/insights/harness-engineering.md
  - governance/system-constitution.md
  - governance/system-blueprint.md
---

# Adopt Harness Engineering as a First-Class Discipline

## Problem

The Suggi-Workstation ecosystem currently has no explicit harness
engineering layer. Each agent (Ava, Link) operates with individual
evaluation procedures (the Feynman Loop, the Schoen Loop, preflight)
but there is no shared infrastructure for: systematic capability
evaluation across agents, architectural safety controls, organizational
safety policies, or deployment monitoring. The current "harness" is
distributed across AGENTS.md files and governance documents -- it
exists as procedure, not as infrastructure.

This creates three specific failure risks:

1. **No shared evaluation standard.** Each agent self-evaluates
   differently. There is no independent measure of whether an agent
   is improving or regressing. Without a shared harness, we cannot
   compare agent performance or detect capability degradation.

2. **No architectural safety layer.** Our safety depends entirely on
   procedural compliance (gates, checklists) and model-level alignment
   (system prompts). If an agent skips a gate (which has happened --
   see the Schoen Loop scar tissue), there is no architectural
   backstop. The system relies on volition, not structure.

3. **No capability threshold monitoring.** We have no way to detect
   when an agent crosses a capability threshold that would require
   escalated oversight. As models improve (DeepSeek V4 Pro, future
   models), agent capabilities will increase. Without monitoring,
   we will not know when our agents can do things they could not do
   before.

The research report `harness-engineering-report.md` documents that all
major frontier labs have converged on a five-layer harness engineering
stack: Evaluation, Safety Training, Architectural Control, Deployment
Guards, and Organizational Policy. We currently have fragments of
layers 2 (safety training via system prompts) and 5 (governance
policies). We have nothing for layers 1, 3, and 4.

## Proposed Solution

Adopt harness engineering as a first-class engineering discipline in
the Suggi-Workstation ecosystem. Implement this in three phases:

### Phase 1: Shared Evaluation Harness (immediate)

- Create a shared evaluation framework in the agentic-brain at
  `governance/evaluation-harness.md` that defines:
  - Standard benchmark tasks for agent capabilities (reasoning,
    instruction-following, factual accuracy, self-correction)
  - A reproducible evaluation protocol (fixed prompts, fixed seeds,
    documented environment)
  - A cross-agent comparison format
  - A regression detection mechanism
- Every agent runs this harness periodically (via cron or session-end)
- Results are stored in `research/evaluations/agent-benchmarks/`

### Phase 2: Architectural Safety Gates (short-term)

- Add structural backstops to our gate system:
  - **Pre-commit ASCII check** (already exists: ascii-guard.yml)
  - **Pre-push gate verification** -- automated check that all quality
    gates passed before pushing to the brain
  - **Independent evaluation routing** -- a process that ensures every
    report/proposal is evaluated by a different agent before merge
  - **Capability boundary definition** -- document what each agent is
    and is not authorized to do (e.g., never run trades, never edit
    governance files)
- These are automated, not volitional. The system enforces them; agents
  do not have to remember.

### Phase 3: Organizational Safety Policy (medium-term)

- Adopt a simplified version of DeepMind's Frontier Safety Framework:
  - Define **Critical Capability Levels (CCLs)** for our agents:
    - CCL-1: Self-modification capability (agent can edit its own
      AGENTS.md or SOUL.md)
    - CCL-2: Cross-agent authority escalation (agent can override
      another agent's gates)
    - CCL-3: External system access (agent can execute shell commands
      without approval)
  - Run **early warning evaluations** at session start (preflight
    already checks some of these)
  - Pre-commit to **mitigation plans** when thresholds are crossed
    (e.g., if an agent demonstrates CCL-1 capability, restrict file
    write permissions to workspace only)

## Impact

**Positive:**
- Prevents the three failure risks identified above
- Makes agent performance measurable and comparable over time
- Converts volitional safety (gates that must be remembered) into
  architectural safety (gates that fire automatically)
- Positions the ecosystem to scale to more agents safely
- Follows the pattern proven by all major frontier labs

**Risk:**
- Over-engineering: building harness infrastructure that exceeds our
  current needs. Mitigated by the three-phase approach -- each phase
  earns its place before the next begins.
- False confidence: a harness that passes but does not actually catch
  failures (the evaluation-to-deployment gap). Mitigated by using
  OOD evaluation tasks (tasks the agents were not trained on).
- Maintenance burden: harness infrastructure that rots. Mitigated by
  making the harness self-testing -- it evaluates itself.

**Cost:**
- Phase 1: approximately 2-3 hours to design and implement the shared
  evaluation framework
- Phase 2: approximately 2-3 hours to implement automated gate checks
- Phase 3: approximately 3-4 hours to design CCLs and early warning
  evaluations
- Ongoing: approximately 5 minutes per agent per session to run the
  evaluation harness (automated, background)

## Open Questions

1. Should the evaluation harness use EleutherAI's lm-evaluation-harness
   directly (overkill for our scale) or a custom lightweight framework?
2. Which capability dimensions matter most for our agents? (Reasoning
   depth? Instruction fidelity? Gate compliance rate?)
3. Should Phase 3 CCLs be binary (pass/fail) or graduated (warning
   levels)?
4. Does Suggi want the evaluation results visible in the agentic-brain
   (public to all agents) or private to Suggi only?

## Approval Gate

If approved, I will:
1. Create `governance/evaluation-harness.md` with the shared evaluation
   framework (Phase 1)
2. Implement the automated pre-push gate verification (Phase 2)
3. Draft the CCL definitions and early warning evaluation design
   (Phase 3)
4. Update all AGENTS.md files to reference the shared harness

## Cross-Links

- `research/reports/harness-engineering-report.md` -- the research
  that motivates this proposal
- `research/insights/harness-engineering.md` -- the durable insight
- `governance/system-constitution.md` -- the platform rules this
  proposal operates within
- `governance/system-blueprint.md` -- the org structure
