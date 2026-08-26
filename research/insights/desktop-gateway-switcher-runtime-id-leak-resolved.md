---
name: desktop-gateway-switcher-runtime-id-leak-resolved
id: 20260826T125940Z
tier: insight
status: active
source:
  - 20260825T205034Z
  - 20260826T125940Z
author: Morpheus
tags: [hermes-desktop, multi-connection, session-routing, remote-gateway, connection-json, connections-json, per-profile-override, sidebar-switcher, bug, fleet, resolved]
links:
  - research/insights/desktop-gateway-switcher-runtime-id-leak.md
  - reflections/2026-08-20_link_local-aliases-outperform-multiconnection.md
  - reflections/2026-08-22_morpheus_desktop-app-state-has-three-tiers.md
  - research/insights/unified-serve-all-profiles.md
---

# The Desktop Gateway Switcher Runtime ID Leak Is Fixed -- PR #95080

## The Insight

The Hermes desktop app's registered-gateway sidebar switcher could
not safely mix local and remote profiles on one machine because it
leaked the previous connection's runtime session ID into the new
backend, producing a deterministic "session not found" on every
remote session resume. This bug (GitHub #93937, #93888) is now
fixed by PR #95080 (merged 2026-08-26, upstream d0351e32), which
consolidates seven contributor fixes into one atomic switch
lifecycle: gateway switches commit before the new source is
published, the registry primary's socket is reused for its own
(connectionId, profile) sessions, untagged remote rows resolve to
the active registry connection, stale stored-session-to-runtime
bindings are invalidated before a profile reopens, and explicit-
local source picks honor legacy per-profile remote overrides. The
fix is verified live on our fleet: both local Link and remote VPS
agents (morpheus, neo, runners) work simultaneously through the
desktop app sidebar with connection.json at mode=remote, profiles
empty. Zero session-not-found errors after the update.

The v1 connection.json layer and the v2 connections.json registry
remain two parallel routing systems, but the conflict zone at the
session-RPC boundary is now closed: the sidebar switcher uses the
same beforeConnectionSwitch() cleanup lifecycle as the Settings >
Gateway path, and freshDraftReady guards prevent old-session resume
from racing new-session creation. The fix markers in the dist code
are beforeConnectionSwitch (6 occurrences in index bundle) and
freshDraftReady (6 occurrences). The failure mode -- messages
reaching the VPS but responses not streaming back because the
WebSocket was bound to the wrong session ID -- is eliminated.

This is a resolved failure class: the bug was real, the fix is
merged and verified, and the fleet operates normally. The original
insight (desktop-gateway-switcher-runtime-id-leak, 20260825T205034Z)
documented the bug, four attempted fixes, and the correct fix path;
this insight supersedes it with the resolution record.

## Evidence

### 1. The fix: PR #95080

PR #95080 ("fix(desktop): gateway switches, primary reuse, and
session routing hold exact route identity") by teknium1 was opened
2026-08-25 and merged into main at commit 682a34a7. The PR summary
states: "Multi-gateway Desktop no longer leaks one gateway's runtime
identity into another: switches commit before the new source is
published, the registry primary's socket is reused for its own
(connectionId, profile) sessions instead of dialing a duplicate,
untagged remote rows resolve to the active registry connection
instead of the local dispatcher, and stale stored-session-to-runtime
bindings are invalidated before a profile reopens."

The PR consolidates salvaged work from seven contributors, each
addressing one facet of the route-identity failure class:

- #94145 (@Zeus-Deus) -- gateway-switch commit barrier: begin/end
  lifecycle, ownership guards, timeout cancellation. This is the
  core fix that makes selectConnection() use the same atomic
  transition as softSwitch().
- #94824 (@aryaxo) -- primary connectionId publication +
  requestGatewayForAgent primary-socket reuse. Prevents the
  duplicate-backend dial that lost session ownership.
- #93451 (@lukeroberts) -- untagged remote row fallback to the
  active registry connection. Remote sessions without an explicit
  connectionId now resolve to the active registry connection
  instead of the local dispatcher.
- #94927 (@Tomenatore) -- pre-open invalidation of stale
  stored-session-to-runtime bindings. Before a profile reopens,
  stale runtime IDs are invalidated so the resume path gets a
  fresh runtime ID from the correct backend.
- #94166 (@cmoiccool) -- explicit-local source picks honor legacy
  per-profile remote overrides. When the user explicitly selects
  the local source, per-profile remote overrides are still
  respected for profiles that should route remotely.
- #81165 (@echoes666) -- profile-switch dial failures surfaced.
  Errors that were previously silent are now visible to the user.
- #68632 (@bashrusakh) -- gateway-becomes-open resume guarded by
  freshDraftReady. Prevents old-session resume from racing /new
  when a profile gateway opens.

The PR explicitly lists: "Fixes #93937, #94709 (4001 session-not-
found shape), #94162, #68594; advances #90149/#88680."

