---
name: graham-number-quantitative-value-screens
id: 20260726T121602Z
tier: library-topic
domain: valuation-screening
author: Researcher-1
tags: [graham-number, quantitative-screening, value-investing, net-net, defensive-investor, benjamin-graham, margin-of-safety]
links: [library/valuation-screening/discounted-cash-flow-dcf-methodology.md, library/valuation-screening/valuation-multiples-pe-ev-ebitda-pb-analysis.md, library/value-investing/anchor-value-investing.md]
reviewed: 2026-10-01
---

# The Graham Number and Quantitative Value Screens -- Cheapness Filters Organize Research but Do Not Establish Intrinsic Value

The Graham Number is a later algebraic shorthand for Benjamin Graham's 1973 rule that the product of a defensive stock's price-to-earnings and price-to-book ratios should not exceed 22.5; it is not a standalone appraisal and does not require both nominal ratio ceilings to pass separately [1][2]. Graham-style net-current-asset screens and later value-factor screens can impose price discipline and narrow a research universe, but their historical returns depend on definitions, samples, accounting data, test construction, and implementation [3][4][5][6][7][8]. The author's assessment is that a screen identifies a proposition to investigate; it does not establish asset realizability, durable earning power, control over value, or an adequate expected return for a particular security.

## Background

Benjamin Graham's quantitative rules were parts of distinct investment programs, not one universal formula. In Chapter 14 of the 1973 edition of *The Intelligent Investor*, his defensive-investor program required adequate enterprise size, financial strength, ten years of positive earnings, twenty years of uninterrupted dividends, at least one-third growth in per-share earnings over ten years measured with three-year averages, a price no greater than fifteen times three-year average earnings, and a price ordinarily no greater than 1.5 times reported book value [1]. Graham then qualified the last two price tests: a lower earnings multiple could justify a higher asset multiple, provided that the product of the P/E multiple and price-to-book ratio did not exceed 22.5 [1]. The familiar square-root expression now called the Graham Number follows from that product rule, but the primary text presents the rule as one element of a seven-part defensive selection system [1][2].

The historical details matter. Graham called the size thresholds arbitrary, distinguished industrial companies from public utilities in his balance-sheet tests, and used nominal thresholds fitted to the companies, accounting conventions, security prices, and interest-rate environment discussed in that edition [1]. He did not say that every company below the 22.5 product boundary was worth buying. Four of the seven criteria addressed operating history and financial condition before the two price criteria were applied. Treating the square-root result as an estimate of intrinsic value removes the quality tests and changes a multidimensional selection rule into a valuation claim that the source does not make [1].

Graham's net-current-asset method served a different part of the program. He described acquiring a diversified group below net current assets after deducting all prior claims and assigning zero value to fixed and other assets [1]. The book reports satisfactory group experience for more than thirty years, approximately 1923-1957, but explicitly identifies 1930-1932 as a period of real trial and gives only a qualified endorsement for conditions at the start of 1971 [1]. The relevant quantity is not ordinary working capital, current assets minus current liabilities. Graham's usage was current assets minus total liabilities and prior claims; the method was deliberately severe because it gave no credit to fixed assets or future earnings [1]. Mohanty and Oxman's later empirical study defines its entry rule as a market price below two-thirds of net current asset value rather than merely below NCAV [8].

The group character of Graham's process survived his revisions. In a 1976 *Financial Analysts Journal* interview, he questioned whether elaborate security analysis usually justified its cost in a heavily researched market and favored a simplified portfolio approach using one or two objective price criteria, with results judged for the group rather than predicted security by security [3]. He still required impersonal reasoning, a margin of safety, a selling policy, and minimum allocations to both stocks and bond equivalents [3]. The interview therefore supports mechanical discipline, but it does not support an automatic single-stock buy signal. A rule can reduce discretion at the selection stage while leaving accounting verification, implementation, and realization risk unresolved.

Academic research later tested related, but not identical, propositions. Fama and French examined U.S. stocks over July 1963-December 1990 and reported a strong positive relation between book-to-market equity and average returns; they also treated book-to-market as a possible proxy for multidimensional risk or relative distress rather than proving that all of the spread was mispricing [4]. Lakonishok, Shleifer, and Vishny formed value and glamour portfolios using book-to-market, cash-flow-to-price, earnings-to-price, and past sales growth, and argued that investor extrapolation explained much of the value advantage in their sample [5]. These papers examine portfolio sorts. They do not test the Graham Number as a complete seven-criterion rule, and they do not convert a historical cross-sectional association into the intrinsic value of an individual company.

