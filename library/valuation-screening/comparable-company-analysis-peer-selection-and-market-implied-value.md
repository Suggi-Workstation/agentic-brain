---
name: comparable-company-analysis-peer-selection-and-market-implied-value
id: 20261001T013809Z
tier: library-topic
domain: valuation-screening
author: Librarian
tags: [comparable-company-analysis, trading-comparables, peer-selection, relative-valuation, enterprise-value, normalization, market-implied-value]
links: [library/valuation-screening/valuation-multiples-pe-ev-ebitda-pb-analysis.md, library/valuation-screening/enterprise-value-equity-value-reconciliation.md, library/valuation-screening/precedent-transaction-analysis.md, library/valuation-screening/sum-of-the-parts-valuation.md, library/valuation-screening/reverse-dcf-and-sensitivity-analysis.md]
reviewed: 2026-10-01
---

# Comparable Company Analysis Is a Controlled Comparison, Not a Peer Median

Comparable company analysis converts the observed prices of selected public peers into a market-implied enterprise-value or equity-value range for a target.[1][2][3] Its reliability depends on controlling the valuation date, peer economics, claim perimeter, accounting definitions, forecast period, and statistical treatment.[1][2][3][12] The author's synthesis is that an uncontrolled peer median is a market quotation rather than a defensible valuation.

## Background

Comparable company analysis, also called trading comparables or public-company comparables, is a market-approach valuation method. The analyst identifies publicly traded businesses that can inform the value of a target, measures each peer's equity value or enterprise value at a common date, divides that value by a consistently defined operating or equity metric, and applies a selected multiple range to the target's corresponding metric. The method is relative: it asks how the market prices comparable economics. It does not independently estimate the present value of the target's future cash flows.[1][2][3]

The author's synthesis uses a limited law-of-one-price intuition: if two businesses expose capital to sufficiently similar growth, profitability, reinvestment, and risk, then a large unexplained difference in their valuation ratios deserves investigation.[1][14] International Valuation Standards describe the market approach as comparison with identical or comparable assets or liabilities for which price information is available. The standards also require qualitative and quantitative analysis where comparables are not substantially identical, and they require adjustments to be reasonable, documented, and quantified.[2] The author's synthesis is that "comparable" describes a conclusion reached after analysis, not a database industry code.

Trading comparables use public-market prices. NACVA's guideline-public-company-method materials describe the initial output as a minority, marketable equity value because the underlying observations are individual securities sold in public markets.[16] That output differs from a negotiated change-of-control price, which can include control rights, expected synergies, auction effects, and transaction-specific financing. Professional valuation guidance treats control and marketability as characteristics of the interest being valued rather than automatic premiums or discounts.[2][16] The author's synthesis is that a trading-comps result should be labeled as a market-implied indication at the stated level of value and should not absorb a generic acquisition premium.

Relative valuation is useful because observed prices and financial metrics can be reduced to ratios and peer ranges without disclosing a complete long-term cash-flow forecast. The author's assessment is that this convenience is also the central risk. Damodaran shows that a multiple is a compressed valuation model: P/E reflects payout, growth, and required return; P/B reflects profitability relative to equity capital as well as growth and risk; and enterprise multiples reflect operating cash flow, reinvestment, growth, and the cost of capital.[1] McKinsey similarly argues that peers should have similar expected growth and return on invested capital, that forward multiples usually carry more information than historical multiples, and that enterprise-value ratios need adjustment for nonoperating items.[14] The ratio hides assumptions; it does not eliminate them.

Observed multiples also inherit the market regime. Interest rates, risk premiums, sector enthusiasm, liquidity, and aggregate expectations can lift or compress a whole peer group.[1][6] Damodaran explicitly warns that relative valuation can reproduce a sector's collective overvaluation or undervaluation.[1] The author's synthesis is that a precise multiple applied to a carefully normalized target can remain consistent with a mispriced market: it answers what value is implied on comparable current-market terms, not what the target is worth independent of those prices.

Three distinctions organize the method. First, equity-value multiples pair the market value of common equity with a metric attributable to common equity, such as net income, earnings per share, or book equity. Enterprise-value multiples pair the value of operating claims with a pre-financing metric such as revenue, EBIT, or EBITDA. Damodaran and CFA Institute both state the numerator-denominator consistency rule: an equity numerator must use an equity denominator, while an enterprise numerator must use a firm-wide denominator.[1][3]

