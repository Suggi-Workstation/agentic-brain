---
name: valuation-multiples-pe-ev-ebitda-pb-analysis
id: 20260725T171650Z
tier: library-topic
domain: valuation-screening
author: Researcher-1
tags: [valuation-multiples, price-to-earnings, ev-ebitda, price-to-book, price-to-sales, cape-ratio, comparable-company-analysis, relative-valuation]
links: [library/valuation-screening/discounted-cash-flow-dcf-methodology.md, library/valuation-screening/anchor-valuation-screening.md, library/value-investing/margin-of-safety.md]
---

# Valuation Multiples -- Why the Most Common Valuation Tools Are Also the Most Misused

Valuation multiples -- price-to-earnings (P/E), EV/EBITDA, price-to-book
(P/B), and price-to-sales (P/S) -- are the most widely used tools in
equity valuation because they offer speed, simplicity, and direct
comparability to market prices. But this convenience masks a dangerous
trap: every multiple has a specific set of conditions under which it
produces meaningful results, and using the wrong multiple for the wrong
company type produces not just noise but systematically misleading
conclusions. The skill is not in calculating a multiple -- it is in
knowing which multiple to use, when it fails, and how to adjust for
differences in growth, profitability, capital structure, and accounting
quality between the target company and its comparables.

## Background

The practice of valuing companies by comparing them to similar firms
dates back to the earliest days of organized securities markets. Before
discounted cash flow analysis became widespread in the 1960s and 1970s,
investors relied almost exclusively on rules of thumb: a stock should
trade at so many times its earnings, so many times its book value, or
so many times its dividends. Benjamin Graham, in the 1934 first edition
of Security Analysis co-authored with David Dodd, codified many of
these heuristics, recommending that defensive investors buy stocks
trading below 15 times average earnings and below 1.5 times book value.

The shift from heuristic rules to formalized relative valuation took
hold in the 1980s and 1990s as investment banking and equity research
professionalized. The method of comparables -- selecting a peer group
of publicly traded companies, computing their valuation multiples, and
applying the median or mean multiple to the target -- became the
standard first-pass valuation technique on Wall Street. Surveys of
equity analysts consistently find that over 90% use market multiples
as part of their valuation process, with P/E used by 88% and EV/EBITDA
used by 77% of analysts (Morgan Stanley, 2024). DCF analysis is widely
taught but, in practice, multiples dominate everything from sell-side
research reports to merger fairness opinions.

The academic foundation for multiples came from two directions. First,
the efficient market hypothesis provided a theoretical justification:
if markets price securities correctly on average, then the multiples
at which comparable firms trade reflect their fundamental value, and
deviations from the peer group signal mispricing. Second, fundamental
analysis demonstrated that every multiple can be derived from a
discounted cash flow model given assumptions about growth, profitability,
and risk -- the "justified" multiple framework. This linkage means
multiples are not arbitrary; they embed specific forecasts about future
performance. The analyst's job is to understand which forecasts are
embedded in a given multiple and whether they are reasonable.

The CAPE ratio, developed by Robert Shiller and John Campbell in 1988,
extended the multiples framework to the market level. By using a
ten-year average of inflation-adjusted earnings as the denominator,
Shiller aimed to smooth out business-cycle distortions in single-year
P/E ratios. The CAPE has demonstrated a correlation of approximately
-0.55 to -0.65 with subsequent ten-year real returns over 145 years
of data -- making it the most robust single-factor predictor of
long-term equity returns available. Shiller's work earned him the
2013 Nobel Prize in Economics and elevated the CAPE to the status of
academic reference for long-term market valuation.

## Core Concepts

### The Fundamental Divide: Equity Value Multiples vs. Enterprise Value Multiples

All valuation multiples fall into one of two categories, and confusing
them is perhaps the single most common error in applied valuation.

**Equity value multiples** use the market value of equity (share price
or market capitalization) in the numerator and a metric attributable
to equity holders in the denominator. The canonical examples are P/E
(price-to-earnings), P/B (price-to-book), and P/S (price-to-sales).
Because the numerator represents only equity, these multiples are
sensitive to capital structure. A highly leveraged company will show a
higher return on equity and potentially a higher P/E multiple than an
unlevered peer with identical operating performance -- not because the
business is better, but because financial risk is concentrated on a
smaller equity base.

