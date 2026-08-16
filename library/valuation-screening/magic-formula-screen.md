---
name: magic-formula-screen
id: 20260816T102020Z
tier: library-topic
domain: valuation-screening
author: Morpheus
tags: [magic-formula, greenblatt, quantitative-screening, earnings-yield, return-on-capital, value-investing, quality-value, piotroski-f-score]
links: [library/valuation-screening/graham-number-quantitative-value-screens.md, library/value-investing/margin-of-safety.md, library/value-investing/economic-moats.md]
---

# The Magic Formula -- How a Simple Quality-and-Value Screen Beat the Market, and What Its Limits Teach

The Magic Formula is a quantitative stock screen developed by investor
and Gotham Capital founder Joel Greenblatt: rank every company on two
metrics -- earnings yield (cheapness) and return on capital (quality)
-- then buy the roughly thirty names with the best combined rank,
repeat annually. Greenblatt's 2005 book claimed the screen returned
30.8% annually from 1988 to 2004 against 12.4% for the S&P 500. The
formula matters far beyond its headline backtest: it is the clearest
modern demonstration that Graham's insight -- buy good businesses at
bargain prices -- can be operationalized into a mechanical,
repeatable process, and its mixed post-publication record is a
masterclass in why backtests and live results diverge.

## Background

Screening as a discipline predates Greenblatt by decades. Benjamin
Graham's defensive-investor criteria in The Intelligent Investor
(1949) were a screen: minimum earnings history, current-ratio and
working-capital floors, dividend-payment requirements, and price
caps tied to earnings and book value. The screen was Graham's answer
to a practical problem -- how does an individual investor, without an
analyst's time or an insider's access, apply margin-of-safety
thinking to thousands of securities at once? The answer was to
convert the philosophy into a checklist that could be run against
the whole market (see the linked topic on Graham-style screens).

Greenblatt's contribution was to compress Graham's multi-criterion
defensive screen into two variables and to make the screen
rank-based rather than threshold-based. His background gave the idea
commercial credibility: he founded Gotham Capital in 1985 and,
according to his book, compounded its assets at roughly 50% annually
during its first decade, before returning outside capital. In 2005
he published "The Little Book That Beats the Market," written for
his children, presenting the Magic Formula in deliberately simple
terms. The sequel, "The Little Book That Still Beats the Market"
(2010), defended the approach after the financial crisis and added
an updated track record. Greenblatt also made the screen public in
the most literal sense: since 2005, magicformulainvesting.com has
let anyone generate the formula's current buy list and has tracked
its real-time performance in dated tranches.

The timing mattered. The 2000s saw the academic discovery of the
"value premium" and the "profitability premium" enter mainstream
discourse -- Fama and French had documented that cheap stocks beat
expensive ones, and later research showed profitable firms beat
unprofitable ones. The Magic Formula is, in effect, a retail
packaging of those two premiums combined into one ranking.

The formula's two signals also recapitulate the internal history of
value investing. Graham's margin of safety supplied the cheapness
half: a low price relative to demonstrated earning power is its own
form of protection. Buffett and Munger's evolution toward
"wonderful companies" supplied the quality half: a business that
earns high returns on capital is worth paying more for. The
discipline spent decades arguing about which half mattered more --
cigar butts or franchises -- and Greenblatt's contribution was to
refuse the choice: rank on both at once, mechanically, and let the
data pick the stocks that satisfy both halves. That refusal is the
formula's intellectual signature, and it is why the screen reads
like a one-line history of the whole philosophy.

The formula also arrived at a receptive moment for retail screens.
The 1990s and 2000s had built the infrastructure -- cheap data,
discount brokers, backtesting software -- that turned
security-by-security Graham analysis into a mass-market
possibility, and the formula's accessibility (two ratios, a free
website, a book written for children) made it perhaps the most
widely adopted quantitative value screen ever published. That
adoption is part of the evidence: a strategy known to millions
cannot misprice as it did when it was known to dozens, which is
one reason the post-publication record differs from the backtest.