Second, trailing and forward multiples answer different questions. A trailing ratio uses realized historical performance, commonly the latest twelve months. A forward ratio uses estimated performance for a future period. CFA Institute defines trailing P/E using the most recent four quarters and forward P/E using expected earnings.[3] McKinsey and the empirical studies by Liu, Nissim, and Thomas and by Kim and Ritter find advantages to forward measures in their examined settings, while those studies also expose forecast-availability, forecast-quality, and sample limitations.[4][5][14] The author's synthesis is that mixing one peer's trailing metric with another peer's forward metric destroys period comparability even if both columns are labeled EBITDA.

Third, observed and normalized metrics are not the same. Acquisitions, restructuring, unusual gains or charges, lease accounting, stock compensation, pension items, and different accounting policies can make reported values economically noncomparable.[2][10][11][12][14][17] The SEC warns that a non-GAAP measure can be misleading if it excludes normal recurring cash operating expenses, applies adjustments inconsistently across periods, or relabels an accounting measure without a clear definition.[9] The author's synthesis is that the analyst must reconstruct a common definition rather than accept each company's adjusted EBITDA as if the labels guaranteed comparability.

The author's synthesis is that comparable company analysis is best understood as a controlled experiment with imperfect matches. The peer set supplies market observations; normalization tries to hold measurement constant; peer selection tries to hold economics constant; range selection acknowledges residual differences; and DCF, precedent transactions, SOTP, and reverse DCF test what the market evidence actually implies. The analysis becomes useful when every departure from comparability is visible. It becomes weak when judgment is hidden behind a median.

## Core Concepts

### Define the question, date, perimeter, and level of value

The author's proposed control framework starts with four declarations: the target being valued, the valuation date, the asset and claim perimeter, and the desired level of value.[2][12] The target may be a consolidated public company, a private company, a subsidiary, or one segment of a diversified group. The valuation date fixes market prices, exchange rates, debt, cash, share counts, estimates, and information available to investors. The perimeter states which operations and assets belong in the denominator. The level of value states whether the output is operating enterprise value, aggregate common equity value, or diluted value per share.[2][12]

The author's synthesis is that these declarations prevent a common mismatch. A peer's market capitalization at today's price cannot be combined with debt from a stale annual report and a forecast issued after the valuation date without creating a hybrid observation. A target segment cannot use a consolidated peer's enterprise value unless noncomparable operations and claims are removed. A valuation of common shares cannot stop at enterprise value. Each input should carry a source date and definition so that the model can be reproduced.[2][12]

### Build a broad universe, then prove the peer set

Peer selection should proceed from a documented universe to a narrower primary set. The broad universe can be assembled by product, service, customer, industry classification, geography, and competitor disclosures. The final set should be based on economic drivers rather than labels alone. IVS identifies market segment, geography, size, growth, profit margins, leverage, liquidity, and diversification as relevant comparison dimensions.[2] McKinsey emphasizes expected growth and ROIC because two firms in one industry can deserve different multiples when one reinvests at high returns and the other destroys value.[14]

The author's proposed peer matrix records, for each candidate, business and product mix, customer type, revenue geography, scale, growth, margins, capital intensity, cyclicality, leverage, accounting regime, forecast coverage, free float, and trading liquidity.[2][12][14][16] No candidate must match on every column. The author's framework uses primary peers for substantial weight, secondary peers for broader sensitivity, and peripheral companies only as contextual observations.[2][12]

The author's proposed exclusion policy requires a recorded reason. Examples include a materially different business mix, a structural margin difference, financial distress, an acquisition that makes historical metrics stale, a negative or near-zero denominator, thin trading, unreliable estimates, or an accounting definition that cannot be reconciled.[1][2][12] The same rule should be applied symmetrically. Damodaran warns that deleting only high outliers can bias the selected multiple, while unstable denominators can make an observation economically unusable.[1]

Peer count is not a substitute for peer quality. Cooper and Lambertides find that a small set of growth-matched firms can equal or exceed the accuracy of a full-industry set, although the result depends on how closely the selected peers match the target and on the risk of extreme errors.[8] The author's synthesis is to prefer the smallest set that captures the target's material economics without making the valuation depend on one observation. The model should also show how the result changes when the primary set is widened.

### Construct equity value and enterprise value consistently

For a public peer, aggregate common equity value begins with price per share multiplied by current fully diluted shares. Fully diluted capitalization requires analysis of options, warrants, restricted units, convertibles, and other equity-linked instruments under their actual terms. Rosenbaum and Pearl describe the treasury stock method for in-the-money options and warrants and the if-converted or settlement analysis for convertible securities.[12] FASB's 2020 convertible-instrument update requires the if-converted method for diluted EPS under US GAAP.[15] The author's synthesis is that accounting diluted EPS and point-in-time valuation dilution serve different purposes; the valuation model should use current security terms and should not count a convertible simultaneously as debt and equity.[12][15]

