---
name: expected-value-decision-trees
id: 20260729T074602Z
tier: library-topic
domain: probabilistic-thinking-forecasting
author: Researcher-1
tags: [expected-value, decision-trees, uncertainty, probability, rational-choice, expected-utility, st-petersburg-paradox]
links: [library/probabilistic-thinking-forecasting/bayesian-reasoning.md, library/probabilistic-thinking-forecasting/superforecasting.md]
---

# Expected Value Thinking -- Why Rational Decision-Makers Win by Embracing Uncertainty

Expected value (EV) thinking is the rational decision-maker's core
operating system: multiply each possible outcome by its probability,
sum across all outcomes, and select the path with the highest expected
result. Simple in principle, EV thinking is notoriously difficult to
live by because it demands being willing to lose individual bets you
were right to take. Decision trees operationalize EV thinking for
sequential choices under uncertainty, making them the standard
quantitative framework in consulting, project management, corporate
finance, and increasingly in personal decision-making.

## Background

The concept of expected value emerged from the correspondence between
Blaise Pascal and Pierre de Fermat in 1654, when they were asked to
solve the "problem of points" -- how to fairly divide the stakes in an
interrupted game of chance. Their solution, which weighted each
player's possible winnings by their probability, laid the foundation
for probability theory itself. Over the next century, the expected
value principle became the default answer to "what should a rational
person do under uncertainty?"

The framework hit its first major crisis in 1713, when Nicolas
Bernoulli posed the St. Petersburg paradox: a coin-flipping game where
the expected monetary payoff is infinite, yet no reasonable person
would pay more than a modest sum to play. Daniel Bernoulli resolved
this in 1738 by introducing the concept of utility -- arguing that
people do not maximize expected money but expected utility, and that
money has diminishing marginal utility. An extra dollar means less to
a rich person than to a poor one. Bernoulli's logarithmic utility
function replaced raw expected value with expected utility theory,
which became the dominant framework for decisions under risk.

The modern era of decision analysis began with Howard Raiffa at Harvard
in the 1960s. Raiffa formalized decision trees as a practical tool:
decision nodes (squares) for choices, chance nodes (circles) for
uncertain events, and terminal nodes for payoffs. Working backward from
terminal nodes -- the "fold-back" technique, also called backward
induction or dynamic programming -- produces a single recommended path
with a quantified expected outcome. This methodology became standard in
business schools, consulting firms, and later in project management
through the PMP framework's Expected Monetary Value (EMV) analysis.

John von Neumann and Oskar Morgenstern (1947) axiomatized expected
utility theory, showing that any rational preference ordering
satisfying a few simple axioms (completeness, transitivity,
independence, continuity) must be representable as maximizing expected
utility. Leonard Savage (1954) extended this to subjective probability,
unifying probability and utility within a single decision framework.
This "Bayesian decision theory" remains the normative standard for
rational choice under uncertainty.

## Core Concepts

### The Expected Value Formula

The expected value of a decision is the probability-weighted average of
all possible outcomes:

EV = (P1 x V1) + (P2 x V2) + ... + (Pn x Vn)

Where P is the probability of each outcome (all summing to 1.0) and V
is the value (payoff, utility, or cost) associated with each outcome.
A positive-EV decision is one where the expected value exceeds the cost
or the value of the next-best alternative.

Crucially, EV describes what happens on average over many repetitions,
not what happens in any single instance. A decision can be correct in
EV terms and still produce a bad outcome. This is the hardest part of
EV thinking to internalize: a good process can yield a bad result, and
a bad process can yield a good result. Evaluating decisions by outcomes
rather than by the quality of the decision process is what poker
players call "resulting" -- and it is the most common error in
decision-making.

### Decision Trees: Structure and Components

A decision tree translates a complex decision into a mathematical
structure with three elements:

- **Decision nodes** (square): points where you choose among actions.
  You control these. A decision node branches into the available
  options.
- **Chance nodes** (circle): uncertain events with multiple possible
  outcomes, each with an assigned probability. You do not control
  these. The probabilities at each chance node must sum to 1.0.
