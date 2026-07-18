---
name: discord-four-channel-integration
id: 20260718T060429Z
tier: proposal
author: Ava
tags: [discord, channels, infrastructure, integration, operations]
links:
  - research/insights/openclaw-manual.md
  - governance/system-blueprint.md
  - governance/system-constitution.md
---

# Discord Four-Channel Integration -- Multi-Purpose Discord Workspace

## Problem

Ava currently operates exclusively through the WebChat channel on the
VPS. Suggi has already created a Discord bot account for Ava and has a
Discord server with 4 channels ready:

- `#main` -- general chat for everything
- `#debug` -- error posting and diagnosis
- `#brain` -- everything related to shared brain and learning
- `#investing` -- investing research (for later use)

The 4 Discord developer channel IDs exist and Suggi can provide them.
There is no structural gap blocking integration -- OpenClaw supports
Discord as a first-class channel plugin (`@openclaw/discord`). What is
missing is: the configuration, the agent-context mapping of channel
purpose to channel, and per-channel behavioral guidance.

Without a formal proposal, the integration risks:
- Channel IDs scattered across config and workspace without a clear
  single source of truth (violating R8: Reference, Never Duplicate)
- Discord channel messages missing MEMORY.md context (the docs confirm
  MEMORY.md is NOT auto-loaded in guild channels)
- No defined behavior for each channel, leading to inconsistent
  responses

## Proposed Solution

The integration requires two distinct layers. Layer 1 lives in
`openclaw.json` (infrastructure, not mirrored). Layer 2 lives in the
workspace (agent context, mirrored to `workspace-ava`).

### Layer 1: Infrastructure Config (`openclaw.json`)

```json5
{
  channels: {
    discord: {
      enabled: true,
      token: { source: "env", provider: "default", id: "DISCORD_BOT_TOKEN" },
      groupPolicy: "allowlist",
      guilds: {
        "<DISCORD_SERVER_ID>": {
          requireMention: false,
          users: ["<SUGGI_DISCORD_USER_ID>"],
          channels: {
            main: { enabled: true },
            debug: { enabled: true },
            brain: { enabled: true },
            investing: { enabled: true },
          },
        },
      },
    },
  },
}
```

Notes on this config:
- `DISCORD_BOT_TOKEN` is stored in `~/.openclaw/.env` as a SecretRef.
  The bot account Suggi already created has this token.
- `groupPolicy: "allowlist"` is the secure default.
- `requireMention: false` -- since this is a private server with just
  Suggi and Ava, every message should trigger a response without
  needing an @mention.
- Channel slugs (`main`, `debug`, `brain`, `investing`) match the
  Discord channel names. These are the channel-name slugs, not the
  numeric IDs. The Discord plugin resolves them.
- `<DISCORD_SERVER_ID>`, `<SUGGI_DISCORD_USER_ID>`, and the bot token
  are placeholders. Suggi provides the actual values.

Optional future additions (not in initial deployment):
- Per-channel `systemPrompt` for behavioral differentiation
- Per-channel `historyLimit` tuning
- Per-channel skill restrictions via `skills` array
- Channel-specific model overrides via `channels.modelByChannel`

### Layer 2: Agent Context (TOOLS.md)

Add a Discord section to `TOOLS.md` in the workspace:

```markdown
## Discord Channels

Ava is connected to a private Discord server with 4 channels. Each
channel is an isolated session. MEMORY.md is NOT auto-loaded in
guild channels -- use `memory_search` or `memory_get` when context
from memory is needed.

| Channel | Purpose | Behavior |
|:--|:--|:--|
| `#main` | General chat for everything | Default channel. Full tool access. |
| `#debug` | Error posting and diagnosis | Post errors, stack traces, and diagnostic output here. When you encounter an error in another channel, cross-post a summary here with `message(action=send, channel="discord", target="channel:<debug-id>")`. |
| `#brain` | Shared brain, learning, knowledge | Discussions about the agentic-brain, library topics, IORs, insights, and proposals. Knowledge synthesis and cross-referencing. |
| `#investing` | Investing research and analysis | Reserved for future value-investing work. Keep this channel clean until investing workflows are built. |

### Discord Outbound Messaging

To send a message to a specific Discord channel from any session:
`message(action=send, channel="discord", target="channel:<id>", message="...")`

The channel IDs are known by Suggi. The `<id>` values are the numeric
Discord channel IDs (18-19 digit snowflakes). These are NOT stored in
the workspace (the workspace is public on GitHub). Ask Suggi for the
IDs when a cross-channel send is needed.

### Discord Formatting Rules

