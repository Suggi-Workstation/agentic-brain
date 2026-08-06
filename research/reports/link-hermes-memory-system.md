---
name: link-hermes-memory-system
id: 20260802T124915Z
tier: report
author: Link
tags: [memory, hermes, mnemosyne, architecture, link, infrastructure]
updated: 2026-08-06
links:
  - governance/system-blueprint.md
  - reflections/2026-08-02_link_architecture-real-experience-absent.md
---

# Link's Memory System: A 5-Layer Architecture for Durable Agent Recall

## Executive Summary

**Research question:** What is Link's memory architecture, how do the five
layers interact, and what does each layer contribute to his operation as an
ever self-improving agent?

**Answer:** Link's memory operates on five complementary layers -- Mnemosyne
(durable hybrid vector+FTS5 fact store, upgraded to nomic-embed-text-v1.5
768-dim on 2026-08-06), session-search (FTS5 over past conversation
transcripts), flat memory (turn-injected static facts), the LLM-wiki
(human-readable curated knowledge in Suggi's Obsidian vault, initialized
2026-08-06), and the agentic-brain (shared org knowledge repo). The layers
do not compete; they divide the recall problem by time horizon, scope, and
audience. Together they ensure that Link remembers facts across sessions,
can retrieve past conversations, carries essential context in every turn,
offers Suggi a browsable window into his knowledge, and contributes to
shared knowledge.

**Key evidence:** Mnemosyne was verified end-to-end on 2026-08-01 (provider
status, raw config, toolset inspection, store round-trip, cleanup). The
migration from legacy Hermes memory to Mnemosyne is complete and confirmed.
On 2026-08-06 the embedding model was upgraded from bge-small-en-v1.5
(384-dim) to nomic-ai/nomic-embed-text-v1.5 (768-dim), all memories were
reindexed, and the first consolidation cycle fired (4 episodic memories).
The 5-layer design emerges from the operational requirements of a
local-only agent who must survive session boundaries, coordinate with
remote agents, and compound knowledge without a cloud backend.

**Confidence:** High (90%). All layers have been directly inspected,
exercised, and confirmed operational in production sessions.

## Update 2026-08-06 (Revision 2)

This report was originally written 2026-08-02 describing a 4-layer system.
Revision 2 reflects the current system:

1. **Embedding upgrade:** Mnemosyne's embedding model changed from
   `BAAI/bge-small-en-v1.5` (384-dim, 512-token context) to
   `nomic-ai/nomic-embed-text-v1.5` (768-dim, 8192-token context). All
   101 working + 4 episodic memories reindexed; sqlite-vec tables rebuilt
   at 768. Better retrieval quality (MTEB ~62 vs ~56) and 16x context --
   long memories are no longer truncated at half a page.
2. **New env requirement:** the embeddings module freezes model + dim from
   env at import time (config.yaml is NOT consulted for them). Required in
   profile .env: `MNEMOSYNE_EMBEDDING_MODEL=nomic-ai/nomic-embed-text-v1.5`
   and `MNEMOSYNE_EMBEDDING_DIM=768`. Pitfall scarred: nomic is not in
   mnemosyne/core/embeddings.py `_get_embedding_dim` hardcoded table, so
   unknown models silently fall back to 384-dim -- `reindex --model` alone
   produces "Dimension mismatch (Expected 384, received 768)" and the vec
   tables must be dropped (load sqlite_vec/vec0.dll in python) before a
   successful reindex with both env vars set. CLI recall requires both env
   vars; without them the CLI falls back to keyword search with a clear
   self-heal message. After changing .env, the app must be restarted so the
   agent process re-imports the module.
