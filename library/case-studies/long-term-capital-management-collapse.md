---
name: long-term-capital-management-collapse
id: 20260831T071629Z
tier: library-topic
domain: case-studies
author: Library Runner
tags: [ltcm, hedge-fund, leverage, systemic-risk, model-risk, convergence-arbitrage, russian-default, federal-reserve, moral-hazard, liquidity-crisis]
links: [library/case-studies/2008-financial-crisis.md, library/portfolio-risk-management/tail-risk-hedging.md, library/portfolio-risk-management/value-at-risk-risk-measurement-frameworks.md]
---

# Long-Term Capital Management -- How the Smartest Minds in Finance Nearly Destroyed the Global System

Long-Term Capital Management (LTCM) was a hedge fund founded in 1994 by
former Salomon Brothers bond arbitrage chief John Meriwether and two
Nobel Prize-winning economists, Robert Merton and Myron Scholes. The
fund used mathematical models to exploit tiny price discrepancies in
bond markets, amplifying them into spectacular returns through
leverage exceeding 25-to-1. In August and September 1998, triggered by
Russia's sovereign debt default and a global flight to liquidity,
LTCM lost over $4.6 billion in weeks and required a Federal
Reserve-orchestrated, $3.625 billion bailout by 14 major banks to
prevent a cascading systemic collapse. The case stands as the
definitive lesson in the dangers of excessive leverage, the limits of
mathematical modeling, and the catastrophic cost of intellectual hubris.

## Background

The intellectual roots of Long-Term Capital Management extend to the
academic finance revolution of the 1970s and 1980s, which sought to
transform investing from an art practiced by intuition-guided
practitioners into a science governed by equations. The pivotal
intellectual contribution was the Black-Scholes option pricing model
(1973), developed by Fischer Black, Myron Scholes, and Robert Merton,
which provided a mathematically rigorous framework for valuing
financial derivatives. This work, which earned Scholes and Merton the
1997 Nobel Prize in Economics, established the proposition that
market prices follow identifiable statistical patterns and that
systematic exploitation of those patterns could produce returns
uncorrelated with broader market movements.

John Meriwether had pioneered the practical application of these
ideas at Salomon Brothers, where he built the bond arbitrage group in
the late 1970s and 1980s. Meriwether's team -- including Lawrence
Hilibrand, Victor Haghani, and several future LTCM partners --
identified small pricing inefficiencies in government bond markets
and used borrowed money to amplify the returns. The Salomon
arbitrage group became one of the most profitable operations on Wall
Street, generating hundreds of millions in profits annually. The
group's success attracted institutional capital and elite academic
talent, blurring the line between theory and practice.

Meriwether left Salomon Brothers in 1991 after a Treasury bond
auction scandal involving a trader he supervised. The scandal cost
Salomon a $290 million settlement and the resignation of its
chairman, though Meriwether himself was not personally implicated in
wrongdoing. Rather than returning to Salomon, where he believed he
had been denied the top position he deserved, Meriwether resolved to
build a new institution from scratch. He recruited the best of his
former Salomon team and added two of the most celebrated academics in
finance: Myron Scholes of Stanford and Robert Merton of Harvard
Business School. David Mullins, a former vice-chairman of the Federal
Reserve Board, also joined as a partner, giving the fund
unprecedented credibility with both the academic and regulatory
establishments.

LTCM launched in 1994 with approximately $1.1 billion in capital --
at the time, the largest hedge fund startup in history. The minimum
investment was $10 million, and investors were locked in for three
years. The fee structure was aggressive: 2 percent management fee
plus 25 percent of profits, well above industry norms. Despite these
terms, 80 founding investors committed capital, drawn by the
stellar reputations of the principals. Early investors included
Central Banks of Italy, the Netherlands, and Thailand, major
university endowments, and prominent financial institutions.

The fund was spectacularly successful in its first three years.
LTCM returned 28 percent in 1994 (20 percent after fees), 59 percent
in 1995 (43 percent after fees), and 57 percent in 1996 (41 percent
after fees), far outperforming every benchmark. By the end of 1997,
LTCM had approximately $7 billion in equity and controlled over $125
billion in assets. The fund returned $2.7 billion to investors at
the end of 1997 because, as Meriwether stated, investment
opportunities were not large and attractive enough to deploy the
capital productively.

