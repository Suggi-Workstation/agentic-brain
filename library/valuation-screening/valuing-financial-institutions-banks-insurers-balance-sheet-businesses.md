---
name: valuing-financial-institutions-banks-insurers-balance-sheet-businesses
id: 20260923T053245Z
tier: library-topic
domain: valuation-screening
author: Librarian
tags: [financial-institutions-valuation, bank-valuation, insurer-valuation, price-to-book, residual-income, regulatory-capital, normalized-roe, credit-losses]
links: [library/valuation-screening/valuation-multiples-pe-ev-ebitda-pb-analysis.md, library/valuation-screening/dividend-discount-models.md, library/finance/banking-maturity-transformation.md, library/finance/insurance-underwriting-economics.md]
---

# Valuing Financial Institutions -- Capital and Liability Quality Determine What Book Value Is Worth

A bank or insurer cannot be valued reliably by treating its funding liabilities as incidental debt and its accounting equity as automatically realizable cash. The valuation task is to connect credible book equity and sustainable returns on that equity to required capital, credit or claim losses, funding behavior, and the price paid for the common claim ([1] [2] [3] [4]).

## Background

A conventional industrial valuation often starts with operating profit, subtracts reinvestment, and discounts cash available to all capital providers. This separation is awkward for a bank, whose deposits and wholesale borrowing are inputs to the product it sells, and for an insurer, whose policyholder obligations generate investable assets but also impose uncertain future claims. Damodaran explains that distinguishing operating from financing debt and estimating reinvestment and free cash flow to the firm are unusually difficult for financial services companies. His alternative is to value equity directly through dividends, distributable capital, or excess returns over the cost of equity ([3]). This is a model-selection argument, not a claim that cash flows do not matter.

The apparent simplicity of price-to-book emerged from the balance-sheet structure of financial intermediaries. The BIS notes that bank assets comprise loans, securities, derivatives, and other financial claims, making book equity a more relevant starting point than for many industrial companies. But loans at amortized cost, credit provisions, deposit franchises, off-balance-sheet commitments, and market-value movements can all separate reported book from economic worth. The BIS explicitly recommends combining book- and market-based measures rather than treating a price-to-book ratio as a verdict on its own ([1]). A discount to book can therefore signal low future profitability, understated liabilities, capital pressure, or mispricing; the observed ratio alone cannot distinguish these explanations ([1] [2]).

The intellectual bridge between a balance-sheet starting point and a forward-looking valuation is residual income. Rather than capitalize reported equity as if it were a liquidating payment, the analyst adds the present value of future earnings after charging equity for its required return. CFA Institute defines residual income as earnings minus the cost-of-equity charge on beginning book equity; the present value of these residuals added to current book value produces equity value, subject to accounting-consistency and forecasting assumptions ([4]). This gives economic meaning to the difference between price and book: an institution expected to earn less than its equity cost does not become cheap merely because its shares trade below accounting equity.

Bank capital rules created a further distinction between accounting net worth and distributable value. Basel III combines risk-weighted capital, leverage, and liquidity requirements, with jurisdiction-specific implementation and buffers that may constrain payouts even when the income statement is profitable ([11]). Damodaran treats additions to required regulatory capital as reinvestment in the equity franchise: growth that consumes capital cannot be paid out at the same time ([3]). Regulation is an input to the common-stock valuation, not a substitute for the valuation, and accounting equity is not necessarily equal to Common Equity Tier 1 or freely deployable parent capital ([3] [11]).

Credit-loss recognition changed the interpretation of reported bank earnings and equity. The US interagency statement describes the current expected credit losses approach for loans and certain other financial assets measured at amortized cost: expected losses depend on historical information, current conditions, and reasonable, supportable forecasts. An allowance reduces the carrying value of the affected asset, while changes in expected losses affect income ([5]). An analyst assessing a loan book should therefore inspect the assumptions and exposure cohorts behind the allowance, not add it back as though it were unnecessary expense. Neither a large nor a small allowance alone establishes whether the underlying assets are safe ([5]).

Insurance introduces a different estimation horizon. Policyholder premiums can arrive well before final claims are paid, creating float, but claims may develop after the initial estimate. For EU Solvency II reporting, EIOPA states that technical provisions comprise a best estimate of future obligations and a risk margin, with reinsurance recoverables calculated separately ([8]). This is not identical to every jurisdiction's accounting reserve, but it makes the economic distinction clear: expected claims are liabilities, required capital bears deviations, and investable float is not shareholder equity. A P/C insurer's underwriting and reserve development, or a life insurer's asset-liability duration mismatch, can materially change the worth of nominal book capital ([8] [9] [10]).

