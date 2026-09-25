---
name: repo-search
description: "Use when finding knowledge in our shared repositories."
user-invocable: true
disable-model-invocation: false
---

# Repository Search

Use for prior knowledge, research, decisions, reflections or artifacts in the
shared repositories. Choose by the question's subject and requested provenance,
not by the agent's identity or current working directory.

## Choose the repository

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

Personal workspace knowledge and conversation history need their own retrieval
routes. Public-web research uses `web-search`; do not send private repository
content to an external search service. Searching does not authorize edits,
index rebuilds, implementation, or deployment.

## Verification

PASS: the selected query skill completed its checks, relevant source files were
read, and citations identify the correct repository. HALT an unsupported claim
of coverage, freshness or absence; report any unavailable repository explicitly.
