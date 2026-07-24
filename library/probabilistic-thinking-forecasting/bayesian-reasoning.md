---
name: bayesian-reasoning
id: 20260724T162528Z
tier: library-topic
domain: probabilistic-thinking-forecasting
author: Ava
tags: [bayesian-reasoning, probability, belief-updating, base-rates, bayes-theorem, uncertainty]
links: [library/probabilistic-thinking-forecasting/anchor-probabilistic-thinking-forecasting.md, library/psychology-behavior/cognitive-biases.md, library/science/scientific-method-falsifiability.md]
---

# Bayesian Reasoning -- Updating Beliefs by Quantifying Uncertainty

Bayesian reasoning is a framework for updating beliefs about the world
in light of new evidence, grounded in probability theory and Bayes'
theorem. Rather than holding beliefs as true or false, the Bayesian
thinker assigns probabilities to hypotheses and revises them as data
arrives. This approach is not merely a statistical technique -- it is a
normative standard for rational belief: any reasoning that violates
Bayes' rule is provably incoherent. From medical diagnosis to
superforecasting to everyday judgment, Bayesian reasoning provides a
systematic method for moving from "I think" to "given what I have seen,
the odds are."

## Background

The theorem that powers Bayesian reasoning was discovered by Reverend
Thomas Bayes, an 18th-century English Presbyterian minister and
mathematician. His essay "An Essay towards solving a Problem in the
Doctrine of Chances" (1763), published posthumously by Richard Price,
contained the core insight: a mathematical rule for updating the
probability of a hypothesis given new observations. Independently,
Pierre-Simon Laplace rediscovered and generalized the theorem in 1774,
applying it to problems in astronomy, demography, and jurisprudence.
For most of the 19th and early 20th centuries, Bayesian methods were
marginalized in favor of frequentist statistics, which avoided the
subjectivity of prior probabilities.

The Bayesian revival began in the mid-20th century, driven by
statisticians who argued that all inference is necessarily Bayesian --
the only question is whether priors are stated explicitly or hidden.
Dennis Lindley, a leading British statistician, championed Bayesian
methods throughout his career and coined Cromwell's Rule: never assign
a prior probability of exactly 0 or 1 to any empirical proposition. In
the late 20th century, computational advances -- particularly Markov
Chain Monte Carlo (MCMC) methods -- made Bayesian inference practical
for complex problems, fueling its adoption in machine learning,
artificial intelligence, and the sciences. Today, Bayesian reasoning
has expanded beyond statistics: cognitive scientists propose that the
brain itself is a Bayesian prediction engine, and superforecasters
treat their judgments as probabilities to be continuously updated.

## Core Concepts

### Bayes' Theorem as a Belief-Updating Engine

Bayes' theorem, in its simplest form, states:

```
P(H|E) = P(E|H) * P(H) / P(E)
```

Where P(H) is the prior probability -- what you believed before seeing
the evidence. P(E|H) is the likelihood -- how probable the evidence is
if the hypothesis is true. P(E) is the total probability of observing
the evidence under all hypotheses. The result, P(H|E), is the posterior
probability -- what you should believe after accounting for the
evidence.

The key insight is that updating beliefs is mechanical. You do not need
to "decide" how much to update -- the math tells you. If the evidence
is highly likely under your hypothesis and highly unlikely under
alternatives, the posterior shifts sharply toward your hypothesis. If
the evidence is equally likely under all hypotheses, your belief does
not change. This process is iterative: today's posterior becomes
tomorrow's prior, and beliefs converge toward the truth as evidence
accumulates.

### Priors and the Problem of Base Rate Neglect

The prior probability is the Bayesian's starting point -- what you
believe before the specific evidence arrives. The most common failure
of Bayesian reasoning, and one of the most consequential reasoning
errors in human judgment, is base rate neglect: the systematic tendency
to ignore or underweight prior probabilities when new, vivid evidence
appears.

The classic demonstration is the medical test problem. Suppose a disease
affects 1% of the population, and a test for it is 90% accurate (90%
sensitivity and 90% specificity). A person tests positive. What is the
probability they have the disease? Most people, including many
physicians, answer approximately 90% -- anchoring on the test's
accuracy. The correct Bayesian answer is approximately 8%. Among 1,000
people, 10 have the disease (the base rate) and 990 do not. The test
catches 9 of the 10 sick people, but also produces 99 false positives
from the 990 healthy people. Of the 108 people who test positive, only
9 are actually sick -- roughly 8% (Gigerenzer & Hoffrage, 1995).

