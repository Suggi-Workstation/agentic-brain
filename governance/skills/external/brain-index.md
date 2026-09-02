---
name: brain-index
description: "Build, query, eval, and maintain the agentic-brain hybrid search index. Covers index.py (full + incremental), query.py (dense + BM25 + RRF, optional rerank), eval.py (recall@20, MRR, nDCG), gold queries, freshness heartbeat."
user-invocable: true
disable-model-invocation: false
---

# Brain-Index -- Hybrid Search for the Agentic-Brain

The brain-index tool lives at `brain-index/` in the agentic-brain repo.
It provides hybrid dense+sparse search over all markdown files
in the shared knowledge base.

## Architecture

```
agentic-brain/brain-index/          (tool code -- committed to repo)
  index.py            Build index: full (--force) or incremental
  query.py            Query: hybrid (dense+BM25+RRF; optional rerank), --no-dense, --no-sparse
  eval.py             Eval: recall@20, MRR, nDCG against gold queries
  config.yaml         Embedding model, chunking, RRF, reranker, freshness
  gold-queries.yaml   Test queries with expected file hits
  requirements.txt    sentence-transformers, pyyaml, numpy
  README.md           Usage docs for all agents

~/.brain-index/                   (index data -- per-machine, NOT in repo)
  chunks.jsonl        Text chunks + frontmatter metadata
  vectors.npy         float16 embedding vectors (768-dim)
  meta.json           Build metadata
  manifest.json       File hash manifest for change detection
  heartbeat.json      Freshness metadata (built_at_head vs git HEAD)
```

## Quick Start

```bash
# Clone brain, install deps, build index (once per machine)
git clone https://github.com/Suggi-Workstation/agentic-brain.git /tmp/brain
cd /tmp/brain/brain-index
pip install -r requirements.txt
python index.py --force

# Query
python query.py "antitrust risk in digital platforms" --top-k 20

# Check freshness
python query.py --check-freshness

# Run eval
python eval.py --verbose
```

## Build Workflow

### First build (once per machine)

```bash
python index.py --force
```

Downloads `unsloth/embeddinggemma-300m` (~314 MB, cached after first
run). First build is slow (~16-20 min for ~5,000 chunks on CPU,
single process); CPU staying saturated means it is working, not hung.
Incremental builds take seconds. A first build that takes 40+ min is
usually TWO processes fighting (see watcher-concurrency pitfall), not
a slow model.

### Incremental build (session start)

```bash
cd /tmp/brain && git pull
python brain-index/index.py
```

Only rebuilds changed/new files. Detects changes via file hash
manifest.

### Check only (no rebuild)

```bash
python brain-index/index.py --check
```

Reports whether index is current without embedding anything.

## Query Modes

```bash
# Hybrid (default) -- dense + BM25 + RRF fusion (rerank optional, off)
python query.py "your question" --top-k 20

# Vector-only (semantic)
python query.py "your question" --no-sparse

# Keyword-only (BM25)
python query.py "your question" --no-dense
```

Results show file path, domain, score, and snippet. Deduplicated by
file (one result per file, highest scoring chunk). When
`reranker.enabled` is true in config.yaml, the fused top-20 are
reranked by the in-process cross-encoder before output.

## Eval Gate

```bash
python eval.py              # Summary only
python eval.py --verbose    # Per-query results
```

Metrics: recall@20, MRR, nDCG@20. Run after every model or config
change and compare against the recorded baseline. Gold queries live
in `gold-queries.yaml`; add queries as the brain grows.

## Freshness

- `heartbeat.json` lives in `~/.brain-index/` (DATA_DIR), not the
  clone dir. `index.py` writes it; `query.py` reads it.
- `query.py --check-freshness` compares heartbeat `built_at_head`
  against live `git rev-parse HEAD`. STALE when they differ.
- Incremental rebuilds refresh the heartbeat to current HEAD even on
  tool-only commits (no content change), so freshness stays accurate.