Research on NCAV and financial strength makes the same distinction. Oppenheimer found that diversified NCAV portfolios outperformed benchmarks over 1970-1983, while individual thirty-month portfolio outcomes were widely variable [6]. Piotroski began with the highest book-to-market quintile and used nine accounting signals to separate financially stronger from weaker firms; his result was a quality overlay inside a preselected value universe, not evidence that cheapness alone resolves business deterioration [7]. Mohanty and Oxman's 1969-2019 U.S. study found significant long-run NCAV returns after several factor and liquidity controls, but also found declining profitability in 2004-2019 [8]. The current evidence is therefore conditional: some transparent cheapness rules have worked in specified historical samples, but strength, timing, and implementability vary.

The accounting base has also changed. CFA Institute's 2025 investor report documents that internally generated intangibles are often absent from balance sheets even when investors regard them as economically important; more than 70 percent of surveyed respondents agreed that unrecognized intangibles materially explain differences between book and market equity for many listed companies [10]. That does not make book value useless. It means that a price-to-book threshold compares price with an accounting residual whose economic content differs across industries, firms, acquisition histories, and reporting regimes. A mechanical rule remains useful only when the analyst understands what its numerator and denominator represent.

## Core Concepts

### The Graham Number implements a product rule

Let `P` be price per common share, `E` be the relevant earnings per share, and `B` be the relevant book value per common share. When `E` and `B` are positive, the product of the two observed multiples is:

`(P / E) x (P / B) = P^2 / (E x B)`

Setting that product equal to Graham's 22.5 boundary and solving for price gives:

`Graham Number = sqrt(22.5 x E x B)`

A price at or below that number satisfies the product rule, subject to the validity and consistency of `E` and `B` [1][2]. The arithmetic is an algebraic transformation, not an independent valuation model. It contains no forecast of future cash flow, no discount rate, no explicit cost of capital, no competitive-advantage period, no adjustment for nonoperating assets or senior claims, and no estimate of liquidation proceeds.

The product rule must not be confused with simultaneous enforcement of separate P/E and P/B ceilings. Graham expressly wrote that an earnings multiple below fifteen could justify a correspondingly higher asset multiple and gave nine times earnings and 2.5 times asset value as an admissible example; `9 x 2.5 = 22.5` [1]. Such a company passes the product boundary while exceeding the nominal 1.5 price-to-book guideline. Conversely, a user who requires both P/E at or below fifteen and P/B at or below 1.5 is applying a stricter intersection rule. Both rules can be stated, but they answer different questions and must not be represented as equivalent.

The inputs also need an as-of definition. Graham's defensive criterion used average earnings for the past three years, not automatically the latest trailing twelve months, a single forecast year, adjusted EBITDA, or management's preferred earnings measure [1]. Book value was the reported common-equity amount relevant to the shares being priced. A reproducible modern implementation must state whether earnings are basic or diluted, continuing or total, reported or normalized; whether book value excludes preferred equity or other senior claims; which share count is used; how stock splits and restatements are handled; and how long after a fiscal period the data become investable. Changing any of these choices changes the screen.

The author's mathematical interpretation is that positive accounting inputs are an economic gate. If either earnings per share or book value per share is zero or negative, the ordinary price multiples and their product no longer carry the intended defensive meaning. When one input is negative, the square root has no real positive value. When both inputs are negative, their product is positive and a calculator can return a number, but that result is economically nonsensical: losses and a common-equity deficit have not become evidence of value by multiplication. The Graham Number should then be marked not meaningful and replaced with a method suited to the company's claim structure and economics.

### Earnings and book value are measurements, not facts of nature

The author's accounting synthesis is that reported earnings can be affected by cyclicality, asset sales, impairments, restructuring, tax items, acquisition accounting, stock compensation, pension assumptions, credit provisions, and changes in share count. A three-year average can dampen one-year noise but does not necessarily span a full business cycle or remove a structural decline. The screen should preserve both reported and normalized versions rather than overwrite the filing number: the reported version makes the rule reproducible, while a separately documented normalization shows the analyst's judgment. A large difference between the two is itself a research signal.