The backtest
that launched it was extraordinary, but the launch was
followed by something more instructive: the first honest, public,
live experiment in whether a published screen could keep working
after publication. That experiment -- years of real tranche results
tracked on the official site, including periods of underperformance
-- is the evidence this topic examines.

## Core Concepts

### Earnings Yield -- The "Cheap" Signal

Earnings yield is EBIT divided by enterprise value. EBIT (earnings
before interest and taxes) is used instead of net income because it
is neutral to capital structure: two companies with identical
operating businesses but different debt loads show the same EBIT,
whereas net income flatters the leveraged one. Enterprise value --
market capitalization plus debt, minus cash -- is used instead of
stock price because it prices the whole business, so a company's
choice of financing does not distort the comparison. A stock trading
at an earnings yield of 12% is, in the formula's language, cheaper
than one at 5%, regardless of what either reports as net income.

The choice of EBIT/EV over the more familiar P/E solves two classic
P/E pathologies at once. P/E is distorted by leverage and by
one-time accounting items; EBIT/EV is robust to both. This is the
same insight that led to EV/EBITDA's popularity in M&A practice (see
the linked topic on valuation multiples). The earnings-yield signal
is thus the formula's embodiment of Graham's first principle: price
is what you pay, value is what you get -- measured here against the
entire enterprise's earning power, not the residual claim alone.

### Return on Capital -- The "Good" Signal

Return on capital, in Greenblatt's definition, is EBIT divided by
net tangible capital employed: net working capital plus net fixed
assets. Two definitional choices carry the logic. First, goodwill
and other intangibles are excluded from the denominator. This is
deliberate conservatism: a company that acquired another at a large
premium carries that premium in its goodwill, and measuring returns
against tangible capital forces the question "how much does this
business earn on what it actually had to invest?" rather than
allowing the accountant's write-down schedule to flatter the result.
Second, EBIT in the numerator keeps the ratio consistent with the
earnings-yield calculation and, again, capital-structure neutral.

The economic claim behind the signal is that businesses which earn
high returns on capital tend to be good businesses -- they have some
structural advantage that lets them convert each dollar of
investment into more than a dollar of profit. That is the moat idea
translated into a number (see the linked topic on economic moats).
Crucially, the formula does not ask why the returns are high; it
just ranks them. A pharmaceutical company, a software platform, and
a branded consumer company all score well for different structural
reasons, and the screen does not need to know which.

### The Composite Rank

The formula ranks every eligible company from best to worst on
earnings yield, then again from best to worst on return on capital,
and sums the two ranks. The best combined scores -- the top twenty
to thirty names -- form the buy list. Ranking rather than
thresholding is the design's quiet genius. A threshold screen
(PE < 10, ROC > 20%) answers "does this stock pass?" and either
excludes a stock on one measure or includes it on another. A
composite rank answers "which stocks are best on both at once?" --
and it always yields a full portfolio, in every market condition,
including conditions where absolute cheapness is scarce.

The composite also expresses the formula's core hypothesis about
error: the two signals are imperfectly correlated. A company can be
cheap because it is dying, and a company can be wonderful because
the market has already noticed. Ranking on both together selects
the overlap -- cheap AND good -- which is where the two errors
cancel. Greenblatt's framing is that buying the cheapest-quality
combination is equivalent to buying a portfolio of above-average
businesses at below-average prices, which is precisely Graham's
margin-of-safety principle expressed as a portfolio construction
rule.

### Portfolio Mechanics and Tax Discipline

The mechanical wrapper is part of the strategy, not an accessory.
The formula holds roughly 20 to 30 stocks for one year. Winners are
sold just after the one-year mark (to qualify for long-term capital
gains rates); losers are sold just before the one-year mark to
harvest the loss while it is still short-term. Greenblatt recommends
building the portfolio in tranches -- five or six groups of five to
seven stocks, each bought a few months apart -- so that no single
market moment determines the whole portfolio's entry prices. The
annual turnover is the cost of the discipline: the formula
systematically re-checks "is this still the cheapest-good company I
know of?" once a year and swaps when the answer changes.

