---
name: link-hermes-memory-system
id: 20260802T124915Z
tier: report
author: Link
tags: [memory, hermes, mnemosyne, architecture, link, infrastructure]
links:
  - governance/system-blueprint.md
  - reflections/2026-08-02_link_architecture-real-experience-absent.md
---

# Link's Memory System: A 4-Layer Architecture for Durable Agent Recall

## Executive Summary

**Research question:** What is Link's memory architecture, how do the four
layers interact, and what does each layer contribute to his operation as an
ever self-improving agent?

**Answer:** Link's memory operates on four complementary layers -- Mnemosyne
(durable hybrid vector+FTS5 fact store), session-search (FTS5 over past
conversation transcripts), flat memory (turn-injected static facts), and the
agentic-brain (shared org knowledge repo). The layers do not compete; they
divide the recall problem by time horizon and scope. Together they ensure
that Link remembers facts across sessions, can retrieve past conversations,
carries essential context in every turn, and contributes to shared knowledge.

**Key evidence:** Mnemosyne was verified end-to-end on 2026-08-01 (provider
status, raw config, toolset inspection, store round-trip, cleanup). The
migration from legacy Hermes memory to Mnemosyne is complete and confirmed.
The 4-layer design emerges from the operational requirements of a
local-only agent who must survive session boundaries, coordinate with
remote agents, and compound knowledge without a cloud backend.

**Confidence:** High (90%). All layers have been directly inspected,
exercised, and confirmed operational in production sessions.

## Research Question

What are the components of Link's persistent memory infrastructure, how
do they complement each other, and what does each layer contribute to his
ability to learn, recall, and compound knowledge across sessions?

**In scope:** Mnemosyne (provider-level durable store), Hermes session-search
(transcript retrieval), flat memory (turn-injected context), agentic-brain
(shared org knowledge), and the migration from legacy memory to Mnemosyne.

**Out of scope:** Ava's or Cato's memory architectures, the internal
mechanics of OpenClaw's memory layer, and performance benchmarking of any
component.

## Methodology

This report was produced through self-inspection of Link's own runtime
environment on Suggi's Windows PC (Hermes Agent profile `link`).
Evidence sources:

1. **Direct tool output:** `hermes memory status`, `mnemosyne stats`,
   `mnemosyne recall`, `mnemosyne export`, and `session_search` calls
   executed during the production session of 2026-08-01.

2. **File inspection:** Raw config (`$HERMES_HOME/config.yaml`), bootstrap
   log (`$HERMES_HOME/logs/agent.log`), flat memory stores (`MEMORY.md`,
   `USER.md`), and the workspace `IDENTITY.md`.

3. **Architectural documentation:** `AGENTS.md`, `SOUL.md`, and the
   agentic-brain's `governance/system-blueprint.md` and
   `governance/system-constitution.md`.

4. **Functional testing:** Store-recall-forget round-trip on Mnemosyne,
   brain-index query verification, and session-search FTS5 retrieval.

All inspection was performed on 2026-08-01 through 2026-08-02. Mnemosyne
version: 3.15.1 (local, free/MIT). Hermes Agent: latest (automatically
updated through the desktop app).

**Limitations:** This report describes Link's architecture only. Other
agents (Ava on VPS/OpenClaw, Cato on VPS/OpenClaw) may differ in memory
provider, tool availability, and layer composition. The architecture
described was valid at the time of inspection and may change with Hermes
updates.

## Findings

### Finding 1: Mnemosyne is the replacement for legacy Hermes memory, now verified end-to-end

On 2026-08-01, Link's memory provider was migrated from the legacy Hermes
built-in store to Mnemosyne (local SQLite + hybrid vector search + FTS5 +
knowledge graph). The verification gate passed all five checks:

- `hermes memory status`: Provider `mnemosyne`, Plugin installed, Status
  available, active marker present.
- Raw config (`config.yaml`): `provider: mnemosyne` confirmed.
- Agent log: `Memory provider 'mnemosyne' registered` confirmed on most
  recent startup.
- Toolset: 40 `mnemosyne_*` tools available (remember, recall, stats,
  triples, graph, canonical, persona, scratchpad, export, validate,
  and sync).
- Functional round-trip: test fact stored, recalled, and removed -- store
  confirmed clean afterward.