**Enterprise value multiples** use enterprise value (market cap plus
debt minus cash) in the numerator and a metric attributable to all
capital providers in the denominator. EV/EBITDA, EV/EBIT, and EV/Sales
are the most common. Because enterprise value includes both debt and
equity, these multiples are capital-structure-neutral. Two companies
with identical operating profiles will have the same EV/EBITDA
regardless of how much debt each carries. This makes EV multiples
inherently better for comparing companies with different leverage,
and they should be the default choice in most cross-company analyses
unless there is a specific reason to use equity multiples.

The principle is simple: match the numerator to the denominator. If
the denominator is a pre-interest metric (EBITDA, EBIT, revenue), the
numerator must be enterprise value. If the denominator is a post-interest
metric (net income, earnings per share, book value of equity), the
numerator must be equity value. Violating this rule produces a ratio
that is economically meaningless.

### P/E Ratio: The Default Multiple and Its Hidden Assumptions

The price-to-earnings ratio is the most intuitive and widely quoted
valuation multiple. P/E = share price / earnings per share (EPS). It
answers the question: how many years of current earnings is the market
willing to pay for this company?

The justified P/E, derived from the Gordon Growth Model, reveals what
drives the multiple:

Justified P/E = (Dividend Payout Ratio) / (Required Return - Growth Rate)

This equation makes explicit that a higher P/E is justified by: (1) a
higher dividend payout ratio, (2) a lower required rate of return (i.e.,
lower risk), or (3) higher expected earnings growth. A stock trading at
30x earnings is not necessarily overvalued; it may simply be a
high-growth, low-risk business that deserves a premium multiple.

The P/E's greatest weakness is its denominator: earnings. Net income
is the bottom-line number most subject to accounting distortions.
Non-recurring items (asset sales, restructuring charges, litigation
settlements), different depreciation schedules, inventory accounting
methods (LIFO vs. FIFO), and management discretion over accruals all
flow through earnings. Two companies with identical economic performance
can report materially different EPS. Furthermore, when earnings are
negative, the P/E is undefined -- a limitation that makes it useless
for early-stage companies, cyclically depressed firms, and turnaround
situations.

The P/E is also distorted by capital structure. Because interest expense
is deducted before reaching net income, a leveraged company may report
lower earnings (depressing the denominator and inflating the P/E) even
if its operating business is identical to an unlevered peer. Comparing
P/E multiples across companies with different debt levels produces
misleading results. For cross-company comparison, EV/EBIT or EV/EBITDA
is usually superior.

### EV/EBITDA: The Workhorse Multiple and the CapEx Blind Spot

EV/EBITDA is the most commonly used enterprise value multiple. EBITDA
(earnings before interest, taxes, depreciation, and amortization) serves
as a rough proxy for operating cash flow available to all capital
providers. Its key advantage is that by removing depreciation and
amortization -- non-cash charges that vary significantly with accounting
policy and acquisition history -- it facilitates comparison across
companies with different asset bases, different acquisition histories,
and different depreciation methods. EBITDA also normalizes for capital
structure (interest excluded) and tax jurisdiction (taxes excluded).

The multiple typically ranges from 6.0x to 18.0x across industries,
with higher multiples commanded by asset-light, high-growth businesses
and lower multiples by capital-intensive, slow-growth firms.

However, EV/EBITDA has a critical blind spot that is among the most
important concepts in applied valuation: by removing depreciation,
EBITDA ignores the cost of maintaining and replacing a company's
physical assets. For a capital-intensive business -- a manufacturer,
mining company, airline, or utility -- depreciation is a real economic
cost. Equipment wears out, facilities must be replaced, and if
depreciation does not accurately reflect maintenance capex, EBITDA
overstates the cash actually available to capital providers. A steel
mill and a software company might both trade at 10x EBITDA, but the
steel mill must reinvest a large fraction of that EBITDA just to
maintain its productive capacity, while the software company can
distribute nearly all of it.

The author's assessment is that EV/EBITDA is best used as a first-pass
filter, not a final answer. For capital-intensive industries, EV/EBIT
(which treats depreciation as a real cost) or EV/(EBITDA minus
maintenance capex) provides a truer picture. Warren Buffett has been
explicit on this point: he considers depreciation a genuine expense and
views EBITDA-based valuation with suspicion in asset-heavy businesses.

### P/B Ratio: The Tangible-Asset Trap

Price-to-book value (P/B) compares a company's market capitalization to
its accounting book value of equity. Historically, it was the signature
metric of value investing. Benjamin Graham's net-net strategy targeted
stocks trading below two-thirds of net current asset value -- an extreme
form of P/B screening. The Fama-French three-factor model (1993)
established book-to-market as one of the two primary factors explaining
cross-sectional stock returns, cementing P/B's place in academic
finance.