Book value likewise requires claim and accounting discipline. Common book equity is an accounting residual, not an appraisal of recoverable assets, and it can include goodwill created in acquisitions while excluding internally generated brands, software, research capability, customer relationships, and organizational capital [10]. CFA Institute reports both the asymmetric treatment of acquired and internally generated intangibles and the widening gap between book and market equity for many large issuers [10]. The author's interpretation is that a low P/B ratio may indicate asset backing, expected weak returns, unrecognized liabilities, poor capital allocation, or merely a business whose recorded equity is economically important. A high P/B ratio can reflect overpricing, but it can also reflect valuable earning assets that accounting does not recognize [10].

The author's assessment is that the Graham Number can compound input errors because it multiplies two accounting quantities. Peak-cycle earnings can raise `E` while an overstated or obsolete asset base raises `B`, producing an attractive number from two weak anchors. Buybacks can reduce book equity and shares in ways that alter both EPS and BVPS, while acquisitions can add goodwill and change the comparability of book value across firms [10]. A pass should therefore trigger a reconciliation of earnings, assets, liabilities, and share claims; it should never terminate that work.

### NCAV is a balance-sheet screen, not cash in hand

At the aggregate company level, a basic Graham-style calculation is [1]:

`NCAV = current assets - total liabilities - senior equity claims`

The comparison is between market capitalization of the common equity and aggregate NCAV, or equivalently between per-share values calculated with a consistent diluted share count. Fixed assets and future earnings receive zero credit in the screen [1]. The stricter two-thirds rule requires market capitalization below two-thirds of NCAV [8]. Because the test uses current assets rather than all book assets and subtracts total claims rather than only current liabilities, it is materially different from a current ratio, ordinary working capital, or price-to-book screen.

NCAV is still not liquidation value: Graham's rule is an accounting screen that assigns zero to fixed and other assets, not a sale-proceeds appraisal [1]. The author's asset-and-claim checklist asks whether cash is restricted; receivables are doubtful or concentrated; inventory is obsolete, pledged, or costly to sell; tax assets are cash-realizable; and contingencies, guarantees, lease termination costs, taxes, severance, and wind-down expenses are complete. It also asks whether operations can consume the apparent current-asset surplus while a minority shareholder waits. The author's interpretation is that the two-thirds purchase threshold and diversification create room for error at the group level, but neither proves realizability for a particular issuer [1][8]. A complete investigation requires the notes, claim priority, cash-burn trajectory, control rights, and a plausible path by which value reaches common shareholders.

The author's terminology rule is not to treat "net-net," "NCAV stock," "below working capital," and "below liquidation value" as automatic synonyms. A screen should publish the exact formula, treatment of preferred stock and lease liabilities, source date, market-cap definition, and any asset haircuts. If receivables and inventory are haircut explicitly, the result is an adjusted liquidation scenario rather than the unadjusted NCAV rule. Both can be useful, but combining their names hides which assumptions produced the candidate.

### Broad value screens rank relative cheapness

The author's claim-matching synthesis is that low P/E, high earnings-to-price, low P/B, high book-to-market, low price-to-cash-flow, and low enterprise-value multiples are related but noninterchangeable signals [4][5]. Equity multiples compare common-share price with common-share quantities, while enterprise multiples compare operating enterprise value with pre-financing operating quantities. Earnings, cash flow, and book value respond differently to leverage, capital intensity, accounting choices, cyclicality, and negative denominators [4][5][10]. A multi-metric screen is useful only when each metric is matched to the claim it prices and the analyst explains why the metrics provide independent information rather than counting the same accounting exposure several times.

Absolute rules and relative ranks also differ. Graham's defensive product boundary is an absolute cutoff. Fama and French's evidence came from portfolios sorted by book-to-market within a historical universe [4]. Lakonishok, Shleifer, and Vishny used deciles and combinations of past growth with valuation ratios [5]. Piotroski applied an accounting-strength score only after selecting high book-to-market firms [7]. A backtest of a relative top decile does not validate an absolute P/E or P/B threshold, and evidence for a U.S. book-to-market portfolio does not validate every stock selected by a Graham Number screen.

### Quality overlays test whether cheapness accompanies deterioration

Piotroski's F_SCORE combined nine binary signals covering profitability, cash generation, accrual quality, leverage, liquidity, external equity issuance, gross-margin change, and asset-turnover change [7]. In the original study, scores of eight or nine defined the high-score group and scores of zero or one defined the low-score group within the highest book-to-market quintile [7]. The design illustrates a general principle: a value screen can identify low expectations, while a separate financial-strength test asks whether recent accounting evidence is improving or deteriorating.

