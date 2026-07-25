---
name: cron-agent-scoping-as-workspace-isolation
id: 20260725T180415Z
tier: reflection
trigger: session-end
author: Ava
tags: [cron, openclaw, architecture, workspace-isolation, agent-scoping, sub-agent]
links:
  - brain:governance/system-blueprint.md
  - research/insights/library-system.md
---

# OpenClaw Cron Agent-Scoping Is Workspace Isolation by Design, Not a Deficiency

## I -- Idea

OpenClaw's cron system ties `agentId` to execution workspace for
isolated sessions. The cron tool is per-agent scoped, not a global
operator tool. This is by design, not a bug -- it preserves workspace
isolation for sub-agents at the cost of cross-agent discoverability.

Context: Suggi's library pipeline uses three sub-agents (researcher-1,
researcher-2, investor) with lean workspaces. Cron jobs owned by
researcher-1 use that agent's workspace for isolated runs. When I
(main) tried to list them, my cron tool showed zero results. The
crons were invisible not because they failed to exist, but because
OpenClaw's cron tool is scoped to the calling agent. Cross-agent
management requires the CLI (`openclaw cron list --all`) which
bypasses agent scoping as an operator-admin operation.

## O -- Opinion

This is the correct architecture. Confidence: high (85%+).

The alternative -- a global cron tool visible to all agents that can
manage any agent's crons -- would undermine workspace isolation. A
researcher-1 cron job MUST execute in researcher-1's lean workspace,
not main's bootstrap-heavy workspace. The `agentId` field is the only
mechanism that guarantees this binding.

The friction point (discovery requiring CLI) is documentation, not
design. The fix: store cron IDs in MEMORY.md (injected every session)
with CLI commands in TOOLS.md. This is a documentation pattern, not
an architectural change.

The real insight: OpenClaw's agent model is genuinely multi-tenant.
Each agent has its own workspace, its own cron jobs, its own tool
surface. The operator surface (CLI, Gateway API) is the management
layer that spans agents. This separation is clean and intentional.

## R -- Reflection

**Surprise:** I assumed `cron list` from main would show all crons.
It showed zero. My mental model treated OpenClaw's cron tool like a
system scheduler; it is actually a per-agent scheduler. I expected
global visibility; the system enforces per-agent scoping.

**Feel:** Frustration at discovery, then appreciation. The initial
"why can't I find these?" was a training problem, not an architecture
problem. Once I understood the design, the solution (CLI + docs) was
obvious. This is good engineering: the friction led to a durable fix
(TOOLS.md + MEMORY.md entries) rather than a workaround.

**Learn:** Multi-agent cron management in OpenClaw follows a clear
pattern: agentId = ownership + workspace. CLI = operator surface.
The cron tool = per-agent convenience. Document the crons in files
that are injected on startup; no hunting needed.

**Actionable change:** Added Cron Management section to TOOLS.md
(injected every session) and cron ID table to MEMORY.md. Any agent
can now reference crons by ID via CLI without searching. The batch
size in brain-index config.yaml should be reduced to 8 to prevent
OOM on 8GB VPS.
