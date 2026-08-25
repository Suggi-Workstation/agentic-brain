---
name: risk-parity-and-factor-based-construction
id: 20260825T130114Z
tier: library-topic
domain: portfolio-risk-management
author: Library-Runner
tags: [risk-parity, factor-investing, portfolio-construction, all-weather, smart-beta, fama-french, momentum, value-factor, quality-factor, leverage]
links: [library/portfolio-risk-management/modern-portfolio-theory.md, library/portfolio-risk-management/diversification-mathematics.md, library/portfolio-risk-management/portfolio-rebalancing-strategies.md, library/portfolio-risk-management/kelly-criterion.md]
---

# Risk Parity and Factor-Based Portfolio Construction -- Why Allocating by Risk Beats Allocating by Capital

Risk parity is a portfolio construction approach that allocates
capital based on each asset's risk contribution rather than its
dollar weight, ensuring no single asset class dominates the
portfolio's risk profile. Factor-based construction extends this
logic by targeting systematic return drivers -- value, momentum,
quality, size, and low volatility -- that academic research has
identified as persistent sources of excess returns across markets
and decades. Together, these two frameworks represent the most
significant evolution in portfolio construction since Markowitz: they
replace capital-weight allocation, which is dominated by equity
risk, with risk-balanced and factor-tilted approaches that achieve
genuinely diversified exposure. Their promise is substantial, but
their implementation challenges -- leverage, post-publication factor
decay, and crowding -- demand the same skepticism that any
systematic strategy deserves.

## Background

The intellectual lineage of risk parity and factor-based
construction runs through three distinct but connected strands of
twentieth-century finance. The first is Modern Portfolio Theory,
introduced by Harry Markowitz in 1952, which established that
investors should evaluate assets by their contribution to total
portfolio risk, not in isolation. Markowitz showed that combining
assets with imperfectly correlated returns produces a portfolio
whose volatility is less than the weighted average of its
components -- the mathematical foundation of diversification. But
MPT's practical prescription, the mean-variance efficient frontier,
proved notoriously difficult to implement because it requires
estimating expected returns, volatilities, and correlations for
every asset, and small errors in these inputs produce wildly
different "optimal" portfolios. Risk parity emerged as a pragmatic
answer: rather than estimating expected returns (the hardest input),
allocate by risk alone, which is more stable and more measurable.

The second strand is the Capital Asset Pricing Model (CAPM),
developed by Sharpe, Lintner, and Mossin in the 1960s, which held
that the only risk worth pricing is market risk (beta), and that
expected returns increase linearly with beta. CAPM implied that a
market-cap-weighted index portfolio was optimal -- an implication
that dominated institutional investing for decades. But empirical
anomalies accumulated. Banz (1981) found that small-cap stocks
outperformed large-caps beyond what beta predicted. Basu (1977)
found that low price-to-earnings stocks outperformed. These
anomalies chipped away at CAPM's dominance and set the stage for a
more granular model of return drivers.

The third strand is the Fama-French revolution. In 1992, Eugene
Fama and Kenneth French published "The Cross-Section of Expected
Stock Returns," demonstrating that two variables -- firm size
(market capitalization) and book-to-market ratio (a value measure) --
explained a substantial portion of the variation in stock returns
that market beta alone could not. Their 1993 paper formalized this
into the three-factor model, adding SMB (small minus big) and HML
(high minus low book-to-market) to the market factor. This was the
birth of modern factor investing: the idea that returns are driven
not by a single market risk premium but by multiple systematic
factors, each with its own risk and return characteristics. Mark
Carhart added momentum as a fourth factor in 1997, and Fama and
French extended the model to five factors in 2015, adding
profitability (RMW) and investment (CMA).

Risk parity's commercial birth came from a different direction.
Ray Dalio and his team at Bridgewater Associates spent the 1980s and
early 1990s developing what they called the "All Weather" strategy,
launched in 1996 for Dalio's family trust. Their insight was
deceptively simple: traditional portfolios were roughly 95 percent
correlated to equities because equities dominated both the capital
allocation and the risk allocation. By risk-adjusting all assets
so that each contributed equally to portfolio risk, and by
leveraging lower-risk assets (bonds) to match the risk of
higher-risk assets (equities), they could build a portfolio that was
balanced across economic environments -- rising growth, falling
growth, rising inflation, falling inflation -- rather than a bet on
any single scenario. A consultant later coined the term "risk
parity" to describe this approach, and it became an asset class of
its own, with hundreds of billions in institutional allocations by
the 2010s.