A general enterprise-value bridge is:

`Enterprise value = common equity value + debt + preferred claims + noncontrolling interests + other operating claim adjustments - cash and nonoperating assets.`

This is a classification framework, not a universal instruction to add every liability or subtract all cash. The analyst asks whether the claim finances the operating assets represented in the denominator and whether its related income or expense is included in that denominator.[1][3][12] Cash, debt, preferred claims, noncontrolling interests, lease obligations, and convertible instruments require treatment consistent with the denominator.[10][11][12][15] The bridge should state each convention and apply it to every peer and the target.

Lease accounting illustrates why matching matters. Topic 842 requires US GAAP lessees to recognize assets and liabilities for operating and finance leases, but operating leases retain a different income-statement pattern from finance leases. IFRS 16 generally uses a single lessee model that replaces former operating-lease expense with depreciation and interest, which tends to increase EBITDA.[10][11] Adding lease liabilities to enterprise value while leaving peer EBITDA definitions inconsistent can double count or manufacture differences. The analyst can use a lease-adjusted or lease-unadjusted convention, but the numerator and denominator must follow the same convention across the set.

### Align denominators, periods, currencies, and estimate vintages

The denominator should represent the same economic claim, period, and accounting policy for every observation. Equity value belongs with net income, EPS, or book equity. Enterprise value belongs with revenue, EBIT, EBITDA, or another pre-financing operating measure.[1][3] EV/EBITDA can reduce differences caused by leverage and taxes, but it does not neutralize capital intensity, working-capital needs, lease classification, or reinvestment. Revenue multiples require explicit margin analysis because equal revenue can produce very different cash flow.[1][3]

Period alignment normally requires separate panels for historical LTM, current-calendar-year estimates, and next-calendar-year estimates. Calendarization converts peers with different fiscal year ends to a common calendar period. Rosenbaum and Pearl describe a weighted blend of current and next fiscal-year estimates and recommend quarterly estimates when available.[12] The approximation is weak when seasonality, acquisitions, or nonlinear growth make annual blending misleading. A model should identify whether a figure is reported, consensus, management guidance, or analyst-estimated and should preserve the estimate vintage available on the valuation date.

The author's proposed currency control is to state one convention and apply it consistently. The model should identify the exchange-rate date or period used for market values, balance-sheet claims, and operating metrics, and it should avoid creating a numerator-denominator mismatch through inconsistent translation. Businesses exposed to volatile or multiple currencies may need separate sensitivity analysis; this is an analytical convention rather than a claim that one translation method is universally correct.

### Normalize raw financials through a visible schedule

Normalization is not a single adjusted EBITDA line. It is a peer-by-peer bridge from reported figures to a common economic definition. A useful schedule separates operating, nonoperating, recurring, nonrecurring, acquired, disposed, and accounting-policy effects. IVS requires presentation of subject and comparison-company financial data on a consistent basis and identifies arm's-length, related-party, nonrecurring, and accounting-basis adjustments as relevant.[2]

The author's proposed normalization checklist includes restructuring, unusual legal costs, impairments or asset write-downs, acquisition adjustments, pension and lease effects, stock compensation, and differences in treatment of intangible investment.[2][9][10][11][12][14][17] The decision rule is not whether management calls an item adjusted. It is whether the item belongs in the sustainable economic metric being compared. The SEC's non-GAAP guidance supplies a guardrail: normal recurring cash operating costs remain operating costs even if they occur irregularly, and comparable gains and charges should be treated consistently.[9]

The author's pro forma control aligns acquisitions and divestitures to the same operating perimeter. A peer's current price may reflect an acquisition that is absent from its LTM denominator, while a target's denominator may include a business that has been sold.[12] Pro forma adjustments should reflect the operating perimeter known at the valuation date and should not include speculative synergies merely to raise earnings. Differences between reported, company-adjusted, and analyst-normalized figures should remain visible so that another reviewer can reverse the choices.[2][12]

Intangible investment creates another comparison problem. R&D, software, branding, and customer acquisition are commonly expensed even when analysts regard them as investments, which can reduce reported earnings, EBITDA, and invested capital for intangible-intensive businesses.[17] Capitalizing and amortizing selected expenditures can materially change P/E and EV/EBITDA, but the adjustment requires judgment.[17] The author's synthesis is that an analyst can make a supported capitalization adjustment or preserve reported accounting and address business-model differences through the peer matrix; inventing unverifiable assets is not an improvement over unadjusted accounting.

