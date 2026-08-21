---
name: unified-serve-all-profiles
id: 20260821T171622Z
tier: insight
source:
  - 20260821T074320Z
  - 20260820T224313Z
author: Morpheus
tags: [hermes, serve, profiles, desktop-app, gateway, vps, multi-agent, architecture, systemd]
links:
  - reflections/2026-08-21_link_hermes-desktop-leveldb-collateral-damage.md
  - reflections/2026-08-20_link_local-aliases-outperform-multiconnection.md
  - research/insights/workspace-search-system.md
  - research/insights/vps-brainclone-plus-index.md
---

# One Hermes Serve Can Back Every Profile on the VPS

## The Insight

Hermes's default serve mode is a single machine-level server that
hosts every profile on the box; the fleet's two isolated per-profile
serves on ports `9119` and `9120` are an explicit `--isolated`
opt-out, and one unified serve can replace both, at the cost of
process-level isolation.

## Evidence

### 1. What a Hermes "serve" is

`hermes serve` runs the backend server the desktop app connects to:
"the JSON-RPC/WebSocket gateway the desktop app and remote clients
connect to." It is the chat/session backend, distinct from two other
components people confuse with it:

- The **messaging gateway** (`hermes gateway`, systemd
  `hermes-gateway-<name>`) -- inbound platforms (Telegram, Discord,
  webhooks) and the cron ticker. One per profile, separate process.
- The **web dashboard** (`hermes dashboard`) -- a browser admin
  panel; machine-level, with a profile switcher.

A **profile** is a separate Hermes home directory
(`/home/hermes/.hermes/profiles/<name>/`) with its own `config.yaml`,
`.env`, `SOUL.md`, skills, memory, cron, and `state.db` (the SQLite
session store). Sessions live per-profile in that `state.db`, no
matter which surface created them (CLI, TUI, desktop, or bot chat),
which is why a CLI session is visible in the desktop app the moment
the app is connected to the same backend.

### 2. Current fleet setup (verified 2026-08-21)

Two dedicated systemd units, both binding the Tailscale IP
`100.99.142.120`:

```
hermes-morpheus.service:
  ExecStart=... hermes -p morpheus serve --isolated --host 100.99.142.120 --port 9119
hermes-neo.service:
  ExecStart=... hermes -p neo serve --isolated --host 100.99.142.120 --port 9120
```

Both run as user `hermes`, both have an `auth.json` (OAuth) in their
profile home, and both backends accept the same credentials (Link's
ENT-068 note). Non-loopback binds require authentication -- the old
`--insecure` flag is a documented no-op since the June 2026
hardening. Suggi's desktop app on the PC/laptop reaches these ports
over Tailscale through connector profiles Link rebuilt on
2026-08-20/21. Additionally: `hermes-gateway-morpheus` and
`hermes-gateway-neo` (messaging gateways, active), and
`hermes-dashboard` on `suggi-vps.tail40302e.ts.net:8642` (the
machine-level admin surface).

### 3. The discovery: per-profile serving is the opt-out

`hermes serve --help` states the default explicitly:

> `--isolated`: When launched from a named profile, run a dedicated
> server scoped to that profile instead of routing to the
> machine-level server. **Default behavior is unified: profile
> launches attach to (or start) ONE machine-level server and
> preselect the profile.**

So the fleet's two servers exist because the units force
`--isolated`. Without it, both profiles attach to one machine-level
server; each incoming session just preselects its profile. The
official docs describe this as the standard "gateway -> profile ->
sessions" model: the desktop app shows a profile selector, and a
backend with many profiles condenses its avatar strip into a named
selector. The docs' multi-gateway guide says a one-process-per-profile
split is right "when you want hard process-level isolation", and the
unified route is for hosts "where N supervisor units, N ports, and N
PID files are a burden" -- the fleet VPS is that host, verbatim.

The same isolated/unified pattern exists for the dashboard subcommand
(verified in `hermes_cli/subcommands/dashboard.py`), so the
machine-level concept is a platform-wide design, not a serve quirk.

### 4. Three mechanisms that sound alike but are different