Factor investing's commercial trajectory paralleled risk parity's
but arrived slightly later. The academic factor literature
exploded in the 2000s and 2010s, with Jegadeesh and Titman (1993)
documenting momentum, Asness, Frazzini, and Pedersen (2019)
formalizing quality, and Frazzini and Pedersen (2014) explaining low
volatility through their Betting Against Beta framework. The
financial industry packaged these insights into "smart beta" ETFs
that tilted index portfolios toward specific factors, and global
smart beta assets under management exceeded $1.5 trillion by 2025.
The two approaches -- risk parity at the asset-class level and
factor tilting at the security level -- are complementary: risk
parity addresses the question of how to balance risk across asset
classes, while factor investing addresses which characteristics
within each asset class to target.

## Core Concepts

### Risk Contribution and the Mathematics of Risk Parity

The central idea of risk parity is that a portfolio's total risk
can be decomposed into the risk contribution of each component
asset. For portfolio volatility, defined as sigma(w) = sqrt(w^T
Sigma w) where w is the weight vector and Sigma is the covariance
matrix, Euler's homogeneous function theorem provides the
decomposition: each asset's risk contribution RC_i equals w_i
multiplied by the partial derivative of portfolio volatility with
respect to that asset's weight. The sum of all risk contributions
equals total portfolio risk. Risk parity seeks the weight vector
where every asset's risk contribution is equal -- hence "parity."

This mathematical foundation, rooted in Euler's theorem for
positively homogeneous functions, means that risk parity is not an
ad hoc heuristic. It is a precisely defined optimization problem.
The choice of risk measure matters: volatility, value-at-risk
(VaR), and conditional VaR (CVaR) all satisfy Euler's requirement,
but they produce different decompositions. Most practical risk
parity implementations use volatility because it is the most
stable and computationally tractable, though CVaR-based risk parity
offers better tail-risk properties for portfolios with non-normal
return distributions.

The practical consequence of risk contribution parity is
dramatic. In a traditional 60/40 stock-bond portfolio, equities
contribute roughly 90 percent of the portfolio's volatility because
equities are roughly three to four times more volatile than bonds.
The 60/40 split looks balanced by capital but is deeply
concentrated by risk. Risk parity corrects this by increasing the
bond allocation and/or leveraging bonds so that their risk
contribution matches equities'. The result is a portfolio where
no single asset class dominates -- a genuinely diversified risk
profile rather than an illusion of diversification created by
capital weights.

### The All Weather Framework: Four Economic Environments

Dalio's contribution was not merely the mathematical equalization of
risk contributions but a structural framework for thinking about
why diversification across risk contributions works. He observed
that all asset classes have "environmental biases" -- they perform
well in certain economic conditions and poorly in others. Equities
thrive when growth exceeds expectations. Bonds thrive when growth
falls short or inflation declines. Commodities thrive when growth
is strong and inflation rises. Cash is most attractive when money
is tight. The key insight: since markets are always discounting
future conditions, and investors have roughly equal odds of being
right or wrong about any single scenario, a portfolio balanced
across all four environments (rising growth, falling growth,
rising inflation, falling inflation) will perform reasonably
regardless of which scenario actually unfolds.

The All Weather portfolio places approximately 25 percent of risk
in each of these four quadrants. This is not 25 percent of capital --
it is 25 percent of risk-adjusted exposure, achieved through
leverage on lower-volatility assets. The framework's elegance is
that it requires no forecast of which economic scenario will
prevail. It is a passive, structural allocation designed to be
indifferent to economic surprises. Bridgewater's research
indicates this approach historically reduced risk by roughly
one-third relative to a 60/40 portfolio while maintaining similar
returns, implying a Sharpe ratio improvement from approximately
0.4 to 0.6.

### Leverage: The Tool and the Stigma

Risk parity requires leverage to function. Low-volatility assets
like bonds must be leveraged up to match the risk contribution of
higher-volatility assets like equities. Without leverage, achieving
risk parity would mean allocating so much capital to bonds that
expected returns would be unacceptably low. With leverage, bonds
can be risk-adjusted to equity-like risk levels, and the portfolio
achieves both diversification and return.

