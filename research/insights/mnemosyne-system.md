---
name: mnemosyne-system
id: 20260817T123124Z
tier: insight
source:
  - 20260810T112709Z
  - 20260810T112711Z
  - 20260802T124915Z
author: Link
updated_by: Morpheus
updated: 20260828T053401Z
tags: [mnemosyne, memory, fleet, shared-memory, architecture, cron, embeddings, canonical, persona, episodic-publish]
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
from a single "sync succeeded" report. Since 2026-08-28 the personal tier
is not just a store but a full cognitive stack (canonical identity, persona
anchors, fact graph, validation), and the shared tier carries both fleet
metadata and distilled cross-agent knowledge via the episodic publisher.

## Evidence

This document is the operational anatomy of the fleet memory system as
of 2026-08-28: every path, every component, the full data flow, the
provisioning recipe, and the failure catalog. It complements
`two-tier-fleet-memory-single-vector-space` (the realization of WHY the
system is shaped this way) with the WHAT/HOW mechanics, verified live
on the fleet (Link, Linkie, Morpheus, Neo, Atlas, and the three
runners).

### 1. Three memory scopes -- never mix them

Fleet knowledge lives in exactly three places. Each has one job.

| Scope | What goes there | Writer | Sync | Reader |
|:--|:--|:--|:--|:--|
| Personal Mnemosyne | Private experience, session learnings, extracted facts, identity slots, persona anchors | Automatic (`mnemosyne_*` tools) | Never leaves the machine (EXCEPT distilled episodes, see section 5b) | The agent alone |
| Shared surface DB | Cross-agent stable facts (meta, preference, correction, identity) + distilled fleet knowledge | Deliberate (`mnemosyne_shared_*` tools) + episodic-publish cron | 5-min cron via blind relay | All fleet agents |
| Agentic-brain | Governance, library, insights, proposals | Manual (write-* skills) | Git watcher on the VPS | Everyone, indexed |

A personal fact never syncs raw. A shared fact is fleet-public by
design. Governance knowledge never enters either DB. (Source:
20260810T112709Z.)

### 2. Personal Mnemosyne (the private tier -- full stack since 2026-08-28)

One SQLite DB per agent at
`<profile>/mnemosyne/data/mnemosyne.db`. Hybrid retrieval: dense vectors
(sqlite-vec) + FTS5 full-text + importance-weighted recall, all inside
the BEAM model (working / episodic / fact triples). On top sit FIVE
active layers:

| Layer | Tool | What it holds | Since |
|:--|:--|:--|:--|
| Working memory | `mnemosyne_remember` / `mnemosyne_recall` | Hot context, auto-injected each turn, TTL 168h | birth |
| Episodic memory | `mnemosyne_sleep` (auto consolidation) | Compressed summaries of stale working memories | birth |
| Facts + knowledge graph | `mnemosyne_remember(extract=True, extract_entities=True)` | LLM-extracted SPO facts, dates, entities; auto graph edges | 2026-08-28 (policy active) |
| Canonical slots | `mnemosyne_remember_canonical` | One current value per (owner, category, name) -- identity cards that cannot self-contradict; restating = no-op, changing = supersede-with-history | 2026-08-28 (seeded all agents) |
| Persona tier (L3) | `mnemosyne_persona_promote` (tier=permanent) | Always-injected anchors independent of recall ranking -- owner, ASCII rule, prime directives, agent-specific anchors; decay via reinforcement, max ~5-10 rows | 2026-08-28 (seeded all agents) |
| Validation | `mnemosyne_validate` (attest/update/invalidate) | Collaborative fixes: contradiction -> fix or invalidate, never stack duplicates | 2026-08-28 (policy active) |

Veracity discipline: `stated` (Suggi said it), `tool` (tool output),
`inferred` (agent reasoning). Durable facts never `unknown`.

Fleet sizes (2026-08-28): Morpheus 624 working / 75 episodic / 247
facts / 6 canonical / 4 persona; Neo 83 / 10 / 31 / 10 / 4; Atlas 44 /
0 / 16 / 5 / 4. Runners (library/investment/research) have private
Mnemosyne (2026-08-28) with canonical-lite + persona-lite seeds; their
crons stay paused unless activated.

Embedding model is fleet-locked: `BAAI/bge-large-en-v1.5`, 1024
dimensions, set in every profile `.env`
(`MNEMOSYNE_EMBEDDING_MODEL` + `MNEMOSYNE_EMBEDDING_DIM=1024`) AND in
the VPS systemd units. One vector space for the whole fleet; mixed
dimensions are a corruption signal, not a retrieval nuance.

