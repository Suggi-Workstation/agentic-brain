---
name: prospect-theory
id: 20260726T110159Z
tier: library-topic
domain: psychology-behavior
author: Researcher-1
tags: [prospect-theory, loss-aversion, behavioral-economics, kahneman, tversky, decision-making, framing, endowment-effect]
links: [library/psychology-behavior/cognitive-biases.md, library/value-investing/margin-of-safety.md, library/probabilistic-thinking-forecasting/bayesian-reasoning.md]
---

# Prospect Theory -- Why Losses Feel Twice as Painful as Gains Feel Good

Prospect theory, developed by Daniel Kahneman and Amos Tversky in
1979, is the most influential descriptive theory of how people actually
make decisions under risk. It replaced expected utility theory -- the
long-dominant normative model of rational choice -- with an empirically
grounded alternative that accounts for systematic human deviations from
rationality: people evaluate outcomes as gains and losses relative to a
reference point rather than in absolute terms, they weight probabilities
nonlinearly, and they feel losses approximately twice as intensely as
equivalent gains. Kahneman received the 2002 Nobel Prize in Economics
for this work (Tversky having died in 1996), and the theory launched
the field of behavioral economics.

## Background

Before prospect theory, the dominant framework for understanding
decision-making under risk was expected utility theory, formalized by
John von Neumann and Oskar Morgenstern in 1944. Expected utility theory
assumed that rational agents evaluate outcomes in terms of their effect
on total wealth, weight each possible outcome by its objective
probability, and choose the option that maximizes expected utility.
This model was normatively elegant -- it described how a perfectly
rational agent should choose, not how people actually do choose.

By the 1970s, Kahneman and Tversky had accumulated substantial evidence
that human decision-makers systematically violate the axioms of
expected utility theory. People were risk-averse for gains but
risk-seeking for losses -- a pattern impossible under standard utility
theory. People treated identical outcomes differently depending on how
they were framed. People overweighted small probabilities (explaining
why they buy lottery tickets and insurance simultaneously) and
underweighted moderate to high probabilities. People's choices depended
on reference points, not absolute wealth levels.

In their landmark 1979 paper "Prospect Theory: An Analysis of Decision
under Risk," published in Econometrica, Kahneman and Tversky proposed
an alternative model organized around two functions: a value function
that replaces the utility function, and a probability weighting
function that replaces objective probabilities with decision weights.
The paper became one of the most cited in the history of economics.
Richard Thaler, who would later win the 2017 Nobel Prize in Economics,
spent the following decades translating prospect theory's laboratory
findings into practical economic applications: mental accounting, the
endowment effect, the disposition effect, and the behavioral
life-cycle hypothesis.

A significant theoretical refinement came in 1992 when Tversky and
Kahneman published "Advances in Prospect Theory: Cumulative
Representation of Uncertainty," which introduced cumulative prospect
theory. This version replaced the original probability weighting
approach with rank-dependent weighting, solving a technical problem
(original prospect theory could violate stochastic dominance) and
extending the theory to uncertain prospects with many outcomes.

## Core Concepts

### The Value Function

The value function is the centerpiece of prospect theory. It replaces
the standard utility function with three defining properties, each
backed by experimental evidence.

**Reference dependence.** Outcomes are not evaluated in absolute
terms of final wealth but as gains or losses relative to a reference
point. That reference point is typically the status quo, but it can
shift depending on framing, expectations, or social comparisons.
A person earning $80,000 per year evaluates a raise to $90,000 as a
$10,000 gain, not as the difference between two absolute wealth levels.
This property explains why framing effects are so powerful: the same
objective outcome can be experienced as either a gain or a loss
depending on how the reference point is set.

**Loss aversion.** The value function is steeper in the loss domain
than in the gain domain. Empirically, the pain of losing $100 is
roughly 2.25 times as intense as the pleasure of gaining $100. Tversky
and Kahneman (1992) estimated this loss aversion coefficient (lambda)
at approximately 2.25 based on experimental data from college students
making choices among monetary gambles. This asymmetry is the single
most consequential finding in behavioral economics because it implies
that people will reject bets with positive expected value if there is
any chance of loss, and that people will take risks to avoid sure
losses that they would never take to achieve sure gains.

**Diminishing sensitivity.** Both gains and losses exhibit diminishing
marginal impact as their magnitude increases. The difference between
winning $0 and $100 feels far larger than the difference between
winning $1,000 and $1,100. Similarly, the difference between losing $0
and $100 is more painful than the difference between losing $1,000 and
$1,100. Mathematically, the value function is concave in the gain
domain and convex in the loss domain, producing an S-shaped curve
centered at the reference point. The 1992 parameterization used a
power function with an exponent (alpha and beta) of approximately 0.88
for both gains and losses.