### 2. Verification on our fleet (2026-08-26)

Both VPS and PC updated to upstream d0351e32 (local dcfdc8de).

Fix markers in PC dist code (release build):
- connections-BXEwB0hN.js: beforeConnectionSwitch (1x),
  freshDraftReady (1x)
- index-BSobfBgL.js: beforeConnectionSwitch (6x),
  freshDraftReady (6x)

These markers were ABSENT in the previous build (v0.20.5 upstream
5259f565 / 4032a15a). Their presence confirms the fix code is
compiled into the running app.

VPS serve health: {"ok":true,"version":"0.20.5","auth_required":
true} on 100.99.142.120:9119.

Session-not-found error timeline from VPS errors.log:
- 2026-08-25 22:44-22:45 CEST: 8 errors (session_id='1076289e') --
  these were during the per-profile override attempt, before revert
- 2026-08-26 13:09 CEST: 2 errors (session_id='c309ddf6') -- before
  the PC's last boot at 12:36 UTC (14:36 CEST)
- After 12:36 UTC boot: ZERO session-not-found errors

PC boot log (2026-08-26T12:36:51Z):
- Remote backend: "Connecting to remote Hermes backend at
  http://100.99.142.120:9119" -> "Remote Hermes backend is ready"
- Link backend: "Starting Hermes backend for profile 'link'" ->
  HERMES_BACKEND_READY port=54866
- Default backend: "Starting Hermes backend for profile 'default'"
  -> HERMES_BACKEND_READY port=54867
- sessions.changed events flowing normally

connection.json: mode=remote, profiles={} (the original/reverted
state). Both local and remote profiles work through the sidebar
without per-profile overrides.

User confirmed: "Link and you work again like before."

### 3. Prior fleet context

The original insight (20260825T205034Z) documented four attempted
fixes:
1. mode=local (broke VPS profiles)
2. mode=local + per-profile remote overrides (correct config but
   sidebar switcher bug blocked it -- messages reached VPS but
   responses did not stream back)
3. mode=remote + per-profile local for link (code does not support
   this direction -- profileRemoteOverride only checks
   modeIsRemoteLike)
4. Revert to mode=remote (working, Link via CLI)

Attempt 2 was the theoretically correct routing configuration. The
fix from PR #95080 makes attempt 2's configuration workable by
closing the runtime ID leak. However, with the current fleet setup
(mode=remote, VPS as global backend), per-profile overrides are not
needed: the app spawns local backends for link and default on boot,
and the sidebar switcher now properly transitions between local and
remote without leaking session IDs. The per-profile override
approach remains available as a future option if the fleet topology
changes (e.g., multiple remote backends on different machines).

Link's 2026-08-20 reflection (local-aliases-outperform-multiconnection)
documented the same architectural tension on v0.20.4: the v2
registry could see a gateway and list profiles, but activation was
unstable. That conclusion is now superseded for v0.20.5+ with the
fix: the sidebar switcher is the reliable path.

Morpheus's 2026-08-22 reflection (desktop-app-state-has-three-tiers)
documented the three-tier local state model. The v1/v2 conflict at
the session-RPC boundary (the fourth tier) is now closed by the fix.

### 4. Dashboard stale-code warning (side fix)

After the VPS update, the hermes-dashboard systemd service was
running stale code (6ce7ab8bfb) while the disk had the new code
(dcfdc8de). The dashboard refused model picker requests with:
"This dashboard is running code from 6ce7ab8bfb but the checkout
on disk is now dcfdc8deec." Fixed by restarting the service:
sudo systemctl restart hermes-dashboard. This is a standard
post-update step: the dashboard service does not auto-restart on
hermes update.

## Implications

1. **Fleet configuration is stable at mode=remote.** The current
   setup (connection.json mode=remote, profiles empty) works for
   both local and remote profiles. VPS agents route through the
   global remote backend; Link and default get local backends
   spawned on boot. The sidebar switcher properly transitions
   between them. No per-profile overrides are needed.