This return of capital marked a critical turning point. Rather than
reducing risk in proportion to the smaller capital base, LTCM
increased its leverage to maintain returns. The competitive landscape
had also shifted: by 1998, many Wall Street banks and competing hedge
funds had adopted similar convergence strategies, compressing the
spreads LTCM had historically exploited. To maintain the same dollar
returns on a smaller equity base, LTCM reached further -- taking on
larger positions in riskier, less liquid markets, including emerging
market debt, equity index volatility, and merger arbitrage. The
fund that had been a disciplined bond arbitrageur was now a
multi-strategy behemoth with exposures spanning dozens of markets
globally, its original risk discipline diluted by the need to deploy
capital wherever models identified any statistical edge.

## Core Concepts

### Convergence Arbitrage

LTCM's central strategy was convergence trading: identifying pairs
of securities that, according to theory and historical data, should
trade at similar prices or yields, and betting that temporary
divergences between them would narrow. The most classic example was
the on-the-run versus off-the-run Treasury trade. When the U.S.
Treasury issues a new 30-year bond, it becomes the "on-the-run"
issue and trades at a slight premium (lower yield) because it is more
liquid and sought after by institutional investors. The previous
issue becomes "off-the-run" and trades at a slight discount (higher
yield) because it is less liquid. As time passes and a new bond is
issued, the current on-the-run bond becomes off-the-run, and the
spread between the two narrows. LTCM would buy the cheaper off-the-run
bond and short the more expensive on-the-run bond, profiting as the
spread converged.

The critical feature of this trade is that the profit per trade is
tiny -- often just a few basis points (0.02 to 0.10 percent). To
convert these microscopic spreads into the 20 to 40 percent annual
returns investors expected, LTCM applied leverage of 25-to-1 or
higher. At 25-to-1 leverage, a 0.04 percent spread becomes a 1
percent return on equity. With hundreds of such trades running
simultaneously, the strategy appeared to produce consistent, high
returns with low risk -- as long as the spreads converged and
leverage remained available.

### The Leverage Mechanism

LTCM's leverage operated through several channels. The primary
mechanism was repurchase agreements (repo): LTCM would buy a
security, then lend it to a dealer bank in exchange for cash, which
it used to buy more securities, posting them as collateral for more
borrowing. Because LTCM traded primarily in top-grade government
securities, counterparties permitted 100 percent financing -- LTCM
could borrow the full value of the collateral. This created a
self-reinforcing leverage loop that, in theory, could compound to
infinity.

LTCM also used over-the-counter (OTC) derivatives -- interest rate
swaps, swaptions, and equity options -- to gain exposure without
posting initial margin. Because of the fund's prestige and the
competitive pressure among dealers for LTCM's business, counterparties
offered favorable terms: low or zero initial margins, high thresholds
before collateral calls, and minimal independent amounts. These
terms were set by sales relationships, not by risk departments,
meaning the collateral cushion that should have protected
counterparties was thinner than prudent risk management demanded.

By 1998, LTCM's balance sheet leverage reached approximately 25-to-1
to 30-to-1, with approximately $125 billion in assets against roughly
$4.7 billion in equity. But the true economic exposure was far
larger: the fund held over $1.25 trillion in notional derivative
positions, representing roughly 5 percent of the entire global
derivatives market at the time. At the peak of the crisis in
September 1998, as equity collapsed to $400 million while positions
remained near $100 billion, effective leverage reached approximately
250-to-1.

### Trade Types and Market Expansion

LTCM pursued four main categories of convergence trades. The first was
convergence among U.S., Japanese, and European sovereign bonds: the
fund identified yield spreads between government bonds of similar
maturity across different developed markets that had historically
narrowed and bet that they would converge again. The second was
convergence among European sovereign bonds in anticipation of monetary
union: as countries prepared to adopt the euro, their bond yields
were expected to converge toward German benchmarks, and LTCM
positioned to profit from the narrowing. The third was the on-the-run
versus off-the-run Treasury trade described above. The fourth was
convergence in swap spreads -- the difference between the fixed rate
on interest rate swaps and the yield on Treasury bonds of matching
maturity -- which LTCM bet would revert to historical norms.

As spreads in core government bond trades compressed through
competition, LTCM expanded into riskier and less liquid markets. The
fund took positions in emerging market debt, mortgage-backed
securities, and corporate bonds. It entered merger arbitrage --
betting that announced acquisitions would complete -- and equity
volatility trades, selling options on stock indices and betting that
implied volatility would revert to historical levels. Each expansion
moved the fund further from its core competence in government bond
arbitrage and deeper into markets where its models had less historical
data and its positions were harder to liquidate. The fund that began
as a disciplined bond arbitrageur became a multi-strategy behemoth
whose risk profile no single model or manager could fully capture.