A quality overlay is not a guarantee and should not be copied without definitions. Piotroski's sample covered 1976-1996, used point-in-time lags intended to make annual information available, and assigned a zero delisting return whenever a firm delisted [7]. Later users must decide how to handle revised databases, financial companies, negative denominators, mergers, restatements, and delistings. The author's synthesis is that the value of an overlay lies in making a second hypothesis explicit, not in adding enough factors to fit historical noise.

### Backtest construction determines what a screen result means

A testable screening study specifies the investable universe, security types, minimum price and liquidity, accounting lag, rebalance frequency, holding period, weighting, treatment of mergers and delistings, transaction costs, and capacity. Oppenheimer's conclusions concern portfolios, not isolated securities [6]. Fama and French's headline book-to-market figures came from equal-weighted one-dimensional portfolios [4]. Mohanty and Oxman report a value-weighted NCAV portfolio and separate controls [8]. These research choices determine which screening proposition is being measured and how far its result can be generalized.

Point-in-time discipline is essential. Using a later restatement, a database field unavailable at the formation date, or a survivorship-cleaned list gives the historical screen information that a real investor did not possess. Shumway documents that missing negative delisting returns can bias CRSP-based results upward [11]. Piotroski delayed return measurement until the fifth month after fiscal year-end to improve information availability, but assigned a zero delisting return whenever a firm delisted [7][11]. A trustworthy screening test retains the formation-date data and records every exclusion.

Implementation is another research input. Li, Chow, Pickard, and Garg show that factor strategies with similar labels can have materially different market-impact costs because turnover, concentration, weighting, portfolio volume, and assets under management differ [12]. A deep-value screen concentrated in small or neglected companies can look attractive before spreads and market impact while being difficult to replicate at scale. A gross backtest is therefore not evidence of an implementable return until the cost and feasibility of obtaining and later exiting its positions have been tested.

## Evidence and Research Foundation

### Fama and French: book-to-market was strong in a specific U.S. sample

Fama and French studied NYSE, AMEX, and NASDAQ stocks from July 1963 through December 1990. In their one-dimensional book-to-market sort, the average equal-weighted monthly return rose from 0.30 percent for the lowest book-to-market portfolio to 1.83 percent for the highest, a difference of 1.53 percentage points per month [4]. The spread was larger than the size-portfolio spread reported nearby, and the paper found that size and book-to-market helped explain cross-sectional average returns when market beta alone did not [4]. These are historically important results, but the portfolio construction, equal weighting, sample period, and accounting definition are part of the result.

The paper did not establish one uncontested cause. Fama and French discussed book-to-market as a possible proxy for relative distress and stated that, under rational pricing, the variables must proxy for risk [4]. They also acknowledged the possibility that the result reflected market overreaction. The evidence supports a historical relation between relative price and subsequent return; it does not prove that high book-to-market companies were mispriced, that the relation would remain constant, or that the Graham Number measures intrinsic value.

### Lakonishok, Shleifer, and Vishny: value beat glamour in portfolio tests

Lakonishok, Shleifer, and Vishny used NYSE and AMEX firms over a sample beginning in 1963, with annual portfolio formations from April 1968 through April 1989 for strategies requiring five years of accounting history [5]. Their value and glamour classifications used cash-flow-to-price, earnings-to-price, book-to-market, and past sales growth. For one combined classification, the average postformation-year return was 22.1 percent for the value portfolio and 11.4 percent for the glamour portfolio, a difference of 10.7 percentage points per year; another combined classification produced an 11.2-point average annual difference [5]. They reported value outperformance across the five postformation years and argued that naive extrapolation contributed to the spread [5].

The study also addressed risk and data design rather than treating raw returns as self-interpreting. It presented size-adjusted results, used annual buy-and-hold periods, restricted much analysis to NYSE and AMEX firms, and discussed look-ahead and survivorship concerns [5]. Its behavioral interpretation differs from Fama and French's risk emphasis, demonstrating that a return spread can be well documented while its economic cause remains disputed. A screening process should preserve that disagreement rather than describe value outperformance as proof of a free return.

### Oppenheimer and Mohanty-Oxman: NCAV evidence is positive but conditional

Oppenheimer tested Graham's net-current-asset criterion over 1970-1983. CFA Institute's abstract reports that qualifying portfolios had higher mean returns than market benchmarks and significantly greater full-period risk-adjusted returns; thirty-month portfolio outcomes were widely variable even though the portfolios as a group outperformed [6]. The most deeply discounted portfolios tended to outperform by the widest margins [6]. This supports the diversified-screen concept and warns against converting the average result into certainty about a selected company.

