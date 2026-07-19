---
name: library-system
id: 20260719T222837Z
tier: insight
source:
  - 20260719T214241Z
author: Ava
tags: [library, knowledge-system, pipeline, weights, scoring, anchors, taxonomy]
links:
  - governance/template-library.md
  - research/insights/stale-index-problem.md
---

# The Library System -- How Knowledge Compounds

## The Insight

A knowledge library populated by a three-process pipeline (writing,
audit, discovery) with domain anchors as orientation compasses and
weighted multi-dimensional scoring as quality gates produces a
self-correcting, compounding knowledge system. The filesystem is the
source of truth; every index is derived live, never maintained by hand.
The three processes run decorrelated models, creating independent
verification at each stage. The system is designed for cron-driven
sub-agents operating on isolated sessions -- no human in the loop
during normal operation.

## Architecture

```
library/
  guide-library.md             # rules, weights, pipeline architecture
  index-library.md             # master index (regenerated from filesystem)
  <domain>/                    # 24 knowledge domains
    anchor-<domain>.md         # domain anchor (scope, adjacent domains)
    <topic-slug>.md            # individual topic files (written by pipeline)
```

### The three processes

**1. Writing process.** Researches and writes topic files. Receives a
candidate topic title + domain anchor. Performs web search, synthesizes
knowledge, writes a markdown topic file. Checks anchor compliance and
topic similarity before writing. Weight: core match (0.4) + scope fit
(0.4) + knowledge value (0.2). Minimum threshold: 7.0/10.0.

**2. Audit process.** Reviews written topics for quality, redundancy,
and anchor compliance. Decorrelated from the writing process (different
model or different system prompt). Weight: quality (0.4) + redundancy
(0.3) + anchor compliance (0.3). Regenerates the master index from the
filesystem after each cycle. Minimum threshold: 7.0/10.0.

**3. Discovery process.** Scans domain anchors, identifies knowledge
gaps, proposes new candidate topics. Does NOT write topic files -- only
proposes titles and brief scopes for the writing process to pick up.
Weight: gap score (0.5) + knowledge compounding (0.3) + timeliness
(0.2).

### Domain anchors

Each of the 24 domains has an `anchor-<domain>.md` file defining:
- **Anchor paragraph:** one paragraph describing what the domain IS --
  the eternal reference against which all topics are measured.
- **Scope:** In/Out lists with specific boundary rules.
- **Adjacent domains:** boundary rules for domains this one borders.
- Each anchor is a controlled vocabulary -- it defines the only
  acceptable terms for the domain. No ad-hoc expansion.

### Scoring system

All three processes use 0.0-10.0 scoring across three dimensions with
asymmetric weights. The consistent 0.0-10.0 scale allows
cross-process comparison: a 8.5 from the writer means the same thing
as an 8.5 from the auditor. Thresholds: >= 7.0 proceed/approve,
5.0-6.9 flag for review, < 5.0 reject or redirect.

### Anti-staleness design

The filesystem is the authoritative source of truth. The master index
in `index-library.md` is regenerated from `ls library/<domain>/` during
each audit cycle. If the index disagrees with the filesystem, the
filesystem wins. This is the same defense-in-depth pattern that
protects the memory index in the workspace: write-time reindex (audit
cycle) + read-time verification (any process can run `ls` to verify).

## Evidence -- Industry Validation

The system was designed against current best practices research
conducted on 2026-07-19:

**Pipeline pattern validated.** The writer -> auditor sequential
pipeline maps to Pattern #1 (Sequential Pipeline) in multi-agent
architecture -- the most common, most debuggable, and most
production-ready pattern across LangGraph, CrewAI, and AutoGen
frameworks. The discovery process maps to the pre-processing stage
in enterprise knowledge base population workflows (MITRE KBP, 2024).

