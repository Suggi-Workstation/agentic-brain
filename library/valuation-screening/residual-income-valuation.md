---
name: residual-income-valuation
id: 20260930T233514Z
tier: library-topic
domain: valuation-screening
author: Librarian
tags: [residual-income-valuation, abnormal-earnings, clean-surplus-accounting, book-value, return-on-equity, economic-profit, price-to-book]
links: [library/valuation-screening/discounted-cash-flow-dcf-methodology.md, library/valuation-screening/dividend-discount-models.md, library/valuation-screening/cost-of-capital-capm-wacc-erp.md, library/valuation-screening/valuation-multiples-pe-ev-ebitda-pb-analysis.md, library/valuation-screening/valuing-financial-institutions-banks-insurers-balance-sheet-businesses.md]
---

# Residual Income Valuation Prices Equity Through Book Value and Forecast Economic Profit

Residual income valuation estimates common equity as current book equity plus the present value of future earnings after charging shareholders for the capital already committed. The method does not create a different source of value from dividends or free cash flow; under consistent accounting and forecasts, it reorganizes the same equity claim so that recorded book value is recognized now and only future economic profit must be forecast.[1][2][3]

## Background

Conventional accounting subtracts interest expense before reporting net income but does not subtract a charge for common equity capital. A company can therefore report positive net income while earning less than shareholders require for the risk they bear. Residual income corrects that omission analytically: it subtracts an equity charge, equal to the required return on common equity multiplied by beginning common book equity, from earnings attributable to common shareholders. The remainder is also called abnormal earnings or economic profit because it measures profit beyond the opportunity cost of the equity base.[1]

The modern accounting-based valuation framework is associated especially with James Ohlson and with Gerald Feltham and James Ohlson. Ohlson's 1995 model relates market value to contemporaneous and future earnings, book values, and dividends. Its two accounting foundations are that the clean-surplus relation holds and that dividends reduce book value without affecting current earnings. Feltham and Ohlson separately model operating and financial activities and show how, under clean-surplus accounting, a dividend-discount representation can be restated in terms of book value and future abnormal earnings.[2][3]

Clean surplus is the roll-forward identity that connects the income statement, dividends, and common book equity:

`B_t = B_(t-1) + E_t - D_t`

Here `B_t` is ending common book equity, `E_t` is earnings attributable to common shareholders, and `D_t` is net distributions to common shareholders. Capital contributions and repurchases require explicit treatment rather than being hidden inside dividends. If all non-owner changes in common equity pass through the earnings measure used in the model, the dividend-discount model can be algebraically transformed into residual income valuation. The transformation does not depend on the market assigning book value its accounting amount; book value is the recorded capital base from which the model measures future excess returns.[2][3][8]

That reorganization changes where value appears in a finite forecast. A dividend model may recognize little value during the explicit period when a company retains cash. A free-cash-flow model may likewise place much of value in a terminal estimate when current investment depresses distributable cash. Residual income begins with book equity and forecasts the spread between return on equity and the required equity return. It can therefore recognize value earlier when earnings and book value are forecast more reliably than payout or free cash flow. The models remain theoretically equivalent only when their earnings, distributions, financing, accounting roll-forwards, discount rates, and terminal assumptions describe the same business.[1][4][5]

The method is particularly relevant when common book equity is economically interpretable, dividends are not representative of distributable capacity, or free cash flow is negative or difficult to forecast. Financial institutions are a common application because equity capital is both visible and operationally important, although reported book still requires analysis of credit losses, reserves, asset marks, regulatory constraints, and non-common claims. The method is less reliable when book equity is severely distorted, when expected clean surplus cannot be reconstructed, or when future earnings are no easier to forecast than cash flow.[1]

Residual income also has an enterprise-level relative, economic value added. Equity residual income subtracts an equity charge from net income attributable to common owners and discounts the result at the cost of equity. Economic value added ordinarily subtracts a capital charge from after-tax operating profit and uses invested capital and a cost of capital. Damodaran shows that the present value of future economic value added can reconcile to discounted-cash-flow value when capital, operating profit, reinvestment, and discount rates are defined consistently. He also warns that accounting capital and operating income often require adjustments for research and development, leases, one-time items, and goodwill before the measure represents economic investment and return.[1][10]

