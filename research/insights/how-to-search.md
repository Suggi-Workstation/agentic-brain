---
name: how-to-search
id: 20260717T063000Z
tier: insight
source:
  - 20260717T053000Z
author: ava
tags: [memory-search, hybrid-search, openclaw, knowledge-retrieval, agent-tools, local-embeddings]
links:
  - research/reports/living-memory-vs-openclaw-memory-search.md
  - research/insights/openclaw-manual.md
---

# How Memory Search Works in OpenClaw

## The Insight

`memory_search` is a hybrid retrieval tool that finds relevant notes
by meaning AND by exact terms -- it is not just keyword search, not
just semantic search, but both fused together.

## Evidence

OpenClaw ships a built-in memory engine backed by SQLite. It chunks
workspace memory files (MEMORY.md + memory/*.md) into ~400-token
pieces, then indexes each chunk two ways in parallel:

1. **Vector embeddings** -- a local embedding model (embeddinggemma-300m,
   768 dimensions) converts each chunk into a list of numbers
   representing its meaning. "gateway host" will match "the machine
   running OpenClaw" because their vectors are close.

2. **BM25 keyword index** (FTS5) -- every word is tokenized for exact
   matching. Config keys like `bootstrapMaxChars` and error codes find
   their literal matches here.

Results from both paths are merged with weighted scoring. A chunk that
matches both semantically AND contains the exact keyword ranks highest.

The embedding model runs locally on the VPS via the llama.cpp provider
plugin. No API key, no external service. Reindexing is automatic on
file change, with a 1.5-second debounce. Force a full rebuild with
`openclaw memory index --force --agent main`.

Source: `20260717T053000Z` (Living Memory vs OpenClaw memory_search
architecture comparison report). The implementation was validated on
2026-07-17 with a local provider, 2 files indexed, 6 chunks, working
search confirmed.

## OpenClaw memory_search

### What it searches
The tool searches only workspace memory files: `MEMORY.md` (curated
long-term memory) and `memory/YYYY-MM-DD.md` (daily session logs).
It does NOT search the agentic-brain, external repos, or session
transcripts (unless the experimental session-memory feature is enabled).

### How the agent uses it
I call `memory_search` with a natural-language query before answering
questions about prior work, decisions, dates, people, or preferences.
For example: `memory_search "github token setup"` returns the chunk
from MEMORY.md about `OPENCLAW_GITHUB_TOKEN` even though those exact
words never appear in the query.

The search hits are scored. Higher score = stronger match. I use the
results to ground my answers in what was actually written, not what
I assume was written.

### How the index is built and maintained
- **Provider:** local (llama.cpp + embeddinggemma-300m-qat-Q8_0.gguf,
  768-dim vectors, ~600 MB model, zero API cost).
- **Storage:** per-agent SQLite database at
  `~/.openclaw/agents/main/agent/openclaw-agent.sqlite`.
- **Auto-reindex:** file watcher detects changes and reindexes
  incrementally within 1.5 seconds.
- **Force rebuild:** `openclaw memory index --force --agent main`
  rebuilds everything from scratch. Required after changing the
  embedding provider or model.
- **Health check:** `openclaw memory status` shows indexed file count,
  chunk count, provider, and dirty status.

### When the index is unavailable
If the index is broken or missing (0 files, 0 chunks), `memory_search`
returns disabled. Fall back to direct file reads with the `read` tool
and tell Suggi. The fix is typically `openclaw memory index --force`.

### What it is not
`memory_search` is NOT a general-purpose knowledge-base search. It
does not search the agentic-brain library, archived workspaces, or
external websites. Those require separate tools: cloning the brain
temporarily for file reads, `web_search` for the internet, or the old
Living Memory brain-index system for the shared knowledge base.

## Implications

1. I must call `memory_search` before answering any question about
   prior work, decisions, or preferences -- this is already in my
   Retrieval instructions in AGENTS.md.
2. If memory_search returns disabled, I must fall back to `read` on
   memory files directly and report the broken index.
3. The index is workspace-scoped only. For agentic-brain content,
   I clone temporarily and use `read` -- never `memory_search`.
4. The local embedding model means memory search is always available
   as long as the llama-cpp plugin is installed and the index exists.
   No API dependency.

## Counter-evidence

This insight would be invalidated if:
- The local embedding model proves too slow or inaccurate for recall
  at scale (tested: 2 files, 6 chunks -- trivial. At 500+ files the
  quality and latency are untested).
- The hybrid fusion produces worse results than pure keyword or pure
  vector search on our specific corpus (not yet benchmarked).
- The llama-cpp provider fails on this VPS hardware (4 vCPU, no GPU)
  under load (embedding 6 chunks worked; embedding 100+ concurrently
  is untested).

## Version History

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-07-17 | ava | Initial insight from memory_search implementation session. |

## Cross-Links

- `research/reports/living-memory-vs-openclaw-memory-search.md` -- source report
- `research/insights/openclaw-manual.md` -- related OpenClaw platform reference
- `research/insights/context-engineering.md` -- related context system insight

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
