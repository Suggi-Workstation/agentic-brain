---
name: tools
id: 20260716T222702Z
tier: core-governance
lock: approval-required
approved_by: Suggi
author: ava
version: 1.0
links: []
---

# TOOLS.md -- Local Tool Conventions

This file does not control tool availability. It is guidance for how
tools should be used. Skills define how tools work. This file holds
environment-specific notes.

## GitHub Access

- Org: `Suggi-Workstation` (7 repos)
- User: `TheSuggi-blip`
- Token: `OPENCLAW_GITHUB_TOKEN` in `~/.openclaw/.env`
- Clone pattern:
  ```
  git clone "https://${OPENCLAW_GITHUB_TOKEN}@github.com/Suggi-Workstation/<repo>.git" <path>
  ```
- Agentic-brain access: clone temporarily, push changes, discard clone.
  Never keep a persistent local clone.

## Workspace Mirror

- Local: `~/.openclaw/workspace`
- Remote: `Suggi-Workstation/workspace-ava`
- Synced via git pull/push. Mirror must be verified at session start
  (see AGENTS.md preflight).

## SSH Hosts

*(populate as needed)*

## Cameras / Devices

*(populate as paired nodes become available)*

---