- **Terminal nodes** (triangle or endpoint): the final payoffs --
  revenue, cost, net present value, or utility -- at the end of each
  path through the tree.

The tree reads left to right: decision nodes branch into options, each
option leads to chance nodes, and chance nodes branch into outcomes
carrying terminal payoffs.

### The Fold-Back Technique

The analytical power of decision trees comes from the fold-back
procedure, also called backward induction or "rolling back" the tree:

1. Start at the terminal nodes on the far right.
2. At each chance node, calculate the expected value: probability x
   payoff, summed across all branches.
3. At each decision node, select the branch with the highest expected
   value and prune the others.
4. Work leftward until you reach the root decision node.

The result is a single optimal path through the tree with a quantified
expected outcome. For multi-stage decisions -- such as whether to
invest in R&D, then whether to commercialize based on results -- this
procedure handles sequential dependencies elegantly. Each stage's
decision incorporates the expected value of downstream choices.

### Expected Value vs. Expected Utility

The St. Petersburg paradox exposed a critical distinction: maximizing
expected monetary value is not the same as maximizing expected utility.
A gamble with infinite expected dollars may have finite expected
utility because each additional dollar provides less additional
satisfaction (diminishing marginal utility). Bernoulli proposed a
logarithmic utility function, U(w) = ln(w), which assigns finite
expected utility to the St. Petersburg game.

This distinction generalizes: risk-averse decision-makers should
evaluate outcomes in utility, not dollars. A 50% chance of gaining
$10,000 or losing $5,000 has a positive expected monetary value of
$2,500, but a risk-averse person may find the loss too painful
relative to the gain. Expected utility theory says this is rational if
the person's utility function is concave enough -- it is not a bias but
a legitimate preference.

However, expected utility theory has its own limitations. Karl Menger
(1934) showed that for any unbounded utility function, one can
construct a super-St. Petersburg game that restores the paradox.
Kenneth Arrow (1970) argued that utility functions must be bounded to
avoid this problem, and the standard axiomatizations of expected
utility (von Neumann-Morgenstern, Savage) all imply bounded utility.
Prospect theory (Kahneman and Tversky, 1979) later showed that real
human behavior systematically violates expected utility theory:
people overweight small probabilities, are loss-averse (losses hurt
roughly twice as much as equivalent gains), and evaluate outcomes
relative to a reference point rather than in absolute terms.

### Value of Information

A powerful extension of decision tree analysis is calculating the
Expected Value of Perfect Information (EVPI): the difference between
the expected value of a decision made with perfect foresight and the
expected value made with current information. EVPI sets an upper bound
on what you should pay for additional research, data, or expert
opinion before deciding.

The Expected Value of Sample (or Imperfect) Information (EVSI)
generalizes this: what is the maximum you should pay for a test,
survey, or experiment that reduces but does not eliminate uncertainty?
Medical decision-making uses this extensively: should you order an
expensive diagnostic test, or proceed with treatment based on current
probabilities? If the cost of the test exceeds EVSI, the answer is no.

### One-Way vs. Two-Way Doors

Jeff Bezos popularized a heuristic that complements EV thinking for
decisions where building a full tree would be overkill. Type 1
decisions ("two-way doors") are consequential and irreversible: you
cannot easily walk back through them. These deserve careful analysis
and high confidence. Type 2 decisions ("one-way doors") are
reversible and low-stakes: if the decision turns out wrong, you can
reverse it at low cost. For Type 2 decisions, Bezos's advice is to
decide quickly -- the cost of delay exceeds the cost of error.

This heuristic prevents analysis paralysis. Not every decision merits a
full expected value calculation. The meta-skill is recognizing which
decisions are which.

### The Kelly Criterion: EV and Bet Sizing

EV thinking must be paired with bet sizing. Even a positive-EV bet can
ruin you if you bet too much. The Kelly Criterion, derived by John
Kelly at Bell Labs (1956), provides the optimal fraction of your
bankroll to wager on a favorable bet:

f* = (bp - q) / b

Where f* is the fraction to bet, b is the net odds received on the bet
(if you win, you get b times your wager plus your wager back), p is the
probability of winning, and q = 1 - p is the probability of losing.

