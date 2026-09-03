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
fail-closed state validation -- transforms the agentic-brain from a
pile of unsearchable Markdown files into a queryable knowledge base.
It uses local CPU infrastructure and no external embedding API.

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

- **heartbeat.json** records `built_at_head` at index time. One validator
  serves both health commands and checks heartbeat schema/types/time,
  required artifacts, model/dimension/chunking agreement, counts,
  vector shape and dtype, manifest/live Markdown hashes, and current
  HEAD.
- **eval.py** runs recall@20, MRR, and nDCG against gold queries. A
  regression exits nonzero instead of being reported as healthy.
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

~/.brain-index/               <-- index DATA path (NOT in repo)
  chunks.jsonl                Text chunks + frontmatter metadata
  vectors.npy                 Embedding vectors (float16, 768-dim)
  meta.json                   Build metadata (model, dim, count, chunking)
  manifest.json               Indexed Markdown paths and content hashes
  heartbeat.json              Freshness state (last_run_utc, built_at_head)
```

**Why code in repo, data outside:** the tool scripts are small,
shared, and versioned. Index data is derived, rebuildable from source,
and machine-local. It goes in `~/.brain-index/` and is gitignored --
the same pattern as `node_modules/` or `__pycache__/`.

### Who needs what

| Environment | Repository and index | Normal operation |
|---|---|---|
| Fleet VPS | Persistent clone at `/srv/brain/agentic-brain`; shared index at `/srv/brain/index` through `~/.brain-index` | Watcher pushes/pulls and incrementally reindexes; profiles query the shared data |
| Other machine | Its own clone and per-machine `~/.brain-index` | Pull source, maintain its local index, and run the same health/eval gates |

The source and package are shared through Git. Derived index data is
shared only by profiles on the same filesystem.

### Technology choices

| Component | Choice | Why |
|---|---|---|
| Embedding model | `unsloth/embeddinggemma-300m` (768-dim) | English-optimized, MTEB ~69 (Eng v2). Zero API cost. Runs on CPU. Public mirror of google/embeddinggemma-300m. Upgraded from bge-m3 on 2026-08-10. |
| Keyword search | Inline BM25 | Python-native, no database or stored keyword tables. |
| Rank fusion | Reciprocal Rank Fusion (k=60) | Balances semantic and keyword signals. Same formula the archive prototype used. |
| Chunking | Paragraphs up to 1,500 characters; 200-character overlap when splitting an oversized paragraph | Keeps ordinary paragraphs intact and bounds oversized ones. |
| Storage | `~/.brain-index/` with JSONL + NPY files | Simple, portable, no database server. Survives reboots. |
| Eval metric | recall@20, MRR, nDCG | Industry standard. Catches regression before deployment. |
| Freshness | Heartbeat + artifact/config/shape/manifest/live-corpus/HEAD validation | Any unverifiable state fails closed before retrieval. |

### Embedding model -- why embeddinggemma-300m

The live system uses `unsloth/embeddinggemma-300m`, a public mirror of
Google's 768-dimensional EmbeddingGemma retrieval model. Query and
document encoders are asymmetric and must remain distinct. The warm
daemon serves both with an in-process fallback; BM25 supplies the
sparse half. Routine builds embed only chunks from new or changed
files. Model, dimension, or chunking changes invalidate incremental
reuse and require a deliberate full rebuild followed by evaluation.

### VPS query flow -- how an agent uses it

```
BEFORE QUERY
============
1. Confirm the agentic-brain watcher line exists in the hermes crontab.
2. cd /srv/brain/agentic-brain
3. python brain-index/query.py --check-freshness
   -> OK: continue.
   -> STALE / UNVERIFIED / NO INDEX: HALT, inspect the index log, and
      report the watcher/index fault. Do not hide it with a rebuild.

DURING SESSION (as needed)
==========================
4. python brain-index/query.py "antitrust risk in digital platforms" --top-k 20
   -> Returns:
      [1] library/law-regulation/antitrust-digital-platforms.md
          "...market definition in two-sided platforms presents unique..."
      [2] library/technology/platform-regulation-eu-dma.md
          "...the Digital Markets Act establishes ex-ante obligations..."
      [3] research/insights/network-effects-moat.md
          "...switching costs and data network effects create durable..."
      ...

5. read_file on the top 3-5 results for deep context
6. Cite repository-relative source paths

SESSION END
===========
7. No action needed -- querying is read-only. The watcher owns routine
   synchronization and incremental indexing.

FALLBACK (if index unavailable)
===============================
8. Use `search_files` only against `/srv/brain/agentic-brain`, then read
   the full matching files. Report that this is keyword-only degraded
   mode. Never substitute another repository's index.
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

No index design is accepted until the eval harness exists and the gold
set contains validated, representative information needs. This inverts
the old pattern (index first, eval retrofitted) and keeps quality
measurable from day one.

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

Uniform frontmatter gives result labels and metadata predictable
meaning. The current CLI displays available domain and title metadata;
it does not perform graph expansion or expose metadata filters.

### Why not a network search server

Three reasons the filesystem-local index is the right architecture:

1. **No search API to maintain.** Retrieval reads JSONL/NPY files on
   the local filesystem. The only long-lived process is the local warm
   embedding daemon, shared by all three repository indexes.

2. **Machine boundaries stay explicit.** VPS profiles share filesystem
   data. Other machines can maintain their own derived indexes without
   adding a public service, authentication layer, or uptime dependency.

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

2. **Knowledge cannot be buried.** Every included Markdown artifact is
   discoverable after the next watcher tick. No manual cataloging is
   needed.

3. **Search quality is measurable.** The eval gate validates relevance
   targets and measures file-level Recall@20, MRR, and nDCG. It rejects
   an empty dense or sparse branch instead of scoring a partial hybrid
   pipeline as healthy.

4. **Freshness and integrity are visible.** Health checks compare the
   heartbeat, metadata, vectors, chunks, manifest, live corpus, config,
   and HEAD. A missing, malformed, stale, or incompatible component
   fails before retrieval.

5. **Zero external embedding cost.** EmbeddingGemma runs on local CPU;
   there are no embedding API calls, rate limits, or usage bills.

6. **New VPS profiles reuse the shared index.** They need the query
   skill and filesystem access, not a private dependency install or
   full rebuild.

## Counter-evidence

This architecture would be invalidated if:

- **Machine-local indexes diverge.** All VPS profiles read one shared
  index, so they cannot diverge from each other. An index on another
  machine may differ until its clone and index catch up; the same
  fail-closed health check makes that state visible.

- **A full build exceeds the session budget.** Mitigation: watcher-owned
  incremental indexing is the normal path. Full builds are exceptional
  operations for first setup, model/chunking changes, or corruption;
  they are not a response to an unexplained health failure.

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
