---
name: unified-serve-all-profiles
id: 20260821T171622Z
tier: insight
status: active
source: []
author: Morpheus
tags: [hermes, serve, dashboard, profiles, desktop-app, gateway, vps, architecture, systemd]
links:
  - research/insights/desktop-gateway-switcher-runtime-id-leak-resolved.md
  - reflections/2026-08-22_morpheus_desktop-app-state-has-three-tiers.md
---

# One Hermes Backend Serves Every Profile on the VPS

The fleet VPS (`suggi-vps`) runs exactly one Hermes backend: the systemd
system service `suggi-vps-hermes`, a `hermes dashboard` process listening
on the tailnet address `100.99.142.120:9119`. It serves every Hermes
profile on the box to the Desktop apps on Suggi's PC and laptop, and it
serves the web dashboard to a browser. A separate service, the gateway,
runs crons, messaging and terminal chats. This page describes the parts,
how they work, the rules that keep them running, and their limits.

## Parts

| Part | What it is | Where it lives |
|:--|:--|:--|
| Backend | `hermes dashboard --host 100.99.142.120 --port 9119 --skip-build --no-open`, run as user `hermes` on the default home (`HERMES_HOME=/home/hermes/.hermes`) | `/etc/systemd/system/suggi-vps-hermes.service`: `Restart=always`, `RestartSec=5`, `RestartPreventExitStatus=78`, `EnvironmentFile=/home/hermes/.hermes/.env` (login credentials) |
| Web dashboard | The browser UI of the backend; sign in with username and password | `http://suggi-vps.tail40302e.ts.net:9119/` |
| Desktop apps | Remote clients; one registered connection named `suggi-vps-hermes`, a profile chosen per chat | Each Desktop app's connection registry; URL `http://100.99.142.120:9119` |
| Gateway | `hermes gateway run` with `gateway.multiplex_profiles: true`: ticks every profile's crons, runs messaging and `hermes chat -q` turns | systemd user unit `hermes-gateway` |
| Profiles | One Hermes home per agent with its own `config.yaml`, `.env`, skills, memory and `state.db` session store | `/home/hermes/.hermes/profiles/<name>/` |

## How It Works

1. **One machine-level backend.** The backend runs on the default home
   and hosts every profile. A Desktop chat names its profile; the session
   is stored in that profile's `state.db`, so a profile's terminal and
   Desktop sessions appear in the same history.
2. **Access checks.** The backend binds to the tailnet address only, so
   it is unreachable from the public internet. Every client signs in
   through the basic username/password provider (the Desktop app signs in
   once and reuses the session). A host-header guard then admits only
   requests addressed to the bound IP or to the hostname in
   `dashboard.public_url`, set in `/home/hermes/.hermes/config.yaml` to
   `http://suggi-vps.tail40302e.ts.net:9119`. Any other host name gets
   HTTP 400 "Invalid Host header". The setting is read at startup.
3. **One backend per host.** When a backend starts, it looks for the
   host's existing backend. If that one looks orphaned -- parent is init,
   no recorded spawner, no Desktop SSH lock, older than 180 seconds -- the
   new one terminates it (`hermes_cli/process_identity.py`, log line
   "reaped orphaned ... backend owner"). Every systemd system service fits
   that test, so two backend units on this box kill each other.

## Rules

- **Exactly one backend.** Never start a second `hermes serve` or
  `hermes dashboard` on this box, including for a test.
- **Run `hermes dashboard`, not `hermes serve`.** `hermes serve` is the
  same server without the browser UI: it shows the login page, then
  answers "Headless backend (hermes serve): web UI disabled", and has no
  setting to enable it. The official web dashboard guide ("Remote
  dashboard setup") documents one `hermes dashboard` unit as the backend
  for Desktop clients and the browser.
- **New VPS agents are new profiles.** They join this backend; no agent
  gets its own backend unit or port.
- **Restart only when no agent is mid-turn.** A restart drops every open
  Desktop chat for a few seconds and ends any turn running on it.

## Operations

- **Health:** `systemctl show suggi-vps-hermes -p ActiveState -p
  ActiveEnterTimestamp`; `GET http://100.99.142.120:9119/api/status`
  returns 200.
- **Dashboard check:** sign in (`POST /auth/password-login`) and load
  `/`; the page title is "Hermes Agent - Dashboard". A login page alone
  proves nothing, because a headless backend serves it too.
- **Was it killed?** `grep 'reaped orphaned'
  /home/hermes/.hermes/logs/agent.log`.
- **After `hermes update`:** confirm the backend's start time is later
  than the update and restart it if not. The updater's systemd restart
  pass matches units named `hermes-serve*` and `hermes-dashboard*` only
  (`hermes_cli/update_cmd_fleet.py`), not `suggi-vps-hermes`.
- **Restarting from a chat that runs on this backend:** schedule it, e.g.
  `sudo systemd-run --on-active=120 systemctl restart
  suggi-vps-hermes.service`, so the reply finishes before the restart.

## Limits

- **One crash domain.** All Desktop and browser access stops together,
  and there is no per-profile restart of the backend.
- **The gateway is independent.** Crons, messaging and `hermes chat -q`
  keep running while the backend restarts, and the backend keeps running
  while the gateway restarts.
- **Upstream gaps.** Hermes has no install command for a backend service,
  so the unit is written by hand (issue #135478); the headless-serve trap
  and two-backend conflicts are reported in issues #84865, #120165 and
  #121596.

## Cross-Links

- `research/insights/desktop-gateway-switcher-runtime-id-leak-resolved.md`
  -- the Desktop app side: how the apps route chats to this backend.
- `reflections/2026-08-22_morpheus_desktop-app-state-has-three-tiers.md`
  -- where the Desktop apps store the connection to this backend.