### The Probability Weighting Function

The second major innovation of prospect theory is the probability
weighting function. People do not treat stated probabilities as linear
weights -- they systematically transform them. The weighting function
has an inverse-S shape: small probabilities (below roughly 0.35) are
overweighted, and moderate to large probabilities (above roughly 0.35)
are underweighted.

This single nonlinearity explains several paradoxes of human behavior.
People buy both lottery tickets (overweighting the tiny probability of
winning) and insurance policies (overweighting the tiny probability of
a catastrophic loss). People are disproportionately influenced by the
difference between 95% and 100% probability -- the certainty effect,
where a sure outcome receives a psychological premium beyond what its
objective probability would justify. And people are less sensitive to
differences between intermediate probabilities (e.g., 45% vs. 55%) than
rational models predict.

In cumulative prospect theory (1992), the weighting function is applied
to cumulative probabilities rather than individual outcomes, which
ensures the model does not violate stochastic dominance (the principle
that a prospect that is better in every possible state should be
preferred). The cumulative version also distinguishes between the
weighting of gains and losses, allowing for separate probability
weighting curves in each domain.

### The Fourfold Pattern of Risk Attitudes

The interaction of the value function and the probability weighting
function produces a distinctive fourfold pattern of risk attitudes
that expected utility theory cannot generate:

| | Gains | Losses |
|:--|:--|:--|
| **High probability** | Risk-averse (take the sure gain) | Risk-seeking (gamble to avoid loss) |
| **Low probability** | Risk-seeking (buy the lottery ticket) | Risk-averse (buy insurance) |

For high-probability gains, the certainty effect and diminishing
sensitivity combine to make a sure gain more attractive than a gamble
with a slightly higher expected value. For high-probability losses,
loss aversion drives risk-seeking behavior -- people would rather gamble
on avoiding a loss than accept it with certainty, even when the gamble
has a worse expected outcome. For low-probability gains, the
overweighting of small probabilities makes long-shot gambles
psychologically attractive. For low-probability losses, the same
overweighting makes people pay disproportionately for insurance
against unlikely catastrophes.

### Mental Accounting

Richard Thaler (1985, 1999) extended prospect theory with the concept of
mental accounting: the cognitive operations people use to organize,
evaluate, and track financial activities. Money is not fungible in the
human mind. People divide their resources into separate mental accounts
(household budget, vacation fund, retirement savings, gambling winnings)
and apply different decision rules to each. A dollar in the "serious
savings" account is treated differently from a dollar in the "fun money"
account -- a violation of economic rationality but a reliable feature of
human psychology.

Mental accounting interacts with loss aversion to produce the
disposition effect: investors are reluctant to sell assets that have
declined in value because closing the mental account at a loss is
psychologically painful. Shefrin and Statman (1987) documented that
investors sell winning stocks far more readily than losing stocks, even
when the tax consequences and future return prospects favor selling the
losers. Mental accounting also explains the sunk cost fallacy: people
continue investing in failing projects because abandoning them requires
closing the mental account at a loss.

### The Endowment Effect and Status Quo Bias

A direct consequence of loss aversion is the endowment effect: people
value items they own more than identical items they do not own. In
Thaler's (1980) classic experiment, participants given a coffee mug
demanded roughly twice as much to sell it as participants without a mug
were willing to pay. The ownership itself created a new reference point,
and giving up the mug felt like a loss. Kahneman, Knetsch, and Thaler
(1991) formalized this finding, showing that the minimum compensation
people demand to give up a good (willingness to accept) is typically
two to three times the maximum amount they would pay to acquire it
(willingness to pay).

Status quo bias, identified by Samuelson and Zeckhauser (1988), is the
closely related tendency to stick with the current state of affairs
even when switching would be objectively beneficial. Loss aversion
makes any change from the status quo feel like a potential loss,
producing inertia that preserves the existing situation. Default
options in retirement plans, insurance contracts, and software
installations are extraordinarily powerful because they exploit this
bias: most people will accept whatever option is pre-selected rather
than incur the psychological cost of evaluating alternatives and
potentially experiencing regret.

### Framing Effects

