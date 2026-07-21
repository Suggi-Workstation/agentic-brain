---
name: guide-library
id: 20260719T220256Z
tier: library-meta
author: Ava
version: 2.0
tags: [library, anchor, index, pipeline, weights, scoring]
links:
  - research/insights/library-system.md
  - research/insights/stale-index-problem.md
  - logbook/protocol.md
---

# Library Guide (v2)

## What this file is

This is the parent file for the library knowledge system. It defines:

1. The three-process pipeline that populates library domains with topics.
2. The global weight rules each agent uses (v2: 4 dimensions per process).
3. The structure every domain anchor must follow.
4. How the master index is maintained (R11: derive live, never hardcode).

It does NOT contain a static list of topics. The filesystem is the
source of truth. To get the current topic list for a domain, run:
`ls library/<domain>/*.md`. The auditor agent regenerates index
snapshots below during each audit cycle.

## Library structure

```
library/
  guide-library.md             # this file (rules, weights, pipeline)
  index-library.md             # master index (regenerated from filesystem)
  candidate-queue.md           # topics proposed by the discoverer, awaiting the writer
  <domain>/                    # one folder per knowledge domain
    anchor-<domain>.md          # domain anchor (scope, adjacent domains)
    <topic-slug>.md            # individual topic files
    quarantine/                 # topics rejected by the auditor
    ...
```

Currently 24 domains: accounting-financial-shenanigans, anthropology,
books, case-studies, coding-agentic-ai, earth-climate, ethics-philosophy,
finance, geopolitics, industries-sectors, investors, law-regulation,
macro-micro, mathematics-statistics, notable-people, pop-culture,
portfolio-risk-management, probabilistic-thinking-forecasting,
psychology-behavior, science, self-improvement, technology,
valuation-screening, value-investing.

## The three-process pipeline

Three processes run as isolated cron jobs with independent models
(decorrelation rule). Each process has 4 weighted dimensions (v2)
scored on a consistent 0.0-10.0 scale. Thresholds: >= 7.0 proceed,
5.0-6.9 flag for review, < 5.0 reject or redirect.

### Writing process

**Purpose:** Research and write topic files. Receives a candidate topic
title + domain anchor. Performs web search, synthesizes knowledge,
writes a markdown topic file to the domain folder. Checks anchor
compliance, topic similarity, and source credibility before writing.

**Cron:** Runs periodically. Each cycle: picks one candidate topic
from the discovery queue, researches it, writes it.

**Weighted scoring (4 dimensions):**

| Dimension | Weight | What it measures |
|:--|:--|:--|
| Core match | 0.35 | How central is this topic to the domain anchor? Does it directly concern the domain's subject matter? |
| Scope fit | 0.35 | Does it fit the domain's In scope? Does it avoid Out scope and adjacent domain overlap? |
| Knowledge value | 0.20 | Would this compound with existing brain knowledge? Is it worth the token cost? |
| Source authority | 0.10 | Are the web sources credible? Academic papers, reputable publications, primary sources -- or random blog posts and forums? |

Weighted score: `(core * 0.35) + (scope * 0.35) + (value * 0.20) + (authority * 0.10)`.

**Topic similarity gate:** Before writing, the writer MUST check the
candidate topic against existing topics in the domain. If >= 80%
semantic overlap, skip and flag DUPLICATE. If 50-80% overlap, proceed
but cross-reference the existing topic and focus on the uncovered
portion. If < 50%, proceed normally.

**Minimum threshold:** Weighted score >= 7.0 to proceed. 5.0-6.9: flag
for review, skip. < 5.0: reject or redirect to adjacent domain.

### Audit process

**Purpose:** Review written topics for quality, redundancy, anchor
compliance, and source accuracy. Regenerates the master index from the
live filesystem after each cycle. Decorrelated from the writing process
(different model or different system prompt emphasis).

**Cron:** Runs after writing cycles. Each cycle: picks the most
recently written (unaudited) topics and evaluates them.

**Weighted scoring (4 dimensions):**

| Dimension | Weight | What it measures |
|:--|:--|:--|
| Quality | 0.35 | Factual accuracy, completeness, source citations, ASCII compliance, structural correctness. Is this a well-researched topic? |
| Redundancy | 0.25 | Does this topic overlap with any other topic in the same domain or adjacent domains? Semantic similarity check against all existing topics. |
| Anchor compliance | 0.30 | Does the topic stay within the domain's anchor scope? Would it fit better in an adjacent domain? |
| Source verification | 0.10 | Spot-check: do the cited sources actually support the claims made? Pick 2-3 cited claims and verify against the source material. |

Weighted score: `(quality * 0.35) + (redundancy * 0.25) + (anchor * 0.30) + (source * 0.10)`.

**Minimum threshold:** Weighted score >= 7.0 to APPROVE. Update topic
frontmatter with `audited: true` and `audit-score: X.X`. 5.0-6.9: FLAG
with specific change requests. < 5.0: REJECT, move file to
`quarantine/` directory.

**Index update:** After each audit cycle, the auditor regenerates the
master index in `index-library.md` from the live filesystem. The auditor
is the ONLY agent authorized to update index entries.

### Discovery process

**Purpose:** Discover new candidate topics. Scans domain anchors,
identifies knowledge gaps, proposes new topics. Runs before the
writing process to populate the candidate queue. Does NOT write topic
files -- only proposes titles and brief scopes.

**Cron:** Runs periodically. Each cycle: picks a subset of domains
and proposes 1-3 candidate topics per domain. Rotates domains across
cycles to ensure even coverage.

**Weighted scoring (4 dimensions):**

| Dimension | Weight | What it measures |
|:--|:--|:--|
| Gap score | 0.40 | How uncovered is this topic? Does a topic on this subject already exist? Is this a known gap in the domain's coverage? |
| Knowledge compounding | 0.25 | Would this topic connect multiple existing topics? Would it fill a bridge between domains? |
| Timeliness | 0.20 | Is this topic currently relevant? Are there recent developments, new research, or active debates? |
| Domain balance | 0.15 | Is this domain underrepresented vs others? Prioritize domains with fewer topics to prevent library tilt. |

Weighted score: `(gap * 0.40) + (compounding * 0.25) + (timeliness * 0.20) + (balance * 0.15)`.

No minimum threshold for discovery -- all scored candidates are
proposed. The writer applies its own >= 7.0 threshold.

**Output:** Candidate topic proposals with title, domain, brief scope
description, and discovery score. Appended to `library/candidate-queue.md`.

## The anchor file format

Every domain folder MUST contain an `anchor-<domain>.md` file. Format:

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

## Index

The master index lives in `index-library.md` -- a separate file to
keep the index lean for agents reading it during operations. The
audit process regenerates the index snapshot from the live filesystem.

## Logging

All three processes write to `logbook/library.log` following the
logbook protocol (`logbook/protocol.md`). Category: `library`.
Each entry includes the ENT counter, timestamp, agent name, reference
to the affected file, and a summary of the action taken with scores.

## Version History

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1.0 | 2026-07-19 | Ava | Initial design: 3 dimensions per process |
| 2.0 | 2026-07-21 | Link | Added 4th dimension per process: source authority (writer), source verification (auditor), domain balance (discoverer). Research consensus: 3-5 dims optimal. Weights redistributed per Crosley 2026 pattern. |