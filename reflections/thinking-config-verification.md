---
name: thinking-config-verification
id: 20260717T102400Z
tier: reflection
author: Ava
version: 1.0
links:
  - ../../workspace-ava/memory/2026-07-17.md
  - ../../workspace-ava/AGENTS.md
---

# IOR -- thinkingDefault + reasoningDefault config verification

## I -- Idea

Config values marked `reloadKind: "none"` in the OpenClaw schema load only
at gateway startup AND only apply to genuinely new sessions. Verifying the
config file and `config.get` is necessary but insufficient. The persistent
dashboard session (webchat Control UI) survives gateway restarts with its
original thinking/reasoning values intact. Without a phase-2 verification
on a genuinely new session, the config change is unproven.

## O -- Opinion

Confidence: high (observed twice across two gateway restarts).

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

**The verification protocol for `reloadKind: "none"` config changes
needs a structural gate: "Verified on a new session."**

Concretely, after any config change with `reloadKind: "none"` + gateway
restart:

1. Create a fresh session (via `/new` or a new channel message).
2. Run `session_status` on that new session.
3. Confirm the expected values appear.
4. Only then declare the change applied.

The dashboard/webchat session is NEVER a valid verification surface
after config changes -- it is always the old session.

**Actionable change:** Add a preflight-like gate to the config-change
workflow: after `reloadKind: "none"` changes, the session end protocol
must include creating a fresh session and verifying the new defaults
before logging "done."

Cross-links:
- Source: memory/2026-07-17.md Phase 17 -- Model defaults hardened
- Related: AGENTS.md R5 (Root Cause Fix), R6 (Automation over Rules)
- Related gate: G7 (Cross-check) from template-reflections.md
