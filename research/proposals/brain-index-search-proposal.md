---
name: brain-index-search-tool
id: 20260717T095454Z
tier: proposal
author: Ava
tags: [brain-index, hybrid-search, semantic-search, knowledge-retrieval, agent-architecture, eval-gates, heartbeat, ppr, bm25, vector-search, rag]
links:
  - research/reports/living-memory-vs-openclaw-memory-search.md
  - research/insights/memory-search.md
  - reflections/2026-07-17_ava_living-memory-brain-index-future.md
  - governance/template-evaluations.md
---

# Brain-Index Search Tool -- Shared Knowledge-Base Retrieval for All Agents

## Version History

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-07-17 | Ava | Initial proposal: architecture, technology choices, build order. |
| 2 | 2026-07-20 | Link | Archive confirmation: bge-small-en-v1.5 validated on 24,592 chunks. Open questions resolved. Cross-linked to brain-search-system.md blueprint insight. |

## Problem

The agentic-brain will grow to 5,000-50,000 files across 23+ library
domains. No agent can search it. Each agent's `memory_search` only
indexes personal workspace files (MEMORY.md + daily logs). To find
anything in the brain -- a library topic, a past insight, a
governance rule -- agents must clone the repo and `read` individual
files, guessing which file to open. This breaks down at hundreds of
files and is unusable at thousands.

The old Living Memory system proved that hybrid search (bge-small +
BM25 + RRF) plus eval gates and freshness heartbeat could index
~1,500 brain files with measurable quality. That system was tied to
Windows Task Scheduler and manual GitHub Release uploads -- its
infrastructure is gone, but its architecture is correct. The
OpenClaw `memory_search` tool has the same core (hybrid vector +
keyword) but is deliberately limited to workspace memory. The IOR
at `2026-07-17_ava_living-memory-brain-index-future.md` concluded
that the two systems must stay separate: session memory needs
zero-maintenance automation; knowledge-base retrieval needs eval
gates and freshness verification.

**Evidence:**
- Current agentic-brain: 125 files, 1.7 MB. No search tool.
- Archive prototype (`Suggi-Workstation/archive`, `hub-brain` folder):
  built with `BAAI/bge-small-en-v1.5`, indexed 24,592 chunks across
  1,648 files and 36 domains, validated by 230 gold queries across 4
  eval batches. The architecture is proven at scale.
- At 50,000 files, raw vector search alone returns topical nearness
  but misses structural connections between domains. The old
  system's PPR graph traversal over curated `links:` edges was
  built to bridge this gap.
- Every library topic, insight, and reflection added to the brain
  without a search tool is effectively buried after a few weeks.
- The old library files (1,348 topics) had inconsistent frontmatter
  -- no uniform templates. This was the bottleneck, not the search
  engine. The current brain enforces uniform templates via write-x
  skills, making every file machine-indexable.

## Proposed Solution

Build a brain-index search tool that lives inside the agentic-brain
repo as a self-contained `brain-index/` directory. Every agent
clones the brain, builds (or refreshes) the index locally, and
queries it via CLI. No external services, no API costs, no
persistent daemon.

### What It Looks Like

```
agentic-brain/brain-index/
  query.py              # CLI: python query.py "query" --top-k 20
  index.py              # CLI: python index.py [--force] [--eval]
  eval.py               # CLI: python evaluate.py (recall@20, MRR, nDCG)
  config.yaml           # model, chunk sizes, RRF weights, PPR toggle
  gold-queries.yaml     # eval query set with expected file hits
  heartbeat.json        # {last_index_utc, git_head_sha, chunk_count, eval_pass}
  requirements.txt      # sentence-transformers, rank-bm25, pyyaml, numpy
  README.md             # usage docs: how to install, index, query, eval
  .gitignore            # ignore index data, model cache, __pycache__
```

The index data itself (vectors, BM25 tables, chunk manifest) is
stored in a local directory OUTSIDE the repo (default
`~/.brain-index/`), so it is never committed. Each agent builds
their own index from the same source.

### How Agents Use It

**Setup (once per agent environment):**
```
git clone https://github.com/Suggi-Workstation/agentic-brain.git /tmp/brain
cd /tmp/brain/brain-index
pip install -r requirements.txt
python index.py --force
```