## Per-Machine Index

- VPS agents share ONE index at `/srv/brain/index/` (hermes reaches
  it via the symlink `~/.brain-index`). On the VPS the WATCHER
  maintains it (cron, `/opt/repo-tools/repo-pull.sh`): it reindexes
  on content change in either direction (pulled OR pushed) and
  refreshes the heartbeat. Do NOT build or rebuild manually there
  except for model switches or corruption repair.
- Non-VPS agents (Link PC, Linkie laptop): build their own index at
  `~/.brain-index/` via the clone-discard pattern.
- Both built from the same brain repo, verified by the same eval gate.

## Technology

| Component | Choice |
|---|---|
| Embedding | `unsloth/embeddinggemma-300m` (768-dim, in-process, public mirror of google/embeddinggemma-300m) |
| Reranker | `BAAI/bge-reranker-base` (in-process CrossEncoder, config-gated, disabled by default) |
| Keyword | BM25 (inline implementation; k1=1.5, b=0.75) |
| Fusion | RRF (k=60) |
| Chunking | max 1500 chars, 200 overlap, heading-aware |
| Storage | JSONL + NPY files |

## Model Switch Procedure

1. Edit `config.yaml`: `embedding.model`, `embedding.dim`, and the
   `reranker` block if needed.
2. Run `index.py --force` manually as hermes on the VPS (the watcher
   does NOT rebuild on config-only changes -- config.yaml is in
   `exclude_patterns` and changes no indexed content).
3. Verify `meta.json` shows the new model + dim.
4. Run `eval.py` and compare against the pre-upgrade baseline.
5. Update every file that names the model, in one pass: brain repo
   (`config.yaml`, `brain-index/README.md`,
   `research/insights/brain-search-system.md`), and ALL agent skill
   copies (Link PC, Linkie laptop, Morpheus VPS) including frontmatter
   tags. Grep every copy with fixed strings; query-brain-vps and
   AGENTS.md are model-agnostic (no change needed).

## Pitfalls

- **Reindex means incremental.** `--force` is only for first build on
  a machine, model switches, or corruption repair (IndexError on
  query, `--check` inconsistency). Check freshness + one test query
  first; if healthy, run plain `index.py`.
- **Model switches need explicit `--force`.** Without it, the
  incremental path finds no content change and the index stays on the
  old model; a later content change embeds at the new dim and the
  concatenation raises a dimension-mismatch ValueError.
- **Watcher concurrency (VPS).** The watcher reindexes on ANY content
  change (pulled OR pushed). A manual `--force` that overlaps the
  watcher's own rebuild = TWO processes embedding the same chunks,
  each at half speed -- a 16-20 min build balloons past 40 min.
  `repo-pull.sh` has a pgrep guard (skips if another index.py is
  running), so overlap is prevented, but diagnose long builds as
  concurrency FIRST: `ps aux | grep index.py`. If two are running,
  kill both and start ONE clean `--force`. Note: the guard means a
  manual rebuild owns the index and the watcher defers to it.
- **eval.py must mirror the query pipeline.** eval.py imports
  `rerank` from query.py so the gate scores what agents actually get
  (post-rerank), not raw fusion. If query.py's pipeline changes,
  eval.py must follow or the gate silently measures a different
  system. When comparing eval runs, only compare same-set results:
  MRR across different gold-query sets is not apples-to-apples (a
  broader set covers harder queries and can look higher or lower for
  reasons unrelated to model quality).
- **Reranker economics: disable by default.** A cross-encoder
  reranker in a fresh-process-per-query architecture reloads the
  model EVERY query (+15-18s for bge-reranker-base on CPU; the
  embedder alone is ~2s). At brain scale (415 files, recall already
  100%, gold usually at rank 1-3 pre-rerank), eval showed NO
  measurable gain (100-set + reranker: MRR 0.817 / nDCG 0.863 vs
  50-set no reranker: 0.8185 / 0.8616). Keep `reranker.enabled:
  false`; only enable with a persistent serving process or a corpus
  where recall is genuinely weak. Model choice: bge-reranker-base
  (278M, 512 ctx, nDCG 0.699, ~92ms) fits 375-token chunks exactly;
  bge-reranker-v2-m3 (568M, 8192 ctx but fine-tuned at 1024) is
  overkill for our chunk size.
