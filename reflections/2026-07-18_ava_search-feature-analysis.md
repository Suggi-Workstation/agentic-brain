---
name: search-feature-analysis
id: 20260718T083044Z
tier: reflection
trigger: research
author: Ava
tags: [memory-search, brain-index, extraPaths, knowledge-base, architecture, comparison]
links:
  - research/proposals/brain-index-search-proposal.md
  - research/reports/living-memory-vs-openclaw-memory-search.md
  - research/insights/memory-search.md
  - reflections/2026-07-17_ava_living-memory-brain-index-future.md
---

# Two Search Systems, One Architecture -- Why extraPaths Cannot Replace the Brain-Index

## I -- Idea

Suggi asked whether the agentic-brain repo (or its `research/` and
`reflections/` folders) could be added to `memorySearch.extraPaths` to
give semantic search over the shared knowledge base. The question is
logical: if `extraPaths: ["identity"]` works for identity archives, why
not `extraPaths: ["../agentic-brain/research"]` for brain content? The
answer involves three technical constraints and three architectural
principles that together make a dedicated brain-index tool the correct
approach.

The existing `brain-index-search-proposal.md` (2026-07-17) already
analyzed this question and reached the same conclusion: the two systems
must stay separate. This reflection extends that analysis with the
concrete technical constraints discovered during this session's
`extraPaths` implementation, and validates the proposal's reasoning
against the current system state.

## O -- Opinion

Confidence: high (90%). The separation is correct for three reasons the
proposal already identified, plus two technical constraints revealed by
this session's implementation work.

### The proposal's three architectural reasons

1. **Trust models differ.** Session memory (daily logs, MEMORY.md) is
   personal and low-stakes -- a missed result is inconvenient. Brain
   content (library topics, governance, research) is shared and
   consequential -- a missed result is a research gap. The brain-index
   proposal mandates eval gates (recall@20, MRR, nDCG) and a freshness
   heartbeat specifically because the trust model is higher. memory_search
   has neither of these.

2. **Separation of concerns.** Mixing "what did I do yesterday?" with
   "what does the org know about digital platform regulation?" in one
   index produces noise in both directions. The query "template" would
   return daily log mentions of template work alongside the formal
   governance template files. The signal-to-noise ratio degrades with
   corpus size.

3. **Git refresh problem.** The AGENTS.md retrieval rules say "clone the
   brain temporarily, read, push changes, discard the clone." The
   brain-index needs a persistent local copy to stay fast. memory_search
   indexes a persistent workspace directory. extraPaths inherits this
   assumption -- the path must be stable and within the workspace scope.

### Two additional technical constraints from this session

4. **extraPaths is workspace-scoped.** The config schema confirms
   extraPaths takes workspace-relative paths. The agentic-brain is not
   in the workspace and must not be (workspace is mirrored to a public
   GitHub repo; the brain is a separate, larger repo). To use extraPaths,
   we would need to maintain a persistent clone of the brain inside the
   workspace -- violating both the workspace layout rules (research
   artifacts belong in the brain, not the workspace) and the git hygiene
   rules (two repos in one workspace creates commit confusion).

5. **Memory index rebuild cost at scale.** This session's extraPaths
   test added 8 small files (~15 new chunks) -- the reindex was
   instantaneous. Adding 5,000-50,000 brain files would produce a
   massive index. The brain-index proposal estimates 1.25 GB of vectors
   at 50K files. Every `memorySearch.extraPaths` change triggers a full
   reindex. The workspace memory index would need to be rebuilt every
   time the brain is pulled with new content. This couples the two
   systems in a way that makes each rebuild more expensive than the
   scheduled, incremental brain-index rebuild.

### The hybrid approach that could work

There IS a middle ground: index a SMALL subset of the brain -- just
`reflections/` and `research/proposals/` -- as a lightweight supplement
to memory_search. These are the files most relevant to "what did we
learn?" and "what was proposed?" -- both session-memory-adjacent
questions. At current brain size (~24 files), this is feasible. But it
does not replace the brain-index tool for library topics, governance
files, or investing content. It is a complement, not a substitute.