Residual income is therefore neither an accounting shortcut nor a license to treat book value as intrinsic value. It is a valuation identity implemented through forecasts. Its practical advantage is that it turns the gap between market value and book value into an explicit claim about future excess returns. Its practical danger is the same feature: a distorted starting book, optimistic earnings, or an unjustified assumption that above-cost returns persist can make the model appear anchored while the forecasted premium remains speculative.[1][7][8]

## Core Concepts

### Equity residual income and the valuation identity

For common equity, residual income in period `t` is:

`RI_t = E_t - r * B_(t-1)`

The same quantity can be written as:

`RI_t = (ROE_t - r) * B_(t-1)`

where `r` is the required return on common equity and `ROE_t` is earnings divided by beginning common book equity. Intrinsic common-equity value at time zero is:

`V_0 = B_0 + sum[RI_t / (1 + r)^t]`

The first term is the current common book equity recognized immediately. The second term is the present value of expected future earnings above or below the equity charge. Positive residual income adds value above book; negative residual income subtracts value. If expected `ROE` equals the cost of equity in every future period and the starting book is measured consistently, value equals book under the model.[1][2]

The equity charge is not an accounting expense reported in net income. It is an opportunity-cost deduction imposed by the valuation analyst. Its rate must match the common-equity claim, currency, inflation basis, and risk of the forecast earnings. Using WACC in an equity residual-income model mixes an enterprise discount rate with a common-equity earnings measure. Conversely, an enterprise economic-profit model can use after-tax operating profit, invested capital, and a cost-of-capital charge, but its output is enterprise value and still requires a complete bridge to common equity.[1][10]

### Why clean surplus produces equivalence

Begin with the dividend-discount identity, under which equity value is the present value of expected net distributions. Substitute the clean-surplus relation, rearranged as `D_t = E_t - (B_t - B_(t-1))`, into that dividend stream. The change in book equity telescopes through the discounted series: current book value remains as the starting stock, while each future earnings amount is reduced by the required return on the opening book base. The result is current book equity plus discounted residual income.[2][3]

This derivation supplies a control for model builders. A residual-income valuation and a dividend valuation should converge when both use the same earnings, book-value roll-forward, net distributions, cost of equity, forecast horizon, and terminal state. A difference is diagnostic evidence that at least one input is inconsistent. It may arise from omitted repurchases, new share issuance, other comprehensive income, a different terminal assumption, or a book-value forecast that does not reconcile with earnings and distributions. Averaging inconsistent outputs hides the error instead of resolving it.[1][4][8]

Clean surplus should be tested at the aggregate common-equity level before it is applied per share. Ohlson's later critique notes that expected changes in shares outstanding can break a naive per-share clean-surplus relation and that new shareholders can receive or surrender value when capital is raised on non-neutral terms. A model that forecasts EPS and book value per share while ignoring repurchase prices, option exercises, employee awards, or discounted equity issuance can therefore violate the condition that makes the valuation identity work.[8]

### Forecast book equity, earnings, and distributions as one system

The explicit forecast should begin with common book equity attributable to the security being valued. Preferred equity, noncontrolling interests, and other senior or outside claims do not belong in that base unless the earnings measure and final value also include them. Forecast net income attributable to common, then forecast dividends, repurchases, issuance, and other owner transactions. Ending book equity should be calculated from those flows rather than inserted independently.[1][8]

ROE is useful because it makes the economic spread visible, but it is not a standalone forecast. A high ROE can reflect genuine pricing power and low reinvestment needs, or it can reflect leverage, write-downs, an understated asset base, one-time income, or repurchases that shrink book equity. The analyst should forecast the income statement and equity roll-forward first, then use `ROE - r` as a diagnostic of value creation. If ROE improves only because the denominator was impaired or bought back, the residual-income path may not represent improved operating economics.[1][8][10]

Growth also requires a consistent retention policy. Under a simplified clean-surplus steady state with no new equity issuance, growth in book equity follows retained earnings. A model cannot simultaneously assume high distributions, rapid book growth, and unchanged ROE without identifying another source of capital. The correct sequence is to forecast earnings, net distributions, and book equity together, then calculate residual income from the resulting beginning book base.[1][2]

### A worked five-year fade example

