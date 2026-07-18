---
name: two-layer-channel-configuration
id: 20260718T071159Z
tier: reflection
trigger: research
author: Ava
tags: [discord, channels, architecture, configuration, security]
links:
  - research/insights/openclaw-manual.md
  - research/proposals/discord-four-channel-integration.md
---

# Two-Layer Channel Configuration -- Config vs. Context Separation

## I -- Idea
Channel integration in OpenClaw requires a clean two-layer separation:
infrastructure configuration (how to connect) lives only in
`openclaw.json` (private), while channel purpose mapping (what to do)
lives in workspace context files like TOOLS.md (public-safe mirror).
Naively putting channel IDs in the workspace leaks infrastructure
details into a public GitHub mirror. Naively keeping purpose mapping
only in config means the agent has no behavioral context for what each
channel is for. The two-layer pattern solves both problems.

Suggi asked where to store Discord channel info for 4 channels
(#main, #debug, #brain, #investing) and whether a new skill was needed.
Research across 5 OpenClaw docs (discord.md, config-channels.md,
channel-routing.md, plugin-reference/discord.md, openclaw-manual.md)
confirmed: no skill needed (the `message` tool handles outbound), but
the information architecture matters. Channel IDs are not secrets per
se, but they are infrastructure details that should not appear in a
public-facing workspace mirror. The purpose mapping is agent context
that belongs in the workspace.

Before this session, I assumed channel integration was a single-layer
problem -- put everything in config. The Feynman blank page revealed
I understood the config structure but had not thought through the
security boundary between infrastructure and agent context.

## O -- Opinion
Confidence: high (90%). The two-layer pattern is not opinion -- it is
derived from hard constraints. The workspace IS mirrored to a public
GitHub repo. The config IS NOT. This is not a preference; it is a
boundary enforced by the system architecture.

The pattern extends beyond Discord. Any future channel integration
(Telegram, Slack) follows the same rule: channel IDs, tokens, and
connection details stay in config. Purpose mapping, behavioral
guidance, and formatting rules stay in workspace context. The
boundary is the mirror line.

The one nuance: channel IDs are not secrets. Someone who discovers a
Discord channel ID cannot do much with it without the bot token. But
"not a secret" is not the same as "belongs in a public repo." The
principle is minimization -- the workspace should contain only what
the agent NEEDS to operate, not every piece of infrastructure data.

One additional finding: MEMORY.md is only auto-loaded in Discord DMs,
not guild channels. This is documented in the OpenClaw Discord docs
but was unknown to me before this session. The fix is operational
(use memory_search/memory_get on demand), documented in the TOOLS.md
section of the proposal.

## R -- Reflection

### Surprise (30%)
I expected channel integration to be a straightforward config exercise.
I did not expect the two-layer architecture to be the central design
decision. The depth of OpenClaw's Discord support (voice channels,
thread binding, streaming previews, component v2 UI, exec approvals,
multi-account) was also surprising -- the Discord plugin is not a thin
wrapper but a deep, production-grade integration.

The interaction between Feynman contamination and this session was
unexpected. I had already read the Discord docs during preflight
research before the blank-page step, which partially contaminated the
diagnostic. The blank page captured the core architecture correctly
but missed the security boundary detail (no IDs in workspace). That
detail emerged during research, not blank-page -- which is evidence
that the contamination was real but limited.

### Feel (30%)
Satisfied with the proposal. The 4-channel structure (#main, #debug,
#brain, #investing) maps cleanly to the agent's architecture. Each
channel gets an isolated session with independent context. The
two-layer pattern is elegant -- it resolves the tension between "the
agent needs to know what channels are for" and "the workspace is
public." That is good architecture.

Mild frustration at the recurring Feynman contamination. This is the
second session where the contamination flag gap (v4.4) was observed
but not fixed. The structural fix exists on paper but is not
implemented. The pattern: I notice contamination, I document it, I
do not fix the procedure. This is itself a failure class worth
gating against.

### Learn (40%)
1. Channel integration has a natural two-layer architecture. The
   boundary between config (private) and context (public-safe) is
   not a preference -- it is enforced by the workspace mirror
   architecture. Future integrations use this pattern by default.
2. Channel IDs are not secrets but still do not belong in the
   workspace. The test is: "does the agent need this to operate, or
   does it need this to connect?" Connection data stays in config.
   Operational data goes in context.
3. The Feynman contamination fix needs implementation, not just
   documentation. Every session that observes the contamination gap
   without fixing it is a session where the failure class recurred
   without structural change. The fix (contamination flag in the
   Feynman Loop procedure) is simple and known. The gap is
   implementation, not discovery.

## One Actionable Change
When the Discord integration is deployed (post-approval), verify the
TOOLS.md entry against the actual channel behavior: does the agent
correctly differentiate channel purposes? Does the MEMORY.md gap cause
confusion? If yes, add a structural gate (per-channel systemPrompt with
memory_search instructions).

## Cross-links
- `research/proposals/discord-four-channel-integration.md` -- full
  proposal with config structure, deployment steps, and open questions
- `research/insights/openclaw-manual.md` -- message tool documentation
  confirming Discord outbound capability
