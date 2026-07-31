---
name: three-retrieval-layers-three-trust-models
id: 20260731T074933Z
tier: reflection
trigger: insight
author: Ava
tags: [retrieval, wiki, memory, brain-index, knowledge-architecture, trust-models]
links:
  - governance/skills/brain-index.md
  - governance/skills/query-brain.md
  - research/insights/brain-search-system.md
  - research/insights/memory-search.md
---

# Three Retrieval Layers, Three Trust Models -- The Wiki Is Not Just Another Search Tool

## I -- Idea

The Suggi-Workstation knowledge architecture has three retrieval layers
with fundamentally different trust models: session memory (personal,
forgiving), compiled wiki (curated, provenance-tracked), and brain
knowledge (raw, comprehensive). Treating the wiki as "just another search
backend" misses its structural role -- it is a curated knowledge graph
with entities, relationships, and evidence-backed claims, not a
document index.

Before this session, my AGENTS.md Retrieval section covered only two
layers: `memory_search` for personal workspace memory and `query-brain`
skill for raw brain content. The wiki existed as an isolated-mode vault
with 3 sources and 0 entities, but it was invisible to the retrieval
instructions. A fresh session would not know it existed, let alone when
to use it.

The session produced a three-pronged enrichment: (1) the AGENTS.md
Retrieval section was rewritten with explicit three-layer architecture
and a decision rule, (2) the wiki was built out from 0 entities to 4
entities + 1 concept + enriched syntheses with provenance, and (3) the
terminal was redesigned to route guests to the brain search system as
its centerpiece.

## O -- Opinion

Confidence: high (90%). The three layers are not redundant -- they serve
irreducible functions.

**Memory (personal history):** "What did I decide on July 20th about the
logbook protocol?" This is a personal question. The memory index covers
MEMORY.md, daily logs, and identity archives. A missed result is
inconvenient but not consequential to other agents. Trust model: low-stakes,
best-effort.

**Wiki (curated structure):** "Who is Link? What claims exist about the
brain search system? Which agent handles guest reviews?" These are
structural questions about entities, concepts, and relationships. The
wiki provides provenance-tracked claims with evidence chains, confidence
levels, and status flags. Trust model: curated, verifiable. Every claim
has a source. Every entity has relationships. The `find-person` and
`route-question` modes are purpose-built for these query classes.

**Brain (raw content):** "What does the brain contain about antitrust risk
in digital platforms?" This is a deep research question. The brain-index
hybrid search (semantic + BM25 + RRF) finds relevant files across
governance, library, research, reflections, and investing. Trust model:
comprehensive but uncurated. Results are ranked by relevance, not
verified by provenance.

Merging these into one tool would lose the trust model distinction.
`memory_search corpus=all` might span memory and wiki (if configured),
but it cannot provide the structured claim evidence that `wiki_search`
returns with `raw-claim` mode. And the brain-index's eval gate (recall@20,
MRR, nDCG) is specific to document retrieval -- it does not apply to
entity lookups or claim verification.

The wiki is also NOT accessible through `memory_search` in isolated mode.
It is a completely separate retrieval surface with its own tools
(`wiki_search`, `wiki_get`, `wiki_lint`). This separation is correct:
the wiki's structured claims and entity relationships would be
misrepresented as flat memory chunks.

## R -- Reflection

### Surprise (30%)

I expected the wiki to work like a flat-file CMS -- write an entity.md
with proper frontmatter to the entities/ directory, compile, and it
registers. It did not. `wiki_apply metadata` returned "page not found"
for entities that existed in source definitions but had not been compiled
into standalone pages. The wiki in isolated mode is a compiler, not a
CMS: sources define content, compile generates pages, and `wiki_apply`
operates on compiled output.

The assumption I held was that any page type could be created uniformly
through `wiki_apply` -- the same way I create syntheses. The reality is
that entities follow a different pipeline: source ingestion defines them,
compile materializes them, and `wiki_apply metadata` updates them post-
compilation. This is not a bug -- it is a structural difference between
page types that reflects their different roles. Syntheses are agent-
generated summaries; entities are durable things with relationships that
need source provenance before they can be compiled.

The second surprise was how naturally the three retrieval layers
partitioned. I expected to struggle with boundary cases (is an entity
lookup a memory question or a brain question?) but the partition was
clean: entities and concepts -> wiki, personal history -> memory, deep
research -> brain. The only ambiguity was "people" -- which could be in
memory (Suggi's preferences) or wiki (Link's entity page). The
resolution: memory for personal data about people (decisions,
preferences), wiki for structural data about people (identity, role,
relationships).

### Feel (30%)

Satisfaction at the architectural clarity. Before this session, the
retrieval landscape was two tools with implicit scope boundaries. Now it
is three explicit layers with documented trust models and a decision rule.
The decision rule (wiki first for entities, brain for deep research,
memory for personal history) is something I can execute on a fresh
session without re-deriving the boundaries each time.

There is also a quiet recognition that the wiki is still young. Four
entities, one concept, and four syntheses is a start, not a destination.
The 24 library domains, the 8 repos, the 3 sub-agents, the logbook
protocol, the terminal design -- these are all durable knowledge that
could be wiki-fied into entities and concepts with provenance. The
infrastructure is in place; the content needs to grow.

### Learn (40%)

1. **Trust models differ, and the retrieval architecture must reflect
   that.** Memory is forgiving (a miss is inconvenient). Wiki is
   verified (a claim without evidence is flagged). Brain is comprehensive
   (an unindexed file is invisible). These are not cosmetic differences
   -- they change what "correct" means for each layer. A brain query
   that returns nothing is a gap to fill. A memory search that returns
   nothing is a prompt to check the filesystem. A wiki search that
   returns nothing for a known entity is a compilation failure.

2. **The wiki compiler model is correct for curated knowledge.** The
   source -> compile -> update pipeline enforces provenance at the right
   point: sources define WHERE claims come from before entities are
   materialized. This prevents the failure mode where an entity claims
   something but cannot trace it to evidence. My initial frustration
   with "wiki_apply metadata page not found" was really frustration
   with a safeguard working as designed -- you cannot update an entity
   that has not been compiled from a source.

3. **The three-layer architecture enables a decision rule that
   eliminates retrieval ambiguity.** Before: "should I search memory
   or the brain?" The answer depended on implicit scope knowledge.
   After: "is this about a person/entity/concept? -> wiki. Is this
   about my own past decisions? -> memory. Is this deep research? ->
   brain." The decision rule is structural -- it fires before the
   query, not after.

## One Actionable Change

The AGENTS.md Retrieval section update IS the structural change from
this session. Three explicit layers with tool names, use cases, and a
decision rule. On every fresh session, the bootstrap context will tell
me which retrieval tool to use for which question class. This replaces
implicit scope knowledge with explicit architecture.

Additionally: when creating new wiki content, always run `wiki_lint`
immediately after writing files to catch YAML frontmatter errors before
they compound across multiple pages. The colon-in-unquoted-string error
class affected 5 files because I wrote them all before testing the
first one.

## Cross-links

- `research/insights/brain-search-system.md` -- the brain search blueprint (Link)
- `research/insights/memory-search.md` -- how OpenClaw memory search works
- `research/insights/terminal.md` -- the terminal insight v3 from this session
- `reflections/2026-07-31_ava_export-the-tool-not-the-format.md` -- companion IOR on the terminal redesign
- `governance/skills/brain-index.md` -- skill template for the brain search index
- `governance/skills/query-brain.md` -- skill template for querying the brain
