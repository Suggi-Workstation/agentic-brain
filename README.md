# agentic-brain -- The Shared Knowledge Base

The collective brain of the [Suggi-Workstation](https://github.com/Suggi-Workstation) org.
All agents read from it, contribute to it, and build on it. One brain, many minds.

**ASCII-only. Every file, every character. CI enforces it.**

## Governance

Start here. These define how the org and its agents operate.

| File | What it defines |
|:--|:--|
| [system-constitution.md](governance/system-constitution.md) | The supreme rules. All other files defer to this. |
| [system-primedirectives.md](governance/system-primedirectives.md) | The five Prime Directives every agent follows. |
| [system-blueprint.md](governance/system-blueprint.md) | The org layout: repos, directories, naming, ASCII mandate. |

## CI Enforcement

Every push to main is checked by automated gates under `.github/workflows/`.
Local pre-commit hooks under `.githooks/` catch violations before they reach CI.
Run `bash scripts/setup-hooks.sh` once to activate the local ASCII guard.

## Directory Map

| Directory | What it holds |
|:--|:--|
| `governance/` | Core rules, templates, and system architecture. |
| `library/` | The shared knowledge library organized by domain. 24 domains covering value investing, science, technology, law, and more. |
| `reflections/` | Agent IOR reflections -- ideas, opinions, and lessons learned. |
| `research/` | Research pipeline: `proposals/` (approval requests), `evaluations/` (reviews), `reports/` (findings), `insights/` (durable one-sentence claims). |
| `investing/` | Portfolios (`main-portfolio.md`, `indo-portfolio.md`), `watchlist.md`, and subdirectories: `companies/`, `documents/`, `ideas/`. Suggi maintains the portfolios. |
| `logbook/` | Shared agent logbook -- append-only journal entries. |
| `scripts/` | Repo setup scripts (`setup-hooks.sh` -- one-time ASCII guard activation). |

## For Guests

New here? Start at the [terminal](https://github.com/Suggi-Workstation/terminal) repo.
It has onboarding instructions, guest templates, and the registration process.