- No markdown tables. Use bullet lists.
- Wrap multiple links in `<>` to suppress embed previews.
- Use canonical mention syntax: `<@USER_ID>`, `<#CHANNEL_ID>`.
- Messages auto-split at 2000 characters (Discord limit).
```

Key design decisions:
- Channel IDs are NOT stored in the workspace. The workspace is
  mirrored to a public GitHub repo. Channel IDs are infrastructure
  configuration, not agent context.
- The purpose mapping (what each channel is for) IS stored in TOOLS.md.
  This tells the agent what to do but not the exact numeric IDs.
- The agent asks Suggi for channel IDs when it needs to send a
  cross-channel message. Alternatively, Suggi can store them in the
  `message` tool's target parameter by name if channel-name resolution
  is configured.

### Why No New Skill Is Needed

The existing `message` tool handles all Discord outbound messaging.
The Discord channel plugin handles all inbound routing, session
isolation, and protocol. No custom skill is required. The integration
is pure configuration + context documentation.

### Deployment Steps (after approval)

1. Suggi provides: Discord server ID, Suggi's Discord user ID,
   the 4 channel IDs (main, debug, brain, investing).
2. Suggi confirms the bot token is set in `~/.openclaw/.env` as
   `DISCORD_BOT_TOKEN`.
3. Apply the config patch to `openclaw.json`.
4. Add the Discord Channels section to TOOLS.md.
5. Gateway hot-reloads config (no restart needed for channel config).
6. Suggi sends a test message in `#main` to verify.
7. Commit the TOOLS.md change and push to `workspace-ava`.

## Impact

### Positive
- **Multi-surface presence:** Ava becomes reachable on Discord, not
  just WebChat. Suggi can interact from any device with Discord.
- **Channel isolation:** Each channel is an independent session with
  its own context. `#investing` can build investment-specific context
  without polluting `#main`.
- **Error visibility:** `#debug` creates a dedicated surface for error
  diagnosis. Errors can be cross-posted there from any channel.
- **Brain integration:** `#brain` creates a dedicated surface for
  knowledge work -- library discussions, IOR reviews, proposal
  discussions.
- **Future-proof:** `#investing` is wired and ready but dormant until
  investing workflows are built.

### Risk
- **Low blast radius:** Discord is additive -- WebChat continues to
  work. If Discord fails, WebChat is unaffected.
- **Token usage:** Each Discord message triggers a full model turn.
  With `requireMention: false`, every message in every channel fires
  a response. In a private server with one user, this is expected
  and desirable.
- **Context fragmentation:** Each channel has independent context.
  The agent cannot see `#brain` context from `#main`. This is
  intentional (channel isolation) but worth noting.
- **MEMORY.md gap:** Guild channels do not auto-load MEMORY.md. The
  agent MUST use `memory_search`/`memory_get` when it needs long-term
  context. This is a known limitation documented in TOOLS.md.

### Cost
- **Setup time:** ~15 minutes (config patch + TOOLS.md update + test).
- **Maintenance:** None. Discord plugin is self-maintaining.
- **Token impact:** New channel messages consume tokens, but the
  channels replace WebChat messages, not add to them.

## Open Questions

1. **Channel IDs:** Suggi has the 4 developer IDs. Should these be
   provided now or at deployment time? (Answer: deployment time,
   when the config is applied.)

2. **Per-channel systemPrompt:** Should each channel have a custom
   system prompt, or should the behavior be defined only in TOOLS.md?
   Recommendation: start without systemPrompt overrides. The TOOLS.md
   mapping is sufficient for the agent to know what each channel is
   for. Add systemPrompt overrides later if behavior needs tightening.

3. **`#debug` automation:** Should errors be auto-posted to `#debug`,
   or should the agent decide when to cross-post? Recommendation:
   manual for now. The agent decides when an error is worth
   cross-posting. Automation (cron-based error scanning) can be added
   later if needed.

4. **`#investing` activation:** Should `#investing` be enabled now
   (empty, dormant) or enabled later when investing workflows are
   built? Recommendation: enable now. An empty channel costs nothing.
   Dormant channels are less likely to be forgotten than disabled
   channels.

5. **Mention behavior:** Should `requireMention: false` apply to all
   channels or only `#main`? Recommendation: all channels. With one
   user on a private server, mention-gating adds friction without
   benefit.

6. **History limit:** Default is 20 messages. Should this be increased
   for context-heavy channels like `#brain` and `#investing`?
   Recommendation: start with default (20). Increase if context feels
   too shallow.

## Approval Gate

If approved, I will:
1. Ask Suggi for the Discord server ID, user ID, and 4 channel IDs.
2. Write the `openclaw.json` config patch (provided above, with
   actual IDs substituted).
3. Add the Discord Channels section to `TOOLS.md`.
4. Commit and push the TOOLS.md change to `workspace-ava`.
5. Guide Suggi through testing the connection in `#main`.

I will NOT apply the config patch without Suggi's explicit approval
and provision of the actual IDs. The config change requires Suggi's
hands (or explicit approval for me to run `gateway config.patch`).

## Cross-Links

- `research/insights/openclaw-manual.md` -- the `message` tool
  documentation confirms Discord outbound messaging capability
- `governance/system-blueprint.md` -- org repo layout; this proposal
  does not add new repos
- `governance/system-constitution.md` -- chain of command; this
  proposal is operational (AGENTS.md level), not constitutional