### Select a statistic and range without hiding dispersion

Once the model produces valid peer multiples, it should show the individual observations and their distribution. Useful summaries include median, quartiles, arithmetic mean, harmonic mean, and selected weighted statistics. Damodaran documents positive skewness in P/E distributions and explains why arithmetic means can exceed medians when extreme positive observations are present.[1] Baker and Ruback find the harmonic mean close to their minimum-variance benchmark in a sample of S&P 500 industries, while Liu, Nissim, and Thomas also find strong performance from harmonic-mean aggregation in their tested setting.[4][7] Those results do not establish one universal statistic.

Outliers should be investigated before they are excluded. A high multiple may reflect exceptional growth, a temporarily small denominator, a data error, a different business, or market exuberance. A low multiple may reflect distress, structural decline, poor liquidity, or a noncomparable claim bridge.[1][12][13] Exclusion is defensible when the observation fails stated comparability or measurement rules, not merely because it widens the range. The author's assessment is that winsorization can limit influence in a large statistical sample but is difficult to justify in a small peer set where each company is economically distinct.

The author's proposed range presentation shows the full observed set, interquartile range, median, and a selected range based on the strongest peers. Weighting can be qualitative or quantitative, but the reason should be stated.[1][2][12][13] Damodaran and Meitner describe regression as one way to relate multiples to value drivers.[1][13] The author's assessment is that regression is useful only when the sample and specification are stable enough to interpret, and that an in-sample relationship should not be described as causal without separate evidence.

### Apply the range and reconcile to diluted per-share value

An enterprise multiple is applied to the target's corresponding normalized enterprise metric:

`Implied enterprise value = selected enterprise multiple x target enterprise metric.`

The analyst then moves claim by claim to common equity:

`Implied common equity value = implied enterprise value - debt and senior claims + cash and nonoperating assets, subject to the stated perimeter.`

Finally:

`Implied value per diluted share = implied common equity value / current fully diluted shares.`

An equity multiple can be applied directly to an equity metric, but it still requires a consistent diluted share count and treatment of equity-linked claims.[12][15] A valuation table should show low, midpoint, and high multiples across more than one target metric where appropriate. It should also show sensitivity to net debt, dilution, and target normalization because those items can dominate the residual value for common shareholders.

Premiums and discounts should be explained through economics rather than appended as undocumented percentages. Higher sustainable growth, margins, ROIC, recurring revenue, or lower risk can support a higher multiple; greater capital intensity, cyclicality, customer concentration, or execution risk can support a lower one.[1][14] Liquidity and free float can affect public-market evidence, but the magnitude of any adjustment requires support.[2] NACVA describes the public-company method's initial result as minority and marketable and treats control or marketability adjustments as dependent on the subject interest.[16] The author's synthesis is that a generic control premium does not belong in a trading-comps output unless the valuation purpose changes and the control economics are separately established.

The author's synthesis is that the final result should be reconciled with DCF, precedent transactions, SOTP, and reverse DCF.[1][14] DCF tests the cash-flow assumptions that a multiple compresses; precedent transactions supply dated control-price evidence; SOTP tests whether different segments require different comparison sets; and reverse DCF expresses the market-derived value as operating assumptions.[1][14] Disagreement among methods is evidence to analyze, not noise to average away.

## Evidence

### Forward measures improve fit, but forecasts create a new error source

Liu, Nissim, and Thomas compare multiple-based equity valuations across earnings, cash flow, book value, and sales measures. In their sample, forward-earnings multiples perform best; two-year-ahead forecast earnings produce absolute pricing errors below 16 percent for approximately half of the firms. Same-industry comparables perform better than using the entire cross-section, and harmonic-mean aggregation performs strongly relative to the arithmetic mean and median.[4] The result supports forward, economically matched comparisons. It does not show that consensus forecasts are unbiased or that earnings are the best denominator for loss-making or analyst-uncovered firms.

Kim and Ritter study IPO valuation using 1992-1993 observations. They report that average absolute prediction error falls from 55.0 percent using historical earnings to 43.7 percent using current-year forecast earnings and 28.5 percent using next-year forecast earnings. Peers chosen by a specialist research firm also outperform a mechanical industry algorithm, although the authors attribute much of the improvement to forecast use.[5] The sample concerns young IPOs in a specific period, so the numerical error rates should not be generalized to mature public companies. The durable finding is narrower: estimate quality and economically informed peer selection materially affect the result.

