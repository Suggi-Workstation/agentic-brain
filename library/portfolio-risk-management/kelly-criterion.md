---
name: kelly-criterion
id: 20260726T080304Z
tier: library-topic
domain: portfolio-risk-management
author: Researcher-1
tags: [kelly-criterion, position-sizing, geometric-mean-maximization, fractional-kelly, risk-management, portfolio-allocation]
links: [library/value-investing/margin-of-safety.md, library/probabilistic-thinking-forecasting/bayesian-reasoning.md, library/portfolio-risk-management/anchor-portfolio-risk-management.md]
---

# The Kelly Criterion -- Why Maximizing Geometric Growth Beats Maximizing Expected Value

The Kelly criterion is a mathematical formula that determines the
optimal fraction of capital to allocate to a favorable bet or
investment in order to maximize the long-run compound growth rate of
wealth. Published by John L. Kelly Jr. at Bell Labs in 1956 as a
result in information theory, it has become a foundational concept in
quantitative trading, sports betting, and institutional portfolio
management. Despite its theoretical elegance, most practitioners use a
fractional version -- betting 25-50% of the full Kelly amount --
because the full criterion produces drawdowns too severe for real-world
risk tolerances and because parameter estimates are never perfectly
accurate.

## Background

The Kelly criterion emerged from a problem in information theory, not
finance. John Larry Kelly Jr., a mathematician at Bell Laboratories,
was studying how to maximize the transmission rate of information over
noisy telephone lines when his colleague Claude Shannon -- the father
of information theory -- recognized that Kelly's mathematical
framework had a direct analogue to gambling. The problem was this: a
gambler receives tips over a noisy channel about which horse will win;
how much should the gambler bet on each race to maximize long-run
wealth? Kelly's 1956 paper, "A New Interpretation of Information
Rate," derived the answer: bet a fraction equal to the edge divided by
the odds.

The criterion's migration from gambling to finance was accelerated by
Edward O. Thorp, a mathematics professor who used the Kelly criterion
to develop his pioneering blackjack card-counting system in the 1960s.
Thorp's 1969 paper "Optimal Gambling Systems for Favorable Games"
rigorously proved the criterion's optimality properties and extended
it beyond binary bets. Thorp later applied Kelly-based position sizing
to his hedge fund, Princeton-Newport Partners, which achieved a
compound annual return of approximately 20% over nearly two decades
without a single down year -- performance that Thorp himself
attributed to disciplined Kelly-based allocation.

Simultaneously, economist Henry Latane had independently derived
the same criterion as a portfolio selection rule based on geometric
mean maximization. Latane's work, alongside that of Kelly and Thorp,
established the criterion's dual identity: it is both an information-
theoretic result and a capital growth rule. Robert Merton later
derived the continuous-time version independently in his work on
optimal portfolio choice, creating what is sometimes called the
Merton-Kelly formula.

The criterion's history is also the subject of William Poundstone's
2005 book "Fortune's Formula," which chronicles the intersection of
information theory, gambling, and Wall Street through the lives of
Shannon, Kelly, and Thorp. The book's central tension -- between the
mathematical optimum and the practical realities of risk tolerance --
remains the core debate around Kelly sizing today.

## Core Concepts

### The Kelly Formula

The Kelly criterion has two primary forms. The discrete form applies to
bets with a binary outcome:

```
f* = (bp - q) / b
```

Where:
- f* = optimal fraction of capital to wager
- b = net odds received (e.g., b = 2 means you win $2 for every $1
  risked)
- p = probability of winning
- q = probability of losing (q = 1 - p)

For even-money bets (b = 1), this simplifies to f* = p - q = 2p - 1.

The continuous form, applicable to investment returns that follow a
distribution rather than a binary payoff, is:

```
f* = (mu - r) / sigma^2
```

Where:
- mu = expected return of the investment
- r = risk-free rate
- sigma^2 = variance of returns

This version reveals a deep connection to the Sharpe ratio. Since the
Sharpe ratio equals (mu - r) / sigma, the Kelly fraction can be
expressed as f* = (Sharpe ratio) / sigma. Higher Sharpe ratios and
lower volatility both increase the optimal allocation.