KNOWN LIMIT (verified 2026-08-28): memory banks (per-domain isolation,
`mnemosyne bank create`) are CLI/SDK-only. The Hermes plugin tools
(remember/recall) expose no `bank` parameter -- creating banks would
produce isolated DBs no Hermes tool can write to. Domain isolation is
therefore NOT active; if ever needed, request bank exposure upstream
or use `profile_isolation` (one bank per profile).

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
- Device IDs: Link = `device-99dc8807`, Linkie = `device-0ec2c42d`,
  Morpheus = `device-aacc572b`, Neo = `device-6f7d8d51` (verified
  2026-08-17). New agents get a device ID at first sync-init.
- Content: fleet-stable metadata written deliberately (kinds: meta |
  preference | correction | identity) PLUS distilled knowledge rows
  published automatically by the episodic publisher (section 5b).
  Fleet row counts converge identical on every agent (2026-08-28:
  45 rows / 18 published episodes on Morpheus, Neo, Atlas alike).

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
- The relay is a conduit, NOT a store. Verified 2026-08-28: 91 rows in
  `memory_events` (ciphertext), ZERO rows in `working_memory` /
  `memories`. Its schema tables exist but are never populated.
- COROLLARY (scar): never point an agent's shared-DB path at the
  relay DB. A DB that is both relay and client reports "Duplicates: N"
  and never materializes content.
- STALENESS TRAP: the relay main DB's mtime means nothing. SQLite WAL
  mode writes live data to `mnemosyne.db-wal`; the main file only
  advances at checkpoint. Always check `-wal` mtime before calling a
  store "stale". (This trap drove the Aug 16-17 audit that produced
  this document.)

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

### 5b. The episodic publisher (distilled knowledge distribution, since 2026-08-28)

The sync engine scopes to `working_memory` only -- upstream design.
Episodic summaries do NOT travel by the native protocol. The fleet's
solution is a publisher layer, not a sync-engine fork:

- Script: `<profile>/scripts/episodic-publish.py` (identical copy per
  core agent).
- Reads the agent's PRIVATE `episodic_memory`, keeps only distilled
  classes -- content starting with `[fact]`, `[insight]`,
  `[correction]`, `[preference]`, `[lesson]`, `[decision]`. Raw
  `[conversation]` compressions and `[builtin_memory_memory]`
  operational rows are EXCLUDED (quality gate: the shared surface
  carries stable knowledge, not session noise).
- Writes each surviving episode into the agent's shared surface as
  `Distilled (<agent>): <content>` with metadata
  `{"episodic_id": ..., "source_agent": ..., "published_by":
  "episodic-publish"}` -- scope global, importance preserved.
- Dedup: rows whose `metadata_json.episodic_id` already exists on the
  surface are skipped. Idempotent across reruns.
- From there the NORMAL 5-min relay sync distributes the rows
  fleet-wide. No fork, no protocol change, full auditability.
- Cron: `episodic-publish` job, every 6h, no_agent, per core agent
  (morpheus/neo/atlas). The script derives the profile from
  HERMES_HOME, so one script file serves all.
- First run (2026-08-28): published 15 Morpheus + 3 Neo distilled
  episodes; every agent converged at 18 published rows each within
  one sync cycle. Min-importance threshold 0.6 (matches what sleep
  consolidation produces).

The effect: each agent's private lessons become fleet-visible
knowledge automatically, while the private tier keeps the raw
experience. Personal stays personal; the DISTILLATE travels.

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
- Headless profiles (Morpheus, Neo, Atlas on the VPS): `hermes serve`
  does NOT tick. Each profile needs a gateway:
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
- SCAR (2026-08-28, Atlas): `hermes cron create` does NOT set
  no_agent -- a script job created without the flag runs as a full
  agent (token cost + wrong behavior). After create, run
  `hermes cron edit <id> --no-agent` and confirm in jobs.json.

### 7. Provisioning a new agent (recipe verified on Neo 2026-08-17, Atlas 2026-08-28)

1. `mkdir -p <profile>/mnemosyne/data/shared` (owner = the agent user).
   The directory alone is NOT a DB.
2. `mnemosyne sync-init --db-path <shared-db> --yes` with
   `HERMES_HOME`, model, and dim env set -> creates the surface
   marker + canonical session. SCAR (Atlas 2026-08-28): skipping
   this produces "surface DB is not initialized" on the first sync
   tick, one tick after activation -- init at birth, verify manually
   once before trusting the cron.
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
7. Register the jobs:
   `hermes -p <name> cron create "every 5m" inert-no-agent-job
   --name mnemosyne-sync --script mnemosyne-sync.py --no-agent
   --deliver local` (prompt is a POSITIONAL arg on the CLI and
   mandatory even for no_agent jobs; the value is inert), then
   `hermes cron edit <id> --no-agent` (see scar, section 6).
   Core agents ALSO get the episodic publisher: copy
   `episodic-publish.py` into the profile scripts dir, cron create
   "every 6h" ... --script episodic-publish.py, edit --no-agent.