Interest-rate shocks make these differences visible. A rising yield can improve income on newly invested assets while reducing the market value of fixed-rate securities and altering deposit costs or insurance-liability values. The FDIC's second-quarter 2026 profile reports industry earnings, margins, and unrealized securities losses separately, illustrating why current income and economic capital cannot be read as the same signal ([6]). The Federal Reserve's review of Silicon Valley Bank documents how duration exposure, concentrated funding, and weak liquidity preparation interacted; a favorable earnings presentation did not eliminate a deteriorating balance-sheet and funding position ([7]). The valuation question is not which single ratio predicted an event, but how losses, claims, and forced financing change equity's future distributable capacity.

## Core Concepts

### Equity Is the Claim, Not a Residual after Artificial Enterprise Value

For an operating company, enterprise value is often estimated by discounting cash before interest and then subtracting financing claims. A bank's interest expense and funding balances are not merely detachable financing; they are central to the spread business. Damodaran recommends equity valuation for financial firms because separating debt from operations and measuring conventional capital expenditure and working-capital reinvestment are problematic ([3]). An insurer's policy liabilities are likewise part of the operating contract. The analyst can still value distinct fee businesses separately when justified, but should not apply an industrial EV/EBITDA bridge to all deposits or reserves as if their associated assets and income were unrelated.

A consistent equity model discounts expected distributions to common shareholders at the cost of common equity, after taxes, expected credit or claim costs, and capital retention. Its accounting starting point is common equity after carefully distinguishing preferred claims, minority interests, goodwill, and accumulated comprehensive income. An equity price divided by total consolidated equity can mix non-common capital into the denominator; a common price divided by tangible common equity is a different ratio with a different accounting base. The analysis must state which denominator it uses and reconcile it to the reported statements and regulatory capital before comparing peers ([1] [3] [11]).

### Price-to-Book Must Be Read Through Sustainable ROE

Price-to-book compares the market price of common equity with a stated book-equity measure. It is not a direct estimate of realizable sale proceeds. In an excess-return model, equity value equals current book equity plus the present value of projected residual income: RI in year t equals projected net income attributable to common minus the cost of equity times beginning book equity. Equivalently, when ROE and book equity use consistent definitions, RI equals beginning book equity times the spread between ROE and the required equity return ([3] [4]). A negative expected spread lowers justified value relative to credible book equity; a positive durable spread raises it. This relationship depends on the credibility of starting book, projected earnings, terminal residual returns, and clean reconciliation of distributions and book changes ([4]).

Normalized ROE is the return expected over a range of plausible conditions, not the latest quarter divided by an arbitrary point-in-time equity number. For banks, adjust for loan charge-offs and provisioning through a credit cycle, noninterest expense, one-time trading gains, tax changes, and deposit repricing. For P/C insurers, distinguish current accident-year underwriting from prior-year reserve releases, catastrophe experience, investment income, and the capital exposed to tail losses. For life insurers, distinguish spread income from changes in discount assumptions and policy liabilities. The author's synthesis is that equal reported ROEs are not economically interchangeable if one institution relies on correlated uninsured deposits or optimistic claims development to earn its return ([2] [7] [8] [9] [10]).

A higher ROE created by reducing the equity denominator through riskier leverage does not automatically create value. The risk to common shareholders, and therefore the required equity return, can increase as buffers narrow. The BIS study of global systemically important banks links price-to-book ratios not only to projected ROE but also to the headroom of capital above requirements ([2]). This is a reason to model both numerator and risk, rather than placing a low-multiple bank into a peer group solely because its current ROE is high.

### Distributable Capital and the Dividend Model

A dividend-discount model values distributions that common owners may actually receive. Its immediate attraction is observability of declared dividends; its weakness is that present payouts can be constrained by regulators, retained voluntarily, financed by temporary gains, or later cut. Damodaran proposes treating retained capital needed to support regulated growth as reinvestment, so the potential payout reflects earnings remaining after required capital is funded ([3]). Forecasting a bank's dividend without forecasting the balance-sheet growth and capital ratio required to sustain it double-counts the same cash.