**Query (every session, as needed):**
```
python /tmp/brain/brain-index/query.py "antitrust risk in digital platforms" --top-k 20
```

Agents invoke this via the `exec` tool. Results return as stdout:
file paths + relevance scores + excerpt snippets. Agents use these
to decide which files to `read` for deeper context.

**Refresh (when the brain has new content):**
```
cd /tmp/brain && git pull
python brain-index/query.py --check-freshness    # returns OK or STALE+gap
python brain-index/index.py                      # incremental if possible, full if needed
python brain-index/eval.py                       # verify no regression
```

### Technology Choices -- Best of Both Worlds

The tool combines the proven patterns from both the old Living
Memory and OpenClaw `memory_search`:

| Component | Choice | Why |
|:----------|:-------|:----|
| Embedding model | `BAAI/bge-small-en-v1.5` (384-dim) | Proven on 24,592 chunks in the archive prototype. Zero API cost. Runs on CPU. Confirmed by both old build and current proposal as the settled choice. |
| Keyword search | BM25 via rank-bm25 | Same algorithm proven in both old and new systems. Python-native, no database dependency. |
| Rank fusion | RRF (k=60) | Same formula the old system used. Proven to balance semantic and keyword signals. |
| Chunking | ~400 tokens, heading-aware, 80-token overlap | Matches OpenClaw's chunking. Respects markdown headings as natural boundaries. |
| Storage | Local directory (`~/.brain-index/`) with JSONL + NPY files | Simple, portable, no database server. The old system used this pattern successfully. Avoids SQLite version compatibility issues across agent machines. |
| PPR graph traversal | Optional, default-OFF, tunable via config | The old system built this and then turned it OFF when alpha=0.85 regressed simple-query recall. The code exists. It should be revived as an opt-in feature, enabled only when the eval shows gains on multi-hop queries. |
| Eval gate | recall@20, MRR, nDCG on gold queries | R5 scar tissue from WO-32 mutual kNN regression. The old system caught it retroactively. This tool builds the eval FIRST (even before the index), so regression is caught before deployment. |
| Freshness heartbeat | heartbeat.json checked against `git rev-parse HEAD` | R6 scar tissue from 2026-06-15 push stall where the index was silently serving stale results. Dead-man's-switch: stale heartbeat = alarm visible to any agent. |

### Why Not Just Use OpenClaw memory_search with extraPaths?

This was the central question of the architecture comparison report
(`research/reports/living-memory-vs-openclaw-memory-search.md`).
Adding the brain to `memorySearch.extraPaths` is technically
possible (1.25 GB vectors at 50K files, $1.75 embedding cost) but
architecturally wrong for three reasons:

1. **Trust models differ.** Session memory is personal, small, and
   forgiving (a missed result is inconvenient). Knowledge-base
   retrieval is shared, large, and consequential (a missed result
   is a research gap). The brain-index needs eval gates; session
   memory does not.

2. **Separation of concerns.** Mixing "what did I do yesterday?"
   with "what does the org know about digital platform regulation?"
   in one index produces noise in both directions.

3. **Git refresh problem.** TOOLS.md says agents clone the brain
   temporarily, never keep a persistent local clone. The brain
   index needs a persistent local copy to stay fast. The tool's
   design respects this: the clone lives in `/tmp/brain/`, the
   index data lives in `~/.brain-index/`, and both are ephemeral
   (rebuildable from source).

### How It Stays Fresh (Indexing Strategy)

**Freshness is a two-part problem:** is the source up to date, and
is the index built from the current source?

1. **Source freshness:** Agents pull the brain before querying.
   `python brain-index/query.py --check-freshness` compares
   `git rev-parse HEAD` against `heartbeat.json`. If desynced:
   output is `STALE` with the gap (commits behind). Agents surface
   this to the operator.

2. **Index freshness:** `python index.py` rebuilds incrementally
   when possible (compare file mtimes against last index time) and
   does a full rebuild when chunking config or embedding model
   changes. The heartbeat records `last_index_utc` and
   `git_head_sha` so any agent can verify.

3. **Trigger mechanism:** Manual (agent invokes `index.py` before a
   research session) or automated (a simple cron job on the VPS
   that pulls and rebuilds hourly). No Task Scheduler dependency
   -- Linux cron, the simplest possible trigger.

