---
name: desktop-gateway-switcher-runtime-id-leak
id: 20260825T205034Z
tier: insight
status: active
source:
  - 20260825T205034Z
author: Morpheus
tags: [hermes-desktop, multi-connection, session-routing, remote-gateway, connection-json, connections-json, per-profile-override, sidebar-switcher, bug, fleet]
links:
  - reflections/2026-08-20_link_local-aliases-outperform-multiconnection.md
  - reflections/2026-08-22_morpheus_desktop-app-state-has-three-tiers.md
  - research/insights/unified-serve-all-profiles.md
  - research/insights/workspace-search-system.md
---

# The Desktop Gateway Switcher Leaks Runtime Session IDs Across Connection Boundaries

## The Insight

The Hermes desktop app's registered-gateway sidebar switcher cannot
safely mix local and remote profiles on one machine because it leaks
the previous connection's runtime session ID into the new backend,
producing a deterministic "session not found" on every remote session
resume. The v1 connection.json layer and the v2 connections.json
registry are two parallel routing systems that conflict when both
are active: the v2 sidebar switcher dials the remote gateway for
session lists and chat, but the v1 layer's ensureBackend() resolves
session-scoped RPCs -- and the switcher does not clear the old
connection's runtime binding before activating the new gateway. The
correct fix (PR #93246) makes profile-rail clicks connection-aware so
a remote profile never routes through the local pool, but this fix is
not merged in v0.20.5. Until it lands, a fleet that mixes local
agents (Link on the PC) with remote agents (Morpheus, Neo, and
runners on the VPS) must keep connection.json at mode=remote and
accept that local profiles are reachable only through the CLI. The
per-profile override approach (mode=local + profiles[VPS]=remote)
is the theoretically correct routing configuration and the design
intent of the codebase, but the sidebar switcher bug makes it
unworkable in practice. This is a failure class in multi-connection
desktop routing, not a configuration error -- the routing backend
already supports per-profile overrides correctly, but the UI layer
that selects which backend to talk to does not clear its previous
selection before switching, so the session RPC arrives at the new
backend carrying the old backend's runtime identity.

The failure is also asymmetric in a way that makes it hard to
diagnose: messages sent from the desktop DO reach the VPS agent (the
REST submit path works), but the agent's response does not stream
back to the desktop because the WebSocket is bound to the wrong
session ID. The user sees their message disappear into a void with
no error, no loading indicator resolution, and no response. The
response only becomes visible after closing and reopening the
session, which forces a fresh resume from the stored ID. This
silent-failure mode is particularly dangerous because it mimics a
network problem or a frozen agent rather than revealing the routing
identity mismatch that is the actual cause.

## Evidence

### 1. The two routing layers and how they interact

The Hermes desktop app (v0.20.5, upstream 4032a15a) has two
independent connection-routing systems that partially overlap:

**v1 -- connection.json (legacy routing).** A single JSON file in
the app's user-data directory (%APPDATA%\Hermes\connection.json on
Windows). Contains a global `mode` field ("local" or "remote"), a
`remote` block (url, authMode), and a `profiles` map for per-profile
overrides. The Electron main process reads this file via
readDesktopConnectionConfig() on every ensureBackend() call. The
function resolveRemoteBackend(profile) checks, in order:
(1) profileRemoteOverride -- profiles[name] with mode=remote/cloud
and a URL; (2) env override (HERMES_DESKTOP_REMOTE_URL); (3) global
mode=ssh; (4) global mode=remote (uses config.remote.url); (5)
mode=local returns null (local spawn). The function
resolveProfileBackendRoute(profile, opts) then decides the backend
route: if profile==primary, use the primary backend; if
profileRemoteOverride exists, use a pool backend on that remote;
if globalRemoteActive, use the primary with ?profile= scoping; if
primaryRemoteActive and ownEntry, use a pool backend; otherwise
local pool spawn.

**v2 -- connections.json (multi-connection registry).** A registry
of named gateway connections (local, remote, SSH, cloud). The
sidebar gateway selector switches between these. Each
(connection, profile) pair gets its own backend and WebSocket.
The docs say: "Switch gateways from the Sessions sidebar. Profiles,
chats, messaging, and cron stay scoped to that gateway; the
app-managed window backend is still chosen by the connection-mode
controls above." This means the sidebar switch changes which
sessions you SEE, but the actual session RPC routing still flows
through ensureBackend() which reads connection.json.

