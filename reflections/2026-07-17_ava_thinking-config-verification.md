---
name: thinking-config-verification
id: 20260717T102400Z
tier: reflection
trigger: error
author: Ava
tags: [configuration, thinking, reasoning, reload-kind, verification, gates, sessions]
links:
  - governance/template-reflections.md
---

# i+o+r  config reloadKind:none needs new-session verification (Ava)

## I -- Idea

Config values marked `reloadKind: "none"` in the OpenClaw schema load only
at gateway startup AND only apply to genuinely new sessions. Verifying the
config file and `config.get` is necessary but insufficient. The persistent
dashboard session (webchat Control UI) survives gateway restarts with its
original thinking/reasoning values intact. Without a phase-2 verification
on a genuinely new session, the config change is unproven.

This surfaced when Suggi set `thinkingDefault: "xhigh"` and
`reasoningDefault: "on"` via `openclaw config set`. The config file was
correct, the gateway was restarted, but the dashboard session still showed
`Think: high` and `Fast: off`. Two gateway restarts later, the same
session still showed the old values. The root cause was not a config
failure -- it was a verification failure. The dashboard session key
persisted across restarts and kept the values baked in at creation time.

## O -- Opinion

Confidence: high (observed across two gateway restarts, confirmed by
`config.schema.lookup` showing `reloadKind: "none"` on both fields).

Every `reloadKind: "none"` config change needs a two-phase verification
gate:

1. **Config file correct.** `config.get` confirms the value.
2. **New session picks it up.** Start a genuinely new session (not the
   persistent dashboard session) and check with `/status` or
   `session_status`.

Without phase 2, the change is aspirational. The phase-1 signal ("config
is xhigh") is contradicted by the phase-2 observation ("session is
high"), and only phase 2 tells you the real state of the system.

This is a specific instance of a general pattern: verifying config
correctness from within the session that the config was supposed to
change is circular. You need an independent observer -- a fresh session.
The dashboard session is convenient but always stale for config-change
verification.

## R -- Reflection

### Surprise (30%)

The dashboard session key (`agent:main:dashboard:...`) survived the
gateway restart. I assumed gateway restart == clean slate for the
webchat session. Wrong. Sessions are stateful entities managed by the
gateway, and the dashboard session is sticky by design -- it persists
across restarts so the user does not lose their conversation. The
thinking/reasoning defaults are baked into the session at creation
time and are immutable for that session's lifetime.

This is correct behavior (you do not want thinking mode changing
mid-conversation), but the docs do not call it out explicitly, and
it created a two-hour blind spot where I believed the config was
applied when it was not.

### Feel (30%)

This is a second-order configuration failure. The config was right.
The gateway restart happened. The preflight verified the config.
But the observer (me) was verifying from inside the stale session,
so the measurement itself was contaminated. I was the broken
thermometer checking my own calibration.

The frustration is that I checked everything except the one thing
that mattered: what does a NEW session see? The dashboard session
was the default testing surface, and its stickiness made it the
wrong one.

### Learn (40%)

The verification protocol for `reloadKind: "none"` config changes
needs a structural gate: "Verified on a new session."

Concretely, after any config change with `reloadKind: "none"` + gateway
restart:

1. Create a fresh session (via `/new` or a new channel message).
2. Run `session_status` on that new session.
3. Confirm the expected values appear.
4. Only then declare the change applied.

The dashboard/webchat session is NEVER a valid verification surface
after config changes -- it is always the old session.

## One Actionable Change

Add a preflight-like gate to the config-change workflow: after any
`reloadKind: "none"` config change with gateway restart, the session-end
protocol must include creating a fresh session (via `/new`) and verifying
the new defaults are active before logging the change as complete.

## Cross-links

- `governance/template-reflections.md` -- IOR format and quality gates
- `2026-07-17_ava_template-hard-gate.md` -- prior instance of R10
  (Bootstrap Propagation) in template fix workflow
- Source: workspace-ava `memory/2026-07-17.md` Phase 17-18
