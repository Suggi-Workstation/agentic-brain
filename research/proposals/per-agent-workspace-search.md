---
name: per-agent-workspace-search
id: 20260819T100332Z
tier: proposal
author: Morpheus
tags: [workspace-search, semantic-search, hybrid-search, brain-index, agent-architecture, local-index, embed-daemon]
links:
  - research/insights/brain-search-system.md
  - research/insights/vps-brainclone-plus-index.md
  - research/proposals/brain-index-search-proposal.md
---

# Per-Agent Workspace Folder Search -- Semantic Search for Local Workspace Folders

## Problem

Morpheus and Neo each carry workspace folders that hold personal
knowledge not indexed anywhere: Morpheus has `memory/` (3 files, dated
snapshots) and `identity/` (2 files, versioned evolution log); Neo has
`knowledge/` (1 file, growing). These folders are NOT bootstrapped at
session start (only SOUL.md and AGENTS.md auto-load), NOT in the brain
index (which covers `/srv/brain/agentic-brain` only), and NOT in
Mnemosyne (which stores recalled facts via explicit writes, not folder
files). The only search path today is `search_files` (ripgrep keyword
match) + `read_file` -- no semantic layer, no ranking, no relevance
scoring.

At 5 total files this is adequate. At 20-50+ files (the trajectory for
both agents), ripgrep-only search breaks: it cannot match by meaning,
cannot rank by relevance, and cannot surface the right file when the
exact keyword is absent. This is the same problem the brain-index
solved for the agentic-brain repo (see
`research/insights/brain-search-system.md`), now replicated at a
smaller scale inside each agent's workspace.

A prior suggestion was to copy these folders into Mnemosyne so they
are "always present." That is architecturally wrong for three reasons:
(1) Mnemosyne is recall-on-demand (`mnemosyne_recall`), not
auto-injected at startup -- "always present" is a false expectation;
(2) Mnemosyne has no folder-watch, so a copy diverges on every edit
(the fossil/drift failure class already seen in brain-pull.log);
(3) the folder files are the canonical source -- a copy creates a
dual source-of-truth (violates R8/R9). The correct analog to OpenClaw's
`memory_search` is index-in-place, not copy-into-store.

## Proposed Solution

Build a lightweight per-agent workspace search system that reuses the
brain-index engine architecture, retargeted at each agent's specific
folders. Two independent deployments, one per agent, sharing zero state
but reusing the warm embed daemon.

### Architecture Overview

```
Morpheus:
  workspace-morpheus/scripts/workspace-search/
    index.py            (fork of brain index.py, parameterized)
    query.py            (byte-copy of brain query.py, config-driven)
    config.yaml         (per-agent: root + include_dirs + data_dir)
    index-data/         (generated: chunks.jsonl, vectors.npy, meta.json, heartbeat.json -- gitignored)

  skills/query-workspace-morpheus/SKILL.md   (thin loader skill)

Neo:
  workspace-neo/scripts/workspace-search/
    index.py            (identical fork)
    query.py            (identical byte-copy)
    config.yaml         (per-agent: root + include_dirs + data_dir)
    index-data/         (generated, gitignored)

  skills/query-workspace-neo/SKILL.md        (thin loader skill)
```

### Key Design Decisions

**1. Fork, not import.** The engine scripts (index.py, query.py) are
copied into each agent's `scripts/workspace-search/` folder. We do NOT
import from `/srv/brain/agentic-brain/brain-index/` because: (a) the
brain index.py is the brain's engine -- a local copy keeps workspace
search independent and lets it evolve separately; (b) the brain
scripts are not a library API, they are standalone CLIs; (c) each
agent's workspace is a separate git repo, so the engine should live
there for reviewability. The copies are plain files in the workspace
git repo, versioned alongside everything else.

