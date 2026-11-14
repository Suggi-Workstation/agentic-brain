---
name: vps-brainclone-plus-index
id: 20260807T181615Z
tier: insight
status: active
source: []
author: Link
tags:
  - vps
  - live-mirror
  - brain-index
  - watcher
  - two-way-sync
  - freshness
  - fleet-infrastructure
  - cron
links:
  - research/insights/brain-search-system.md
  - research/insights/workspace-search-system.md
  - research/insights/stale-index-problem.md
  - research/insights/library-system.md
  - governance/skills/repo-write-vps.md
  - governance/template-insights.md
---

# VPS Live Mirrors and Watcher -- How the Repo Clones and Search Indexes Stay Current

The fleet VPS holds the working copies of the org's three content
repositories (`agentic-brain`, `agentic-forge`, `investing-hub`) and a
search index for each. Agents on the VPS read and write these clones
directly; GitHub is the mirror for the outside world. One program, the
watcher (`/opt/repo-tools/watch.py`), runs once a minute and does two
jobs: it keeps each clone and its GitHub repository equal in both
directions, and it keeps every search index equal to the files it
indexes. The same run keeps the search index of every agent workspace
current. Agents therefore never push, pull or rebuild an index: they
commit, and within a minute the commit is on GitHub and searchable.

## Parts

| Part | Where | What it does |
|:--|:--|:--|
| Watcher | `/opt/repo-tools/watch.py` | The program described here; Python, standard library only |
| Watcher tests | `/opt/repo-tools/watch-test.py` | Run the watcher against throwaway repositories and workspaces |
| Index runtime | `/opt/repo-tools/venv/` | Python environment of the index tools |
| Embedding service | `brain-embed.service`, `127.0.0.1:8099` | Keeps the embedding model loaded for every index build and query |
| Schedule | crontab of the `hermes` user | One line, every minute |
| Clone | `/srv/<name>/<repo>` | Working copy of one repository, branch `main` |
| Index tool | `<clone>/<name>-index/` | `index.py` (build), `query.py` (search and freshness check), `config.yaml` |
| Index data | `/srv/<name>/index/` | The built index, outside the repository; the tool reaches it as `~/.<name>-index` |
| Logs | `/srv/<name>/logs/` | `<name>-pull.log` (sync) and `<name>-index.log` (index) |

`<name>` is `brain`, `forge` or `investing`; the clones are
`/srv/brain/agentic-brain`, `/srv/forge/agentic-forge` and
`/srv/investing/investing-hub`. Clones, index data, logs and tools belong
to the group `agents` and sit outside every agent's home, so no single
agent's lifecycle owns them.

The crontab line:

```
* * * * * /opt/repo-tools/watch.py /srv/brain/agentic-brain /srv/forge/agentic-forge /srv/investing/investing-hub 2>&1 | logger -t repo-watch
```

## Targets

| Kind | Found by | Synced with GitHub | Index tool | Index log |
|:--|:--|:--|:--|:--|
| Repository | its clone path on the crontab line | yes | `<clone>/<name>-index/` | `/srv/<name>/logs/<name>-index.log` |
| Agent workspace | every `<profiles>/<agent>/workspace-<agent>/` that contains `scripts/workspace-search/` | no | that folder | `<profiles>/<agent>/logs/workspace-search-refresh.log` |

`<profiles>` is the Hermes profiles folder of the `hermes` user. A
workspace is a local git repository that is not on GitHub; which of its
folders are indexed is set in its own `config.yaml`
(`research/insights/workspace-search-system.md`).

## One Run

Each target runs in its own thread, so a slow target delays no other. A
run with nothing to do takes about a second.

Sync, for repositories only, under the sync lock:

1. `git fetch origin`.
2. If the clone has commits that GitHub lacks, push them. The push waits
   while the clone holds untracked files; the sync log names them.
3. If GitHub has commits that the clone lacks, fast-forward the clone to
   `origin/main`.
4. If both sides have new commits, no fast-forward is possible: rebase
   the local commits onto `origin/main` and push. The commits keep their
   authors; the watcher signs as committer `Repo Watcher`. History stays
   linear and holds the work of both sides.
5. If the rebase stops on a conflict (both sides changed the same
   lines), abort it, which leaves the clone as it was, and log it. The
   watcher never resolves a conflict and never commits anything.

Index, for every target, under the index lock:

6. `query.py --check-freshness` compares the index with its source: the
   index files are present and well-formed, were built with the model
   and chunking settings in `config.yaml`, every indexed file has the
   hash of the live file, and the build belongs to the current commit.
7. Answer `OK`: write one `ok` line to the index log.
8. Answer `STALE` or `NO INDEX`: run `index.py`, which embeds new and
   changed files and drops deleted ones.
9. Any other answer (`UNVERIFIED`, a crash): log it and leave the index
   alone.

The check runs on every run, not only after a push or pull. A build that
was skipped, interrupted or failed is therefore repeated on a later run
without a new commit. A fetch or push that hangs is ended after five
minutes; an index build has no time limit.

## Locks

