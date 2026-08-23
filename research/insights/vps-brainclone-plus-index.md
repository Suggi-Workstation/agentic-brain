---
name: vps-brainclone-plus-index
id: 20260807T181615Z
tier: insight
source:
  - 20260720T182751Z
  - 20260719T070443Z
author: Link
tags:
  - vps
  - live-mirror
  - brain-index
  - watcher
  - two-way-sync
  - freshness
  - fleet-infrastructure
  - tailscale
  - cron
links:
  - research/insights/brain-search-system.md
  - research/insights/stale-index-problem.md
  - governance/template-insights.md
---

# VPS Brain Clone Plus Index -- The Live-Mirror Blueprint

## Version History

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-08-07 | Link | Initial insight. |
| 2 | 2026-08-08 | Link | Watcher interval 5 min -> 1 min (idle cycle cost measured: 0.42 s, 17 MB). |
| 3 | 2026-08-09 | Link | Watcher logs moved to /srv/brain/logs (fleet-visible, root:agents) + logrotate (size 1M, rotate 5, compressed). |
| 4 | 2026-08-23 | Morpheus | Multi-repo generalization: index data moved to /srv/<domain>/index, watcher generalized to repo-pull.sh (one cron line per repo), forge + investing-hub onboarded. |

This file is the finished-system reference for the fleet VPS live
mirror: the persistent agentic-brain clone, the shared index, and the
watcher that keeps both fresh. It extends brain-search-system.md (the
search-tool blueprint) with the infrastructure layer that makes the
index always fresh without per-session rituals. Every agent in the
Suggi-Workstation org should read this file before operating on the
fleet VPS.

## The Insight

A persistent live-mirror clone of the agentic-brain on the fleet VPS,
synced with GitHub in both directions every minute by a cron
watcher that reindexes on any content change, turns the brain from a
per-agent clone-discard ritual into an always-fresh fleet-shared
service.

## Evidence

### Design phase -- 2026-08-06

The live-mirror pattern was researched and confirmed by the user
before any server was ordered:

- Persistent clone at /srv/brain/agentic-brain replaces the
  clone-discard ritual for VPS agents.
- Cron git pull every minute (no webhooks, tailnet-only network).
- Cron incremental reindex on HEAD change.
- NO auto-commit cron (secrets and junk risk; commits stay
  deliberate).
- Index data lives outside the repo, outside agent homes.
- Hermes (user hermes) and OpenClaw (user openclaw) live side by
  side; shared data belongs to neither.

### Build phase -- 2026-08-07

The server was provisioned and the system built:

- netcup RS 4000 G12, Vienna, 12 dedicated EPYC cores, 32 GB RAM,
  1 TB NVMe, Ubuntu 24.04.4 UEFI Minimal, hostname suggi-vps.
- Tailscale as root system daemon (the box is the tailnet node);
  Hermes v0.20.0 installed under user hermes.
- agents group created; /srv/brain and /srv/brain/index owned
  root:agents with setgid 2775 -- any agent user in the group can
  read and write (openclaw joins the group on migration).
- Clone at /srv/brain/agentic-brain; token moved to
  /home/hermes/.git-credentials (mode 600); remote URL clean.
- Fleet-neutral tools at /opt/brain-tools: brain-pull.sh (the
  watcher) + venv/ (index python environment, root:agents, setgid).
- Initial index build: 4931 chunks across 397 files -- identical to
  the PC index, proving the same embedder on the same source yields
  the same vectors.

### The gap found by questioning

The user asked: "when you commit to the local clone, does the
embedder run?" The answer was no. The watcher's reindex condition was
before != after (pull-only). A purely local commit pushed by the
watcher had before == after, so the new artifact sat unindexed until
some future pull triggered a reindex. Root cause: a state-transition
condition that checked one of two paths (pulled) but not the other
(pushed). Fixed structurally: the watcher tracks a pushed flag and
reindexes when content changed in EITHER direction. The lesson:
every state-transition condition in a sync system must enumerate all
paths, and every path must be verified by questioning, not by
inspection alone.

### End-to-end proofs

- ENT-048 logbook entry: committed locally, NOT pushed manually;
  the watcher pushed it (commit 68cb3f1 verified on origin/main).
- Divergence simulation in /tmp (git init --bare -b main + two
  clones): with Suggi's write X on GitHub and agent write Y local,
  the watcher's push is rejected (non-fast-forward), fast-forward
  fails, rebase replays Y on top of X, and the final linear history
  contains both writes. Nothing is lost.
