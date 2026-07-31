---
name: query-brain
description: "Query the agentic-brain knowledge base with hybrid semantic + keyword search. Clones brain, checks index freshness, runs query, returns ranked results with scores and snippets. Use when asked to search, query or discover from the brain, find a brain artifact of any kind, check for prior or existing work, or discover what the brain contains."
user-invocable: true
disable-model-invocation: false
---

# Query-Brain -- Search the Agentic-Brain

## What This Skill Does

Searches the agentic-brain knowledge base using the brain-index hybrid
search tool (semantic vectors + BM25 keyword + RRF fusion). Returns
ranked file paths with relevance scores and text snippets. The agent
then reads the top results for deeper context.

## When to Invoke

- User asks a question that might be answered by brain content
  (governance, research, reflections, library topics, insights)
- Researching a topic before writing artifacts
- Looking up prior agent work (reflections, proposals, evaluations)
- Any query where `grep` alone is insufficient (conceptual questions
  that don't share keywords with the target content)

## Self-Check -- HARD GATE

- [ ] Brain cloned to /tmp/brain-pf (or reuse existing preflight clone) (PASS / HALT)
- [ ] Index freshness checked (--check-freshness returned OK) (PASS / HALT)
- [ ] Query executed with relevant terms (PASS / HALT)
- [ ] Top 3-5 results read for deep context (PASS / HALT)
- [ ] Clone discarded (unless shared with other preflight steps) (PASS / HALT)

## Procedure

### 1. Ensure brain clone exists

If a preflight brain clone already exists at /tmp/brain-pf (from
governance or brain-index freshness checks), reuse it. Otherwise:

```bash
cd /tmp && rm -rf brain-pf && git clone --depth 1 \
  "https://${GITHUB_TOKEN}@github.com/Suggi-Workstation/agentic-brain.git" brain-pf
```

### 2. Verify index freshness

```bash
cd /tmp/brain-pf
python brain-index/query.py --check-freshness
```

If STALE or NO INDEX: invoke `brain-index` skill to rebuild or
perform first-time setup. Then re-check freshness before proceeding.

### 3. Run the query

Query using any mode from the `brain-index` skill (hybrid, vector-only,
or keyword-only). Default: `python brain-index/query.py "<query>" --top-k 20`.

Results return file path, domain, title, relevance score, and a text snippet:

```
[1] research/insights/logbook.md [Research] -- logbook
    score: 0.0325
    The logbook is the shared append-only event log... (snippet)
[2] governance/system-constitution.md [Governance] -- system-constitution
    score: 0.0164
    This file is the highest-precedence document... (snippet)
```

### 4. Read top results

Use `read_file` on the top 3-5 results for full context. The snippet
in the query output is ~200 chars -- enough to decide relevance, not
enough for understanding.

### 5. Discard clone

```bash
cd /tmp && rm -rf brain-pf
```

Skip if the clone is shared with other session steps (preflight
governance check, logbook read, mid-session poll).

## Fallback

If brain-index is unavailable (missing dependencies, broken index):

```bash
grep -r "<search terms>" /tmp/brain-pf/ --include="*.md"
```

Keyword-only search on raw files. No semantic matching, no ranking.
Report the broken tooling to Suggi.

## Pitfalls

- **First query is slow (~2s).** The embedding model loads on first
  query. Subsequent queries in the same process reuse the loaded model.
- **Index must exist.** If `~/.brain-index/` does not exist, the query
  fails. Invoke `brain-index` skill to build it first.
- **Clone path collision.** If another process uses /tmp/brain-pf,
  use /tmp/brain-pf-query as a unique clone path.
- **Outdated results.** If another agent pushed new brain files since
  your last index build, the query returns stale results. The
  freshness check (step 2) catches this. Always check before querying.

## Related

- `brain-index` skill -- build and maintain the search index
- AGENTS.md Retrieval section -- the gate that invokes this skill
- `brain:research/insights/brain-search-system.md` -- full system blueprint
- `brain-index/README.md` -- tool usage documentation (query modes,
  eval gate, technology choices)
