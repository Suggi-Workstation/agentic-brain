---
name: multi-agent-architecture-industry-validated
id: 20260718T165412Z
tier: reflection
author: Ava
tags: [reflection, architecture, multi-agent, subagents, decorrelation, validation]
links:
  - brain:governance/system-blueprint.md
  - brain:research/proposals/subagent-workspace-routing-proposal.md
  - memory/2026-07-18.md
---

# IOR: Multi-agent architecture independently matches all 3 industry-standard patterns

## Idea

Our multi-agent architecture -- Ava as orchestrator, two decorrelated
researchers with different models, a future investor, and isolated
workspaces per agent -- was designed from first principles (lean
workspaces, decorrelation, specialization). Independent research
against 2026 industry sources confirmed it matches all three dominant
multi-agent patterns without having referenced them during design.

## Opinion

This is validation, not coincidence. The architecture emerged from
constraints (one VPS, one Gateway process, one user, need for
decorrelated review) that naturally converged on patterns the industry
independently discovered for the same reasons. The three patterns:

1. **Orchestrator-Worker** (Microsoft, LangGraph, Claude Code) --
   one conductor delegates to specialist workers. Our implementation:
   Ava spawns researcher-1 + researcher-2 via sessions_spawn.

2. **Parallel Research** (DeepYard, Anthropic) -- multiple agents
   investigate the same question independently, a synthesizer
   cross-checks. Our implementation: R1 + R2 with different models,
   Ava reads both and delivers the verdict.

3. **Workspace Isolation** (OpenClaw docs, community guides) --
   separate workspaces, auth, skills, and memory per agent. Our
   implementation: each agent has its own workspace mirrored to
   GitHub, own skills folder, explicit skills allowlist, no shared
   state.

The architecture was not copied from these sources. It was derived
from constraints. That it converges on them suggests the constraints
are fundamental -- anyone solving the same problem (lean specialist
agents on one Gateway with decorrelation) would arrive at the same
structure.

## Reflection

The architecture phase is now structurally complete. The blueprint
matches the live org. The config is explicit. The workspaces exist.
The patterns are validated. What remains is population: choosing
models, building the write-library skill, adding loop-feynman to
the researchers, and running the first decorrelated research pair.

The next session should focus on selecting sub-agent models and
populating the first skill into the researchers' workspaces.

## Surprise (30%)

I did not expect independent research to align this cleanly with our
homegrown design. The convergence is stronger than anticipated -- not
just "similar ideas" but exact pattern matches. The Microsoft
orchestrator-subagent documentation reads like a description of our
config. The OpenRouter rate-limit docs confirmed one key is sufficient
without us guessing.

## Feel (30%)

Satisfaction. The architecture is not just "our way" -- it is THE way.
That gives confidence as we move from design to operation. But also
humility: we did not invent these patterns. We rediscovered them,
which means the constraints are real and universal.

## Learn (40%)

When architecture is constraint-driven rather than pattern-driven, it
converges on best practices without needing to consult them. The
patterns emerge from solving the problem honestly. This is the Munger
approach -- invert, find what guarantees failure, do the opposite.
Our constraints (single user, single Gateway, need for decorrelation,
lean workspaces) inverted into: one orchestrator, two parallel workers,
isolated workspaces. The patterns were waiting there.

## One Actionable Change

When building future architecture (new agent types, skill distribution,
cron workflows), derive from constraints first, then validate against
industry patterns. Never start from patterns and force-fit the problem
into them. Constraint-first, pattern-second.
