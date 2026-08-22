---
name: mnemosyne-system
id: 20260817T123124Z
tier: insight
source:
  - 20260810T112709Z
  - 20260810T112711Z
  - 20260802T124915Z
author: Link
tags: [mnemosyne, memory, fleet, shared-memory, architecture, cron, embeddings]
links:
  - research/insights/two-tier-fleet-memory-single-vector-space.md
  - research/reports/link-hermes-memory-system.md
  - reflections/2026-08-10_link_shared-memory-is-an-operations-problem.md
  - logbook/queue.log
  - governance/system-blueprint.md
---

# Mnemosyne System Anatomy (Fleet Memory Reference)

## The Insight

Fleet memory is one end-to-end loop -- every silent failure mode lives at
exactly one link of the chain (write path, cron ticker, relay, or pull
path), so the system is only trustworthy when verified link by link, never
from a single "sync succeeded" report.

## Evidence

This document is the operational anatomy of the fleet memory system as
of 2026-08-17: every path, every component, the full data flow, the
provisioning recipe, and the failure catalog. It complements
`two-tier-fleet-memory-single-vector-space` (the realization of WHY the
system is shaped this way) with the WHAT/HOW mechanics, verified live
on all four fleet agents (Link, Linkie, Morpheus, Neo).

### 1. Three memory scopes -- never mix them

Fleet knowledge lives in exactly three places. Each has one job.

| Scope | What goes there | Writer | Sync | Reader |
|:--|:--|:--|:--|:--|
| Personal Mnemosyne | Private experience, session learnings | Automatic (`mnemosyne_*` tools) | Never leaves the machine | The agent alone |
| Shared surface DB | Cross-agent stable facts (meta, preference, correction, identity) | Deliberate (`mnemosyne_shared_*` tools) | 5-min cron via blind relay | All fleet agents |
| Agentic-brain | Governance, library, insights, proposals | Manual (write-* skills) | Git watcher on the VPS | Everyone, indexed |

A personal fact never syncs. A shared fact is fleet-public by design.
Governance knowledge never enters either DB. (Source: 20260810T112709Z.)

### 2. Personal Mnemosyne (the private tier)

One SQLite DB per agent at
`<profile>/mnemosyne/data/mnemosyne.db`. Hybrid retrieval: dense vectors
(sqlite-vec) + FTS5 full-text + importance-weighted recall, all inside
the BEAM model (working / episodic / fact triples). On top sit canonical
single-source-of-truth slots (`mnemosyne_remember_canonical`) and the
temporal knowledge graph (`mnemosyne_triple_*`). Consolidation
(`mnemosyne_sleep`) compresses old working memories into episodic
summaries. Relevant context is auto-injected into every turn.

Current fleet sizes (2026-08-17): Link 560 working / 41 episodic,
Morpheus 35 working / 3 episodic (post-cleanup), Neo/Linkie smaller.
New memories embed automatically AT WRITE TIME -- no manual reindex
exists for ordinary writes; reindex is only for model switches or
corruption repair.

Embedding model is fleet-locked: `BAAI/bge-large-en-v1.5`, 1024
dimensions, set in every profile `.env`
(`MNEMOSYNE_EMBEDDING_MODEL` + `MNEMOSYNE_EMBEDDING_DIM=1024`) AND in
the VPS systemd units. One vector space for the whole fleet; mixed
dimensions are a corruption signal, not a retrieval nuance.

### 3. Shared surface DB (the public tier, per agent)

A SECOND SQLite DB per agent at
`<profile>/mnemosyne/data/shared/mnemosyne.db`. It is a local working
copy of the fleet shared surface -- agents never touch the relay
directly for reads or writes. Key internals:

- Canonical session `hermes_shared_surface`; all rows are
  `scope='global'`. Rows with any other session/scope are "unowned"
  and the sync engine refuses to work with them.
- The `sync_meta` table holds the per-agent sync identity:
  `device_id`, `surface_db_id=shared-surface-v1`,
  `configured_push_remote`, `last_pull_cursor_<remote>`, and
  `last_sync_at_<remote>`. This is the first table to read when
  debugging "is my agent in the loop".