### Comparison to brain-index-search-proposal

| Aspect | extraPaths approach | Brain-index tool (proposal) |
|:--|:--|:--|
| Index location | Inside workspace | `~/.brain-index/` (outside repos) |
| Source location | Must be in workspace | Cloned to `/tmp/brain/` |
| Workspace purity | Violated (brain files in workspace mirror) | Preserved |
| Eval gates | None (memory_search has no eval) | recall@20, MRR, nDCG mandatory |
| Freshness check | None (implicit on reindex) | heartbeat.json dead-man's-switch |
| Scale ceiling | ~500 files before reindex pain | 50,000+ files, incremental |
| Agent model | Single agent, personal memory | All agents, shared knowledge |
| Build effort | 1 config line + brain clone in workspace | 2-3 sessions (eval first) |
| Separability | Mixed corpus = noise | Clean corpus per tool |

The extraPaths approach trades build simplicity (one config line) for
architectural debt that compounds with brain growth. The brain-index tool
trades build effort (2-3 sessions) for a clean separation that scales.

## R -- Reflection

### Surprise (30%)
I expected the config schema to reveal some way to point extraPaths
outside the workspace, making a brain-in-workspace workaround
unnecessary. It does not -- extraPaths is workspace-scoped by design.
This constraint is not a bug; it is the architectural boundary enforced
by the system. The identity/ folder worked with extraPaths because it is
NATURALLY inside the workspace. The brain is naturally OUTSIDE it. The
system's design pushes you toward the right architecture by refusing the
wrong one.

The brain-index-search-proposal's prescience was also surprising. It was
written on 2026-07-17, before this session's extraPaths discovery, and
it already asked and answered the exact question Suggi raised today:
"why not just use memory_search with extraPaths?" The proposal's three
reasons hold up perfectly against the technical constraints I discovered
independently. This is validation of the existing architecture, not
revision of it.

### Feel (30%)
The question was good. Suggi's instinct -- "can we extend what already
works?" -- is exactly the right engineering reflex. It is the instinct
that led to extraPaths for identity/ in the first place, and that
instinct was correct there. The fact that it does not extend to the
brain is not a failure of the instinct; it is evidence that the two
problems are genuinely different. A tool that works for both would be
either over-engineered for personal memory or under-engineered for
shared knowledge.

### Learn (40%)
1. The same config feature (extraPaths) that elegantly solved the
   identity/ problem does NOT elegantly solve the brain-index problem.
   The boundary is not the feature; it is the workspace scope. Files
   that belong IN the workspace can be indexed via extraPaths. Files
   that belong OUTSIDE the workspace need a separate index. This
   principle applies to any future "can we add X to memory_search?"
   question.
2. The brain-index-search-proposal is architecturally correct and its
   reasoning has been independently validated by this session's
   implementation work. The proposal should be treated as the canonical
   plan for knowledge-base retrieval. No revision is needed.
3. A lightweight middle ground exists: index a small subset of brain
   files (reflections + proposals) via a persistent brain clone in a
   workspace-adjacent path, treated as a supplement to memory_search.
   This is neither the brain-index tool nor a replacement for it.
   It is a tactical improvement for the most common "what did we decide?"
   queries, at low cost.

## One Actionable Change
When the brain-index tool is built (per the existing proposal), add a
section to its README documenting why it is separate from memory_search
extraPaths -- cite this reflection and the original proposal's three
reasons. This prevents future agents from re-litigating the same
question.

## Cross-links
- `research/proposals/brain-index-search-proposal.md` -- the canonical
  plan for a dedicated brain search tool
- `research/reports/living-memory-vs-openclaw-memory-search.md` --
  architecture comparison report
- `research/insights/memory-search.md` -- memory_search tool mechanics
- `reflections/2026-07-17_ava_living-memory-brain-index-future.md` --
  the IOR that motivated the brain-index revival