### Model Risk and the Normality Assumption

The mathematical models LTCM relied on were built on historical data
and assumed that future market behavior would resemble the past. The
key assumptions were: price changes follow a normal (Gaussian)
distribution, correlations between different trade types remain
stable, and liquidity is available when needed. Each of these
assumptions was reasonable during the calm period over which the
models were calibrated -- but each failed catastrophically under the
stress conditions of August 1998.

The normality assumption led LTCM's models to assign extraordinarily
low probabilities to large adverse moves. According to the models,
the losses LTCM experienced in August 1998 were so unlikely that they
should not have occurred even once over the entire life of the
universe. This is the classic "fat tails" problem: financial market
returns exhibit much more frequent extreme events than the normal
distribution predicts. LTCM's models systematically underestimated
the probability and magnitude of tail events -- precisely the events
that destroy leveraged portfolios.

The correlation assumption was equally fatal. LTCM held dozens of
different trades across multiple asset classes and geographies,
believing that diversification across 60 to 70 independent positions
reduced portfolio risk. The models estimated correlations of 0.30 or
lower between trade types. But during a systemic crisis, correlations
across all risk assets converge toward 1.0 -- everything falls
simultaneously. In August 1998, what appeared to be 70 independent
bets became one giant bet on global liquidity and risk appetite
remaining stable. The diversification that made the model appear safe
evaporated in the exact moment it was needed.

### The Flight to Liquidity

The specific mechanism that destroyed LTCM was not the Russian
default itself -- LTCM had limited direct exposure to Russian
government bonds. Rather, it was the behavioral response of global
investors to the default. When Russia devalued the ruble and declared
a moratorium on debt payments on August 17, 1998, investors
worldwide panicked. They sold every asset that carried any risk and
flocked to the safest, most liquid securities -- primarily U.S.
Treasury bonds. This "flight to quality" widened every spread LTCM
had bet would narrow. The gap between on-the-run and off-the-run
Treasuries widened. Corporate bond spreads blew out. Emerging market
debt collapsed. Equity volatility surged. Every convergence trade
in LTCM's portfolio moved against it simultaneously.

This was a liquidity phenomenon, not a credit phenomenon. The
securities LTCM held were not necessarily impaired in fundamental
value -- many of the convergence bets, held to maturity with
unlimited time and capital, might eventually have converged. But
LTCM had neither unlimited time nor unlimited capital. Leverage
removed the fund's ability to survive being temporarily wrong. A
firm with a correct long-run thesis and insufficient capital to
weather a short-run shock can be forced to liquidate at the worst
possible moment -- which is a leverage and liquidity failure, not
necessarily a forecasting one.

### Counterparty Interconnectedness and Systemic Risk

LTCM's failure threatened the global financial system not because of
its own $4.7 billion in equity but because of its interconnectedness
with nearly every major financial institution. The fund had 75
counterparties for repo financing and over 50 OTC derivatives
counterparties. Its positions touched every major bond, currency, and
equity market. No single counterparty could see the full picture of
LTCM's exposure -- each knew only its own slice. Collectively,
LTCM's counterparties had extended enormous financing and derivatives
exposure without understanding the aggregate risk.

The systemic threat was a fire sale. If LTCM defaulted and was forced
to liquidate its positions rapidly, the flood of securities into
already distressed markets would drive prices down further, causing
losses for every other institution holding similar positions. Those
institutions would face their own margin calls and be forced to sell,
creating a cascading downward spiral. Federal Reserve Chairman Alan
Greenspan testified that "the probability of system collapse was
sufficiently large to make us very uncomfortable about doing
nothing." The core systemic risk was not that LTCM was too big to
fail -- it was that LTCM was too interconnected to fail.

## Evidence

### The Timeline of Collapse

The destruction of LTCM unfolded over months but accelerated with
terrifying speed in August and September 1998. In May 1998, the fund
lost 6.42 percent; in June, it lost 10.14 percent -- its largest
one-month loss to date. By the end of July, LTCM's equity had
declined from $4.7 billion to approximately $4 billion. The fund
remained solvent but under stress.

August 1998 was catastrophic. On August 17, Russia devalued the ruble
and declared a moratorium on 281 billion rubles ($13.5 billion) of
Treasury debt. The global flight to quality that followed hit every
LTCM position simultaneously. The fund lost 44 percent of its
remaining capital in August alone -- approximately $1.85 billion.
LTCM's equity dropped from approximately $4 billion to $2.3 billion
by September 1.