Consider an illustrative company with beginning common book equity of 100, a 10 percent required return on equity, and a 40 percent dividend payout. Assume ROE fades from 15 percent in year 1 to 11 percent in year 5 and equals the 10 percent cost of equity thereafter. The following calculations use `RI_t = (ROE_t - 10%) * B_(t-1)` and clean surplus; amounts are rounded from tool-calculated values.

| Year | Beginning book | ROE | Earnings | Dividends | Residual income | Present value of RI | Ending book |
|:--|--:|--:|--:|--:|--:|--:|--:|
| 1 | 100.00 | 15% | 15.00 | 6.00 | 5.00 | 4.55 | 109.00 |
| 2 | 109.00 | 14% | 15.26 | 6.10 | 4.36 | 3.60 | 118.16 |
| 3 | 118.16 | 13% | 15.36 | 6.14 | 3.54 | 2.66 | 127.37 |
| 4 | 127.37 | 12% | 15.28 | 6.11 | 2.55 | 1.74 | 136.54 |
| 5 | 136.54 | 11% | 15.02 | 6.01 | 1.37 | 0.85 | 145.55 |

Because ROE equals the required return after year 5, continuing residual income is zero in this illustration. Value is therefore 100 plus 13.40 of present-valued explicit residual income, or 113.40. The example shows why book growth is not automatically value creation: book equity rises to 145.55, but each retained dollar creates less incremental value as the ROE spread fades.[1][2]

The example is a calculation, not evidence that five years, a 40 percent payout, or linear fade fits any company. A real model must derive the fade from competition, regulation, asset duration, customer economics, and reinvestment opportunities. It should also use scenarios when ROE can change discontinuously. The author's assessment is that the fade assumption is the residual-income counterpart of a DCF terminal margin and return-on-capital assumption: it often determines more value than the explicit arithmetic reveals.[1][7]

### Continuing residual income and persistence

A finite forecast needs a continuing-value assumption because companies do not ordinarily stop earning at the horizon. Common treatments include: zero continuing residual income; residual income that persists at the horizon level; residual income that grows at a rate below the cost of equity; or residual income that fades toward zero according to an explicit persistence process. Each treatment embeds a claim about how long `ROE - r` survives.[1][7]

Zero continuing residual income assumes competition or regulation drives ROE to the required return at the horizon. Perpetual residual income assumes the existing spread survives without decay. A growing-residual-income perpetuity requires `g < r` and must reconcile growth with retained equity and future ROE. An explicit fade model is often more transparent because it separates the current spread, the speed of erosion, and the mature spread. Extreme current ROE, unusual accruals, one-time charges, weak barriers to entry, and short-lived assets generally argue for faster fade; durable customer relationships, regulatory franchises, network effects, or scarce assets can support slower fade only when evidence shows that competitors cannot replicate the returns.[1][7]

A terminal value should be written in residual-income terms rather than imported from an unrelated multiple without reconciliation. If year `T+1` residual income grows at constant `g`, continuing value at `T` is `RI_(T+1) / (r - g)`. If residual income fades geometrically instead, the denominator and forecast must reflect the chosen persistence process. Whichever method is used, the terminal assumption must agree with terminal ROE, book growth, distributions, and cost of equity. A model that assumes both persistent high ROE and a price-to-book multiple based on mature peer economics can count the same optimism twice.[1][3][7]

### The justified price-to-book connection

Residual income gives price-to-book an economic interpretation. Divide the valuation identity by current book equity: the premium or discount to book is the present value of future residual income scaled by book. A company expected to earn ROE above its cost of equity should trade above a credible book value; a company expected to earn below its cost should trade below book; equality of ROE and required return implies price equal to book in the stable simplified case.[1][11]

For a constant-growth company with internally consistent payout and growth, a common justified relation is:

`P_0 / B_0 = (ROE - g) / (r - g)`

This formula is not a universal fair-multiple table. It assumes a stable ROE, cost of equity, growth rate, and clean-surplus relation. Its analytical value is inversion. Given a market price-to-book ratio and an estimated required return, the analyst can solve for the ROE spread or residual-income growth the price implies, then compare that requirement with normalized profitability and competitive evidence.[1][11]

