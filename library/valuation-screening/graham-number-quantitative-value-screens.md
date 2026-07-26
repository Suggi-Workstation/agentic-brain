---
name: graham-number-quantitative-value-screens
id: 20260726T121602Z
tier: library-topic
domain: valuation-screening
author: Researcher-1
tags: [graham-number, quantitative-screening, value-investing, net-net, defensive-investor, benjamin-graham, margin-of-safety]
links: [library/valuation-screening/discounted-cash-flow-dcf-methodology.md, library/valuation-screening/valuation-multiples-pe-ev-ebitda-pb-analysis.md, library/value-investing/anchor-value-investing.md]
---

# The Graham Number and Quantitative Value Screens -- Why Mechanical Filters Produce Superior Returns but Require Human Judgment

Quantitative value screens, epitomized by Benjamin Graham's Graham
Number formula (sqrt(22.5 x EPS x BVPS)), are mechanical rules that
filter the universe of stocks down to a manageable set of candidates
trading below conservative estimates of intrinsic value. Research
spanning nearly a century -- from Graham's own partnership returns
through Fama and French's (1992) demonstration that high book-to-market
stocks outperform -- confirms that systematic cheapness screens
generate excess returns. But the same evidence reveals a critical
caveat: purely mechanical screens produce false positives (value traps)
at a rate that demands qualitative overlay. The screens identify
candidates; human judgment determines which candidates are bargains and
which are cheap for good reason.

## Background

Benjamin Graham developed his quantitative screening framework over
decades of teaching at Columbia Business School and managing the
Graham-Newman partnership (1936-1956). His approach was a response to
the speculative excesses of the 1920s and the subsequent Great
Depression, which wiped out investors who had paid any price for growth.
Graham's core insight was that a stock's price and its underlying value
are distinct things -- the market is a voting machine in the short run
but a weighing machine in the long run. Quantitative screens
operationalize this insight by converting accounting data into buy/sell
rules.

Graham first articulated his screening approach in Security Analysis
(1934, co-authored with David Dodd) and later refined it for individual
investors in The Intelligent Investor (1949). The Intelligent Investor
introduced the distinction between the "defensive" (passive) investor,
who wants reasonable returns with minimal effort, and the "enterprising"
(active) investor, who is willing to do the work for superior results.
The Graham Number was designed for the defensive investor: a single
formula that caps the maximum price one should pay.

The quantitative screening tradition evolved dramatically after Graham.
The rise of computing power in the 1980s and 1990s enabled researchers
to test mechanical value strategies across thousands of stocks and
decades of data. The most influential study was Fama and French (1992),
which demonstrated that stocks with high book-to-market ratios (low P/B,
i.e., value stocks) produced significantly higher returns than stocks
with low book-to-market ratios (growth stocks), even after controlling
for market beta. This finding legitimized quantitative value screening
within academic finance and spawned the modern factor investing
industry.

## Core Concepts

### The Graham Number: Architecture of a Defensive Screen

The Graham Number formula is: square root of (22.5 x EPS x BVPS). Each
component encodes a specific constraint. The constant 22.5 is not
arbitrary: it is the product of Graham's two maximum valuation
multiples. A stock should trade at no more than 15 times earnings (P/E
<= 15) and no more than 1.5 times book value (P/B <= 1.5). Multiplying
these constraints together -- 15 x 1.5 = 22.5 -- and placing the result
under a square root creates a single maximum-price ceiling that enforces
both limits simultaneously.

The formula's mathematical derivation works as follows. If P/E <= 15,
then Price <= 15 x EPS. If P/B <= 1.5, then Price <= 1.5 x BVPS.
Squaring both sides of the inequality and combining: Price squared <=
(15 x EPS) x (1.5 x BVPS) = 22.5 x EPS x BVPS. Taking the square root
yields the Graham Number: the maximum price at which both constraints
can be satisfied.

The Graham Number has important boundary conditions. Both EPS and BVPS
must be positive -- the formula is undefined for unprofitable companies
or those with negative equity. This is by design: Graham considered
companies that cannot generate earnings or that have destroyed
shareholder capital to be outside the defensive investor's universe
regardless of how cheap they appear. The Graham Number also implicitly
assumes that book value is a meaningful measure of asset backing, which
makes it most appropriate for asset-heavy industries (manufacturing,
financials, utilities) and least appropriate for asset-light businesses
(technology, services, brand-driven companies) where most value resides
in intangible assets not reflected on the balance sheet.