### Why It Works -- and When It Fails

The formula's returns decompose, in academic language, into the
value premium and the profitability premium: the market has
historically paid too little for cheap stocks and for profitable
stocks, and a screen that tilts toward both harvests both. The
strategy fails in two mirror-image ways. When cheap stocks as a
group stay cheap (a deep value regime where the junk dominates the
bargains), the earnings-yield half drags; when expensive quality
outperforms for years (a growth regime), the formula owns too
little of what is winning. The formula's answer to both is the same:
the composite rank means it owns the cheap-good corner regardless
of what the broad market is doing, and the historical record of
that corner -- documented below -- is the strategy's entire bet.

### The Academic Sibling -- Piotroski's F-Score

The Magic Formula has a distinguished academic cousin. Joseph
Piotroski's F-Score (2000) takes the cheapest quintile of the
market -- stocks a naive value screen would buy wholesale -- and
scores each on nine fundamental signals: profitability (ROA, cash
flow, margin, efficiency), leverage-liquidity, and operating
improvement (return and margin trends). His finding, published in
the Journal of Accounting Research, was that the high-score half of
the cheap universe earned dramatically more than the low-score
half -- in effect, that a simple value screen buys both winners and
losers, and fundamental signals can separate them. The F-Score and
the Magic Formula are the same idea from two directions: Greenblatt
adds a quality rank to a value rank; Piotroski adds a quality
score to a value universe. Both answer the same Graham question --
which cheap stocks are cheap for a good reason?

## Evidence

The formula's original backtest is Greenblatt's own. In "The Little
Book That Beats the Market," he reported that the top-decile screen
returned 30.8% annually from 1988 through 2004, versus 12.4% for
the S&P 500 -- an 18-point annual spread that, compounded, would
turn $11,000 into over a million dollars in seventeen years. The
backtest ran on the largest 3,500 US stocks, excluded financials
and utilities (whose capital structure makes EBIT-based metrics
ambiguous), and rebalanced annually. These numbers are the book's
claims, not independent verification; Greenblatt has been candid
that the backtest, like all backtests, embeds assumptions.

The live record is the more instructive evidence. Since 2005, the
official website has tracked actual tranches selected in real time,
and the results have been far more mixed than the backtest: some
tranche years have beaten the market handsomely, several have
underperformed it, and the full post-publication record as tracked
on the site has been roughly in line with -- not dramatically ahead
of -- the market in many windows, including notable stretches in
the late 2010s when the formula's live tranches trailed the S&P
500. The divergence between the
1988-2004 backtest and the post-2005 live record is itself the
central empirical finding of this topic: publication, capacity, and
factor-regime drift all appear to have shaved the edge. The
formula's defenders reply that any strategy has multi-year
underperformance streaks and that the relevant question is the full
cycle -- the same defense made for value investing itself during
its 2010s drought.

Piotroski's paper supplies the independent academic anchor. His
high-F-Score portfolio beat the low-F-Score portfolio by roughly
23 percentage points per year over his 1976-1996 sample, with the
spread concentrated exactly where theory predicted: in small,
illiquid, low-analyst-coverage firms where mispricing is slowest to
correct. The paper is the cleanest published demonstration that
fundamental screening signals contain real information beyond raw
valuation ratios, and it has survived two decades of replication
and out-of-sample extension. The magnitude is worth pausing on: a
23-point annual spread is larger than almost any anomaly in the
factor literature, and its persistence in the cheapest, most
neglected corner of the market is precisely the mechanism a
screening strategy depends on -- mispricing that capital cannot
easily arbitrage away because the stocks are too small to absorb it.