### Maximizing the Logarithm of Wealth

The Kelly criterion does not maximize expected value (arithmetic mean).
It maximizes the expected logarithm of wealth -- equivalently, the
geometric mean return. This distinction is critical.

If an investment has a positive expected arithmetic return, a naive
maximizer would bet everything. But a single total loss sends the
geometric return to negative infinity. The logarithm accounts for the
compounding effect: a 50% loss requires a 100% gain just to break even.
By maximizing E[ln(W)], the Kelly criterion balances the desire for
growth with the risk of permanent capital impairment.

The expected log growth rate G(f) for a binary bet is:

```
G(f) = p ln(1 + bf) + q ln(1 - f)
```

Taking the derivative with respect to f and setting to zero yields the
Kelly formula. What makes this result powerful is that no other
strategy produces a higher expected growth rate over a sufficiently
long sequence of bets -- the Kelly criterion is asymptotically optimal.

### No Edge, No Bet

An important property of the Kelly formula is that f* is positive only
when bp > q, meaning the expected value of the bet is positive. If the
formula returns a negative number, the rational decision is to bet
nothing (or bet the other side, if allowed). Kelly embeds the most
fundamental investment rule: do not allocate capital without a genuine
edge.

### The Multi-Asset Extension

The Kelly criterion generalizes to portfolios of multiple correlated
assets. The multi-asset Kelly problem maximizes:

```
E[ln(1 + sum(w_i * r_i))]
```

Where w_i are the portfolio weights and r_i are the asset returns.
This requires estimating the full covariance matrix of returns, not
just individual expected returns and variances. With N assets, the
number of covariance terms grows as N(N-1)/2, making estimation error
a compounding problem. In practice, multi-asset Kelly works best with
a small number of relatively uncorrelated strategies where the
covariance matrix can be estimated with reasonable confidence.

### Fractional Kelly

Fractional Kelly simply multiplies the full Kelly fraction by a
constant less than one. The most common variants are half-Kelly (0.5x)
and quarter-Kelly (0.25x). This appears to sacrifice growth, but the
trade-off is extraordinarily favorable:

- Half-Kelly retains approximately 75% of the full Kelly growth rate
  while roughly halving the volatility and dramatically reducing the
  severity of drawdowns.
- Quarter-Kelly retains approximately 44% of the growth rate with even
  lower risk, suitable when estimation uncertainty is high.

The reason fractional Kelly is nearly universal in practice is not risk
aversion per se -- it is the recognition that parameter estimates are
uncertain. If you overestimate your edge (p is too high) or
underestimate your risk (sigma is too low), full Kelly will have you
overbetting. And the penalty for overbetting is asymmetric: betting 1.5x
the correct Kelly fraction can turn the expected growth rate negative,
meaning you lose money on average despite having a genuine edge.
Fractional Kelly provides a buffer against this estimation error.

### The Asymmetric Penalty Function

A central insight of Kelly analysis is that the cost of overbetting
vastly exceeds the cost of underbetting. If the true optimal fraction
is 10%, betting 5% (half) reduces your growth rate modestly. But
betting 20% (double) can produce a negative growth rate -- you destroy
capital despite having an edge. This asymmetry is why conservative
sizing is not just a matter of temperament but of mathematical
prudence. As Thorp demonstrated, betting fractionally above Kelly is
mathematically ruinous; betting fractionally below is merely suboptimal.

## Evidence

The empirical and theoretical evidence supporting the Kelly criterion
is extensive but comes with important caveats about real-world
applicability.

Kelly's original 1956 paper proved that the criterion maximizes the
asymptotic growth rate of capital when the underlying probabilities are
known. The proof is rigorous within its assumptions: independent,
identically distributed bets with known parameters. Kelly showed that
any strategy deviating from the optimal fraction will, over a long
enough horizon, be dominated by the Kelly strategy in terms of final
wealth -- in fact, the ratio of Kelly wealth to any other strategy's
wealth tends to infinity almost surely.

