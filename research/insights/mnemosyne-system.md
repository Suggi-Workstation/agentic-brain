---
name: mnemosyne-system
id: 20260817T123124Z
tier: insight
source:
  - 20260810T112709Z
  - 20260810T112711Z
  - 20260802T124915Z
author: Morpheus
tags: [mnemosyne, memory, fleet, shared-memory, architecture, cron, embeddings, canonical, persona, episodic-publish]
links:
  - research/insights/two-tier-fleet-memory-single-vector-space.md
  - research/reports/link-hermes-memory-system.md
  - reflections/2026-08-10_link_shared-memory-is-an-operations-problem.md
  - logbook/queue.log
  - governance/system-blueprint.md
---

# Mnemosyne System Blueprint

## The Insight

Memory creation, consolidation, publication, synchronization, and recall
are separate stages. A successful cron run proves only that its script
finished, not that useful knowledge reached another agent. Verify the
intended records at each boundary.

## Scope

This describes the deployed VPS design for Morpheus, Neo, and Atlas.
Other fleet clients can participate in shared sync; their current desktop
runtime is outside this verification scope. Machine-specific access and
deployment details belong in private operational references, not here.

| Store | Purpose | Boundary |
|:--|:--|:--|
| `<profile>/mnemosyne/data/mnemosyne.db` | Private working memories, episodes, facts, canonical slots, persona anchors | Per agent; the private database is not synchronized |
| `<profile>/mnemosyne/data/shared/mnemosyne.db` | Local materialized copy of fleet-shared knowledge | Explicit shared writes plus selected published episodes |
| Agentic-brain repository | Reviewed governance and knowledge artifacts | Git/watchers and repository search, separate from Mnemosyne |

Sharing is deliberate at the system boundary. The publisher's category
filter is not a confidentiality detector: sensitive material mislabeled
as a shareable fact can still pass it.

## End-to-End Flow

```text
Conversation / explicit private-memory tools
  -> private working memory
  -> gated consolidation -> private episodic summaries
  -> episodic-publish selection --------+
                                       |
Explicit shared-memory tools ----------+-> local shared working memory
                                             |
                                   sync discovers local changes
                                             |
                                    encrypted event relay
                                             |
                                  recipient materializes changes
                                             |
                                    shared / merged recall
```

### 1. Capture and organize privately

The Hermes memory provider captures permitted turns and accepts explicit
`mnemosyne_*` writes. Capture is subject to role and context filters; it
is not an unconditional copy of every message.

| Layer | Role |
|:--|:--|
| Working memory | Recent context and explicit facts; searchable with vector similarity, FTS5, importance, and optional recency weighting |
| Episodic memory | Consolidated summaries of eligible working memories |
| Facts and graph | Subject-predicate-object relationships, entities, and linked memories; extraction depends on the enabled extraction path |
| Canonical slots | One current value per owner/category/name, with superseded history |
| Persona | Promoted anchors injected independently of ordinary recall ranking |
| Validation | Attest, correct, or invalidate existing knowledge rather than accumulating contradictions |

Veracity records provenance (`stated`, `tool`, `inferred`, etc.); copying
a memory must not silently upgrade that provenance. All participating
clients use the fleet embedding model `BAAI/bge-large-en-v1.5` with 1024
dimensions. This is separate from the agent's chat model and from the
repository-search embedding service.

### 2. Consolidate into episodes

Mnemosyne's sleep path selects eligible unconsolidated working memories.
Automatic sleep is gated by memory volume, age, and a reflection budget;
session-end or explicit sleep can also invoke consolidation. It is not
the six-hour publishing cron.

Consolidation is additive: originals are marked consolidated, not
deleted. Consolidated working rows are exempt from ordinary working-memory
TTL trimming in the installed implementation.

When its summarization LLM is available, consolidation can use it.
Otherwise the installed fallback compresses source text and adds category
labels such as `[fact]`. A label is not proof of semantic distillation.
Inspect episode metadata (`llm_used`, consolidation method) and logs to
verify which path ran. Switching the chat model to Astra does not prove
that the separate summarization adapter is using Astra successfully.

### 3. Publish selected episodes

The native shared-sync path handles `working_memory`, not private
`episodic_memory`. The publisher bridges that boundary without modifying
the sync protocol.

`<profile>/scripts/episodic-publish.py` runs every six hours for Morpheus,
Neo, and Atlas. Each has its own runtime copy and databases; the code is
identical. The job has `no_agent: true`: Python does the copying, with no
chat-model call and no new summarization.

Publisher contract:

- Select nonempty, unexpired, nonsuperseded episodes with importance
  at least `0.6` and an approved prefix: `[fact]`, `[insight]`,
  `[correction]`, `[preference]`, `[lesson]`, or `[decision]`.
  Conversation and operational-memory prefixes stay private.
- Copy selected content into shared working memory, preserving importance,
  veracity, and expiry. Rows use session `hermes_shared_surface`, scope
  `global`, source `episodic_publish`, and `metadata_json` containing
  `source_agent`, `episodic_id`, and `published_by: episodic-publish`.
  The legacy display prefix `Distilled (<agent>):` is a label, not a
  guarantee that an LLM created the summary.
- Skip previously published `(source_agent, episodic_id)` pairs and
  exact-content collisions, including inactive copies. An unchanged rerun
  does not refresh timestamps or rewrite memories. Duplicate content in
  the same batch is copied once. A SQLite writer reservation protects the
  final collision check and insertion against concurrent sync/writes.