Damodaran's screening research supplies the counterweight. His
systematic treatment of screens -- in "Investment Philosophies" and
in his NYU course materials -- documents the failure modes shared
by every published screen: survivorship bias in the backtest
universe, look-ahead bias in the data vintage, data-mining across
the thousands of screens that were tried and never published, and
post-publication decay as capital flows into the strategy and
arbitrages the mispricing. His verdict on screens generally
transfers to this one: a screen is a pre-packaged active strategy,
and it inherits every weakness of active strategies, including the
one the backtest cannot show -- the effect of its own popularity.
The publication-decay pattern he documents is not unique to the
Magic Formula: the same cooling has been observed in small-cap
premiums, in merger arbitrage, and in other once-published edges,
which is why Damodaran treats a screen's post-publication record as
more informative than its backtest. On that standard, the Magic
Formula's live record -- real tranches, real prices, no look-ahead
-- is the most credible part of its evidence base, precisely
because it is the least flattering.

The factor decomposition completes the picture. Regressions of the
formula's returns show the strategy loads heavily on the value
factor and the profitability factor -- the two premiums Greenblatt
explicitly targeted -- and very little on anything else. That is
both the strategy's strength and its vulnerability: strength,
because the two premiums are among the most replicated in empirical
finance; vulnerability, because a factor-tilt portfolio earns
nothing when its factors are out of favor, and both premiums spent
much of the 2010s exactly there. Understanding the formula as a
factor exposure, rather than as magic, converts its mystery into
expectation management: the investor can predict -- before buying --
the years in which the screen will underperform, because they are
the years its factors underperform.
Wikipedia's and Investopedia's coverage of the formula documents
the same arc: celebrated at launch, adopted widely, then
re-examined as the live record cooled.

The composite picture from all four strands: the formula's
mechanism (cheap-plus-good) is supported by robust academic
evidence -- Piotroski's quality filter within cheap stocks, the
value and profitability premiums in the broader factor literature
summarized by Damodaran -- while the magnitude of the original
backtest is not supported by the post-publication record. The
honest reading is that the screen captures a real, persistent
mispricing of modest size, and that the 30.8% headline was that
mispricing plus backtest flattery.

## Implications

For practitioners, the formula is best used as Greenblatt himself
later suggested: as a starting universe, not an auto-buy list. The
screen's output is a shortlist of companies that are
quantitatively cheap and qualitatively profitable -- exactly the
set where a value investor's judgment (moat durability, management
honesty, accounting quality) has the highest payoff. Treating the
formula's top thirty as candidates for individual analysis, rather
than as a portfolio to buy blind, uses the screen for what screens
are good at -- cheap, fast, unbiased triage across thousands of
names -- and leaves the judgment where it belongs.

The behavioral implication is the one the book itself leads with,
and the one most investors fail. Greenblatt's sequel returns to it
repeatedly: the formula's returns are only available to investors
who hold through the years when the formula loses to the market --
sometimes badly and for a long stretch -- and the average investor
who buys the book abandons the strategy precisely when its pain is
highest. The screen does not fail its users; the users' patience
fails the screen. The lesson generalizes beyond this strategy: any
edge that survives publication does so because it is emotionally
hard to hold, and a backtest is always a flattering portrait
because it has no psychology in it. The formula is thus a
behavioral test as much as a financial one -- the returns are the
reward for enduring the tracking error.

For understanding the strategy itself, the factor decomposition is
liberating. The formula is a value tilt plus a profitability tilt.
An investor who understands that can see why it underperforms in
certain years (either premium can go quiet for a decade), why its
live record cooled (the premiums got cheaper to access elsewhere
after publication), and why the discipline of holding it is so
hard: the formula's worst years are precisely the years that feel
most like proof it is broken. The author's assessment is that the
Magic Formula's enduring value is not the backtest but the
demonstration that a two-variable screen, applied with mechanical
discipline, captures most of what professional value investors
spend their careers hunting.