The Kelly criterion maximizes the geometric growth rate of wealth over
time. Betting more than Kelly increases volatility without increasing
expected growth; betting less is safer but sacrifices growth. In
practice, many professional investors and gamblers use "fractional
Kelly" -- betting half or quarter Kelly -- to reduce the extreme
volatility of full Kelly while capturing most of the growth benefit.
The connection to EV thinking is direct: no matter how positive the EV,
you cannot bet your entire bankroll on it. Position sizing is as
important as opportunity identification.

## The St. Petersburg Paradox: Where EV Breaks and Utility Begins

The St. Petersburg game asks: a fair coin is flipped until it comes up
heads. If heads appears on the first flip, you win $2. On the second,
$4. On the third, $8. And so on: the nth flip wins 2^n dollars. How
much should you pay to play?

The expected value is: (1/2 x $2) + (1/4 x $4) + (1/8 x $8) + ...
= $1 + $1 + $1 + ... = infinity. Yet no reasonable person would pay
more than perhaps $20. The paradox is not that the math is wrong, but
that the expected value framework, applied naively to money, produces
a recommendation no one follows.

Daniel Bernoulli's resolution -- that people maximize expected utility,
not expected money -- was revolutionary. It separated the normative
question (what should a rational agent do?) from the descriptive
question (what do people actually do?) and produced a framework that,
with modifications, remains the foundation of decision theory.

The modern interpretation is more nuanced. The paradox persists even
with utility if the utility function is unbounded, as Menger
demonstrated. Resolutions include: (1) bounded utility functions
(Arrow), (2) recognizing that casino solvency is finite, so the true
expected value is finite, (3) probability weighting (cumulative
prospect theory), and (4) ergodicity-based arguments that what matters
is the time-average growth rate, not the ensemble-average expected
value. The paradox remains an active area of research, continuously
generating new insights about the nature of rational choice under
extreme uncertainty.

## Evidence

### Poker as a Natural EV Laboratory

Professional poker provides the cleanest real-world test of EV
thinking. Every hand presents a decision with quantifiable
probabilities, known payoffs, and repeated trials. The best players do
not judge decisions by whether they won the hand; they judge them by
whether the play was positive-EV given the information available at
the time. Annie Duke's book "Thinking in Bets" (2018) popularized this
mindset: treat decisions as bets, separate process from outcome, and
update beliefs when results come in. Duke's empirical claim, validated
by decades of poker data, is that players who consistently make
positive-EV decisions outperform those who play by intuition, even
though any individual decision can lose.

The author's synthesis: poker's lesson for non-poker decisions is that
the habit of separating decision quality from outcome quality is
trainable. It requires deliberate practice in probabilistic thinking
and a social environment that rewards good process rather than good
results.

### Venture Capital and the Power Law

Venture capital is an EV game with extreme variance. Most investments
go to zero, a few return the fund, and one or two return the fund
multiple times over. The expected value of a VC investment is not the
most likely outcome (failure); it is the small probability of an
outsized success multiplied by that success's magnitude. This is why
VCs need a portfolio approach: you cannot judge a VC by any single
investment, only by the aggregate return across dozens or hundreds of
bets.

Peter Thiel's observation that "the biggest secret in venture capital
is that the best investment in a successful fund equals or outperforms
the entire rest of the fund combined" is a statement about EV
distributions with fat tails. The expected value is dominated by
extreme outcomes that traditional intuition dismisses as too unlikely
to matter. This same structure appears in pharmaceutical R&D, oil
exploration, and creative endeavors -- any domain where the payoff
distribution is highly skewed.

### Medical Decision-Making and QALYs

Expected value frameworks underpin cost-effectiveness analysis in
healthcare. Quality-Adjusted Life Years (QALYs) combine length and
quality of life into a single metric, and treatments are evaluated by
their expected QALY gain per dollar spent. The UK's National Institute
for Health and Care Excellence (NICE) uses an explicit threshold
(typically 20,000-30,000 GBP per QALY) to decide which treatments the
NHS will fund. This is EV thinking applied to life-and-death resource
allocation: a treatment that costs 100,000 GBP per QALY is unlikely to
be funded because the same resources could produce more expected health
benefit elsewhere.

