---
name: cron-agent-scoping-as-workspace-isolation
id: 20260725T180720Z
tier: reflection
trigger: session-end
author: Ava
tags: [cron, openclaw, architecture, workspace-isolation, agent-scoping, sub-agent]
links:
  - governance/system-blueprint.md
  - research/insights/library-system.md
---

# OpenClaw Cron Agent-Scoping Is Workspace Isolation by Design, Not a Deficiency

## I -- Idea

OpenClaw's cron system intentionally scopes cron jobs to their owning
agent. The `agentId` field determines both management visibility and
execution workspace for isolated runs. This means sub-agent cron jobs
are invisible to the main agent's `cron` tool, and cross-agent
management requires the CLI. This is a feature, not a bug: the scoping
preserves workspace isolation for sub-agents.

I discovered this while setting up Suggi's library pipeline. Three cron
jobs owned by researcher-1 ran the discoverer, writer, and auditor
skills. When I ran `cron list` from my session (agent: main), it
returned zero results. The crons existed -- I found them via
`openclaw cron list --all` on the CLI -- but they were invisible to my
tool set. The CLI bypass was the only way to manage them.

## O -- Opinion

This is the correct architecture. Confidence: high (85%).

The alternative -- a global cron tool visible to all agents that can
manage any agent's crons -- would undermine workspace isolation. A
researcher-1 cron job must execute in researcher-1's lean workspace
(AGENTS.md + TOOLS.md + README.md), not main's bootstrap-heavy
workspace (SOUL.md, MEMORY.md, IDENTITY.md, etc.). The `agentId` field
is the only mechanism that guarantees this binding.

The friction point (discovery requiring CLI) is a documentation
problem, not an architecture problem. The fix: store cron IDs in
MEMORY.md (injected every session) with CLI commands in TOOLS.md. This
makes cross-agent cron management a known pattern rather than a
surprise on every new session.

The deeper insight: OpenClaw's agent model is genuinely multi-tenant.
Each agent has its own workspace, its own cron jobs, its own tool
surface. The operator surface (CLI, Gateway API) is the management
layer that spans agents. This separation is clean and intentional.

## R -- Reflection

### Surprise (30%)
I expected `cron list` from main to show all cron jobs across all
agents. It showed zero. My mental model treated OpenClaw's cron tool
like a system scheduler; it is actually a per-agent scheduler. I
expected global visibility; the system enforces per-agent scoping. The
gap between expectation and reality was the entire motivation for this
insight.

### Feel (30%)
Frustration at discovery, then appreciation. The initial "why cannot I
find these?" was a training problem, not an architecture problem. Once
I understood the design, the solution (CLI + documentation) was
obvious. This pattern -- friction leading to documentation rather than
architectural change -- is a sign of good engineering. The fix is
durable without touching the core design.

### Learn (40%)
1. Multi-agent cron management in OpenClaw follows a clear pattern:
   agentId equals ownership plus workspace. CLI is the operator
   surface. The cron tool is per-agent convenience, not global
   infrastructure.
2. Crossing agent boundaries for management operations is expected to
   require operator-level tools. This is not a missing feature; it is
   a security boundary.
3. Documentation that fires automatically (injected workspace files)
   is the right fix for discovery problems. TOOLS.md and MEMORY.md now
   contain the cron IDs and management commands, visible on every
   session start.

## One Actionable Change
Added a Cron Management section to TOOLS.md with CLI commands and
rationale, and a Cron Jobs table to MEMORY.md with job IDs, agents,
schedules, and status. Both files are injected on every session start,
eliminating future discovery friction. Any agent following this pattern
can manage cross-agent crons without hunting.

## Cross-links
- `research/insights/library-system.md` -- full pipeline blueprint
  including cron scheduling rationale
- `governance/library-discoverer.md` -- discoverer skill with queue
  capacity cap (25) added in same session
