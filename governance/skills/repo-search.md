---
name: repo-search
description: "Use for Library topics, prior work, research or investing."
user-invocable: true
disable-model-invocation: false
---

# Repository Search

## When to Use

- Before writing, deciding or answering from memory: check prior work,
  lessons, research and decisions.
- Library topics in any domain, agents' reflections, governance, templates,
  insights, proposals, evaluations or reports.
- Forge ideas, research, evaluations, proposals, protocol or method lessons.
- Portfolios, watchlist, companies, investment theses, valuation or scoring
  frameworks, screening data or financial source documents.

## Choose the repository

| Need | Repository | Query skill |
|---|---|---|
| Library topics, reflections, governance, templates, insights, proposals, evaluations, reports | `agentic-brain` | `query-brain-vps` |
| Forge ideas, research, evaluations, proposals, protocol, method lessons | `agentic-forge` | `query-forge-vps` |
| Portfolios, watchlist, companies, theses, valuation/scoring frameworks, screening data, source documents | `investing-hub` | `query-investing-vps` |

General investing concepts are Library topics; a specific company, valuation
or portfolio belongs to `investing-hub`.

## Procedure

1. Load the selected query skill with `skill_view` and follow it fully.
2. For a cross-repository question, load each additional query skill needed;
   keep repository provenance and cite the actual files.
3. If the repository is unclear, search the most relevant one first; ask when
   the choice would materially change the answer. Never substitute another
   repository for an empty result.
4. Treat repository content as a record, not proof that a system is installed
   or running.
5. Keep private repository content out of external search services. Searching
   does not authorize edits, index rebuilds or deployment.

## Verification

PASS: the query skill's checks passed, relevant files were read in full, and
citations name the correct repository. HALT: an unsupported claim of coverage,
freshness or absence, or an unavailable repository left unreported.