The relation also explains why low P/B is not sufficient evidence of cheapness. A discount can be justified by expected sub-cost ROE or by an overstated book base. A high P/B can be justified by durable positive residual income or can reflect an optimistic persistence assumption. Screening should therefore pair P/B with book-quality tests, normalized ROE, cost of equity, and an explicit fade horizon.[1][11]

### Accounting adjustments determine the starting anchor

Residual income recognizes current book equity immediately, so errors in that anchor enter value at full weight unless corrected. The analyst should reconcile common equity for preferred claims, noncontrolling interests, accumulated other comprehensive income, asset write-downs, pension or insurance measurements, and other items that affect the equity attributable to common owners. The earnings forecast must use the same perimeter. An adjustment to book without a corresponding adjustment to future earnings or distributions can create a second inconsistency.[1][2]

Write-offs require special care. An impairment can reduce book equity and current earnings while leaving future reported ROE mechanically higher because the denominator is smaller. Adding the write-off back to earnings while retaining the reduced book value can overstate residual income. A consistent model either accepts the write-down and forecasts returns on the new base, or reconstructs an adjusted asset and equity base and reverses related earnings effects. The objective is not to erase unfavorable accounting but to prevent the same economic loss from being omitted or counted twice.[1][10]

Repurchases also change both ownership and the book base. A repurchase below book can raise book value per remaining share, while a repurchase above book can reduce it; neither mechanical effect alone proves value creation or destruction. The economic result depends on the price paid relative to value and on the financing source. Aggregate equity modeling is safer when repurchase prices, shares retired, employee issuance, option exercises, and new capital are material. Per-share residual income should be derived only after those transactions reconcile.[8]

Goodwill and acquired intangibles can make book equity acquisition-dependent. Internally generated goodwill is not recognized as an asset under IAS 38, while acquired identifiable intangibles can be recognized in a business combination under applicable criteria. IAS 38 also expenses research expenditure and capitalizes qualifying development expenditure. Two economically similar firms can therefore report different book equity and earnings because one built an asset internally and another acquired it. A residual-income comparison should identify that asymmetry and, where evidence supports it, construct an adjusted capital base and matched amortization or expense schedule rather than adding an invented intangible value without a reliable cost or life.[9][10]

Other comprehensive income and direct-to-equity items matter because clean surplus requires all non-owner changes in equity to appear in the comprehensive earnings measure used by the model. The practical repair is a forecast roll-forward that begins with reported common equity and separately tracks net income, OCI, dividends, repurchases, issuance, and other direct equity changes. If a recurring item bypasses net income, the model can use comprehensive income or add the item to the residual-income forecast and book roll-forward consistently. Ignoring it breaks the algebra even if the spreadsheet balances.[2][8]

### Residual income, DDM, FCFE, DCF, and EVA answer different implementation questions

Dividend discounting is direct when payout policy is representative and forecastable. FCFE is useful when cash available to equity can be forecast after reinvestment and debt financing. FCFF DCF values operations for all capital providers and requires an enterprise-to-equity bridge. Residual income is useful when book equity and accrual earnings are more informative than near-term cash distributions. EVA applies a related excess-return logic at the enterprise or project level.[1][4][5][10]

No method wins by identity alone. Under complete and consistent forecasts, dividend, cash-flow, and residual-income representations converge. In finite practice, they differ because the analyst can forecast some attributes more reliably than others and because terminal values recognize the unforecast portion differently. Penman and Sougiannis and Francis, Olsson, and Oswald provide evidence that accrual-earnings approaches produced lower finite-horizon valuation errors in their tested designs, but those results do not make accounting numbers immune to distortion or residual income universally superior.[4][5]

A disciplined analyst uses the representation that makes the uncertain economics most visible and then reconciles it with at least one alternative. For a bank, residual income and DDM may expose capital retention and ROE. For an industrial company, FCFF may expose reinvestment more directly, while residual income tests whether forecast accounting returns exceed the equity charge. For an intangible-intensive company, adjusted residual income can be informative only if the adjustment to book and earnings is supportable. The author's assessment is that model selection should minimize hidden terminal assumptions, not maximize the value estimate.[1][4][9][10]

## Evidence

### Ohlson establishes the accounting-based valuation benchmark