But P/B has a fundamental and growing problem that limits its usefulness
in the modern economy: book value is an accounting construct that
systematically understates the value of intangible assets. Research and
development, brand equity, customer relationships, proprietary software,
and human capital -- the primary sources of competitive advantage in
today's knowledge economy -- are either expensed immediately (R&D under
GAAP, though software development costs can be capitalized) or never
appear on the balance sheet at all. A pharmaceutical company with a
pipeline of patented drugs, a consumer brand with decades of loyalty,
or a technology platform with network effects will all show book values
that are a fraction of their true economic worth.

The result is that P/B works reasonably well for asset-heavy businesses
where book value approximates replacement cost -- banks, insurers, real
estate companies, industrial manufacturers -- and produces systematically
misleading results for asset-light, intangible-rich businesses. A
software company might trade at 15x book value not because it is
overvalued but because its balance sheet captures almost none of its
economic assets. The author's synthesis is that P/B is best restricted
to financial companies (where assets are marked to market) and
asset-heavy industrials, and should be avoided entirely for technology,
consumer, and healthcare companies.

### P/S Ratio: The Last-Resort Multiple

Price-to-sales (P/S) compares market capitalization to total revenue.
Its primary appeal is that revenue is the least manipulable line on the
income statement -- it sits above all the accounting choices that affect
earnings and cash flow. Revenue is also never negative, making P/S
usable when P/E and EV/EBITDA are undefined.

P/S is most appropriate for: (1) early-stage companies with negative
earnings where revenue growth is the primary valuation driver, (2)
cyclical companies at the trough of their cycle when earnings are
depressed, and (3) as a check on other multiples (a company that looks
cheap on P/E but expensive on P/S likely has unsustainably high margins).

The critical limitation of P/S is that it ignores profitability entirely.
Two companies with identical revenue but gross margins of 20% and 80%
will trade at vastly different P/S multiples for good reason -- the
high-margin company generates far more value per dollar of revenue.
Using P/S without also examining margins is one of the most common
errors in growth-stock analysis. The justified P/S ratio, derived from
fundamentals, is:

Justified P/S = (Net Profit Margin * Dividend Payout Ratio) /
(Required Return - Growth Rate)

This shows that P/S is positively related to profit margin: higher-margin
businesses deserve higher P/S multiples. EV/Sales is conceptually
preferable to P/S because it uses enterprise value in the numerator,
making it neutral to capital structure differences.

### The CAPE Ratio: Cyclically Adjusted for Market-Level Valuation

The Shiller CAPE (Cyclically Adjusted Price-to-Earnings) ratio addresses
the single-year earnings distortion that plagues the standard P/E.
Instead of dividing price by the most recent year's EPS, CAPE divides
by the ten-year average of real (inflation-adjusted) earnings. This
smoothing eliminates the illusion of cheapness at the top of the cycle
(when earnings are artificially high) and the illusion of expensiveness
at the bottom (when earnings are depressed).

Empirically, the CAPE has demonstrated a correlation of -0.55 to -0.65
with subsequent ten-year real S&P 500 returns over the 1881-2025 period.
A regression of the form Real Return 10Y = 9.04% - 0.16 * CAPE explains
approximately 40% of the variance in future decadal returns -- far more
than any other single valuation metric. Four historical regimes
structure the data: deep value (CAPE below 10, observed after major
crises), normal (13-20), elevated (20-30), and extreme (above 30,
observed three times: 1929, 1999, and since 2021).

The CAPE has important limitations. First, it is a decadal predictor,
not a timing signal -- it can remain elevated for years before a
correction. Second, rising share buybacks inflate EPS without changing
total earnings, mechanically pushing up the CAPE over time relative to
historical averages. Third, the changing composition of the S&P 500
toward higher-margin, asset-light technology companies may justify a
structurally higher CAPE than the historical median, as Jeremy Siegel
has argued. Fourth, comparing CAPE across countries is problematic
because differences in sector composition, buyback prevalence, and
accounting standards affect the ratio independently of valuation.

### The PEG Ratio: Growth-Adjusted P/E

The Price/Earnings-to-Growth (PEG) ratio divides the P/E by the
expected earnings growth rate: PEG = P/E / EPS Growth Rate (%). A PEG
of 1.0 is often cited as indicating fair value -- the idea being that
a stock deserves a P/E equal to its growth rate. Below 1.0 suggests
undervaluation; above 1.0 suggests overvaluation.