Graham intended the EPS figure to be a multi-year average -- typically
three years -- rather than a single year's earnings. This reduces the
risk of buying into cyclically inflated earnings that will mean-revert.
He also required that the underlying company pass qualitative screens
before applying the formula: adequate size, strong financial condition
(current ratio >= 2, long-term debt < net current assets), at least 10
years of uninterrupted dividends, earnings growth of at least 33% over
the prior decade, and a P/E below 15 using three-year average earnings.

### Net-Net Working Capital: The Ultimate Margin of Safety

Graham's most extreme quantitative screen is the net-net working capital
(NNWC) approach, which he introduced in Security Analysis (1934). A
stock qualifies as a net-net when its market capitalization falls below
its net current asset value (NCAV), defined as current assets minus all
liabilities (both current and long-term, plus preferred stock). In other
words, the market values the entire company at less than the liquidation
value of its current assets alone, after paying off every liability.

Graham typically required the price to be no more than two-thirds (67%)
of NCAV to provide an adequate margin of safety. At this price, an
investor is essentially buying the company's cash, receivables, and
inventory at a discount while receiving all fixed assets (property,
plant, equipment) and any future earnings for free. Graham recommended
diversifying across at least 30 such positions because some would
inevitably turn out to be value traps -- companies so broken that even
liquidation would not recover the NCAV.

Walter Schloss, who worked for Graham and later ran his own partnership
(1956-2002), implemented a pure net-net strategy and compound annual
returns of approximately 16% over 45 years, dramatically outperforming
the S&P 500. Schloss did no management meetings, no industry research,
and no DCF modeling. He screened for stocks trading below net working
capital, bought 50-100 positions, and sold when they reached book value.

Warren Buffett ran a concentrated net-net strategy during his Buffett
Partnership years (1956-1969), achieving compound annual returns of
approximately 30%. He later described these as "cigar butt" investments:
companies with one free puff left in them. Buffett abandoned the
approach in the 1970s as his capital base grew too large for small-cap
net-nets and as he shifted toward buying quality businesses at fair
prices under Charlie Munger's influence.

### Low P/E, Low P/B, and High Dividend Yield Screens

Beyond the Graham Number and net-nets, a family of single-metric and
multi-metric screens emerged from Graham's principles. The low P/E
screen identifies stocks trading at low multiples of earnings,
reflecting the market's pessimism about future growth. The low P/B
screen identifies stocks trading at a discount to accounting book value,
capturing the idea that assets have a floor value even if earnings are
temporarily depressed. The high dividend yield screen identifies mature,
cash-generating companies that return capital to shareholders.

The academic evidence strongly supports these screens. Fama and French
(1992) showed that sorting US stocks by book-to-market (the inverse of
P/B) produced a value premium of approximately 4-5% annually for the
highest quintile compared to the lowest, over the period 1963-1990.
Lakonishok, Shleifer, and Vishny (1994) demonstrated that value
strategies (low P/E, low P/B, low P/CF) outperformed glamour strategies
by 10-11% annually from 1968 to 1990 across multiple markets. The
authors attributed much of the premium to systematic investor errors:
over-extrapolation of past growth and naive expectation that good
companies are necessarily good investments.

### The Seven Defensive Investor Criteria

Graham provided a complete checklist of seven criteria for defensive
investors in The Intelligent Investor, going well beyond the Graham
Number alone. These criteria form a multi-dimensional quantitative
screen: (1) adequate size -- excluded small companies subject to
above-average volatility; (2) strong financial condition -- current
ratio of at least 2:1; (3) earnings stability -- positive earnings in
each of the past 10 years; (4) dividend record -- uninterrupted
dividend payments for at least 20 years; (5) earnings growth -- minimum
33% increase in per-share earnings over the past decade using three-year
averages; (6) moderate P/E ratio -- no more than 15 times average
earnings of the past three years; and (7) moderate price-to-book --
no more than 1.5 times book value. The Graham Number collapses criteria
6 and 7 into a single formula, but Graham intended it as a quick
preliminary screen, not a substitute for the full seven-criteria
checklist.

