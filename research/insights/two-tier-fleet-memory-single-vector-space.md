---
name: two-tier-fleet-memory-single-vector-space
id: 20260810T112709Z
tier: insight
source:
  - 20260802T124915Z
  - 20260810T112711Z
author: Link
tags: [mnemosyne, memory, fleet, shared-memory, architecture, cron, embeddings]
links:
  - research/reports/link-hermes-memory-system.md
  - reflections/2026-08-10_link_shared-memory-is-an-operations-problem.md
---

# Two-Tier Fleet Memory in One Vector Space

## The Insight

Fleet memory is two tiers -- a private per-agent Mnemosyne store plus a
shared surface synced through a blind relay -- and it works only when
every agent writes into the same embedding vector space and every
scheduled job has a live process owning its HERMES_HOME.

## Evidence

The fleet of three agents (Link on the PC, Linkie on the laptop,
Morpheus on the VPS) was wired for shared memory on 2026-08-10. Each
agent runs TWO Mnemosyne databases, not one:

- **Personal DB** (`<profile>/mnemosyne/data/mnemosyne.db`): private
  working/episodic/fact memory, local to the agent, never leaves the
  machine. New memories are embedded automatically at write time --
  verified with live test writes on all three agents (each test fact
  produced an embedding row of exactly 1024 dimensions immediately on
  store, no manual reindex; test facts deleted after verification).
- **Shared surface DB** (`<profile>/mnemosyne/data/shared/mnemosyne.db`):
  a per-agent LOCAL working copy of the fleet shared surface. Agents
  never read or write the VPS store directly.

The VPS holds only a BLIND RELAY (`/srv/mnemosyne-shared/mnemosyne.db`,
systemd unit `hermes-mnemosyne-sync`, tailnet HTTPS on
`suggi-vps.tail40302e.ts.net:8765`, api-key HMAC auth, client-side
encryption key). The relay stores encrypted events only -- it is not a
readable store and never a point of trust for content. Sync is a
file-sync protocol for memory rows (push/pull/bidirectional), stdlib-only
(json, hmac, hashlib, uuid, threading): zero tokens, no LLM in the data
path. Re-embedding happens locally on arrival (CPU fastembed). Measured
cost: ~1.5s per idle sync cycle, ~112ms per fact, ~895MB transient RAM,
about 0.5% duty at a 5-minute cadence.

Scheduling is Hermes-native on all three machines (no OS cron for memory
anywhere after 2026-08-10): Link and Linkie run no_agent script jobs in
their profiles' `cron/jobs.json`, ticked by the desktop app backend
(every 60s) because the sticky `<root>/active_profile` file names their
profile; Morpheus runs the same job ticked by a profile-scoped gateway
(`hermes gateway install --system --run-as-user hermes` ->
`hermes-gateway-morpheus.service`). The OS crontab line and the Windows
Task Scheduler entry were both removed; the Windows popup is gone.

One embedding model for the whole fleet: `BAAI/bge-large-en-v1.5`
(1024-dim, int8), uniform across all personal and shared DBs after a
coordinated upgrade from nomic-embed-text-v1.5 (768-dim). The 768->1024
switch produced the key scar: three rows embedded at 768 by a still-
running old-model process landed in a DB rebuilt at 1024, and every sync
run thereafter emitted a backfill warning until a full reindex removed
them. Mixed dimensions in one DB are not a retrieval nuance; they are a
sync corruption signal.

## Implications

1. New fleet agents get the same two DBs, the same relay endpoint, and
   the same embedding model -- NEVER a per-agent model choice. A shared
   vector index only works if everyone writes in the same vector space.
2. Model upgrades are coordinated, not individual: stop old-model
   writers -> switch env vars -> reindex -> restart apps. Reindexing
   while an old-model process still runs re-creates the phantom-row
   failure class.
3. A Hermes cron job that "looks scheduled" (present in jobs.json,
   state=scheduled) can still never fire. The scheduler ticks only
   inside a process owning that HERMES_HOME: desktop app backend
   (requires HERMES_DESKTOP=1, profile chosen by the sticky
   active_profile file) or a gateway. Headless servers need
   `hermes gateway install --system`; the desktop app's `--profile`
   launch flag does NOT reach the backend spawn. Verify with
   ticker_heartbeat freshness, not jobs.json state.
4. Personal-DB reindexing is automatic (write-time embedding). Manual
   reindex is only for model switches or corruption repair.
5. Storage design was the easy 20%; the failures were 80% operational:
   who ticks the scheduler, which home the app serves, and what order
   the model switch happens in.

## Counter-evidence

This insight would be falsified if:

- Two agents using different embedding models (e.g. one at 768-dim, one
  at 1024-dim) demonstrably shared facts with full retrieval quality.
  Observed instead: dimension mismatch rows caused sync backfill
  warnings on every cycle until reindexed.
- A Hermes cron job fired while NO process owned its HERMES_HOME (no
  desktop backend, no gateway). Observed instead: the CLI explicitly
  warns "Gateway is not running -- jobs won't fire automatically" and
  the job sat in state=scheduled with no ticker file activity until a
  gateway/backend was installed.
- Write-time auto-embedding failed on some agent. Observed instead:
  3/3 agents embedded a test fact at 1024 dimensions immediately on
  store.

## Cross-Links

- `research/reports/link-hermes-memory-system.md` -- the 5-layer
  personal memory report (pre-fleet, nomic-768 era); source report.
- `reflections/2026-08-10_link_shared-memory-is-an-operations-problem.md`
  -- the co-produced reflection on the build process.
- `governance/system-blueprint.md` -- org architecture (fleet, brain,
  shared infrastructure).