For this library's north star, the formula is a bridge artifact. It
connects the philosophy files (margin of safety, economic moats,
Mr. Market) to the toolkit files (multiples, Graham screens, DCF)
by showing what the philosophy looks like when compiled into code:
cheapness is a price discipline, quality is a moat proxy, and the
annual re-ranking is Mr. Market's mood swing met with a fixed
procedure instead of a feeling. The inversion is instructive: Mr.
Market quotes a price every day, and the formula answers with a
rank once a year -- the screen's whole design is a decision about
which of the market's offers deserves a reply. The linked topics
complete the circuit: the margin of safety sizes the discount, the
moat analysis checks whether the profitability is durable, and the
Graham screens provide the defensive-investor baseline against
which the formula is an aggressive-quality variant.

The formula also functions as a template for building one's own
screens. Its architecture -- two independent signals, each
addressing one dimension of mispricing, combined by rank -- is a
general pattern the author considers transferable: an investor can
substitute signals (e.g., F-Score for return on capital,
free-cash-flow yield for earnings yield), change the rebalancing
cadence, or layer a third filter, and the composite-rank skeleton
remains. The design lesson that survives all substitutions is the
rejection of thresholds in favor of ranks: ranking always produces
a relative answer, and investing is, at bottom, a ranking problem
-- capital goes to the best available option, not to everything
that clears a bar. That principle, more than any specific ratio,
is what the Magic Formula contributes to the screening toolkit.

The limitations deserve equal billing. The formula works worst in
capacity-constrained corners: its backtest edge lived in small and
mid-sized stocks that cannot absorb much capital without moving the
prices that make them cheap. The annual turnover creates tax drag
in taxable accounts -- Greenblatt's sell-loser-before-a-year rule
mitigates but does not eliminate it. And every input is accounting
data, which means the screen is only as honest as the statements it
reads; a company whose EBIT is an artifact of aggressive
recognition will rank well for exactly the wrong reason, which is
why the adjacent domain on accounting shenanigans exists. None of
these limits invalidates the formula; they define where it belongs
-- as the triage layer of a value process, not the whole process.

## Sources

1. Greenblatt, J. (2005). "The Little Book That Beats the Market."
   John Wiley & Sons. The original presentation of the Magic
   Formula, its mechanics, and the 1988-2004 backtest. [high]

2. Greenblatt, J. (2010). "The Little Book That Still Beats the
   Market." John Wiley & Sons. Sequel updating the record through
   the financial crisis and defending the approach. [high]

3. Magic Formula Investing. Official screen, current buy list, and
   tracked tranche results since 2005.
   https://www.magicformulainvesting.com/ [high]

4. Piotroski, J. (2000). "Value Investing: The Use of Historical
   Financial Statement Information to Separate Winners from
   Losers." Journal of Accounting Research, 38, 1-41.
   https://www.jstor.org/stable/2672906 [high]

5. Damodaran, A. (2012). "Investment Philosophies: Successful
   Strategies and the Investors Who Made Them Work." 2nd ed. Wiley.
   Systematic treatment of screening strategies and their failure
   modes. Course materials: https://pages.stern.nyu.edu/~adamodar/
   [high]

6. Investopedia. "Magic Formula Investing: Definition, How It
   Works." Practical explanation of the formula's mechanics and
   adoption history. [medium]

7. Wikipedia. "Magic formula investing."
   https://en.wikipedia.org/wiki/Magic_formula_investing
   Documented account of the formula's post-publication
   performance and criticism. [medium]

## See Also

- `library/valuation-screening/graham-number-quantitative-value-screens.md` -- the Graham-style defensive screens the Magic Formula descends from, including net-nets and the seven defensive criteria.
- `library/valuation-screening/valuation-multiples-pe-ev-ebitda-pb-analysis.md` -- the multiple-based valuation toolkit the formula's two ratios belong to.
- `library/value-investing/margin-of-safety.md` -- the philosophical principle the composite rank operationalizes.
- `library/value-investing/economic-moats.md` -- what the return-on-capital signal is a proxy for.
- `library/value-investing/anchor-value-investing.md` -- the philosophy domain the formula serves as a tool.