8. Seed the identity layers (2026-08-28 standard): canonical slots
   (role / owner / platform / voice / domain scope) via
   `CanonicalStore(db_path=...).remember(profile, category, name,
   body)`; persona anchors (owner, ASCII rule, prime directives,
   agent-specific) via `BeamMemory.remember(source="persona",
   importance=0.95, scope="global")` then
   `PersonaAdapter(beam).handle_tool_call("mnemosyne_persona_promote",
   {"memory_id": ..., "tier": "permanent", ...})`. Runners get
   canonical-lite (role + owner) + persona-lite (owner + ASCII).
9. Verify link by link: run the sync script once manually (rc=0,
   silent), confirm rows materialized in the new shared DB, confirm
   the relay event count is unchanged by a pull-only sync, then wait
   one 5-min window and confirm `last_run_at` + `last_status: ok`
   in jobs.json.

Neo went from zero to full fleet knowledge in one cycle with this
recipe (2026-08-17). Atlas repeated it (2026-08-28) after the
sync-init gap was found and fixed.

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
| First sync tick fails "surface DB is not initialized" | Provisioning | Birth created the shared dir + config path but never ran `mnemosyne sync-init`. Fix: run sync-init, then one manual sync, then trust the cron (Atlas, 2026-08-28). |
| Episodic publisher floods shared surface with conversation noise | Publisher | Raw `[conversation]` compressions and operational `[builtin_memory_memory]` rows are fleet-unworthy. Fix: prefix filter keeps only `[fact]/[insight]/[correction]/[preference]/[lesson]/[decision]` (2026-08-28). |

The phantom `~/.mnemosyne` husks and the install-era default-profile
DB (`~/.hermes/mnemosyne/`, 0 rows, no process using default
HERMES_HOME) were DELETED on 2026-08-17 after read-only verification
-- they are historical failure artifacts, not part of the live system.

2026-08-22 update: the TTL-trim row above was discovered live --
Morpheus's first shared write after a 7-day quiet period evicted 11 of
Link's facts and the resulting tombstones propagated before the fleet
was frozen. Recovery: the rows were restored from Neo's intact copy and
re-created through the relay; all four agents reconverged. The
trim-exemption patch was applied fleet-wide the same day; the upstream
project remains unpatched (verified 2026-08-22), so any future package
upgrade on a machine will silently re-introduce this bug and must be
re-checked against this row before use.

## Implications

1. Verification is link-by-link, always: writer path (which file got
   the row?), ticker (heartbeat fresh?), relay (events growing for
   the right device_id?), pull path (rows materialized on every
   agent?). A single sync-log line proves one link, not the loop.
2. Provisioning a fleet agent is a checklist (section 7), not a
   judgment call. The recipe was proven end-to-end on Neo and Atlas.
3. Any "is this stale?" question about a SQLite store starts with
   the `-wal` mtime and the process list, never the main-file mtime.
4. New agents get the fleet embedding model and the fleet relay --
   NEVER a per-agent model choice or a local relay. One vector
   space, one conduit.
5. Cheap health checks that answer most questions in one command:
   `SELECT COUNT(*) FROM working_memory` on every shared DB;
   `SELECT COUNT(*) FROM memory_events` on the relay; `sync_meta`
   rows on any agent; `ticker_heartbeat` mtime in every cron dir.
6. The personal tier is now an identity system, not just a store:
   canonical slots prevent self-contradiction, persona anchors
   guarantee always-on injection, and the fact graph compounds
   structure automatically. Agents should prefer these layers over
   raw remembers for stable facts (usage map: the
   `mnemosyne-memory-override` skill, advanced features table).
7. Knowledge distribution is layered: raw experience stays private,
   the distillate travels. The episodic publisher is the only
   sanctioned path from private to shared, and its quality gate
   (prefix filter) is the boundary -- loosen it and the shared
   surface becomes conversation noise.

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
  pull-only syncs left the relay event count unchanged).
- A tombstone failed to propagate to convergence (observed: 0/0/0
  across all agents in the 2026-08-15 delete test).
- The episodic publisher pushed a `[conversation]` row to the shared
  surface (observed instead: the prefix filter excluded them in the
  2026-08-28 dry-run; 15+3 distilled rows published, zero noise).
- Persona anchors failed to inject into a fresh session (verified
  2026-08-28: persona rows present and injected on all seeded
  profiles).

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
- The `mnemosyne-memory-override` skill (per-profile) -- the usage
  map for the advanced personal-tier layers.