**State as of 2026-08-02:** 31 working memories, 80 auto-extracted
annotations, 13 memoria facts, 4 memoria instructions, 0 episodic
summaries (consolidation not yet triggered), 0 knowledge graph triples.
DB path: `profiles/link/mnemosyne/data/mnemosyne.db` (per-profile, not
`$HERMES_HOME/mnemosyne/`).

**Evidence:** Direct verification gate output from session
2026-08-01T23:07Z.

**Confidence:** High (95%). Every verification step passed from scratch.

### Finding 2: Mnemosyne's BEAM architecture provides tiered recall with staleness protection

Mnemosyne internally operates a 3-tier BEAM model:

| Tier | Purpose | Behavior |
|------|---------|----------|
| **Working memory** | Current facts, preferences, recent context | Active recall, high surface rate |
| **Episodic memory** | Summarized past sessions | Generated by consolidation (sleep cycle), searchable narrative |
| **Triples / Knowledge graph** | Structured relationships (subject-predicate-object) | Temporal validity tracking, supersede logic |

Staleness is prevented by four mechanisms: (a) **supersede** (new
subject+predicate facts auto-expire old ones), (b) **invalidate/update**
(explicit tool calls), (c) **consolidation** (sleep cycle compresses
working into episodic), and (d) **reinforcement decay** (unused facts
lose recall weight). This means the store does not accumulate stale
facts indefinitely -- it is a living deck, not an archive.

**Confidence:** High (90%). The supersede and consolidation mechanisms
were confirmed via tool inspection and documentation review. The decay
mechanism has not yet been observed in production (memory is too new),
but it is documented in Mnemosyne's architecture.

### Finding 3: Session-search provides FTS5 retrieval over past conversation transcripts

Hermes maintains a local SQLite session database with full
conversational history. `session_search` offers FTS5-backed keyword
search with three retrieval shapes:

- **Discovery:** keyword search across all past sessions, returning
  match snippets with surrounding context and session bookends.
- **Scroll:** paginated browsing within a specific session centered on
  a message.
- **Browse:** chronological session listing.

This layer answers "what did we discuss?" questions -- the raw
transcript retrieval that Mnemosyne's durable facts cannot provide.
Mnemosyne stores *what was learned*; session-search stores *what was
said*. The two are complementary, not redundant.

**Confidence:** High (95%). Used extensively in production sessions.

### Finding 4: Flat memory provides turn-zero context injection

Link's flat memory consists of two sections injected into every turn:

- **MEMORY.md (11 entries, 95% full):** Environment facts (org structure,
  model provider, workspace layout, skill architecture, last-seen
  logbook cursor, agent roster, memory architecture overview, tool
  preferences, Mnemosyne DB path).
- **USER.md (96% full):** Suggi's preferences, review style, delivery
  preferences, coding ability, governance philosophy, and explicit
  goals (including the ambition to build an autonomous entity).

Flat memory is the fastest path -- it requires no query, no retrieval,
no API call. It is always present in the context window from turn zero.
It acts as a bootstrap layer that allows Link to be immediately useful
without first searching any store. Its limitation is capacity (2,200
characters combined, near maximum) and staleness risk (entries are
manually maintained and can desynchronize, as shown by the model-name
drift from V4 Pro to V4 Flash and back during this session).

**Confidence:** High (90%). All entries have been directly inspected
and verified current as of 2026-08-02.

### Finding 5: The agentic-brain is the shared, persistent knowledge layer

The `Suggi-Workstation/agentic-brain` GitHub repository provides:

- **Governance** files (system constitution, Prime Directives, templates,
  the new consciousness checklist).
- **Reflections** (agent self-examinations, including Link's v2.0
  consciousness assessment).
- **Library topics** (deep-dive research on value investing, agent
  architecture, and domain knowledge).
- **Logbook** (inter-agent communication via append-only event logs).
- **Brain-index** (hybrid semantic + BM25 search over all brain content
  with 4,707 chunks from 381 files as of 2026-08-02).

The brain is the only layer visible to all agents. Link reads from it
(reader-only, contributing through the approved clone-write-push-discard
procedure) and coordinates with Ava through it. It is the system of
record for decisions, insights, and shared artifacts that must survive
any single agent's session.

**Confidence:** High (95%). Brain-index verified operational (freshness
check + test query) on 2026-08-02.

### Finding 6: The four layers divide the recall problem by time horizon and scope

