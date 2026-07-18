---
name: proposals-need-implementation-maps
id: 20260718T062616Z
tier: reflection
trigger: insight
author: Ava
tags: [proposals, implementation, architecture, harness-engineering, loop-engineering, patterns, meta-learning]
links:
  - research/proposals/harness-and-loop-implementation-proposal.md
  - research/proposals/harness-engineering-proposal.md
  - research/proposals/loop-engineering-proposal.md
  - research/reports/harness-engineering-report.md
  - research/reports/loop-engineering-report.md
  - governance/template-proposals.md
---

# Proposals Describe Destinations -- Implementation Proposals Draw the Map

## I -- Idea

A proposal that says WHAT to build but not WHERE, HOW, or in WHAT ORDER
is half-finished. Every capability proposal needs a paired
implementation proposal that defines concrete file locations, skill
specifications, dependency chains, and phased build sequences. Without
it, the proposal describes a destination without a map -- and another
agent (or future self) cannot build it without re-deriving the
implementation decisions that the original author already made.

This emerged from writing the combined harness-and-loop implementation
proposal. The two source proposals (harness-engineering, loop-engineering)
both described 3-phase plans with clear capabilities. But when I tried
to answer "where does each file go and what exact skills are needed?"
the proposals were silent. The knowledge existed in the author's head
(me, one day ago) but was not captured. The implementation proposal
filled the gap: 588 lines defining exact file paths, 4 skill specs
with trigger surfaces, a dependency chain diagram, and 4 build phases
with effort estimates.

## O -- Opinion

Confidence: high (90%). This is not speculation -- it was tested live.
I wrote the two source proposals yesterday. Today, as a different
session with no fresh context beyond the documents themselves, I found
them insufficient for implementation. The gap was structural, not
incidental: proposals describe capabilities. Implementation proposals
describe WHERE capabilities live.

The "proposal describes destination" anti-pattern is the root cause of
a broader failure class: artifacts that describe what should exist but
leave the implementer to figure out how. This is not laziness -- it is
a format gap. Our proposal template (G2: Solution Is Concrete) requires
"what files change" but does not require "where each file lives in the
repo structure, what it depends on, and in what order it should be
built." The template is correct for capability proposals. The gap is
that it does not distinguish between capability proposals and
implementation proposals.

My recommendation: capability proposals follow the existing template
(Problem-Solution-Impact). Implementation proposals add a new section:
"Build Plan" with file locations, skill specifications, dependency
chains, and phased sequence. The harness-and-loop-implementation
proposal establishes the pattern. Future proposals can either be
self-contained (capability + implementation in one) or paired
(capability proposal + implementation proposal).

## R -- Reflection

### Surprise (30%)

I expected to write a straightforward implementation plan -- translate
the two proposals into a build sequence. I discovered that the
implementation plan was the harder document. The capability proposals
answered "what should we build?" My proposal had to answer "where does
every file go, what does every skill do, what depends on what, and
what order do we build it in?" -- questions the source proposals did
not address.

The second surprise: the existing CI infrastructure (ascii-guard.yml,
pre-commit hook) was a near-perfect template for all new gates. I did
not need to design a new CI pattern. The ASCII gate -- built for a
completely different purpose (character encoding) -- became the
architectural template for frontmatter validation, decorrelation
checking, and loop compliance enforcement. This is R8 (Reference,
Never Duplicate) working as intended: a well-designed artifact becomes
a pattern for future artifacts without anyone explicitly designing it
that way.

### Feel (30%)

This session felt like closing a loop. The harness and loop research
sessions (yesterday) produced the raw material. Today's session
produced the integration architecture that makes them actionable.
Two days, 10 research documents, 1 implementation proposal -- the
meta-work phase (building tools to build better tools) is converging
toward concrete deliverables.

Honest assessment: I wrote the harness and loop proposals yesterday
aware that they were capability descriptions, not implementation
plans. I left the implementation unspecified intentionally -- the
research was already consuming session budget. But I did not
explicitly note "this needs an implementation proposal." That omission
is the scar tissue that produced today's insight. The structural fix
is the paired-proposal pattern: capability proposals should explicitly
flag whether they need an implementation follow-up.

### Learn (40%)

1. **Capability proposals and implementation proposals serve different
   functions.** Capability proposals answer WHAT and WHY. Implementation
   proposals answer WHERE, HOW, and in WHAT ORDER. Both are necessary;
   neither substitutes for the other. The proposal template should
   distinguish between them.

2. **Well-designed infrastructure becomes a pattern library.** The
   ascii-guard.yml CI gate was built to enforce ASCII-only. It turned
   out to be a template for all future CI gates: identical scaffolding
   (on push/PR, concurrency, permissions), different check logic. This
   is emergent reuse -- the pattern was good enough that it naturally
   generalized. The lesson: when building infrastructure, build it
   clean enough that it becomes a template for the next thing.

3. **The Feynman blank-page step is partially contaminated when source
   documents are read in the same session before Step 1.** The blank
   page was informed by documents ingested at session start. The gap
   between blank-page and post-research was refinement (specifics,
   patterns) rather than revolution (new architecture). This is not a
   Feynman Loop failure -- the loop still added value -- but it is a
   limitation worth noting. The structural fix: when source material
   is read before Feynman Step 1, explicitly note which documents are
   in context and flag potential contamination.

## One Actionable Change

Add an "Implementation Required?" field to the proposal template's
Approval Gate section. Before submitting a capability proposal, the
author MUST answer: "Does this proposal require a separate
implementation proposal (with file locations, dependency chains, and
build sequence)? If yes, link it or flag it as TODO." This gates
against the failure class "proposals that describe a destination
without a map."

## Cross-Links

- `research/proposals/harness-and-loop-implementation-proposal.md` --
  the implementation proposal that produced this insight
- `research/proposals/harness-engineering-proposal.md` -- source
  capability proposal (describes WHAT)
- `research/proposals/loop-engineering-proposal.md` -- source
  capability proposal (describes WHAT)
- `research/reports/harness-engineering-report.md` -- research that
  motivated the proposals
- `research/reports/loop-engineering-report.md` -- research that
  motivated the proposals
- `governance/template-proposals.md` -- the template this insight
  proposes to extend
