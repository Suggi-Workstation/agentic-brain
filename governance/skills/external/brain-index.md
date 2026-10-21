---
name: brain-index
description: "Build, query, eval, and maintain your own agentic-brain hybrid search index. Covers index.py (full + incremental), query.py (dense + BM25 + RRF, optional rerank), eval.py (recall@20, MRR, nDCG), gold queries, freshness heartbeat."
user-invocable: true
disable-model-invocation: false
---

# Brain-Index -- Hybrid Search for the Agentic-Brain

The brain-index tool lives at `brain-index/` in the agentic-brain repo.
It provides hybrid dense+sparse search over all markdown files in the
shared knowledge base. You build and keep your own index on your own
machine from a clone of the brain; the org's server keeps its own.

This is the external copy for agents outside the org's server. Daily
searching follows `agentic-brain:governance/skills/external/query-brain.md`.

## Architecture

```
agentic-brain/brain-index/          (tool code -- committed to repo)
  index.py            Build index: full (--force) or incremental
  query.py            Query: hybrid (dense+BM25+RRF; optional rerank), --no-dense, --no-sparse
  eval.py             Eval: recall@20, MRR, nDCG against gold queries
  config.yaml         Embedding model, chunking, RRF, reranker, data path
  gold-queries.yaml   Test queries with one or more relevant files
  self-test.py        Package contract and regression tests
  requirements.txt    sentence-transformers, pyyaml, numpy
  README.md           Engine and evaluation commands

~/.brain-index/                   (index data -- per machine, NOT in repo)
  chunks.jsonl        Text chunks + frontmatter metadata
  vectors.npy         float16 embedding vectors (768-dim)
  meta.json           Build metadata
  manifest.json       File hash manifest for change detection
  heartbeat.json      Freshness metadata (built_at_head vs git HEAD)
```

## Quick Start

Keep one read-only clone for searching (`<brain-clone>`, for example
`~/agentic-brain`); the index records which commit it was built from.

```bash
# Clone the brain, install deps, build the index (once per machine)
git clone https://github.com/Suggi-Workstation/agentic-brain.git <brain-clone>
cd <brain-clone>
pip install -r brain-index/requirements.txt
python brain-index/index.py --force

# Query
python brain-index/query.py "antitrust risk in digital platforms" --top-k 20

# Check freshness
python brain-index/query.py --check-freshness

# Run eval
python brain-index/eval.py --validate-only
python brain-index/eval.py --verbose
```

## Build Workflow

### First build (once per machine)

```bash
python brain-index/index.py --force
```

Downloads `unsloth/embeddinggemma-300m` on first run (cached afterwards)
and embeds every chunk on CPU. The first build takes as long as it needs;
a saturated CPU means it is working, not hung. Run one build at a time.

### Incremental build (after each pull)

```bash
cd <brain-clone> && git pull --ff-only
python brain-index/index.py
```

Only re-embeds changed or new files, detected through the file hash
manifest, and refreshes the heartbeat to the current commit.

### Check only (no rebuild)

```bash
python brain-index/index.py --check
```

Reports whether the index is current without embedding anything.

## Query Modes

```bash
# Hybrid (default) -- dense + BM25 + RRF fusion (rerank optional, off)
python brain-index/query.py "your question" --top-k 20

# Vector-only (semantic)
python brain-index/query.py "your question" --no-sparse

# Keyword-only (BM25)
python brain-index/query.py "your question" --no-dense
```

Results show file path, domain, score, and snippet. Deduplicated by
file (one result per file, highest scoring chunk). When
`reranker.enabled` is true in config.yaml, the fused results are
reranked by the in-process cross-encoder before output.

## Embedding Service

`index.py` and `query.py` first try a local embedding service at
`http://127.0.0.1:8099/embed` (`index.py` honours `BRAIN_EMBED_URL`); the
org's server runs one to keep the model loaded. Without a service they
load the model in-process, which is the normal case on your machine.

## Eval Gate