Leverage is the most controversial aspect of risk parity and the
source of most criticism. Critics argue that leveraging bonds is
a bet on falling interest rates, and that risk parity's strong
historical performance coincided with a thirty-year bull market in
bonds that may be ending. The 2013 "taper tantrum," when bond prices
fell sharply on signals that the Federal Reserve would reduce
quantitative easing, raised urgent questions about whether risk
parity portfolios could withstand rising rates. Advocates
respond that risk parity is not a levered bond portfolio -- it is a
diversified portfolio that uses leverage as a tool, and that
diversification across asset classes provides protection that a
pure bond position does not. The empirical record after 2013
showed risk parity recovering strongly, but the debate over
leverage in a rising-rate environment remains live.

### The Five Canonical Factors

Factor-based construction rests on five factors that have
accumulated the strongest academic and practitioner support:

**Value.** Stocks with low prices relative to fundamentals (book
value, earnings, cash flow) outperform stocks with high prices
relative to fundamentals. Fama and French (1992) documented this
using the book-to-market ratio, finding a value premium of roughly
6 percent per year from 1963 to 1990. The mechanism is debated:
behavioral explanations attribute it to investor overreaction to
bad news, while risk-based explanations argue that value stocks are
fundamentally riskier (they are often distressed companies). The
value premium experienced a severe and prolonged drawdown in the
2010s, raising questions about its persistence, but it remains one
of the most documented anomalies in finance.

**Momentum.** Stocks that have outperformed over the past 3 to 12
months tend to continue outperforming over the following 3 to 12
months. Jegadeesh and Titman (1993) documented this with portfolios
earning excess returns of approximately 1 percent per month.
Momentum has the strongest post-publication evidence of any factor
-- it has survived scrutiny better than value, size, or quality.
Its mechanism is likewise debated: behavioral explanations cite
underreaction to news and herding, while risk-based explanations are
less developed. Momentum is notorious for occasional violent
"crashes" -- sharp reversals that can wipe out months of gains in
days, particularly during market regime transitions.

**Quality.** Companies with high profitability, stable earnings,
low leverage, and strong growth outperform companies with the
opposite characteristics. Asness, Frazzini, and Pedersen (2019)
formalized this in their Quality Minus Junk (QMJ) factor, which
earned risk-adjusted returns of 0.66 percent per month in the U.S.
and 0.45 percent internationally across 24 countries. The quality
premium is puzzling from an efficient-market perspective: if
high-quality companies are demonstrably better, their prices should
be high enough that no excess return remains. The AQR finding is
that the market systematically under-prices quality, paying more
for quality than for junk but not by enough to eliminate the return
differential.

**Size.** Small-cap stocks outperform large-cap stocks over long
periods. Banz (1981) first documented this, and Fama and French
incorporated it as the SMB factor. The size premium is the weakest
and most contested of the canonical factors. Much of the original
small-cap premium weakened or disappeared in the decades after
publication, a pattern consistent with post-publication decay. The
premium that remains is concentrated in small-cap value stocks,
not small-cap growth stocks, and is sensitive to implementation
costs (small-cap stocks have higher transaction costs and lower
liquidity).

**Low Volatility.** The least volatile stocks in the market have
historically delivered better risk-adjusted returns than the most
volatile stocks -- the opposite of what CAPM predicts. This
"low-volatility anomaly" was noted as early as Haugen and Heins
(1972) but gained prominence through Ang et al. (2006) and
Frazzini and Pedersen's (2014) Betting Against Beta (BAB) framework.
Their explanation: many institutional investors face leverage
constraints and therefore cannot leverage low-risk assets to
achieve target returns. Instead, they overweight high-beta stocks,
bidding up their prices and reducing future returns. Unconstrained
investors who buy low-beta stocks and short high-beta stocks earn
excess returns from this distortion.

### Factor Models: From Three to Five and Beyond

The Fama-French three-factor model (1993) added size and value to
the market factor. Carhart's four-factor model (1997) added
momentum. The Fama-French five-factor model (2015) added
profitability (RMW) and investment (CMA), finding that in U.S. data
these two new factors made the value factor (HML) largely
redundant. The five-factor model explains more of the cross-sectional
variation in returns than its predecessors but still fails the
Gibbons-Ross-Shanken test for full explanatory adequacy, and the
exclusion of momentum remains a point of contention -- Cliff
Asness, Fama's former student and AQR co-founder, has argued
forcefully for its inclusion.

### The Factor Zoo and Multiple Testing