Ohlson's 1995 paper develops a model relating market value to earnings, book values, and dividends. Its method begins from two owners' equity accounting constructs: clean surplus, and the treatment of dividends as reductions in book value rather than current earnings. The result provides a benchmark in which current book value and expected future residual income organize the valuation information. This is theoretical evidence for the identity, not an empirical guarantee that reported book and forecast earnings are measured without error.[2]

Feltham and Ohlson extend the framework by distinguishing operating and financial activities. Their model assumes market value equals the present value of expected future dividends and shows how clean-surplus accounting supports a book-value-plus-residual-income representation. The distinction matters because operating assets can be conservatively recorded while financial assets and liabilities can behave differently under accounting measurement. The paper supports separate modeling of operating and financing effects rather than treating all book-value deviations as one homogeneous bias.[3]

### Penman and Sougiannis test finite-horizon truncation

Penman and Sougiannis compare dividend discount, discounted cash flow, and accrual-earnings valuation techniques under finite forecast horizons. They use average ex post payoffs over alternative horizons, with and without terminal values, and compare the resulting estimates with ex ante market prices to measure the error introduced by truncating forecasts that theoretically extend to infinity. They report lower valuation errors for accrual-earnings techniques than for cash-flow and dividend-discount techniques in their tests and identify accounting conditions under which each method requires a longer forecast horizon.[4]

The bounded conclusion is that residual-income-style accrual accounting can reduce finite-horizon dependence when book value recognizes a substantial part of value and earnings are forecastable. The study does not show that residual income is intrinsically more correct under inconsistent accounting, or that market price is a perfect measure of intrinsic value. It shows that the location of value recognition matters when practical forecasts stop after a few years.[4]

### Francis, Olsson, and Oswald compare forecast-based estimates

Francis, Olsson, and Oswald compare discounted dividends, discounted free cash flow, and discounted abnormal earnings using a large sample of Value Line forecasts. The CFA Institute digest reports 2,907 companies drawn from third-quarter Value Line reports for 1989 through 1993, with forecast data through a five-year horizon and terminal values calculated under zero-growth and 4 percent growth specifications. Accuracy is measured by absolute deviations from observed prices, and explainability by cross-sectional price variation.[5]

Abnormal-earnings estimates have smaller absolute deviations from observed prices and explain more price variation than the dividend and free-cash-flow estimates in that design. The authors attribute the relative performance to the sufficiency of book equity as a measure of part of intrinsic value and to greater precision and predictability in abnormal-earnings forecasts. The result supports residual income as a useful finite-horizon representation; it does not establish that the observed price is true value or that the ranking survives every sample, accounting regime, and forecast source.[5]

### Frankel and Lee test residual-income value against price and returns

Frankel and Lee estimate firm fundamental values using I/B/E/S consensus forecasts in a residual-income model. Their peer-reviewed study reports that the resulting value estimates are highly correlated with contemporaneous prices and that the value-to-price ratio predicts long-horizon cross-sectional returns. They also report that the effect is not explained by market beta, book-to-price, or market capitalization and that predictable analyst-forecast errors can improve the signal.[6]

This evidence supports two uses: residual income as a valuation framework and value-to-price as a screening variable. It does not prove that every high value-to-price company is mispriced or that analyst forecasts are unbiased. The study itself identifies forecast errors as predictable, which means the model's apparent precision depends on correcting rather than merely importing consensus expectations.[6]

### Dechow, Hutton, and Sloan test the information dynamics

Dechow, Hutton, and Sloan empirically assess Ohlson's residual-income model relative to competing accounting-based approaches. Their analysis emphasizes that many applications of residual income are restatements of the dividend-discount model and that Ohlson's distinctive empirical content comes from the assumed information dynamics for residual income and other information. They conclude that the framework is parsimonious for combining earnings, book value, and earnings forecasts, while their tests also show that specifying persistence is an empirical problem rather than a free assumption.[7]

For practice, this means the fade parameter should not be selected merely because a closed-form terminal value requires one. Persistence must be tied to firm and industry evidence, forecast horizon, accounting quality, and competitive conditions. The author's synthesis is that the information-dynamics evidence strengthens the method as a disciplined forecast structure while weakening any claim that one universal persistence factor can be applied across companies.[7]

### Ohlson's later critique defines the share-count boundary

