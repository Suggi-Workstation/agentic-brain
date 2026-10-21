---
name: query-brain
description: "Use when searching the agentic-brain with your own brain-index, outside the org's server."
user-invocable: true
disable-model-invocation: false
---

# Query-Brain -- Search the Agentic-Brain

## Purpose

Searches `agentic-brain` with a brain-index you build and keep on your own
machine. The engine runs EmbeddingGemma semantic search and BM25 keyword
search in parallel, combines them with Reciprocal Rank Fusion (RRF), and
returns one ranked result per file. The agent reads the best files for full
context.

Gold questions are an offline quality test. They never influence live ranking.

This is the external copy for agents outside the org's server. Org agents on
the server use `agentic-brain:governance/skills/query-brain-vps.md`.

## Use When

- The answer may exist in governance, Library topics, research, and reflections.
- Conceptual retrieval is needed because exact keyword search is insufficient.
- Prior repository work must be checked before writing or deciding.

## Paths

| Item | Path |
|:--|:--|
| Repository | your read-only clone of `Suggi-Workstation/agentic-brain` (`<brain-clone>`) |
| Search tool | `<brain-clone>/brain-index/` |
| Index data | `~/.brain-index` (outside git) |

Keep one clone for searching; the index records which commit it was built
from. First-time setup and index builds: `brain-index` skill.

## Procedure

### 1. Update the clone

```bash
cd <brain-clone>
git pull --ff-only
```

PASS: fast-forward or already up to date. HALT: any other result; never edit
or commit in the search clone.

### 2. Verify freshness

```bash
python brain-index/query.py --check-freshness
```

PASS: exit code 0 and output begins `OK --`. On `STALE` after a pull, run the
incremental build (`python brain-index/index.py`) and check again. On
`NO INDEX`, build the index first (`brain-index` skill). HALT on `UNVERIFIED`
or a failed build; never query a stale index.

### 3. Query

```bash
python brain-index/query.py "<question>" --top-k 20
```

Use the default hybrid mode. Use `--no-dense` or `--no-sparse` only for a
specific diagnostic comparison, not routine retrieval.

PASS: ranked repository paths and snippets returned. HALT: command failure.

### 4. Read results

Read the top 3-5 relevant files from `<brain-clone>/<returned-path>`. Snippets
select candidates; they are not enough for understanding or citation.

PASS: full files read before using their claims. HALT: conclusions drawn from
snippets alone.

### 5. Cite and stop

Cite exact repository-relative paths. A query changes nothing in the
repository.

## Same-Repository Fallback

If the index tool is unavailable but the clone is readable, search the clone's
Markdown files by keyword, then read the matching files:

```bash
grep -rn --include='*.md' "<search terms>" <brain-clone>
```

This is keyword-only and has no semantic ranking. If the clone itself is
unavailable, read the files on GitHub. Never substitute another repository's
search; that silently searches the wrong corpus.

## Hard Gate

- [ ] Clone updated by fast-forward; nothing edited or committed in it (PASS / HALT)
- [ ] Freshness command returned exit 0 and literal `OK --` (PASS / HALT)
- [ ] Query returned ranked paths from `agentic-brain` (PASS / HALT)
- [ ] Top 3-5 relevant files read in full (PASS / HALT)

## Pitfalls

- The first query in a process loads the embedding model, so it is slower
  than the rest. The tool first tries a local embedding service on
  `127.0.0.1:8099` (the org's server runs one); without one it loads the model
  in-process, which is normal on your machine.
- `STALE` right after `git pull` is expected: the index was built from an older
  commit. The incremental build catches it up.
- Gold questions test retrieval after ranking; they are not query expansion,
  training data, or a runtime answer key.
- A snippet is candidate evidence, never the complete source.

## Related

- `agentic-brain:governance/skills/external/brain-index.md` -- build and maintain your index
- `agentic-brain:brain-index/README.md` -- engine and evaluation commands
- `agentic-brain:research/insights/brain-search-system.md` -- retrieval design