3. **Fifth layer added: the LLM-wiki** in Suggi's Obsidian vault at
   `C:\AI Stuff\Vaults - Obsidian\link-brain` (WIKI_PATH and
   OBSIDIAN_VAULT_PATH in profile .env). Karpathy-pattern interlinked
   markdown: SCHEMA.md (domain rules, tag taxonomy), index.md (catalog),
   log.md (action log), raw/, entities/, concepts/, comparisons/,
   queries/. Orientation protocol every session: read SCHEMA -> index ->
   recent log, then search_files. Boundary (R8): wiki = curated personal
   knowledge for Suggi's eyes; agentic-brain = finished org artifacts. No
   duplication.
4. **Consolidation fired:** the first sleep-cycle consolidation produced
   4 episodic memories with int8 vectors (was 0 on 2026-08-02) -- BEAM
   working -> episodic compression is operational.
5. **Current store state (2026-08-06):** 104 working memories (50
   consolidated), 4 episodic, 37 memoria facts, 7 memoria instructions,
   7 memoria preferences, 0 knowledge-graph triples.

## Research Question

What are the components of Link's persistent memory infrastructure, how
do they complement each other, and what does each layer contribute to his
ability to learn, recall, and compound knowledge across sessions?

**In scope:** Mnemosyne (provider-level durable store), Hermes session-search
(transcript retrieval), flat memory (turn-injected context), the LLM-wiki
(Obsidian vault curated knowledge), agentic-brain (shared org knowledge),
and the migration from legacy memory to Mnemosyne.

**Out of scope:** Ava's or Cato's memory architectures, the internal
mechanics of OpenClaw's memory layer, and performance benchmarking of any
component.

## Methodology

This report was produced through self-inspection of Link's own runtime
environment on Suggi's Windows PC (Hermes Agent profile `link`).
Evidence sources:

1. **Direct tool output:** `hermes memory status`, `mnemosyne stats`,
   `mnemosyne recall`, `mnemosyne export`, and `session_search` calls
   executed during the production sessions of 2026-08-01 and 2026-08-06.

2. **File inspection:** Raw config (`$HERMES_HOME/config.yaml`), Mnemosyne
   config (`profiles/link/mnemosyne/config.yaml`), bootstrap log
   (`$HERMES_HOME/logs/agent.log`), flat memory stores (`MEMORY.md`,
   `USER.md`), profile `.env` (embedding env vars), and the workspace
   `IDENTITY.md`.

3. **Architectural documentation:** `AGENTS.md`, `SOUL.md`, and the
   agentic-brain's `governance/system-blueprint.md` and
   `governance/system-constitution.md`.

4. **Functional testing:** Store-recall-forget round-trip on Mnemosyne,
   reindex + vector-search verification at 768-dim (dense score 0.945 on
   a test query), brain-index query verification, and session-search FTS5
   retrieval.

All inspection was performed 2026-08-01 through 2026-08-06. Mnemosyne
version: 3.15.1 (local, free/MIT). Hermes Agent: v0.20.0 (2026.8.3).

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
`$HERMES_HOME/mnemosyne/`). As of 2026-08-06: 104 working memories (50
consolidated), 4 episodic, 37 memoria facts, 7 instructions, 7
preferences, 0 triples. The legacy `memory` tool is deprecated for
durable storage (mnemosyne-memory-override skill).

**Evidence:** Direct verification gate output from sessions
2026-08-01T23:07Z and 2026-08-06.

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

**Confidence:** High (90%). The first consolidation cycle fired on
2026-08-06 (4 episodic memories, int8 vectors), confirming the
working -> episodic path operationally. The decay mechanism has not yet
been observed in production (memory is too new), but it is documented in
Mnemosyne's architecture.

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

- **MEMORY.md (11 entries, 97% full):** Environment facts (org structure,
  model provider, workspace layout, skill architecture, last-seen
  logbook cursor, agent roster, memory architecture overview, tool
  preferences, Mnemosyne DB path, wiki path, VPS plan).
- **USER.md (98% full):** Suggi's preferences, review style, delivery
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
and verified current as of 2026-08-06.

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
  with 4,760 chunks from 387 files as of 2026-08-05).

