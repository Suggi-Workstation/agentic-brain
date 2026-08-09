---
name: brain-index
description: "Build, evaluate, reindex, and maintain the agentic-brain, or brain, hybrid search index. Covers index.py (full + incremental), eval.py (recall@20, MRR, nDCG), gold queries, freshness heartbeat, index freshness, check freshness, and the eval-first build pattern."
user-invocable: true
disable-model-invocation: false
---

# Brain-Index -- Hybrid Search for the Agentic-Brain

The brain-index tool lives at `brain-index/` in the agentic-brain repo.
It provides hybrid dense+sparse search over all markdown files in the
shared knowledge base. This skill covers building, evaluating, reindexing,
and maintaining the index. For querying, see the query-brain skill.

## When to Invoke

- User says "reindex brain", "rebuild the brain index", or similar
- Preflight: brain-index freshness check (via preflight skill)
- Session-end: after pushing new brain content, rebuild so the next
  session starts fresh
- Mid-session: after other agents push new brain files, or when a
  query-brain search returns stale results
- Index corruption detected (counts mismatch between chunks and vectors)
- First-time setup on a new machine (--force build)

Do NOT invoke for querying the brain -- use the query-brain skill
for search. The query-brain skill will route back to brain-index
automatically when the index is stale.

## Self-Check -- HARD GATE

- [ ] Brain cloned to /tmp/brain-pf (or reuse existing clone) (PASS / HALT)
- [ ] Dependencies installed (sentence-transformers, pyyaml, numpy) (PASS / HALT)
- [ ] Index built or rebuilt successfully (PASS / HALT)
- [ ] Freshness verified (--check-freshness returned OK) (PASS / HALT)
- [ ] If corrupted (counts mismatch): --force rebuild validated (PASS / HALT)
- [ ] Clone discarded (unless shared with other preflight steps) (PASS / HALT)

## Architecture

```
agentic-brain/brain-index/          (tool code -- committed to repo)
  index.py            Build index: full (--force) or incremental
  query.py            Query: hybrid (dense+BM25+RRF), --no-dense, --no-sparse
  eval.py             Eval: recall@20, MRR, nDCG against gold queries
  config.yaml         Embedding model, chunking, RRF, freshness settings
  gold-queries.yaml   Test queries with expected file hits
  requirements.txt    sentence-transformers, pyyaml, numpy
  README.md           Usage docs for all agents

~/.brain-index/                   (index data -- per-machine, NOT in repo)
  chunks.jsonl        Text chunks + frontmatter metadata
  vectors.npy         float16 embedding vectors (384-dim)
  meta.json           Build metadata
  manifest.json       File hash manifest for change detection
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

Downloads `BAAI/bge-small-en-v1.5` (~130 MB, cached after first run).
Builds chunks from all brain files. Subsequent incremental builds take
seconds.

### Incremental build (session start)

```bash
cd /tmp/brain && git pull
python brain-index/index.py
```

Only rebuilds changed/new files. Detects changes via file hash
manifest. A session with a few new library topics takes seconds.

### Check only (no rebuild)

```bash
python brain-index/index.py --check
```

Reports whether index is current without embedding anything.

### Corrupted index (counts mismatch)

If queries fail with IndexError or results are empty, the chunks and
vectors may be out of sync -- cumulative corruption from repeated
incremental builds that concatenated mismatched old and new data.

```bash
python -c "
import json, numpy as np
with open('$HOME/.brain-index/meta.json') as f: m=json.load(f)
with open('$HOME/.brain-index/chunks.jsonl') as f: c=sum(1 for l in f if l.strip())
v=np.load('$HOME/.brain-index/vectors.npy').shape[0]
print(f'chunks={c} vectors={v} meta={m[\"count\"]}')
print('OK' if c==v==m['count'] else 'CORRUPTED -- run index.py --force')
"
```

If CORRUPTED:

```bash
python brain-index/index.py --force
```

Full rebuild from scratch. Guarantees chunks == vectors. Use only when
incremental builds produce errors -- this is the nuclear option.

## Query Modes

```bash
# Hybrid (default) -- dense + BM25 + RRF fusion
python query.py "your question" --top-k 20

# Vector-only (semantic)
python query.py "your question" --no-sparse