Ohlson's 2000 critique identifies three problems in applying residual-income valuation to equity. It argues that per-share clean surplus generally fails when shares outstanding are expected to change, that new shareholders can receive a net benefit from capital contributions, and that generally accepted accounting can violate clean surplus when some capital contributions are not recorded at market value. The paper proposes focusing on expected EPS adjusted for dividends as an alternative in those settings.[8]

The evidence is conceptual rather than a return study, but it supplies an important falsification test. A residual-income model that ignores buybacks, employee issuance, conversions, or below-value capital raising can be algebraically wrong even if its forecast earnings are reasonable. The repair is to model aggregate common equity and owner transactions explicitly or to use a per-share framework that fully reconciles them.[8]

### Accounting standards and EVA practice show why adjustments are necessary

IAS 38 does not recognize internally generated goodwill, expenses research expenditure, and recognizes qualifying development expenditure under specified criteria. It also treats acquired identifiable intangibles differently from many internally generated items. These rules establish a real source of book-value asymmetry between builders and acquirers. They do not tell the analyst what an unrecognized brand, data asset, or research program is worth; an adjustment remains a valuation estimate that must be tied to identifiable spending, useful life, and future benefit.[9]

Damodaran's EVA treatment reaches the same practical issue from valuation rather than standard setting. He identifies book capital as a proxy shaped by historical depreciation, inventory, acquisition, lease, and R&D accounting, recommends matched adjustments to capital and operating income, and notes that some book values are too flawed to repair without rebuilding invested capital from the assets. He also demonstrates the equivalence between discounted economic value added and discounted cash flow under consistent assumptions.[10]

Together, the evidence supports a conditional verdict. Residual income can reduce terminal-value dependence and organize the relation among book value, earnings, and required return. Its advantage is strongest when the starting book and forecast earnings carry reliable information. The same reliance becomes a weakness when accounting recognition, owner transactions, or persistence assumptions are not reconciled.[1][4][5][8][9][10]

## Implications

### For fundamental investors

Start by asking whether common book equity is a useful economic anchor. Reconcile reported equity to the common claim, inspect the sources of accumulated OCI, write-offs, goodwill, acquired intangibles, pension or insurance measurements, and off-balance-sheet obligations, and determine which adjustments can be supported. If the starting book cannot be made interpretable, a residual-income model may be less transparent than FCFF, asset value, or scenario analysis. A low P/B ratio is not a substitute for this work.[1][9][10][11]

Next, forecast normalized earnings and book equity together. Separate recurring operating earnings from one-time items, but do not add a loss back while retaining a balance-sheet reduction that makes future ROE look better. Track dividends, repurchases, issuance, and share-based claims explicitly. Compute residual income only after the earnings perimeter, book base, and cost of equity refer to the same owners. This sequence prevents the model from manufacturing excess returns through inconsistent accounting.[1][8][10]

Then invert the market price. Subtract current adjusted book equity from market equity value; the difference is the present value of residual income that the market price requires under the model. Solve for a supportable combination of normalized ROE, fade duration, book growth, and required return. The question becomes: what economic spread must the business sustain, for how long, to justify the premium or discount to book? This is more diagnostic than declaring a P/B ratio high or low without identifying its embedded profitability assumptions.[1][11]

Use multiple scenarios. A base case can forecast a gradual fade in ROE. A downside case should connect weaker profitability with write-downs, slower book growth, financing needs, and a possibly higher required return rather than moving one cell in isolation. An upside case should identify the reinvestment and competitive mechanism that preserves above-cost ROE. The author's assessment is that the worst-case residual-income error is to recognize book value at full weight and then capitalize an accounting spread that cannot survive competition or correction.[1][7][10]

### For financial institutions and other balance-sheet businesses

Residual income is often well suited to banks and insurers because book equity, regulatory capital, and returns on equity are central to distributable capacity. That suitability is conditional. Loan allowances, securities marks, insurance reserves, reinsurance recoverables, capital trapped in subsidiaries, and required buffers can separate reported book from value available to common owners. Forecasted ROE must include normalized credit or claim costs and the capital required to support growth.[1]