Framing effects demonstrate that the way a choice is presented -- not
just its objective properties -- determines the decision. In the classic
"Asian disease" problem (Tversky and Kahneman, 1981), participants
were told to imagine that the U.S. is preparing for an outbreak of a
disease expected to kill 600 people. When programs were framed in terms
of lives saved ("Program A saves 200 lives; Program B has a 1/3 chance
of saving 600 and a 2/3 chance of saving none"), 72% chose the sure
option (risk-averse in the gain frame). When the identical outcomes were
framed in terms of deaths ("Program C results in 400 deaths; Program D
has a 1/3 chance of no deaths and a 2/3 chance of 600 deaths"), 78%
chose the gamble (risk-seeking in the loss frame). The objective
outcomes were identical -- the only difference was whether the reference
point made them feel like gains or losses.

## Evidence

The empirical foundation of prospect theory spans decades of
experimental and field research. Kahneman and Tversky (1979) tested
their model against expected utility theory using choices between
hypothetical monetary gambles with student participants. Across
multiple problem sets, expected utility theory failed to predict
majority choice in 30-40% of cases, while prospect theory accurately
predicted the dominant choice in nearly every case. The key findings
included: the certainty effect (a sure outcome receives a
disproportionate psychological weight), the reflection effect (risk
preferences reverse between gains and losses), and the isolation effect
(people simplify choices by ignoring shared components).

Thaler (1980) demonstrated that these laboratory patterns extend to
real consumer behavior. Consumers systematically violate the axioms of
rational choice: they pay attention to sunk costs, they are influenced
by suggested retail prices (anchoring), and they treat windfall gains
differently from earned income (mental accounting). These findings
showed that prospect theory was not merely a laboratory curiosity but
a description of how people navigate real economic decisions.

The endowment effect has been replicated in numerous settings. Kahneman,
Knetsch, and Thaler (1991) conducted experiments with Cornell University
students using coffee mugs and pens, consistently finding
willingness-to-accept / willingness-to-pay ratios of approximately
2:1. List (2003, 2004) extended this research to real markets, showing
that the endowment effect diminishes with trading experience --
experienced traders at sports card conventions showed much smaller
gaps between buying and selling prices than novices, suggesting that
market experience can partially overcome loss aversion, though the
effect does not disappear entirely.

Benartzi and Thaler (1995) applied prospect theory and mental accounting
to one of the biggest puzzles in financial economics: the equity premium
puzzle. The historical difference between stock returns and risk-free
bond returns was far larger than standard rational models could explain
with reasonable levels of risk aversion. Benartzi and Thaler's answer
was "myopic loss aversion": investors evaluate their portfolios too
frequently (e.g., annually rather than over multi-decade horizons), and
because losses loom larger than gains, the frequent experience of
short-term losses makes stocks seem much riskier than they actually are
over long holding periods. When investors are loss-averse and check
their portfolios frequently, they demand an equity premium far above
what rational models predict.

The framing effect has been demonstrated in contexts ranging from
medical decisions to consumer purchases to legal judgments. A
meta-analysis by Kuhberger (1998) of 136 empirical framing studies
confirmed that attribute framing (describing an option positively vs.
negatively) and risky choice framing (the Asian disease paradigm)
produce reliable, medium-to-large effect sizes. A 2015 meta-analysis
by Steiger and Kuhberger of 51 studies involving over 7,500
participants found a significant framing effect overall, with framing
as losses producing a risk-seeking shift compared to framing as gains.

Johnson and Goldstein (2003), in a study published in Science,
documented the real-world consequences of default effects rooted in
status quo bias. In countries with opt-in organ donation systems
(where citizens must actively choose to become donors), consent rates
ranged from 4% (Denmark) to 28% (Netherlands). In countries with
opt-out systems (where citizens are automatically enrolled as donors
and must actively choose to opt out), consent rates ranged from 86%
(Sweden) to nearly 100% (Austria, France). The default option did not
just nudge behavior -- it effectively determined the outcome. This
finding directly validates prospect theory's prediction that reference
points and loss aversion (opting out feels like a loss of the status
quo) dominate decision-making when the costs of switching are
non-zero.

## Implications

For investors, prospect theory explains behaviors that cost real money.
The disposition effect -- selling winners too early and holding losers
too long -- is a direct consequence of the value function's shape:
locking in a gain closes a mental account at a profit (pleasurable),
while realizing a loss closes an account at a loss (painful enough to
postpone indefinitely). The resulting portfolios systematically
underperform: the winners that are sold continue to appreciate while
the losers that are held continue to decline. Value investors like
Warren Buffett and Charlie Munger explicitly train themselves to
counteract this bias, treating investment decisions as independent
judgments rather than as chapters in a mental accounting story.

Myopic loss aversion explains why investors who check their portfolios
daily experience far more psychological distress than those who check
annually -- and why the daily-checkers tend to trade more, hold less
equity, and earn lower returns. The practical prescription is to reduce
the frequency of portfolio evaluation. Benartzi and Thaler's work
implies that the optimal evaluation period for a loss-averse investor
is approximately one year; checking less frequently produces better
long-term outcomes because short-term losses are not mentally
registered.

For public policy, prospect theory provides the intellectual foundation
for nudge theory, developed by Thaler and Cass Sunstein in their 2008
book "Nudge." The key insight is that because people predictably deviate
from rationality, choice architecture can be designed to steer them
toward better outcomes without restricting freedom. Automatic
enrollment in retirement savings plans exploits status quo bias: when
employees must opt out rather than opt in, participation rates rise
from roughly 40% to over 90%. The Save More Tomorrow program, developed
by Thaler and Benartzi, adds a second behavioral insight: asking
employees to commit to future increases in savings contributions
(rather than immediate ones) exploits hyperbolic discounting -- the
commitment feels costless because the sacrifice is in the future, but
once enrolled, status quo bias keeps them in the program. The result
was a near-quadrupling of savings rates over four years in early
implementations.

For negotiation and business, framing matters enormously. Concessions
framed as losses from one's current position are psychologically far
more painful than identical concessions framed as forgone gains. Skilled
negotiators reframe proposals to make their offers feel like gains to
the other party and their own concessions feel like reductions in
potential gains rather than certain losses. In pricing, discounts and
sales exploit loss aversion: "save $50" feels more motivating than
"spend $450" because the consumer frames the purchase price against a
higher reference point, making the discount feel like avoiding a loss.

For everyday decision-making, prospect theory reveals that many
apparently irrational choices have a coherent underlying logic. The
person who drives across town to save $5 on a $15 calculator but not
on a $500 television is not being inconsistent in their own mental
framework: the $5 saving is coded as a 33% discount on the calculator
account but only a 1% discount on the television account. Mental
accounting makes both decisions feel sensible within their respective
frames. Recognizing these patterns does not eliminate them -- loss
aversion and mental accounting appear to be deeply wired features of
human cognition -- but it does allow for the deliberate construction of
decision environments that counteract them when the stakes are high.

## Sources

1. Kahneman, D. & Tversky, A. (1979). "Prospect Theory: An Analysis of
   Decision under Risk." Econometrica, 47(2), 263-291.
   https://www.jstor.org/stable/1914185 [high]

2. Tversky, A. & Kahneman, D. (1992). "Advances in Prospect Theory:
   Cumulative Representation of Uncertainty." Journal of Risk and
   Uncertainty, 5(4), 297-323.
   https://doi.org/10.1007/BF00122574 [high]

3. Kahneman, D., Knetsch, J. L., & Thaler, R. H. (1991). "Anomalies:
   The Endowment Effect, Loss Aversion, and Status Quo Bias." Journal
   of Economic Perspectives, 5(1), 193-206.
   https://www.aeaweb.org/articles?id=10.1257/jep.5.1.193 [high]

4. Thaler, R. H. (1999). "Mental Accounting Matters." Journal of
   Behavioral Decision Making, 12(3), 183-206.
   https://onlinelibrary.wiley.com/doi/abs/10.1002/%28SICI%291099-0771%28199909%2912%3A3%3C183%3A%3AAID-BDM318%3E3.0.CO%3B2-F [high]

5. Benartzi, S. & Thaler, R. H. (1995). "Myopic Loss Aversion and the
   Equity Premium Puzzle." Quarterly Journal of Economics, 110(1),
   73-92. https://doi.org/10.2307/2118511 [high]

6. Johnson, E. J. & Goldstein, D. G. (2003). "Do Defaults Save Lives?"
   Science, 302(5649), 1338-1339.
   https://doi.org/10.1126/science.1091721 [high]

7. Kahneman, D. (2011). "Thinking, Fast and Slow." Farrar, Straus and
   Giroux. Chapters 25-29 provide an accessible synthesis of prospect
   theory and its implications. [high]

## See Also

- `library/psychology-behavior/cognitive-biases.md` -- broader category
  of systematic thinking errors; prospect theory provides the formal
  model underlying many cognitive biases.
- `library/value-investing/margin-of-safety.md` -- how loss aversion
  and the disposition effect manifest in investing behavior; the margin
  of safety is a structural defense against psychological error.
- `library/probabilistic-thinking-forecasting/bayesian-reasoning.md` --
  the normative framework for belief updating under uncertainty that
  prospect theory's descriptive model complements by showing where
  human judgment systematically departs from Bayesian rationality.
- `library/probabilistic-thinking-forecasting/superforecasting.md` --
  how the best forecasters overcome the biases prospect theory
  describes; Tetlock's superforecasters deliberately counteract
  loss aversion and framing effects.