Thorp's 1969 paper extended this result, proving that the Kelly
criterion is not merely asymptotically optimal but also maximizes the
median terminal wealth for any fixed number of bets. Thorp's own track
record at Princeton-Newport Partners provided a real-world case study:
the fund's consistent 20% compound returns with minimal drawdowns over
19 years were achieved using Kelly-based position sizing across
convertible arbitrage, warrant hedging, and other quantitatively
identified edges.

Chopra and Ziemba (1993) demonstrated a finding that fundamentally
shapes how practitioners should use the Kelly criterion. In their study
of portfolio optimization, errors in estimating expected returns
(p and mu in the Kelly framework) were approximately 20 times as costly
as errors in estimating variances, and about 10 times as costly as
errors in estimating covariances. This means the Kelly criterion's
Achilles heel is the mean estimate -- get that wrong, and the
portfolio suffers severely. The practical implication is clear:
conservatism in position sizing (fractional Kelly) is the rational
response to the known difficulty of estimating expected returns.

MacLean, Thorp, and Ziemba (2011) catalogued the "good and bad
properties" of the Kelly criterion. The good properties include
asymptotic optimality, maximization of median wealth, and the
mathematical guarantee of never going broke (in continuous time with
infinitely divisible capital). The bad properties include extreme
short-term volatility, drawdowns exceeding 50% even with a genuine
edge, and catastrophic sensitivity to errors in mean estimation. Their
conclusion: for long-term compounders who can tolerate high volatility
and who have accurately estimated parameters, the good properties
dominate. For nearly everyone else, fractional Kelly is essential.

Estrada (2010) compared geometric mean maximization (GMM) portfolios --
which are equivalent to Kelly portfolios -- against traditional
Sharpe-ratio-maximized portfolios using historical data across multiple
markets. The GMM portfolios delivered higher compound growth, greater
upside potential, and limited downside relative to mean-variance
portfolios. However, the study also confirmed that GMM portfolios are
more concentrated and more volatile than their mean-variance
counterparts, underscoring the fractional Kelly compromise.

The author's synthesis of this evidence is that the Kelly criterion
provides the correct conceptual framework for position sizing --
maximize geometric growth, not arithmetic expectation -- but that the
theoretical optimum is generally too aggressive for practical deployment
with estimated parameters. Fractional Kelly is not a compromise; it is
the logical response to the empirically validated finding that mean
estimation error is the dominant source of portfolio optimization
failure.

## Implications

### For Value Investors

The Kelly criterion provides a formal framework for the concentration
versus diversification debate that runs through value investing. Warren
Buffett has famously advocated putting large fractions of capital into
your best ideas, while most institutional investors diversify across
dozens or hundreds of positions. The Kelly criterion resolves this
tension mathematically: concentrate when your edge (the gap between
your estimated probability of success and the market-implied
probability) is large and the volatility of outcomes is low. Diversify
when edges are small and uncertain.

Applied to a value investment -- say, a stock you believe has a 70%
probability of delivering a 50% return over two years and a 30%
probability of a 30% permanent loss -- the Kelly formula yields a
specific position size. If that size is 15% of your portfolio, it
implies that a 20% position is overbetting and a 5% position is
underbetting. The Kelly criterion brings quantitative discipline to
what is otherwise a gut-feel decision.

### For Portfolio Construction

The Kelly framework exposes a limitation of mean-variance optimization.
Markowitz optimization asks the investor to specify a risk aversion
parameter -- essentially, to choose a point on the efficient frontier.
The Kelly criterion fixes the risk aversion at log utility, which
corresponds to maximizing long-run growth. Investors who are more
conservative than log utility implies can use fractional Kelly as their
risk-control mechanism, maintaining the growth-optimal structure while
scaling down risk.

The multi-asset extension also reveals why covariance estimation
matters. Two investments with identical Kelly fractions in isolation
may require different allocations in a portfolio if their returns are
correlated. The Kelly criterion naturally penalizes concentration in
correlated bets, aligning with the intuitive principle that
diversification benefits are real but should be pursued deliberately,
not as an unthinking response to uncertainty.