A justified P/B analysis should therefore have two layers: adjusted common book equity and the present value of future ROE spreads. A bank trading below book can be correctly priced if normalized ROE remains below the cost of equity or if book is overstated. A bank above book can be worth the premium if a deposit, underwriting, or fee franchise supports durable excess returns after losses and capital retention. The existing financial-institution valuation topic develops those institution-specific adjustments; this topic supplies the general residual-income identity that organizes them.[1]

### For intangible-intensive and acquisition-heavy companies

Reported book equity is least comparable when internally generated economics and acquisition accounting diverge. IAS 38's recognition rules mean that research and many internally generated intangibles can be expensed while acquired identifiable intangibles and goodwill enter the balance sheet under different rules. Raw ROE can therefore punish an acquirer with a larger recorded base and flatter an organic builder whose investment passed through expense.[9]

An adjusted residual-income model can capitalize a supportable portion of past investment and amortize it over an evidence-based life, with matched changes to earnings and book equity. The adjustment must be symmetric: adding an asset without reversing the related expense, or reversing expense without charging amortization, overstates residual income. The author's assessment is that unverifiable intangible capitalization is worse than leaving book imperfect because it converts uncertainty into an invented anchor. Use an adjustment only when spending, useful life, attrition, and future benefit can be defended.[9][10]

Acquisition goodwill also requires a two-sided test. A write-off may reveal that capital was destroyed, but leaving the impairment entirely in one historical period and then evaluating management on a smaller capital base can make future residual income appear improved. Retain or reconstruct the acquisition capital needed to judge economic returns, while separately recognizing any genuine loss in value. This keeps performance measurement from rewarding a company merely for admitting an earlier overpayment.[10]

### For model builders and reviewers

Build the model as a closed accounting system. The minimum schedules are: common-equity opening balances; net income attributable to common; dividends; repurchases and issuance at transaction value; OCI and other direct equity changes; ending book; cost of equity; residual income; and the enterprise-to-common-share reconciliation for any non-common claims. Each schedule should share a valuation date, currency, and ownership perimeter.[1][2][8]

Make the terminal state explicit. Report terminal book equity, ROE, cost of equity, residual income, growth, and the share of value arising after the explicit forecast. If a continuing value assumes positive residual income forever, explain the competitive or contractual protection. If it assumes zero residual income, explain why the company has no durable spread. If it uses a fade factor, show the resulting year-by-year ROE path rather than presenting the factor as an unexplained constant.[1][7]

Reconcile alternative models rather than average them. DDM, FCFE, FCFF, residual income, and EVA should tell compatible stories when they use consistent forecasts. A material gap should be traced to distributions, reinvestment, financing, book-value adjustments, terminal assumptions, or claim definitions. Penman and Sougiannis and Francis, Olsson, and Oswald show why finite-horizon implementations can differ; their evidence makes reconciliation more important, not less.[4][5]

### For screening and implied-expectations analysis

A residual-income screen should combine price-to-adjusted-book, normalized ROE, cost of equity, forecast book growth, and a conservative persistence rule. It should flag negative or unusually small book equity, large buybacks, repeated impairments, acquisition-heavy accounting, large OCI movements, and material unrecognized intangibles because those conditions weaken comparability. The screen narrows a research universe; it does not produce a buy decision.[1][8][9][11]

Value-to-price can carry information beyond raw book-to-price, as Frankel and Lee report, but the forecast input is itself a risk. Consensus earnings errors can be predictable, and a residual-income model can compound them through terminal persistence. A robust screen should therefore include a reverse case based on the market price, a conservative fade case, and a case that corrects identifiable forecast bias. The signal is strongest when all three indicate that the market requires less residual income than the business can plausibly earn.[6][7]

### For boards and capital allocators

Residual income makes the opportunity cost of equity visible. A project, division, or acquisition that reports positive accounting profit can still destroy value if its return on committed capital is below the relevant required return. EVA applies this principle at the enterprise or operating-capital level, while equity residual income applies it to common book equity. Growth creates value only when the return on the incremental capital exceeds its charge.[1][10]

The metric should not be used mechanically for compensation. Managers can improve measured residual income by delaying necessary investment, writing assets down, repurchasing shares, or changing the accounting base without improving long-term economics. A governance design should use multi-period measures, matched capital and earnings adjustments, and controls for investment, risk, and owner transactions. Damodaran's discussion of the many accounting adjustments required in practical EVA systems shows why a single reported number is not a self-validating performance measure.[10]