A residual-income model can help when payout is irregular or distorted, provided earnings and book equity are measured consistently. Under suitable accounting and terminal assumptions, discounted dividends and residual income are alternate representations of the same equity claim, not two independent assets to add together ([4]). The practical triangulation is to ask whether implied value from future residual returns is consistent with dividends and buybacks that the institution can distribute while maintaining adequate capital. A terminal value based on perpetual above-cost ROE needs an explanation for why competition and regulation will not erode that excess return ([3] [4] [11]).

### Credit, Reserves, and the Quality of the Starting Book

A bank loan carried near contractual principal can be worth less if expected borrower payments deteriorate, and a security at amortized cost can have an economic loss when discount rates rise. Allowances for expected credit losses concern collectibility; market-value changes arising solely from interest rates are a different mechanism. The US interagency statement describes CECL's expected-loss measurement for covered assets and exposures, while the BIS describes how accounting measurement and provisioning complicate comparisons between bank book and market value ([1] [5]). An analyst should avoid both counting an already recognized expected loss twice and ignoring losses that accounting or regulation has not passed through common capital.

Reserve analysis starts with what is covered, not with a generic reserve-to-loans target. Segment by loan type, vintage, collateral, borrower capacity, concentration, and contractual protection; compare allowance movements with charge-offs, recoveries, and underwriting changes. A benign recent loss history is not decisive when the portfolio has grown rapidly or when the forecasts underlying expected losses have changed ([5] [7]). For insurers, distinguish claim reserves from solvency capital, and gross claim obligations from recoverables due from reinsurers. EIOPA's separate calculation of reinsurance recoverables illustrates why netting a doubtful recovery against a policyholder obligation can overstate economic equity ([8]). These are valuation adjustments to honest estimates, not allegations of fraud.

### Funding Cost, Duration, and Liquidity in the Model

A bank's deposit franchise may provide funding below prevailing market rates, but maintaining the franchise costs money and balances may leave or demand higher rates under stress. Model the yield on earning assets, interest paid on deposits and wholesale funding, noninterest costs, and credit costs separately. Stress both income repricing and the market value of longer-lived assets. The Federal Reserve's SVB review details the danger of concentrating on net-interest-income scenarios while failing to convey economic-value-of-equity risk and operational liquidity shortcomings to the board ([7]). Valuation should not assume a historically low funding cost remains unchanged after a rate shock or a loss of depositor confidence.

An insurer faces the matching problem from the opposite contractual direction: policyholders have claims at uncertain dates while invested assets generate coupon, principal, and potential sale proceeds. BIS research on life insurers describes the role of liability duration, technical provisions, low-rate reinvestment pressure, and the growth of less-liquid asset strategies ([9]). Higher asset yield is not free value if it requires taking more credit, duration, or liquidity risk against claims. For both banks and insurers, the downside case must connect asset marks, liability behavior, capital needs, and the price or availability of emergency funding rather than moving one input independently ([7] [9]).

### Multiples and Peer Selection

Price-to-earnings and price-to-book are equity multiples whose numerators and denominators refer to common owners. A bank's low P/E can reflect a temporary release of allowances or unusually favorable net interest margins; its low P/B can reflect a genuinely sub-cost ROE. A P/C insurer's superficially low earnings multiple can capitalize a year with favorable catastrophe and reserve development; a life insurer's book-value comparison may be distorted by different liability valuation and asset classification. Damodaran's financial-firm analysis relates both P/E and P/B to growth, profitability, payout, and risk rather than supplying universal sector multiples ([3]).

Comparable institutions should have similar product mix, accounting definitions, geographic exposure, underwriting or loan vintage, capital quality, and risk-bearing duration. If peers differ on these, show separate segments or a justified adjustment rather than averaging ratios. The author's assessment is that a multiple is most useful as a reverse question: what sustainable ROE, required equity return, and buffer against adverse losses would make the observed price reasonable? A screen narrows the investigation; it cannot replace the forecast of returns and liabilities that explains the multiple ([1] [2] [3] [4]).

## Evidence

### BIS Cross-Sectional Study of Bank Valuation

Caparusso, Lewrick, and Tarashev examine a panel of 31 global systemically important banks over 2014-2022. Their method relates observed price-to-book ratios to analysts' ROE forecasts, banks' capital headroom above regulatory requirements, and institution-specific characteristics. They report that higher projected ROE and a larger management buffer are associated with higher price-to-book ratios, and that the modeled factors together account for almost 90 percent of the variation in the sample. They also document that low-valued banks tend to preserve capital buffers partly by reducing risk-weighted assets and may pay out earnings while facing unfavorable reactions to large losses ([2]). This supports joint modeling of profitability and resilience; the observational association is not a guaranteed pricing law for every bank or period.