Mohanty and Oxman extend the U.S. evidence through 2019. Their sample contains 648 unique firms meeting a price-below-two-thirds-of-NCAV criterion over 1969-2019 [8]. The value-weighted NCAV portfolio earned an average 1.94 percent per month. After controls for the Fama-French five factors, the Pastor-Stambaugh liquidity factor, and the January effect, the reported alpha was 1.09 percent per month, equivalent in the paper to 13.9 percent annually; compounding 1.09 percent for twelve months gives approximately 13.89 percent [8]. Industry- and size-matched controls showed no abnormal return, but strategy profitability declined in 2004-2019 [8]. The long sample strengthens the evidence for a historical anomaly while the later weakening argues against a timeless expected return.

### Piotroski: financial strength changed outcomes within value stocks

Piotroski assembled 14,043 high-book-to-market firm-year observations over twenty-one annual cohorts associated with 1976-1996 returns [7]. One-year buy-and-hold returns began in the fifth month after fiscal year-end, a lag chosen to improve information availability [7]. High F_SCORE firms, scores eight or nine, earned a mean one-year market-adjusted return of 13.4 percent, compared with 5.9 percent for the full high-book-to-market sample and negative 9.6 percent for low-score firms, scores zero or one [7]. The high-minus-all difference was 7.5 percentage points and the high-minus-low difference was 23.0 points, both reported as statistically significant at the one-percent level [7].

The distributional evidence was broader than the mean: several percentiles and the proportion of positive observations shifted in favor of the high-score group [7]. Yet the design remains conditional on high book-to-market selection, binary accounting definitions, a historical U.S. sample, and data-handling choices. The paper itself notes a potential data-snooping limitation [7]. Its proper implication is that simple contemporaneous financial information can help discriminate within a cheap universe, not that a nine-point score eliminates valuation, business, or implementation risk.

### Practitioner records show process, not causal proof

Buffett's 1984 essay reports that Walter Schloss's limited partners compounded at 16.1 percent over 28.25 years compared with 8.4 percent for the S&P, while the partnership before general-partner allocations compounded at 21.3 percent [9]. The accompanying description identifies approximately one hundred positions and emphasizes Schloss's independence and price-versus-value orientation [9]. This corrects the stronger claim that the cited record proves a pure NCAV strategy: the source presents a broadly diversified Graham-influenced process, not a controlled attribution of returns to one formula.

The essay is relevant evidence that a Graham-derived discipline was implemented over a long period. It is not a randomized comparison, and Buffett selected an intellectual group to make an argument about efficient markets [9]. Practitioner records combine security selection, portfolio construction, fees, cash, taxes, trading, changing opportunity sets, and judgment. They can demonstrate that a process existed and produced a documented record; they cannot isolate the causal contribution of the Graham Number.

### Accounting and implementation evidence narrow the usable claim

CFA Institute's 2025 report shows why a fixed book-value multiple can change meaning over time. More than 70 percent of surveyed investors agreed that important unrecognized intangibles explain material book-to-market gaps for many listed companies, and the report illustrates how expensed research and other internal investment can leave recorded equity small relative to market value [10]. This evidence does not justify capitalizing every expense or abandoning balance sheets. It requires the analyst to understand recognition differences before comparing firms or declaring a high P/B ratio irrational.

Backtests face an additional failure mode when unsuccessful securities disappear. Shumway documents that missing performance-related delisting returns in CRSP were large and negative and that omitting them biased return evidence [11]. Trading costs add another wedge: Li, Chow, Pickard, and Garg show that factor-index costs depend on turnover, trade concentration, liquidity, weighting, and scale, and that market impact is not captured merely by visible commissions [12]. These findings explain why gross historical factor returns, especially in small or distressed names, are not the same as returns available to a particular investor.

The evidence supports a bounded conclusion. Transparent cheapness screens have produced strong average returns in several historical portfolio studies, and financial-strength information has improved discrimination in at least one influential high-book-to-market sample [4][5][6][7][8]. The studies differ in signal, universe, period, weighting, and interpretation, and newer NCAV evidence reports weaker later-period profitability [8]. Quantitative screening is therefore evidence-backed as a search and research-design discipline; it is not evidence-backed as a universal guarantee of superior returns or as a substitute for valuing the common claim.

## Implications

### Build a screen as a falsifiable specification

