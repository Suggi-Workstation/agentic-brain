---
name: memory-search
id: 20260717T063000Z
tier: insight
source:
  - 20260717T053000Z
author: ava
tags: [memory-search, hybrid-search, openclaw-memory, knowledge-retrieval, agent-tools, local-embeddings]
links:
  - research/reports/living-memory-vs-openclaw-memory-search.md
  - research/insights/openclaw-manual.md
---

# How Memory Search Works in OpenClaw

## The Insight

`memory_search` is a hybrid retrieval tool that finds relevant notes
by meaning AND by exact terms -- it is not just keyword search, not
just semantic search, but both fused together in a single call.

## Evidence

OpenClaw ships a built-in memory engine backed by a per-agent SQLite
database. It chunks workspace memory files (MEMORY.md + memory/*.md)
into ~400-token pieces, then indexes each chunk two ways in parallel:

1. **Vector embeddings** -- a configured embedding model converts
   each chunk into a high-dimensional vector representing its
   semantic meaning. "gateway host" will match "the machine running
   OpenClaw" because their vectors are close, even with zero shared
   words. The provider is configurable: OpenAI, Gemini, Ollama,
   Voyage, local GGUF via llama.cpp, and others.

2. **BM25 keyword index** (FTS5) -- every word is tokenized for
   exact matching. Config keys like `bootstrapMaxChars`, error codes,
   and identifiers find their literal matches here. This path catches
   what embeddings miss: precise strings, version numbers, and
   technical symbols.

Results from both paths are merged with weighted scoring. A chunk that
matches both semantically AND contains the exact keyword ranks highest.
A chunk matching only one path still ranks, just lower.

The embedding provider is set via `agents.defaults.memorySearch.provider`
in `openclaw.json`. In the Suggi-Workstation setup, the local llama.cpp
provider (embeddinggemma-300m, 768-dim, ~600 MB) runs with zero API
cost and no external dependency. Other deployments may use OpenAI,
Ollama, or any supported backend.

Reindexing is automatic on file change with a 1.5-second debounce. A
full rebuild runs with `openclaw memory index --force --agent main`.

Source: `20260717T053000Z` (Living Memory vs OpenClaw memory_search
architecture comparison report). Implementation validated 2026-07-17:
local llama.cpp provider, 2 files, 6 chunks, hybrid search confirmed
functional.

## OpenClaw memory_search

### What it searches
The tool searches the agent's workspace memory files: `MEMORY.md`
(curated long-term memory) and `memory/YYYY-MM-DD.md` (daily session
logs). It does NOT search the agentic-brain, external repos, or
session transcripts by default (session transcript indexing is an
opt-in experimental feature).

### How the agent uses it
The agent calls `memory_search` with a natural-language query before
answering questions about prior work, decisions, dates, people, or
preferences. The tool accepts a query string and optional parameters
(`maxResults`, `minScore`, `corpus`).

Example: `memory_search "github token setup"` returns the chunk from
MEMORY.md about `OPENCLAW_GITHUB_TOKEN` even though those exact words
never appear in the query -- the vector path bridges the gap.

Search hits are scored (0.0 to 1.0). Higher score = stronger match.
The agent uses results to ground answers in what was actually written,
not assumed. Scores below ~0.3 are typically noise; scores above ~0.5
are usually relevant.

### How the index is built and maintained
- **Provider:** configurable via `openclaw.json`. Defaults to OpenAI
  if an API key is present; falls back to keyword-only otherwise.
  The Suggi-Workstation deployment uses `local` (llama.cpp).
- **Storage:** per-agent SQLite database at
  `~/.openclaw/agents/<agentId>/agent/openclaw-agent.sqlite`.
- **Auto-reindex:** a file watcher detects changes and reindexes
  incrementally within 1.5 seconds. No manual step needed after
  editing memory files.
- **Force rebuild:** `openclaw memory index --force --agent <id>`
  rebuilds everything from scratch. Required after changing the
  embedding provider, embedding model, or chunking configuration.
- **Health check:** `openclaw memory status` shows indexed file
  count, chunk count, provider, dirty status, and FTS readiness.

### When the index is unavailable
If the index is broken or missing (0 files, 0 chunks, or index
metadata error), `memory_search` returns disabled. The agent must:
1. Fall back to direct file reads with the `read` tool.
2. Notify the operator that the index is unavailable.
3. Run `openclaw memory index --force --agent <id>` to rebuild.

Common causes: embedding provider changed without a reindex, API key
missing for a remote provider, or the index database was corrupted.

### What it is not
`memory_search` is NOT a general-purpose knowledge-base search. It
does not search the agentic-brain library, archived workspaces, or
external websites. For brain content, the agent clones the brain
temporarily and uses `read`. For internet research, the agent uses
`web_search` or `web_fetch`. For the shared knowledge base at scale,
the old Living Memory brain-index system (bge-small + RRF + PPR
over explicit links) remains the reference architecture.

## Implications

1. Every agent must call `memory_search` before answering questions
   about prior work, decisions, or preferences -- this is a standard
   Retrieval instruction in agent bootstrap files.
2. If `memory_search` returns disabled, the agent must fall back to
   `read` on memory files directly and report the broken index to
   the operator.
3. The index is workspace-scoped. For agentic-brain content, agents
   clone temporarily and use `read` -- never `memory_search`.
4. When using a local embedding provider (llama.cpp), memory search
   has no API dependency and will not silently expire from an API
   outage. Only database corruption or missing files can break it.
5. Agents should not assume the index exists on a fresh deployment.
   The preflight should verify `openclaw memory status` before
   relying on `memory_search`.

## Counter-evidence

This insight would be invalidated if:
- The hybrid fusion (vector + BM25) produces worse results than pure
  keyword or pure vector search on a given corpus (not yet benchmarked
  on the Suggi-Workstation memory files at scale).
- The configured embedding model proves too slow or inaccurate for
  recall beyond trivial file counts (tested at 2 files, 6 chunks).
- A remote embedding provider outage causes a harder failure than
  the "fall back to keyword-only" design intends (not yet tested
  with a remote provider configured).

## Version History

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-07-17 | ava | Initial insight from memory_search implementation and architecture comparison. |

## Cross-Links

- `research/reports/living-memory-vs-openclaw-memory-search.md` -- source report
- `research/insights/openclaw-manual.md` -- related OpenClaw platform reference

---

[ ] Frontmatter complete (all fields, source: lists every origin artifact)
[ ] id is UTC timestamp, never used before
[ ] One-sentence insight: fits in one quotable line
[ ] Evidence: at least one source cited by id, chain of evidence complete
[ ] Implications: concrete changes or decisions, not platitudes
[ ] Counter-evidence: states what would prove the insight wrong
[ ] Version history: at minimum, a v1 row with date + author + change
[ ] Cross-links: source artifacts + related insights + affected governance
[ ] Filename: lowercase, kebab-case slug
[ ] ASCII-only: zero non-ASCII characters in the file