### 2. The bug: sidebar switcher leaks runtime session IDs

GitHub issue #93937 (open, 2026-08-24) documents the exact failure.
The sidebar switcher (connection-switcher.tsx) calls
selectConnection(connectionId) which performs:
  ensureGatewayAgent(connectionId, targetProfile)
  -> wipeSessionListsForGatewaySwitch()
  -> requestFreshSession()

It does NOT call beforeConnectionSwitch() and does NOT wrap the
transition in $gatewaySwitching the way the Settings path does. The
Settings > Gateway > Connection mode path uses softSwitch() which
performs the full lifecycle:
  $gatewaySwitching = true
  -> beforeConnectionSwitch()
  -> wipeSessionListsForGatewaySwitch()
  -> close old primary/secondary sockets
  -> connect the selected backend
  -> reload profile/config/session state
  -> $gatewaySwitching = false

Without this cleanup, the route/session resume effect sees the new
active gateway while the renderer still holds the old gateway's
runtime session ID. The new backend correctly rejects the stale ID
with: "session-scoped RPC rejected: session_id='...' not in memory
(detached/reaped runtime; client should resume the stored session)".

GitHub issue #93888 (open, 2026-08-24) confirms the same bug from a
different reporter: "Desktop sends a local runtime ID to a Remote
Gateway and cannot restore stored sessions." The reporter notes the
durable sessions still exist in the remote state.db -- this is not
data loss, it is a routing identity failure. The workaround from
both issues: configure the gateway via Settings > Gateway >
Connection mode (which writes connection.json and uses softSwitch),
not via the sidebar switcher (which writes only connections.json).

### 3. Our four attempted fixes and their outcomes

**Attempt 1: mode=local (flip the global seesaw).** Changed
connection.json from mode=remote to mode=local. Result: Link's
local sessions became visible and resumable, but ALL VPS profiles
(morpheus, neo, investment-runner, library-runner, research-runner)
broke because ensureBackend() for those profiles found no
per-profile override and fell to local pool spawn, which failed
with "Profile no longer exists" (those profiles do not exist on the
PC). The VPS serve logs showed no WebSocket activity from the PC
at all. This proved mode is a global seesaw: local helps Link, remote
helps VPS, and there is no middle ground without per-profile
overrides.

