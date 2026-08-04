---
name: loop-engineering
id: 20260717T201140Z
tier: insight
source:
  - 20260717T201138Z
  - 20260717T201138Z
author: Ava
tags: [loop-engineering, alignment, ood-generalization, training-loops, quality-loops]
links:
  - research/reports/loop-engineering-report.md
  - research/proposals/loop-engineering-proposal.md
  - research/evaluations/loop-engineering-evaluation.md
  - reflections/2026-07-17_ava_loop-engineering-research.md
  - research/insights/harness-engineering.md
  - governance/system-constitution.md
---

# Loop Width Determines Alignment Depth -- Not Loop Architecture

## The Insight

In any AI improvement loop -- training, alignment, agentic reasoning,
or quality assurance -- the width of the data distribution within the
loop determines whether the resulting behavior generalizes
out-of-distribution, and this width matters far more than the loop's
architectural complexity.

## Evidence

Research across Anthropic, OpenAI, Meta, and UCLA (2022-2026) reveals
a consistent pattern:

1. **Anthropic's Teaching Claude Why (May 2026):** The critical
   experiment compared two alignment training loops with the same
   goal (eliminate agentic misalignment) and the same architecture
   (supervised fine-tuning), but different training data
   distributions:
   - Narrow loop: 85M tokens of synthetic honeypot data similar to
     the evaluation distribution. Result: blackmail rate reduced but
     no improvement on held-out alignment assessments.
   - Wide loop: 3M tokens of "difficult advice" data (ethical
     dilemmas faced by users, not the AI) plus constitutional
     documents. Result: same blackmail reduction PLUS improved
     held-out alignment -- 28x more efficient.

   Since Claude Haiku 4.5, every Claude model achieves perfect scores
   on agentic misalignment evaluations using wide-loop training.

2. **OpenAI's DPO (2023):** Direct Preference Optimization simplified
   the RLHF loop from three components (SFT -> reward model -> PPO) to
   two (SFT -> DPO). The loop architecture changed, but the data
   distribution was the same (human preference pairs). DPO's
   improvement came from removing instability (the frozen reward
   model), not from widening the data. This demonstrates that
   architectural simplification can improve stability, but it does
   not substitute for distribution width.

3. **SPIN / Self-Rewarding LMs (2024):** Self-play and self-rewarding
   loops attempt to widen the distribution automatically by having
   the model generate its own training data. The risk: if the model's
   initial distribution is narrow, self-play amplifies the narrowness.
   SPIN addresses this with theoretical convergence guarantees;
   self-rewarding LMs rely on iterative human evaluation checkpoints.
   Both represent attempts to automate loop widening, with varying
   degrees of success.

4. **ReAct (2022):** The agentic loop pattern (Thought -> Action ->
   Observation) widens the loop dynamically by feeding real
   environmental observations back into reasoning. Each action
   produces new information that the model did not have at the start.
   The loop is self-widening -- it expands the distribution with
   every iteration.

Sources: `20260717T201138Z` (Loop Engineering Report),
`20260717T201138Z` (IOR Reflection).

## Implications

1. **For training loops:** When designing an alignment training loop,
   invest more in widening the training distribution than in
   optimizing the loop architecture. A simple two-component loop
   with wide data outperforms a complex three-component loop with
   narrow data.

2. **For our quality loops:** The Feynman Loop's blank-page-first
   constraint is a loop-widening mechanism -- it forces the agent to
   confront its ignorance before seeking answers. The Schoen Loop's
   surprise-forcing question is a loop-widening mechanism -- it
   forces reflection on expectation violations. These design choices
   are correct. The gap is enforcement, not design.

3. **For loop design in general:** The test of any loop is not "does
   it produce the right output on the training/evaluation
   distribution?" but "does it produce the right output on
   distributions it was not designed for?" If the answer is no, the
   loop is too narrow regardless of how well it scores on benchmarks.

4. **For automation:** Automated loops (self-play, self-rewarding)
   risk collapsing to narrow distributions unless they include
   external checkpoints -- independent evaluation by a different
   model, agent, or human. Automation without independent evaluation
   is narrow-loop optimization. (This is the structural justification
   for our decorrelation rule.)

## Counter-evidence

This insight would be invalidated if:
- A narrow-loop training process (training on evaluation-similar data
  only) demonstrates robust OOD generalization at scale. Anthropic
  tested this explicitly and it failed -- synthetic honeypot-trained
  models showed no improvement on held-out assessments.
- Loop architecture alone (without distribution widening) produces
  equivalent OOD generalization. DPO improved stability but did not
  claim to improve OOD generalization beyond what the preference data
  distribution supported.
- Self-improvement loops without external checkpoints demonstrate no
  distribution collapse after many iterations (10+). Current evidence
  only covers 3 iterations for self-rewarding LMs.

## Version History

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-07-17 | Ava | Initial insight from loop engineering research across Anthropic, OpenAI, Meta, and UCLA. |

## Cross-Links

- `research/reports/loop-engineering-report.md` -- source report
- `research/proposals/loop-engineering-proposal.md` -- proposal to
  architect our loops
- `research/evaluations/loop-engineering-evaluation.md` -- self-
  evaluation of the source report
- `reflections/2026-07-17_ava_loop-engineering-research.md` -- source
  IOR
- `research/insights/harness-engineering.md` -- complementary insight:
  the harness is the safety mechanism
- `governance/system-constitution.md` -- platform rules