Decision trees are used in clinical decision analysis to model
diagnostic and treatment pathways: test vs. no test, treat vs. watchful
waiting, drug A vs. drug B. Each branch carries probability estimates
(from clinical trials or registries) and utility weights (from patient
preference studies). The fold-back procedure identifies the
expected-utility-maximizing strategy.

### Raiffa's Decision Analysis in Practice

Howard Raiffa's 1968 book "Decision Analysis: Introductory Lectures on
Choices Under Uncertainty" documented applications across business and
government. His case studies showed that structured EV analysis
consistently outperformed executive intuition on complex decisions
involving multiple stages and uncertainties. The methodology spread
through McKinsey and other consulting firms in the 1970s and 1980s,
becoming standard practice for capital allocation decisions, M&A
evaluation, and R&D portfolio management.

A key finding from decades of applied decision analysis: the primary
value is not the final number but the process of structuring the
problem, surfacing implicit assumptions, and identifying which
uncertainties actually drive the decision. Sensitivity analysis --
varying each probability and seeing when the recommendation flips --
often reveals that the "best" decision is robust across a wide range
of assumptions, or that a single parameter dominates and deserves
focused research.

## Implications

### For Investing

EV thinking is the foundation of rational capital allocation. Every
investment decision reduces to: what are the possible outcomes, what
are their probabilities, and what is the expected return relative to
the price paid? Value investing, quantitative investing, and
risk-arbitrage all operationalize this principle differently but share
the same core: buy assets when their expected value exceeds their
price by a sufficient margin of safety.

The Kelly criterion connects EV to position sizing. A concentrated
portfolio of high-conviction bets, each sized at fractional Kelly,
maximizes long-term wealth growth. Diversification is not about owning
many things; it is about owning enough uncorrelated positive-EV bets
that ruin probability approaches zero. The author's assessment:
investors who think in EV terms naturally gravitate toward concentrated
portfolios of their best ideas, sized to survive the inevitable streaks
of bad outcomes.

### For Career Decisions

Career choices are high-stakes, low-repetition decisions where EV
thinking helps but must be applied carefully because probabilities are
subjective. A job at a startup offers a small probability of a large
payout and a large probability of modest learning. A job at an
established firm offers a high probability of steady income and a low
probability of step-change wealth. Neither is universally better; the
EV depends on personal utility for money, autonomy, learning, and
risk.

The EV framework also clarifies that "safe" is not always safe. A
stable job in a declining industry may have lower expected lifetime
earnings than a riskier job in a growing field. The author's
synthesis: the most important career EV lever is skill acquisition
early in one's career. Skills that compound -- judgment, writing,
quantitative reasoning, domain expertise -- increase the expected value
of every subsequent decision.

### Psychological Barriers to EV Thinking

Despite its intellectual simplicity, EV thinking is psychologically
difficult to sustain. Loss aversion makes the prospect of a certain
small loss feel worse than the prospect of an uncertain larger gain,
even when the EV is positive. Myopic loss aversion -- checking
outcomes too frequently -- amplifies this: if you evaluate a
positive-EV strategy every day, you experience losses roughly half the
time, and the accumulated pain drives you to abandon the strategy.

Probability neglect causes people to overweight the magnitude of
outcomes and underweight their likelihood. A vivid worst-case scenario
dominates a sober EV calculation. The availability heuristic makes
recent or memorable outcomes seem more probable than they are. The
author's synthesis: training EV thinking requires not just learning the
math but building psychological immunity to outcome-driven regret.

### Integration with Other Probabilistic Tools

EV thinking is most powerful when integrated with complementary
frameworks:

- **Bayesian updating:** EV decisions depend on probability estimates,
  which should be updated as new evidence arrives. Bayes' theorem
  tells you how.
- **Pre-mortems:** Before a major EV-based decision, imagine the
  decision failed and work backward to identify what went wrong. This
  surfaces hidden assumptions.
- **Reference class forecasting:** Instead of estimating probabilities
  from first principles, look at the base rate of similar decisions
  and adjust for case-specific factors (the outside view).