The BIS's separate 2018 Quarterly Review discussion is an institutional and accounting comparison rather than a causal test. It explains why financial assets and regulatory capital make reported bank book value more informative than industrial book value in some respects, while credit losses and differing accounting treatments keep it from being a perfect market-value measure. Its conclusion favors combining book and market metrics ([1]). Read alongside the cross-sectional study, the two sources supply both the accounting mechanism behind the ratio and evidence that a specific profitability-and-capital interpretation has empirical content, without treating any market price as an intrinsic-value proof.

### An Official US Bank-Industry Cross-Check

The FDIC's second-quarter 2026 Quarterly Banking Profile aggregates regulatory reports from insured institutions and separately reports profits, funding, net interest margins, credit indicators, capital, and unrealized securities losses. It reports a second-quarter return on assets of 1.37 percent and quarterly net income of $90.1 billion, while noting that unrealized losses on investment securities remained elevated ([6]). The method is an industry-wide descriptive profile, not a company-level fair-value appraisal. Its evidentiary use in a model is to demonstrate that current profitability can coexist with unrealized balance-sheet losses; aggregate strength says nothing conclusive about a particular bank's duration, depositor mix, loan cohorts, or stock price.

The Federal Reserve's 2023 investigation of Silicon Valley Bank adds an institution-specific case. It reviewed internal governance and supervisory records, liquidity plans, and interest-rate-risk metrics. It found failures in management and board risk oversight, concentrated uninsured funding, long-duration exposure, and weaknesses in mobilizing liquidity. The report also showed that estimated full liquidity-coverage ratios under the pre-2019 regime would have fallen below the specified full requirement in the period before failure; these are supervisory counterfactual estimates, not ratios the bank actually reported under that regime ([7]). The case tests a valuation stress scenario: realized funding pressure can force losses and constrain new capital precisely when an earnings multiple appears superficially attractive. It does not show that every bank with unrealized securities losses is insolvent.

### Insurance Liability Evidence

EIOPA's Solvency II Article 77 specifies how technical provisions are calculated: a best estimate using projected obligations and a separate risk margin, with reinsurance recoverables accounted for separately. This is a rule for the relevant regime rather than an observed stock-return study ([8]). It supports a disciplined valuation bridge from gross policy liabilities to net economic equity and cautions against identifying gross float with distributable common capital. The rule does not make a best estimate certain or make capital above the minimum risk-free.

BIS researchers' 2024 analysis of life insurers combines sector balance-sheet evidence with a mechanism study of rate-sensitive liabilities, investment portfolios, and asset-intensive reinsurance. They describe the dominance of technical provisions in life-insurer liabilities and the shift toward private assets and reinsurance arrangements under pressure to sustain returns. Their finding is that apparent capital relief and higher asset yields may bring additional leverage, liquidity, and network risks, not an automatic addition to common-stock value ([9]). The unit of analysis and legal treatment differ from P/C underwriting; applying the life-insurance mechanism to every insurer without checking product mix would be an error.

Berkshire Hathaway's 2025 annual report provides a company disclosure case, not a representative industry sample. Its insurance discussion reports separate underwriting results, investment income, insurance liabilities and float; it reports a property-and-casualty combined ratio of 87.1 percent for 2025, with retroactive reinsurance excluded from that measure ([10]). The method is issuer financial reporting with segment explanations; it shows why a multiple of consolidated net income or the face amount of float cannot isolate normalized underwriting returns or policyholder obligations. Berkshire's diversified non-insurance businesses also mean that its consolidated P/B cannot be used as an insurer-only comparison without separating the other segments ([10]).

### Capital and Credit-Estimate Evidence

The US interagency CECL statement is an official measurement and governance document. Its method instructs institutions to estimate expected losses with past experience, present information, and reasonable and supportable forecasts; it covers relevant amortized-cost assets and specified commitments. This establishes which inputs are already embedded in reported loan allowances and which need stress testing by an investor ([5]). The Basel Committee's evaluation of the Basel III reforms discusses the multi-dimensional capital and liquidity framework, giving a separate reason why forecast earnings are not necessarily fully distributable ([11]). Neither document establishes a universal fair P/B; both delimit the inputs an honest model must reconcile before interpreting one.

