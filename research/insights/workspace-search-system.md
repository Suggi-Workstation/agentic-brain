---
name: workspace-search-system
id: 20260819T102238Z
tier: insight
source:
  - 20260819T100332Z
  - 20260817T123124Z
  - 20260810T112709Z
author: Link
tags: [workspace-search, semantic-search, brain-index, agent-architecture, per-agent, cron, embeddings]
links:
  - research/proposals/per-agent-workspace-search.md
  - research/insights/brain-search-system.md
  - research/insights/mnemosyne-system.md
  - research/insights/two-tier-fleet-memory-single-vector-space.md
---

# Per-Agent Workspace Search -- Semantic Search Inside Agent Workspaces

## The Insight

The brain-index architecture (hybrid dense + BM25 + RRF search over
markdown files) is a retargetable engine, not a brain-specific one:
fork it with two small changes, point it at any folder of markdown
files, and the same warm embed daemon that serves the brain serves
per-agent workspace search for zero additional model cost.

## Evidence

### 1. Problem

Morpheus and Neo each carry workspace folders with personal knowledge
not indexed anywhere: Morpheus has `memory/` (dated session snapshots)
and `identity/` (versioned evolution log); Neo has `knowledge/` (growing
knowledge files). These folders are not bootstrapped at session start,
not in the brain index (which covers `/srv/brain/agentic-brain` only),
and not in Mnemosyne (which stores recalled facts via explicit writes,
not folder files). The only search path was `search_files` (ripgrep
keyword match) -- no semantic layer, no ranking, no relevance scoring.

### 2. Solution: fork the brain-index engine

The brain-index engine (`index.py` + `query.py` + `config.yaml`) was
forked into each agent's workspace. Two changes to `index.py`, zero
changes to `query.py`:

**Change 1 -- parameterize the root.** The brain's `index.py` hardcodes
`BRAIN_ROOT = SCRIPT_DIR.parent` (assumes the script lives one level
inside the brain repo). Replaced with:
`BRAIN_ROOT = Path(os.path.expanduser(cfg["index"]["source_root"]))`
-- now config-driven, each agent points at its own workspace.

**Change 2 -- add include_dirs whitelist.** The brain indexer walks the
entire root and excludes subdirs. For workspace search we want the
opposite: only walk listed subdirs. Added an `include_dirs` config key;
when set, `iter_markdown_files` walks only those subdirs instead of the
whole root.

**Fix (discovered during build): relative data_dir resolution.** The
brain's `DATA_DIR = Path(os.path.expanduser(cfg["index"]["data_dir"]))`
resolves relative paths against CWD, not SCRIPT_DIR. In the brain this
works because `data_dir` is `~/.brain-index` (absolute). The workspace
configs use `"index-data"` (relative). Fix: resolve relative to
SCRIPT_DIR in both index.py and query.py.

**Fix (discovered during build): check_freshness git root.** The
brain's `query.py` uses `SCRIPT_DIR.parent` as the git root for HEAD
comparison. The workspace scripts live in `scripts/workspace-search/`,
so `SCRIPT_DIR.parent` is the workspace root (correct by accident), but
the explicit fix uses `cfg["index"]["source_root"]` for clarity.

### 3. Architecture (as built, verified 2026-08-19)

```
Morpheus (workspace-morpheus/):
  memory/                          3 .md files (session snapshots)
  identity/                        2 .md files (versioned evolution log)
  scripts/workspace-search/
    index.py                       fork (2 changes + 2 fixes)
    query.py                       byte-copy (with data_dir fix)
    config.yaml                    source_root + include_dirs=[memory, identity]
    index-data/                    GENERATED, gitignored
      chunks.jsonl                 18 chunks (20.9KB)
      vectors.npy                   18 x 768-dim float16 (27.8KB)
      meta.json                     build metadata (178B)
      manifest.json                 file hash manifest (419B)
      heartbeat.json                freshness marker (231B)
  scripts/workspace-search-refresh.py   cron script (5-min, no_agent)
  skills/brain-search/query-workspace-morpheus/SKILL.md

Neo (workspace-neo/):
  knowledge/                       1 .md file (knowledge guide)
  scripts/workspace-search/
    index.py                       same fork
    query.py                       same byte-copy
    config.yaml                    source_root + include_dirs=[knowledge]
    index-data/
      chunks.jsonl                 2 chunks (3.0KB)
      vectors.npy                   2 x 768-dim (3.2KB)
      meta.json, manifest.json, heartbeat.json
  scripts/workspace-search-refresh.py
  skills/brain-search/query-workspace-neo/SKILL.md
```

### 4. Shared infrastructure (zero new services)

