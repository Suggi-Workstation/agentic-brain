---
name: stale-code-refusal-is-not-a-bug
id: 20260827T134937Z
tier: reflection
trigger: surprise
author: Morpheus
tags: [infrastructure, verification, serve, debugging]
links:
  - reflections/2026-08-22_morpheus_desktop-app-state-has-three-tiers.md
  - reflections/2026-08-24_morpheus_limits-are-choices-in-disguise.md
---

# Stale-Code Refusal Is Not a Bug -- It Is a Safety Check Hiding as a Symptom

## I -- Idea

A serve that refuses to serve specific endpoints when its running code
does not match the on-disk checkout is not broken -- it is defending
itself against stale-module crashes, and the diagnostic path that reveals
this is not the one you would expect.

The session began with Suggi reporting that the model picker in the
desktop app's Settings page was broken -- no providers could be
selected, and the app kept refreshing every 20-30 seconds, interrupting
his typing. The .env keys were all present. The serve was running. The
models were configured. Everything looked correct from the
configuration side. The symptom -- periodic refresh and empty picker --
pointed at a network issue, a websocket reconnect loop, or an
onboarding stuck state. None of those were the cause.

What I found instead was a version mismatch: the Hermes Agent code on
disk had been updated to commit 5fc308a707 (v0.20.6), but the serve
process was still running the old code from commit 6ce7ab8bfb. The serve
has a safety check that compares its running code version against the
on-disk checkout. When they diverge, it refuses to serve the
`/api/model/options` endpoint -- not with a crash, not with an error
page, but with an empty response. The desktop app interprets the empty
response as "still loading" and retries. That retry loop IS the
refresh. The input losing focus is the UI re-mounting on each cycle.

This is a sophisticated guard. Most servers I have encountered either
crash on stale-module access (undefined function, missing import) or
silently serve degraded behavior with no indication. This serve
explicitly detects the version divergence and refuses to serve
endpoints that would risk a stale-module crash -- it trades an
unresponsive picker for a safe one. The symptom looks like a network
bug; the cause is an intentional safety refusal at the API layer.

## O -- Opinion

Confidence: high (90%).

This design pattern -- explicit stale-code refusal -- is the right
trade-off, and I think it should be documented as a known diagnostic
state, not treated as a bug to fix.

The alternative approaches each have worse failure modes. A serve that
crashes on stale-module access gives you a 500 error and a dead process
-- harder to diagnose, worse UX. A serve that silently serves with stale
code risks data corruption or undefined behavior when the API contract
changed between versions. The refusal approach gives you a degraded
but safe service: the endpoints that would crash are blocked, the rest
keeps working, and a restart fixes everything. The cost is that the
symptom (empty response, refresh loop) is misleading -- it looks like
a network problem when it is a version problem.

Where the design falls short is in surfacing the cause to the user. The
refusal response is empty -- no error message, no header, no log line
visible in the app UI. The diagnostic information lives only in the
serve's internal log (`agent.log`), which requires SSH access to the
VPS to read. If the serve returned a structured error like
`{"error": "stale_code_version", "running": "6ce7ab8bfb", "disk":
"5fc308a707", "action": "restart_serve"}` instead of an empty response,
the desktop app could display "Serve needs restart after update" and
the user would know exactly what to do. That is a feature request, not a
bug report.

The broader lesson is about diagnostic defaults. When an endpoint
returns empty, my instinct is to check network connectivity, firewall
rules, and websocket health. Those are the common causes. But this
session showed that the uncommon cause -- version mismatch safety
check -- can produce the same symptom. The diagnostic path that reveals
it is not "is the network working?" but "does the running code match the
disk?" That is a different question, and I would not have asked it if
the serve did not log the refusal explicitly.

## R -- Reflection

### Surprise (30%)

I expected the model picker failure to be a configuration or network
problem. The .env keys were present, the serve was active, the
websocket was connecting. Everything pointed at "the serve is fine, the
app is broken." But the serve was NOT fine -- it was running stale code
and deliberately refusing to serve the picker endpoint. I have never
encountered a server that guards against its own staleness at the
endpoint level. The surprise is not that the mechanism exists (it is a
reasonable safety measure) but that its symptom so perfectly mimics a
network problem. The empty response is indistinguishable from a
network timeout at the client level. The only way to distinguish them
is to read the serve's internal log -- which requires access the
desktop app user does not have. This is a class of debugging where the
symptom's shape (empty response) maps to multiple causes, and the
default diagnostic path (network) is the wrong one for this particular
cause.

### Feel (30%)

I spent the first several terminal calls checking websocket stability,
serve health endpoints, and API response shapes -- all the network-layer
diagnostics. None of them revealed the problem because the problem was
not at the network layer. The version mismatch only showed up when I
read the serve's `agent.log` and found the explicit refusal message.
That is the honest read: I went down the network path first because the
symptom pointed there, and I should have read the serve log earlier.
The serve log is always the first place to look when a serve endpoint
returns empty -- not the third place after network and config checks.

### Learn (40%)

1. When a serve endpoint returns empty, check for version-stale
   conditions before network conditions. The diagnostic order should
   be: (a) read the serve log for explicit refusal/error messages, (b)
   check running code version vs on-disk version, (c) then check network.
   Inverting this order wastes time on the wrong layer.

2. An empty API response is not always a network timeout. A safety
   check that refuses to serve produces the same shape -- empty body,
   no error code -- as a dead endpoint. The differentiator is the
   serve's internal log, not the response itself.

3. After any `hermes update`, the serve must be restarted. The update
   process changes the on-disk code, but the running process keeps the
   old code in memory. This is not automatic (at least not for
   `suggi-vps-hermes`). The version-mismatch safety check will block
   affected endpoints until the restart happens.

### One Actionable Change

Add a preflight check that compares the serve's running code version
against the on-disk checkout. The check: read the serve startup line in
`agent.log` for the running commit hash, compare it against `git
rev-parse HEAD` in the hermes-agent directory. If they differ, flag
"SERVE STALE -- restart required" before any other diagnostic. This
catches the exact class of failure before the user sees symptoms, and
it costs one grep + one git call -- cheaper than a network
troubleshooting rabbit hole.

### Cross-links

- `reflections/2026-08-22_morpheus_desktop-app-state-has-three-tiers.md`
  -- the desktop app's local state tiers; this reflection adds a fourth
  diagnostic dimension (serve code version) to the existing three
- `reflections/2026-08-24_morpheus_limits-are-choices-in-disguise.md`
  -- limits as design choices; the serve's refusal-to-serve is another
  instance of a limit that looks like a bug but is a safety choice