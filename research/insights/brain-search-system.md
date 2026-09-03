---
name: brain-search-system
id: 20260720T182751Z
tier: insight
source:
  - 20260719T070443Z
  - 20260717T095454Z
  - 20260717T035333Z
author: Link
tags:
  - brain-index
  - hybrid-search
  - semantic-search
  - retrieval
  - eval-gate
  - freshness
  - bm25
  - vector-search
  - uniform-templates
links:
  - research/insights/stale-index-problem.md
  - research/proposals/brain-index-search-proposal.md
  - research/reports/living-memory-vs-openclaw-memory-search.md
  - research/insights/memory-search.md
  - governance/template-library.md
  - governance/template-insights.md
---

# Brain Search System -- The Complete Blueprint

This file is the finished-system reference for the brain-index search
tool. It describes the system as built and operational -- every agent
in the Suggi-Workstation org can search the shared knowledge base. It
serves as the single source of truth for HOW the system works, WHERE
each piece lives, and WHAT each agent must do to use it.

## The Insight

A self-contained hybrid search tool -- semantic vectors plus keyword
BM25 fused with reciprocal rank fusion, gated by eval benchmarks and
a freshness heartbeat -- transforms the agentic-brain from a pile of
unsearchable markdown files into a queryable knowledge base that every
agent can use independently, without servers, without API costs, and
without drift between what is on disk and what is in the index.

## Evidence

### Archive provenance -- the system already works

The June 2026 hub-brain archive (`Suggi-Workstation/archive`, folder
`hub-brain - github repo - 20.06.26`) contains a fully operational
prototype of this system:

- **Embedder:** `unsloth/embeddinggemma-300m` (768-dim,
  public mirror of google/embeddinggemma-300m), sentence-transformers
- **Index scale:** 24,592 chunks across 1,648 brain files, 36 domains
- **Tools:** `build_semantic_index.py` (indexer), `query_brain.py`
  (query CLI), `eval_retrieval.py` (eval harness)
- **Eval gate:** 230 gold queries across 4 batches (Ava batch1/2,
  Link batch1/2), each with expected file hits and heading targets
- **Freshness:** `heartbeat.json` with `git rev-parse HEAD` comparison
- **Fusion:** semantic (embeddinggemma-300m) + BM25 +
  frontmatter-graph expansion (three retrieval edges combined).
  Cross-encoder reranking was evaluated (bge-reranker-base) and
  REMOVED: it added +15s/query (model reload per fresh process) and
  measurably hurt ranking (MRR 0.817 with vs 0.955 without on the
  100-query gold set). Embed + BM25 + RRF is the final pipeline.

The prototype proved the architecture at scale. The only failure mode
was data quality: the 1,348 library files had inconsistent frontmatter
(no uniform templates, no standard `id:` fields, random tags). The
search engine worked. The content being searched was the bottleneck.

That bottleneck is now solved. The current agentic-brain (v2, rebuilt
from scratch) enforces uniform templates via write-x skills: every
library topic follows `template-library.md`, every insight follows
`template-insights.md`, every proposal follows `template-proposals.md`.
Uniform frontmatter means the indexer can reliably extract domain,
tags, status, author, and cross-links from every file.

### Stale index problem -- the structural fix

The insight at `stale-index-problem.md` (20260719T070443Z) identified
the failure class: index health checks that use threshold conditions
(`files > 0`) instead of consistency checks (`indexed_count ==
filesystem_count`) allow silent drift. The brain-index system embeds
this fix structurally:

- **heartbeat.json** records `built_at_head` at index time. Every health
  check validates the heartbeat, index artifacts, metadata counts, live
  Markdown hashes against the manifest, and current HEAD.
- **eval.py** runs recall@20, MRR, and nDCG against gold queries. A
  regression in search quality fails the build -- silence is broken.
- **index.py --check** returns OK, STALE, or UNVERIFIED with the detected
  inconsistency. Agents surface this to their operator.

### Separation from session memory

The report at `living-memory-vs-openclaw-memory-search.md`
(20260717T035333Z) established why brain-index retrieval must stay
separate from session memory search:

1. **Trust models differ:** session memory is personal and forgiving
   (a missed result is inconvenient). Knowledge-base retrieval is
   shared and consequential (a missed result is a research gap).
2. **Scale differs:** the brain grows to 50,000 files. Session memory
   stays at hundreds of daily logs.
3. **Verification differs:** the brain-index needs eval gates and
   freshness heartbeat. Session memory needs zero-maintenance
   automation.

## The System -- How It Works

### Where everything lives