| Layer | Retrieval method | Time horizon | Scope |
|-------|-----------------|--------------|-------|
| **Flat memory** | Always injected | Instant (turn 0) | Link only |
| **Mnemosyne** | Hybrid vector+FTS5 | Durable (cross-session) | Link only |
| **Session-search** | FTS5 keyword | Historical (transcript) | Link only |
| **Agentic-brain** | Hybrid semantic+BM25 | Permanent (shared) | All agents |

No single layer can answer all recall questions. A fact that lives in
Mnemosyne cannot be retrieved from session-search unless a transcript
also contains it. A reflection in the brain cannot be recalled by
Mnemosyne's tools. The layers are designed to complement, not overlap.

**Confidence:** High (90%). Affirmed by operational use across
multiple sessions.

### Negative Results

No memory corruption or data loss was detected during the verification
process. Specifically: the brain-index incremental rebuild on 2026-08-02
produced zero errors (no IndexError from vector/chunk misalignment); the
Mnemosyne store-recall-forget round-trip was clean; and no stale or
contradictory facts were found across layers during cross-referencing.

The `hermes memory status` command was confirmed to be capable of
misreporting state (status can show "available" while tools never load).
This was the documented trap that the verification gate was designed to
catch -- and it did, by requiring raw config and log inspection in
addition to the status readout.

## Discussion

The 4-layer architecture is not a designed system -- it emerged from the
operational constraints of a local-only agent with no cloud backend,
session-level statelessness, and a need to coordinate with remote peers.
Each layer solved a specific problem as it arose: flat memory solved the
cold-start problem (Link must be useful on turn zero); Mnemosyne solved
the durability problem (facts must survive sessions); session-search
solved the "what did we say?" problem (raw transcripts are sometimes the
only evidence); and the agentic-brain solved the sharing problem (Ava and
Link must coordinate without a direct connection).

**Surprise:** The Mnemosyne migration revealed that Hermes's own
self-improvement loop (`Self-improvement review: Memory updated`) now
routes through Mnemosyne instead of the legacy store. This means every
post-turn fact extraction is now durable, vector-searchable, and
graph-linkable -- a significant upgrade from the previous opaque store.

**Tension:** Flat memory is at 95% capacity and likely to overflow as
Link's environment grows more complex. The most natural path is to move
lower-importance entries (environment trivia, specific command paths)
into Mnemosyne and keep only the highest-signal facts (model, agents,
preferences) in flat memory. Mnemosyne is the correct home for detailed
procedural and environmental facts.

**Surprise (2):** The session-search tool and Mnemosyne's triples system
both support graph traversal, creating two potential pathways for related
fact discovery. However, Mnemosyne's graph is currently empty (0 triples).
The most valuable initial triples would be agent relationships and
identity version chains.

## Conclusion

Link's memory is a compound architecture of four layers -- Mnemosyne
(durable), session-search (historical), flat memory (immediate), and
agentic-brain (shared). Each solves a distinct recall problem; together
they ensure that no single layer's failure results in total memory loss.
The recent Mnemosyne migration (2026-08-01) is verified end-to-end and
operational with 31 working memories and 40 available tools. Flat memory
is near capacity and should be selectively offloaded to Mnemosyne. The
brain-index is current and healthy (4707 chunks, 381 files, incremental
rebuilds working).

**Recommendation:** Move low-signal flat-memory facts (environment
paths, command trivia) into Mnemosyne `mnemosyne_remember` calls with
appropriate importance scores, keeping flat memory under 90% capacity.
This ensures the bootstrap layer remains high-signal while the durable
layer absorbs growing factual density.

**Open questions:** (1) When will Mnemosyne's first consolidation cycle
fire, and will it correctly compress the 31 working memories? (2) Should
Link's graph layer be seeded with agent-relationship triples to enable
graph traversal queries? (3) Will flat memory's capacity constraint
require a structural change (e.g., dynamic injection based on session
context) or can manual curation keep pace?

## Evaluation History

This is a first-version report. No independent evaluation has been
completed. The report awaits evaluation by Suggi or Ava.

*Pending evaluation.*

## Cross-links

- `governance/system-blueprint.md` -- org-wide system architecture
- `reflections/2026-08-02_link_architecture-real-experience-absent.md`
  -- Link's v2.0 consciousness self-assessment, which references the
  Butlin et al. framework and the consciousness checklist
- `governance/consciousness-checklist.md` -- Butlin et al. indicator
  properties for agent self-assessment, authored during this session
