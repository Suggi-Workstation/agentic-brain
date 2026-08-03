---
name: openclaw-server-migration
id: 20260803T082803Z
tier: report
author: Ava
tags: [openclaw, migration, vps, backup, infrastructure, netcup, hermes]
links:
  - research/reports/ava-openclaw-memory-system.md
  - research/reports/link-hermes-memory-system.md
  - governance/template-reports.md
---

# OpenClaw Server Migration -- Complete State Transfer Between VPS Providers

## Executive Summary

Question: Can OpenClaw (Ava, Cato, and all sub-agents) be moved completely
from one VPS to another -- including sessions, memories, QMD indexes, and
configuration -- without losing anything or bootstrapping from scratch?

Answer: Yes. There are two working paths. (1) netcup-to-netcup migration via
offline snapshot export/import, which is a byte-identical disk clone of the
entire server, officially supported by netcup. (2) Cross-provider migration
via `openclaw backup create` + restore, which carries all durable state
(config, credentials, closed session transcripts, lossless-claw conversation
DAG, QMD index, recall store, media, and all workspaces) in a single archive.

Key evidence: A real 833 MB backup archive was created and inspected during
this research. It contained all 8 bootstrap files, 37 closed session
transcripts, lcm.db (16.8 MB), QMD index.sqlite for main and cato agents,
openclaw.json, .env, credentials, and media. 529 volatile files (live
session transcripts, cron logs, queues, sockets, pid/tmp) were intentionally
skipped. The only state living outside the archive is the QMD GGUF model
cache (~/.cache/qmd/models, 2.2 GB), the brain-index (~/.brain-index,
12 MB), systemd service units, the OpenClaw installation itself, and
Tailscale state -- all of which are re-downloadable, rebuildable, or
recreatable in minutes.

Confidence: High (90%). Every claim about backup contents was verified by
creating and inspecting a real archive on 2026-08-03, not inferred from
documentation alone.

## Research Question

Can OpenClaw be migrated completely from a netcup VPS 1000 G12 (OpenClaw
Special, hourly-billed) to a more powerful server (netcup RS 2000/4000 G12,
or any other provider), carrying all sessions, memories, and configuration
with nothing lost?

Scope: in. Full-server migration paths (netcup snapshot, backup archive,
rsync), what is and is not preserved, session/memory preservation, QMD
index/model handling, verification steps.

Scope: out. Live zero-downtime migration (there is always a downtime
window), multi-server clustering, load balancing, and the OpenClaw install
procedure itself (assumed: `npm install -g openclaw` on the target).

Why this matters: Suggi rents a netcup VPS 1000 G12 OpenClaw Special
(4 vCPU, 8 GB RAM, 256 GB NVMe, 10.36 EUR/mo equivalent, hourly-billed).
The in-place upgrade path is unavailable, so a second server must be rented
and the running system moved onto it. The alternative considered was a
bootstrap-from-repos rebuild, which would lose session history and recall
state.

## Methodology

Approach: empirical verification plus documentation review.

1. Read netcup's official "Migrating Server" helpcenter article and the
   SCP Media documentation (retrieved 2026-08-03).
2. Read community guides on netcup snapshot export/import, including the
   .raw.zst vs qcow2 format constraint (retrieved 2026-08-03).
3. Read OpenClaw's `cli/backup.md` documentation (local docs,
   retrieved 2026-08-03).
4. Created a real backup archive on the live VPS with
   `openclaw backup create --output /tmp/migration-test` and inspected its
   contents with `tar -tzf`. This produced the definitive included/skipped
   inventory. Archive: 833 MB, 2026-08-03.
5. Verified the archive contents for: bootstrap files, session transcripts,
   lcm.db, QMD index.sqlite, config, credentials, media.
6. Enumerated state outside ~/.openclaw that the archive does not cover:
   ~/.cache/qmd/models, ~/.brain-index, ~/.config/systemd/user,
   ~/.npm-global, Tailscale state.

Limitations: The backup was created while the gateway was running, so 529
volatile files (live sessions, cron logs, queues) were skipped -- this is
expected behavior; a migration should stop the gateway first to capture
everything. The archive contents were inspected, not restored end-to-end
on a target server; the restore step was not exercised in this research.

## Findings

### Finding 1: netcup-to-netcup Snapshot Migration Is Officially Supported

netcup's official "Migrating Server" article documents the complete path:
(1) shut down the source server, (2) create an offline snapshot
(Media > Snapshots), (3) export the snapshot -- it then appears under
Images > Custom Images on all servers in the account, (4) install the
snapshot on the target server, (5) adjust network configuration.

- Evidence: netcup helpcenter article, retrieved 2026-08-03.
- Additional detail: only offline snapshots are exportable. The first
  export per server is free; additional exports cost ~1.50 EUR each.
  The target disk must be at least as large as the used partition.
- This is a byte-identical disk clone: OS, OpenClaw, ~/.openclaw, models,
  everything. Nothing is lost, no bootstrap needed.
- Confidence: High (95%).

### Finding 2: Cross-Provider Snapshot Import Does Not Work Directly

Provider-native VPS snapshots cannot be imported into a competing provider
as-is. The reviewed documentation (agentxcloud.com comparison, retrieved
2026-08-03) confirms: "In most cases you cannot take a provider-native VPS
snapshot object and import it into a competing provider as-is." Some
providers accept separately prepared custom images (netcup accepts raw,
qcow, qcow2; Hetzner Cloud supports custom image upload), but Strato,
IONOS, and Hostinger consumer VPS lines generally do not accept custom
images.