### For Risk Management

Perhaps the most important implication of the Kelly criterion is its
asymmetric penalty function. The fact that overbetting by a factor of
two can turn a winning strategy into a losing one has profound
consequences for risk management. It means that position sizing is not
merely about calibrating returns -- it is a survival constraint. An
investor who sizes positions correctly will survive the inevitable
streak of adverse outcomes; an investor who overbets will not.

This connects to the broader principle that risk management is about
avoiding the permanent impairment of capital, not about smoothing
short-term volatility. The Kelly criterion maximizes growth precisely
by avoiding ruin -- the log utility function assigns infinite negative
utility to going to zero, which forces the strategy to preserve capital
even while pursuing aggressive growth. This is why value investors like
Mohnish Pabrai and quantitative investors like Jim Simons have
independently converged on Kelly-like frameworks: the mathematics of
long-term compounding demands it.

### Practical Limitations

The Kelly criterion's practical limitations are substantial and should
be acknowledged. First, it requires probability estimates that are
rarely available with precision in investing contexts. A value investor
cannot know with 70% confidence that a stock will return 50%; these
are rough estimates at best. Second, investments are not independent
repeated bets with identical parameters -- each investment has unique
characteristics, and the parameters shift over time. Third, the
criterion assumes the investor can continuously rebalance and recover
from losses, which requires access to additional capital or income
streams. Fourth, the psychological burden of full Kelly drawdowns --
watching half of your net worth disappear, even temporarily -- is more
than most investors can bear without abandoning their strategy.

The resolution is not to abandon the Kelly framework but to use it
as a thinking tool rather than a mechanical rule. The key principles --
maximize geometric growth, never bet without an edge, size positions
conservatively when edge estimates are uncertain, and recognize the
asymmetric cost of overbetting -- survive even when the exact formula
cannot be applied.

## Sources

1. Kelly, J.L. (1956). "A New Interpretation of Information Rate."
   Bell System Technical Journal, 35, 917-926.
   https://www.princeton.edu/~wbialek/rome/refs/kelly_56.pdf [high]

2. Thorp, E.O. (1969). "Optimal Gambling Systems for Favorable Games."
   Review of the International Statistical Institute, 37(3), 273-293. [high]

3. Poundstone, W. (2005). Fortune's Formula: The Untold Story of the
   Scientific Betting System That Beat the Casinos and Wall Street.
   Hill and Wang. [high]

4. MacLean, L.C., Thorp, E.O., & Ziemba, W.T. (2011). "Good and Bad
   Properties of the Kelly Criterion." In The Kelly Capital Growth
   Investment Criterion: Theory and Practice. World Scientific.
   https://www.stat.berkeley.edu/~aldous/157/Papers/Good_Bad_Kelly.pdf [high]

5. Chopra, V. & Ziemba, W.T. (1993). "The Effect of Errors in Means,
   Variances, and Covariances on Optimal Portfolio Choice." Journal of
   Portfolio Management, 19(2), 6-11. [high]

6. Estrada, J. (2010). "Geometric Mean Maximization: An Overlooked
   Portfolio Approach?" Journal of Investing, 19(4), 81-93.
   https://blog.iese.edu/jestrada/files/2012/06/GMM-Extended.pdf [high]

7. Quantt (2026). "Kelly Criterion: Optimal Bet Sizing Explained 2026."
   https://www.quantt.co.uk/resources/kelly-criterion-explained [medium]

## See Also

- `library/value-investing/margin-of-safety.md` -- the Kelly
  criterion's asymmetric penalty function is the mathematical
  expression of Graham's margin of safety principle.
- `library/probabilistic-thinking-forecasting/bayesian-reasoning.md` --
  Bayesian updating addresses the Kelly criterion's core weakness:
  parameter estimation under uncertainty.
- `library/valuation-screening/discounted-cash-flow-dcf-methodology.md` --
  DCF provides the estimated returns and probabilities that feed into
  Kelly-based position sizing.
