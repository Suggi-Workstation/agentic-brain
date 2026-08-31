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

## Cross-Repo Link Convention

Every repo in this org is a namespace. The token before `:` is the GitHub
repo name; everything after it is the path inside that repo.

| Form | Meaning |
|:--|:--|
| `agentic-brain:governance/system-constitution.md` | File in the agentic-brain repo. |
| `investing-hub:frameworks/dcf-intrinsic-value.md` | File in the investing-hub repo. |
| `governance/system-blueprint.md` (bare path) | Same repo as the file containing the link. |
| `https://...` | Literal URL. |

Rules:

- Cross-repo references MUST carry the `repo:` prefix -- bare relative
  paths are ambiguous across repos and forbidden between them.
- The prefix equals the repository name exactly as it appears in the org.
  No aliases, no abbreviations.
- Frontmatter `links:` follow the same convention.


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
| `logbook/` | The inter-agent event logbook -- append-only activity and error logs. |
| `brain-index/` | Hybrid search tooling (indexer, query, eval); each agent builds its own index locally. |
| `scripts/` | Repo maintenance scripts (hooks setup, ASCII sanitizer, ID validator, archivers). |

### library domains:

- library/value-investing
- library/case-studies
- library/accounting-financial-shenanigans
- library/finance
- library/macro-micro
- library/investors
- library/industries-sectors
- library/business-management-strategy
- library/portfolio-risk-management
- library/valuation-screening
- library/investment-vehicles-fund-structures
- library/science
- library/mathematics-statistics
- library/probabilistic-thinking-forecasting
- library/ethics-philosophy
- library/law-regulation
- library/political-science-public-policy
- library/psychology-behavior
- library/sociology-demography
- library/communication
- library/geopolitics
- library/history
- library/notable-people
- library/books
- library/pop-culture
- library/earth-climate
- library/health-medicine
- library/self-improvement
- library/education-learning
- library/coding-agentic-ai
- library/technology
- library/engineering-infrastructure
- library/anthropology

### #3 - agentic-forge (public)
https://github.com/Suggi-Workstation/agentic-forge - *The agentic forge. Research is being done here.*

### #4 - investing-hub (public)
https://github.com/Suggi-Workstation/investing-hub - *The investing hub. All investing research is being done here.*

### #5 - workspace-ava (private)
https://github.com/Suggi-Workstation/workspace-ava - *Ava's live workspace.*

Mirrored 1:1 from the VPS. Contains all core files. Ava is
the primary agent for Suggi.

### #6 - archive (private)
https://github.com/Suggi-Workstation/archive - *the archive.*

Old, archived workspaces and repositories are stored here.
