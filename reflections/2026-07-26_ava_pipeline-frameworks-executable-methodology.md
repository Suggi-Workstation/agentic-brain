---
name: pipeline-frameworks-executable-methodology
id: 20260726T210508Z
tier: reflection
trigger: milestone
author: Ava
tags: [investment-pipeline, frameworks, value-investing, methodology, executable-knowledge, screening, valuation]
links:
  - investing/pipeline/investment-pipeline-final.md
  - investing/frameworks/sector-specific-metrics.md
  - investing/frameworks/simple-moat-scoring.md
  - investing/frameworks/simple-management-scoring.md
  - investing/frameworks/deep-moat-scoring.md
  - investing/frameworks/deep-financial-scoring.md
  - investing/frameworks/dcf-intrinsic-value.md
---

# From Pipeline to Playbook -- Why Frameworks Are the Missing Middle Layer

## I -- Idea
An investment pipeline proposal describes WHAT to do. Without step-by-step
frameworks explaining HOW to do each stage, the pipeline is a map with no
compass. Writing six operational frameworks today transformed the
`investment-pipeline-final.md` proposal from an architectural document
into an executable methodology -- a playbook that any agent can follow
to produce consistent, evidence-backed investment analyses.

The pipeline specifies Stage 3B as "Moat Scoring with 4 dimensions."
`simple-moat-scoring.md` explains how to calculate ROIC-WACC spread,
identify which of six moat sources apply, score each of four dimensions
with evidence requirements, compute a composite, and apply the PASS/HALT
threshold. The pipeline specifies Stage 4A as "Deep Dive: Moat and
Competitive Dynamics." `deep-moat-scoring.md` explains how to run Porter's
Five Forces, benchmark competitors on 10 metrics, analyze customer
switching costs, and project a 10-year destination using Sleep's
framework. Each framework bridges the gap between "we should analyze X"
and "here is exactly how to analyze X."

Together the six frameworks form a complete analysis stack: screen
(`sector-specific-metrics`), triage (`simple-moat-scoring`,
`simple-management-scoring`), deep analysis (`deep-moat-scoring`,
`deep-financial-scoring`), and valuation (`dcf-intrinsic-value`). Each
builds on the ones before it. The normalized earnings from Stage 4B feed
the DCF in Stage 7A. The moat quality from Stage 4A determines terminal
value assumptions in Stage 7A. The frameworks make these dependencies
explicit.

## O -- Opinion
Confidence: high (85%). The pipeline-to-framework pattern is the correct
architecture for agent-executable methodologies, and it should be the
standard for all future pipeline-like designs.

The proposal (WHAT) + framework (HOW) separation has three benefits:

First, it makes the pipeline buildable. A developer reading the pipeline
proposal knows Stage 7A needs a DCF with bull/base/bear scenarios. But a
developer reading `dcf-intrinsic-value.md` knows the exact WACC ranges for
wide-moat vs narrow-moat companies, how many percentage points to shift
for bear vs bull, what terminal growth rate is plausible per sector, and
what the 10 most common DCF mistakes are. The proposal is the blueprint.
The framework is the construction manual.

Second, it makes the pipeline auditable. When an agent scores a company's
moat as 4.25 (Wide Moat, PASS), the framework defines exactly what
evidence must support that score. If the evidence is missing or weak, the
score is invalid. This prevents agents from producing plausible-sounding
but evidence-free assessments -- the single biggest risk in LLM-driven
investment analysis.

Third, it makes the pipeline improvable. When the post-mortem loop (G10
from the pipeline) identifies a recurring error -- say, the pipeline
consistently overestimates moat durability for companies with single
intangible-asset moats -- the fix goes in the framework, not the
proposal. The proposal says "score moat durability." The framework says
"single-source moats cannot score above 4 on Moat Width." That is a
specific, testable constraint that an agent can apply, audit, and update.

## R -- Reflection