- **Model caching inside one process.** Cross-encoders load once per
  process via a module-level cache (`_RERANKER_CACHE` keyed by
  model+max_length); loading per call made a 100-query eval take
  13+ min. Same pattern applies to any heavy model: cache at module
  level, never instantiate per call.
- **Killing the SSH wrapper does NOT kill the remote python.** A
  backgrounded `ssh ... python index.py/eval.py` whose local session
  is killed leaves the remote process running and burning CPU (hit
  twice this arc: reindex double-run and eval orphan). After killing
  any background SSH job, verify with `ps aux | grep <script>` on the
  VPS and `pkill -f <script>` the remote python explicitly.
- **EmbeddingGemma is asymmetric.** Use `encode_query` /
  `encode_document`, not plain `encode`, or quality silently drops.
- **HF gating.** Before committing a pipeline to any HF model, probe:
  `curl -s -o /dev/null -w "%{http_code}" https://huggingface.co/api/models/<org>/<model>`
  -- 401/307 means gated/redirect; 200 means public. Prefer public
  mirrors (e.g. unsloth repacks) over gated originals. Verified
  sub-300M model comparison + decision data:
  `references/embedding-model-comparison.md`.
- **Reranker lives in query.py.** Config-gated stage 2
  (`reranker:` block in config.yaml), graceful fallback to fused
  results if it fails to load.
- **rank-bm25 incompatible with Python 3.14.** `query.py` implements
  BM25 inline (~60 lines, same IDF formula, k1/b params). No external
  keyword-search dependency.
- **HF Hub symlink warning on Windows.** Cosmetic. Suppress with
  `HF_HUB_DISABLE_SYMLINKS_WARNING=1`.
- **Stale index after brain push.** If another agent pushed new files
  after your last build, `--check-freshness` reports STALE. Run
  `git pull && python index.py` to catch up.
- **ENT-ID collision in queue.log.** Two agents can derive the same
  ENT-ID and both write it. The append-only design tolerates
  duplicates; scan for duplicate ENT-IDs at preflight logbook read.
- **First query is slow (model load).** `query.py` lazy-loads the
  embedder on first query (~2s warm-up); subsequent queries in the
  same process reuse it. `eval.py` loads once.
- **Don't commit generated files.** `heartbeat.json` and
  `eval-results.json` are gitignored.
- **Post-Hermes-update dependency breakage.** Hermes updates can
  downgrade `huggingface-hub`, breaking sentence-transformers load.
  Fix: `python -m pip install huggingface-hub -U`.
- **Gold query staleness.** When new files ship, check whether they
  should be added as additional gold files for existing queries (a
  query can have multiple valid gold files). Otherwise MRR decline is
  uninterpretable. When ADDING gold queries: verify each gold_file
  exists AND is non-empty (an empty file passes `os.path.exists` but
  has no chunks and can never be retrieved -- watchlist.md was a 0-byte
  gold target). Also verify file paths against the live repo before
  committing the set; guessed paths are wrong ~10% of the time.
- **Heartbeat count source.** `index.py` writes the heartbeat `count`
  field from `meta.json` (chunk count), never from the manifest file
  count. Preserve this when modifying index.py.

## Cross-Links

- `agentic-brain:research/insights/brain-search-system.md` -- finished-system blueprint
- `agentic-brain:research/proposals/brain-index-search-proposal.md` -- original proposal
- `agentic-brain:research/insights/stale-index-problem.md` -- staleness failure class
- `brain-write` skills -- artifact writing workflow