The bleeding accelerated. In the first three weeks of September,
LTCM's equity tumbled from $2.3 billion to just $400 million by
September 25. The fund was losing hundreds of millions per day. On
September 2, LTCM sent a letter to investors disclosing its August
losses, making its distress public knowledge. Wall Street firms that
had been counterparties to LTCM began to realize the fund's positions
were larger and riskier than they had understood. Some dealers began
trading against LTCM -- front-running the positions they knew the fund
would be forced to sell, accelerating the losses.

### The Federal Reserve Intervention

On September 23, 1998, the Federal Reserve Bank of New York convened
a meeting of 14 major financial institutions at its offices at 33
Liberty Street. In attendance were representatives of Bankers Trust,
Bear Stearns, Chase Manhattan, Goldman Sachs, J.P. Morgan, Lehman
Brothers, Merrill Lynch, Morgan Stanley Dean Witter, and Salomon
Smith Barney, among others. The Fed did not contribute its own funds
and made no promises -- it facilitated a private-sector agreement.

Before the consortium deal was reached, Warren Buffett, Goldman
Sachs, and AIG made an independent offer to buy out LTCM's partners
for $250 million and inject $3.75 billion. The offer was stunningly
low -- at the start of the year, the firm had been worth $4.7
billion. Buffett gave Meriwether less than one hour to accept. The
deadline passed before a deal could be structured, and the offer
expired.

The consortium ultimately invested $3.625 billion, receiving 90
percent of LTCM's equity. The partners retained a 10 percent stake
worth approximately $400 million, but this was entirely consumed by
their debts. The partners had invested $1.9 billion of their own
money in the fund -- all of it was wiped out. The creditors took
control and wound down the portfolio over the following months in an
orderly fashion, eventually realizing a small profit on the rescue.

### The Greenspan Testimony

Federal Reserve Chairman Alan Greenspan's testimony before the
Committee on Banking and Financial Services on October 1, 1998
provides the most authoritative primary-source account of the Fed's
rationale. Greenspan stated that the Federal Reserve Bank of New York
acted because "the probability of system collapse was sufficiently
large to make us very uncomfortable about doing nothing." He
emphasized that the intervention was not a government bailout -- no
Federal Reserve funds were provided or even suggested. The Fed's role
was to facilitate a private-sector resolution and prevent a fire-sale
liquidation that could have impaired the broader economy.

Greenspan identified the core policy questions the episode raised:
how much dependence should be placed on financial modeling that can
get too far ahead of human judgment; whether counterparties
adequately stress-tested their exposure; what lessons bank regulators
should draw; whether direct regulation of hedge funds was feasible or
desirable; and how to weigh moral hazard against the need to prevent
fire sales. He acknowledged that "some moral hazard, however slight,
may have been created" but argued that the risks of inaction
outweighed this cost. This testimony became the foundational document
for post-LTCM regulatory debates.

### The Loss Composition

The total losses were approximately $4.6 billion. The largest losses
came from just two trade categories: interest rate swaps and short
positions in long-term equity options. According to analysis
referenced by the Richmond Federal Reserve, approximately $3 billion
of the $4.4 billion in losses came from these two trade types alone.
This finding undermines the diversification narrative: LTCM held
thousands of positions across dozens of markets, but they mapped to
a small set of underlying risk factors. The apparent diversification
was illusory because the positions shared hidden common exposures --
primarily to liquidity and volatility.

The loss distribution also revealed the asymmetry of leverage. In the
calm years, LTCM's convergence trades produced small, steady gains
that leverage amplified into spectacular returns. In the crisis, the
same leverage amplified small adverse moves into capital-destroying
losses. The strategy was not asymmetric in its design -- convergence
trades have defined upside (the spread narrows to zero) but undefined
downside (the spread can widen indefinitely before converging).
Leverage converted this asymmetry into a survival constraint: the
fund could not hold on long enough for convergence to occur.

### Academic Analysis

The American Economic Association published a comprehensive analysis
in the Journal of Economic Perspectives (1999) titled "Hedge Funds
and the Collapse of Long-Term Capital Management." This academic
treatment confirmed the key findings: the models underestimated
correlation under stress, leverage magnified losses beyond the fund's
capacity to survive, and counterparty risk management failed because
no single institution could see the aggregate exposure. The analysis
also noted that LTCM's strategies were compared to "picking up
nickels in front of a bulldozer" -- a likely small gain balanced
against a small chance of a catastrophic loss.