- Conflict case: both writes touching the same lines halt the
  rebase; the watcher aborts the rebase back to a clean state, logs
  loudly, and exits non-zero. An agent resolves manually; the next
  tick resumes normal sync. Never auto-resolved, because
  auto-resolving knowledge conflicts risks silently mangling
  content.
- Freshness check after the reindex-path exercise: OK, 4931 chunks,
  heartbeat updated to current HEAD.
- Daemon wiring (2026-08-18): index.py rebuilds verified in a /tmp
  sandbox -- daemon path 1.2s vs in-process fallback 10.2s for the
  same 6 chunks; row-wise cosine between daemon-normalized and
  in-process vectors = 1.0 (identical). Production incremental
  reindex 2.6s. Divergence self-heal (rebase + push, nothing lost,
  linear history) and conflict abort (clean state, exit 1) both
  verified in sandbox.

## The System -- How It Works

### Where everything lives -- three categories, never mixed

```
/srv/brain/agentic-brain/       KNOWLEDGE: the persistent clone
                                (root:agents, setgid 2775)
/srv/brain/index/               DATA: chunks.jsonl, vectors.npy,
                                bm25/, meta.json, heartbeat.json
                                (root:agents, setgid 2775;
                                ~/.brain-index is a symlink to it)
/opt/brain-tools/               CODE: brain-pull.sh + venv/
                                (root:agents, setgid 2775)
/home/hermes/crontab            SCHEDULE: * * * * *
                                /opt/brain-tools/brain-pull.sh
/srv/brain/logs/              OBSERVABILITY: brain-pull.log,
                                brain-index.log
```

The rule: knowledge goes in the repo, data goes in /srv, code goes
in /opt, schedule goes in cron. No category is nested inside another.
This differs from brain-search-system.md in two deliberate ways:
(1) the index DATA moved from per-machine ~/.brain-index to the
fleet-shared /srv/brain/index (the VPS is the shared index service),
and (2) tooling moved from user homes to /opt/brain-tools so no
single user's lifecycle owns the fleet infrastructure.

### The watcher -- brain-pull.sh

Every minute the cron fires and the watcher:

1. cd /srv/brain/agentic-brain, record before = HEAD, pushed = 0.
2. git fetch origin.
3. If the clone has committed-but-unpushed work (rev-list count of
   origin/main..HEAD > 0): git push. Never auto-commits -- only
   already-committed work moves.
4. git merge --ff-only origin/main. If it fails (divergence),
   git rebase origin/main && git push.
5. Record after = HEAD. If before != after (pulled) OR pushed = 1:
   run the embedder (unsloth/embeddinggemma-300m, 768-dim, via the
   isolated venv with the warm daemon brain-embed.service at
   127.0.0.1:8099) for an incremental reindex, and log the event.
   Indexing calls the daemon first (document path, normalized
   locally) and falls back to in-process loading if the daemon is
   down -- same pattern as query.py.

The embedder runs together with the watcher, in both directions,
always after content moved. It never runs standalone.

### Two-way sync semantics

| Direction | Mechanism | Max lag |
|:--|:--|:--|
| GitHub -> clone | cron fetch + ff-only (rebase if diverged) | 1 min |
| clone -> GitHub | watcher auto-push of committed work | 1 min |
| clone -> index | reindex on pushed OR pulled content change | seconds after pull/push |
| GitHub -> Suggi's Obsidian | Obsidian Git auto-pull (PC) | 5 min |

Eventual consistency with a 1-minute bound is the accepted standard
for git-sync systems; webhook real-time was explicitly rejected
(GitHub cannot reach the tailnet, and the infra cost is unjustified
for a small fleet).

### Divergence and conflict handling

Both sides advancing in different directions is the normal
convergence case: the push is rejected by GitHub (non-fast-forward
guard), fast-forward fails, rebase replays local commits on top of
remote commits, push succeeds. History stays linear and contains
both writes. Only same-line conflicts halt the watcher; those are
resolved deliberately by an agent (git rebase --continue) and the
next tick pushes. There is no silent loss and no auto-resolution.

### Who uses it

- VPS Hermes agents (Morpheus, Neo, subagents): read and write the
  clone directly at /srv/brain/agentic-brain; query the shared index
  through brain-index/query.py; their commits are pushed by the
  watcher within 1 minute.
- OpenClaw (Ava, when migrated): same access via the agents group;
  the layout is framework-neutral (files, not APIs).