- Device IDs (verified 2026-08-17): Link = `device-99dc8807`,
  Linkie = `device-0ec2c42d`, Morpheus = `device-aacc572b`,
  Neo = `device-6f7d8d51`. The relay's `memory_events` table is
  partitioned by these IDs.

### 4. The relay (blind conduit on the VPS)

`/srv/mnemosyne-shared/mnemosyne.db`, owned by systemd unit
`hermes-mnemosyne-sync.service`:

```
ExecStart: mnemosyne sync-serve --db-path /srv/mnemosyne-shared/mnemosyne.db \
  --host 127.0.0.1 --port 8765 --api-key-file /srv/mnemosyne-shared/.secrets/api-key
```

- Binds loopback only. Tailscale serve fronts it with a real cert:
  `https://suggi-vps.tail40302e.ts.net:8765 -> http://127.0.0.1:8765`
  (tailnet-only; not the public web).
- Auth: API key (constant-time compare) + HMAC body signature on all
  data endpoints; `/healthz` is deliberately public (heartbeat only).
- Content is end-to-end encrypted with a client-side key (file
  `/srv/mnemosyne-shared/.secrets/encryption-key`, mode 600). The
  relay CANNOT read any memory even if fully compromised.
- The relay is a conduit, NOT a store. Verified 2026-08-17: 31 rows in
  `memory_events` (ciphertext), ZERO rows in `working_memory` /
  `memories`. Its schema tables exist but are never populated.
- COROLLARY (scar): never point an agent's shared-DB path at the
  relay DB. A DB that is both relay and client reports "Duplicates: N"
  and never materializes content.
- STALENESS TRAP: the relay main DB's mtime (Aug 10) means nothing.
  SQLite WAL mode writes live data to `mnemosyne.db-wal`; the main
  file only advances at checkpoint. Always check `-wal` mtime before
  calling a store "stale". (This trap drove the Aug 16-17 audit that
  produced this document.)

### 5. The data flow, end to end

1. An agent writes a fact with `mnemosyne_shared_remember` (kind:
   meta | preference | correction | identity). The write lands in
   the agent's LOCAL shared DB via the
   `memory.mnemosyne.shared_surface_path` config key.
2. NO sync events exist yet -- the engine diff-generates events AT
   SYNC TIME, not at write time (`memory_events: 0` right after a
   write is normal, not a bug).
3. Every 5 minutes the agent's Hermes cron job `mnemosyne-sync`
   (no_agent Python watchdog) runs
   `mnemosyne sync --mode bidirectional` with explicit env
   (model + dim), key files, and the agent's DB path.
4. Push: local diff becomes encrypted events, POSTed to the relay.
5. Pull: the relay returns events newer than the agent's
   `last_pull_cursor`; the agent materializes and re-embeds them
   locally (CPU fastembed, ~112ms/fact).
6. Deletes become tombstones generated at sync time, so a fact
   deleted anywhere converges to deleted everywhere (proven
   2026-08-15 with a 3-agent create/delete test: 3/3/3 propagation,
   then 0/0/0 convergence, no resurrection).
7. Convergence: every agent's shared DB holds the same working set
   within one 5-minute cycle. Measured cost: ~1.5s per idle cycle,
   zero LLM tokens (stdlib-only sync protocol, no model in the data
   path).

Verified fleet-wide 2026-08-17: 18 working rows on Link, Morpheus,
and Neo (Linkie lags only when his app is closed); 31 relay events.

### 6. The cron and ticker layer (where schedules go to die)

Cron is NOT a daemon. Jobs live in `<profile>/cron/jobs.json`; they
only FIRE when a process owning that HERMES_HOME runs a 60-second
ticker:

- Desktop machines (Link PC, Linkie laptop): the desktop app backend
  ticks when `HERMES_DESKTOP=1` and the sticky
  `<HERMES_ROOT>/active_profile` file names the profile. The app's
  own `--profile` launch flag does NOT reach the backend spawn.
  Scar: Linkie's ticker was dead Aug 11-15 simply because the app
  was closed -- config was perfect, sync was silently frozen.
