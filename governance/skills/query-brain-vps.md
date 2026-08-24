---
name: query-brain-vps
description: "Query the shared agentic-brain index on the fleet VPS -- no cloning, watcher-maintained freshness. Use for all brain searches by any fleet agent."
user-invocable: true
disable-model-invocation: false
---

# Query-Brain-VPS -- Search the Agentic-Brain (Shared VPS Index)

## What This Skill Does

Searches the agentic-brain knowledge base using the brain-index hybrid
search tool (semantic vectors + BM25 keyword + RRF fusion) against the
SHARED index on the fleet VPS. Returns ranked file paths with relevance
scores and text snippets. The agent then reads the top results for
deeper context. No cloning, no local index, no manual rebuilds -- the
watcher keeps the live mirror and the index fresh automatically.

## When to Invoke

- User asks a question that might be answered by brain content
  (governance, research, reflections, library topics, insights)
- Researching a topic before writing artifacts
- Looking up prior agent work (reflections, proposals, evaluations)
- Any query where `grep` alone is insufficient (conceptual questions
  that don't share keywords with the target content)

## Self-Check -- HARD GATE

- [ ] Watcher healthy: cron line present + manual run exits 0
      (PASS / HALT)
- [ ] Index freshness checked (--check-freshness returned OK)
      (PASS / HALT)
- [ ] Query executed with relevant terms (PASS / HALT)
- [ ] Top 3-5 results read for deep context (PASS / HALT)
- [ ] No manual index rebuild performed (the watcher owns the index)
      (PASS / HALT)

## Procedure

### 1. Verify the watcher is healthy

The fleet depends on the watcher (cron every minute). If it stopped,
results are silently stale. Check before querying:

```bash
crontab -l | grep repo-pull
```

PASS: the cron line is present. The watcher logs are EVENT-DRIVEN:
brain-pull.log records pushes only, brain-index.log records reindexes
only. Quiet logs on a quiet system are normal, NOT a failure.

If content changed on GitHub recently, the matching reindex entry
must exist in brain-index.log within ~2 minutes of the change:

```bash
tail -3 /srv/brain/logs/brain-index.log
```

Final proof the door works end-to-end: run the watcher once manually
(idempotent -- an idle run does nothing; exit 0 = healthy):

```bash
/opt/repo-tools/repo-pull.sh /srv/brain/agentic-brain /srv/brain/logs /srv/brain/agentic-brain/brain-index brain && echo WATCHER_OK
```

### 2. Verify index freshness

```bash
cd /srv/brain/agentic-brain && /opt/repo-tools/venv/bin/python brain-index/query.py --check-freshness
```

PASS: "OK -- N chunks, built <timestamp>". STALE means the watcher
pulled but did not reindex -- investigate /srv/brain/logs/
brain-index.log. NEVER rebuild manually: the watcher owns the index.
A manual --force rebuild is reserved for corruption recovery, done
as hermes, and only after diagnosis.

### 3. Run the query

Query using any mode of the `brain-index` tool (hybrid, vector-only,
or keyword-only). Default: `query.py "<query>" --top-k 20`.

VPS agents (running on the server, no SSH):

```bash
cd /srv/brain/agentic-brain
/opt/repo-tools/venv/bin/python brain-index/query.py "<query>" --top-k 20
```

VPS-connected agents (remote machines, e.g. PC or laptop agents):
connect over SSH with the agent's own key door, then run the same
query inside the clone:

```bash
ssh -i <agent-key> -p 22 root@100.99.142.120 \
  "su - hermes -c \"cd /srv/brain/agentic-brain && /opt/repo-tools/venv/bin/python brain-index/query.py '<query>' --top-k 20\""
```

Quoting rule:
the remote command sits in double quotes; the query string sits in
single quotes inside it. If the query contains an apostrophe, rephrase
or escape it -- a broken quote fails the whole command.

Results return file path, domain, title, relevance score, and a text
snippet:

```
[1] research/insights/logbook.md [Research] -- logbook
    score: 0.0325
    The logbook is the shared append-only event log... (snippet)
[2] governance/system-constitution.md [Governance] -- system-constitution
    score: 0.0164
    This file is the highest-precedence document... (snippet)
```

### 4. Read top results

Read the top 3-5 results for full context. VPS agents use `read_file`
on the server paths; remote agents read the paths over SSH (e.g.
`cat`). The snippet in the query output is ~200 chars -- enough to
decide relevance, not enough for understanding.

### 5. Cite

Cite exact paths in the artifact (research/insights/...,
governance/..., library/...).

## Fallback

If the VPS or the shared index is unavailable:

```bash
grep -r "<search terms>" /srv/brain/agentic-brain/ --include="*.md"
```

Keyword-only search on the raw files of the live mirror. No semantic
matching, no ranking. If the VPS itself is unreachable (tailnet and
public door both down), fall back to the external query-brain skill
(clone + local index). Report broken tooling to Suggi.

## Pitfalls

- **First query ~1s (warm daemon).** `brain-embed.service`
  (127.0.0.1:8099) keeps embeddinggemma-300m loaded; query.py uses it
  and falls back to in-process load (~15s) if the daemon is down.
- **NEVER run index.py --force on the VPS index without a specific
  corruption diagnosis.** The watcher owns the index.
- **Bare `crontab` is EDIT mode.** `crontab` with no flag opens the
  editor and can wipe the crontab in non-interactive contexts. Read:
  `crontab -l` (own) or `crontab -u hermes -l` (root). Install:
  `echo '<line>' | crontab -u hermes -`.
- **Run brain commands as hermes, not root.** The index path resolves
  via hermes's `~/.brain-index` symlink (`/srv/brain/index`); root has
  no symlink and `query.py` reports "NO INDEX" (false alarm). The
  clone is `hermes:agents`; commits and the watcher run as hermes.
- **STALE freshness is a WATCHER problem, not a query problem.**
  Diagnose before querying.
- **SSH quoting.** Remote command in double quotes, query in single
  quotes. Apostrophes inside the query break it -- rephrase.
- **Public repo opsec.** This skill lives in a public repo. Never add
  key paths, the public IP, credentials, or tokens. The tailnet IP is
  safe (unreachable outside the tailnet); everything else is not.
- **Tailscale SSH check re-prompts when node keys rotate.** The
  key-based door on port 22 never re-prompts -- prefer it.
- **Outdated results.** Fresh results lag GitHub by at most 1 minute
  (watcher window) plus seconds of reindex time. If the watcher is
  alive, results are current. Do not treat seconds-late results as a
  bug.

## Related

- `brain-index` skill -- the tool this skill queries (build and
  maintain the index; non-VPS agents only)
- AGENTS.md Retrieval section -- the gate that invokes this skill
- `agentic-brain:research/insights/vps-brainclone-plus-index.md` -- the
  live-mirror blueprint (authoritative system reference)
- `agentic-brain:research/insights/brain-search-system.md` -- full system
  blueprint (query modes, eval gate, technology choices)
- `agentic-brain:governance/skills/external/query-brain.md` -- the
  clone-based query skill for non-VPS agents and fallback
- `brain-index/README.md` -- tool usage documentation