These sources also define different kinds of uncertainty. The interagency policy concerns estimates of eventual borrower payment, whereas the Basel assessment concerns the capacity to absorb loss and sustain funding under multiple constraints. A model that improves its expected-loss forecast but ignores capital consumption from new lending has only addressed the first question. Conversely, a generous capital buffer does not prove that the loan book is correctly priced or reserved. The author's synthesis is to record separately the forecast credit loss, the accounting allowance already recognized, the incremental capital needed for growth or adverse outcomes, and any change in the required equity return. Each has a distinct place in the book-to-value bridge; collapsing them into a single arbitrary discount to book hides whether a loss has been recognized once, twice, or not at all ([3] [5] [11]).

## Implications

### For a Long-Term Equity Investor

Begin with common equity attributable to the security being purchased. Reconcile the reported figure with tangible common equity, unrealized asset marks where relevant, credit or claim estimates, noncontrolling and preferred claims, and capital trapped in regulated subsidiaries. This is not a mechanical instruction to subtract every unrecognized securities loss from book while ignoring offsets: liability values, tax effects, realization paths, hedges, and funding behavior may change the economic result ([1] [5] [7] [8]). The author's synthesis is to present both reported and stressed common equity, with each adjustment identified once and its source specified.

Forecast normalized, not merely current, earnings. For a bank, build interest income, deposit and wholesale funding expense, fee income, operating expense, expected credit losses, and tax; compare normalized ROE with the cost of common equity and specify how much profit must be retained to maintain a credible capital buffer. For an insurer, build sustainable underwriting and investment results against the gross and net claim obligations, asset mix, reserve uncertainty, and capital consumed by tail risk ([3] [4] [5] [8] [10]). If an investment thesis depends on returns that appear only when reserves are released or credit cost is temporarily benign, identify that dependence rather than inserting the year into a perpetuity.

Use a range rather than a single target. A base case may assume stable funding, reasonable claim or credit development, and a defensible long-term ROE. An adverse case should allow losses, runoff or claims, higher funding costs, lower asset realizations, and a period of reduced dividends to interact. A favorable case can recognize an economically supported franchise only after costs and capital retention are included. These cases are the author's scenario-design synthesis of the bank study, supervisory case, insurance discussion, and residual-income framework; their probabilities are analyst judgments, not historical frequencies furnished by those sources ([2] [4] [7] [9]).

Finally, compare the market price with the modeled values and ask what future ROE and capital resilience the price implies. The BIS bank study provides evidence that the market considers both profitability and buffer size; it does not tell an investor that every low-P/B security offers a margin of safety ([2]). A discount to reported book is only meaningful if that book is credible and the institution can earn its equity cost without unacceptable risks. The method's value-investing discipline is to identify what can be lost before assuming an accounting discount is a bargain; this is an application of the model, not a prediction of any individual security.

### For Credit Analysts and Financial-Institution Boards

An equity valuation differs from a creditor's repayment test, but both require the same reconciliation of loss estimates, funding timing, and capital quality. Credit analysts should compare reported loss absorption with severe but plausible joint shocks rather than treating a profitable quarter as proof of solvency. The Federal Reserve's SVB review shows why collateral accessibility and outflow speed matter alongside nominal asset values, while the interagency CECL statement shows why expected borrower loss should be included before presenting book equity as protection ([5] [7]). A creditor may require a safer outcome than common equity holders because its upside is contractually limited; that distinction should appear in the valuation scenario, not be lost in a shared ratio.

Boards using share price or P/B as a performance measure should not optimize the ratio by increasing risk or cutting buffers indiscriminately. The BIS panel links valuation to both expected ROE and capital headroom, so shrinking the denominator without safeguarding resilience can erode the basis for a higher multiple ([2]). For insurers, a management decision to chase investment yield or cede policies to free capital should be assessed alongside retained exposure, counterparty recovery, policyholder liabilities, and the duration of supporting assets ([8] [9]). These are tests of the value of a capital-allocation decision, not a restatement of banking or insurance regulatory doctrine.

### For Screening and Model Governance