The proliferation of documented factors created what John Cochrane
called a "factor zoo" in his 2011 American Finance Association
presidential address. By 2016, Harvey, Liu, and Zhu catalogued at
least 316 published factors claiming to predict stock returns.
They argued that the standard statistical threshold (a t-statistic
above 2.0, corresponding to roughly a 5 percent false positive rate)
was indefensible given the volume of testing. With hundreds of
researchers testing hundreds of variables on overlapping datasets,
many "significant" factors would appear by chance alone. Harvey,
Liu, and Zhu recommended raising the threshold to t > 3.0,
implying that a substantial fraction of published factors are
likely false discoveries -- the product of data mining rather than
genuine economic relationships.

## Evidence

### Bridgewater All Weather: Three Decades of Risk Parity in Practice

The most compelling evidence for risk parity is Bridgewater's All
Weather strategy itself. Launched in 1996, the portfolio was
designed to hold four sub-portfolios, each with equal risk, each
performing well in one of four economic environments. Bridgewater's
own analysis, presented in Dalio's 2004 article and subsequent
publications, shows that the All Weather asset mix run at the same
risk level as a conventional 60/40 portfolio would have produced
300-400 basis points of additional return per year from 1970 onward.
Alternatively, run at the same return level as the conventional
portfolio, it would have achieved that return with approximately
half the risk.

The strategy weathered the 2008 financial crisis, the 2013 taper
tantrum, and numerous smaller shocks. In the 2008 crisis, assets
that perform poorly when growth falls (equities) declined, but
were offset by assets that perform well when growth falls (Treasury
bonds), which had been leveraged to comparable risk. The
diversification held because the strategy was balanced by risk
contribution, not by capital. This is the central empirical claim
of risk parity: that risk-balanced diversification provides more
robust protection than capital-weighted diversification because it
prevents any single asset class from dominating the portfolio's
risk.

Critics note that All Weather's strong historical returns coincided
with a three-decade decline in interest rates that inflated bond
returns. An analysis by AQR and other researchers examined this
claim by stripping out the windfall gains from unexpected interest
rate declines and found that risk parity still generated meaningful
diversification benefits, though the magnitude of outperformance
was reduced. The debate is unresolved but the core finding holds:
risk parity's Sharpe ratio improvement comes primarily from
diversification, not from betting on falling rates.

### Fama-French: Value and Size Premiums

The foundational empirical evidence for factor investing comes from
Fama and French's 1992 study, which examined all non-financial firms
on the NYSE, AMEX, and NASDAQ from 1963 to 1990. They found that
both size and book-to-market ratio had strong explanatory power for
cross-sectional returns, subsuming the role of beta. The value
premium (HML) averaged approximately 6 percent annually over the
sample period. The size premium (SMB) was smaller but statistically
significant. Their 2015 five-factor extension found that
profitability (RMW) and investment (CMA) also carried significant
premiums, and that together with the other factors, they made the
value factor redundant in U.S. data -- a surprising finding that
complicates the interpretation of value as an independent risk
factor.

### Jegadeesh-Titman: Momentum Across Markets and Time

The momentum evidence is arguably the strongest in the factor
literature. Jegadeesh and Titman's 1993 study showed that
zero-cost momentum strategies (buying past winners, shorting past
losers) earned approximately 1 percent per month. Subsequent
research extended the finding to international markets, different
time periods, and even other asset classes (commodities,
currencies). Momentum has survived post-publication scrutiny better
than any other factor, though the severe momentum crash of 2009 --
when the strategy lost approximately 73 percent in a few months as
the market reversed and beaten-down financial stocks surged --
demonstrated that the premium carries significant tail risk.

### McLean and Pontiff: Post-Publication Factor Decay

The most sobering evidence for factor investing comes from McLean
and Pontiff (2016), who tracked 97 published stock-return anomalies
after their papers appeared. They found that average anomaly
returns fell by approximately 26 percent after publication compared
to the in-sample period. Critically, the decline was concentrated
in the post-publication window specifically, not spread evenly
across the post-sample period -- exactly what you would expect if
the paper itself attracted arbitrage capital that traded away the
premium. The decay was larger for anomalies that were easier to
trade: liquid, large-cap stocks with low transaction costs saw
sharper post-publication declines than anomalies concentrated in
small, illiquid names.

A subsequent international study examining 241 anomalies across 38
markets found post-publication declines of 62-66 percent for
equally-weighted and value-weighted anomaly returns in the U.S.,
confirming the McLean-Pontiff finding at a larger scale. The
international evidence was more mixed, with weaker post-publication
effects outside the U.S., possibly because arbitrage capital is
less concentrated in international markets.

