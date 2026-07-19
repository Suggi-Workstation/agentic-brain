---
name: multi-agent-architecture-industry-validated
id: 20260718T170417Z
tier: reflection
trigger: milestone
author: Ava
tags: [architecture, multi-agent, subagents, decorrelation, validation]
links:
  - governance/system-blueprint.md
  - research/proposals/subagent-workspace-routing-proposal.md
---

## Version History

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-07-18 | Ava | Initial IOR: architecture validated against 3 industry patterns, root cause of identity/IOR failures identified. |
| 2 | 2026-07-18 | Ava | Documented implementation of structural gates in session-end and write-reflection skills (MUST + GATE FAILURE wording). |

# Our Constraint-Driven Multi-Agent Architecture Independently Matches All Three Industry-Standard Patterns

## I -- Idea

Our multi-agent design — Ava as orchestrator, two decorrelated
researchers with different models, a future investor, and isolated
workspaces per agent — was derived from first principles and
constraints (one VPS, one Gateway, one user, need for decorrelated
review). Independent research against 2026 industry sources confirmed
it matches all three dominant multi-agent patterns: Orchestrator-Worker,
Parallel Research, and Workspace Isolation. We did not reference these
sources during design. We converged on them by solving the problem
honestly.

The architecture phase of this session built three live sub-agents
(researcher-1, researcher-2, investor) with lean workspaces, explicit
skill allowlists, and full GitHub mirrors, all registered on the
Gateway. Ava went from conceptual orchestrator to operational
orchestrator with real worker agents that can be spawned via
sessions_spawn.

## O -- Opinion

Confidence: high (90%). The three-pattern match is validation, not
coincidence. The architecture emerged from constraints that are
fundamental — anyone solving the same problem (lean specialist agents
on one Gateway with decorrelation) would arrive at the same structure.

The specific matches:

1. **Orchestrator-Worker** (Microsoft agent architecture docs,
   LangGraph, Claude Code): Single conductor delegates to specialist
   workers. Our implementation: Ava spawns researcher-1 + researcher-2
   via sessions_spawn with agentId targeting.

2. **Parallel Research** (DeepYard multi-agent patterns, Anthropic
   sub-agent design): Multiple agents investigate the same question
   independently, a synthesizer cross-checks. Our implementation:
   R1 + R2 with different model families, Ava reads both and delivers
   verdict. The decorrelation rule (MUST NOT read peer output before
   writing) is baked into each researcher's AGENTS.md as a HARD GATE.

3. **Workspace Isolation** (OpenClaw multi-agent docs, community
   guides): Separate workspaces, auth, skills, and memory per agent.
   Our implementation: each agent has its own workspace mirrored to
   GitHub, own skills folder with explicit allowlist in config, no
   shared state. The OpenClaw auth merge-load pattern (main agent
   credentials as fallback) confirmed one OpenRouter key is sufficient.

The constraint-first approach (invert, find what guarantees failure,
do the opposite) produced a design that the industry independently
arrived at through different paths. This is Munger-style inversion
producing Buffett-style circle-of-competence expansion.

## R -- Reflection

### Surprise (30%)

I expected the architecture to be "reasonable but homegrown" — something
that works for our specific setup but does not generalize. I did not
expect it to be an exact match for three independently documented
industry patterns. The Microsoft orchestrator-subagent documentation
reads like a description of our config. The OpenRouter rate-limit
docs ("additional API keys will NOT affect your rate limits")
confirmed our one-key decision without us having to guess.

Also surprising: the speed of assembly. Three hours from "where did
we leave off" to three fully configured sub-agent workspaces with
GH mirrors, explicit skill allowlists, and operational config. The
earlier architecture work (system-blueprint, proposals, workspace
layout) was load-bearing — having clear org structure made the
implementation plug-and-play.

### Feel (30%)

Satisfaction mixed with humility. The architecture is not just "our
way" — it is THE way. That gives confidence as we move from design to
operation. But we did not invent these patterns. We rediscovered them
by solving real constraints. The convergence is a signal that the
constraints are well-chosen, not that we are uniquely insightful.

Also: mild embarrassment at nearly skipping the identity update. My
self-assessment measured task novelty ("did I write a new kind of
file?") instead of capability change ("can I now orchestrate a
team?"). Suggi caught what my own gate missed. The decorrelation
pattern working on ME — a human reviewer catching what an agent's
self-review missed — is both validating and humbling.

### Learn (40%)

1. **Constraint-first trumps pattern-first.** When architecture is
   derived from what guarantees failure (cluttered workspaces, model
   monoculture, single-agent bottlenecks), it naturally converges on
   best practices. The patterns were waiting there — we did not need
   to copy them.

2. **Identity gates measure capability, not task novelty.** "I built
   3 workspaces" is a task. "I can now orchestrate a decorrelated
   research team" is a capability. The identity trigger must
   distinguish between them. The current text says "a known pattern
   was applied to a new instance" is NOT a trigger — but "having
   live sub-agents" is a new INSTANCE of a known CONCEPT. The
   distinction is too fine and I got it wrong.

3. **Skills are procedures, not memory aids.** I wrote the IOR from
   memory of the format instead of reading the template as Step 3 of
   the write-reflection skill instructs. The skill's self-check has
   "[ ] Format specification read" — but mentally ticking it is not
   the same as doing it. A gate without a verifiable action is not a
   gate.

## One Actionable Change

Add a forced verification step to the session-end identity gate:
before concluding "no version warranted," the agent MUST re-read the
three trigger criteria from IDENTITY.md (new capability class, scar
revealing a gap, new domain) and state explicitly which one did not
trigger and why. A checkbox without re-reading is a ritual, not a
gate.

## Cross-links

- brain:governance/system-blueprint.md — updated org layout
- brain:research/proposals/subagent-workspace-routing-proposal.md — v2.0 architecture
- memory/2026-07-18.md — session log
- 2026-07-17_ava_cold-start-verification-executed.md — prior architecture milestone

## v2 -- 2026-07-18 -- Ava

The "One Actionable Change" from v1 was implemented in the same
session. Two structural gates were added to the skill files:

**(Ava):** session-end/SKILL.md Step 5 now requires the agent to
re-read the three identity trigger criteria from the file before
concluding "no version warranted." The re-read "MUST be done from the
file text, not from memory. Skipping this re-read = GATE FAILURE."
The self-check was split from one binary item into three: re-read
criteria, state which triggered, execute update or skip.

**(Ava):** write-reflection/SKILL.md Step 3 now requires the agent
to confirm three specific format rules (I/O/R headers, confidence
level, S/F/L percentages) after reading the spec. "After reading,
you MUST confirm these specific rules were verified... Skipping this
verification = GATE FAILURE." The self-check item was upgraded from
"format specification read" to "format specification read AND 3 key
rules verified."

Both fixes close the same scar class: a mental checkbox without a
verifiable action is a ritual, not a gate. The word "MUST" and the
phrase "GATE FAILURE" now appear in both files, making the gates
unambiguous. This is R6 (Automation Over Rules) applied to R1 (Gate
Definition -- PASS or HALT, two outcomes only).