A first-pass screen can flag low P/B with adequate normalized ROE, sound buffers, transparent reserve development, and manageable duration and funding risk. Every metric needs a definition and comparable denominator. A bank P/B on total equity should not be compared unadjusted with a peer's tangible-common P/B; a life insurer cannot be screened against a P/C writer solely on reported combined ratio; and an EV/EBITDA figure that treats deposits as ordinary corporate debt is not a shortcut to equity value ([1] [3] [8] [10]). The screen produces research candidates, not buy decisions or a cross-sector league table.

Model governance requires tracing each forecast into subsequent disclosures. For banks, compare predicted deposit costs, credit-loss vintages, securities marks, and capital retention with realized outcomes; revise assumptions when evidence changes. For insurers, track underwriting cohorts and reserve development across years and check that the cash-flow duration assumed for investments remains compatible with claim payments. A residual-income forecast should roll forward beginning book equity through comprehensive income and distributions consistently, while explicitly identifying material deviations from a simple clean-surplus relation ([4] [5] [8]). Without that reconciliation, apparent agreement between dividend and residual-income models may be an accounting coincidence.

The worst valuation error is to count a liability-created funding benefit as free equity while leaving out the adverse scenario in which the liability must be paid or refinanced. The author's synthesis is therefore sequential: verify the starting common book, estimate normalized after-loss ROE, deduct the capital needed to sustain that ROE, test the joint asset-liability stress, and only then decide whether the market price offers compensation for the remaining uncertainty ([1] [3] [4] [7] [8]). This keeps the subject in security valuation: policy rules, macro forecasts, portfolio weights, and issuer biographies supply context only when they change those valuation inputs.

## Sources

1. Bank for International Settlements (2018). "Bank valuation and price-to-book
   ratios (PBRs)." BIS Quarterly Review, March 2018.
   https://www.bis.org/publications/bank-valuation-and-price-to-book-ratios-pbrs [high]

2. Caparusso, J., Lewrick, U., and Tarashev, N. (2023). "Profitability,
   valuation and resilience of global banks - a tight link." BIS Working
   Papers No. 1144.
   https://www.bis.org/publications/working-paper-1144-profitability-valuation-and-resilience-global-banks-tight-link [high]

3. Damodaran, A. (2009). "Valuing Financial Service Firms." NYU Stern.
   https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/finfirm09.pdf [high]

4. CFA Institute (2026). "Residual Income Valuation." CFA Program
   Refresher Readings.
   https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/residual-income-valuation [high]

5. Federal Deposit Insurance Corporation and US federal financial
   regulators (2020). "Interagency Policy Statement on Allowances for
   Credit Losses."
   https://www.fdic.gov/news/financial-institution-letters/2020/interagency-policy-statement-allowances-credit-losses [high]

6. Federal Deposit Insurance Corporation (2026). "FDIC Quarterly Banking
   Profile Second Quarter 2026," statement on results.
   https://www.fdic.gov/news/speeches/2026/fdic-quarterly-banking-profile-second-quarter-2026 [high]

7. Board of Governors of the Federal Reserve System (2023). "Review of
   the Federal Reserve's Supervision and Regulation of Silicon Valley Bank."
   https://www.federalreserve.gov/publications/files/svb-review-20230428.pdf [high]

8. European Insurance and Occupational Pensions Authority. "Solvency II
   Single Rulebook, Article 77: Calculation of technical provisions."
   https://www.eiopa.europa.eu/rulebook/solvency-ii-single-rulebook/article-2160_en [high]

9. Bank for International Settlements (2024). "Shifting landscapes: life
   insurance and financial stability." BIS Quarterly Review, September.
   https://www.bis.org/publications/qr-202409/shifting-landscapes-life-insurance-and-financial-stability [high]

10. Berkshire Hathaway Inc. (2025). "2025 Annual Report," insurance
    operations, liabilities, and investments.
    https://www.berkshirehathaway.com/2025ar/2025ar.pdf [high]

11. Basel Committee on Banking Supervision (2022). "Evaluation of the
    impact and efficacy of the Basel III reforms."
    https://www.bis.org/bcbs/publ/d544.pdf [high]

## See Also

- `library/valuation-screening/valuation-multiples-pe-ev-ebitda-pb-analysis.md` -- the general framework for interpreting equity multiples.
- `library/valuation-screening/dividend-discount-models.md` -- the distributable-cash alternative to a residual-income model.
- `library/finance/banking-maturity-transformation.md` -- the asset-liability mechanism behind a bank's valuation risk.
- `library/finance/insurance-underwriting-economics.md` -- the claim-cost and reserve inputs to an insurer valuation.