```bash
python brain-index/eval.py --validate-only  # Schema, path, existence, index membership
python brain-index/eval.py                  # Summary only
python brain-index/eval.py --verbose        # Per-query results
python brain-index/self-test.py             # Package contract and regressions
```

Metrics: recall@20, MRR, nDCG@20. Run after every model or config
change and compare against your previous run on the same gold set.
Gold queries live in `gold-queries.yaml`; each uses `gold_files`
because several files may be relevant to one question. Validation
fails before scoring when a target is unsafe, missing, empty, or absent
from the index.

## Freshness

- `heartbeat.json` lives in `~/.brain-index/`, not the clone. `index.py`
  writes it; `query.py` reads it.
- `query.py --check-freshness` compares heartbeat `built_at_head`
  against the clone's `git rev-parse HEAD`. It also checks required
  index files, heartbeat/metadata counts, and live Markdown hashes
  against `manifest.json`. Any mismatch is STALE or UNVERIFIED.
- Incremental builds refresh the heartbeat to current HEAD even on
  tool-only commits (no content change), so freshness stays accurate.

## Technology

| Component | Choice |
|---|---|
| Embedding | `unsloth/embeddinggemma-300m` (768-dim, public mirror of google/embeddinggemma-300m) |
| Reranker | `BAAI/bge-reranker-base` (in-process CrossEncoder, config-gated, disabled by default) |
| Keyword | BM25 (inline implementation; k1=1.5, b=0.75) |
| Fusion | RRF (k=60) |
| Chunking | paragraphs up to 1500 chars; 200-char overlap for oversized paragraphs |
| Storage | JSONL + NPY files |

## Model Switch

1. Edit `config.yaml` in your clone: `embedding.model`, `embedding.dim`,
   and the `reranker` block if needed.
2. Run `python brain-index/index.py --force`. The incremental path does
   not rebuild on a config-only change.
3. Verify `meta.json` shows the new model and dim.
4. Run `eval.py` and compare against your run before the switch.

A local config change makes your clone differ from the org's; revert it
before pulling, or keep it on a branch.

## Pitfalls

- **Reindex means incremental.** `--force` is only for the first build,
  model switches, or corruption repair (IndexError on query, `--check`
  inconsistency). Check freshness and one test query first; if healthy,
  run plain `index.py`.
- **Model switches need explicit `--force`.** Without it, the
  incremental path finds no content change and the index stays on the
  old model; a later content change embeds at the new dim and the
  concatenation raises a dimension-mismatch ValueError.
- **One build at a time.** Two `index.py` processes embed the same
  chunks at half speed each. Check with `ps aux | grep index.py`; if two
  run, stop both and start one.
- **Keep the reranker off.** A fresh process per query reloads the
  cross-encoder on every query; it showed no measurable retrieval gain
  on the gold set. Enable it only with a persistent serving process.
- **EmbeddingGemma is asymmetric.** The tool uses `encode_query` /
  `encode_document`; plain `encode` silently lowers quality.
- **HF gating.** Before switching to any HF model, probe
  `curl -s -o /dev/null -w "%{http_code}" https://huggingface.co/api/models/<org>/<model>`
  -- 401/307 means gated or redirected; 200 means public.
- **Dependency drift.** A `huggingface-hub` downgrade can break
  sentence-transformers loading. Fix: `python -m pip install huggingface-hub -U`.
- **HF Hub symlink warning on Windows.** Cosmetic. Suppress with
  `HF_HUB_DISABLE_SYMLINKS_WARNING=1`.
- **Don't commit generated files.** Index data lives outside the repo;
  `heartbeat.json` and `eval-results.json` are gitignored.

## Cross-Links

- `agentic-brain:governance/skills/external/query-brain.md` -- daily search procedure
- `agentic-brain:brain-index/README.md` -- engine and evaluation commands
- `agentic-brain:research/insights/brain-search-system.md` -- finished-system blueprint
- `agentic-brain:research/insights/stale-index-problem.md` -- staleness failure class
