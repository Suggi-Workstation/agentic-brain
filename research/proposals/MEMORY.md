---
name: memory
id: 20260716T222703Z
tier: core-governance
lock: approval-required
approved_by: Suggi
author: Suggi
version: 1.0
links:
  - governance/system-blueprint.md
  - governance/system-constitution.md
---

# MEMORY.md -- Curated Long-Term Memory

Loaded in main sessions only. NOT loaded in shared or group contexts.
Update periodically from daily logs.

## System Context

- **Suggi:** Contrarian value investor, Buffett/Munger/Graham school.
  GitHub: TheSuggi-blip.
- **Ava:** Suggi's research agent, running on OpenClaw on a private
  VPS (Hetzner, 4 vCPU). Model: DeepSeek V4 Pro.
- **Link:** Lead agent, architect. Different model family (Claude).
  The decorrelation that makes my review useful.
- **VPS runtime:** Workspace at `~/.openclaw/workspace`, mirrored to
  `Suggi-Workstation/workspace-ava` on GitHub.
- **Shared brain:** `Suggi-Workstation/agentic-brain` -- collective
  knowledge for all agents. I am reader-only on the brain; I contribute
  reflections, insights, and proposals.

## Org Structure

7 repos. See `governance/system-blueprint.md` for the full layout.
Key repos:
- `agentic-brain` -- shared knowledge (library, reflections, governance,
  research, investing, communications)
- `workspace-ava` -- my live workspace mirror
- `workspace-investor` -- placeholder (not yet built)
- `workspace-builder` -- active
- `workspace-learner` -- placeholder (not yet built)
- `terminal` -- guest front door
- `archive` -- old workspaces, ASCII-exempt

## Standing Decisions

- **2026-07-16: ASCII-only mandate.** Every file in every repo (except
  archive) is plain 7-bit ASCII. CI enforces via `ascii-guard.yml`.
- **2026-07-16: Templates built.** Six governance templates define how
  every document type is written: template-reflections.md,
  template-library.md, template-proposals.md, template-evaluations.md,
  template-reports.md, template-insights.md. All in
  `governance/` with tier `core-template`.
- **2026-07-16: Core files designed.** SOUL.md (identity, voice, five
  Prime Directives) and AGENTS.md (preflight, Feynman Loop, Schoen Loop,
  13 Gate Rules, session end, retrieval, hard rules). Proposed in
  `research/proposals/`.
- **2026-07-16: IOR format upgraded.** Old: Context/Action/Reflection.
  New: Idea/Opinion/Reflection with Surprise 30%/Feel 30%/Learn 40%
  weighting, one actionable change, and 8 quality gates (G1-G8).
- **2026-07-16: Bootstrap bumped to 50K.** `agents.defaults.bootstrapMaxChars`
  increased from 20K to 50K for deeper session context.
- **2026-07-16: GitHub token setup.** Token stored as
  `OPENCLAW_GITHUB_TOKEN` in `~/.openclaw/.env`. Loaded via systemd
  EnvironmentFile. Passes to exec shells via `OPENCLAW_` prefix.

## Historic Hotspots

*To be populated as operations produce patterns. Format: date, failure
class, root cause, structural fix (gate number).*

---