### Asness, Frazzini, and Pedersen: Quality Minus Junk

The QMJ factor, documented across 24 countries, earned
risk-adjusted returns of 0.66 percent per month in the U.S. with an
information ratio of 1.46, and 0.45 percent per month
internationally. The return was positive in 23 of 24 countries
studied, ranging from 0.20 percent in Spain to 1.06 percent in
Greece. Frazzini and Pedersen's related BAB factor showed that low-beta
stocks earned higher risk-adjusted returns than CAPM predicts,
confirming the low-volatility anomaly across asset classes. The
combined evidence from QMJ and BAB suggests that the market
systematically overprices risk and underprices quality, creating
persistent opportunities for unconstrained investors.

### Harvey, Liu, and Zhu: The Factor Zoo Problem

The cautionary evidence comes from Harvey, Liu, and Zhu's 2016
analysis of 316 published factors. Their multiple-testing framework
showed that the conventional t > 2.0 threshold was indefensible given
the volume of hypothesis testing in the literature. Applying
Bonferroni, Holm, and Benjamini-Hochberg corrections, they
recommended a threshold of t > 3.0 for newly proposed factors. The
implication: a substantial fraction of published factors would fail
this higher bar and should be reclassified as likely false
positives. A subsequent study by Hou, Xue, and Zhang tested 452
anomalies in a unified framework and found that roughly 65 percent
did not produce statistically significant premiums at the
conventional 5 percent level, and the failure rate increased
further under the t > 3.0 standard.

## Implications

### For Institutional Portfolio Construction

Risk parity has fundamentally changed how large institutional
investors -- pension funds, endowments, sovereign wealth funds --
think about asset allocation. The traditional approach allocated
capital across asset classes (60 percent equities, 40 percent
bonds) and accepted that equities dominated risk. Risk parity
exposed this as a hidden concentration bet and offered a
systematic alternative. By 2025, an estimated 4 percent of U.S.
institutional assets (roughly $400 billion) were allocated to risk
parity strategies, with Bridgewater managing approximately half of
the external portion. The implication extends beyond the specific
strategy: risk parity established the principle that risk
allocation, not capital allocation, is the correct framework for
portfolio construction. Even investors who do not implement pure
risk parity increasingly report their portfolios in terms of risk
contributions rather than capital weights.

For institutions considering risk parity, the practical
implications are threefold. First, leverage is required and must be
managed carefully -- the strategy uses approximately 2x leverage,
less than the average S&P 500 company, but more than a traditional
unlevered portfolio. Second, the strategy is sensitive to the
interest rate environment, and investors must understand whether
the diversification benefit survives in a rising-rate world. Third,
risk parity is a strategic, long-horizon allocation, not a tactical
one. Its benefits accrue over full market cycles, and abandoning it
during periods of stress (such as the 2013 taper tantrum) would
forfeit the recovery that typically follows.

### For Individual Investors and Factor Tilting

Factor-based construction gives individual investors a systematic
way to target excess returns without active stock picking. Smart
beta ETFs make factor exposure accessible at low cost, and
multi-factor products provide diversification across factors in a
single vehicle. The practical guidance from the literature is
clear: factor tilts should be modest (20-30 percent of equity
allocation is a reasonable starting point), multifactor exposure
is preferable to single-factor timing (the evidence for successful
factor timing is thin), and investors must be prepared for
multi-year underperformance of any individual factor.

Value and momentum tend to be negatively correlated -- value looks
for cheap assets, momentum looks for recently rising assets (which
are becoming more expensive). Holding both simultaneously smooths
the ride because when one underperforms, the other tends to
compensate. This negative correlation is one of the strongest
arguments for multi-factor construction: even if the timing of
individual factors is unpredictable, diversifying across factors
with low correlations improves risk-adjusted expected returns. The
CFA Institute's review of the factor literature identified value,
momentum, illiquidity, and low beta as the most robust factors,
with size and quality exhibiting weaker premiums.

### For Risk Management and Drawdown Control

Both risk parity and factor-based construction carry specific risk
management implications. Risk parity's use of leverage means that
drawdowns can be amplified relative to an unlevered portfolio,
though the diversification benefit partially offsets this. The
strategy's reliance on bonds for diversification creates
concentration in a single risk factor (duration) that may not
provide protection in a stagflationary environment where both
equities and bonds decline simultaneously -- a scenario that
historically has been rare but is not impossible.