Forward estimates can also create circularity. McKinsey warns that forward forecasts inferred from an assumed multiple can become circular.[14] Liu, Nissim, and Thomas exclude firms without analyst forecasts, while Kim and Ritter note potential conflicts involving underwriter-affiliated analyst forecasts.[4][5] The author's synthesis is to use forward multiples when the estimates are independent enough to be informative, preserve the estimate date, and show a trailing or normalized cross-check rather than treating consensus as observed fact.

### Economic matching can matter more than industry labels or peer count

Dittmann and Weiner examine EV/EBIT valuation across 16 countries from 1993 through 2002. Their study finds that peers selected by similar return on assets outperform selection based only on industry or total assets in their principal comparisons. The preferred geographic pool differs by market, and valuation errors increase around the 1999-2000 boom.[6] These results support three controls: profitability belongs in the peer matrix, geographic comparability is context dependent, and regime conditions affect relative-valuation accuracy.

Cooper and Lambertides find that about 10 growth-matched firms were as accurate on average as the entire industry, while five were only slightly less accurate; small sets performed best when their average expected growth was close to the target's.[8] The evidence rejects the assumption that more observations automatically improve valuation. A larger set reduces dependence on one company but can increase economic mismatch.

The studies do not produce one mechanical peer algorithm. Profitability, growth, geography, and industry each matter differently across samples. The author's synthesis is to use theory to identify the target's material value drivers, score candidate peers on those drivers, and disclose sensitivity to alternative defensible sets. A peer matrix is more auditable than a claim that management selected "leading companies" without criteria.[6][8]

### Aggregation rules matter because multiple distributions are not symmetric

Damodaran documents positive skewness in P/E distributions and explains why the arithmetic mean can sit above the median when extreme positive observations are present.[1] Baker and Ruback estimate industry multiples for 22 S&P 500 industries in 1995 and find the harmonic mean close to their minimum-variance estimator. In their setting, the simple mean systematically exceeds the harmonic mean and can overestimate value.[7] Liu, Nissim, and Thomas likewise find favorable performance for harmonic-mean peer multiples in their tested sample.[4]

These findings support reporting more than one summary statistic and explain why a mean is not neutral. They do not make the harmonic mean universally correct. Negative or near-zero denominators can make a multiple undefined or unstable, a harmonic mean can place strong weight on low observations, and a small hand-selected set may be better interpreted company by company. Meitner's market-approach treatment therefore presents arithmetic mean, median, harmonic mean, and regression as distinct methods whose suitability depends on the sample and error structure.[13]

The economic investigation of outliers remains prior to the statistical decision. If the highest multiple belongs to the only peer with recurring revenue and superior ROIC, deleting it removes information. If it arises from a denominator depressed by a one-time charge, normalizing the denominator may solve the problem. If it is a data error, correction is required. A robust process records the raw observation, the adjustment, the exclusion rule, and the effect on the selected range.[1][7][12][13]

### Standards and accounting evidence support consistent normalization

Current IVS guidance requires consistent presentation between the subject and comparison businesses, reasonable and documented adjustments, and analysis of differences rather than unexamined reliance on a label.[2] The SEC's non-GAAP interpretations warn that excluding normal recurring cash operating costs can mislead and that inconsistent treatment across periods requires disclosure and explanation.[9] Together, these sources support an analyst-normalized schedule with explicit definitions; they do not support accepting every issuer's preferred adjusted metric.

Lease standards show a concrete cross-company measurement break. US GAAP Topic 842 recognizes operating and finance lease assets and liabilities but retains different expense presentation by lease classification. IFRS 16 generally uses one lessee model, with depreciation and interest replacing former operating-lease expense for most leases, thereby affecting EBITDA and leverage metrics.[10][11] A peer set spanning the two regimes can show different EBITDA even when lease economics are similar. A consistent model must align the enterprise-value claim and the earnings definition rather than add a generic lease adjustment.

Dilution presents another break. FASB's amended diluted-EPS guidance uses the if-converted method for convertible instruments and adjusts both numerator and denominator where applicable.[15] Trading-comps valuation, however, measures current capitalization at a point in time. Rosenbaum and Pearl's investment-banking framework calculates current diluted equity value from share price and fully diluted shares, then reconciles debt, preferred claims, noncontrolling interests, and cash to enterprise value.[12] The accounting denominator can inform the analysis, but the valuation schedule must follow actual settlement terms and avoid double counting.

### Market fit is not intrinsic truth

Empirical multiples research often defines accuracy by proximity to observed market prices. A model can therefore score well because it reproduces prevailing market pricing, even when the peer group is collectively expensive or cheap. Damodaran makes this limitation explicit: relative valuation is more likely than intrinsic valuation to track current market sentiment.[1] Dittmann and Weiner's higher valuation errors around the internet-boom period provide sample-specific evidence that regime conditions affect the method.[6]

