---
name: query-forge-vps
description: "Use when searching the shared agentic-forge index on the VPS."
user-invocable: true
disable-model-invocation: false
---

# Query-Forge-VPS -- Search the Agentic-Forge

## Purpose

Searches `agentic-forge` with the watcher-maintained VPS index. The engine runs
EmbeddingGemma semantic search and BM25 keyword search in parallel, combines
them with Reciprocal Rank Fusion (RRF), and returns one ranked result per file.
The agent reads the best files for full context.

Gold questions are an offline quality test. They never influence live ranking.

## Use When

- The answer may exist in protocol, ideas, proposals, research, evaluations, builds, and verifications.
- Conceptual retrieval is needed because exact keyword search is insufficient.
- Prior repository work must be checked before writing or deciding.

## Paths

| Item | Path |
|:--|:--|
| Repository | `/srv/forge/agentic-forge` |
| Search tool | `forge-index/` |
| Index data | `~/.forge-index` (`/srv/forge/index`) |
| Index log | `/srv/forge/logs/forge-index.log` |

Run repository commands as `hermes`, never root. VPS-connected agents use their
own established key door to run the same commands; this skill does not duplicate
connection details or credentials.

## Procedure

### 1. Verify watcher ownership

Run `crontab -l` and confirm the exact `agentic-forge` watcher line is present.
Do not run the watcher or rebuild the index during a normal query.

PASS: watcher line present. HALT: missing line.

### 2. Verify freshness

```bash
cd /srv/forge/agentic-forge
/opt/repo-tools/venv/bin/python forge-index/query.py --check-freshness
```

PASS: exit code 0 and output begins `OK --`. HALT: nonzero, `STALE`,
`NO INDEX`, or `UNVERIFIED`; inspect `/srv/forge/logs/forge-index.log` and report the fault.
Never hide a freshness failure by rebuilding first.

### 3. Query

```bash
cd /srv/forge/agentic-forge
/opt/repo-tools/venv/bin/python forge-index/query.py "<question>" --top-k 20
```

Use the default hybrid mode. Use `--no-dense` or `--no-sparse` only for a
specific diagnostic comparison, not routine retrieval.

PASS: ranked repository paths and snippets returned. HALT: command failure.

### 4. Read results

Read the top 3-5 relevant files from `/srv/forge/agentic-forge/<returned-path>`. Snippets
select candidates; they are not enough for understanding or citation.

PASS: full files read before using their claims. HALT: conclusions drawn from
snippets alone.

### 5. Cite and stop

Cite exact repository-relative paths. A read-only query makes no repository,
index, config, or runtime changes.

## Same-Repository Fallback

If the index tool is unavailable but the repository is readable, use
`search_files` against `/srv/forge/agentic-forge` with an appropriate Markdown filter, then
read the matching files. This is keyword-only and has no semantic ranking.

If the repository itself is unavailable, HALT and report it. Never substitute
another repository's query skill; that silently searches the wrong corpus.

## Evaluation and Maintenance

These commands are maintenance gates, not part of each query:

```bash
cd /srv/forge/agentic-forge
/opt/repo-tools/venv/bin/python forge-index/index.py --check
/opt/repo-tools/venv/bin/python forge-index/eval.py --validate-only
/opt/repo-tools/venv/bin/python forge-index/eval.py --verbose
/opt/repo-tools/venv/bin/python forge-index/self-test.py
```

Run evaluation after model, chunking, fusion, or ranking changes and when the
corpus grows materially. Relevance judgments may name multiple `gold_files`.

## Hard Gate

- [ ] Watcher line present (PASS / HALT)
- [ ] Freshness command returned exit 0 and literal `OK --` (PASS / HALT)
- [ ] Query returned ranked paths from `agentic-forge` (PASS / HALT)
- [ ] Top 3-5 relevant files read in full (PASS / HALT)
- [ ] No manual rebuild or write occurred during retrieval (PASS / HALT)

## Pitfalls

- `STALE` is a watcher/index problem, not permission to rebuild manually.
- Root lacks the hermes user's index symlink and can report a false `NO INDEX`.
- Gold questions test retrieval after ranking; they are not query expansion,
  training data, or a runtime answer key.
- The shared `brain-embed.service` name is historical; it serves all three
  repository indexes.
- A snippet is candidate evidence, never the complete source.

## Related

- `forge-index/README.md` -- engine and evaluation commands
- `agentic-brain:research/insights/brain-search-system.md` -- retrieval design
- `agentic-brain:research/insights/vps-brainclone-plus-index.md` -- watcher design