The practical fix is not to exhort people to "use base rates" but to
change how information is presented. Gerd Gigerenzer demonstrated that
recasting Bayesian problems in natural frequencies ("10 out of 1,000
people have the disease, and 9 of those 10 test positive") rather than
conditional probabilities triples the share of people who reach the
correct answer -- from approximately 16% to 46% (Gigerenzer & Hoffrage,
1995; Cosmides & Tooby, 1996). The human mind appears well-adapted to
reason about frequencies encountered through experience; it is the
unnatural format of single-event probabilities that produces the error.

### Cromwell's Rule and the Trap of Certainty

Cromwell's Rule, named by Dennis Lindley after Oliver Cromwell's plea
to the Church of Scotland ("I beseech you, in the bowels of Christ,
think it possible that you may be mistaken"), states that prior
probabilities of exactly 0 or 1 should never be assigned to any
empirical proposition. The reason is mechanical: if your prior is 0 or
1, Bayes' theorem guarantees that no amount of evidence can change your
mind. The posterior will always be 0 or 1, regardless of what you
observe.

Lindley's memorable formulation: "Leave a little probability for the
moon being made of green cheese; it can be as small as 1 in a million,
but have it there since otherwise an army of astronauts returning with
samples of the said cheese will leave you unmoved" (Lindley, cited in
statisticshowto.com). The principle applies to any empirical claim: you
should be willing to name the evidence that would change your mind. If
no conceivable evidence would do so, you are not reasoning -- you are
dogmatizing. This is the Bayesian foundation for the maxim "strong
opinions, weakly held": hold beliefs with conviction but assign
non-zero probability to being wrong, and update when the evidence
demands it.

### Likelihood Ratios and the Strength of Evidence

From a Bayesian standpoint, the strength of evidence is measured by the
likelihood ratio: P(E|H1) / P(E|H2) -- how much more probable the
evidence is under one hypothesis than another. A likelihood ratio of 10
means the evidence is ten times more likely under H1 than H2; a ratio
of 1 means the evidence is equally consistent with both and your belief
should not change.

This framing clarifies what makes evidence "strong" or "weak." Evidence
that is equally predicted by all competing hypotheses -- a test that
returns positive at the same rate whether or not the disease is present
-- has a likelihood ratio near 1 and is worthless, regardless of how
dramatic or vivid it appears. Conversely, evidence that is highly
specific to one hypothesis -- a test with near-zero false positive rate
-- can be extremely informative even if it is rare.

### The Outside View: Reference Class Forecasting

Daniel Kahneman, drawing on his experience in curriculum design
projects that ran dramatically over budget, distinguished between the
"inside view" and the "outside view." The inside view focuses on the
specific details of the case at hand -- the team's talent, the plan's
ingenuity, the unique circumstances. The outside view ignores all
specifics and asks: what happened when similar projects were attempted
in the past? The outside view is a Bayesian prior: before you adjust
for the specifics of this case, start with the base rate.

Philip Tetlock's research on superforecasters confirmed that Bayesian
updating is a core habit of the most accurate forecasters. In Tetlock's
Good Judgment Project, superforecasters would begin with a base rate
("what percentage of similar events occurred?") as their prior, then
update incrementally as new information arrived. They treated their
forecasts as hypotheses to be tested, not positions to be defended.
This is Bayesian reasoning in practice: start with the outside view,
update with the inside view, and never let the posterior reach 0 or 1
(Tetlock & Gardner, 2015).

## Evidence

The empirical case for Bayesian reasoning rests on two pillars:
demonstrations of what happens when people fail to use it, and
demonstrations of superior performance when they do.

**The base rate neglect literature** is the negative pillar. Across
decades of research, from Kahneman and Tversky's early heuristics-and-biases
work to Gigerenzer's natural frequencies research, the finding is
consistent: when people are presented with Bayesian reasoning problems
in probability format, the majority fail to incorporate base rates. The
medical test problem has been replicated with physicians, medical
students, and statistically trained professionals, all of whom
overestimate the posterior probability by an order of magnitude
(Gigerenzer & Hoffrage, 1995; Koehler, 1996).

**The superforecasting research** is the positive pillar. Tetlock's Good
Judgment Project identified a small group of individuals --
superforecasters -- whose probability judgments were consistently better
calibrated than those of professional intelligence analysts with access
to classified information. One of the defining habits of
superforecasters was Bayesian updating: they treated their initial
estimates as provisional, updated frequently as new information became
available, and maintained probability ranges that reflected genuine
uncertainty. Hedgehogs -- thinkers committed to one big idea -- were
consistently outperformed by foxes, who stitched together multiple
perspectives and updated their beliefs incrementally (Tetlock &
Gardner, 2015).

**The Bayesian brain hypothesis**, advanced by neuroscientist Anil Seth
and others, proposes that the brain itself implements a form of
Bayesian inference. Perception, under this view, is not a passive
recording of sensory data but an active process of prediction and error
correction: the brain generates predictions (priors) about sensory
input, compares them to actual input (likelihood), and updates its
internal model (posterior). This suggests that Bayesian reasoning is
not an exotic statistical technique but a formalization of what a
well-functioning brain already does -- and that conscious Bayesian
reasoning is simply extending this native capacity to domains where
intuition systematically fails (Seth, cited in Chivers, "The Bayesian
Brain").

## Implications

For **investors**, Bayesian reasoning is the intellectual foundation of
the margin of safety. An investor's thesis is a prior -- an estimate of
intrinsic value based on available information. As quarterly reports,
industry developments, and competitive dynamics unfold, the thesis is
updated. The investor who refuses to update -- who assigns a prior of 1
to their valuation -- is the investor who rides a losing position to
zero. The discipline of naming what would change your mind, and then
updating when it happens, is Bayesian discipline applied to capital
allocation.

For **medicine and law**, Bayesian reasoning prevents catastrophic
misinterpretation of evidence. The prosecutor's fallacy -- mistaking
the probability of a forensic match given innocence for the probability
of innocence given the match -- is base rate neglect in a courtroom. A
DNA match with a one-in-a-million random-match probability does not
mean a one-in-a-million chance the defendant is innocent; it depends on
the prior probability that the defendant is the source, which in turn
depends on the size of the suspect pool and other evidence. Bayesian
reasoning makes this dependence explicit.

For **everyday decision-making**, Bayesian reasoning provides an
alternative to the binary true/false mindset. Few important questions
admit of certainty. "Will this project succeed?" is not answerable with
yes or no -- it is answerable with a probability distribution that
should narrow as information accumulates. "Is this person trustworthy?"
is not a fixed trait to be discovered but a hypothesis to be updated.
The Bayesian habit is to hold beliefs as probabilities, name the
evidence that would shift them, and update when it arrives.

## Common Pitfalls

**Anchoring on the wrong prior.** The Bayesian framework gives no
guidance on selecting the initial prior -- it only specifies how to
update. A bad prior, updated correctly, converges slowly toward the
truth. The outside view and reference class forecasting are the best
available remedies: ground your prior in the base rate of what actually
happens, not in the narrative of what makes this case special.

**Over-updating on small samples.** Bayes' theorem updates continuously,
but it does not protect against over-interpreting noisy data. A single
data point from a small sample should produce a small update. The human
tendency is the opposite: a vivid anecdote shifts beliefs more than a
large but abstract dataset. The Bayesian remedy is to attend to sample
size when assessing the likelihood -- a small sample has wide
confidence intervals, so the likelihood ratio is weak.

**Priors are unavoidable, not optional.** A common objection to Bayesian
reasoning is that priors are subjective. The Bayesian response is that
all reasoning uses priors -- the only question is whether they are
stated explicitly (and therefore open to challenge) or hidden inside
implicit assumptions. A prior of "I will treat this company like the
average company in its industry" is explicit and debatable. A prior of
"I have a gut feeling about this management team" is implicit and
unexaminable. The Bayesian choice is the former, every time.

## Sources

1. Gigerenzer, G. & Hoffrage, U. (1995). "How to Improve Bayesian
   Reasoning Without Instruction: Frequency Formats." Psychological
   Review, 102(4), 684-704.
   https://pubmed.ncbi.nlm.nih.gov/7480466/ [high]

2. Tetlock, P. & Gardner, D. (2015). "Superforecasting: The Art and
   Science of Prediction." Crown Publishing Group.
   https://www.goodjudgment.com/research [high]

3. Yudkowsky, E. (2016). "Bayesian Reasoning." Arbital.
   https://arbital.com/p/bayes_reasoning [medium]

4. BayesianStatistics.com. "Cromwell's Rule."
   https://bayesianstatistics.com/Cromwells_Rule [medium]

5. Cosmides, L. & Tooby, J. (1996). "Are humans good intuitive
   statisticians after all? Rethinking some conclusions from the
   literature on judgment under uncertainty." Cognition, 58(1), 1-73.
   https://www.sciencedirect.com/science/article/abs/pii/0010027795006648 [high]

6. StatisticsHowTo.com. "Cromwell's Rule: Simple Definition."
   https://www.statisticshowto.com/cromwells-rule [medium]

## See Also

- `library/probabilistic-thinking-forecasting/anchor-probabilistic-thinking-forecasting.md` -- domain anchor defining the full scope of probabilistic thinking and forecasting.
- `library/psychology-behavior/cognitive-biases.md` -- the systematic thinking errors, including base rate neglect, that Bayesian reasoning helps correct.
- `library/science/scientific-method-falsifiability.md` -- how Bayesian updating provides a normative framework for scientific inference and why bold, falsifiable predictions are Bayesian virtues.
