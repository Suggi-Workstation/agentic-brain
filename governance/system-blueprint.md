---
name: system-blueprint
id: 20260618T120013Z
tier: core-system
lock: approval-required
approved_by: Suggi
author: Suggi
links:
  - governance/system-constitution.md
  - governance/system-primedirectives.md
---

## Blueprint
**This is the evergreen layout for the GitHub org**

> **ASCII-ONLY - every file, no exceptions.** Write every file in this system in plain 7-bit ASCII.

## The GitHub Org
- **Name:** Suggi-Workstation
- **URL:** https://github.com/Suggi-Workstation
- **Access:** GitHub UI; `gh` CLI; `git` (pull/push)

## Known Agents

| Agent | Location | GitHub Mirror | Role |
|:--|:--|:--|:--|
| Ava | VPS (OpenClaw) | `workspace-ava` | Suggi's personal assistant |
| Cato | VPS (OpenClaw) | `workspace-cato` | Experimental self-learning solo agent |
| Link | Hermes (local PC) | none (local only) | Suggi's personal assistant |
| Linkie | Hermes (laptop) | none (local only) | Suggi's personal assistant |

Ava, Link, and Linkie form a decorrelated agent team -- three independent
perspectives cross-checking each other's work. Cato is an independent
main agent pursuing autonomous research through a self-directed
forge pipeline -- he operates solo, not as part of the review team.


## Repos

### #1 - terminal
https://github.com/Suggi-Workstation/terminal - *the main terminal.*

A Readme + Instructions for guests. And also a main hub with directions to the whole GitHub org. A navigation hub starting point.

### #2 - agentic-brain
https://github.com/Suggi-Workstation/agentic-brain - *the shared brain hub.*

| Path | Holds |
| :---------------------------- | :--------------------------------------------------------------------------------- |
| `library/[domain]` | The shared library with the various knowledge domains and their individual topics. |
| `reflections/` | The shared individual reflections of all Agents. |
| `governance/` | The core rules for the system governance. |
| `research/proposals/` | Research proposals are stored here. |
| `research/evaluations/` | Research evaluations are stored here. |
| `research/reports/` | Research reports are stored here. |
| `research/insights/` | Insights are stored here. |
| `investing/companies/` | The individual company files are stored here. |
| `investing/documents/` | Investment documents are stored here. |
| `investing/ideas/` | Investment ideas are stored here. |
| `investing/main-portfolio.md` | The Main Portfolio. Only Suggi will keep it up to date. |
| `investing/indo-portfolio.md` | The Indonesia Portfolio. Only Suggi will keep it up to date. |
| `investing/watchlist.md` | The watchlist. Potential candidate companies for the portfolios are kept here. |
| `logbook/` | The inter-agent event logbook -- append-only activity and error logs. |

### library domains:

- library/value-investing
- library/case-studies
- library/accounting-financial-shenanigans
- library/finance
- library/macro-micro
- library/investors
- library/industries-sectors
- library/portfolio-risk-management
- library/valuation-screening
- library/science
- library/mathematics-statistics
- library/probabilistic-thinking-forecasting
- library/ethics-philosophy
- library/law-regulation
- library/psychology-behavior
- library/geopolitics
- library/notable-people
- library/books
- library/pop-culture
- library/earth-climate
- library/self-improvement
- library/coding-agentic-ai
- library/technology
- library/anthropology

### #3 - workspace-ava

https://github.com/Suggi-Workstation/workspace-ava - *Ava's live workspace.*

Mirrored 1:1 from the VPS. Contains all core files. Ava is
the primary agent for Suggi.

### #4 - workspace-cato

https://github.com/Suggi-Workstation/workspace-cato - *Cato's live workspace.*

Mirrored 1:1 from the VPS. Contains all core files. Cato is
the experimental self-learning solo agent for Suggi.

### #5 - workspace-researcher-1

https://github.com/Suggi-Workstation/workspace-researcher-1 - *workspace for the first research agent.*

Lean workspace for independent deep-dive research. Runs on its own model.

### #6 - workspace-researcher-2

https://github.com/Suggi-Workstation/workspace-researcher-2 - *workspace for the second research agent.*

Lean workspace for independent deep-dive research. Runs on its own model.

### #7 - workspace-verifier

https://github.com/Suggi-Workstation/workspace-verifier - *workspace for the verifier agent.*

Lean workspace for verifying. Runs on its own model.

### #8 - archive
https://github.com/Suggi-Workstation/archive - *the archive.*

Old, archived workspaces and repositories are stored here.