For an analyst, the first deliverable should be a written rule that another person can reproduce. It should name the universe, security and exchange eligibility, valuation date, price source, filing cutoff, accounting fields, treatment of preferred stock and noncontrolling claims, share-count convention, currency, negative-value handling, rebalance date, holding period, weighting, and exclusions. The output should retain the raw inputs and show why each security passed. This discipline prevents a convenient data substitution after results are known and makes later review possible [7][11].

A Graham Number screen should report at least five fields: price, three-year average EPS if following the 1973 criterion, common BVPS, the observed `(P/E) x (P/B)` product, and the square-root boundary [1]. It should separately mark whether the nominal P/E and P/B guidelines pass. This makes the product-rule distinction visible. If a modern user substitutes trailing EPS, forecast EPS, tangible book, or adjusted book, the screen should receive a different label rather than silently borrowing Graham's authority.

An NCAV screen should display current-asset components, total liabilities and senior claims, diluted common shares, aggregate market capitalization, NCAV, and price as a percentage of NCAV. It should flag restricted cash, doubtful receivables, inventory concentration, cash burn, contingencies, and control over realization. The author's synthesis is that the unadjusted rule and a haircut liquidation case should be shown side by side: the first preserves the historical screen, while the second tests whether its apparent cushion survives economic adjustments [1][6][8].

### Separate discovery, verification, valuation, and decision

The author's workflow separates discovery, verification, valuation, and decision. The screen's job is discovery. Verification confirms that the data were available, correctly classified, and matched to the security and claim. Valuation asks what the assets or normalized cash flows are worth under explicit scenarios. The decision compares that range with price, required return, alternative opportunities, liquidity, governance, and other relevant constraints. Collapsing these stages invites a low ratio to masquerade as a complete thesis.

The author's research sequence begins by asking why the candidate is cheap. One branch tests temporary accounting or operating weakness; another tests structural decline; another tests financial distress and claim priority; another tests whether book value is economically relevant; another tests whether the market price reflects a catalyst delay or agency problem. Piotroski's evidence suggests that recent financial strength can help distinguish outcomes within high-book-to-market stocks [7]. It does not remove the need to understand the business, and it does not establish that every high-score company is undervalued.

The author's inversion identifies a false margin of safety as the worst screening error. A Graham Number built from peak earnings and overstated book equity can appear conservative while capitalizing two fragile inputs. An NCAV surplus can disappear through operating losses or senior claims before shareholders receive it. The prevention is to challenge each input with a downside case, reconcile all claims ahead of common equity, and identify how value can be realized. If the screen cannot survive those checks, its historical pedigree does not rescue the candidate.

### Interpret an empty or crowded screen cautiously

Few passing candidates do not by themselves prove that the whole market is expensive. The outcome can also reflect the screen's industry bias, inflation-stale nominal thresholds, accounting changes, rising intangible intensity, an altered interest-rate environment, or a universe that excludes the segment where the rule historically operated [1][10]. Many passing candidates likewise do not prove that the market is cheap; widespread losses, impaired assets, leverage, or a recession can make backward-looking ratios look attractive together.

The author's assessment is that candidate count is a diagnostic series, not a market-timing signal. A disciplined user can track the count, median inputs, sector distribution, and later outcomes under an unchanged specification. Any decision to alter thresholds should be justified by the economics and accounting of the measure, tested out of sample, and documented before seeing which change produces a preferred backtest.

### Match conclusions to the study design

Graham's own NCAV discussion and Oppenheimer's test concern diversified groups [1][6]. Piotroski's score operates across a broad high-book-to-market sample [7]. The author's inference is that these studies support average screening results, not certainty about an isolated security. Selecting one distressed company from evidence generated by many observations changes the proposition, while copying the historical group without its eligibility, timing, weighting, and cost rules also changes the test.

Implementation limits determine whether published screen evidence can be reproduced. Li, Chow, Pickard, and Garg show that turnover, rebalance concentration, weighting, liquidity, and scale affect market-impact cost [12]. A screening report should therefore state the bid-ask spread, expected market impact, turnover, rebalance timing, and capacity assumptions used to translate a gross historical return into an implementable estimate. These are validation conditions for the claimed screen result; decisions about actual portfolio allocation belong in the adjacent portfolio-risk-management domain.

### Backtests should preserve failed and inconvenient observations

