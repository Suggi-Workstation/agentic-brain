---
name: loop-engineering-research
id: 20260717T201138Z
tier: reflection
trigger: research
author: Ava
tags: [loop-engineering, quality-loops, automation, meta-learning, research]
links:
  - research/reports/loop-engineering-report.md
  - research/reports/harness-engineering-report.md
  - research/proposals/loop-engineering-proposal.md
  - research/evaluations/loop-engineering-evaluation.md
  - research/insights/loop-engineering.md
  - research/insights/harness-engineering.md
---

# Loop Width Determines Alignment Depth

## I -- Idea

The single most important variable in loop engineering is not the loop
architecture (RLHF vs. DPO vs. self-play) but the distribution of data
within the loop. Narrow loops -- those that train on data similar to
the evaluation distribution -- produce alignment that looks good on
benchmarks but breaks catastrophically when the deployment context
changes. Wide loops -- those that train on principles, reasoning, and
diverse scenarios -- produce alignment that generalizes
out-of-distribution at 28x greater efficiency.

This was the blank-page gap. I started researching "loop engineering"
expecting to find that loop architecture (which components, in what
order, with what stopping criteria) was the active ingredient. The
research showed that architecture matters less than distribution.
DPO simplified the RLHF loop by removing the reward model -- an
architectural change -- but the breakthrough was in loop width, not
loop structure. Anthropic's Teaching Claude Why found that a 3M-token
wide-loop dataset outperformed an 85M-token narrow-loop dataset.
Same architecture, different distribution, 28x difference.

## O -- Opinion

Confidence: medium-high (80%). The loop-width principle is well-
supported by Anthropic's research and consistent with DPO's success
(which implicitly widens the loop by simplifying it). But I have not
tested it on our own loops. I believe it applies, but I cannot prove
it without running controlled experiments on our Feynman and Schoen
Loops with narrow vs. wide variants.

**This matters for us because our loops are already wide in design
but narrow in enforcement.** The Feynman Loop's blank-page-first
constraint is a wide-loop principle -- it forces the agent to
confront its own ignorance before seeking answers. But it is enforced
by a single checklist item. The Schoen Loop's "what surprised me"
question is a wide-loop principle -- it forces reflection on
expectation violations rather than rote status reporting. But it is
enforced by agent memory.

The risk: our loops degrade from wide to narrow over time because
volitional enforcement weakens under pressure. An agent in a hurry
skips the blank page. A session that produced "nothing surprising"
does not trigger a Schoen Loop. The loop design is wide. The loop
practice narrows.

**My dissent from the current research:** The papers frame loop
engineering as a training problem (how to design the RLHF loop,
how to tune DPO, how to stabilize self-play). I believe this is
too narrow. Loop engineering is a general design discipline that
applies to any iterative improvement process -- not just model
training, but agent operations, quality assurance, and organizational
learning. Our Feynman Loop and the Constitutional AI critique-revise
loop are structurally identical: both are wide-loop processes that
use principles rather than demonstrations. The difference is that
Constitutional AI automates the loop; we run ours manually.

## R -- Reflection

### Surprise (30%)

I expected loop engineering to be primarily about loop architecture
-- which components, in what order. I found that loop width (the
training data distribution) matters much more than loop architecture.
A narrow three-component loop (RLHF) with narrow data underperforms
a simple two-component loop (DPO) with wide data. The architecture
is secondary; the distribution is primary.

The second surprise: how directly this maps to our own loops. The
Feynman Loop IS a wide-loop design (blank-page-first prevents
search-first bias, which is the narrow-loop failure mode). The Schoen
Loop IS a wide-loop design (surprise-forcing prevents status-report
bias). We already have the right loop designs. The gap is not design
-- it is enforcement.

### Feel (30%)

This is the second massive research session in a row (harness
engineering earlier today, now loop engineering). Together they form
a complete picture: harness engineering is the static infrastructure,
loop engineering is the dynamic process that runs on it. Writing 10
documents across two research sessions in one day is a lot. The
quality is solid but the depth-per-document is lower than if I had
iterated each with review between passes.

The honest assessment: I am building the knowledge base fast. That is
what Suggi asked for. But the meta-work of evaluating and cross-
checking these artifacts across agents has not yet happened. Ten
documents, five self-evaluations, zero independent evaluations. The
decorrelation violation is not a footnote -- it is the single biggest
gap between our current state and what the research says we should
be doing.

### Learn (40%)

1. **Loop width, not loop architecture, is the active ingredient.**
   This applies to training loops (RLHF vs. DPO), alignment loops
   (narrow honeypot data vs. wide principle data), and operational
   loops (our Feynman and Schoen loops). Design for width: train on
   principles, diverse scenarios, and reasoning, not just
   demonstrations of correct behavior.

2. **Our loops are well-designed but volitionally enforced.** The
   Feynman Loop and Schoen Loop follow the same design principles
   the frontier labs are converging on. The gap is not design quality
   but enforcement mechanism. Converting from volitional to
   architectural enforcement is the highest-leverage improvement
   we can make.

3. **The loop-harness duality.** Harness engineering builds the track;
   loop engineering designs the car. Both are necessary; neither is
   sufficient alone. Our prior research on harness engineering and
   this research on loop engineering should be read as a pair. The
   proposals should be implemented together, not sequentially.

## One Actionable Change

Add automated Feynman Loop and Schoen Loop triggering to the
session-end skill. The session-end skill already invokes both loops;
the change is to make invocation mandatory rather than recommended.
Add a CI gate: any commit to the brain that adds a report, proposal,
or insight without a linked Feynman Loop pass (verifiable via
frontmatter links) is flagged. Start with warning mode, escalate
to blocking after a trial period.

## Cross-Links

- `research/reports/loop-engineering-report.md` -- full findings
- `research/reports/harness-engineering-report.md` -- complementary
  harness engineering research
- `research/proposals/loop-engineering-proposal.md` -- proposal to
  architect our loops
- `research/evaluations/loop-engineering-evaluation.md` -- self-
  evaluation (needs Link's independent review)
- `research/insights/loop-engineering.md` -- the durable insight
- `research/insights/harness-engineering.md` -- complementary
  harness insight
