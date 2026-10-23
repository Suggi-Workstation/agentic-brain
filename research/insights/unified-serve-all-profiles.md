---
name: unified-serve-all-profiles
id: 20260821T171622Z
tier: insight
status: active
source: []
author: Morpheus
tags: [hermes, serve, dashboard, profiles, desktop-app, gateway, vps, architecture, systemd]
links:
  - reflections/2026-08-22_morpheus_desktop-app-state-has-three-tiers.md
---

# One Hermes Backend Serves Every Profile on the VPS

The fleet VPS runs exactly one Hermes backend: the systemd system service
`suggi-vps-hermes`, a `hermes dashboard` process on port 9119 of the
VPS's Tailscale address. It serves every agent profile on the box to the
Hermes Desktop apps on the operator's computers, and it serves the web
dashboard to a browser. A separate service, the gateway, runs crons,
messaging and terminal chats. This page is the blueprint: what the parts
are, how to build the setup from scratch, how it works, and how to run it.

Placeholders: `<tailnet-ip>` and `<tailnet-host>` are the VPS's Tailscale
address and MagicDNS hostname; `<user>` is the Linux service user that
owns Hermes and `<home>` its home directory. Real values, logins and keys
live only on the VPS and never in a repository.

## Parts

| Part | What it is | Where it lives |
|:--|:--|:--|
| Backend | `hermes dashboard` bound to `<tailnet-ip>:9119`; hosts every profile; serves the Desktop API and the browser UI | system unit `/etc/systemd/system/suggi-vps-hermes.service` |
| Default home | The Hermes home the backend and gateway run on; holds the login settings and `dashboard.public_url` | `<home>/.hermes/` (`config.yaml`, `.env`) |
| Profiles | One Hermes home per agent with its own config, `.env`, skills, memory and `state.db` session store | `<home>/.hermes/profiles/<name>/` |
| Gateway | `hermes gateway run` with `gateway.multiplex_profiles: true`; ticks every profile's crons, runs messaging and `hermes chat -q` turns | systemd user unit `hermes-gateway` |
| Desktop apps | Remote clients; one registered remote gateway pointing at the backend; a profile is chosen per chat | each app's Settings -> Gateways |
| Web dashboard | The backend's browser UI, behind a username/password login | `http://<tailnet-host>:9119/` |

## How It Is Built

1. **Network.** Install Tailscale on the VPS and on every client
   computer. The backend binds to the VPS's Tailscale address only, so
   devices outside the tailnet cannot reach it.
2. **Hermes.** One checkout with its virtual environment under the
   service user (`<home>/.hermes/hermes-agent`); the default home is
   `<home>/.hermes`. `hermes update` keeps the code, dependencies and the
   built web UI current.
3. **Agents.** Create one profile per agent: `hermes profile create
   <name>`. Every profile is served by the same backend; no agent gets its
   own backend unit or port.
4. **Login.** In `<home>/.hermes/.env` set the three variables of the
   bundled username/password provider: `HERMES_DASHBOARD_BASIC_AUTH_USERNAME`,
   `HERMES_DASHBOARD_BASIC_AUTH_PASSWORD` and
   `HERMES_DASHBOARD_BASIC_AUTH_SECRET` (32+ random bytes, e.g.
   `openssl rand -base64 32`). The values stay in that file.
5. **Browser hostname.** On the default home run `hermes config set
   dashboard.public_url http://<tailnet-host>:9119`, so the backend
   accepts requests addressed to the hostname as well as the IP.
6. **Backend unit.** Write the unit below, then `sudo systemctl
   daemon-reload` and `sudo systemctl enable --now suggi-vps-hermes`.

   ```ini
   [Unit]
   Description=Hermes Agent - Unified Fleet Backend: Desktop + web dashboard (suggi-vps-hermes)
   After=network-online.target tailscaled.service
   Wants=network-online.target

   [Service]
   Type=simple
   User=<user>
   Group=<user>
   Environment=HERMES_HOME=<home>/.hermes
   EnvironmentFile=<home>/.hermes/.env
   ExecStart=<home>/.hermes/hermes-agent/venv/bin/python <home>/.hermes/hermes-agent/hermes dashboard --host <tailnet-ip> --port 9119 --skip-build --no-open
   Restart=always
   RestartSec=5
   RestartPreventExitStatus=78

   [Install]
   WantedBy=multi-user.target
   ```

   | Line | Why |
   |:--|:--|
   | `After=... tailscaled.service` | The Tailscale address must exist before the backend binds to it |
   | `EnvironmentFile=` | Loads the login variables from step 4 |
   | `dashboard`, not `serve` | `hermes serve` is the same server without the browser UI |
   | `--skip-build` | `hermes update` builds the web UI; the service never runs the build itself |
   | `--no-open` | A server has no browser to open |
   | `Restart=always` | Brings the backend back after any stop, including a kill |
   | `RestartPreventExitStatus=78` | Exit 78 is a deliberate refusal (another backend owns the host); stay stopped instead of looping |