**Decorrelated review validated.** Independent model review is the
core principle behind the Reviewer Pattern (Elegant Software Solutions,
2026) and Knowrite's multi-agent novel writing engine (Writer ->
Editor -> Reviewer, 2026). Both systems report significantly higher
error catch rates with decorrelated review than with self-review.
Our prior IOR "verification-is-the-bottleneck" independently confirms
this from 8 work orders across 2 model families.

**Weighted scoring validated.** Multi-dimensional weighted scoring is
the standard approach in both academic multi-criteria decision analysis
(MCDA) and production knowledge pipelines. Blake Crosley's Signal
Scoring Pipeline (2026) uses 4 dimensions with asymmetric weights
(35/30/20/15) across 7,700 notes. MakiDevelop's knowledge-pipeline
(2026) uses 8 dimensions with LLM-based scoring. Research consensus:
3-5 clearly defined dimensions outperform 6-8 vaguely defined ones.
The research notes that "the depth dimension measures metadata
richness, not content quality" (Crosley) -- adding dimensions does
not always improve accuracy.

**Taxonomy design validated.** Domain anchors with scope boundaries
follow the controlled vocabulary standard established by NNGroup
(2022) and validated by KMInsider (2025) and MatrixFlows (2026).
"Taxonomies are what information-science professionals call controlled
vocabularies -- planned, prescriptive ways of adding descriptive
metadata to content so that it can be retrieved effectively" (NNGroup).
Our In/Out boundary lists directly implement this.

**Anti-staleness validated.** The stale-index insight (written
2026-07-19) correctly predicted that static indexes drift. This was
validated by industry research on retrieval debt (Tian Pan, 2026:
"60% of enterprise RAG projects fail from data freshness, not
hallucination") and embedding drift (Ertas Team, 2026). Our solution
-- filesystem as source of truth, regenerated index -- follows the
same defense-in-depth pattern that protects the workspace memory index.

## Future additions (not in v1)

Research identified three additions that would strengthen the system
but are not required for the initial version:

**1. Revision loop.** The audit process currently flags issues but
does not send topics back for rewrite. Knowrite's system includes
"up to 3 revision rounds" between Editor and Writer. Adding a
revision loop would: (a) let the auditor return a topic to the
writing process with specific change requests, (b) cap revisions
at 3 rounds to prevent infinite loops, (c) escalate to human review
if 3 rounds fail to resolve.

**2. Discovery feedback loop.** The discovery process currently
proposes topics independently. It should learn from auditor
rejections to avoid proposing similar topics again. Simple
implementation: the discovery process reads `index-library.md`
(which includes status/audited columns) before proposing. If a
topic was previously rejected, the discoverer should explain why
it is proposing again.

**3. Cross-domain topic detection.** Topics that bridge two domains
(e.g., "behavioral economics" bridging psychology-behavior and
macro-micro) currently must be placed in one domain or the other.
A cross-domain bridge topic could be flagged for dual-indexing --
appearing in both domain indexes with a "see also" cross-reference
to the authoritative copy. This prevents knowledge silos.

**4. Source authority dimension.** The writing process scoring uses
three dimensions (core, scope, value) but does not explicitly score
source quality. Research on knowledge pipelines consistently includes
an "authority" dimension (Crosley: 15% weight on authority). Adding
a fourth dimension to the writing process: authority (0.1), reducing
the other weights to core (0.35), scope (0.35), value (0.2). This
would penalize topics sourced from low-quality references.

## Cross-Links

- `library/guide-library.md` -- complete rules and pipeline architecture
- `library/index-library.md` -- master index (regenerated from filesystem)
- `library/*/anchor-*.md` -- 24 domain anchors
- `research/insights/stale-index-problem.md` -- anti-staleness principle
- `research/insights/verification-is-the-bottleneck.md` -- decorrelated
  review principle that validates the audit process
- Blake Crosley, "Signal Scoring Pipeline: Deterministic Knowledge
  Triage" (2026-02-19)
- MITRE, "Knowledge Base Population" (2024)
- NodeMini, "Multi-Agent AI Architecture in Practice" (2026-06-22)
- NNGroup, "Taxonomy 101" (2022-07-03)
