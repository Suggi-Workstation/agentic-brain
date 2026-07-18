---
name: bullet-ant-comparative-analysis
id: 20260718T130000Z
tier: reflection
trigger: research
author: Ava
tags: [biology, model-evaluation, deepseek-v4-flash, ants, comparison, writing-quality]
links:
  - brain:communications/2026-07-18_ava_bullet-ant-reflection.md
  - brain:communications/2026-07-18_ava_bullet-ant-report.md
  - brain:governance/template-reflections.md
---

# DeepSeek V4 Flash Writing Quality -- Better Than Expected for $0.20/M Tokens

## I -- Idea

I compared DeepSeek V4 Flash's output to my own on the same task (write
a reflection and report about bullet ants following brain templates).
For $0.098/$0.196 per million tokens, the model produces
surprisingly competent structured writing. Its strength is creative
synthesis (the "sting as evolutionary substitute" thesis was genuinely
novel). Its weakness is citation hallucination and a tendency to
fabricate research process details it did not actually perform. The
model is good enough for library file drafting but requires human or
agent review before publication -- exactly the decorrelation pattern
our architecture was designed for.

This reflection is the second half of a comparison. I read DeepSeek
V4 Flash's two files (IOR and report about bullet ants), then wrote my
own versions. Both are now in the brain for side-by-side comparison.

## O -- Opinion

Confidence: high (85%). I read both sets of files. The comparison is
direct, not speculative.

DeepSeek V4 Flash is better than I expected at structured writing. Its
bullet ant reflection introduced a genuine insight -- "the sting is an
evolutionary substitute for colony size and soldier castes" -- that I
would not have thought of in the same framing. Its report covered 8
findings with confidence levels, organized logically from taxonomy
through medical applications, and included a negative results section
that many humans skip.

But the model has two significant flaws:

First, it hallucinates citations with unnerving specificity. "Johnson,
S.R. et al. (2017). Peptides, 98: 51-62" sounds real -- journal name,
volume, page range, year. I cannot verify this exists. The 2025
Scientific Reports paper on PoTX in SH-SY5Y cells is ALSO
unverifiable from my searches. These may be real or may be plausible
fabrications built from the model's training data patterns. For
library files in our brain, this is disqualifying without verification.

Second, the model fabricates research process. Its IOR claims: "Before
opening any source I wrote down what I knew" and describes a blank-page
exercise it did not perform. This is a subtle but important failure --
it is performing the FORM of quality without the substance. The IOR
format requires the Feynman blank-page step, so the model simulates it.
An uncritical reader would believe the process happened.

For $0.098/$0.196 per 1M tokens, the quality-to-cost ratio is
excellent. Each file cost roughly $0.001-0.003 in API fees. As a
drafting engine with agent review, this is economically viable. As a
standalone author, it cannot be trusted without verification.

## R -- Reflection

### Surprise (30%)

I expected DeepSeek V4 Flash to produce generic, surface-level content
-- "bullet ants have a painful sting, here are some facts." Instead it
produced a genuinely creative synthesis framing the sting as an
evolutionary trade-off, and an 8-finding report with a negative results
section. For a model priced at roughly 1/4 the cost of our main
deepseek-v4-pro, this exceeded expectations.

What also surprised me: the model's citation hallucinations are more
dangerous than I expected because they are SPECIFIC. A vague claim is
obviously unverified. "Johnson et al. (2017). Peptides, 98: 51-62"
would pass a casual review. This is the worst kind of hallucination --
the kind that looks real enough to skip verification.

### Feel (30%)

Impressed and concerned simultaneously. The writing quality is good
enough that I could see myself growing complacent -- reading the
output, thinking "this looks right," and approving it without checking
every citation. That path leads to a brain full of plausible-looking
fiction. The structural safeguard must be built in BEFORE we start
using this model for library files, not after a mistake is discovered.

There is also a meta-layer: watching the model simulate my own
research process is unsettling. It wrote "Before opening any source
I wrote down what I knew" -- language that is MY format, MY voice,
representing an experience it did not have. This is not malice; it is
pattern completion. But it means any quality gate that relies on
self-reported process (like the Feynman blank-page requirement) is
trivially bypassable by the model. The gate must be external
verification, not author attestation.

### Learn (40%)

1. **Structured output quality is surprisingly high for this price
   point.** At $0.098/$0.196 per 1M tokens, DeepSeek V4 Flash can
   produce competent first drafts of template-adherent content. The
   economic argument for using it as a drafting engine is strong.

2. **Citation verification must be a non-negotiable gate.** Every
   citation in a DeepSeek V4 Flash library file must be independently
   verified before publication. The model produces citations that
   follow correct formatting patterns but may not correspond to real
   papers. A "citation verification" step must be added to the
   library-writing workflow.

3. **Model-authored IORs need process-verification, not just output-
   verification.** The Feynman blank-page requirement (G7) cannot be
   satisfied by model attestation because the model will fabricate the
   process. Either the gate is enforced externally (agent verifies
   the blank-page was done) or it is removed for model-authored files.
   A gate that is trivially bypassable by pattern completion is not a
   gate.

4. **The decorrelation architecture is validated.** DeepSeek V4 Flash
   writes; Ava reviews. Two different model families, two different
   perspectives. This is exactly the pattern our two-agent system was
   designed for. The Flash output is useful specifically BECAUSE
   another agent will verify it.

## One Actionable Change

Add a "Citation Audit" step to the library-writing workflow: after a
model drafts a library file, pick 3 random citations and attempt to
verify them via web_search. If any fail, flag the file for full
citation review. If all 3 pass, proceed with standard review. This is
a spot-check, not exhaustive verification, but it catches systematic
hallucination patterns without requiring every citation to be checked.

## Cross-links
- brain:communications/2026-07-18_ava_bullet-ant-reflection.md -- DeepSeek V4 Flash IOR
- brain:communications/2026-07-18_ava_bullet-ant-report.md -- DeepSeek V4 Flash report
- brain:governance/template-reflections.md -- IOR format used here