- Headless profiles (Morpheus, Neo on the VPS): `hermes serve` does
  NOT tick. Each profile needs a gateway:
  `HERMES_HOME=<profile> hermes gateway install --system
  --run-as-user hermes --start-now` -> `hermes-gateway-<name>.service`,
  which runs InProcessCronScheduler even with zero messaging adapters.
- The job itself is a no_agent watchdog script (one per agent,
  e.g. `profiles/<name>/scripts/mnemosyne-sync.py`): silent exit 0
  on success; prints an alert on rc!=0, tracebacks, or nonzero
  conflicts/failed counts. Watch out: the sync CLI prints
  "Conflicts: 0" on every healthy run, so keyword-matching "conflict"
  or "error" as an alert trigger always trips (use regexes for
  nonzero counts only).
- Windows machines must use `.py` scripts (the runner resolves bash
  via WSL; no WSL distro = `execvpe(/bin/bash) failed` every tick).
- After any cron change, verify the job actually fired once:
  `ticker_heartbeat` freshness + `last_status: ok` in jobs.json.
  "Scheduled" state is not proof.
- VPS agents sync over loopback (`http://127.0.0.1:8765`); PC and
  laptop sync over tailnet HTTPS. Non-loopback remotes REQUIRE https.

### 7. Provisioning a new agent (recipe verified on Neo, 2026-08-17)

1. `mkdir -p <profile>/mnemosyne/data/shared` (owner = the agent user).
2. `mnemosyne sync-init --db-path <shared-db> --yes` with
   `HERMES_HOME`, model, and dim env set -> creates the surface
   marker + canonical session.
3. Ensure `<profile>/.env` has the four sync vars
   (`MNEMOSYNE_SYNC_REMOTE`, `MNEMOSYNE_SYNC_ENCRYPT=1`,
   `MNEMOSYNE_SYNC_TOKEN`, `MNEMOSYNE_SYNC_KEY`; fleet-shared values).
4. Set the adapter path: `hermes -p <name> config set
   memory.mnemosyne.shared_surface_path <profile>/mnemosyne/data/
   shared/mnemosyne.db` (the "unrecognized key" warning is expected;
   the mnemosyne adapter reads it anyway). Restart the agent's serve
   process -- a running adapter ignores config changes.
5. Install the sync watchdog script at
   `<profile>/scripts/mnemosyne-sync.py` (DB path adapted; key files
   and remote per machine class).
6. Headless: install the gateway (section 6). Desktop: nothing extra.
7. Register the job:
   `hermes -p <name> cron create "every 5m" inert-no-agent-job
   --name mnemosyne-sync --script mnemosyne-sync.py --no-agent
   --deliver local` (prompt is a POSITIONAL arg on the CLI and
   mandatory even for no_agent jobs; the value is inert).
8. Verify link by link: run the script once manually (rc=0, silent),
   confirm rows materialized in the new shared DB, confirm the relay
   event count is unchanged by a pull-only sync, then wait one 5-min
   window and confirm `last_run_at` + `last_status: ok` in jobs.json.

Neo went from zero to 18 working rows / full fleet knowledge in one
cycle with this recipe (2026-08-17). No new relay writes appear for
a pull-only agent, which is correct: only pushes create relay events.

### 8. Silent failure catalog (each failure lives at ONE link)

