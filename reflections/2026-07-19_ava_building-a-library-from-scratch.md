---
name: building-a-library-from-scratch
id: 20260719T223450Z
tier: reflection
trigger: milestone
author: Ava
tags: [library, knowledge-system, anchors, pipeline, weights, taxonomy, architecture]
links:
  - research/insights/library-system.md
  - research/insights/stale-index-problem.md
  - governance/template-library.md
---

# Building a Library From Scratch -- Anchors, Pipelines, and the Filesystem as Truth

## I -- Idea

Designing a knowledge library from scratch requires solving three
problems simultaneously: (1) how to define what belongs in each
domain without creating overlap, (2) how to populate domains with
quality content without human curation at every step, and (3) how to
prevent the index from going stale -- the same failure class that
already cost us a session earlier today. The solution that emerged
across this session segment is: domain anchors as controlled
vocabularies with explicit boundary rules, a three-process pipeline
with decorrelated scoring, and the filesystem as the single source of
truth for all indexes.

The library now has 24 domain anchors, a guide file defining the
pipeline architecture, a master index regenerated from live filesystem
state, and no static lists anywhere. Suggi drove the design through
iterative refinement: start with the concept, test it against real
domains, identify drift points, fix the naming, remove redundancy,
rename for uniformity. Six iterations in one session.

## O -- Opinion

Confidence: high (90%). The system matches established best practices
across knowledge management taxonomy (NNGroup), multi-agent pipeline
architecture (NodeMini, Knowrite), and weighted scoring (Crosley,
MakiDevelop). Every design decision is traceable to either industry
validation or our own scar tissue (R11 stale-index, R8 deduplication,
R6 automation over rules).

The most important decision was making the filesystem the authoritative
source of truth. The stale-index insight from earlier today predicted
exactly this class of failure: any static list of topics will drift
from reality. The solution -- regenerate the index from `ls` during
each audit cycle -- is the same defense-in-depth pattern that protects
the workspace memory index. Write-time reindex + read-time verification.

The naming convention refinements (anchor.md -> anchor-<domain>.md,
library-guide.md -> guide-library.md, master-index.md -> index-library.md)
were not cosmetic. Unique filenames enable cross-referencing without
folder context. Consistent <type>-<name> naming makes the library
navigable by pattern, not by memory.

## R -- Reflection

### Surprise (30%)

How quickly the anchor format stabilized. The first anchor (science)
was written as a detailed template. By the third iteration, Suggi had
identified three changes: remove R11 mentions from the index paragraph
(rule references date themselves), extract the index to a separate
file (bloat prevention), and remove redundant topic discovery text
from all 24 anchors (single source of truth in the guide). Each
iteration tightened the system without adding complexity.

The second surprise: the industry research confirmed every design
decision we made independently. The writer -> auditor sequential
pipeline, the decorrelated review, the weighted scoring with
thresholds, the taxonomy with scope boundaries -- all validated by
external sources. We did not know this when we designed it. The system
emerged from first principles (R8, R11, the three-process intuition)
and then matched what the industry independently converged on. This
is either good engineering intuition or confirmation that the problem
space dictates the solution shape.

### Feel (30%)

Satisfied. 25 files, 24 anchors, 3 scoring systems, 1 guide, 1 index,
1 insight, zero ASCII violations at final commit. The iterative
refinement with Suggi was clean -- propose, review, identify drift,
fix, recommit. Each cycle produced fewer errors because the pattern
was hardening. By the final iteration (naming convention uniformization),
there was only one change to make.

The em-dash ASCII violations are a recurring scar. I fixed 3 separate
files for the same issue in this session. The structural gate should
be: never use em-dashes or arrows in first drafts. Write ASCII-only
from the start, not as a post-processing step.

### Learn (40%)

1. **Build the anchor before the content.** The 24 domain anchors are
   not topics -- they are compasses. Every future topic written in
   this library will be oriented against these anchors. Getting the
   anchors right before writing a single topic prevents category
   errors that would be expensive to fix later. The same principle
   applies to any taxonomy: define the boundaries, then populate.

2. **Separate rules from indexes.** The guide-library.md / index-library.md
   split was Suggi's insight and it is correct. When an agent needs
   to know what exists, it reads the index (a lean table). When it
   needs to know how to operate, it reads the guide (rules and weights).
   Combining them bloats both use cases. This is the same principle
   as AGENTS.md (constitution) vs skills (procedure) -- different
   artifacts for different readers at different times.

3. **Naming conventions are structural gates.** Uniform <type>-<name>
   filenames (guide-library.md, index-library.md, anchor-science.md)
   enable pattern-based navigation. An agent can find all anchors with
   `ls */anchor-*.md` without knowing the domain names. This is not
   cosmetic -- it is discoverability encoded in the filesystem.

## One Actionable Change

Pre-write ASCII gate: never use em-dashes (--) or arrows (->) in first
drafts. Write `--` and `->` directly. The sed post-processing step is
error-prone (3 separate fixes this session). Add this to the
write-library skill when we build it: ASCII check before commit, not
after.

## Cross-links

- `research/insights/library-system.md` -- complete library architecture
  insight with industry validation
- `research/insights/stale-index-problem.md` -- the scar that made
  filesystem-as-truth non-negotiable
- `governance/template-library.md` -- template for library topics
  (to be built next session)
- `library/guide-library.md` -- pipeline rules and weight systems
- `library/index-library.md` -- master index
- `library/*/anchor-*.md` -- 24 domain anchors