# Keyword-only (BM25)
python query.py "your question" --no-dense
```

Results show file path, domain, score, and snippet. Deduplicated
by file (one result per file, highest scoring chunk).

## Eval Gate

The eval gate prevents silent search quality regression:

```bash
python eval.py              # Summary only
python eval.py --verbose    # Per-query results
```

Metrics: recall@20 (did the gold file appear in top 20?), MRR
(mean reciprocal rank), nDCG@20 (normalized discounted cumulative
gain). Run `python eval.py` for current baseline against
`gold-queries.yaml`.

Gold queries live in `gold-queries.yaml`. Each entry: question,
expected file path, domain. Add queries as the brain grows.

## Freshness

- `heartbeat.json` lives in `~/.brain-index/` (NOT the clone dir).
  The clone dir version was gitignored and lost on fresh clone.
  Fixed: `index.py` writes to DATA_DIR, `query.py` reads
  from DATA_DIR. Verify: `ls ~/.brain-index/heartbeat.json`.
- `query.py --check-freshness` compares heartbeat `built_at_head`
  against live `git rev-parse HEAD`. STALE when they differ.
- Incremental rebuilds update the heartbeat automatically. Even
  when no content files changed (tool-only commits), `index.py`
  refreshes the heartbeat to current HEAD so --check-freshness
  stays accurate.
- Stale index = visible warning. Agents surface this to their
  operator. The index is never silently stale.

## Preflight Integration

The brain-index freshness check shares the brain clone at `/tmp/brain-pf`
with governance verification and logbook read. The clone persists across
these checks -- do NOT clone the brain separately for each one.

1. Governance confirmed -- clone brain to /tmp/brain-pf, verify all
   governance templates present and non-empty
2. **Brain-index freshness** -- in same clone: invoke this skill to
   check freshness. If STALE: incremental rebuild.
3. Logbook queue -- in same clone: read queue.log + errors.log
4. GitHub auth -- discard /tmp/brain-pf clone

Read-proof line includes brain-index status:
`brain-index: OK (N chunks)` or `brain-index: OK (N chunks, rebuilt)`.

## Session-end Integration

After pushing brain files at session-end, the local brain-index is
stale. Invoke this skill to rebuild the index so the next session
starts fresh. See AGENTS.md Session-End section for the exact item.

The session-end + preflight pair provides defense-in-depth:

- **Session-end:** rebuild after pushing brain files (offline indexing).
  Triggered when session-end brain push produces new content.
- **Preflight:** verify freshness, rebuild if another agent pushed
  between sessions (online verification). Runs unconditionally.

Two gates at two time points. A corruption that escapes one is caught
by the other. See `research/insights/stale-index-problem.md` for the
failure class this pattern prevents.

## Technology

| Component | Choice | Why |
|---|---|---|
| Embedding | `BAAI/bge-small-en-v1.5` (384-dim) | Proven at scale in the archive prototype; zero API cost; CPU-only |
| Keyword | BM25 (inline implementation) | No external dependency; k1=1.5, b=0.75 |
| Fusion | RRF (k=60) | Balances semantic + keyword signals |
| Chunking | max 1500 chars, 200 overlap | Heading-aware paragraph splitting |
| Storage | JSONL + NPY files | Portable, no database server |

## Per-Machine Index

- VPS agents (Ava, researcher-1/2, investor): share ONE index at
  `~/.brain-index/` (same filesystem).
- Link (Hermes, Suggi's PC): builds own index at `~/.brain-index/`.
- Both built from same brain repo, verified by same eval gate.

## Pitfalls

- **rank-bm25 incompatible with Python 3.14.** The `rank-bm25` package
  fails to install on Python 3.14. `query.py` implements BM25 inline
  (~60 lines) with the same IDF formula and k1/b parameters. No
  external keyword-search dependency. See: `references/bm25-inline.md`.

- **FutureWarning: get_sentence_embedding_dimension.** Sentence-
  transformers 3.x renamed this to `get_embedding_dimension`. The
  warning is cosmetic; `index.py` catches it silently. Fix by
  updating the method name in a future patch.

- **HF Hub symlink warning on Windows.** Windows without Developer
  Mode cannot create symlinks in the HF cache. The warning is
  cosmetic; the model downloads and works correctly (non-symlink
  copy mode). Suppress with `HF_HUB_DISABLE_SYMLINKS_WARNING=1`.

- **Stale index after brain push.** If another agent pushes new files
  after your last index build, `query.py --check-freshness` will
  report STALE. Run `git pull && python index.py` to catch up.
  Incremental rebuild handles this in seconds for a few new files.

- **Heartbeat desync on tool-only commits.** When git commits only
  change brain-index/*.py (not markdown content), the incremental
  rebuild detects no content changes. Fixed: `index.py`
  now refreshes heartbeat.json to current HEAD even when zero
  content files changed. No action needed -- this is automatic.

- **ENT-ID collision in queue.log.** Two agents reading the same
  last-seen state can derive the same ENT-ID and both write it.
  The append-only design tolerates duplicates but numbering is
  corrupted. At preflight logbook read, scan for duplicate ENT-IDs
  and note them. See `logbook` skill for full mitigation.

- **First query is slow (model load).** `query.py` lazy-loads the
  embedding model on first query (~2s warm-up). Subsequent queries
  in the same process reuse the loaded model. For batch eval,
  `eval.py` loads once and reuses.

- **Don't commit generated files.** `heartbeat.json` and
  `eval-results.json` are gitignored. Generated, not source. CI
  would fail on non-ASCII content anyway.

## Cross-Links

- `agentic-brain:research/insights/brain-search-system.md` -- complete
  finished-system blueprint
- `agentic-brain:research/proposals/brain-index-search-proposal.md` --
  original proposal (v2, all open questions resolved)
- `agentic-brain:research/insights/stale-index-problem.md` -- failure
  class this system structurally prevents
- `suggi-workstation` skill -- brain contribution workflow
- Archive: `Suggi-Workstation/archive` > `hub-brain - github repo -
  20.06.26/brain/_index/` -- proven prototype at scale (24,592 chunks)