2. **The sidebar switcher is the reliable switch path.** The
   workaround ("use Settings > Gateway > Connection mode instead
   of the sidebar switcher") is no longer needed. The sidebar
   switcher now uses beforeConnectionSwitch() with the same
   atomic lifecycle as softSwitch(). Both paths are reliable.

3. **Per-profile overrides remain available but not required.**
   The per-profile override mechanism (mode=local +
   profiles[VPS]=remote) is now functional with the fix, but the
   current fleet topology does not need it. If the fleet adds a
   second remote backend on a different machine, per-profile
   overrides would be the correct configuration to route different
   VPS profiles to different backends.

4. **Post-update: restart the dashboard service.** After a hermes
   update on the VPS, restart hermes-dashboard to clear the
   stale-code warning: sudo systemctl restart hermes-dashboard.
   The serve (suggi-vps-hermes) auto-restarts via systemd; the
   dashboard does not.

5. **Link's state.db metadata remains correct.** The
   cwd/git_repo_root fields set on 2026-08-25
   (C:/AI Stuff/Hermes Agent/profiles/link/workspace-link) are
   still in place and help both CLI and desktop resume find the
   correct workspace.

6. **The v1/v2 dual-routing architecture persists but the
   conflict zone is closed.** Two parallel routing systems
   (connection.json and connections.json) remain, but the fix
   ensures they agree at the session-RPC boundary. The sidebar
   switcher consults v2 for the gateway list and v1 for session
   RPCs, but beforeConnectionSwitch() clears the old binding
   before the new source is published, so no runtime ID crosses
   the connection boundary.

7. **Post-update verification checklist for future updates.**
   After any future Hermes update on the PC, verify the fix is
   still present: grep the dist code for "beforeConnectionSwitch"
   and "freshDraftReady". If both markers are present, the fix is
   intact. If absent, the fix was refactored or removed -- test
   the sidebar switcher before relying on it. After any VPS
   update, restart hermes-dashboard to clear stale-code warnings.
   Check VPS errors.log for "session-scoped RPC rejected" entries
   after the first switching session -- zero errors means the fix
   is working.

8. **The updater window staying open is a separate known bug.**
   Issues #83674 and #90455 document that the Windows updater
   window does not close after the app relaunches because the
   gateway process inherits the updater's pipe handles, preventing
   EOF. This is unrelated to the session-routing fix and remains
   open. Workaround: manually close the updater window after the
   app has relaunched.

## Counter-evidence

This insight (the bug is fixed) would be invalidated if:

- A regression reintroduces the runtime ID leak in a future
  Hermes release. The fix depends on beforeConnectionSwitch()
  being called in selectConnection(); if a refactor removes or
  bypasses this call, the bug returns. Test: switch between local
  and remote gateways via the sidebar, resume a stored remote
  session, and check VPS errors.log for "session-scoped RPC
  rejected" entries. If present, the regression has landed.

- The fix is incomplete for our specific topology (local + remote
  on the same machine with mode=remote). The verification on
  2026-08-26 showed zero errors, but this was a single test
  session. A longer testing period or a different switching
  pattern (rapid switching, switching mid-turn, switching during
  tool execution) might reveal edge cases. Test: use the desktop
  app normally for a week, switching between Link and VPS agents
  multiple times per day, and check for any session-not-found
  errors in VPS errors.log.

- The fix works for mode=remote but not for per-profile overrides
  (mode=local + profiles[VPS]=remote). If a future fleet topology
  change requires per-profile overrides and they still produce
  the runtime ID leak, the fix is incomplete for that
  configuration. Test: set mode=local + profiles[VPS]=remote,
  restart, switch via sidebar, resume VPS sessions. If
  session-not-found errors appear, the per-profile override path
  was not fully fixed.

- The Hermes team removes beforeConnectionSwitch() or
  freshDraftReady() in a refactor, assuming they are no longer
  needed. Test: grep the dist code for these markers after each
  update; if absent, verify the replacement mechanism provides
  equivalent guarantees.

- The fix addresses the sidebar switcher path but a different UI
  path (e.g., profile rail, Bot Mode roster, drag-and-drop session
  transfer) has the same runtime ID leak. The PR covers the
  registered-gateway switcher and profile-rail fresh chats, but
  other activation surfaces may not have been hardened. Test: try
  every profile-switching UI path (sidebar, profile rail, Bot Mode)
  and check VPS errors.log for session-not-found errors from each.

- The fix works for session resume but not for in-flight tool
  execution. If a tool is running when the user switches gateways,
  the tool result might be routed to the wrong backend. The
  freshDraftReady guard prevents old-session resume from racing
  /new, but it may not cover mid-turn gateway switches. Test:
  start a long-running tool on a VPS profile, switch to local Link
  mid-execution, switch back, and check whether the tool result
  arrives correctly.

## Cross-Links

- `research/insights/desktop-gateway-switcher-runtime-id-leak.md`
  -- the original insight documenting the bug, four attempted
  fixes, and the correct fix path (superseded by this insight)
- `reflections/2026-08-20_link_local-aliases-outperform-multiconnection.md`
  -- Link's prior conclusion that local connector aliases outperform
  the v2 multi-connection registry on v0.20.4; superseded for
  v0.20.5+ with the fix
- `reflections/2026-08-22_morpheus_desktop-app-state-has-three-tiers.md`
  -- the three-tier local state model; this insight extends it with
  the resolved session-RPC routing conflict
- `research/insights/unified-serve-all-profiles.md` -- the VPS-side
  architecture (one serve, all profiles); the client-side routing
  now works correctly with this architecture
- GitHub: PR #95080 (consolidated fix, merged), #93937 (bug, fixed),
  #93888 (bug, fixed), #94145/#94824/#93451/#94927/#94166/#81165/
  #68632 (salvaged contributor fixes), #94724 (multi-gateway
  tracker)