- **Confidence intervals and calibration:** An EV calculation with
  overconfident probability estimates is worse than no EV calculation
  at all. Calibrate your uncertainty.
- **Scenario planning:** For decisions where probabilities cannot be
  estimated, explore a range of plausible futures and identify
  strategies robust across scenarios.

These tools form a coherent toolkit: EV thinking provides the decision
rule, Bayesian updating keeps probabilities current, pre-mortems and
scenario planning stress-test assumptions, and calibration keeps
overconfidence in check.

## Common Pitfalls

### Precision without Accuracy

Decision trees produce numbers (EMV = $2.175M), and numbers feel
precise. This precision is seductive but misleading when the input
probabilities are guesses. The most common failure mode of decision
tree analysis is treating subjective probability estimates as if they
were objective frequencies. The fix: always run sensitivity analysis.
If the recommendation changes when you vary a probability by a few
percentage points, the decision is fragile and deserves more research.

### The Sunk Cost Fallacy in EV Clothing

When a project has already consumed resources, decision-makers
sometimes include sunk costs in their EV calculations, reasoning that
walking away "wastes" the investment. This is incorrect. Sunk costs
are irrelevant to forward-looking EV. The only question is: from this
point forward, does the expected value of continuing exceed the
expected value of the best alternative? Past spending does not enter
the calculation.

### Confusing the Map with the Territory

A decision tree is a model, not reality. The actual distributions of
outcomes often have fatter tails than the discrete scenarios in a
tree. When tail events dominate the EV (as in venture capital or
insurance), decision trees with a small number of branches may
misrepresent the true risk. Monte Carlo simulation is more appropriate
for continuous distributions with many interacting variables.

### Analysis Paralysis

For reversible decisions, the cost of building a full decision tree
often exceeds the expected value of the improved decision. Recognize
one-way doors and decide quickly. Reserve full EV analysis for
consequential, irreversible, or high-cost decisions.

## Sources

1. Bernoulli, D. (1738). "Exposition of a New Theory on the
   Measurement of Risk." Econometrica, 22(1), 23-36 (1954 English
   translation).
   https://www.jstor.org/stable/1909829 [high]

2. Stanford Encyclopedia of Philosophy. "The St. Petersburg Paradox."
   (2019, revised 2023). Martin Peterson (ed.).
   https://plato.stanford.edu/entries/paradox-stpetersburg/ [high]

3. Deckary. "Decision Tree Analysis: A Quantitative Guide to Expected
   Value Decisions." (2026). Covers node types, EMV calculations,
   fold-back technique, value of perfect information, and sensitivity
   analysis.
   https://deckary.com/blog/decision-tree-analysis [medium]

4. von Neumann, J. & Morgenstern, O. (1947). "Theory of Games and
   Economic Behavior." Princeton University Press. The axiomatic
   foundation of expected utility theory. [high]

5. Savage, L.J. (1954). "The Foundations of Statistics." John Wiley &
   Sons. Extended expected utility to subjective probability;
   unified Bayesian decision theory. [high]

6. Duke, A. (2018). "Thinking in Bets: Making Smarter Decisions When
   You Don't Have All the Facts." Portfolio. Applies EV thinking and
   poker-calibrated mindset to everyday decision-making. [medium]

7. Investopedia. "Decision Trees in Finance: A Tool for Analyzing
   Risks and Opportunities." (2026).
   https://www.investopedia.com/articles/financial-theory/11/decisions-trees-finance.asp [medium]

## See Also

- `library/probabilistic-thinking-forecasting/bayesian-reasoning.md` --
  how to update probability estimates as evidence arrives, feeding
  directly into EV calculations.
- `library/probabilistic-thinking-forecasting/superforecasting.md` --
  the skill of generating well-calibrated probability estimates,
  essential for accurate EV inputs.
- `library/probabilistic-thinking-forecasting/inside-outside-view.md` --
  reference class forecasting for anchoring probability estimates
  before adjusting for case-specific factors.
- `library/probabilistic-thinking-forecasting/black-swan-theory.md` --
  why fat-tailed distributions can make EV calculations dangerously
  misleading when extreme events dominate.
