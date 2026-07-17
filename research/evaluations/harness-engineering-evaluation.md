---
name: harness-engineering-evaluation
id: 20260717T200303Z
tier: evaluation
source: 20260717T200303Z
author: Ava
tags: [harness-engineering, evaluation, self-review]
links:
  - research/reports/harness-engineering-report.md
  - research/proposals/harness-engineering-proposal.md
---

# Evaluation: Harness Engineering Report

## Source

Evaluating `20260717T200303Z` -- "Harness Engineering -- State of the
Art, July 2026" by Ava. Full-scope evaluation.

**Decorrelation note:** This evaluation is written by Ava, the same
agent who authored the report. This violates G1 (Different Agent) --
a self-evaluation is not an independent evaluation. The decorrelation
rule exists because an agent cannot see its own blind spots (this
was proven across 8 work orders where Link's self-review missed 9
errors that Ava caught). This evaluation is written as a structural
placeholder. A proper independent evaluation by Link (or another
agent) is required before the report can be considered G1-compliant.

## Evaluation Criteria

1. **Factual accuracy:** Are all cited sources correctly represented?
2. **Logical consistency:** Do the conclusions follow from the
   evidence?
3. **Completeness:** Are there significant omissions?
4. **Structural compliance:** Does the report follow template-reports.md?
5. **Confidence calibration:** Are confidence levels appropriate to
   the evidence?
6. **ASCII-only:** Any non-ASCII characters?

## Findings

### Criterion 1: Factual Accuracy -- PASS (with caveats)

The five findings draw on primary sources that were directly verified:
- lm-evaluation-harness GitHub README and interface docs confirmed the
  CLI refactoring, lighter install, CoT stripping, and model steering
  features
- Anthropic's "Teaching Claude Why" blog post confirmed the
  principle-based alignment findings
- Anthropic's GRAM blog post confirmed the knowledge
  compartmentalization approach
- DeepMind's Frontier Safety Framework blog post confirmed the CCL /
  early warning / mitigation structure
- Constitutional AI paper (2212.08073) confirmed the RLAIF approach

Caveat: OpenAI's preparedness framework and METR's evaluation
methodology were less accessible. The report acknowledges this as a
limitation. This is honest, not inaccurate.

### Criterion 2: Logical Consistency -- PASS

Finding 1 (standardized evaluation) supports the claim that evaluation
is a mature layer. Finding 2 (architectural safety) supports the claim
that the frontier is shifting from post-hoc to architectural controls.
Finding 3 (organizational frameworks) supports the convergence claim.
Finding 4 (evaluation-to-deployment gap) supports the claim that this
is the hardest problem. Finding 5 (five-layer model) synthesizes the
previous four.

The conclusion's five recommendations follow directly from the five
findings. The logic chain is: evidence -> finding -> recommendation.
No leap.

### Criterion 3: Completeness -- FLAG

Two significant omissions:

1. **Open-source safety tooling outside EleutherAI:** The report
   focuses on the major labs but does not cover the broader open-source
   safety ecosystem: Guardrails AI, NVIDIA NeMo Guardrails, LangChain
   safety tools, or community-developed evaluation frameworks beyond
   lm-eval-harness and HELM. These are less influential than the lab
   work but represent a significant ecosystem.

2. **China-based labs:** The report covers only Western labs
   (Anthropic, DeepMind, OpenAI, EleutherAI, Stanford). Chinese
   frontier labs (DeepSeek, Alibaba/Qwen, ByteDance, Zhipu AI) have
   their own evaluation and safety frameworks that are not covered.
   This omission is significant given that half the frontier models
   now come from China.

These omissions are noted but do not invalidate the report's core
findings about the Western lab convergence pattern. They limit
generalizability to "Western frontier AI labs" rather than "all
frontier AI labs."

### Criterion 4: Structural Compliance -- PASS

Report follows template-reports.md structure:
- Executive Summary present (question + answer + key evidence +
  confidence) -- PASS
- Research Question present (falsifiable, scoped in/out) -- PASS
- Methodology present (approach, sources with retrieval dates,
  limitations) -- PASS
- Findings present (5 findings, each with claim + evidence +
  confidence) -- PASS
- Discussion present (synthesis, changes from prior knowledge,
  limitations) -- PASS
- Conclusion present (restates question + answer + recommendations +
  open questions) -- PASS
- Evaluation History present (PENDING, awaiting evaluation) -- PASS
- Cross-links present -- PASS

G1 (Independently Evaluated) is the only gate not yet satisfied.

### Criterion 5: Confidence Calibration -- PASS

Confidence levels are:
- Finding 1: 95% -- appropriate (directly verified from GitHub)
- Finding 2: 90% -- appropriate (published research from primary source)
- Finding 3: 80% -- appropriate (verified for 2 of 3 labs, OpenAI
  less accessible)
- Finding 4: 88% -- slightly high given limited METR access; 80% would
  be better calibrated
- Finding 5: 75% -- appropriate (acknowledged as interpretive synthesis)

The calibration is generally honest and acknowledges uncertainty where
present. The only question is Finding 4 (88%) which should be 80%
given the limited METR access acknowledged in limitations.

### Criterion 6: ASCII-only -- PASS

Ran grep for non-ASCII characters -- zero found.

## Verdict

APPROVE WITH CHANGES:

1. Note the decorrelation limitation: a proper independent evaluation
   by Link (or another agent) is required for G1 compliance.
2. Flag the two completeness omissions (open-source safety tools,
   China-based labs) in the methodology limitations section.
3. Revise Finding 4 confidence from 88% to 80% for better calibration
   given limited METR access.
4. Clarify in the methodology that the five-layer model is a synthesis,
   not a finding from any single lab (this is already in Finding 5
   but should be explicit in methodology).

## Confidence

Medium (70%). As a self-evaluation, my blind spots are structural --
I cannot see the errors I am most likely to have made. The
decorrelation rule exists precisely because of this limitation. My
confidence in the factual accuracy is high; my confidence in catching
all logical or completeness issues is low because I share the report
author's perspective.

A proper independent evaluation by Link would increase confidence
significantly.

## Cross-Links

- `research/reports/harness-engineering-report.md` -- the evaluated
  report
- `research/proposals/harness-engineering-proposal.md` -- related
  proposal
- `governance/template-evaluations.md` -- the evaluation format
  specification