McKinsey describes a multiple as a shorthand for the same growth, ROIC, and risk assumptions that a DCF makes explicit.[14] The implication is not that multiples should be discarded. Market evidence contains information about required returns, competitive expectations, and investor alternatives. The implication is that a trading-comps range should be reverse-engineered and cross-checked. If the selected multiple requires a margin or growth path the target cannot plausibly earn, peer pricing does not rescue the valuation.

The evidence supports a bounded conclusion. Comparable company analysis becomes more informative when peers are selected on value drivers, forward and trailing periods are separated, accounting definitions are normalized, claim perimeters match, and distributional choices are visible.[1][2][4][6][7][8] No inspected source supports treating a raw peer median as standalone intrinsic value.

## Implications

### For investors: use comparables to interrogate price, not outsource judgment

An investor should first ask what the peer range assumes. A target at 12x EBITDA may be cheaper than peers at 16x because the market has overlooked it, or because its growth, margins, reinvestment, governance, liquidity, and balance sheet are worse. The multiple alone cannot distinguish those explanations. A useful investment memo links the premium or discount to differences in value drivers and states which differences are temporary, measurable, and capable of closing.[1][14]

The author's proposed investor workflow preserves an intrinsic-value anchor.[1][14] A DCF or earnings-power model asks what the target's own cash flows support; trading comparables ask what the market currently pays for similar claims. Agreement increases confidence only when the methods do not share the same optimistic forecasts. Disagreement should trigger a bridge through growth, margin, ROIC, capital intensity, risk, net debt, market regime, and control basis. If the thesis depends on the peer group remaining expensive, the apparent margin of safety is market-relative rather than intrinsic.

The author's proposed reverse-valuation test applies the selected trading multiple, translates the resulting enterprise value into a cash-flow model, and solves for the growth, margin, reinvestment, or required return that supports it.[1][14] The test can reveal that a target appearing cheap on EV/revenue requires implausibly high future margins, or that a premium multiple is justified by superior reinvestment economics. The author's assessment is that every material comparables conclusion should be expressible as an operating expectation, not only as a ratio.

Capital structure can overturn the headline. An attractive enterprise-value range may leave little value for common equity after debt, leases, preferred claims, pensions, noncontrolling interests, and dilution. Conversely, excess cash or valuable nonoperating assets can make equity worth more than an operating multiple suggests. Investors should inspect the full enterprise-to-equity bridge and stress it at the same valuation date rather than compare share-price multiples that conceal leverage.[3][12][15]

### For analysts: make the workbook reproducible

The author's proposed reproducibility framework uses seven linked schedules. The first defines valuation date, currency, target perimeter, source hierarchy, and level of value. The second records the broad peer universe, selection criteria, exclusions, and peer tiers. The third constructs equity and enterprise value claim by claim. The fourth records reported, company-adjusted, and analyst-normalized metrics. The fifth calendarizes periods and identifies estimate vintages. The sixth calculates multiples and distribution statistics. The seventh applies selected ranges to the target and reconciles to diluted common equity.[2][12]

The author's proposed audit trail assigns every manual adjustment a source, sign, tax treatment where relevant, and explanation. Recurring costs should not disappear merely because management excludes them, and one-time gains and losses should be treated symmetrically.[9] Acquisitions and divestitures should use a common perimeter; lease, pension, stock-compensation, and intangible-investment conventions should be stated.[2][10][11][12][14][17] The raw data should remain visible so that a reviewer can reproduce the unadjusted multiple and understand how normalization changed it.

The author's proposed range-selection disclosure shows the median, quartiles, dispersion, closest peers, exclusions, and sensitivity to alternative statistics or sets.[1][7][13] If a regression supports a premium or discount, the author's assessment is that the model should disclose its sample, variables, period, fit, residual, and instability. If the sample is too small for a credible regression, a qualitative bridge is more honest than a fragile coefficient.

The author's proposed invalidation checklist includes a material earnings revision, acquisition, divestiture, refinancing, accounting restatement, peer delisting, change in fiscal-year alignment, market-regime break, or evidence that the target's business mix differs from the selected peers. Comparable company analysis is date-specific because observed prices, claims, estimates, and peer facts change.[1][2][12][16] The author's assessment is that a model that updates price but not debt, estimates, shares, and peer membership is not current.

### For boards and transaction teams: distinguish marketability from control

