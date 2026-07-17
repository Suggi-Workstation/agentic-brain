---
name: living-memory-vs-openclaw-memory-search
id: 20260717T053000Z
tier: report
author: ava
tags: [living-memory, memory-search, hybrid-search, semantic-search, openclaw, vector-search, rag, agent-architecture, knowledge-retrieval]
links:
  - research/insights/openclaw-manual.md
  - research/insights/context-engineering.md
---

# Living Memory vs. OpenClaw memory_search -- Architecture Comparison & Scale Analysis

## Executive Summary

**Question:** Is OpenClaw's built-in `memory_search` feature the same thing
as the custom Living Memory system we previously built for the agentic-brain?
Can we add the entire agentic-brain repo (projected 5,000--50,000 files) to
`memorySearch.extraPaths`?

**Answer:** They are architecturally identical at the core (hybrid vector +
keyword search over chunked markdown) but differ in implementation,
governance, and serving model. The old Living Memory was a custom Python
pipeline with bge-small embeddings, RRF fusion, PPR link traversal, eval
gates, and a freshness heartbeat -- built for a curated knowledge base.
OpenClaw `memory_search` is the same idea productized: SQLite-backed,
OpenAI-embedded, automatically reindexed, and exposed as an agent tool.
Adding 5,000--50,000 files via `extraPaths` is technically feasible at the
storage level (~1.25 GB vectors at 50K files, ~$1.75 one-time embedding
cost), but architecturally inadvisable: the built-in lacks the eval gates,
graph-based multi-hop, and freshness verification the old system needed to
stay trustworthy at scale. The correct path is to keep them as separate
systems serving different purposes: `memory_search` for agent session memory
(workspace-only), and a revived brain index for knowledge-base retrieval.

**Confidence:** High (85%). Architecture comparison: 90%. Scale feasibility:
80% (projection-based, not empirically tested). Recommendation: 85%.

---

## Research Question

Is OpenClaw's `memory_search` tool the same architecture as the "Living
Memory" system Link and I built for the agentic-brain in June 2026? If so,
can we consolidate by pointing `memorySearch.extraPaths` at the entire
agentic-brain repo, replacing the custom pipeline?

**Scope: in.** Architecture comparison, feature parity analysis, scale
feasibility for 5,000--50,000 files, cost projection, governance fit.

**Scope: out.** Migration implementation plan, detailed code comparison,
performance benchmarking (no access to the old bge-small index to run
side-by-side benchmarks).

**Why this matters:** The two systems exist in parallel. Consolidating them
would reduce maintenance burden, but only if the consolidated system is
at least as trustworthy as the one it replaces.

---

## Methodology

**Approach:** Architecture archaeology + specification analysis. I read the
source documents for both systems, compared them component-by-component,
and projected scale costs.

**Sources consulted (retrieved 2026-07-17):**

- Old Living Memory system:
  - `brain/insights/1a-livingmemory.md` (Core Insight, Link, v1.1)
  - `brain/reflections/2026-06-16_ava_living-memory-triad-audit.md` (Ava)
  - `brain/research/2026-06-16_living-memory-triad-architecture-audit.md` (Ava)
  - `brain/tools/build_semantic_index.py` (Link)
  - `brain/library/coding-ai/rag_vector_search_agent_knowledge_retrieval.md` (Link)
  - All archived in `Suggi-Workstation/archive`

- Current OpenClaw system:
  - `docs/concepts/memory.md` (OpenClaw 2026.7.1)
  - `docs/concepts/memory-search.md` (OpenClaw 2026.7.1)
  - `docs/concepts/memory-builtin.md` (OpenClaw 2026.7.1)
  - `docs/reference/memory-config.md` (OpenClaw 2026.7.1)
  - `docs/cli/memory.md` (OpenClaw 2026.7.1)
  - Live system state: `openclaw memory status --json`
  - `research/insights/openclaw-manual.md` (Link, 2026-07-16)

- Scale projection:
  - Current agentic-brain: 24 files, 169 KB, ~42K tokens
  - Archive: 1,851 files
  - Projection: 7 KB/file average, 4 chars/token, 400 token chunks

**Limitations:** No access to the old bge-small index to run comparative
benchmarks. Scale projection assumes average file size stays constant (it
may grow as library topics mature). Embedding cost is OpenAI-specific
(text-embedding-3-small at $0.02/1M tokens) and may change. The old PPR
multi-hop feature was built but OFF -- its absence in OpenClaw may not be
a real gap.

---

## Findings

### Finding 1: Core Architecture Is Identical

Both systems share the same fundamental design in the retrieval pipeline:

```
Markdown files -> Chunk (headings, ~400 tokens) -> Dual index ->
  (A) Vector embeddings for semantic similarity
  (B) Keyword index (BM25/FTS5) for exact-term matching
-> Rank fusion (RRF in old, weighted merge in new)
-> Top-k results
```