The PEG's virtue is that it explicitly accounts for the fact that a
fast-growing company deserves a higher P/E. A stock at 30x earnings
growing at 30% annually may be cheaper than a stock at 15x earnings
growing at 5%. However, the PEG has significant flaws. The growth rate
used is a forecast, and small changes in the growth assumption produce
large swings in the PEG. The linear relationship between P/E and growth
implied by PEG = 1.0 is a heuristic, not a theoretical requirement.
And the PEG breaks down for slow-growth or no-growth companies (a zero
growth rate makes the PEG undefined).

### Comparable Company Selection: The Most Important Step

Every multiples analysis is only as good as the peer group it uses. The
method of comparables requires selecting companies that are genuinely
comparable on the dimensions that drive valuation: industry, size,
growth rate, profitability (margins, ROIC), and risk profile. Common
errors include:

Using too broad a set of comparables. A large-cap branded consumer
company with 25% EBITDA margins and 10% organic growth is not comparable
to a small-cap private-label manufacturer with 8% margins and 2% growth,
even though both are in "consumer products."

Using the wrong central tendency measure. When a peer group contains
outliers, the median is more robust than the mean. For industry multiples
where sample sizes are small, the harmonic mean may be more appropriate.

Failing to adjust for differences. If the target company grows faster
than the peer group, its multiple should be higher. If its margins are
lower, its multiple should be lower. The analyst must quantify and
adjust for these differences rather than mechanically applying the
peer group median.

## Evidence

The academic evidence on valuation multiples spans decades and converges
on several robust findings.

First, multiples do contain information about future returns. Fama and
French (1992, 1993) demonstrated that stocks with low P/E and low P/B
ratios (value stocks) earn higher subsequent returns than stocks with
high multiples (growth stocks). This value premium has been documented
across markets, time periods, and asset classes, and its persistence
after accounting for risk -- the central puzzle of the value premium
debate -- suggests that investor over-extrapolation of recent growth
and neglect of mean reversion systematically inflate high-multiple
stocks and depress low-multiple stocks.