A credible test uses point-in-time constituents and filing data, includes inactive securities, applies delisting returns consistently, and discloses missing values. Shumway's evidence shows why assigning no loss to a negative delisting can overstate performance [11]. A result should be rerun under alternative reasonable assumptions for missing delisting returns, stale prices, microcap exclusions, transaction costs, and rebalance timing. If the conclusion disappears under a plausible implementation, the screen is not robust enough to support a strong claim.

The study period also matters. Fama and French, Lakonishok-Shleifer-Vishny, Oppenheimer, Piotroski, and Mohanty-Oxman examine different eras and rules [4][5][6][7][8]. Combining their strongest figures into one expected return would be invalid because the portfolios are not the same. The appropriate comparison is a table of definitions, samples, gross results, controls, and limitations. Agreement across distinct designs raises confidence in a broad cheapness effect; disagreement identifies where the effect depends on method.

### Use the formula as a question generator

For a positive-EPS, positive-book company, the Graham Number can quickly reveal how much price is being paid for the joint earnings-and-book base. A large apparent discount should prompt questions about earnings normalization, asset quality, leverage, dilution, capital allocation, and why the opportunity persists. A failure can also be informative: it may show that the market price depends on valuable intangible assets or future economics that the rule intentionally does not capture [1][10]. Neither result is a verdict.

The author's capital-allocation interpretation is that the same decomposition can help managers diagnose what a low multiple may signal. A discount to book may reflect expected poor returns on equity, untrusted asset values, excess capital, or weak governance. Repurchases create value only if the shares are below a defensible value and the company retains adequate financial strength; a low historical ratio alone is insufficient. For fiduciaries and researchers, a mechanical screen is most valuable when it makes assumptions auditable and constrains story-driven exceptions.

The durable Graham lesson is procedural rather than numerical. Define what counts as evidence, pay a price that leaves room for error, diversify when the method relies on group outcomes, and revise implementation when markets or accounting change [1][3]. Modern empirical research supports disciplined cheapness and quality signals in bounded settings [4][5][6][7][8]. Human judgment enters not to override every failed rule, but to determine whether the rule's inputs describe economic reality and whether the resulting common claim offers a realizable margin of safety.

## Common Pitfalls and Limitations

The first pitfall is formula overclaim. `sqrt(22.5 x EPS x BVPS)` is an algebraic boundary derived from a ratio-product rule; it is not a discounted cash flow, an asset appraisal, or proof that both P/E and P/B remain below their separate nominal limits [1][2]. Calling the result intrinsic value imports a conclusion that neither the arithmetic nor the source establishes.

The author's second pitfall is input inconsistency. Mixing forecast EPS with historical book value, basic EPS with diluted BVPS, a post-year-end price with later restated accounts, or equity price with enterprise-level earnings produces a ratio without a coherent claim or date. Negative EPS or BVPS makes the ordinary Graham Number economically unusable. A screen should reject or separately classify such observations rather than force a value through absolute values or sign cancellation.

The author's third pitfall is treating book equity or NCAV as realizable proceeds. Reported assets can be restricted, obsolete, pledged, or costly to collect, while claims and wind-down costs can be incomplete. Internally generated intangibles can also make ordinary book value understate the resources supporting an asset-light business [10]. The fix is not to assume every intangible has value; it is to reconcile the accounting amount to an explicit economic premise.

The fourth pitfall is backtest leakage. Survivorship filtering, future restatements, insufficient filing lags, missing delisting losses, and after-the-fact threshold changes all make historical results too favorable [7][11]. The fifth is friction blindness: turnover, spreads, market impact, taxes, position size, and capacity can absorb a paper return, especially in small or distressed securities [12]. Every published screen result should distinguish gross research return from a documented implementable estimate.

The final pitfall is causal certainty. Fama and French's risk interpretation and Lakonishok, Shleifer, and Vishny's behavioral interpretation are not the same [4][5]. Oppenheimer's and Mohanty-Oxman's NCAV results use different periods and tests, with the later study reporting weaker profitability after 2004 [6][8]. The evidence warrants investigation and disciplined screen design, not the assertion that mechanical cheapness always produces superior returns.

## Sources

1. Graham, B. (1973; 2003 edition with commentary by J. Zweig).
   *The Intelligent Investor*, fourth revised edition. Primary Graham text for
   the seven defensive criteria, 22.5 product rule, and diversified
   net-current-asset method; the linked edition also contains later commentary.
   https://dn760006.eu.archive.org/0/items/bookplanetbookof0000unse_20230621/Benjamin%20Graham%2C%20Jason%20Zweig%2C%20Warren%20E.%20Buffett%20-%20The%20Intelligent%20Investor-Harper%20Business%20%281973%29.pdf [high]