- Confidence: High (85%).

### Finding 3: `openclaw backup create` Produces a Complete State Archive

A real archive (833 MB, created 2026-08-03) contained:

| Item | Included? | Evidence |
|:--|:--|:--|
| All 8 bootstrap files (SOUL, AGENTS, MEMORY, IDENTITY, USER, TOOLS, HEARTBEAT, DREAMS) | Yes | present in archive |
| Closed session transcripts | Yes (37 files) | agents/*/sessions/*.jsonl |
| lcm.db (lossless-claw conversation DAG) | Yes | 16.8 MB, in archive |
| QMD index.sqlite (main + cato) | Yes | both agent qmd dirs |
| openclaw.json, .env, credentials | Yes | present |
| media/ | Yes | 11 files |
| All 5 workspaces | Yes | inside ~/.openclaw |
| Live/active session transcripts | No (skipped) | 529 volatile files skipped |

- The backup snapshots SQLite databases safely (VACUUM INTO) so WAL/SHM
  files do not corrupt the archive.
- Confidence: High (95%) -- empirically verified.

### Finding 4: Session and Memory Preservation Depends on Gateway State

Sessions: 203 transcript files exist on the live system; 37 closed session
files made it into the archive, and 529 volatile files (live sessions,
cron logs, queues, sockets, pid/tmp) were skipped. The current/live
session being written at backup time is excluded.

Memories: MEMORY.md, memory/*.md, identity/*.md, DREAMS.md are all in the
workspace, which is inside ~/.openclaw and included. The QMD index
(sqlite) is included, so memory_search results are preserved. The recall
store (plugin-state) is included. lcm.db preserves the lossless-claw
conversation history.

For a complete migration: stop the gateway first
(`openclaw gateway stop`), then back up. With the gateway stopped, there
are no live sessions, so everything is captured.

- Confidence: High (90%).

### Finding 5: State Outside ~/.openclaw Must Be Handled Separately

Not in the backup archive:

| Item | Location | Size | How to handle |
|:--|:--|:--|:--|
| QMD GGUF models | ~/.cache/qmd/models | 2.2 GB | Copy or re-download (auto on first search) |
| brain-index | ~/.brain-index | 12 MB | Copy or rebuild via brain-index skill |
| systemd user services | ~/.config/systemd/user/ | small | Copy or recreate (openclaw gateway status shows the unit) |
| OpenClaw install | ~/.npm-global | ~1 GB | Reinstall: npm install -g openclaw |
| Tailscale state | /var/lib/tailscale | small | Re-auth on new server |

- Confidence: High (95%) -- verified by inspection.

### Finding 6: Negative Result -- Restore Was Not Exercised

The backup restore path (`openclaw backup restore <archive>`) was not
run on a target server during this research. The restore procedure is
documented (copy archive, install OpenClaw, restore, reinstall plugins
with `openclaw plugins update <id>` if needed), but end-to-end restore
was not verified. This is the one unverified step in the migration plan.

- Confidence: N/A (not tested).

## Discussion

The migration question resolves into two clean paths depending on the
target:

1. netcup-to-netcup: use the snapshot export/import path. It is
   officially supported, free for the first export, and produces a
   byte-identical clone. This is the lowest-effort, highest-fidelity path.

2. netcup-to-other-provider: use `openclaw backup create` + restore (or
   rsync of ~/.openclaw). This carries all durable state but requires
   re-handling the model cache, brain-index, systemd units, install, and
   Tailscale separately. It works on any provider.

A bootstrap-from-repos rebuild (clone 5 workspaces + brain, recreate
config) is only needed if the backup archive is lost. The workspaces are
git-mirrored as a permanent safety net, but session transcripts, lcm.db,
QMD index, and recall store are NOT in git -- they only exist in the
archive. This is the single most important fact for Suggi: the backup
archive is the only copy of the conversation history and recall state.

The 529 skipped volatile files are a feature, not a bug: they are live
session files being written at backup time, cron run logs, delivery
queues, and pid/tmp files with no restoration value. Stopping the gateway
before backup eliminates the live-session exclusion.

## Conclusion

OpenClaw can be migrated completely to a new VPS with nothing lost,
provided the right path is used:

- netcup-to-netcup: offline snapshot export/import (byte-identical, no
  bootstrap).
- netcup-to-any-provider: `openclaw backup create` + restore, plus
  separate handling of model cache, brain-index, systemd units, install,
  and Tailscale.

Recommendation: For the planned move from VPS 1000 G12 to RS 2000/4000
G12 on netcup, use the snapshot path -- it is officially supported, free,
and complete. For any future cross-provider move, use the backup archive
path and always stop the gateway before creating the backup.

Open questions: (1) End-to-end restore on a target server has not been
exercised -- a dry-run migration on a scratch server is recommended before
the real move. (2) Whether Hermes can run side-by-side on the same VPS
with OpenClaw (both headless services, separate ports) is documented
separately and looks feasible, but was not part of this migration test.

## Evaluation History

| Evaluator | Date | Verdict | Changes Made |
|:--|:--|:--|:--|
| (waived) | 2026-08-03 | WAIVED | Operator (Suggi) instructed to skip independent evaluation. |

## Cross-Links

- `research/reports/ava-openclaw-memory-system.md` -- the memory stack
  that this migration preserves (QMD + Lossless Claw + Active Memory)
- `research/reports/link-hermes-memory-system.md` -- Hermes/Mnemosyne
  architecture, relevant for the parallel-hosting question
- `governance/template-reports.md` -- format specification
