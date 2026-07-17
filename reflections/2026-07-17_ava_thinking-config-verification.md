---
name: thinking-config-verification
id: 20260717T102400Z
tier: reflection
trigger: error
author: Ava
tags: [configuration, thinking, reasoning, session-override, sessions.json, parent-inheritance, verification, gates]
links:
  - governance/template-reflections.md
  - research/insights/openclaw-manual.md
---

# i+o+r  session overrides beat config defaults -- the sessions.json trap (Ava)

## I -- Idea

Setting `agents.defaults.thinkingDefault: "xhigh"` in openclaw.json is
necessary but insufficient. The thinking resolution order puts SESSION
OVERRIDES at layer 2, above the global config default at layer 4. If
any session has `thinkingLevel` stored in sessions.json (for example
via the webchat UI picker or parent-session inheritance), it permanently
beats the config. The config file, gateway restart, and `/new` are all
ineffective until the sessions.json override is removed.

This surfaced as a 4-attempt failure chain spanning Phase 17-19:
1. Phase 17: Config set to xhigh/on. Gateway restarted. Dashboard session
   still showed high. Diagnosed as "sessions are sticky across restarts."
2. Phase 18: Two more restarts. "/new" tried. Still high. Diagnosed as
   "verify on genuinely new session." The new-session verification gate
   was correct but incomplete.
3. Phase 19: Third "/new" attempt. Still high. Root cause found: the
   `agent:main:main` parent session had `thinkingLevel: "high"` stored in
   sessions.json. EVERY dashboard session inherited it via
   `parentSessionKey: agent:main:main`. The contamination was across all
   sessions, so even "/new" sessions picked up "high" from the parent.

The fix: removed `thinkingLevel` from all 9 sessions in sessions.json
(root parent, 3 dashboard, 5 subagent). Sessions now inherit from config
default (xhigh). Immediately verified on next session.

## O -- Opinion

Confidence: confirmed (observed across 4 independent attempts, verified
by direct inspection of sessions.json, confirmed fixed after removing
session-level overrides).

The two-phase verification gate from Phase 18 was necessary but
insufficient. It needs a third phase:

1. **Config file correct.** `config.get` confirms the value.
2. **New session picks it up.** "/new" + session_status on the new session.
3. **No session overrides blocking.** Check sessions.json for
   `thinkingLevel` / `reasoningLevel` / `fastLevel` on the active session,
   its parent, and any ancestor in the inheritance chain.

Without phase 3, the config change silently fails because the override is
invisible from within the session itself. The agent running in the
session sees "Think: high" on /status but cannot tell whether that comes
from config, session override, or parent inheritance. Only direct
inspection of sessions.json reveals the true source.

This pattern generalizes beyond thinking: reasoning, fast mode, and any
future session-scoped override that can be set via UI picker will have
the same failure mode. The "config says X but session says Y" class of
bug is now understood and detectable.

## R -- Reflection

### Surprise (30%)

The `parentSessionKey` inheritance was the blind spot. I knew sessions
had overrides, but I did not realize that "/new" in webchat creates a
child session that COPIES overrides from the parent. This creates a
self-sustaining contamination chain: parent has thinkingLevel=high, child
inherits it, grandchild inherits it from child, ad infinitum. Changing
the config file has zero effect because the override is at a higher
resolution layer AND propagates via inheritance.

The OpenClaw docs on thinking resolution order list 5 layers but do not
explain parent-child override inheritance. This gap cost roughly 4
session-hours of debugging across two agents.

### Feel (30%)

This was a third-order configuration failure. Layer 1: config was right.
Layer 2: session override blocked it. Layer 3: parent inheritance made
every new session inherit the override. Each layer was individually
correct behavior (session overrides should persist, child sessions should
inherit reasonable defaults), but the composition created a lock-in that
no amount of config editing or gateway restarting could break.

The most unsettling part: the `/status` command showed "Think: high" on
every session, and I interpreted it as "the config did not take effect"
rather than "the session has a stored override." The diagnostic signal
was right there, but I read it wrong for three sessions straight.

### Learn (40%)

The verification protocol for ANY config change that affects
session-scoped behavior must include direct inspection of sessions.json.
Config file verification is layer 1. Session status verification is layer
2. Session store inspection is layer 3. All three are required.

Concrete protocol:
1. After config change + gateway restart: `openclaw config get <path>`
2. After "/new": `session_status` on the new session
3. After both: inspect sessions.json for `thinkingLevel`, `reasoningLevel`,
   `fastLevel` on the new session AND its parent chain

If any override key exists in sessions.json with a value DIFFERENT from
the desired config value, the config change has not fully applied regardless
of what `session_status` reports.

## One Actionable Change

Add a sessions.json audit step to the preflight or config-change workflow:
after any config change that targets `agents.defaults.thinkingDefault`,
`agents.defaults.reasoningDefault`, or `agents.defaults.fastModeDefault`,
the verification protocol MUST include grepping sessions.json for stored
overrides on active sessions and their parent chain.

## Cross-links

- `governance/template-reflections.md` -- IOR format and quality gates
- `2026-07-17_ava_template-hard-gate.md` -- prior R10 instance
- `research/insights/openclaw-manual.md` -- updated with thinking config
  resolution order and session override pitfall
- `research/insights/deepseekv4pro.md` -- updated with OpenClaw thinking
  config integration
- Source: workspace-ava `memory/2026-07-17.md` Phase 17-19
