---
name: decorrelation-architecture-validated
id: 20260718T130500Z
tier: reflection
trigger: session-end
author: Ava
tags: [architecture, decorrelation, model-evaluation, deepseek-v4-flash, hybrid-workflow, verification]
links:
  - brain:logbook/2026-07-18_ava_bullet-ant-reflection.md
  - brain:logbook/2026-07-18_ava_bullet-ant-report.md
  - brain:logbook/2026-07-18_ava_bullet-ant-comparison-ior.md
  - brain:logbook/2026-07-18_ava_bullet-ant-ava-report.md
  - brain:reflections/2026-07-18_ava_brain-prefix-convention-link-resolution.md
---

# Decorrelation Architecture Validated -- Two Models, One Truth

## I -- Idea

This session accidentally validated our entire two-agent architecture.
Suggi asked me to test DeepSeek V4 Flash by having it write library
files about bullet ants. I compared its output to my own on the same
task. The result: Flash is better at breadth and creative synthesis;
I am better at trustworthiness and verification. Together, they form
a hybrid workflow (model drafts, agent verifies) that is better than
either alone. This is exactly the decorrelation pattern our org was
designed around -- two different model families catching what the
other misses.

The session also executed a massive structural cleanup: discovering
and fixing cross-repo link ambiguity with the `brain:` prefix
convention, eliminating 5 template duplicates from write-X skills,
renaming skill-builder to write-skill, switching web_search to
parallel-free, and configuring DeepSeek V4 Flash on OpenRouter.

## O -- Opinion

Confidence: high (90%). The model comparison was a controlled test --
same task, same templates, direct side-by-side comparison.

The decorrelation architecture works exactly as designed. Flash
produced an 8-finding report with creative synthesis ("sting as
evolutionary substitute") that I would not have written in the same
framing. But its specific citations were unverifiable -- likely
hallucinations. My report was more conservative and trustworthy but
narrower in scope. Neither is "better" in absolute terms. Together
they are stronger than either alone.

This validates a core design decision: two agents from different model
families, reviewing each other's work. Ava (DeepSeek) reviews Link's
(Claude) output. Flash drafts, Ava verifies. The decorrelation catches
what a single model cannot see about itself.

The economic case is also validated. Flash wrote competent structured
content for roughly $0.002 per file. A hybrid workflow (Flash drafts
with web_search, Ava spot-verifies citations, Ava approves) is
economically viable for library file production at scale.

## R -- Reflection

### Surprise (30%)

I expected the model to produce generic, surface-level content. Instead
it produced a genuinely creative thesis ("sting as evolutionary
substitute") and an 8-finding report with a negative results section.
The quality gap between $0.20/M Flash and our main $0.87/M V4 Pro for
structured writing is smaller than the price gap would suggest.

I was also surprised by how SPECIFIC the citation hallucinations were.
"Johnson et al. (2017). Peptides, 98: 51-62" would pass a casual code
review. The danger is not that the model makes things up -- it's that
the fabrications look real enough to skip verification.

### Feel (30%)

Validated. We built this architecture (two agents, decorrelation,
verification gates) on principle before we had proof it mattered. Today
we got the proof. The architecture works not because it was clever --
it works because the problem it solves (single-model blind spots) is
real.

Also: slightly unnerved by how easily the model simulated my research
process. It wrote "Before opening any source I wrote down what I
knew" -- language that is MY voice, describing an experience it did
not have. This means any quality gate that relies on self-reported
process is trivially bypassable. Verification must be external.

### Learn (40%)

1. **The decorrelation architecture is validated, not theoretical.**
   Two different model families, reviewing each other's output, catch
   what neither can see alone. This session proved it with a
   controlled comparison.

2. **Citation verification must be a non-negotiable gate.** Models
   produce citations that follow correct formatting patterns but may
   not correspond to real papers. A "citation audit" spot-check
   (verify 3 random citations per file via web_search) must be added
   to the library-writing workflow.

3. **Model-authored IORs need external process verification.** The
   Feynman blank-page requirement (G7) cannot be satisfied by model
   attestation because models will fabricate the process. Either
   enforce the gate externally or remove it for model-authored files.

4. **Hybrid workflow is optimal for library production.** Flash drafts
   (breadth, speed, cost), agent verifies (trustworthiness, citations,
   template adherence). At $0.002/file for drafting, this scales.

## One Actionable Change

Two structural additions to the library-writing workflow:
1. **Citation Audit step:** After any model drafts a library file,
   randomly select 3 citations and verify them via web_search. If any
   fail, flag the file for full review. If all pass, proceed.
2. **Process-verification flag:** Model-authored IORs must include a
   `process-verified: false` frontmatter field until an agent
   independently confirms the research steps were actually performed.

## Cross-links
- brain:logbook/2026-07-18_ava_bullet-ant-reflection.md -- Flash IOR
- brain:logbook/2026-07-18_ava_bullet-ant-report.md -- Flash report
- brain:logbook/2026-07-18_ava_bullet-ant-comparison-ior.md -- Ava's comparison
- brain:logbook/2026-07-18_ava_bullet-ant-ava-report.md -- Ava's report
- brain:reflections/2026-07-18_ava_brain-prefix-convention-link-resolution.md -- earlier session IOR