## Evidence and Research Foundation

The empirical case for quantitative value screens rests on multiple
independent research streams spanning decades. The most foundational
contribution comes from Fama and French (1992), who published "The
Cross-Section of Expected Stock Returns" in the Journal of Finance.
Their study demonstrated that two variables -- market capitalization
(size) and book-to-market equity ratio -- capture the cross-sectional
variation in average stock returns more effectively than the
single-factor Capital Asset Pricing Model. The high book-to-market
(value) premium was economically large (approximately 0.4% per month,
or roughly 5% annually) and statistically significant across the full
1963-1990 sample. This was not a marginal anomaly; it was a
first-order effect that challenged the central paradigm of academic
finance. The finding was subsequently replicated internationally by
Fama and French (1998), confirming the value premium across 13 major
markets including Japan, the UK, France, Germany, and Australia, and
reinforcing the conclusion that the value effect is not a data-mining
artifact of US markets.

Lakonishok, Shleifer, and Vishny (1994) took a behavioral approach in
"Contrarian Investment, Extrapolation, and Risk," published in the
Journal of Finance. They constructed portfolios sorted by P/E, P/B,
P/CF, and sales growth and found that value stocks outperformed glamour
stocks by wide margins. Crucially, they showed that the outperformance
was not explained by higher risk (value stocks did not have higher betas
or higher downside during recessions), suggesting the premium arises
from cognitive biases rather than rational risk compensation.

The net-net strategy has its own empirical record. Oppenheimer (1986)
tested a modified NCAV strategy (price < NCAV) on US equities from
1970 to 1983, finding annualized returns of 29% versus 12% for the
market. More recently, a 2014 academic study replicated the NCAV
strategy for the 2003-2010 period and found annualized geometric returns
of 24.7%, with excess returns unexplained by the CAPM, Fama-French
three-factor, or Carhart four-factor models. The persistence of the
return anomaly suggests it capitalizes on a deeply structural market
inefficiency: institutional investors cannot deploy meaningful capital
into micro-cap stocks, leaving them systematically underpriced.

However, the evidence also reveals limitations. Purely mechanical value
screens generate a high proportion of value traps -- companies that
appear cheap because their business is in terminal decline. Piotroski
(2000) demonstrated that applying a simple F-Score (a 9-point
fundamental health check) to the cheapest quintile of book-to-market
stocks eliminated most of the underperformers and roughly doubled the
value premium. This finding underscores a fundamental truth about
quantitative screens: they are starting points for further analysis, not
final answers. The screen provides the candidate list; the investor
provides the judgment to separate the bargains from the value traps.

## Implications

For investors building a systematic process, quantitative screens occupy
a critical middle layer between investment philosophy and practical
execution. The Graham Number and its derivatives provide an initial
filter that reduces the investable universe from thousands of stocks to
a few dozen candidates that warrant deeper analysis. This is not mere
convenience -- it is a structured defense against the behavioral biases
that lead investors to overpay. By committing to a screen before looking
at the details of any individual company, the investor eliminates the
most common error in investing: falling in love with a story and then
rationalizing whatever price the market asks.

The screens also serve as a discipline mechanism. A stock that fails the
Graham Number test is one where the market price exceeds Graham's
conservative estimate of maximum defensible value. The investor who buys
such a stock is making an implicit claim: "I know something the market
does not, and my insight justifies paying above Graham's ceiling." That
claim may occasionally be correct -- the world is full of great
businesses that always traded above Graham multiples -- but it shifts
the burden of proof onto the investor's forecasting ability. Graham's
framework forces investors to acknowledge when they are speculating on
future growth rather than investing in current value.

In portfolio construction, quantitative screens address the practical
problem of maintaining a value discipline in rising markets. Bull
markets gradually eliminate value candidates because prices rise faster
than fundamentals. A mechanical screen keeps the investor honest: when
the screen produces zero candidates, the investor receives an objective
signal that the market is expensive, which is far more reliable than
intuition or media narratives. Graham himself recommended that defensive
investors hold at least 25% in bonds when stocks appear fully valued and
up to 75% when bargains are plentiful -- a mechanical asset allocation
rule driven by the availability of screened candidates.