## Implications

### Leverage as an Existential Risk

The most enduring lesson of LTCM is that leverage is not merely a
multiplier of returns but an existential constraint on survival.
Unleveraged investors can hold a position through a temporary adverse
move and wait for fundamentals to reassert themselves. Leveraged
investors face margin calls, collateral demands, and forced
liquidation that can destroy them before the thesis proves correct.
LTCM's convergence trades may well have converged eventually -- but
the fund could not survive the interim. The lesson for every
investor is that leverage converts temporary price dislocation into
permanent capital destruction. The investor who uses margin,
leveraged instruments, or borrowed capital must understand that the
survival constraint -- not the expected return -- is the binding
limit. At 25-to-1 leverage, a 4 percent adverse move in the portfolio
eliminates the entire equity cushion. The Russian default and flight
to quality produced far larger moves.

This lesson applies directly to individual investors. Any use of
margin, leveraged exchange-traded funds, or mortgage-financed
investments carries the same structural risk that destroyed LTCM. The
multiplier effect works identically on losses as on gains, and the
margin call that forces liquidation at the worst moment does not
distinguish between a portfolio that will eventually recover and one
that will not. The practical implication is that leverage should be
sized not to the expected return but to the worst survivable drawdown
-- the scenario in which everything goes wrong simultaneously.

### The Limits of Quantitative Models

LTCM's failure exposed a fundamental limitation of quantitative
finance: models built on historical data systematically underestimate
tail risk because the data on which they are calibrated contains, by
definition, few or no examples of the extreme events that matter
most. The models assigned probabilities so low to the August 1998
scenario that it was deemed statistically impossible -- yet it
happened. This is not a flaw that can be fixed with more data or
better calibration. It is an epistemic limitation: the relevant
question is not "what has happened" but "what could happen that has
not happened yet."

The implications extend beyond hedge funds. Every risk model --
Value at Risk, credit scoring, portfolio optimization -- embeds
assumptions about correlation, volatility, and liquidity that are
calibrated on past data. These models are useful in normal conditions
but their value collapses precisely in the crisis conditions where
risk management matters most. The Basel II framework, finalized in
2004, incorporated model validation requirements directly traceable
to the LTCM episode. But the deeper lesson is that models must carry
explicit uncertainty disclosures and must never be treated as
substitutes for human judgment. The more sophisticated the model, the
more dangerous its blind spots, because sophistication breeds
confidence and confidence breeds leverage.

### Diversification and Correlation Breakdown

LTCM appeared to hold a diversified portfolio: 60 to 70 different
trade types across bonds, equities, currencies, and geographies. The
models estimated low correlations between these positions, implying
that the portfolio risk was far lower than the sum of individual
trade risks. In the crisis, correlations across all positions
converged toward 1.0 -- diversification failed exactly when it was
needed. The lesson is that diversification measured during calm
periods systematically overstates protection during crises, because
the correlations that matter are crisis correlations, not average
correlations.

This finding has implications for every portfolio construction
framework. Modern Portfolio Theory's optimization, which selects
weights based on historical covariance matrices, produces
portfolios that look well-diversified in backtests but can collapse
in live crises. The practical response is stress testing: rather
than relying on average correlations, investors must test what
happens to the portfolio under scenarios where all correlations
spike to 1.0, liquidity dries up, and every position moves against
them simultaneously. The portfolio that survives this test is
diversified in the only sense that matters -- under stress.

### Moral Hazard and the Too-Interconnected-to-Fail Problem

The LTCM bailout established a precedent that would return at vastly
larger scale a decade later. By organizing a private-sector rescue
to prevent systemic contagion, the Federal Reserve created -- or
reinforced -- the expectation that the government would intervene to
prevent the disorderly failure of a systemically interconnected
institution. This moral hazard did not cause the 2008 crisis, but it
shaped the environment in which the 2008 crisis developed. Financial
institutions that believed they would be rescued in extremis had
reduced incentives to manage their own systemic risk.

The parallels between LTCM and the 2008 crisis are exact: both
involved leveraged institutions trading instruments whose risk models
underestimated correlation; both required government-orchestrated
rescues to prevent cascading failures; both revealed that
interconnectedness, not size, is the true measure of systemic
importance. The difference is scale: LTCM's $3.6 billion rescue was a
rounding error compared to the $700 billion Troubled Asset Relief
Program and the trillions in Federal Reserve emergency lending that
followed the 2008 collapse. The lesson for regulators is that
addressing interconnectedness -- through transparency, position
limits, and resolution mechanisms -- is more important than
addressing size alone.