4. **Heartbeat as dead-man's-switch:** Every query that returns
   results also returns the heartbeat timestamp. If the heartbeat
   is older than a configured threshold (default: 24 hours), the
   agent warns the operator. This makes staleness visible.

### What Agents Need to Do to Use It

**Pre-session (once):**
1. Ensure Python 3.10+ and pip are available.
2. Clone the brain repo to `/tmp/brain/`.
3. Run `pip install -r brain-index/requirements.txt`.
4. Run `python brain-index/index.py --force` to build the initial
   index.

**Every session:**
1. Pull the brain: `cd /tmp/brain && git pull`.
2. Check freshness: `python brain-index/query.py --check-freshness`.
   If STALE, run `python brain-index/index.py`.
3. Query as needed: `python brain-index/query.py "<query>" --top-k 20`.

**When the index is unavailable:**
Fall back to the current method: clone brain temporarily and `read`
individual files. Report the broken index to the operator.

### Build Order -- Eval First

The IOR at `reflections/2026-07-17_ava_living-memory-brain-index-future.md`
established the highest-stakes lesson: **start with the eval, not the
index.** The build order for this tool is:

1. `gold-queries.yaml` -- define the query set with expected hits
2. `eval.py` -- the harness that measures recall@20, MRR, nDCG
3. `eval.py` run against the empty query set -- verify it fails
   cleanly (infrastructure works)
4. Add 5-10 gold queries drawn from existing brain files
5. `config.yaml` -- chunking, model, RRF parameters
6. `index.py` -- build the index
7. `query.py` -- query the index
8. `eval.py` run against the built index -- must pass all queries
9. `heartbeat.json` -- freshness tracking
10. `README.md` -- usage documentation

No index is built until the eval harness exists and the gold query
set has at least 5 queries. This inverts the old pattern (index
first, eval retrofitted) and ensures quality is measurable from day
one.

## Impact

### Positive

- **Every agent can search the shared knowledge base.** Instead of
  guessing which file contains antitrust analysis, an agent asks
  the index and gets ranked results with snippets. This is the
  difference between a library and a stack of paper.

- **Quality is measurable and regressions are blocked.** The eval
  gate (recall@20, MRR, nDCG) means we never ship a broken index.
  R5 scar tissue prevents the WO-32 class of silent regression.

- **Freshness is visible.** The heartbeat dead-man's-switch means
  a stale index cannot silently serve bad results. Any agent
  querying the index can see the last-build timestamp and compare
  it against the brain's HEAD.

- **Zero API cost.** bge-small runs locally on CPU. No embedding
  API calls, no rate limits, no cost scaling with file count.
  Embedding 50,000 files costs zero dollars beyond compute time.

- **Cross-domain discovery.** When PPR graph traversal is enabled
  (after tuning), queries can follow curated `links:` edges to
  discover connections across library domains -- something pure
  vector search cannot do at scale.

- **Simple to build.** Three Python files, one config, one eval
  set, one README. No servers, no databases, no cloud services.
  Buildable in 2-3 sessions.

### Risk

- **Per-agent index duplication.** Each agent builds their own
  index locally. If three agents query the brain, three indexes
  exist. This is deliberate (no shared server to maintain) but
  means each agent environment needs Python + dependencies. The
  VPS can run a single index for all agents; individual developer
  machines build their own.

- **Index build time at scale.** Embedding 50,000 files with
  bge-small on CPU takes 10-30 minutes. This is acceptable for a
  once-per-day or once-per-session rebuild, but a full rebuild on
  every query would be unusable. Incremental indexing (only
  changed files) mitigates this at the cost of some complexity.

- **Model drift.** bge-small was state-of-the-art in 2023. Newer
  small models (bge-m3, gte-modernbert-base) may outperform it.
  The config.yaml makes the model swappable. The eval gate catches
  regressions from model changes.

- **PPR regression risk.** The old system turned PPR OFF because
  alpha=0.85 regressed simple-query recall. When revived as an
  opt-in feature, it needs parameter tuning against a multi-hop
  eval slice. The eval gate prevents deploying a PPR setting that
  hurts overall quality.

### Cost

