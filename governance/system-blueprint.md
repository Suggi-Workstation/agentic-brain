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
| Ava | Openclaw (VPS) | `workspace-ava` | Manager of the VPS, personal assistant |
| Link | Hermes (local PC) | none (local only) | Suggi's personal assistant |
| Linkie | Hermes (laptop) | none (local only) | Suggi's personal assistant |
| Morpheus | Hermes (VPS) | none (VPS only) | Manager of the VPS, personal assistant |
| Neo | Hermes (VPS) | none (VPS only) | Experimental self-learning solo agent |

Link and Linkie are local (PC, Laptop) assistants with Access to the VPS.
Morpheus and Ava are independet managers of the VPS and help Suggi build and
maintaing it.
Neo is an independent solo main agent pursuing autonomous research through a 
self-directed learning.


## Repos

### #1 - terminal (public)
https://github.com/Suggi-Workstation/terminal - *the main terminal.*

A Readme + Instructions for guests. And also a main hub with directions to the whole GitHub org. A navigation hub starting point.

### #2 - agentic-brain (public)
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

### #3 - agentic-forge (public)
https://github.com/Suggi-Workstation/agentic-forge - *The agentic forge. Research is being done here.*

### #4 - workspace-ava (private)
https://github.com/Suggi-Workstation/workspace-ava - *Ava's live workspace.*

Mirrored 1:1 from the VPS. Contains all core files. Ava is
the primary agent for Suggi.

### #5 - archive (private)
https://github.com/Suggi-Workstation/archive - *the archive.*

Old, archived workspaces and repositories are stored here.
