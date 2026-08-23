---
name: unified-serve-all-profiles
id: 20260821T171622Z
tier: insight
source:
  - 20260821T074320Z
  - 20260820T224313Z
author: Morpheus
tags: [hermes, serve, profiles, desktop-app, gateway, vps, multi-agent, architecture, systemd, skins]
links:
  - reflections/2026-08-21_link_hermes-desktop-leveldb-collateral-damage.md
  - reflections/2026-08-20_link_local-aliases-outperform-multiconnection.md
  - research/insights/workspace-search-system.md
  - research/insights/vps-brainclone-plus-index.md
---

# One Hermes Serve Can Back Every Profile on the VPS

## Version History

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-08-21 | Morpheus | Initial insight: unified serving is the platform default; the two isolated serves are the explicit opt-out. |
| 2 | 2026-08-22 | Morpheus | Cutover complete and verified: single suggi-vps-hermes unit live; attach-target question answered; skins lesson added. |

## The Insight

One machine-level `hermes serve` backs every profile on the box --
unified serving is the platform default and per-profile `--isolated`
units are the explicit opt-out -- and the fleet cut over to a single
`suggi-vps-hermes` unit on 2026-08-22, retiring two per-profile
servers at the cost of process-level isolation.

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

### 2. The cutover (verified 2026-08-22)

- systemd `suggi-vps-hermes.service` runs the unified serve:
  `hermes serve --host 100.99.142.120 --port 9119` with no `-p` and
  no `--isolated` -- a machine-level process on the default home,
  basic-auth gated, with OAuth single-use tickets for the chat
  socket. Verified: listener `100.99.142.120:9119` owned by pid
  179237 (user hermes), unit active since 2026-08-22 10:03:56 CEST.
- One backend answers for all profiles: default, investment-runner,
  library-runner, morpheus, neo (verified via profile-scoped
  session.list right after cutover).
- The old per-profile units `hermes-morpheus` and `hermes-neo` are
  stopped; unit files retained for rollback.
- Unaffected and still active: `hermes-gateway-morpheus` and
  `hermes-gateway-neo` (messaging tickers), `hermes-dashboard` on
  8642 (separate machine-level admin surface).
- Suggi's desktop apps on the PC and the laptop both connect through
  the ONE gateway, registered in-app as `suggi-vps-hermes`.

### 3. The discovery: per-profile serving is the opt-out

`hermes serve --help` states the default explicitly:

> `--isolated`: When launched from a named profile, run a dedicated
> server scoped to that profile instead of routing to the
> machine-level server. **Default behavior is unified: profile
> launches attach to (or start) ONE machine-level server and
> preselect the profile.**

So the fleet's two servers existed because the units forced
`--isolated`. Without it, profiles attach to one machine-level
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
  connector architecture implemented before the cutover, pointed at
  `9119`/`9120`. A unified serve shrinks this registry to one entry.

### 5. History: why two serves existed

The two-unit setup was a deliberate rollback, not an accident.
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

- The **systemd unit name** (arbitrary, lowercase-hyphen): the
  unified unit is `suggi-vps-hermes.service`, replacing
  `hermes-morpheus.service` + `hermes-neo.service`.
- The **desktop app's device name** in the Connections registry:
  "Every connection needs a unique device name... The name shows up
  everywhere the instance appears -- roster badges, handles." The app
  shows one connection named `suggi-vps-hermes` (exactly the
  semantics requested), with Morpheus and Neo as profiles on it.

The name describes the box's Hermes backend, which is correct for a
unified serve: per-profile names (morpheus, neo) only make sense
while the serve IS per-profile.

### 7. The open question, answered

Version 1 asked whether the unified serve attaches to the EXISTING
machine-level server (the dashboard process on `8642`) or starts its
own machine-level listener. Answer: **its own listener.**
`suggi-vps-hermes` and `hermes-dashboard` run as two distinct
processes with two distinct listeners on `100.99.142.120` (9119 vs
8642); no attach-to-existing behavior observed. One machine-level
process family, not one process.

### 8. Skins on a unified serve

- The serve pushes ONE skin, machine-wide: the active `display.skin`
  of the serve's home. `config.get skin` ignores profile scope, and
  per-profile looks are a CLIENT-side feature -- the app assigns
  skins per profile in its own storage
  (`hermes-desktop-profile-themes-v1`), independent of the serve.
- The app registers a custom skin only when it receives it over the
  wire: `gateway.ready` seeds the active skin at connect, and
  `skin.changed` registers the new active skin but is gated on the
  active connection+profile scope. A skin flip while the app is
  closed (or an app restart mid-sequence) never reaches the app --
  2026-08-22's miss: the flip ran at 10:36, the app restarted at
  10:38, and only `default` was seeded.