| Symptom | Link | Root cause and fix |
|:--|:--|:--|
| Facts written but relay stays empty | Write path | `shared_surface_path` unset -> shared tools silently write to `~/.mnemosyne/data/shared/mnemosyne.db` while cron syncs the profile DB -- two different files. Fix: config key + app restart. |
| Job "scheduled", never fires | Ticker | No process owns HERMES_HOME (app closed, or headless profile with no gateway). Fix: open app / install gateway. |
| "Last modified" old, store actually live | Relay | WAL mode: live data in `-wal`. Check `-wal` mtime. |
| False "384 vs 1024 mismatch" | CLI | Running `mnemosyne` without HERMES_HOME / model env resolves the base/default DB. Always export HERMES_HOME + model + dim. |
| CLI backed up a tiny phantom DB | CLI | Same resolution trap (`MNEMOSYNE_DATA_DIR` > HERMES_HOME > `~/.hermes`). "Original size 462,848" for a 12MB DB is the tell. |
| Duplicates: N, 0 accepted | Relay | Agent DB path points at the relay DB itself. |
| Watchdog always errors | Cron script | Keyword-matching "conflict"/"error" against healthy CLI output. Regex for nonzero counts only. |
| Backfill warnings every cycle | Vector space | A row embedded by an old-model process landed in a new-dim DB. Fleet-coordinated reindex + restart. |
| Shared facts older than 7 days vanish fleet-wide after any shared write | Write path (personal TTL leaking into the surface) | `BeamMemory._trim_working_memory` (`WORKING_MEMORY_TTL_HOURS=168`) runs on every `remember()`, including `mnemosyne_shared_remember`. The surface session `hermes_shared_surface` reuses the same class, so the personal-memory TTL evicts surface rows; the sync recovery path then turns the eviction into fleet-wide tombstones. Fix (fleet patch 2026-08-22, Suggi-approved): early return exempting session `hermes_shared_surface`, applied to all three venvs (VPS hermes-agent venv, PC, laptop), backups kept as `beam.py.orig-20260822-morpheus`. Upstream main still unpatched as of 2026-08-22. |

The phantom `~/.mnemosyne` husks and the install-era default-profile
DB (`~/.hermes/mnemosyne/`, 0 rows, no process using default
HERMES_HOME) were DELETED on 2026-08-17 after read-only verification
-- they are historical failure artifacts, not part of the live system.

2026-08-22 update: the TTL-trim row above was discovered live --
Morpheus's first shared write after a 7-day quiet period evicted 11 of
Link's facts and the resulting tombstones propagated before the fleet
was frozen. Recovery: the rows were restored from Neo's intact copy and
re-created through the relay; all four agents reconverged. The
trim-exemption patch was applied fleet-wide the same day, and an
upstream issue was filed on the mnemosyne repository.

## Implications

1. Verification is link-by-link, always: writer path (which file got
   the row?), ticker (heartbeat fresh?), relay (events growing for
   the right device_id?), pull path (rows materialized on every
   agent?). A single sync-log line proves one link, not the loop.
2. Provisioning a fleet agent is a checklist (section 7), not a
   judgment call. The recipe was proven end-to-end on Neo.
3. Any "is this stale?" question about a SQLite store starts with
   the `-wal` mtime and the process list, never the main-file mtime.
4. New agents get the fleet embedding model and the fleet relay --
   NEVER a per-agent model choice or a local relay. One vector
   space, one conduit.
5. Cheap health checks that answer most questions in one command:
   `SELECT COUNT(*) FROM working_memory` on every shared DB;
   `SELECT COUNT(*) FROM memory_events` on the relay; `sync_meta`
   rows on any agent; `ticker_heartbeat` mtime in every cron dir.

## Counter-evidence

This anatomy would be invalidated if:

- A fact written by the shared tools appeared in the relay WITHOUT a
  local profile-DB row (would break the "local working copy" model).
- A cron job fired with no process owning its HERMES_HOME (never
  observed; the dead-ticker failure is the exact opposite).
- Two agents on different embedding dimensions exchanged shared facts
  with full retrieval quality (observed instead: persistent backfill
  warnings until reindex).
- A pull-only agent's sync created relay events (observed: Neo's
  pull-only syncs left the relay event count unchanged at 31).
- A tombstone failed to propagate to convergence (observed: 0/0/0
  across all agents in the 2026-08-15 delete test).

## Cross-Links

- `research/insights/two-tier-fleet-memory-single-vector-space.md` --
  the WHY: two tiers, one vector space, ticker ownership.
- `research/reports/link-hermes-memory-system.md` -- the 5-layer
  personal memory architecture report (pre-fleet era).
- `reflections/2026-08-10_link_shared-memory-is-an-operations-problem.md` --
  the co-produced reflection on the original build.
- `logbook/queue.log` -- ENT-052, ENT-053 (sync + tombstone test),
  ENT-057 (Neo wiring): the event trail behind this anatomy.
- `governance/system-blueprint.md` -- org architecture.