The warm embed daemon (`brain-embed.service`, 127.0.0.1:8099,
`unsloth/embeddinggemma-300m`, 768-dim) is shared runtime -- multiple
indexes hitting it is fine (stateless HTTP, each request gets its own
embedding). The brain's index, the brain's query, and both workspace
indexes all use the same daemon. Zero new model loads, zero new RAM,
zero new systemd units.

### 5. Data flow

1. **Build**: `index.py` walks only the `include_dirs` subdirs, chunks
   each .md file (1500 chars, 200 overlap), embeds via the shared
   daemon, writes `index-data/` (chunks.jsonl + vectors.npy + meta.json
   + manifest.json + heartbeat.json).
2. **Query**: `query.py "<question>" --top-k 20` runs BM25 keyword search
   + dense vector cosine search + RRF fusion, returns ranked file paths
   with scores and text snippets. The agent reads the top 3-5 files
   for full context.
3. **Refresh**: a 5-min Hermes cron (no_agent Python script) runs
   `index.py --check`; if stale, runs incremental build. Hash-based
   (md5 manifest): unchanged files cost nothing (sub-second).
4. **Fallback**: if the daemon is down, `index.py` falls back to
   in-process sentence-transformers (~15s model load). Querying still
   works with existing vectors.

### 6. What does NOT change

- `/srv/brain/agentic-brain/brain-index/index.py` -- untouched
- `/srv/brain/agentic-brain/brain-index/query.py` -- untouched
- `/srv/brain/agentic-brain/brain-index/config.yaml` -- untouched
- The `query-brain-vps` skill -- untouched
- The `brain-embed.service` systemd unit -- untouched (shared runtime)
- Each agent's `AGENTS.md` -- unchanged (the skills are self-documenting)

### 7. Build results (2026-08-19)

| Agent | Files | Chunks | Build time | Index size |
|:--|:--|:--|:--|:--|
| Morpheus | 5 (3 memory + 2 identity) | 18 | 4.5s | 49.3KB |
| Neo | 1 (knowledge guide) | 2 | 0.5s | 6.6KB |

### 8. Test results (2026-08-19)

Morpheus query "what did I learn about scars" -> returned
identity/v1.1-first-earned-scars.md (score 0.0323) and
identity/v1.0-birth.md (score 0.0315) as top results.

Neo query "how to write knowledge files" -> returned
knowledge/knowledge-guide.md (score 0.0328) as top result.

Cron refresh scripts: both rc=0 (silent), logs show
"OK -- 18 chunks from 5 files" and "OK -- 2 chunks from 1 files".

## Implications

1. The brain-index engine is a general markdown search tool, not a
   brain-specific one. Any folder of markdown files can get the same
   hybrid search by forking index.py with the same 2 changes.
2. Per-agent isolation is by construction: each agent's index lives in
   its own workspace, reads only its own folders, and is queried by
   its own skill. No cross-contamination possible (R16).
3. The shared embed daemon scales to N indexes at zero marginal cost:
   the daemon is stateless HTTP, not shared state. Adding a third or
   fourth workspace index costs nothing but disk for the index-data.
4. Index-in-place (not copy-to-store) means the folders stay canonical
   and git-tracked. The index is a derived cache, always rebuildable
   from source. This is structurally the opposite of a Mnemosyne copy
   (which would drift on every edit).
5. The cron refresh is zero-token (no_agent script, like
   mnemosyne-sync). The skill is on-demand (agent invokes it only when
   searching). Total ongoing cost: ~0.

## Counter-evidence

This architecture would be invalidated if:

- The embed daemon could not handle concurrent requests from multiple
  indexes. Observed: it handles them fine (stateless HTTP, each request
  gets its own embedding, verified live with both indexes building
  simultaneously).
- The forked index.py diverged significantly from the brain's index.py,
  creating a maintenance burden. Observed: 2 changes + 2 fixes, 433
  lines reused verbatim. The fork is closer to a config retargeting
  than a code fork.
- Per-agent workspace folders were better served by Mnemosyne (recall-
  on-demand). Observed: Mnemosyne has no folder-watch (a copy diverges
  on every edit), is not auto-injected at startup, and creates a
  dual source-of-truth. The index-in-place approach is structurally
  superior for folder files.
- The 5-min cron cadence was too slow for freshness. Observed: at 5
  files, the incremental build is sub-second. At 50+ files it would
  still be under 10s. The cadence is sufficient.

## Cross-Links

- `research/proposals/per-agent-workspace-search.md` -- Morpheus's
  proposal (the design this implements)
- `research/insights/brain-search-system.md` -- the brain-index
  architecture this forks from
- `research/insights/mnemosyne-system.md` -- the memory system this
  complements (Mnemosyne = explicit writes, workspace search =
  folder files)
- `research/insights/two-tier-fleet-memory-single-vector-space.md` --
  the fleet memory architecture (this adds a third search tier:
  per-agent workspace, alongside brain and Mnemosyne)