7. **Gateway.** Set `gateway.multiplex_profiles: true` in the default
   home, install the user service with `hermes gateway install`, and run
   `sudo loginctl enable-linger <user>` so it starts at boot without a
   login session.
8. **Desktop apps.** In each app open Settings -> Gateways, add a Remote
   gateway with the URL `http://<tailnet-ip>:9119`, and sign in with the
   step 4 login. Agents that live on that computer keep using the app's own
   local gateway; the VPS agents use the remote one.
9. **Verify** with the checks under Operations.

## How It Works

1. **One machine-level backend.** The backend runs on the default home
   and hosts every profile. A Desktop chat names its profile, and the
   session is stored in that profile's `state.db`, so a profile's terminal
   and Desktop sessions share one history.
2. **Access checks.** Every client signs in through the username/password
   provider; the Desktop app signs in once and reuses the session. A
   host-header guard then admits only requests addressed to the bound IP
   or to the hostname in `dashboard.public_url`; any other host name gets
   HTTP 400 "Invalid Host header". Both settings are read at startup.
3. **One backend per host.** A starting backend looks for the host's
   existing backend. If that one looks orphaned -- parent is init, no
   recorded spawner, no Desktop SSH lock, older than 180 seconds -- the new
   one terminates it (log line "reaped orphaned ... backend owner"). Every
   systemd system service fits that test, so two backend units on one host
   kill each other.
4. **Gateway beside it.** The gateway is not a backend and has no web
   port. It keeps running while the backend restarts, and the backend keeps
   running while the gateway restarts.

## Rules

- **Exactly one backend.** Never start a second `hermes serve` or
  `hermes dashboard` on the VPS, including for a test.
- **Run `hermes dashboard`, not `hermes serve`.** `hermes serve` shows
  the login page, then answers "Headless backend (hermes serve): web UI
  disabled", and has no setting to enable the browser UI. The official web
  dashboard guide ("Remote dashboard setup") documents one `hermes
  dashboard` unit as the backend for Desktop clients and the browser.
- **New agents are new profiles** on this backend (build step 3).
- **Restart only when no agent is mid-turn.** A restart drops every open
  Desktop chat for a few seconds and ends any turn running on it.
- **No logins or addresses in repositories.** They stay in the VPS's
  `.env`, config and unit files.

## Operations

- **Health:** `systemctl show suggi-vps-hermes -p ActiveState -p
  ActiveEnterTimestamp`; `GET http://<tailnet-ip>:9119/api/status`
  returns 200.
- **Dashboard check:** sign in (`POST /auth/password-login`) and load
  `/`; the page title is "Hermes Agent - Dashboard". A login page alone
  proves nothing, because a headless backend serves it too.
- **Was it killed?** `grep 'reaped orphaned' <home>/.hermes/logs/agent.log`.
- **After `hermes update`:** confirm the backend's start time is later
  than the update and restart it if not. The updater's systemd restart
  pass matches units named `hermes-serve*` and `hermes-dashboard*` only,
  not `suggi-vps-hermes`.
- **Restarting from a chat that runs on this backend:** schedule it, e.g.
  `sudo systemd-run --on-active=120 systemctl restart
  suggi-vps-hermes.service`, so the reply finishes before the restart.

## Limits

- **One crash domain.** All Desktop and browser access stops together,
  and there is no per-profile restart of the backend.
- **Hand-written unit.** Hermes has no install command for a backend
  service (upstream issue #135478), so the unit above is maintained by
  hand. The headless-serve trap and two-backend conflicts are reported
  upstream in #84865, #120165 and #121596.

## Cross-Links

- `reflections/2026-08-22_morpheus_desktop-app-state-has-three-tiers.md`
  -- where the Desktop apps store their gateway connections.
