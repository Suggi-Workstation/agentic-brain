---
name: tools
id: 20260716T153605Z
tier: core-governance
lock: approval-required
approved_by: pending
author: ava
version: 1.0
links: []
---

# TOOLS.md -- Local Tool Conventions

This file does not control tool availability; it is only guidance.
Skills define how tools work. This file holds environment-specific notes.

## GitHub Access

- Token stored as `OPENCLAW_GITHUB_TOKEN` in `~/.openclaw/.env`
- Access pattern:
  ```
  git clone "https://${OPENCLAW_GITHUB_TOKEN}@github.com/Suggi-Workstation/<repo>.git"
  ```
- Org: Suggi-Workstation (7 repos, see blueprint)
- User: TheSuggi-blip

## SSH Hosts

*(populate as needed)*

## Cameras / Devices

*(populate as paired nodes become available)*

## Voice / TTS

*(populate if TTS provider is configured)*

## Workspace Paths

- Workspace: `/home/openclaw/.openclaw/workspace`
- Shared brain (clone-less access): `Suggi-Workstation/agentic-brain`

---

*v1.0 -- proposed 2026-07-16 by Ava.*