Boards often receive trading comparables beside precedent transactions and DCF. The methods should remain separate because they observe different levels of value. NACVA describes the guideline-public-company method's initial output as minority and marketable, while change-of-control transactions can contain different rights and deal-specific economics.[16] The author's synthesis is that a trading-comps range should not be increased by a generic control premium and a transaction-comps range should not be described as ordinary market trading evidence.

The author's proposed board-review framework exposes the initial universe, inclusion criteria, excluded firms, financial definitions, and the effect of changing the selected set.[2][12] It also distinguishes current from forward metrics and identifies whether forecasts are management, consensus, or advisor figures. The author's assessment is that a polished football field cannot replace an auditable bridge from observations to judgment.

The author's synthesis is that a diversified company may require SOTP rather than one consolidated peer set. Segment peers can capture different margins, capital intensity, growth, and risk, but corporate costs, intersegment transactions, taxes, debt, and noncontrolling interests should be reconciled once, not duplicated. Consolidated trading comparables can remain a cross-check on the SOTP result. The author's assessment is that a conglomerate discount should be explained through structure, governance, tax leakage, capital allocation, or market evidence rather than inserted as a customary percentage.

### For private-company and illiquid valuations: identify what public evidence does not transfer

Public peers supply observable prices, but a private target may differ in scale, management depth, customer concentration, access to capital, reporting quality, and marketability.[16] IVS requires analysis and documentation of material differences.[2] The author's synthesis is that the analyst should identify which difference changes expected cash flow or required return, which changes the marketability of the interest, and which is already reflected in the target metric rather than applying one automatic private-company discount.

NACVA distinguishes the marketability and control characteristics of the subject interest from the operating comparison itself.[16] The author's synthesis is that a lack-of-marketability adjustment concerns transferability and liquidity, while a control adjustment concerns rights and feasible policy changes. These effects should be evaluated against the valuation purpose and basis of value. Combining a lower target metric, a lower selected multiple, and an additional generic discount for the same risk would count the problem more than once.

The author's proposed private-company normalization controls owner compensation, related-party rent, discretionary spending, and unusual costs through a documented market-participant basis.[2][9][16] If the valuation assumes a public-market basis, the analyst should test whether the target metric includes the costs needed to operate on that basis. The author's synthesis is that forecasts and customer concentration should be tested through cash flows rather than hidden entirely in an unexplained multiple discount.

### A decision framework

The author's synthesis reduces a complete analysis to ten auditable steps. First, define target, purpose, date, currency, perimeter, and level of value. Second, assemble a broad public-peer universe. Third, score business mix, geography, scale, growth, margins, capital intensity, cyclicality, risk, accounting, liquidity, and forecast quality. Fourth, document the selected primary and secondary sets and every exclusion.[2][6][8][12][14]

Fifth, construct current diluted equity value and enterprise value using one claim convention. Sixth, build reported-to-normalized bridges and align leases, nonrecurring items, acquisitions, divestitures, and accounting definitions. Seventh, calculate separate trailing and forward panels on a common calendar basis. Eighth, inspect each observation, distribution, and outlier before choosing a statistic or weighted range.[1][7][9][10][11][12]

Ninth, apply the selected range to matching target metrics, reconcile enterprise value to diluted common equity, and test changes in net debt, dilution, normalization, and peer composition. Tenth, bridge the result to DCF, precedent transactions, SOTP, and reverse DCF, explaining differences through economics and valuation basis rather than averaging the outputs.[1][3][12][14]

The author's synthesis is that comparability must precede calculation. Market prices are observable, but the economic meaning of a multiple is constructed through definitions, selection, and judgment. A defensible comparable company analysis does not claim that peers reveal intrinsic truth. It reports what current market evidence implies under controlled assumptions, how sensitive that implication is, and which facts would make the comparison fail.

## Sources

1. Damodaran, A. "Relative Valuation." New York University Stern School
   of Business. https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/multiples.pdf [high]

2. International Valuation Standards Council. (2024). "International
   Valuation Standards, Effective 31 January 2025," red-line edition.
   https://www.icaew.com/-/media/corporate/files/technical/corporate-finance/valuation/ivs-effective-31-january-2025-redline-edition.ashx [high]

3. CFA Institute. (2026). "Market-Based Valuation: Price and Enterprise
   Value Multiples." CFA Program refresher reading.
   https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/market-based-valuation-price-enterprise-value-multiples [high]

4. Liu, J., Nissim, D., and Thomas, J. (2002). "Equity Valuation Using
   Multiples." Journal of Accounting Research, 40(1), 135-172.
   https://business.columbia.edu/sites/default/files-efs/pubfiles/318/Equity_Valuation_Using_Multiples.pdf [high]