- **Unified serve** (this insight's subject): one machine-level
  backend for the desktop app; profile preselected per session.
  Default behavior; `--isolated` opts out.
- **`gateway.multiplex_profiles`** (messaging only): set
  `gateway.multiplex_profiles: true` on the default profile and ONE
  gateway process serves inbound messaging for every profile (per
  token, or per URL prefix `/p/<profile>/` for HTTP platforms). It
  does NOT serve the desktop chat backend. Relevant only if we also
  want to collapse the two messaging gateway units into one process.
- **Multi-connection desktop** (client side): the PC/laptop app can
  register several backends in Settings -> Gateways (remote gateway,
  SSH, Cloud) and show every agent side by side. This is what Link's
  connector architecture implements today, pointed at `9119`/`9120`.
  A unified serve makes this registry shrink to one entry.

### 5. History: why two serves exist today

The two-unit setup is a deliberate rollback, not an accident.
Logbook ENT-067 (2026-08-20, Link): after a failed multiconnector
experiment on the desktop side, Link "restored the old Hermes
Desktop connector architecture", "removed the machine-level remote
registry entry", and "restored isolated VPS serve units for Morpheus
and Neo." ENT-068 (2026-08-21, Link): the experiment's fallout
included a LevelDB wipe on the PC app that destroyed unrelated UI
state (workspace pane, theme, layout), a shared-auth token gap, and
several repair cycles. Key distinction: that failure was in the
DESKTOP app's multi-connection routing and its cache handling -- not
in server-side unified serving, which was never the broken part. A
unified serve moves in the opposite direction: fewer connections,
fewer routing layers, one backend URL.

### 6. The name: where "suggi-vps-hermes" lives

Hermes has no separate "serve name" config -- a serve's name is
expressed in two controllable places, and both fit the requested
name:

- The **systemd unit name** (arbitrary, lowercase-hyphen): a unified
  unit would be e.g. `suggi-vps-hermes.service` instead of
  `hermes-morpheus.service` + `hermes-neo.service`.
- The **desktop app's device name** in the Connections registry:
  "Every connection needs a unique device name... The name shows up
  everywhere the instance appears -- roster badges, handles." So the
  app would show one connection named `suggi-vps-hermes` (exactly the
  semantics requested), with Morpheus and Neo as profiles/bots on it.

The name describes the box's Hermes backend, which is correct for a
unified serve: per-profile names (morpheus, neo) only make sense
while the serve IS per-profile.

### 7. The one open question

Unverified: with `--isolated` dropped, whether the unified serve
attaches to the EXISTING machine-level server (the dashboard process
on `8642`) or starts its own machine-level listener (e.g. on
`9119`). The help text says "attach to (or start)", so both are
plausible. A controlled test on the VPS settles it; this insight
does not guess.

## Implications

1. **One serve replaces two.** One systemd unit, one port, one
   backend URL for the desktop app, one crash domain instead of two.
   The docs name our exact situation (N units, N ports, N PID files
   on a VPS) as the reason to unify. Decision this informs: whether
   to consolidate Morpheus + Neo serving into a single
   `suggi-vps-hermes` serve -- the cost being that restarting or
   losing that one process takes down desktop access for BOTH
   agents, which the current split cannot do.
2. **Desktop reconfiguration must be surgical.** Link's LevelDB scar
   (2026-08-21) is the direct precedent: when Suggi's app switches
   from two connections to one, the PC-side change must be targeted
   (remove stale connection entries, back up LevelDB first, restore
   non-routing keys), never a database wipe. The server-side change
   is trivial compared to the client-side one.
3. **Fleet convention for new agents.** New VPS agents should NOT
   get their own serve unit by default. Birth into the unified serve
   (one unit, name it after the box) unless hard process isolation
   is explicitly required. This changes the fleet-agent-birth
   playbook's default.
4. **Naming convention.** Fleet machine-level Hermes backends get
   box-scoped names (`suggi-vps-hermes`), not profile-scoped ones;
   profile-scoped names stay valid only for `--isolated` serves.
5. **Messaging consolidation is a separate, independent option.**
   `gateway.multiplex_profiles` would collapse the two
   `hermes-gateway-*` units the same way, but it is opt-in, off by
   default, and has its own contract (port-binding platforms only on
   the default profile, `/p/<profile>/` URL prefixes, per-profile
   bot tokens). It can be adopted later or never, without blocking
   the serve consolidation.

## Counter-evidence

This insight would be invalidated if:

- A unified-serve test shows cross-profile state bleed (one
  profile's config, keys, or sessions leaking into another's turn).
  The docs claim per-profile isolation is preserved in multiplexed
  operation; if the unified serve violates it, keep `--isolated`.
- Process-level isolation turns out to be operationally mandatory
  here: e.g. profile restarts or crashes routinely requiring
  independent serve lifecycles, which one shared process cannot give.
- The desktop app cannot practically run both bots off one backend
  (a client-side failure distinct from the multiconnector failure --
  that one was routing between connections, not using a single
  multi-profile connection).
- The unified serve's attach target (dashboard process vs new
  listener) makes the one-port story unworkable in practice (e.g.
  port conflicts with `hermes-dashboard` on `8642`).

## Cross-Links

- `reflections/2026-08-21_link_hermes-desktop-leveldb-collateral-damage.md` -- desktop-side repair history (source, implication 2)
- `reflections/2026-08-20_link_local-aliases-outperform-multiconnection.md` -- why the current two-connection setup exists (source)
- `research/insights/workspace-search-system.md` -- sibling insight on per-agent infrastructure built on this VPS
- `research/insights/vps-brainclone-plus-index.md` -- the VPS-native architecture pattern this serve consolidation follows
