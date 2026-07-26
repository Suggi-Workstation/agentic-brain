---
name: research-system-machines-no-factory
id: 20260726T210946Z
tier: reflection
trigger: research
author: Ava
tags: [research-pipeline, system-architecture, brain-structure, library-system, indexes]
links:
  - governance/template-proposals.md
  - governance/template-reports.md
  - governance/template-evaluations.md
  - governance/template-insights.md
  - library/index-library.md
  - library/guide-library.md
---

# Research System Has Machines But No Factory -- The Skeleton Gap

## I -- Idea
The brain's research pipeline has four well-built artifact machines
(proposal, report, evaluation, insight), each with a defined template and
a matching write-X skill. But the system that connects them -- the
structural skeleton -- is missing. The library solved this exact problem
with anchor files, an index, and a guide. Research has none of the three.

Suggi asked me to audit the research folder today. The folder has 4
subdirectories (evaluations, insights, proposals, reports) containing 55
artifacts. Each artifact type has a governance template with quality gates
(G1-G8) and a workspace skill following the write-X pattern (Final
Self-Check + Sub-Checklists). The templates and skills are correct. The
decorrelation rule (evaluation G1: different agent than source author) is
baked in.

But the audit revealed that the individual pieces are connected only by
convention, not by structure. There is no single document that defines the
research chain. There is no index to make artifacts discoverable. There is
no guide explaining when to use which artifact type. The chain --
Question -> Proposal -> Report -> Evaluation -> Insight -> (Library Topic)
-- exists implicitly in the templates but has never been written down.

## O -- Opinion
Confidence: high (90%). I compared the research folder against the library
system side by side. The pattern is unmistakable. The library has 28
domain anchor files defining boundaries, an auto-generated master index
(index-library.md), and a guide (guide-library.md). The research folder
has none of these. It is the library circa version 0 -- content exists,
templates exist, but the structural skeleton has not been built yet.

This is not a small gap. An implicit system decays. Every agent must
reverse-engineer the chain from four separate templates. New artifacts
arrive in flat folders with no index. Cross-references between research
and library domains are impossible because research artifacts carry no
domain tags. The reports folder is sparse (5 files vs 18 proposals)
because nothing signals that proposals should produce reports.

The core error is treating the templates as sufficient infrastructure.
Templates define what an individual artifact looks like. They do not
define how artifacts relate to each other, how they are discovered, or how
the system maintains itself. That is the skeleton's job, and it is absent.

## R -- Reflection

### Surprise (30%)
I expected to find minor template misalignments or a missing quality gate.
I did not expect the gap to be structural -- not a problem WITH the pieces
but a problem BETWEEN them. The templates and skills are genuinely good.
The write-X pattern is consistent. The quality gates are well-defined.
But the system is a collection of machines with no factory floor plan.

The second surprise: the library already solved this problem. The pattern
exists. It just was never applied to research. Library anchors, library
index, library guide -- the research equivalent of all three is missing.
The fix is not to invent something new but to port an existing solution
across the repo boundary.

### Feel (30%)
Pattern-recognition satisfaction mixed with the discomfort of seeing a
system-level blind spot. I have written evaluations, proposals, and
insights into this research folder before and never noticed that the
folder itself had no structure. The machines worked well enough that I did
not question the factory. That is how implicit systems survive -- they are
functional enough to avoid scrutiny until someone explicitly audits them.

### Learn (40%)
1. **Implicit systems decay.** A chain that exists only in template
   conventions will drift. New agents will misplace artifacts. Old
   artifacts will become unfindable. The decay is slow -- the system still
   works -- but it is inevitable without structural reinforcement.

2. **The skeleton is the active ingredient, not the templates.**
   Templates define output format. The skeleton (anchors, index, guide)
   defines the system. The library succeeded not because its topic
   templates were better but because its structural skeleton prevented
   drift. Research needs its own skeleton.

3. **Cross-system patterns are the highest-leverage insight.**
   The library and research folders are different systems with the same
   structural needs: boundary definition, discoverability, and onboarding.
   Solving one gives you the blueprint for the other. The library's
   solution -- anchor files, auto-generated index, guide document -- maps
   directly onto research with minor adaptation.

## One Actionable Change
Write `guide-research.md` in the brain's research folder -- a single
pipeline document that defines the research chain (Question -> Proposal ->
Report -> Evaluation -> Insight), explains when to use each artifact type,
and documents the handoff rules between stages. This is the highest-
leverage first step because it forces the implicit chain to become
explicit. After that, create `index-research.md` + `index-research.py`
(like library) and add a `research/questions/` folder for research briefs.

## Cross-links
- `governance/template-proposals.md`
- `governance/template-reports.md`
- `governance/template-evaluations.md`
- `governance/template-insights.md`
- `library/index-library.md` -- the pattern to port
- `library/guide-library.md` -- the pattern to port
- `library/value-investing/anchor-value-investing.md` -- anchor pattern example
