---
name: repo-search
description: "Use when searching brain, forge or investing-hub knowledge."
user-invocable: true
disable-model-invocation: false
---

# Repository Search

Entry point for knowledge in the shared repositories: choose the repository,
then load and follow its query skill.

## When to Use

- Before writing, deciding or answering from memory, to check for prior work,
  research, decisions or reflections.
- The task names or implies the brain, Library, governance, forge,
  investing-hub, a proposal, insight, evaluation or reflection, a company
  thesis, portfolio or watchlist.
- The right repository is unclear, or the answer may span repositories.

Not for public-web research (`web-search`), personal workspace files or
conversation history. When the repository is already clear, loading its query
skill directly is equivalent.

## Choose the repository

Choose by the question's subject and requested provenance, not by the agent's
identity or current working directory.

| Need | Repository and skill to load |
|---|---|
| General knowledge, Library topics, agents' reflections, governance, shared reports, insights, proposals or evaluations | `agentic-brain`: `skill_view(name="query-brain-vps")` |
| Forge ideas, research, evaluations, proposals, workflow/protocol, method lessons, and building or verification records where present | `agentic-forge`: `skill_view(name="query-forge-vps")` |
| Portfolios, watchlists, company research, investment theses, valuation/scoring frameworks, screening data or financial source documents | `investing-hub`: `skill_view(name="query-investing-vps")` |

A general investing concept in the Library belongs to Brain; an actual company
valuation or portfolio belongs to Investing. A shared reflection can inform a
Forge proposal without becoming a Forge artifact. Repository content alone does
not prove a proposed system is installed or running.

## Procedure

1. Load the relevant query skill and follow it fully. It owns paths, freshness
   checks, queries, source reads and failure handling; do not duplicate or skip
   those procedures here.
2. For a cross-repository question, load only the additional query skills needed.
   Preserve repository provenance when combining evidence; cite the actual files.
3. If the requested source is unclear, inspect the most relevant repository
   first or ask when choosing would materially change the answer. An empty
   result is not permission to substitute another repository silently.

Do not send private repository content to an external search service.
Searching does not authorize edits, index rebuilds, implementation, or
deployment.

## Verification

PASS: the selected query skill completed its checks, relevant source files were
read, and citations identify the correct repository. HALT an unsupported claim
of coverage, freshness or absence; report any unavailable repository explicitly.