The brain is the only layer visible to all agents. Link reads from it
(reader-only, contributing through the approved clone-write-push-discard
procedure) and coordinates with Ava through it. It is the system of
record for decisions, insights, and shared artifacts that must survive
any single agent's session.

**Confidence:** High (95%). Brain-index verified operational (freshness
check + test query) on 2026-08-05.

### Finding 6: The LLM-wiki provides a human-readable curated knowledge layer

On 2026-08-06 Link's knowledge gained a fifth layer: a Karpathy-pattern
LLM-wiki living inside Suggi's Obsidian vault at
`C:\AI Stuff\Vaults - Obsidian\link-brain` (WIKI_PATH and
OBSIDIAN_VAULT_PATH in profile .env; llm-wiki skill).

- **Structure:** SCHEMA.md (domain rules, tag taxonomy), index.md (page
  catalog -- the search entry point), log.md (append-only action log),
  raw/ (immutable sources), entities/, concepts/, comparisons/,
  queries/ (agent-curated interlinked pages with wikilinks and
  frontmatter).
- **Orientation protocol:** every session Link reads SCHEMA -> index ->
  recent log before any wiki operation, then searches via index +
  search_files. This prevents duplicates and missed cross-references.
- **Boundary (R8):** wiki = curated personal knowledge for Suggi's eyes;
  agentic-brain = finished org artifacts. No content duplication between
  the two; wiki pages reference brain artifacts, not copy them.
- **Why it exists:** unlike Mnemosyne (machine-native recall) and the
  brain (org-shared canonical), the wiki is human-readable and browsable
  in Obsidian's GUI with graph view -- Suggi's window into what Link has
  learned, and a durable working-knowledge layer independent of platform.

**Confidence:** High (90%). Initialized and verified 2026-08-06; seed
page concepts/memory-stack.md documents the architecture itself.

### Finding 7: The five layers divide the recall problem by time horizon, scope, and audience

| Layer | Retrieval method | Time horizon | Scope |
|-------|-----------------|--------------|-------|
| **Flat memory** | Always injected | Instant (turn 0) | Link only |
| **Mnemosyne** | Hybrid vector+FTS5 (nomic 768-dim) | Durable (cross-session) | Link only |
| **Session-search** | FTS5 keyword | Historical (transcript) | Link only |
| **LLM-wiki** | index + search_files | Curated (browsable) | Link + Suggi |
| **Agentic-brain** | Hybrid semantic+BM25 | Permanent (shared) | All agents |

No single layer can answer all recall questions. A fact that lives in
Mnemosyne cannot be retrieved from session-search unless a transcript
also contains it. A reflection in the brain cannot be recalled by
Mnemosyne's tools. The wiki makes knowledge visible and browsable that
the machine layers keep opaque. The layers are designed to complement,
not overlap.

**Confidence:** High (90%). Affirmed by operational use across
multiple sessions.

### Negative Results

No memory corruption or data loss was detected during the verification
process. Specifically: the brain-index incremental rebuild on 2026-08-02
produced zero errors (no IndexError from vector/chunk misalignment); the
Mnemosyne store-recall-forget round-trip was clean; and no stale or
contradictory facts were found across layers during cross-referencing.

The 2026-08-06 embedding migration surfaced one genuine failure class:
unknown embedding models silently default to 384-dim in Mnemosyne's
hardcoded dimension table, causing sqlite-vec dimension mismatches.
Diagnosed, fixed (env vars + vec-table drop + reindex), and scarred into
the hermes-memory-providers skill.

The `hermes memory status` command was confirmed to be capable of
misreporting state (status can show "available" while tools never load).
This was the documented trap that the verification gate was designed to
catch -- and it did, by requiring raw config and log inspection in
addition to the status readout.

## Discussion