The integration of quantitative screens with modern factor investing
opens additional applications. Multi-factor models that combine value
(low P/B, low P/E) with quality (high profitability, low leverage) and
momentum produce more consistent returns than value alone, reducing the
frequency and severity of value traps. The author's assessment is that
Graham's original seven-criteria checklist was arguably the first
multi-factor model: it combined size, financial strength, earnings
stability, dividend history, earnings growth, and two valuation
multiples into a single pass/fail screen. Modern factor investors are
reproducing Graham's insight with more sophisticated statistical
machinery.

## Common Pitfalls and Limitations

The most significant pitfall in applying quantitative value screens is
treating them as fully automated buy signals. A screen that produces a
list of candidates passing all criteria still contains both bargains and
value traps. The difference between the two requires qualitative
analysis: assessing competitive position, management quality, industry
trajectory, and the sustainability of the economic moat. No mechanical
rule can replace this judgment because the accounting data the screen
uses reflects the past, while investment returns depend on the future.

A second pitfall is sector incompatibility. The Graham Number assumes
book value is a meaningful floor, which breaks down for asset-light
businesses, technology companies, and firms with significant intangible
assets not on the balance sheet (brands, patents, software, network
effects). Applying the Graham Number to a company like Microsoft or
Alphabet would produce nonsensically low ceilings because most of their
value is in intellectual property and competitive position, not
physical assets. The screen must be matched to the sector: P/B-based
screens for financials and industrials; earnings-based screens for
consumer staples; and entirely different frameworks for technology and
healthcare.

A third limitation is survivorship and look-ahead bias in backtests.
Many studies that show spectacular returns for mechanical strategies
use databases that exclude delisted and bankrupt companies, or they use
accounting data that would not have been available at the screening date
(restated financials, final rather than preliminary filings). Real-world
implementation faces additional friction: many net-net candidates are
illiquid micro-caps with spreads of 5-10%, making the theoretical return
unachievable after transaction costs.

## Sources

1. Graham, B. & Dodd, D. (1934). Security Analysis. McGraw-Hill.
   The foundational text that introduced net-net working capital
   screening and the framework of buying below intrinsic value. [high]

2. Graham, B. (1949, revised 1973). The Intelligent Investor.
   Harper & Brothers. Chapters 7 (defensive investor portfolio policy)
   and 14 (stock selection for the defensive investor) contain the
   Graham Number derivation and the seven defensive criteria. [high]

3. Fama, E.F. & French, K.R. (1992). "The Cross-Section of Expected
   Stock Returns." Journal of Finance, 47(2), 427-465. The seminal
   academic paper demonstrating that high book-to-market stocks
   (value) outperform low book-to-market stocks (growth). [high]

4. Lakonishok, J., Shleifer, A., & Vishny, R.W. (1994). "Contrarian
   Investment, Extrapolation, and Risk." Journal of Finance, 49(5),
   1541-1578. Demonstrates that value strategies outperform glamour
   strategies, attributing the premium to behavioral biases rather
   than risk. [high]

5. GrahamValue. "Using The Graham Number Correctly."
   https://www.grahamvalue.com/article/using-graham-number-correctly
   Detailed derivation of the Graham Number from Graham's seven
   criteria and includes the critical point about using multi-year
   average EPS. [medium]

6. Investopedia. "Graham Number: Definition, Formula, Example, and
   Limitations."
   https://www.investopedia.com/terms/g/graham-number.asp
   Comprehensive reference for the formula, worked examples, and the
   limitations for asset-light companies. [medium]

## See Also

- `library/valuation-screening/discounted-cash-flow-dcf-methodology.md` -- the primary alternative valuation framework. While Graham screens are shortcut heuristics, DCF is a bottom-up intrinsic value estimate. Understanding both provides a complete valuation toolkit.
- `library/valuation-screening/valuation-multiples-pe-ev-ebitda-pb-analysis.md` -- detailed analysis of the individual multiples (P/E, P/B, EV/EBITDA) that Graham screens combine. The screens are constructed from these building blocks.
- `library/value-investing/anchor-value-investing.md` -- the philosophy that motivates quantitative screening. The screens are the "how"; the value investing domain is the "why."
- `library/portfolio-risk-management/anchor-portfolio-risk-management.md` -- the connection between individual security screening and portfolio construction. Graham's diversification requirements (10-30 stocks minimum) are risk management rules, not valuation rules.