- Mark this agent's copies inactive when their source disappears,
  expires, is superseded, or leaves the allowed categories. Private
  memories and other agents' copies are untouched. Shorter source expiry
  is propagated; stricter shared expiry is never extended. The optional
  selection threshold affects new publication, not withdrawal.
- Fail visibly on database/schema, provenance, or write errors; verify
  new writes by reading them back. `--dry-run` reports planned actions
  without writing or printing private content.

This is publication, not continuous text mirroring. To replace a published
claim, invalidate/supersede its private source and publish a new corrected
episode. An inactive shared row prevents accidental republication. Hard
deletion removes that marker: invalidate the private source before
removing its shared copy, or an eligible source can be copied again.

### 4. Synchronize shared changes

Every five minutes, each participating profile's `mnemosyne-sync` job
runs its script in `no_agent` mode. It uses that profile's initialized
shared database, never the private database or the relay database.

At sync time the engine compares local working rows with its sync state.
New rows, changes (including `valid_until`), and deletions become events.
Clients encrypt the payloads; the relay stores and forwards those events
without materializing the plaintext shared working set. It is an encrypted
event store, not an agent's shared-memory database.

Recipients pull events after their saved cursor, materialize the rows,
and generate local retrieval embeddings. Deletions travel as tombstones;
publisher withdrawals travel as expiry updates. Convergence requires a
successful origin push followed by recipient pulls. Five-minute schedules
are not a guarantee of convergence within one cycle; offline clients catch
up after resuming.

### 5. Retrieve useful knowledge

`memory.mnemosyne.shared_surface_path` in Hermes configuration points the
provider at the same shared database that sync uses. With
`memory.mnemosyne.shared_surface_read: true`, explicit `mnemosyne_recall`
merges private/canonical results with shared results. Shared results are
tagged `bank: surface`; `mnemosyne_shared_recall` searches only that tier.

Automatic context prefetch is a different path: the installed provider
prefetches private/canonical memories and persona anchors. Do not infer
that every automatically injected context includes shared results.

## Runtime Ownership and Provisioning

- One user-level `hermes-gateway` service multiplexes the allowlisted VPS
  profiles' isolated cron registries. The unified Desktop serve process
  is separate. Do not install per-profile gateways for this design.
- Jobs live in `<profile>/cron/jobs.json`; execution requires a live
  scheduler. Verify gateway ownership, each profile's ticker heartbeat,
  and actual execution records, not merely an enabled schedule.
- A new shared participant needs an initialized surface database,
  aligned provider/sync paths, fleet embedding settings, and configured
  shared transport. A directory alone is not an initialized database.
- Register `mnemosyne-sync` and, where explicitly authorized, the
  publisher. Set `no_agent` explicitly and read it back. Do not enable
  shared publication for private-only runners by inheritance.
- Observe a real scheduled run and verify the intended row on recipients
  before treating a new participant as operational. This blueprint is
  not permission to install services or change profiles.

## Verification -- PASS or HALT

Before deployment or after relevant package upgrades, run the publisher
regressions and isolated installed-API integration test maintained in
Morpheus's workspace `scripts/`. Then verify the live data path.

- [ ] Scope: PASS if private and shared paths are distinct, profile-owned,
  and provider/sync paths agree; HALT on mismatched or uninitialized paths.
- [ ] Selection: PASS if allowed fresh fixtures publish and expired,
  superseded, conversation, and below-threshold fixtures do not; HALT if
  any exclusion is bypassed.
- [ ] Idempotence: PASS if reruns and exact-content collisions cause no
  rewrites, timestamp refreshes, or revival; HALT on any such mutation.
- [ ] Lifecycle: PASS if source withdrawal reaches only owned copies,
  shorter expiry propagates, and private/unrelated rows survive; HALT
  on stale active copies or collateral changes.
- [ ] Fail-closed behavior: PASS if schema/write failures return nonzero
  and dry-run leaves data unchanged; HALT on success-shaped failures.
- [ ] Runtime: PASS if script copies match, jobs remain script-only, and
  ticker/execution evidence is fresh; HALT if only the schedule is known.
- [ ] Distribution: PASS if exact IDs, content, provenance, and validity
  converge after successful sync; HALT if only row counts or exit codes
  match. Use live SQLite queries, not the main file's mtime in WAL mode.
- [ ] Retention: PASS if an old unrelated shared row survives a new shared
  write; HALT if private-memory TTL trimming evicts shared rows. The
  installed shared-session exemption is a required regression check.
- [ ] Model claims: PASS if claims of LLM distillation have episode/log
  evidence; HALT on inferring them from the chat model or prefix alone.

## References and Evidence Boundary

Implementation anchors: profile publisher and sync scripts; installed
Mnemosyne `core/beam.py` (remember, sleep, invalidate), `core/sync.py`
(mutation discovery and materialization), and the Hermes provider
`mnemosyne_hermes/__init__.py` (capture, prefetch, merged recall).

Verification scope: VPS core profiles, September 2026. Existing episodes
inspected during the audit recorded `llm_used=false`; successful
Astra-backed consolidation was not established by the publisher repair.
Historical incident counts and timings are not live architecture.

- `research/insights/two-tier-fleet-memory-single-vector-space.md` --
  rationale for private/shared separation and one vector space.
- `research/reports/link-hermes-memory-system.md` -- earlier personal
  memory architecture research.
- `reflections/2026-08-10_link_shared-memory-is-an-operations-problem.md` --
  original operational lessons.
- `governance/system-blueprint.md` -- organization architecture.
- `logbook/queue.log` and `logbook/errors.log` -- change history.
- The per-profile `mnemosyne-memory-override` skill -- memory-tool usage.