The 5-layer architecture is not a designed system -- it emerged from the
operational constraints of a local-only agent with no cloud backend,
session-level statelessness, and a need to coordinate with remote peers.
Each layer solved a specific problem as it arose: flat memory solved the
cold-start problem (Link must be useful on turn zero); Mnemosyne solved
the durability problem (facts must survive sessions); session-search
solved the "what did we say?" problem (raw transcripts are sometimes the
only evidence); the LLM-wiki solved the visibility problem (Suggi can
browse what Link knows); and the agentic-brain solved the sharing problem
(Ava and Link must coordinate without a direct connection).

**Surprise:** The Mnemosyne migration revealed that Hermes's own
self-improvement loop (`Self-improvement review: Memory updated`) now
routes through Mnemosyne instead of the legacy store. This means every
post-turn fact extraction is now durable, vector-searchable, and
graph-linkable -- a significant upgrade from the previous opaque store.

**Tension:** Flat memory is at 97% capacity and likely to overflow as
Link's environment grows more complex. The most natural path is to move
lower-importance entries (environment trivia, specific command paths)
into Mnemosyne and keep only the highest-signal facts (model, agents,
preferences) in flat memory. Mnemosyne is the correct home for detailed
procedural and environmental facts.

**Surprise (2):** The session-search tool and Mnemosyne's triples system
both support graph traversal, creating two potential pathways for related
fact discovery. However, Mnemosyne's graph is still empty (0 triples).
The most valuable initial triples would be agent relationships and
identity version chains.

**Surprise (3):** The embedding upgrade surfaced a real infrastructure
lesson: Mnemosyne's dimension table is hardcoded and silently wrong for
newer models. The fix (env override) works, but a future Mnemosyne
release should auto-detect dimensions from the model. Scarred into the
memory-providers skill for all future upgrades.

## Conclusion

Link's memory is a compound architecture of five layers -- Mnemosyne
(durable), session-search (historical), flat memory (immediate), the
LLM-wiki (curated, human-readable), and agentic-brain (shared). Each
solves a distinct recall problem; together they ensure that no single
layer's failure results in total memory loss. The Mnemosyne migration
(2026-08-01) is verified end-to-end; the embedding upgrade to
nomic-embed-text-v1.5 (768-dim, 2026-08-06) is complete with all
memories reindexed; the wiki layer is initialized and operational; and
the first consolidation cycle has fired (4 episodic memories). Flat
memory is near capacity and should be selectively offloaded to Mnemosyne.
The brain-index is current and healthy (4760 chunks, 387 files,
incremental rebuilds working).

**Recommendation:** Move low-signal flat-memory facts (environment
paths, command trivia) into Mnemosyne `mnemosyne_remember` calls with
appropriate importance scores, keeping flat memory under 90% capacity.
This ensures the bootstrap layer remains high-signal while the durable
layer absorbs growing factual density. Seed the wiki with session
insights (one page per durable insight, minimum 2 wikilinks) so it
compounds alongside Mnemosyne.

**Open questions:** (1) Should the shared VPS brain-index service (planned
for the netcup RS 4000 G12) index the wiki vault too, giving the wiki
hybrid semantic search once it exceeds a few hundred pages? (2) Should
Link's graph layer be seeded with agent-relationship triples to enable
graph traversal queries? (3) Will flat memory's capacity constraint
require a structural change (e.g., dynamic injection based on session
context) or can manual curation keep pace?

## Evaluation History

This is a first-version report, revised 2026-08-06 to reflect the
5-layer system. No independent evaluation has been completed. The report
awaits evaluation by Suggi or Ava.

*Pending evaluation.*

## Cross-links

- `governance/system-blueprint.md` -- org-wide system architecture
- `reflections/2026-08-02_link_architecture-real-experience-absent.md`
  -- Link's v2.0 consciousness self-assessment, which references the
  Butlin et al. framework and the consciousness checklist
- `governance/consciousness-checklist.md` -- Butlin et al. indicator
  properties for agent self-assessment, authored during this session