```
agentic-brain repo (GitHub) -- SHARED by all agents
====================================================
brain-index/                  <-- tool CODE (in repo)
  index.py                    Build the search index from markdown files
  query.py                    Query the index, return ranked results
  eval.py                     Run eval against gold queries (recall@20, MRR, nDCG)
  config.yaml                 Embedding model, chunk size, RRF weights
  gold-queries.yaml           Test queries with one or more relevant files
  self-test.py                Package contract and regression tests
  requirements.txt            Python deps (sentence-transformers, pyyaml, numpy)
  README.md                   Setup and usage for every agent

/opt/repo-tools/             <-- FLEET tools (NOT in repo)
  brain-embed.py              Warm embedding daemon (embeddinggemma-300m,
                              loaded once at boot; 127.0.0.1:8099)
  brain-embed.service         systemd unit (enabled, auto-restart)

query.py embeds queries via the warm daemon (sub-second); if the
daemon is down it falls back to in-process model loading (~15s).
Indexing uses the same daemon first and falls back to in-process model
loading when the daemon is unavailable.

~/.brain-index/               <-- index DATA (per-machine, NOT in repo)
  chunks.jsonl                Text chunks + frontmatter metadata
  vectors.npy                 Embedding vectors (float16, 768-dim)
  meta.json                   Build metadata (model, dim, count, built_at)
  manifest.json               Indexed Markdown paths and content hashes
  heartbeat.json              Freshness state (last_run_utc, built_at_head)
```

**Why code in repo, data outside:** the tool scripts are small (~500
lines each), shared, and versioned. The index data is large (~38 MB
for 25K chunks), rebuildable from source, and machine-specific. It
goes in `~/.brain-index/` and is gitignored -- same pattern as
`node_modules/` or `__pycache__/`.

### Who needs what

