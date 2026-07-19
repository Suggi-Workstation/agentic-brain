---
name: anchor-index
id: 20260719T214241Z
tier: library-meta
author: Ava
tags: [library, anchor, index, pipeline, weights, multi-agent]
links:
  - governance/template-library.md
  - research/insights/stale-index-problem.md
---

# Library -- Anchor Index

## What this file is

This is the parent file for the library knowledge system. It defines:

1. The multi-agent pipeline that populates library domains with topics.
2. The global weight rules each agent uses.
3. The structure every domain anchor must follow.
4. How the master index is maintained (R11: derive live, never hardcode).

It does NOT contain a static list of topics. The filesystem is the
source of truth. To get the current topic list for a domain, run:
`ls library/<domain>/*.md`. The auditor agent regenerates index
snapshots below during each audit cycle.

## Library structure

```
library/
  anchor-index.md              # this file
  <domain>/                    # one folder per knowledge domain
    anchor.md                  # domain anchor (scope, adjacent domains, discovery rules)
    <topic-slug>.md            # individual topic files
    ...
```

Currently 24 domains: accounting-financial-shenanigans, anthropology,
books, case-studies, coding-agentic-ai, earth-climate, ethics-philosophy,
finance, geopolitics, industries-sectors, investors, law-regulation,
macro-micro, mathematics-statistics, notable-people, pop-culture,
portfolio-risk-management, probabilistic-thinking-forecasting,
psychology-behavior, science, self-improvement, technology,
valuation-screening, value-investing.

## The multi-agent pipeline

Three sub-agents run as cron jobs on isolated sessions with independent
models (decorrelation rule). Each has a different role, different
weights, and different verification criteria.

### Agent 1: Topic Writer (`write-library` skill)

**Role:** Research and write topic files. Receives a candidate topic
title + domain anchor. Performs web search, synthesizes knowledge,
writes a markdown topic file to the domain folder. Checks anchor
compliance and topic similarity before writing.

**Cron:** Runs periodically. Each cycle: writer picks one candidate
topic from the discoverer's queue, researches it, writes it.

**Weighted scoring (writer weight):**

| Dimension | Weight | What it measures |
|:--|:--|:--|
| Core match | 0.4 | How central is this topic to the domain anchor? Does it directly concern the domain's subject matter? |
| Scope fit | 0.4 | Does it fit the domain's In scope? Does it avoid Out scope and adjacent domain overlap? |
| Knowledge value | 0.2 | Would a well-researched topic on this compound with existing brain knowledge? Is it worth the token cost? |

**Topic similarity gate:** Before writing, the writer must check the
candidate topic against EXISTING topics in the domain. If a similar
topic already exists (>= 80% semantic overlap), skip and flag. If
partial overlap (50-80%), the new topic should cross-reference the
existing one and focus on the uncovered portion. If low overlap
(< 50%), proceed normally.

**Minimum threshold:** Weighted score >= 7.0 to proceed. 5.0-6.9: flag
for human review. < 5.0: reject or redirect to adjacent domain.

### Agent 2: Topic Auditor (`audit-library` skill)

**Role:** Review written topics for quality, redundancy, and anchor
compliance. Updates the master index below. Runs after the writer
has produced new files. Decorrelated from writer (different model
family or different system prompt emphasis).

**Cron:** Runs after writer cycles. Each cycle: auditor picks the
most recently written (unaudited) topics and evaluates them.

**Weighted scoring (auditor weight):**

| Dimension | Weight | What it measures |
|:--|:--|:--|
| Quality | 0.4 | Factual accuracy, completeness, source citations, ASCII compliance, structural correctness. Is this a well-researched topic? |
| Redundancy | 0.3 | Does this topic overlap with any other topic in the same domain or adjacent domains? Semantic similarity check against all existing topics. |
| Anchor compliance | 0.3 | Does the topic stay within the domain's anchor scope? Would it fit better in an adjacent domain? |

**Minimum threshold:** Weighted score >= 7.0 to approve. 5.0-6.9: flag
with specific change requests for the writer. < 5.0: reject (move file
to quarantine or request rewrite).

**Index update:** After each audit cycle, the auditor regenerates the
master index snapshot below from the live filesystem. The auditor is
the ONLY agent authorized to update index entries in this file.

### Agent 3: Topic Discoverer (`discover-library` skill)

**Role:** Discover new candidate topics. Scans all domain anchors,
identifies knowledge gaps, proposes new topics. Runs before the
writer to populate the candidate queue. Does NOT write topic files --
only proposes titles and brief scopes.

**Cron:** Runs periodically. Each cycle: discoverer picks a subset of
domains and proposes 1-3 candidate topics per domain.

**Weighted scoring (discovery weight):**

| Dimension | Weight | What it measures |
|:--|:--|:--|
| Gap score | 0.5 | How uncovered is this topic? Does a topic on this subject already exist? Is this a known gap in the domain's coverage? |
| Knowledge compounding | 0.3 | Would this topic connect multiple existing topics? Would it fill a bridge between domains? Would it enable deeper research on related topics? |
| Timeliness | 0.2 | Is this topic currently relevant? Are there recent developments, new research, or active debates? |

**Output:** Candidate topic proposals with title, domain, brief scope
description, and discovery score. Stored as proposals (not topic files)
for the writer to pick up.

## The anchor file format

Every domain folder MUST contain an `anchor.md` file. Format:

```markdown
---
name: <domain-slug>
tier: library-anchor
domain: <domain-slug>
id: <date-generated>
tags: [<domain-specific-tags>]
---

# <domain-name>

## Anchor
(One paragraph describing what this domain is about. The eternal
reference against which all topics are measured.)

## Scope
**In:** (what belongs)
**Out:** (what does not)

## Adjacent domains
(list of domains this one borders, with boundary rules)

## Topic discovery
(domain-specific discovery guidance for the writer)
```

The anchor paragraph is the most important part. It must be:
- Broad enough to encompass all valid topics in the domain.
- Narrow enough to exclude topics that belong in adjacent domains.
- Stable -- this is an eternal anchor, not a living document.
  It changes only when the domain's scope fundamentally shifts.

## Master index

**R11: This index is derived live from the filesystem, not maintained
by hand.** The authoritative source of truth is `ls library/<domain>/`.
This snapshot is regenerated by the auditor agent during each audit
cycle for human readability. If this snapshot disagrees with the
filesystem, the filesystem wins.

To verify: `ls library/*/*.md | wc -l` returns the live topic count.

### Index snapshot

Last regenerated: (auditor updates this timestamp)

| domain | topic | status | audited |
|:--|:--|:--|:--|

<!-- Auditor: regenerate this table from `ls library/<domain>/*.md` -->
<!-- Writer: never edit this section -->
<!-- Discoverer: read this to avoid proposing duplicate topics -->