| Component | Old Living Memory | OpenClaw memory_search | Match? |
|:----------|:------------------|:----------------------|:-------|
| Source format | Markdown files | Markdown files | Yes |
| Chunking | ~400-1500 chars, heading-aware | ~400 tokens, 80-token overlap | Yes |
| Vector embeddings | bge-small (384-dim, float16) | OpenAI text-embedding-3-small (1536-dim) | Same class |
| Keyword search | BM25 (Python rank-bm25) | FTS5/BM25 (SQLite) | Same class |
| Rank fusion | RRF: sum 1/(k+rank), k~60 | Weighted merge (configurable) | Same class |
| Storage | Flat files (chunks.jsonl + vectors.npy) | Per-agent SQLite | Different |
| Serving | CLI script (query_brain.py) | Agent tool (memory_search) | Different |

**Verdict:** The retrieval core is the same idea implemented twice. The
differences are in embedding model choice, storage backend, and serving
interface -- not in what the system fundamentally does.

### Finding 2: The Old System Had Features OpenClaw Lacks

Three features built into the Living Memory that `memory_search` does not
provide:

**A. Graph-based multi-hop retrieval (PPR over explicit links)**

The old system added a third signal to RRF fusion: Personalized PageRank
over the curated `links:` frontmatter edges. This allowed retrieval to
follow explicit knowledge-graph connections ("this topic links to that
topic"). It was built but default-OFF because at alpha=0.85 it regressed
recall@20 on simple queries -- the documented PPR failure mode from
HippoRAG 2. It was designed to activate only when measured gains on a
multi-hop eval slice outweighed simple-query regression.

OpenClaw has no equivalent. The closest is temporal decay and MMR
diversity, which address different problems (recency and deduplication).

**B. Freshness heartbeat with eval gating**

The old system's `heartbeat.json` recorded both liveness ("did the loop
run?") and readiness ("is the index built against current origin HEAD?").
It was treated as a dead-man's-switch: missing beat = alarm. The eval
gate measured recall@20, MRR, and nDCG on gold queries -- any regression
blocked the index from being trusted.

This was the key insight from the triad audit: structural integrity
(heartbeat) and semantic quality (eval) are complementary. An index can
pass one and fail the other.

OpenClaw's `memory_search` has no eval gating, no heartbeat, and no
regression detection. It trusts the index because it was built -- there
is no verification that what was built is correct.

**C. Permanent ID link resolution**

The old system's "permanent ID" design meant links in frontmatter
(`links: [brain/insights/1a-livingmemory.md]`) survived file renames
because resolution went through the permanent `id:` field, not the
filename. This was partially built (Insight/Maxim cards used it) but
not fully deployed. OpenClaw has no link-resolution layer.

### Finding 3: OpenClaw Has Features the Old System Lacked

| Feature | Old Living Memory | OpenClaw memory_search |
|:--------|:------------------|:----------------------|
| Automatic reindex on file change | Manual (Task Scheduler, ~5 min) | Automatic (file watcher, 1.5s debounce) |
| Temporal decay | No (all content equal weight) | Yes (30-day half-life, configurable) |
| MMR diversity | No | Yes (reduces near-duplicate results) |
| Tool integration in agent loop | No (separate CLI) | Yes (memory_search tool, memory_get tool) |
| Multimodal (image/audio) | No | Yes (Gemini embeddings) |
| Incremental reindex | Homegrown content-hash manifest | Built-in |
| Session transcript indexing | No | Yes (opt-in) |

### Finding 4: Scale Feasibility -- Technically Possible, Architecturally Questionable

**Storage projection for 50,000 files (7 KB/file average):**

```
Files:              50,000
Tokens:             ~87.5 million
Chunks (400 tok):   ~218,750
Vector storage:     ~1.25 GB (1536-dim float32)
FTS5 index:         ~300--500 MB (estimated)
Total SQLite DB:    ~1.5--2 GB
One-time embed cost:~$1.75 (OpenAI text-embedding-3-small)
```

**Storage:** 1.5--2 GB SQLite database is within SQLite's practical limits
(up to 140 TB theoretical, tens of GB practical). The builtin backend
supports sqlite-vec for vector acceleration. This is fine.

**Cost:** $1.75 to embed the entire corpus is negligible. Incremental
reindexes (only changed files) would cost pennies per update cycle.

**Where it breaks down:**

1. **Recall quality at scale.** At 50,000 files, the corpus is diverse
   enough that pure vector + BM25 fusion will return noise for many
   queries. The old system planned a cross-encoder rerank step
   (TO BUILD) and graph-based multi-hop (BUILT, OFF) specifically
   because at ~1,500 files, raw RRF was already hitting precision
   limits. OpenClaw has neither.

2. **No eval gate.** Without recall@20 measurement, there is no way
   to know if search quality degrades. The old system's eval gate was
   built after WO-32 (mutual kNN failure) proved that regression is
   silent. At 50,000 files, a regression could hide for weeks.

3. **Git-based refresh conflict.** The agentic-brain changes
   independently from my workspace. `memorySearch.extraPaths` expects
   local files. TOOLS.md says I clone the brain temporarily, push
   changes, discard the clone. A persistent local clone would violate
   this convention and create a stale-mirror problem: the brain
   updates on GitHub, but my search index only updates when I
   manually pull.

4. **Separation of concerns.** The agentic-brain is a shared knowledge
   base (multiple agents read and write). My workspace memory is
   personal session context. Mixing them in one search index conflates
   two different retrieval intents: "what do I personally remember?"
   vs. "what does the org know about this topic?" These need different
   retrieval strategies, different freshness guarantees, and different
   trust models.

5. **The old system was already ~1,500 files and needed eval gates.
   At 50,000, the need for quality control is 33x greater, not less.**

---

## Discussion

### Convergence Is Not Coincidence

The fact that both systems independently converged on hybrid vector +
BM25 with rank fusion is not coincidence -- it is the 2025-2026 industry
standard. Anthropic's Contextual Retrieval, Qdrant, OpenSearch, Gemini,
and multiple arXiv papers all converge on this pattern. The old Living
Memory got it right. OpenClaw got it right. They are the same because
the problem has a best answer.

### What the Old System Did Better

The old Living Memory was built with a specific corpus in mind: a
curated, version-controlled knowledge base with explicit cross-links,
permanent IDs, and provenance tracking. It treated search quality as
a measurable property (eval gates) and index freshness as a
machine-detectable signal (heartbeat dead-man's-switch). These are
not features you bolt on later -- they are the architecture.

OpenClaw's `memory_search` was built for a different use case:
personal agent memory (MEMORY.md + daily logs). It trades governance
rigor for operational simplicity. It assumes small corpuses (tens to
hundreds of files), the embedding provider is trustworthy (no eval
needed), and file changes are infrequent. These assumptions hold for
workspace memory. They break for a 50,000-file knowledge base.

### What OpenClaw Does Better

The integration of memory search into the agent tool loop is the
killer feature the old system never had. Instead of running a separate
Python script, I call `memory_search` from within a session -- results
flow directly into my reasoning. The automatic file watching means
I never forget to reindex. The temporal decay means recent daily notes
don't get buried by older, larger files. These are real usability wins
that the old system's CLI-based approach could not match.

### The Right Architecture: Both, Not Either

| System | Corpus | Purpose | Governance |
|:-------|:-------|:--------|:-----------|
| `memory_search` | Workspace memory (MEMORY.md, daily logs) | Session context recall | Automatic, no eval needed |
| Brain index | agentic-brain (library, insights, reports) | Knowledge-base retrieval | Eval-gated, heartbeat-verified |

They serve different retrieval intents. Consolidating them into one tool
loses the governance the knowledge base needs and adds noise the session
context does not. The old system should be revived as a separate search
capability -- accessed via `web_search` against a published index, via
a custom tool, or via the `sessions_spawn` pattern where a sub-agent
queries the brain.

---

## Conclusion

OpenClaw `memory_search` IS the same core architecture as the old Living
Memory -- hybrid vector + keyword search over chunked markdown. They
converged independently on the industry-standard retrieval pattern.

But "same architecture" does not mean "same system." The old Living
Memory added governance layers (eval gates, freshness heartbeat, PPR
graph traversal, permanent IDs) that `memory_search` was never designed
to provide. Those layers were scar tissue from specific failures -- they
exist because the system broke without them.

Adding 50,000 files to `memorySearch.extraPaths` is technically possible
(1.25 GB vectors, $1.75 embedding cost) but architecturally wrong. It
would create a system that is neither good session memory (too much
noise) nor trustworthy knowledge retrieval (no eval gates).

**Recommendation:** Keep them separate. Use `memory_search` for
workspace session memory. Revive the brain index as an independently
governed knowledge-base retrieval system. The integration point should
be a tool or sub-agent, not a unified index.

**Open questions for future research:**
- Can a cross-encoder rerank step be added to `memory_search` via the
  QMD backend for precision at scale?
- Is the QMD backend (with its reranking and query expansion) a better
  fit for the brain corpus than the builtin backend?
- Should the revived brain index use OpenClaw's embedding infrastructure
  or stay independent (bge-small local)?

---

## Evaluation History

*Not yet evaluated. This is a first-pass report. Awaiting independent
review by Link (or Suggi's direct review).*

---

[ ] Frontmatter complete (6 fields: name, id, tier, author, tags, links)
[ ] id is UTC timestamp, never used before
[ ] Executive summary: question + answer + key evidence + confidence
[ ] Research question: falsifiable, scoped (in/out)
[ ] Methodology: reproducible, sources have retrieval dates, limitations stated
[ ] Findings: each with claim + evidence + confidence
[ ] Negative results: what was searched for and NOT found
[ ] Discussion: synthesizes findings, addresses surprises
[ ] Conclusion: restates question + answer + one recommendation + open questions
[ ] Evaluation history: at least one independent evaluation (APPROVE or APPROVE WITH CHANGES resolved)
[ ] Cross-links: evaluations + related reports + referenced library topics
[ ] Filename: lowercase, kebab-case slug
[ ] ASCII-only: zero non-ASCII characters in the file