| Component | VPS agents (Ava, researcher-1/2, investor) | Link (Hermes, Suggi's PC) |
|---|---|---|
| `brain-index/` tool code | From `git pull` of brain repo | From `git pull` of brain repo |
| `~/.brain-index/` data | **Shared** -- one index at `~/.brain-index/` on VPS | **Separate** -- own index on Suggi's PC |
| Python 3.10+ + pip | Already on VPS | Already on Windows |
| `pip install -r requirements.txt` | Once | Once |
| `python index.py --force` | Once (full build) | Once (full build) |
| `python query.py` | All VPS agents share the same local index | Link queries his local index |

Three VPS agents share ONE index because they run on the same machine.
Link runs on a different machine and builds his own. Both indexes are
built from the same source (the brain repo). Both are verified by the
same eval gate.

### Technology choices

| Component | Choice | Why |
|---|---|---|
| Embedding model | `unsloth/embeddinggemma-300m` (768-dim) | English-optimized, MTEB ~69 (Eng v2). Zero API cost. Runs on CPU. Public mirror of google/embeddinggemma-300m. Upgraded from bge-m3 on 2026-08-10. |
| Keyword search | Inline BM25 | Python-native, no database or stored keyword tables. |
| Rank fusion | Reciprocal Rank Fusion (k=60) | Balances semantic and keyword signals. Same formula the archive prototype used. |
| Chunking | Paragraphs up to 1,500 characters; 200-character overlap when splitting an oversized paragraph | Keeps ordinary paragraphs intact and bounds oversized ones. |
| Storage | `~/.brain-index/` with JSONL + NPY files | Simple, portable, no database server. Survives reboots. |
| Eval metric | recall@20, MRR, nDCG | Industry standard. Catches regression before deployment. |
| Freshness | `heartbeat.json` vs `git rev-parse HEAD` | Dead-man's-switch: stale index = visible alarm to any agent. |

### Embedding model -- why embeddinggemma-300m

The archive prototype used bge-small-en-v1.5 (24,592 chunks at 384
dimensions, ~38 MB of float16 vectors, CPU-only, ~2 minutes per full
build). Upgraded to unsloth/embeddinggemma-300m (768-dim, MTEB ~69
English v2, public mirror of google/embeddinggemma-300m) on
2026-08-10 -- best English quality for its size. The warm daemon serves
query/document embeddings with an in-process fallback; BM25 provides
the sparse half. Full
rebuild takes 10-30 minutes on the EPYC CPU (one-time cost; the
watcher keeps it incremental afterward). An incremental build
(only changed files)
takes seconds.

The model was released by BAAI (Beijing Academy of AI) in 2023 and is
one of the most battle-tested small embedding models for English text.
It was designed for retrieval tasks on documents like these -- markdown
files with structured frontmatter and prose bodies.

Alternative models (all-MiniLM-L6-v2, bge-m3, gte-modernbert-base
  -- embeddinggemma-300m chosen: best English MTEB for its size,
  public mirror, in-process)
can be swapped via `config.yaml`. The eval gate catches any regression
from model changes.

### Session flow -- how an agent uses it

```
SESSION START
=============
1. cd /tmp && git clone --depth 1 <brain-repo> brain-pf
2. cd brain-pf
3. python brain-index/query.py --check-freshness
   -> OK:        "heartbeat matches HEAD, index is current"
   -> STALE:     "3 commits behind, index built at 2026-07-19 14:00 UTC"
4. If STALE: python brain-index/index.py
   -> Incremental if possible, full rebuild if config changed

DURING SESSION (as needed)
==========================
5. python brain-index/query.py "antitrust risk in digital platforms" --top-k 20
   -> Returns:
      [1] library/law-regulation/antitrust-digital-platforms.md (score: 0.87)
          "...market definition in two-sided platforms presents unique..."
      [2] library/technology/platform-regulation-eu-dma.md (score: 0.82)
          "...the Digital Markets Act establishes ex-ante obligations..."
      [3] research/insights/network-effects-moat.md (score: 0.79)
          "...switching costs and data network effects create durable..."
      ...

6. read_file on the top 3-5 results for deep context
7. Cite sources in the session artifact

SESSION END
===========
8. No action needed -- the index is read-only. The heartbeat records
   when it was last built. The next session's freshness check will
   catch any drift.

FALLBACK (if index unavailable)
===============================
9. grep -r "search term" /tmp/brain-pf/ --include="*.md"
   -> Keyword-only search on the raw files. No semantic matching.
   -> Agent reports the broken index to the operator.
```

### Build order -- eval first

The archive's highest-stakes lesson: start with the eval harness, not
the indexer. The build order is:

```
1. gold-queries.yaml    Define representative queries and relevance sets
2. eval.py              Harness that measures recall@20, MRR, nDCG
3. eval.py (empty)      Run against empty query set -- verify it fails cleanly
4. config.yaml          Chunking, model, RRF parameters
5. index.py             Build the index from current brain files
6. query.py             Query the index
7. eval.py (live)       Run against the built index -- must pass all queries
8. heartbeat.json       Freshness tracking
9. README.md            Usage documentation for all agents
```

No index is built until the eval harness exists and the gold query set
has at least 5 queries. This inverts the old pattern (index first, eval
retrofitted) and ensures quality is measurable from day one.

### Gold queries grow with the brain

Gold queries are written against the current brain content. As the
brain grows, queries are added. This is NOT a chicken-and-egg problem
-- the eval gate works at any scale:

The live target count belongs in `gold-queries.yaml`; do not duplicate it
here. Coverage, not a fixed ratio to chunks, governs set size:

| Surface | Required coverage |
|---|---|
| Library | Every current domain plus cross-domain questions |
| Governance | Stable rules, templates, and operating procedures |
| Research | Proposals, reports, evaluations, and insights |
| Reflections | Representative transferable themes |

### What the index covers

The indexer scans the entire brain repo and indexes every nonexcluded
Markdown file. Frontmatter is extracted when present. The scope is
"compounding knowledge":

- `governance/` -- system-constitution, primedirectives, templates
- `library/` -- all current domain topic files
- `research/` -- insights, proposals, evaluations, reports
- `reflections/` -- agent session reflections

Excluded: `logbook/` (append-only logs, queried separately via tail),
`scripts/` (executable code, not knowledge), `.github/` (CI config).
Investing content moved to the investing-hub repo (see
`governance/system-blueprint.md` for the org layout).

When present, frontmatter is retained as metadata (domain, tags,
status, author, links) and displayed with results. The current CLI
does not expose metadata filters.

### Frontmatter uniformity -- why it matters

The archive prototype's 1,348 library files had inconsistent
frontmatter. Some had `domain:` fields, some did not. Tags were
random. The search engine could find files by content but could
not reliably filter by domain or cross-reference by id.

The current brain enforces uniform templates via write-x skills:

- `template-library.md` -- uniform `domain:`, `tags:`, `status:`,
  `links:` fields on every library topic
- `template-insights.md` -- uniform `source:`, `tags:`, `links:`
  fields on every insight
- `template-proposals.md`, `template-evaluations.md`,
  `template-reflections.md`, `template-reports.md` -- analogously

This uniformity means the indexer can trust that every file has an
`id:`, a `tags:` list, and `links:` edges. The PPR graph traversal
(opt-in) depends on these edges existing. The domain filter depends
on the `domain:` field being present. Uniform templates make the
search engine structurally reliable.

### Why not a shared search server

Three reasons the per-agent local index is the right architecture:

1. **No server to maintain.** The brain-index has zero moving parts:
   Python scripts + JSONL/NPY files on disk. No API to secure, no
   process to keep alive, no database to migrate.

2. **Agents run on different machines.** The VPS (Ava + sub-agents)
   and Suggi's PC (Link) are physically separate. A shared server
   would need network access, authentication, and uptime guarantees.
   A local index works offline.

3. **Rebuildable from source.** If `~/.brain-index/` is corrupted or
   lost, `python index.py --force` rebuilds it from the brain repo
   in minutes. There is no irreplaceable state.

The VPS agents share one index because they share a filesystem. This
is an optimization, not a requirement -- each could build its own.

## Implications

1. **Every agent can search the shared knowledge base.** Instead of
   guessing which file contains antitrust analysis, an agent asks the
   index and gets ranked results with snippets and scores. This is the
   difference between a library and a stack of paper.

2. **Knowledge cannot be buried.** Every library topic, insight, and
   reflection added to the brain is automatically discoverable. The
   indexer picks up new files on the next build. No manual cataloging
   needed.

3. **Search quality is measurable.** The eval gate means regressions
   are caught before deployment. A model change that hurts recall is
   flagged, not shipped. This prevents the stale-index failure class
   documented in `stale-index-problem.md`.

4. **Freshness is visible.** The heartbeat dead-man's-switch means a
   stale index cannot silently serve bad results. Any agent querying
   the index can see the last-build timestamp and compare it against
   the brain's HEAD.

5. **Zero API cost, zero infrastructure.** The entire system runs on
   commodity hardware with no external services. embeddinggemma-300m
   runs on CPU (dense-only via sentence-transformers). No embedding API calls, no rate limits, no monthly
   bills. Embedding 50,000 files costs zero dollars beyond compute
   time.

6. **New agents onboard instantly.** A new agent (Researcher-1,
   Investor, etc.) runs `pip install -r requirements.txt`, then
   `python index.py --force`, and can search the entire brain.
   No other setup needed.

## Counter-evidence

This architecture would be invalidated if:

- **Per-agent index divergence causes conflicting search results.**
  Two agents querying the same term get different top-10 lists because
  their indexes were built at different times from different brain
  states. Mitigation: the heartbeat.json makes freshness visible. An
  agent with a stale index knows it is stale. In practice, divergence
  is bounded by git pull frequency -- two agents who pull the same
  HEAD build identical indexes.

- **Index build time exceeds the session budget.** At 50,000 files,
  a full rebuild with embeddinggemma-300m on CPU takes ~30-40
  minutes for ~5,000 chunks on a 12-core EPYC (300M params, 768-dim,
  batch 32; measured 2026-08-10). An agent that needs to rebuild from
  scratch mid-session cannot afford the wait. Mitigation: incremental
  indexing (only changed files) takes seconds. Full rebuilds are a
  once-per-machine setup cost, not a per-session cost.

- **The eval gate becomes the bottleneck.** Writing and reviewing gold
  queries for every new library domain requires domain expertise. If
  relevance judgment cannot keep pace with brain growth, the eval gate
  loses coverage. Mitigation: validate every target before scoring,
  fail nonzero below the recall threshold, and reassess relevance sets
  at corpus-growth milestones.

- **A simpler tool makes this obsolete.** If GitHub adds semantic
  code search to private repos, or if a tool like `ripgrep-all`
  adds hybrid search with zero setup, the self-built indexer becomes
  unnecessary. Mitigation: the architecture is simpler than it looks
  -- three Python files and a config. The cost of building it is low.
  The cost of replacing it later is lower.

## Cross-Links

- `research/insights/stale-index-problem.md` -- the failure class this
  system structurally prevents (threshold vs consistency checks)
- `research/proposals/brain-index-search-proposal.md` -- the original
  proposal that defined the architecture (now updated with archive
  findings)
- `research/reports/living-memory-vs-openclaw-memory-search.md` --
  why brain-index and session memory must stay separate
- `research/insights/memory-search.md` -- how OpenClaw memory search
  works and its scope limitations
- `governance/template-library.md` -- the uniform template that makes
  library files machine-searchable
- `governance/template-insights.md` -- the uniform template that makes
  insights machine-searchable
- Archive: `Suggi-Workstation/archive` > `hub-brain - github repo -
  20.06.26/brain/_index/` -- proven prototype with 24,592 chunks