2. GrahamValue. "Tweaking Benjamin Graham's Stock Selection Criteria."
   Secondary explanation of the later "Graham Number" shorthand and its
   relationship to Graham's full defensive criteria.
   https://www.grahamvalue.com/article/tweaking-benjamin-grahams-stock-selection-criteria [medium]

3. Graham, B. (1976). "A Conversation with Benjamin Graham."
   *Financial Analysts Journal*, 32(5), 20-23. Primary interview on simplified
   group selection, objective criteria, selling policy, and allocation.
   https://doi.org/10.2469/faj.v32.n5.20 [high]

4. Fama, E.F. and French, K.R. (1992). "The Cross-Section of Expected Stock
   Returns." *Journal of Finance*, 47(2), 427-465. U.S. evidence on size,
   book-to-market, beta, portfolio construction, and risk interpretation.
   https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1992.tb04398.x [high]

5. Lakonishok, J., Shleifer, A., and Vishny, R.W. (1994). "Contrarian
   Investment, Extrapolation, and Risk." *Journal of Finance*, 49(5),
   1541-1578. Value-versus-glamour portfolio evidence and behavioral
   interpretation, with sample and data-design qualifications.
   https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1994.tb04772.x [high]

6. Oppenheimer, H.R. (1986). "Ben Graham's Net Current Asset Values: A
   Performance Update." *Financial Analysts Journal*, 42(6), 40-47.
   Portfolio evidence for the NCAV criterion over 1970-1983.
   https://rpc.cfainstitute.org/research/financial-analysts-journal/1986/ben-grahams-net-current-asset-values-a-performance-update [high]

7. Piotroski, J.D. (2000). "Value Investing: The Use of Historical Financial
   Statement Information to Separate Winners from Losers." *Journal of
   Accounting Research*, 38 Supplement, 1-41. Original F_SCORE study,
   definitions, sample, return timing, findings, and limitations.
   https://www.anderson.ucla.edu/documents/areas/prg/asam/2019/F-Score.pdf [high]

8. Mohanty, S.K. and Oxman, J.J. (2026). "Does Ben Graham's Net Current
   Asset Value Investing Continue to Generate Excess Returns?" *Review of
   Financial Economics*, 44(1), e70034. U.S. NCAV evidence for 1969-2019,
   factor controls, and later-period weakening.
   https://onlinelibrary.wiley.com/doi/full/10.1002/rfe.70034 [high]

9. Buffett, W.E. (1984). "The Superinvestors of Graham-and-Doddsville."
   Columbia Business School. Primary essay and performance tables, including
   Walter Schloss's record and portfolio description.
   https://business.columbia.edu/insights/chazen-global-insights/superinvestors-graham-and-doddsville [high]

10. Peters, S.J. and Winters, M.P. (2025). *Investor Perspectives: Intangible
    Assets*. CFA Institute Research and Policy Center. Accounting-recognition,
    book-to-market, company examples, and investor-survey evidence.
    https://rpc.cfainstitute.org/sites/default/files/docs/surveys/intangibles-report_online.pdf [high]

11. Shumway, T. (1997). "The Delisting Bias in CRSP Data." *Journal of
    Finance*, 52(1), 327-340. Evidence that omitted negative delisting returns
    can bias historical stock-return tests.
    https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1997.tb03818.x [high]

12. Li, F., Chow, T., Pickard, A.J., and Garg, Y. (2019). "Transaction
    Costs of Factor-Investing Strategies." *Financial Analysts Journal*,
    75(2), 62-78. Framework and evidence on turnover, liquidity, market
    impact, weighting, and capacity.
    https://www.tandfonline.com/doi/full/10.1080/0015198X.2019.1567190 [high]

## See Also

- `library/valuation-screening/discounted-cash-flow-dcf-methodology.md` -- an intrinsic-value framework that makes cash-flow, reinvestment, risk, and terminal assumptions explicit.
- `library/valuation-screening/valuation-multiples-pe-ev-ebitda-pb-analysis.md` -- claim matching and interpretation for the component multiples used in quantitative screens.
- `library/valuation-screening/earnings-power-value-and-asset-based-valuation.md` -- reconciliation of current earning power, asset value, NCAV, and claim realization.
- `library/value-investing/anchor-value-investing.md` -- the adjacent philosophy domain for margin of safety and price-versus-value principles.