**2. Per-agent skills, not one shared skill.** A single shared
`query-workspace` skill would have to switch on `--agent` to pick the
right index, which is fragile (a stray `--agent neo` in Morpheus's
session makes him read Neo's files -- scope violation R16). Skills are
loaded per-profile, so each agent carries only its own skill
hard-wired to its own engine + index data. No cross-contamination
possible.

**3. Reuse the warm embed daemon.** Both index.py and query.py already
hit `http://127.0.0.1:8099` (the `brain-embed.service` systemd unit,
model `unsloth/embeddinggemma-300m`, 768-dim). Confirmed alive: a POST
to `/embed` returns vectors in <1s. A second index costs ZERO new
model loads -- the daemon is shared runtime, not shared state. The
in-process fallback (sentence-transformers) remains as a safety net.

**4. Index-in-place, not copy-to-store.** The folders stay canonical
and git-tracked. The index is a derived cache rebuilt from source on
change. This is structurally the opposite of a Mnemosyne copy: the
next refresh tick re-reads the actual files, so drift is impossible by
construction.

### What Changes in index.py (the fork)

The brain's `index.py` hardcodes exactly one assumption:
`BRAIN_ROOT = SCRIPT_DIR.parent` (line 25) -- it assumes the script
lives one level inside the brain repo. To retarget:

**Change 1 -- parameterize the root.** Replace the hardcoded
`BRAIN_ROOT` with a config-driven value:

```python
# BEFORE (line 24-25):
SCRIPT_DIR = Path(__file__).resolve().parent
BRAIN_ROOT = SCRIPT_DIR.parent

# AFTER:
SCRIPT_DIR = Path(__file__).resolve().parent
BRAIN_ROOT = Path(os.path.expanduser(cfg["index"]["source_root"]))
```

**Change 2 -- add include_dirs whitelist.** The brain indexer walks
the entire root and excludes subdirs via `exclude_dirs`. For workspace
search we want the opposite: walk the root but ONLY enter listed
subdirs. Add a new config key `include_dirs` and filter in
`iter_markdown_files`:

```python
# In iter_markdown_files, after the exclude_dirs filter:
include_dirs = set(cfg["index"].get("include_dirs", []))
if include_dirs:
    dirnames[:] = [d for d in dirnames if d in include_dirs or _is_under_include(dirpath, root, include_dirs)]
```

A simpler approach: if `include_dirs` is set, iterate only those
subdirectories directly instead of walking the whole root. This avoids
the walk-complexity:

```python
def iter_markdown_files(root, exclude_dirs, exclude_exts, include_dirs=None):
    if include_dirs:
        targets = [root / d for d in include_dirs]
    else:
        targets = [root]
    for target in targets:
        for dirpath, dirnames, filenames in os.walk(target):
            dirnames[:] = [d for d in dirnames if d not in exclude_dirs]
            for fn in sorted(filenames):
                # ... same logic as existing
```

**Change 3 -- data_dir to local.** Already config-driven
(`cfg["index"]["data_dir"]`). Just set it in each agent's config.yaml
to point at `scripts/workspace-search/index-data`.

Everything else in index.py -- chunking, frontmatter parsing, hash-based
change detection (md5 manifest), daemon embed with in-process fallback,
vector normalization, heartbeat writing -- is reused verbatim. The
heartbeat's git-HEAD check (`built_at_head`) will work naturally since
each workspace is its own git repo.

### What Changes in query.py (the fork)

**Nothing.** query.py is already fully config-driven:
- It reads `config.yaml` from `SCRIPT_DIR` (line 24)
- It gets `DATA_DIR` from `cfg["index"]["data_dir"]` (line 27)
- It hits the daemon at the same URL (line 62)
- BM25, RRF, dense search, reranker -- all operate on loaded chunks/vectors

A byte-copy of query.py placed alongside the per-agent config.yaml
works without modification. The only thing that differs between agents
is the `config.yaml` it reads.

### Per-Agent config.yaml

Morpheus (`workspace-morpheus/scripts/workspace-search/config.yaml`):

```yaml
embedding:
  model: "unsloth/embeddinggemma-300m"
  dim: 768
  batch_size: 32
  device: "cpu"

chunking:
  max_chars: 1500
  overlap_chars: 200
  heading_aware: true

bm25:
  k1: 1.5
  b: 0.75

rrf:
  k: 60

search:
  top_k: 20
  snippet_chars: 300

index:
  source_root: "/home/hermes/.hermes/profiles/morpheus/workspace-morpheus"
  data_dir: "scripts/workspace-search/index-data"
  include_dirs:
    - "memory"
    - "identity"
  exclude_dirs:
    - ".git"
    - ".githooks"
  exclude_patterns:
    - "*.json"
    - "*.yaml"
    - "*.yml"

freshness:
  warn_hours: 24
```

Neo (`workspace-neo/scripts/workspace-search/config.yaml`):

```yaml
# identical except:
index:
  source_root: "/home/hermes/.hermes/profiles/neo/workspace-neo"
  data_dir: "scripts/workspace-search/index-data"
  include_dirs:
    - "knowledge"
  exclude_dirs:
    - ".git"
    - ".githooks"
  exclude_patterns:
    - "*.json"
    - "*.yaml"
    - "*.yml"
```

### The Skill (per agent)

Each skill is a thin Hermes skill that:

1. Checks freshness: `python scripts/workspace-search/index.py --check`
2. If stale: runs incremental build `python scripts/workspace-search/index.py`
3. Queries: `python scripts/workspace-search/query.py "<question>" --top-k 20`
4. Reads the top 3-5 result files with `read_file`, cites paths

The skill instructs the agent to call this before falling back to
`search_files` (ripgrep) when the folder has 10+ files. At current file
counts (5 and 1), `search_files` remains adequate and the skill is
optional -- it becomes mandatory as folders grow.

### Refresh Trigger

A per-agent cron job (Hermes cron) runs the incremental build every 15
minutes. The build is hash-based (md5 manifest): unchanged files cost
nothing (sub-second). This mirrors the brain watcher pattern but is
simpler because each agent's index is private -- no shared-state
divergence problem.

Alternatively, a git post-commit hook in each workspace could trigger a
rebuild on any `.md` change in the target folders. This is
event-driven (faster) but couples the index to the commit flow. The
cron approach is recommended first (simpler, decoupled); the hook can
be added later if latency matters.

### What Does NOT Change

- `/srv/brain/agentic-brain/brain-index/index.py` -- untouched
- `/srv/brain/agentic-brain/brain-index/query.py` -- untouched
- `/srv/brain/agentic-brain/brain-index/config.yaml` -- untouched
- The `query-brain-vps` skill -- untouched
- The `brain-embed.service` systemd unit -- untouched (shared runtime)
- Each agent's `AGENTS.md` Retrieval section -- updated only after the
  system is built and tested (separate proposal or direct edit with
  Suggi approval)

### Build Order (for Link)

1. Fork `index.py` into `workspace-morpheus/scripts/workspace-search/`,
   apply the 2 changes (parameterize root, add include_dirs).
2. Copy `query.py` byte-for-byte into the same folder.
3. Write `config.yaml` for Morpheus (template above).
4. Write `config.yaml` for Neo (template above, different root/include).
5. Copy the same forked `index.py` + byte-copy `query.py` into
   `workspace-neo/scripts/workspace-search/`.
6. First build: `python index.py --force` in each workspace.
7. Test query: `python query.py "what did I learn about scars" --top-k 5`.
8. Write the two skills (`query-workspace-morpheus`,
   `query-workspace-neo`).
9. Add `.gitignore` entry for `scripts/workspace-search/index-data/`
   in each workspace.
10. Set up the cron refresh job per agent.

## Impact

**Positive:**
- Semantic search over personal workspace folders -- find by meaning,
  not just keyword match. Scales to 50+ files without degradation.
- Zero new model load: reuses the warm embed daemon already running.
- Folder stays canonical (git-tracked, single source of truth); index
  is a derived cache that cannot drift.
- Per-agent isolation: no cross-contamination between Morpheus's
  memory/identity and Neo's knowledge.
- The engine is a proven architecture (brain-index runs 5,348 chunks
  in production); we are retargeting, not inventing.

**Risk:**
- Low. The engine is a fork of working code with 2 small changes.
- Blast radius: each agent's workspace only. No brain repo changes.
  No shared infrastructure changes (daemon is read-only shared).
- Rollback: delete the `scripts/workspace-search/` folder + the skill
  + the cron job. The folders themselves are untouched. Zero data loss
  risk -- the index is always rebuildable from source files.

**Cost:**
- ~2-3 hours for Link to fork, parameterize, test both deployments,
  write the two skills, set up crons.
- ~0 ongoing token cost: the cron is a no-agent script run (like
  mnemosyne-sync). Queries are on-demand (agent invokes the skill).
- Disk: ~1-5 MB per agent for index-data (vectors + chunks), trivial.

## Open Questions

1. Should the workspace `AGENTS.md` Retrieval section be updated to
   document this new search path? (Recommend: yes, but as a separate
   edit after the system is built and tested -- not in this proposal.)
2. Should the skill instruct the agent to auto-refresh the index before
   every query, or trust the cron to keep it fresh? (Recommend: trust
   the cron; the skill checks freshness and warns if stale, but does
   not block on a rebuild -- the agent can query a slightly stale index
   safely since it re-reads the actual files for snippets.)
3. Cron cadence: every 15 minutes, or every 5? At current file counts
   (5 and 1), 15 min is more than sufficient. Revisit when folders
   exceed 50 files.
4. Should Neo's `knowledge/` folder eventually include other workspace
   files (e.g. `LEARNINGS.md`, `FRAMEWORKS.md`) in the index? (Recommend:
   start with `knowledge/` only per Suggi's original instruction;
   expand later if needed.)
5. Is the `query.py` byte-copy acceptable, or should we refactor
   `query.py` to accept a `--config` path argument so a single shared
   copy could serve both agents? (Recommend: byte-copy for now --
   per-agent independence is worth the duplication; the file is 345
   lines and rarely changes.)

## Approval Gate

If approved, Link will build the system per the build order above.
Morpheus does not build this (it is Link's domain as the brain-index
builder). The proposal author requests Suggi approval before Link
begins implementation.

## Cross-Links

- `research/insights/brain-search-system.md` -- the blueprint that
  defines the brain-index architecture we are reusing
- `research/insights/vps-brainclone-plus-index.md` -- VPS-native
  brain clone + index design (the same machine, same daemon)
- `research/proposals/brain-index-search-proposal.md` -- Link's
  original brain-index proposal (the system this forks from)