Both locks are files in the target's git directory. They are never
waited for: a run that finds a lock held skips that step, and the next
run tries again.

| Lock | Held by | Effect |
|:--|:--|:--|
| `repo-pull.sync.lock` | the watcher during sync; the Library publisher (`scripts/library-publish.py`) while it writes and commits | two syncs never overlap; a half-written publication is never pushed |
| `repo-pull.index.lock` | the watcher during check and build; a full rebuild run by hand | one build per index at a time |

The locks are separate because a build can take far longer than a
minute. Sync continues every minute while a build runs; when the build
ends, the next check finds what changed meanwhile and catches up.

## Logs

| Log | Holds | Size limit |
|:--|:--|:--|
| `/srv/<name>/logs/<name>-pull.log` | Sync events only: pushes, failed pushes, rebases, conflicts, a held-back push, a failing fetch. Silent while nothing happens | 50 KB, five old copies (`/etc/logrotate.d/brain-tools`) |
| `/srv/<name>/logs/<name>-index.log` | One `ok` line per run, of which the last 50 are kept; every rebuild with its reason and the indexer's output | as above |
| `<profiles>/<agent>/logs/workspace-search-refresh.log` | The same as an index log, for that agent's workspace | 1 MB, two old copies (`/etc/logrotate.d/hermes-misc`) |
| System journal, tag `repo-watch` | Errors of the watcher itself; empty in normal operation | the journal's own limit |

A rebuild line reads
`reindexing (pulled=yes pushed=0): STALE -- <reason>`; `pulled` and
`pushed` say what the sync of that run did, and a workspace line carries
no sync part. A condition that lasts (GitHub unreachable, a held-back
push, a failing check) is logged once, not every minute.

## Rules

- Agents commit in the clone under their own name and never push, pull
  or rebase there; the watcher publishes
  (`governance/skills/repo-write-vps.md`).
- Nobody rebuilds an index by hand in normal operation. `STALE` that
  lasts longer than a build is a fault to report, not a reason to
  rebuild.
- Repository commands run as the `hermes` user, never as root.
- The clones carry no git identity, so a commit without an explicit
  author fails instead of going out under a wrong name.
- An untracked file left in a clone holds back every push of that clone.
  Scratch work stays outside the clones.
- A conflict is resolved by an agent or a person, deliberately. Nothing
  is force-pushed.

## Operations

Check that it works:

```
crontab -l                                # the watch.py line, naming the three clones
cd /srv/<name>/<repo> && env -u PYTHONPATH /opt/repo-tools/venv/bin/python <name>-index/query.py --check-freshness
tail -2 /srv/<name>/logs/<name>-index.log # an `ok` line from the last two minutes
journalctl -t repo-watch --since -1h      # no lines
```

`env -u PYTHONPATH` keeps the calling agent's Python packages out of the
index runtime.

| Task | How |
|:--|:--|
| Add a repository | Clone it to `/srv/<name>/<repo>` with a `<name>-index/` tool folder, an index data folder and a logs folder like the existing three, add its two logs to `/etc/logrotate.d/brain-tools`, and append the clone path to the crontab line |
| Add a workspace | Give the agent's workspace the `scripts/workspace-search/` folder; the next run builds its index |
| Full rebuild after a change of embedding model, dimension or chunking | `cd /srv/<name>/<repo> && flock .git/repo-pull.index.lock env -u PYTHONPATH /opt/repo-tools/venv/bin/python <name>-index/index.py --force`; the lock keeps the watcher out |
| Resolve a conflict | In the clone, naming yourself on each git command (`git -c user.name=<name> -c user.email=<email> ...`): `fetch origin`, `rebase origin/main`, fix the marked lines, `add` them, `rebase --continue`. The next run pushes the result |
| Change the watcher | Run `python3 /opt/repo-tools/watch-test.py`; then prove it on the live repositories: a probe file committed in each clone must reach GitHub and the index on its own, and deleting it on GitHub must remove it from the clone and the index on its own |

## Limits

- Up to one minute passes between a commit and its publication, and
  between a change on GitHub and its arrival on the VPS.
- A same-line conflict stops the sync of that repository until it is
  resolved; the other targets continue.
- While GitHub is unreachable, sync waits; the index still follows local
  commits.
- An `UNVERIFIED` index is not repaired automatically.
- The watcher serves the VPS. Agents on other machines search the VPS
  indexes over their own access to the VPS, or build an index from their
  own clone (`research/insights/brain-search-system.md`).

## Cross-Links

- `research/insights/brain-search-system.md` -- the search tool behind
  the repository indexes
- `research/insights/workspace-search-system.md` -- the workspace search
  engine
- `research/insights/stale-index-problem.md` -- why freshness is checked
  against the source
- `research/insights/library-system.md` -- the Library publisher that
  shares the sync lock
- `governance/skills/repo-write-vps.md` -- how an agent writes to a
  watched clone
- `governance/skills/query-brain-vps.md`,
  `governance/skills/query-forge-vps.md`,
  `governance/skills/query-investing-vps.md` -- the query procedures
- `governance/template-insights.md` -- the template this file follows
