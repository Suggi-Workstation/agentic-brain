---
name: query-brain-vps
description: "Query the shared agentic-brain index on the fleet VPS -- no cloning, watcher-maintained freshness. Use for all brain searches as Link or any VPS agent."
version: 1.0
author: Link
tags:
  - brain-index
  - vps
  - query
  - live-mirror
  - semantic-search
  - watcher
  - freshness
links:
  - governance/skills/external/query-brain.md
  - research/insights/vps-brainclone-plus-index.md
  - research/insights/brain-search-system.md
trigger_keywords:
  - query brain
  - search brain
  - brain query
  - find in brain
---

# Query-Brain-VPS -- Search the Shared Index

## What This Skill Does

Queries the shared brain index on the fleet VPS (suggi-vps). The live
mirror at /srv/brain/agentic-brain is kept fresh by the watcher
(/opt/brain-tools/brain-pull.sh, cron every minute); the index at
/srv/brain-index is reindexed automatically on any content change.
NO cloning, NO local index, NO manual rebuilds. This skill replaces
the clone-and-query ritual for every agent that has access to the VPS
(Link via the key door, all VPS agents directly).

## When to Invoke

- Any brain search: "search the brain for X", "query brain",
  "find in brain".
- Preflight and session-end brain-index checks (via those skills).
- Before writing any artifact that cites brain knowledge
  (retrieval-first discipline).

## Procedure

### 1. Check the watcher is healthy

The fleet depends on the watcher. Verify it ran recently:

```bash
tail -3 /home/hermes/logs/brain-pull.log
```

PASS: last entry within ~2 minutes. If older: the cron may be broken.
Check `crontab -l` and the system clock BEFORE querying. Results from
a dead watcher are silently stale -- that is the new failure class
this check guards.

### 2. Check index freshness

```bash
cd /srv/brain/agentic-brain && /opt/brain-tools/venv/bin/python brain-index/query.py --check-freshness
```

PASS: "OK -- N chunks, built <timestamp>". STALE means the watcher
pulled but did not reindex -- investigate /home/hermes/logs/
brain-index.log. NEVER rebuild manually: the watcher owns the index.
A manual --force rebuild is reserved for corruption recovery, done
as hermes, and only after diagnosis.

### 3. Query

VPS agents (direct, no SSH):

```bash
cd /srv/brain/agentic-brain
/opt/brain-tools/venv/bin/python brain-index/query.py "<query>" --top-k 20
```

Link (PC, via the key door):

```bash
ssh -i ~/.ssh/id_ed25519_vps -p 2222 root@100.99.142.120 \
  "su - hermes -c \"cd /srv/brain/agentic-brain && /opt/brain-tools/venv/bin/python brain-index/query.py '<query>' --top-k 20\""
```

Quoting rule: the remote command sits in double quotes; the query
string sits in single quotes inside it. If the query contains an
apostrophe, rephrase or escape it -- a broken quote fails the whole
command.

Results are ranked with scores, file paths, and snippets.

### 4. Read and cite

Read the top 3-5 results for context (read_file on the VPS paths, or
cat via SSH). Cite exact paths in the artifact
(research/insights/..., governance/..., library/...).

### 5. Fallback -- VPS unreachable

If the key door or the tailnet is down:

1. grep fallback on a fresh clone (see
   governance/skills/external/query-brain.md for the full
   clone-and-query procedure).
2. If the VPS is up but the index is broken: the external skill's
   local rebuild path is the degraded mode. Report the watcher issue
   to the operator -- do not silently accept a broken shared index.

## Pitfalls

- NEVER run index.py --force on the VPS index without a specific
  corruption diagnosis. The watcher owns the index.
- STALE freshness is a WATCHER problem, not a query problem.
  Diagnose before querying.
- Do not clone the brain on the VPS for queries -- the live mirror
  IS the checkout.
- SSH quoting: remote command in double quotes, query in single
  quotes. Apostrophes inside the query break it -- rephrase.
- Tailscale SSH check re-prompts when either node key rotates
  (client auto-updates). The key door (port 2222, tailnet-only,
  key ~/.ssh/id_ed25519_vps) never re-prompts -- prefer it.
- Fresh results lag GitHub by at most 1 minute (watcher window)
  plus seconds of reindex time. Coordination is minute-scale; do
  not treat seconds-late results as a bug.

## Related

- research/insights/vps-brainclone-plus-index.md -- the live-mirror
  blueprint (authoritative system reference)
- governance/skills/external/query-brain.md -- the clone-based query
  skill for non-VPS agents and fallback
- research/insights/brain-search-system.md -- the search-tool
  blueprint (hybrid search, eval gate, technology choices)
- brain-index/README.md -- tool usage documentation
- AGENTS.md Retrieval section -- the gate that invokes this skill