### A practical decision sequence

A defensible residual-income valuation can be organized into eight gates. First, define the common-equity claim. Second, test whether starting book equity is usable or can be adjusted consistently. Third, forecast attributable earnings and all owner transactions. Fourth, roll book equity through clean surplus, including recurring OCI or other direct changes. Fifth, estimate a claim-consistent cost of equity. Sixth, model ROE spread and fade from competitive evidence. Seventh, reconcile the terminal state and at least one alternative valuation. Eighth, compare the resulting value range with market price and state the assumptions that would invalidate it.[1][2][4][8][10]

Failure at an early gate is not repaired by a detailed terminal formula. An unreliable book base, broken share-count reconciliation, or unsupported earnings path contaminates every later calculation. The durable use of residual income is not that it replaces DCF, dividends, or multiples; it makes the economic profit required to bridge book value and market value explicit, auditable, and open to falsification.[1][4][5]

## Sources

1. CFA Institute (2026). "Residual Income Valuation." CFA Program Level II Refresher Reading.
   https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/residual-income-valuation [high]

2. Ohlson, J. A. (1995). "Earnings, Book Values, and Dividends in Equity Valuation." Contemporary Accounting Research, 11(2), 661-687.
   https://doi.org/10.1111/j.1911-3846.1995.tb00461.x [high]

3. Feltham, G. A., and Ohlson, J. A. (1995). "Valuation and Clean Surplus Accounting for Operating and Financial Activities." Contemporary Accounting Research, 11(2), 689-731.
   https://doi.org/10.1111/j.1911-3846.1995.tb00462.x [high]

4. Penman, S. H., and Sougiannis, T. (1998). "A Comparison of Dividend, Cash Flow, and Earnings Approaches to Equity Valuation." Contemporary Accounting Research, 15(3), 343-383.
   https://doi.org/10.1111/j.1911-3846.1998.tb00564.x [high]

5. Francis, J., Olsson, P., and Oswald, D. R. (2000). "Comparing the Accuracy and Explainability of Dividend, Free Cash Flow, and Abnormal Earnings Equity Value Estimates." Journal of Accounting Research, 38(1), 45-70.
   https://doi.org/10.2307/2672922 [high]

6. Frankel, R., and Lee, C. M. C. (1998). "Accounting Valuation, Market Expectation, and Cross-Sectional Stock Returns." Journal of Accounting and Economics, 25(3), 283-319.
   https://doi.org/10.1016/S0165-4101(98)00026-3 [high]

7. Dechow, P. M., Hutton, A. P., and Sloan, R. G. (1999). "An Empirical Assessment of the Residual Income Valuation Model." Journal of Accounting and Economics, 26(1-3), 1-34.
   https://doi.org/10.1016/S0165-4101(98)00049-4 [high]

8. Ohlson, J. A. (2000). "Residual Income Valuation: The Problems." Working paper.
   https://papers.ssrn.com/sol3/papers.cfm?abstract_id=218748 [high]

9. IFRS Foundation (2026). "IAS 38 Intangible Assets."
   https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias38.html [high]

10. Damodaran, A. "Economic Value Added." New York University Stern School of Business.
    https://pages.stern.nyu.edu/~adamodar/New_Home_Page/invfables/eva.htm [high]

11. Damodaran, A. "Determinants of Price to Book Ratios." New York University Stern School of Business.
    https://pages.stern.nyu.edu/~adamodar/New_Home_Page/invfables/pbvdeterminants.htm [high]

## See Also

- `library/valuation-screening/discounted-cash-flow-dcf-methodology.md` -- the cash-flow representation that residual income must reconcile with under consistent forecasts.
- `library/valuation-screening/dividend-discount-models.md` -- the distribution-based equity model from which residual income can be derived through clean surplus.
- `library/valuation-screening/cost-of-capital-capm-wacc-erp.md` -- the required equity return used to calculate and discount the equity charge.
- `library/valuation-screening/valuation-multiples-pe-ev-ebitda-pb-analysis.md` -- the broader multiples framework, including price-to-book and its accounting limits.
- `library/valuation-screening/valuing-financial-institutions-banks-insurers-balance-sheet-businesses.md` -- a major application of residual income to balance-sheet businesses.