Factor strategies carry crowding risk. As more capital flows into
popular factor ETFs, the premium may be competed away, and in
stress conditions, forced simultaneous unwinding by many
investors in similar positions can amplify losses. The evidence
for crowding is strongest in momentum, where the simultaneity of
momentum crashes suggests that many investors hold similar
positions that liquidate together. Quality and low-volatility
strategies have also shown crowding characteristics in recent
years. Monitoring signals include factor spread analysis,
position-level overlap measures, and valuation dispersion within
factor portfolios, but crowding cannot be eliminated -- only
managed.

### For the Philosophy of Evidence-Based Investing

Risk parity and factor investing share a common philosophical
commitment: investment decisions should be grounded in systematic
evidence rather than subjective judgment. This commitment is
admirable but carries its own risks. The factor zoo problem
demonstrates that "evidence" can be manufactured through data
mining, and that the academic publication process itself can
create false confidence. The post-publication decay documented by
McLean and Pontiff shows that the act of publishing evidence
changes the system being studied, potentially destroying the
premium the evidence identified. This is a form of reflexivity: the
factor exists partly because few people knew about it, and it
weakens precisely because the knowledge spreads.

The implication for evidence-based investors is humility. The
strongest factors (value, momentum, quality) have survived decades
of scrutiny and multiple market regimes, but even these have
experienced prolonged periods of underperformance that would test
most investors' conviction. The weakest factors (size, many
recently published anomalies) may not survive at all. The right
approach is to build portfolios around the most robust,
longest-documented factors, size exposures modestly, diversify
across factors with low correlations, and maintain the discipline
to hold through multi-year underperformance -- the same discipline
that portfolio rebalancing demands at market extremes.

## Sources

1. Fama, E.F. & French, K.R. (1992). "The Cross-Section of Expected
   Stock Returns." The Journal of Finance, 47(2), 427-465.
   https://doi.org/10.1111/j.1540-6261.1992.tb04398.x [high]

2. Fama, E.F. & French, K.R. (1993). "Common Risk Factors in the
   Returns on Stocks and Bonds." Journal of Financial Economics,
   33(1), 3-56. [high]

3. Fama, E.F. & French, K.R. (2015). "A Five-Factor Asset Pricing
   Model." Journal of Financial Economics, 116(1), 1-22.
   https://doi.org/10.1016/j.jfineco.2014.10.010 [high]

4. Jegadeesh, N. & Titman, S. (1993). "Returns to Buying Winners
   and Selling Losers: Implications for Stock Market Efficiency."
   The Journal of Finance, 48(1), 65-91. [high]

5. Asness, C.S., Frazzini, A. & Pedersen, L.H. (2019). "Quality
   Minus Junk." Review of Accounting Studies, 24(1), 34-112.
   https://doi.org/10.1007/s11142-018-9470-2 [high]

6. Harvey, C.R., Liu, Y. & Zhu, H. (2016). "...and the Cross-Section
   of Expected Returns." The Review of Financial Studies, 29(1),
   5-68. https://doi.org/10.1093/rfs/hhv059 [high]

7. McLean, R.D. & Pontiff, J. (2016). "Does Academic Research
   Destroy Stock Return Predictability?" The Journal of Finance,
   71(1), 5-32. [high]

8. Dalio, R. (2004). "Engineering Targeted Returns and Risks."
   Reprinted via Orcam Group.
   https://orcamgroup.com/wp-content/uploads/2012/10/pmpt-engineering-targeted-returns-and-risks.pdf
   [high]

9. Bridgewater Associates. "The All Weather Story."
   https://www.bridgewater.com/research-and-insights/the-all-weather-story
   [medium]

## See Also

- `library/portfolio-risk-management/modern-portfolio-theory.md` --
  the Markowitz framework that risk parity builds upon and improves
  upon by replacing return estimation with risk-only allocation.
- `library/portfolio-risk-management/diversification-mathematics.md` --
  the correlation mechanics that make risk-balanced diversification
  more effective than capital-weighted diversification.
- `library/portfolio-risk-management/portfolio-rebalancing-strategies.md` --
  the discipline required to maintain risk parity and factor
  exposures through market cycles, including the behavioral
  challenge of holding through underperformance.
- `library/portfolio-risk-management/kelly-criterion.md` -- the
  geometric growth framework that connects position sizing to
  risk parity's risk-budgeting logic.