- Durable local skins are a device-side concern: a desktop plugin in
  `<local-hermes-home>/desktop-plugins/` contributing `THEMES_AREA`
  themes lands skins in the app's picker without touching the serve
  (deployed on the PC 2026-08-22). Docs: Desktop Plugin SDK.

## Implications

1. **One serve replaces two -- done (2026-08-22).** One systemd
   unit, one port, one backend URL for the desktop app. The cost is
   accepted: one crash domain; restarting the unit drops desktop
   access for every profile. Rollback path: start the two retained
   per-profile units.
2. **Desktop reconfiguration was surgical.** The app-side switch was
   gateway registry edits only -- no LevelDB wipe, the ENT-068 trap
   explicitly avoided.
3. **Fleet convention for new agents.** New VPS agents should NOT
   get their own serve unit by default. Birth into the unified serve
   (one unit, named after the box) unless hard process isolation is
   explicitly required. This changes the fleet-agent-birth playbook's
   default.
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
6. **Per-agent looks are a client-side assignment over a REGISTERED
   skin.** Skins the fleet wants pickable on every device ship as a
   local desktop-plugin theme contribution (per device), or are
   pushed once as the active skin per connect -- the serve itself
   cannot hand out per-profile skins.

## Counter-evidence

This insight would be invalidated if:

- Cross-profile state bleed appears under sustained multi-profile use
  (one profile's config, keys, or sessions leaking into another's
  turn). Not observed in the first day of cutover use; a longer soak
  is the real test.
- Process-level isolation proves operationally mandatory here: e.g.
  profile restarts or crashes routinely requiring independent serve
  lifecycles, which one shared process cannot give.
- The unified serve's own-listener design proves unworkable in
  practice (it has not: the 9119 and 8642 listeners coexist
  stably, and the attach-target question from version 1 is settled).

## Legacy units (archived 2026-08-23)

The pre-cutover isolated-serve units were removed from
`/etc/systemd/system/` on 2026-08-23 (Suggi-approved). They were
still ENABLED until then -- a reboot would have raced them against
this serve on port 9119 -- and `hermes-morpheus.service` hardcoded
the obsolete embedding model (`nomic-ai/nomic-embed-text-v1.5`,
768-dim), making any "rollback" a mixed-model corruption event.
Archived verbatim here as the rollback reference:

`hermes-morpheus.service`:

```ini
[Unit]
Description=Hermes Agent - Morpheus profile (serve backend)
After=network-online.target tailscaled.service
Wants=network-online.target

[Service]
Type=simple
User=hermes
Group=hermes
Environment=HERMES_HOME=/home/hermes/.hermes/profiles/morpheus
Environment=MNEMOSYNE_EMBEDDING_MODEL=nomic-ai/nomic-embed-text-v1.5
Environment=MNEMOSYNE_EMBEDDING_DIM=768
EnvironmentFile=/home/hermes/.hermes/profiles/morpheus/.env
ExecStart=/home/hermes/.hermes/hermes-agent/venv/bin/python /home/hermes/.hermes/hermes-agent/hermes -p morpheus serve --isolated --host 100.99.142.120 --port 9119
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

`hermes-neo.service`:

```ini
[Unit]
Description=Hermes Agent - Neo profile (serve backend)
After=network-online.target tailscaled.service
Wants=network-online.target

[Service]
Type=simple
User=hermes
Group=hermes
Environment=HERMES_HOME=/home/hermes/.hermes/profiles/neo
Environment=MNEMOSYNE_EMBEDDING_MODEL=BAAI/bge-large-en-v1.5
Environment=MNEMOSYNE_EMBEDDING_DIM=1024
EnvironmentFile=/home/hermes/.hermes/profiles/neo/.env
ExecStart=/home/hermes/.hermes/hermes-agent/venv/bin/python /home/hermes/.hermes/hermes-agent/hermes -p neo serve --isolated --host 100.99.142.120 --port 9120
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

## Cross-Links

- `reflections/2026-08-21_link_hermes-desktop-leveldb-collateral-damage.md` -- desktop-side repair history (source, implication 2)
- `reflections/2026-08-20_link_local-aliases-outperform-multiconnection.md` -- why the previous two-connection setup existed (source)
- `research/insights/workspace-search-system.md` -- sibling insight on per-agent infrastructure built on this VPS
- `research/insights/vps-brainclone-plus-index.md` -- the VPS-native architecture pattern this serve consolidation follows