5. Kim, M., and Ritter, J. R. (1999). "Valuing IPOs." Journal of
   Financial Economics, 53(3), 409-437.
   https://site.warrington.ufl.edu/ritter/files/2015/10/Valuing-IPOs-1998-08-18.pdf [high]

6. Dittmann, I., and Weiner, C. (2005). "Selecting Comparables for the
   Valuation of European Firms." Humboldt University SFB 649 Discussion
   Paper 2005-002. https://www.econstor.eu/bitstream/10419/25021/1/495975710.PDF [high]

7. Baker, M., and Ruback, R. S. (1999). "Estimating Industry Multiples."
   Harvard Business School working paper.
   https://www.hbs.edu/ris/Publication%20Files/EstimatingIndustry_b4e64d71-c8fd-4a5e-b31a-623d3a7d02bc.pdf [high]

8. Cooper, I., and Lambertides, N. (2023). "Optimal Equity Valuation
   Using Multiples: The Number of Comparable Firms." European Financial
   Management, 29(5), 1592-1620.
   https://lbsresearch.london.edu/id/eprint/2712/1/Euro%20Fin%20Management%20-%202022%20-%20Cooper%20-%20Optimal%20equity%20valuation%20using%20multiples%20%20The%20number%20of%20comparable%20firms.pdf [high]

9. U.S. Securities and Exchange Commission, Division of Corporation
   Finance. (2022). "Non-GAAP Financial Measures: Compliance and
   Disclosure Interpretations."
   https://www.sec.gov/corpfin/non-gaap-financial-measures [high]

10. Financial Accounting Standards Board. (2020). "FASB In Focus:
    Accounting Standards Update No. 2016-02, Leases (Topic 842)," revised.
    https://storage.fasb.org/FIF_ASU_2016-02_Leases_%28Topic_842%29_%28Rev_6-3-20%29.pdf [high]

11. International Accounting Standards Board. (2016). "IFRS 16 Leases:
    Effects Analysis."
    https://www.ifrs.org/content/dam/ifrs/project/leases/ifrs/published-documents/ifrs16-effects-analysis.pdf [high]

12. Rosenbaum, J., and Pearl, J. (2013). "Comparable Companies Analysis,"
    in Investment Banking: Valuation, Leveraged Buyouts, and Mergers and
    Acquisitions, 2nd ed. Wiley chapter excerpt.
    https://catalogimages.wiley.com/images/db/pdf/9781118472200.excerpt.pdf [medium]

13. Meitner, M. (2006). The Market Approach to Comparable Company
    Valuation. ZEW Economic Studies, Vol. 35.
    https://www.zew.de/fileadmin/FTP/economicstudies/ES_35.pdf [high]

14. Goedhart, M., Koller, T., and Wessels, D. (2005). "The Right Role for
    Multiples in Valuation." McKinsey & Company.
    https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/the-right-role-for-multiples-in-valuation [medium]

15. Financial Accounting Standards Board. (2020). "Accounting Standards
    Update 2020-06: Accounting for Convertible Instruments and Contracts
    in an Entity's Own Equity."
    https://storage.fasb.org/ASU_2020-06.pdf [high]

16. National Association of Certified Valuators and Analysts. (2016).
    "The Market Approach -- Guideline Public Company Method," Chapter Four.
    https://edu.nacva.com/BVTC/University/2015v1/Market_Approach_Writeup_2016v2_8-26-16_Final_Chapter_Four.pdf [medium]

17. Mauboussin, M. J., and Callahan, D. (2024). "Valuation Multiples:
    What They Miss, Why They Differ, and the Link to Fundamentals."
    Morgan Stanley Investment Management.
    https://www.morganstanley.com/im/en-us/individual-investor/insights/consilient-observer/valuation-multiples.html [medium]

## See Also

- `library/valuation-screening/valuation-multiples-pe-ev-ebitda-pb-analysis.md` -- explains the economic drivers and limits of common valuation multiples.
- `library/valuation-screening/enterprise-value-equity-value-reconciliation.md` -- develops the claim-by-claim bridge from operating value to diluted common equity.
- `library/valuation-screening/precedent-transaction-analysis.md` -- contrasts minority public-market evidence with negotiated change-of-control prices.
- `library/valuation-screening/sum-of-the-parts-valuation.md` -- applies distinct peer sets and valuation methods to heterogeneous business segments.
- `library/valuation-screening/reverse-dcf-and-sensitivity-analysis.md` -- tests the operating assumptions implied by a market-derived value range.