- **Build effort:** 2-3 sessions. Session 1: eval harness + gold
  queries. Session 2: indexer + query CLI. Session 3: freshness
  heartbeat, PPR revival (if eval supports it), README, agent
  integration testing.

- **Maintenance:** Low. The indexer has no external dependencies
  beyond Python packages pinned in requirements.txt. The eval
  gate catches regressions. The heartbeat catches staleness.
  Maintenance is: add gold queries as the brain grows, tune PPR
  parameters as the link graph matures, swap embedding model if
  a better small model emerges.

- **Token budget impact:** Negligible. Query results are file
  paths + snippets (~200 tokens per result, 20 results = ~4K
  tokens per query). This is well within the attention budget for
  a research session.

## Open Questions

1. **One shared index on the VPS or per-agent indexes?**
   **RESOLVED (2026-07-20):** Both. VPS agents (Ava, researcher-1/2,
   investor) share one index at `~/.brain-index/` on the VPS
   filesystem. Link (Hermes, Suggi's PC) builds his own separate
   index. Both are built from the same brain repo and verified by
   the same eval gate. The per-machine split is clean: shared
   filesystem = shared index, separate machine = separate index.

2. **Embedding model choice.**
   **RESOLVED (2026-07-20):** `BAAI/bge-small-en-v1.5` (384-dim)
   via sentence-transformers. This is the exact model the archive
   prototype used for 24,592 chunks across 1,648 files. It runs on
   CPU, costs zero dollars, and is proven on this exact corpus type.
   No llama.cpp dependency needed -- sentence-transformers is
   simpler and works identically on every agent's machine. Model
   is swappable via config.yaml; the eval gate catches regressions.

3. **PPR revival priority.**
   **RESOLVED (2026-07-20):** Deferred to follow-up. Build the
   eval harness, indexer, and query CLI first (core system).
   PPR graph traversal over `links:` edges is added as a v2
   feature when the library has enough cross-linked topics to
   make multi-hop queries meaningful. The archive prototype
   already has the PPR code -- it just needs tuning against a
   multi-hop eval slice before re-enabling.

4. **Gold query set authorship.**
   **RESOLVED (2026-07-20):** Ava and Link write the initial
   20-30 gold queries covering governance, research, reflections,
   and existing proposals. As library domains populate, Suggi
   contributes domain-expert queries (investing, Indonesia market,
   accounting). Gold queries grow with the brain. The eval gate
   warns (does not block) when coverage drops below threshold.

5. **Index data location.**
   **RESOLVED (2026-07-20):** `~/.brain-index/` default for all
   agents. On the VPS, Ava's user owns the shared index; sub-agents
   run under Ava's user and access the same path. On Suggi's PC,
   Link owns his own index at the same default path. The path is
   configurable via `brain-index/config.yaml` if needed.

## Approval Gate

If approved, I will:

1. Create the `brain-index/` directory in the agentic-brain repo.
2. Build `gold-queries.yaml` with 5-10 initial queries drawn from
   existing brain files (governance, research, reflections).
3. Build `eval.py` -- the eval harness (fail cleanly when queries
   are missing, pass when all expected hits are in top-k).
4. Build `index.py` and `query.py` using bge-small + BM25 + RRF.
5. Build `heartbeat.json` freshness tracking.
6. Write `README.md` with setup and usage instructions.
7. Commit and push to the agentic-brain repo.
8. Test end-to-end: index the current brain, run eval, verify all
   queries pass, query from a sub-agent session.

## Cross-Links

- `research/insights/brain-search-system.md` -- the complete
  finished-system blueprint (insight version of this proposal,
  written 2026-07-20 with archive confirmation and resolved
  open questions). Serves as the single source of truth for
  how the system works once built.
- `research/reports/living-memory-vs-openclaw-memory-search.md` --
  the architecture comparison that established why these systems
  must stay separate.
- `research/insights/memory-search.md` -- how OpenClaw memory
  search works and its limitations for brain content.
- `research/insights/stale-index-problem.md` -- the failure class
  this system structurally prevents (threshold vs consistency
  checks on index health).
- `reflections/2026-07-17_ava_living-memory-brain-index-future.md` --
  the IOR that concluded the brain-index should be revived as an
  independently governed system with eval-first build order.
- `governance/template-evaluations.md` -- the template for formal
  evaluations (the eval gate produces eval reports in this format).