- Link (PC) and Linkie (laptop): keep the clone-discard ritual and
  their own local indexes per brain-search-system.md. They can
  optionally query the VPS index over the tailnet.
- Suggi: writes to GitHub directly; the watcher pulls and reindexes
  automatically.

### Security model

- Ops access is tailnet-only: Tailscale SSH (passwordless for the
  tailnet owner, one-time browser approval per device).
- The GITHUB_TOKEN lives in /home/hermes/.git-credentials (mode
  600), never in the repo config or remote URL.
- No auto-commits: the watcher can only push work an agent already
  committed deliberately.
- No public exposure: no webhooks, no funnel, no open ports.

## Implications

1. VPS agents never clone-discard again. The live mirror is their
   checkout; writing an artifact means committing into
   /srv/brain/agentic-brain and letting the watcher push.
2. Both directions converge within 1 minute. Suggi's GitHub edits
   reach the fleet and the shared index automatically; fleet
   artifacts reach GitHub automatically.
3. The stale-index failure class is structurally prevented: reindex
   fires on any content change in either direction, and the
   heartbeat dead-man's-switch makes a stale index visible to every
   query (stale-index-problem.md).
4. Fleet-neutral ownership survives any user's lifecycle: data and
   tools live outside agent homes; deleting a user never deletes the
   brain.
5. Zero API cost: the watcher is git plus a local CPU embedder; no
   LLM tokens, no embedding API, no subscriptions.
6. New VPS agents need zero setup to search: the index already
   exists and is kept fresh by the watcher.
7. The PC/laptop pattern (per-machine indexes, clone-discard) stays
   valid; the VPS pattern is the shared-service evolution for the
   fleet box.

## Counter-evidence

This architecture would be invalidated if:

- The 1-minute staleness window causes harmful coordination errors
  (agents acting on a logbook or artifact up to 1 minute stale).
  Not observed; all coordination is minute-scale. A real-time need
  would justify webhooks via Tailscale Funnel.
- The rebase-on-divergence path silently loses or reorders
  knowledge. It cannot: same-line conflicts halt for manual
  resolution, and no auto-resolution exists.
- The watcher fails silently and staleness goes unnoticed. It
  cannot: every run is logged, pushes and reindexes are logged with
  timestamps, and the heartbeat freshness check surfaces gaps to any
  querying agent.
- GitHub adds first-class bidirectional sync that makes the watcher
  obsolete. Then the watcher is deleted and the pattern remains
  documented here.
- A single shared index on the VPS becomes the bottleneck for
  agents on other machines. Mitigation: per-machine indexes remain
  the documented fallback (brain-search-system.md).

## Cross-Links

- `research/insights/brain-search-system.md` -- parent blueprint of
  the search tool this infrastructure serves
- `research/insights/stale-index-problem.md` -- the failure class this
  system prevents structurally
- `governance/template-insights.md` -- the template this file follows
- `logbook/queue.log` -- ENT-048, the watcher-pushed proof entry

### Generalization -- three repos, one watcher (2026-08-23)

The live-mirror pattern now covers every content repo in the org,
grouped by domain under /srv:

```
/srv/brain/agentic-brain/       clone      /srv/brain/index/       data
/srv/forge/agentic-forge/       clone      /srv/forge/index/       data
/srv/investing/investing-hub/   clone      /srv/investing/index/   data
```

- Index DATA lives at `/srv/<domain>/index` (moved from
  `/srv/brain-index` on 2026-08-23); `~/.<name>-index` symlinks
  resolve it per repo (`~/.brain-index`, `~/.forge-index`,
  `~/.investing-index`).
- The search TOOL lives inside each repo (`<name>-index/` folders:
  `brain-index/`, `forge-index/`, `investing-index/`) and indexes
  whatever repo contains it (the SCRIPT_DIR.parent rule).
- The watcher logic lives once in `/opt/brain-tools/repo-pull.sh`;
  one hermes cron line per repo passes clone path, logs dir, tool
  dir, and log prefix. `brain-pull.sh` remains as a compatibility
  shim around it, so existing references stay valid.
- Logs stay event-driven at `/srv/<domain>/logs/<prefix>-pull.log`
  and `<prefix>-index.log`; logrotate covers all of them.
- One warm embed daemon (127.0.0.1:8099) serves all three indexes --
  same model, same dimensions. Cross-index contamination is
  impossible by construction: each tool's config resolves to its own
  data dir.