Second, the choice of multiple matters enormously for the accuracy of
the valuation. Liu, Nissim, and Thomas (2002) compared the valuation
accuracy of various multiples and found that forward earnings-based
multiples (especially those based on analysts' consensus EPS forecasts)
outperform trailing multiples, and that earnings-based multiples
generally outperform sales-based and book-value-based multiples for
mature, profitable companies. However, for loss-making firms, revenue
multiples provide better valuation estimates than earnings multiples,
which are undefined or economically meaningless.

Third, the Shiller CAPE ratio's predictive power over ten-year horizons
is the most robust single-factor relationship in equity valuation. The
-0.55 to -0.65 correlation between CAPE and subsequent decadal returns,
documented across 145 years of US data (Shiller, 2000; updated through
2025), substantially exceeds the predictive power of trailing P/E,
forward P/E, dividend yield, price-to-book, or any other single valuation
ratio over the same horizon. The relationship is not an artifact of a
specific period: it holds across sub-periods, and similar patterns
emerge in international markets.

However, the value premium has weakened since the 2007-2009 financial
crisis, and the rise of intangible-intensive business models has
degraded the information content of traditional multiples. Morgan
Stanley (2024) research notes that the shift toward intangible assets
means "both earnings and invested capital are understated, weakening
the signal that earnings and multiples formerly provided." The P/B
ratio, in particular, has become less effective as a return predictor
as the economy has shifted from tangible-capital-intensive manufacturing
to intangible-capital-intensive services and technology. This does not
mean multiples are obsolete; it means they require more thoughtful
application than in the past, with explicit adjustment for accounting
distortions introduced by intangible investment.

Aptus Capital Advisors (2024) documented three additional limitations
of the CAPE ratio: the changing composition of the S&P 500 index means
current prices reflect the current (larger) earnings power of dominant
technology companies while the denominator includes their much smaller
earnings from a decade ago; share buybacks mechanically increase EPS
and thus the CAPE independently of business performance; and cross-market
CAPE comparisons fail to account for systematic differences in earnings
growth rates and buyback prevalence across countries.

## Implications

For the practicing investor, the implications of understanding multiples
properly are profound and directly actionable.

**Match the multiple to the business model.** There is no universal
"best" multiple. For a stable, profitable industrial company, EV/EBIT
or P/E (with appropriate adjustments) is appropriate. For a capital-intensive
business, EV/EBITDA minus maintenance capex or EV/EBIT will prevent
the CapEx blind spot. For a financial company, P/B and P/E are the
standard tools. For a high-growth, money-losing technology company, P/S
or EV/Revenue -- always analyzed alongside gross margin trends -- is
the least bad option. For a deeply cyclical company at a trough, use
normalized (mid-cycle) earnings or the CAPE framework rather than
current P/E.

**Never use a single multiple in isolation.** Different multiples tell
different stories because they capture different slices of a company's
economics. A company that looks cheap on P/E but expensive on EV/EBITDA
likely has an unusually low tax rate or an unsustainable capital structure.
A company that looks cheap on P/B but expensive on P/E may have low
returns on equity that justify the discount. Triangulating across at
least three multiples -- one equity value, one enterprise value, and
one growth-adjusted -- provides a much more robust picture than any
single metric.

**Understand the fundamentals embedded in the multiple.** Every multiple
implies assumptions about future growth, profitability, and risk. A P/E
of 25x for a company growing earnings at 5% implies either that growth
will accelerate dramatically, that the company's risk has declined, or
that the market is overpaying. The analyst's task is to make these
embedded assumptions explicit and judge whether they are plausible. The
justified multiple framework -- deriving what multiple a company should
trade at given fundamentals -- turns multiples from crude screening
tools into disciplined valuation instruments.

**Adjust, always adjust.** The raw median multiple of a peer group is a
starting point, not a conclusion. If the target company grows faster
than its peers, apply a premium. If it earns lower margins, apply a
discount. If it carries more leverage, use EV multiples to neutralize
the distortion or explicitly adjust equity multiples for the difference.
The difference between a competent valuation and a sloppy one is in
the adjustments.

**For market-level valuation, use CAPE but do not worship it.** The
CAPE is the best single indicator of long-term expected returns available,
but it explains only about 40% of the variance in subsequent ten-year
returns. The remaining 60% is driven by factors the CAPE does not
capture: changes in the equity risk premium, shifts in corporate tax
policy, the evolution of sector composition, and genuine innovations
in the economy that alter the sustainable level of profitability. Treat
the CAPE as a regime indicator -- deep value, normal, elevated, extreme
-- rather than a precision forecast. Combine it with other indicators:
the equity risk premium relative to bonds, corporate profit margins
relative to GDP, and measures of investor sentiment.

## Sources

1. CFA Institute. "Market-Based Valuation: Price and Enterprise Value
   Multiples." CFA Program Curriculum, Refresher Reading (2026).
   https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/market-based-valuation-price-enterprise-value-multiples [high]

2. Morgan Stanley Investment Management. "Valuation Multiples." (2024).
   https://www.morganstanley.com/im/publication/insights/articles/article_valuationmultiples.pdf [high]

3. Shiller, R. & Campbell, J. (1988). "Stock Prices, Earnings, and
   Expected Dividends." Journal of Finance, 43(3), 661-676. [high]

4. Shiller, R. (2000). "Irrational Exuberance." Princeton University
   Press. [high]

5. Fama, E. & French, K. (1992). "The Cross-Section of Expected Stock
   Returns." Journal of Finance, 47(2), 427-465. [high]

6. Liu, J., Nissim, D., & Thomas, J. (2002). "Equity Valuation Using
   Multiples." Journal of Accounting Research, 40(1), 135-172. [high]

7. Jacobs, B. (2024). "Beware CAPE Crusaders: Limitations of Shiller's
   Ratio in Modern Market Valuation." Aptus Capital Advisors.
   https://aptuscapitaladvisors.com/beware-cape-crusaders-limitations-of-shillers-ratio-in-modern-market-valuation/ [medium]

8. Macabacus. "Valuation Multiples: Enterprise vs Equity, P/E, EBITDA."
   https://macabacus.com/valuation/multiples [medium]

9. PrepLounge. "Multiples in Corporate Valuation (PE, EV/EBITDA etc.)."
   https://www.preplounge.com/en/finance-interview-basics/multiples [medium]

## See Also

- `library/valuation-screening/discounted-cash-flow-dcf-methodology.md` --
  the other major branch of valuation: absolute DCF instead of relative
  multiples.
- `library/value-investing/margin-of-safety.md` -- why Ben Graham insisted
  on buying below intrinsic value regardless of the multiple used.
- `library/valuation-screening/anchor-valuation-screening.md` -- the
  domain anchor defining what belongs in this domain.
