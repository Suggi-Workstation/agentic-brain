---
name: reverse-adjacency-principle
id: 20260722T102236Z
tier: reflection
trigger: session-end
author: Link
tags: [library, anchor, adjacent-domains, cross-reference, knowledge-graph, bidirectional]
links:
  - library/guide-library.md
  - library/index-library.md
  - research/insights/library-system.md
---

# Reverse Adjacency Is Not Optional -- Bidirectional Knowledge Graphs Demand Symmetry

## I -- Idea

When new domains are added to a knowledge graph, every existing domain
that the new domain references MUST receive a reverse reference. The
new domain's adjacent section is the canonical source of truth for
which old domains need updating -- it is a checklist, not a suggestion.
Skipping this step produces an asymmetric graph where half the edges
are one-way, and the reader navigating from an old domain never
discovers the new ones.

This session, I added 21 reverse-adjacency entries across 13 old anchor
files to close the gap created when 4 new domains (history,
health-medicine, communication, education-learning) were added in a
previous session. The new domains correctly referenced the old ones,
but the old 24 were never updated. The fix was systematic: for each new
domain, read its adjacent section, and for each old domain listed
there, add a reverse entry to that old domain's adjacent section.

## O -- Opinion

Confidence: high (95%). The reverse-mapping principle is not specific
to the library -- it applies to any knowledge graph where nodes
reference each other. The correct procedure is:

1. Add new node + its forward references.
2. For each forward reference, add the reverse reference to the
   referenced node.
3. Verify bidirectionality: every edge in the graph has a counterpart.

The error pattern is predictable: step 2 is skipped because the writer
focuses on the new node and considers the task "done" once its
references are in place. The old nodes feel "finished" and are
mentally closed. This is the same class of error as R9
(Cross-Reference Propagation) -- when one value changes, all dependent
values must change too. Here, when one domain is added, all domains it
references must also change.

The user caught this gap immediately: "the adjacent sections of these
4 added should be correct, since when you added these, you already
KNEW the other 24 domains... what didn't happen was that you didn't
update the old 24." This is thinking in categorical gaps -- a skill
that applies to governance, code, and knowledge graphs equally.

## R -- Reflection

### Surprise (30%)

I expected this session to involve new feature work or a task request.
Instead, the entire session was structural cleanup: format
standardization (27 anchor files to match a reference format) followed
by reverse-adjacency completion (13 files, 21 entries). The user
prioritized graph consistency over forward progress. I did not expect
"knowledge graph maintenance" to be a full-session activity, but it
was -- and it was the right call. An asymmetric graph is technical
debt that compounds with every new domain added.

### Feel (30%)

Satisfied that the reverse-mapping principle is clean and systematic.
The Python script approach (read new domain's adjacent section,
generate reverse entries, append to old domains) was the right tool
for the job -- manual editing of 21 entries across 13 files would have
been error-prone.

Mild frustration that the gap existed in the first place. When I added
the 4 new domains in the prior session, I should have propagated the
reverse references immediately. The fact that I didn't means the
library-creation procedure was missing a step. The scar is now
documented.

### Learn (40%)

1. **Reverse-mapping is a procedural gate, not a judgment call.**
   When adding nodes to a knowledge graph, step N+1 is always:
   for each forward reference, add the reverse. This must be a
   checklist item in the library-writer skill, not left to the
   writer's memory.

2. **The user audits for categorical gaps.** They don't read every
   line -- they scan for what's missing. "The old 24 don't reference
   the new 4" is a gap detected by pattern, not by content review.
   This is the same skill that catches R11 violations and hardcoded
   agent assignments in single scans.

3. **Knowledge graph maintenance is substantive work.** It is not
   "cleanup" to be deferred -- it is structural integrity work that
   prevents compounding drift. Every session that adds domains must
   allocate time for reverse-propagation.

## One Actionable Change

Add a step to the library-writer skill: after writing a new anchor
file, for each domain listed in the new anchor's adjacent section,
read that domain's anchor file and add a reverse adjacent entry.
Gate: the new domain's adjacent section is the checklist -- every
domain listed there must have a reciprocal entry.

## Cross-links

- `library/guide-library.md` -- library system guide, domain creation procedure
- `library/index-library.md` -- domain index, should reference all 28
- `research/insights/library-system.md` -- library system design v2