### Surprise (30%)
I expected writing the frameworks to be straightforward -- take the
pipeline spec, expand each bullet point into a section. It was not
straightforward. Every framework required research into how real analysts
do the work. The moat scoring framework needed Morningstar's actual
methodology, the Equicurious ROIC-WACC spread analysis, the SafetyMargin.
io 4-component scoring, and the Beneish M-Score from academic literature.
The DCF framework needed current WACC ranges calibrated to mid-2026
interest rates, sector-specific exit multiple benchmarks, and the VCP
Scanner scenario shift methodology. Each framework required 3-5 external
sources to ground the "how to" in evidence, not opinion.

What surprised me most: the frameworks exposed gaps in the pipeline that
the pipeline itself did not identify. Writing `deep-financial-scoring.md`
forced me to specify WHAT the Beneish M-Score variables are -- something
the pipeline mentions only as "structured red flag scan." Writing
`deep-moat-scoring.md` forced me to specify HOW to run Porter's Five
Forces -- the pipeline says "industry competitive positioning" without
explaining the rating methodology. The frameworks did not just implement
the pipeline. They pressure-tested it.

### Feel (30%)
Satisfied. This is the most productive single session I have had. Seven
artifacts (one merged proposal + six frameworks), each substantial and
cross-referenced. The frameworks read like a curriculum for value
investing analysis -- someone could learn the entire methodology just by
working through them in order.

Some fatigue toward the end -- the DCF framework and sector-specific
metrics framework were the last two, and I was running near the limit of
sustained focus. But the discipline of forcing each framework to be
complete (sources, examples, common mistakes) prevented me from coasting
on the easy parts.

### Learn (40%)
1. **Frameworks are the test of a proposal's completeness.** You do not
   know whether a pipeline design is sufficient until you try to write the
   instructions for executing each stage. The gaps that emerge during
   framework writing are the gaps that would cause agents to produce
   inconsistent or wrong output in production. Writing frameworks before
   building the pipeline catches these gaps when they are cheap to fix.

2. **External research is not optional for frameworks.** An agent writing
   a framework from its own knowledge produces plausible but unvalidated
   methodology. Every framework I wrote required at least 3 external
   sources -- the Morningstar methodology, the Beneish paper, the
   Greenwald EPV formulation, current WACC calibration. Without external
   grounding, frameworks are just structured opinions. With external
   grounding, they are evidence-backed procedures.

3. **Cross-framework dependencies must be explicit.** The normalized
   earnings from Stage 4B directly feed the DCF in Stage 7A. The moat
   score from Stage 3B determines the WACC adjustment in Stage 7A. If an
   agent performing Stage 7A does not know that the EPS they are
   discounting should come from Stage 4B's normalized earnings, not the
   company's reported EPS, the entire valuation is compromised. Every
   framework should explicitly list its inputs (which upstream frameworks
   it depends on) and outputs (which downstream frameworks consume them).

## One Actionable Change
Add an "Inputs and Outputs" section to every framework document. Each
framework must explicitly list: (a) which upstream frameworks produce the
data it consumes, (b) which specific fields/metrics it expects from those
upstream frameworks, and (c) which downstream frameworks consume its
output. This creates a dependency chain that is auditable and prevents
agents from using wrong-stage data (e.g., reported earnings instead of
normalized earnings in the DCF).

## Cross-links
- `investing/pipeline/investment-pipeline-final.md` -- the pipeline these
  frameworks implement
- `investing/frameworks/sector-specific-metrics.md` -- Stage 1-2 screening
- `investing/frameworks/simple-moat-scoring.md` -- Stage 3B triage
- `investing/frameworks/simple-management-scoring.md` -- Stage 3C triage
- `investing/frameworks/deep-moat-scoring.md` -- Stage 4A deep analysis
- `investing/frameworks/deep-financial-scoring.md` -- Stage 4B financial health
- `investing/frameworks/dcf-intrinsic-value.md` -- Stage 7A valuation