### The Buffett-Munger Perspective

Warren Buffett's attempted acquisition of LTCM for $250 million --
and his refusal to extend the one-hour deadline -- exemplifies the
value investing philosophy's approach to distress. Buffett understood
that the positions held intrinsic value but that the price had to
reflect the urgency of the seller. His offer was low because he was
providing liquidity in a market where liquidity commanded an enormous
premium. The lesson, consistent with the margin-of-safety principle,
is that the investor who can survive without forced selling holds an
option that the leveraged investor does not: the option to wait.
Patience is not a virtue in leveraged investing -- it is a luxury that
leverage eliminates. The unleveraged investor can afford to be wrong
for a long time; the leveraged investor cannot afford to be wrong
for a day.

## Sources

1. Greenspan, A. (1998). "Private-sector refinancing of the large
   hedge fund, Long-Term Capital Management." Testimony before the
   Committee on Banking and Financial Services, U.S. House of
   Representatives, October 1, 1998. The authoritative primary-source
   account of the Federal Reserve's rationale for intervention.
   https://www.federalreserve.gov/boarddocs/testimony/1998/19981001.htm [high]

2. Federal Reserve History. "Near Failure of Long-Term Capital
   Management." Federal Reserve Bank of New York historical essay
   documenting the September 1998 rescue, the $3.6 billion private-
   sector capital infusion, and the Fed's facilitation role.
   https://www.federalreservehistory.org/essays/ltcm-near-failure [high]

3. Lowenstein, R. (2000). "When Genius Failed: The Rise and Fall of
   Long-Term Capital Management." Random House. The definitive book-
   length narrative account of LTCM's founding, strategy, collapse,
   and rescue, written by a veteran Wall Street Journal
   correspondent with access to participants and records.
   https://www.amazon.com/When-Genius-Failed-Long-Term-Management/dp/0375758259 [high]

4. Edwards, F. (1999). "Hedge Funds and the Collapse of Long-Term
   Capital Management." Journal of Economic Perspectives, 13(2),
   189-210. Academic analysis published by the American Economic
   Association examining the systemic implications of LTCM's failure
   and the regulatory questions it raised.
   https://www.aeaweb.org/articles?id=10.1257/jep.13.2.189 [high]

5. Richmond Federal Reserve (2009). "Too Interconnected to Fail? The
   Rescue of Long-Term Capital Management." Economic Quarterly, Summer
   2009. Analysis of the systemic risk dimensions of the LTCM rescue
   and the policy lessons for financial regulators.
   https://www.richmondfed.org/-/media/RichmondFedOrg/publications/research/econ_focus/2009/summer/pdf/economic_history.pdf [high]

6. Shirreff, D. (1999). "Too close to the hedge: the case of long
   term capital management." Managerial Finance, 25(1). Academic
   analysis of LTCM's hedge fund analytics, leverage structure, and
   the illiquidity and inadequate stress testing that led to its
   near-collapse.
   https://www.sciencedirect.com/science/article/abs/pii/S0263237399000079 [high]

7. Wikipedia contributors. "Long-Term Capital Management." Wikipedia.
   Comprehensive reference article with citations to primary sources,
   timeline details, and the full list of consortium participants.
   https://en.wikipedia.org/wiki/Long-Term_Capital_Management [medium]

## See Also

- `library/case-studies/2008-financial-crisis.md` -- the 2008
  financial crisis repeated LTCM's core pattern -- leveraged
  institutions, model failure, correlation breakdown, and
  government-orchestrated rescue -- at vastly larger scale.
- `library/portfolio-risk-management/tail-risk-hedging.md` -- the
  risk management framework that LTCM's failure made necessary:
  protecting against extreme events that models deem impossible.
- `library/portfolio-risk-management/value-at-risk-risk-measurement-frameworks.md`
  -- the quantitative risk measurement framework whose assumptions
  about normality and stable correlation LTCM's failure exposed.
- `library/portfolio-risk-management/diversification-mathematics.md`
  -- the mathematical foundations of diversification whose limits
  LTCM's simultaneous correlation breakdown revealed.
- `library/value-investing/margin-of-safety.md` -- the principle that
  protects the unleveraged investor from the temporary dislocations
  that destroyed the leveraged LTCM.
- `library/case-studies/anchor-case-studies.md` -- the domain anchor
  defining the case-study framework and scope boundaries.