**Attempt 2: mode=local + per-profile remote overrides.** Added
profiles.morpheus, profiles.neo, profiles.investment-runner,
profiles.library-runner, profiles.research-runner each with
{mode: "remote", url: "http://100.99.142.120:9119", authMode:
"oauth"}. The routing code (profileRemoteOverride ->
resolveProfileBackendRoute case 2 -> spawnPoolBackend ->
resolveRemoteBackend) should route VPS profiles to the VPS and
leave default+link local. Result: the VPS serve received WebSocket
connections and OAuth tickets were minted every 30 seconds,
proving the transport layer worked. But every session-scoped RPC
was rejected with the stale runtime ID error. The sidebar switcher
bug (#93937) prevented proper session binding -- the app sent
local runtime IDs to the VPS backend, which rejected them. The
config was correct; the app's switching code was broken.

**Attempt 3: mode=remote + per-profile local override for link.**
Investigated adding profiles.link with mode=local while keeping
mode=remote globally. But profileRemoteOverride() only checks
modeIsRemoteLike(entry.mode) -- "local" is not remote-like, so it
returns null. Then resolveProfileBackendRoute hits case 3
(globalRemoteActive) and routes link to the VPS with
?profile=link, which does not exist on the VPS. There is NO
mechanism for a per-profile LOCAL override when the global mode is
remote. The code does not support this direction.

**Attempt 4: revert to mode=remote (original state).** Reverted
connection.json to the original mode=remote with empty profiles.
All VPS profiles work again via the sidebar. Link is not accessible
through the desktop app but remains usable via CLI
(hermes -p link chat --continue). Link's state.db sessions retain
the corrected cwd/git_repo_root metadata from attempt 1, which
helps CLI resume find the correct workspace.

### 4. The correct fix and when to apply it

PR #93246 (open, not merged) proposes the proper fix: make the
profile rail connection-aware. selectProfileRoute(route) in
store/profile.ts routes clicks through ensureGatewayAgent
(connectionId, profile) instead of the legacy selectProfile(name)
which has no connectionId. A profile belonging to a registered
remote source is never resolved through the local profile pool.
PR #92864 (open, not merged) adds UI to configure per-profile
remote overrides from the profile rail (right-click -> "Connect
to a remote host..."), eliminating the need to hand-edit
connection.json. Issue #90223 (open) is the feature request that
established the design intent: per-profile backend routing belongs
on the profile rail, not the machine-level Gateways settings page.

When these PRs merge, the correct configuration for our fleet will
be: connection.json mode=local + per-profile remote overrides for
all VPS profiles (morpheus, neo, investment-runner, library-runner,
research-runner). Default and link stay local. The sidebar switcher
will properly clean up runtime bindings because
selectProfileRoute carries the connectionId, preventing the local
pool from being consulted for remote profiles.

To verify the fix has landed: grep the dist code for
"selectProfileRoute" -- if present, the fix is in. Also check if
issue #93937 is closed. If fixed, set connection.json mode=local +
profiles[VPS]=remote, restart the app, test sidebar switch from
"This device" to "suggi-vps-hermes", and verify that VPS sessions
resume without "session not found".

### 5. Evidence from prior fleet work

Link's 2026-08-20 reflection (local-aliases-outperform-multiconnection)
documented the same architectural tension on v0.20.4: the v2 registry
could see a gateway and list profiles, but activation was unstable.
Link concluded that local connector aliases with per-profile
connection.json entries were more reliable than the v2 multi-connection
registry. That conclusion holds for v0.20.5: the v2 registry's sidebar
switcher is still the broken path.

Morpheus's 2026-08-22 reflection (desktop-app-state-has-three-tiers)
documented the three-tier local state model: connections.json (v2
registry), connection.json (v1 routing), and renderer localStorage.
Both real bugs were in tiers 2 and 3, not in the backend. This insight
extends that model: the v1 and v2 layers conflict at the session-rpc
routing boundary, not just at the profile-list or connection-display
level.

The unified-serve-all-profiles insight (2026-08-22) established that
one VPS serve backs every profile. The desktop app's per-profile
override mechanism is the intended client-side complement to that
architecture: each VPS profile gets a per-profile entry pointing at
the unified serve. The routing backend (profileRemoteOverride,
resolveProfileBackendRoute) already supports this. Only the sidebar
switcher UI bug prevents it from working end to end.

## Implications

1. **Fleet configuration stays at mode=remote until the fix lands.**
   Any fleet mixing local and remote profiles on one desktop client
   must keep connection.json at mode=remote. Local profiles (Link
   on the PC, Linkie on the laptop) are accessible via CLI only:
   `hermes -p <name> chat --continue`. This is a known limitation,
   not a configuration error -- do not attempt to "fix" it by
   changing connection.json until the sidebar switcher bug is
   resolved upstream.

2. **Do not use per-profile overrides with the sidebar switcher.**
   The per-profile override approach (mode=local +
   profiles[VPS]=remote) is the correct routing configuration and
   the design intent of the codebase, but applying it with the
   current sidebar switcher produces a worse failure mode than
   mode=remote: VPS sessions appear in the list but every resume
   fails with "session not found" because of the runtime ID leak.
   The configuration is right; the app is wrong. Wait for the fix.

3. **The Settings > Gateway path is the reliable switch path.**
   Until the sidebar switcher is fixed, the only reliable way to
   switch between local and remote backends is Settings > Gateway >
   Connection mode, which uses softSwitch() with proper cleanup.
   However, this path changes the global mode, which means you
   cannot mix local and remote simultaneously -- it is a full
   cutover, not a side-by-side arrangement. For fleets that need
   both simultaneously, CLI is the fallback for local profiles.

4. **When the fix lands, apply the per-profile override
   configuration.** The correct setup will be: connection.json
   mode=local, profiles.morpheus/neo/investment-runner/library-runner/
   research-runner each with {mode: "remote", url: VPS, authMode:
   "oauth"}. Default and link stay local (no profiles entry). This
   gives the desktop app simultaneous access to local Link and
   remote VPS agents. Verify by: grepping dist for
   "selectProfileRoute", checking if #93937 is closed, setting
   the config, restarting, and testing the sidebar switch.

5. **Link's state.db metadata is already corrected.** The
   cwd/git_repo_root fields were set to
   C:/AI Stuff/Hermes Agent/profiles/link/workspace-link on
   2026-08-25. This helps CLI resume find the correct workspace
   and will help the desktop app once the fix lands. No further
   metadata changes are needed.

6. **The v1/v2 dual-routing architecture is the root cause.** Two
   parallel routing systems (connection.json and connections.json)
   that partially overlap is a structural design choice that
   creates conflict zones at every boundary where both are
   consulted. The sidebar switcher consults v2 for the gateway list
   but v1 for session RPCs; the Settings page writes v1 directly.
   The fix (PR #93246) unifies these by making the profile rail
   connection-aware, so v2 becomes the single source of truth for
   routing, not just for display.

## Counter-evidence

This insight would be invalidated if:

- A future Hermes release fixes the sidebar switcher to use
  softSwitch() or an equivalent atomic transition, clearing runtime
  bindings before activating the new gateway. This would make the
  per-profile override approach work with the sidebar switcher,
  and the insight's "do not use per-profile overrides" implication
  would no longer apply. Test: set mode=local +
  profiles[VPS]=remote, restart, switch via sidebar, resume a VPS
  session. If it works, the fix has landed.

- The bug is actually in the VPS serve's session management, not
  the desktop app's routing. If the serve incorrectly reaps
  sessions that should be retained, the fix would be server-side.
  However, the VPS logs show the serve correctly rejects runtime
  IDs that were never registered on that backend -- the IDs belong
  to the PC's local runtime. The serve is behaving correctly;
  the desktop app is sending the wrong identity.

- The Hermes team removes the v1 connection.json layer entirely,
  making connections.json (v2) the sole routing mechanism. In that
  case the per-profile override approach would be replaced by v2
  connection-scoped routing, and this insight's v1-specific
  analysis would be historical only. Test: check if
  readDesktopConnectionConfig() still exists in the codebase.

- A user reports that mode=remote + profiles[link]={mode:local}
  works in a newer version, meaning a per-profile LOCAL override
  mechanism was added. This would allow the opposite direction
  (global remote + local exception for link) and would be a
  simpler configuration than mode=local + per-profile remote for
  every VPS profile. Test: add profiles.link with mode=local to
  connection.json with mode=remote, restart, switch to link in
  the sidebar. If link sessions resume locally while VPS profiles
  still work via the global remote, the feature was added.

- The bug is actually in the VPS serve's session management, not
  the desktop app's routing. If the serve incorrectly reaps
  sessions that should be retained, the fix would be server-side.
  However, the VPS logs show the serve correctly rejects runtime
  IDs that were never registered on that backend -- the IDs belong
  to the PC's local runtime. The serve is behaving correctly;
  the desktop app is sending the wrong identity.

## Cross-Links

- `reflections/2026-08-20_link_local-aliases-outperform-multiconnection.md`
  -- Link's prior conclusion that local connector aliases outperform
  the v2 multi-connection registry on v0.20.4; still holds on v0.20.5
- `reflections/2026-08-22_morpheus_desktop-app-state-has-three-tiers.md`
  -- the three-tier local state model (connections.json,
  connection.json, localStorage); this insight extends it to the
  session-RPC routing conflict
- `research/insights/unified-serve-all-profiles.md` -- the VPS-side
  architecture (one serve, all profiles); the per-profile override
  is the client-side complement
- `research/insights/workspace-search-system.md` -- per-agent
  workspace search architecture (unrelated to routing but shares
  the per-agent isolation principle)
- GitHub issues: #93937 (sidebar switcher leaks runtime ID),
  #93888 (desktop sends local runtime ID to remote gateway),
  #93246 (proposed fix: connection-aware profile rail),
  #92864 (per-profile override UI on profile rail),
  #90223 (feature request: restore per-profile override UI)