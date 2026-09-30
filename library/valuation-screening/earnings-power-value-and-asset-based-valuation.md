---
name: earnings-power-value-and-asset-based-valuation
id: 20260816T111900Z
tier: library-topic
domain: valuation-screening
author: Librarian
tags: [earnings-power-value, asset-based-valuation, epv, liquidation-value, net-net, reproduction-value, greenwald, graham, intrinsic-value]
links: [library/valuation-screening/discounted-cash-flow-dcf-methodology.md, library/valuation-screening/graham-number-quantitative-value-screens.md, library/value-investing/anchor-value-investing.md]
reviewed: 2026-09-30
---

# Earnings Power Value and Asset-Based Valuation -- Anchoring Intrinsic Value in What a Company Already Earns and Owns

Earnings Power Value (EPV) estimates the value of a steady-state business from normalized current operating earnings, while asset-based methods estimate equity from the economic value of assets less liabilities. Both reduce reliance on explicit growth forecasts, but neither is automatically conservative: EPV depends on sustainable earnings, maintenance reinvestment, and the cost of capital, while an asset valuation depends on realizable asset values, complete claims, sale conditions, and costs [1][3][4][6]. Used together, they separate value supported by present operations and resources from value that requires future growth.

## Background

Asset-based analysis begins with a different premise from ordinary going-concern valuation. A going-concern estimate assumes that assets remain organized in a business and continue producing benefits; a liquidation estimate assumes that the business is dissolved and its assets are sold individually. CFA Institute treats these as distinct valuation premises, and the International Valuation Glossary defines liquidation value as the amount realized after relevant preparation and disposal costs, with orderly and forced liquidation distinguished by the available market-exposure period [3][4]. The distinction matters because the same warehouse, receivable, brand, or machine can have different values when used in a functioning operation, sold with adequate time, or sold under compulsion.

Benjamin Graham and David Dodd made balance-sheet protection central to security analysis in the 1930s. Their net current asset value approach counted current assets and deducted all liabilities and senior claims, while assigning no value to fixed assets or future earnings [2][12]. Graham's stricter purchase rule sought a diversified group of shares priced at no more than two-thirds of net current asset value, rather than treating every stock below book value as a bargain [12]. This was a screening and portfolio rule, not a promise that reported current assets would be collected at carrying value or that a minority shareholder could force liquidation.

Book value, adjusted asset value, and liquidation value therefore must not be used as synonyms. Book value is an accounting residual based on recognition and measurement rules, often including historical cost and accumulated depreciation. An adjusted asset valuation re-estimates recorded and unrecorded assets and liabilities under a stated premise. Liquidation value asks what net proceeds would remain if assets were sold and claims, taxes, and disposal costs were paid [3][4]. Reproduction or replacement analysis asks what it would cost at the valuation date to recreate an identical asset or equivalent utility, with deductions for physical, functional, and economic obsolescence where appropriate [1][4]. Each answers a different question.

Bruce Greenwald and his co-authors later organized a valuation process around asset value, current earnings power, competitive advantage, and growth. EPV capitalizes sustainable, steady-state operating earnings without an explicit growth assumption. Greenwald's sequence compares asset value with earnings-power value and then asks whether a competitive advantage can support returns above the cost of capital; it is not a rule that book value, EPV, and a separately estimated growth value should always be added together [1][5]. Columbia Business School's description of the method explicitly presents three comparison cases: EPV below asset value, EPV approximately equal to asset value, and EPV above asset value [5].

This framework does not make discounted cash flow (DCF) obsolete. CFA Institute recommends choosing models according to the company's characteristics, the quality of available information, and the purpose of the valuation, and notes that analysts often use more than one model because each is input-sensitive [3]. DCF is useful when the timing and economics of changing cash flows matter. EPV is useful when a defensible steady state can be estimated. Asset methods are most useful when assets are separable and measurable, when liquidation is relevant, or when earnings cannot be normalized. The methods are complements when they are built on compatible definitions.

The historical appeal of EPV and adjusted asset value is epistemic restraint. They force the analyst to identify what can be supported by current operations and current resources before paying for a future that has not occurred. Yet restraint comes from disciplined inputs, not from the method's label. A peak-cycle profit capitalized forever can overstate EPV; obsolete inventory carried at cost can overstate asset value; omitted pension, lease, environmental, tax, or litigation claims can overstate both. The correct lesson is narrower than "assets and earnings are safe": each input must be converted from an accounting amount into an economic amount under an explicit valuation premise [1][3][4].

## Core Concepts

### EPV is a steady-state operating valuation

EPV asks what the existing operations are worth if their normalized earnings can continue at a constant scale. A common enterprise-level form is:

`Enterprise EPV = normalized steady-state operating cash earnings / WACC`

The numerator ordinarily begins with normalized operating profit, applies a sustainable tax rate, adds back noncash depreciation, subtracts maintenance capital expenditure, and includes any recurring working-capital investment needed to maintain the operation. The denominator is a weighted average cost of capital consistent with the operating cash flow and its risk [1][6]. Excess cash and other non-operating assets are then added, debt and debt-like claims are deducted, and diluted claims are recognized to reach common equity value. Mixing an enterprise numerator with a cost of equity, or calling enterprise EPV a per-share equity value before this reconciliation, is a claim mismatch.

If normalized after-tax operating cash earnings are 100 million and WACC is 10 percent, enterprise EPV is 1 billion. The arithmetic is simple because the model treats the earnings stream as a no-growth perpetuity. Simplicity does not remove sensitivity: the same 100 million is worth 1.25 billion at 8 percent and approximately 833.3 million at 12 percent. EPV removes an explicit terminal-growth rate, but it still requires judgments about the sustainable numerator, operating risk, capital structure, and discount rate [1][6]. A useful EPV therefore shows a range rather than a single precise answer.

### Normalization is the main analytical burden

Current reported earnings are rarely identical to steady-state earnings. The analyst must remove genuinely nonrecurring gains and losses, retain costs labeled nonrecurring when they recur economically, and normalize margins and volumes across a representative cycle. A cyclical producer should not capitalize a commodity-price peak forever, and a temporarily disrupted business should not automatically capitalize a trough. The CFA Institute Hospira case begins with EBIT to remove financing effects, normalizes operating income, averages recurring restructuring charges, applies a sustainable tax rate, and then capitalizes adjusted income at WACC [6]. The case illustrates a process, not a universal set of adjustments.

Normalization also requires consistent treatment of expenses that support the existing franchise. Advertising, research and development, customer acquisition, software development, training, and other spending may contain both maintenance and growth components. Adding all such spending back because some portion may support growth can overstate steady-state earnings; leaving every amount untouched can understate earnings when accounting expense recognition does not match the economic life of the investment. The analyst should identify which expenditures are required to preserve current revenue, margin, capability, and competitive position and should document any capitalization or add-back [1][5].

A steady state also needs a defensible revenue base. "No growth" does not mean that nominal sales, prices, and costs can be combined inconsistently. If the numerator includes inflationary price increases, the analyst must consider the reinvestment required to replace productive capacity at higher prices. If the analysis is in real terms, cash flows and the discount rate must both be real. EPV is internally coherent only when the maintained operating scale, price basis, tax assumptions, and discount rate describe the same economic state [10].

### Maintenance investment is observable only imperfectly

Maintenance capital expenditure is the investment needed to sustain the existing productive capacity and competitive position; growth capital expenditure supports additional capacity or capability. Financial statements generally report total capital expenditure, not a clean split between the two. Depreciation is an accounting allocation of prior cost and can differ from current replacement needs because of inflation, asset age, useful-life estimates, obsolescence, and fully depreciated assets that remain in service [6][13]. Consequently, "maintenance capex equals depreciation" is a starting approximation for some stable businesses, not a fact.

The EPV adjustment can be written as normalized NOPAT plus depreciation and amortization, minus maintenance capital expenditure and maintenance working-capital investment. When depreciation exceeds maintenance needs, the excess may be added back; when maintenance needs exceed depreciation, the shortfall must reduce earnings power. Peddireddy's maintenance-capex research estimates rather than observes this quantity and reports that estimated under-depreciation predicts later asset write-offs and lower future earnings in the studied sample [13]. The result reinforces the practical point: an analyst who assumes reported depreciation is sufficient without examining capacity costs can capitalize earnings that are not economically maintainable.

Working capital deserves the same treatment. A constant-size business still needs receivables, inventory, and operating cash appropriate to its sales and production cycle. Seasonal or cyclical working capital should be normalized. Supplier financing, customer deposits, and negative working capital can be durable features, but they should not be extrapolated beyond what the operating model can sustain. EPV should capitalize distributable steady-state operating cash earnings, not accounting profit before the resources required to preserve that profit [1][6].

### Asset-based values depend on premise and perimeter

CFA Institute defines an asset-based equity value as the estimated value of assets less the estimated value of liabilities [3]. The apparent simplicity hides two hard questions: which assets and claims belong inside the perimeter, and which value premise applies to each. An adjusted net asset schedule should include recorded assets, identifiable unrecorded assets where relevant, operating and non-operating assets, debt, leases, pensions, preferred stock, noncontrolling interests, tax consequences, contingent claims, and wind-down costs. The same perimeter must be used on both sides of the calculation [3][4].

Book value is useful as a reconciliation starting point, not as a default economic value. Cash may be close to face value but can be restricted or trapped. Receivables require collection and concentration analysis. Inventory requires allowances for age, fashion, damage, completion cost, and channel discounts. Property may be worth more or less than depreciated cost. Specialized equipment can have high replacement cost but low resale value. Internally developed brands, data, software, and customer relationships may be economically important yet absent or understated on the balance sheet, while acquired goodwill may have no separate liquidation proceeds [3][4].

Replacement and reproduction analyses support a going-concern or entry-cost question. Replacement cost estimates the cost of equivalent utility; reproduction cost seeks an identical or substantially identical asset. Either must recognize obsolescence and implementation time. A competitor may not need to reproduce every legacy asset, and spending incurred by the incumbent is not automatically value to a new owner. The relevant question is the least economic cost of obtaining equivalent productive capacity, not the historical amount management spent [1][4].

Liquidation analysis instead estimates net sale proceeds. Orderly liquidation assumes a reasonable marketing period intended to maximize expected proceeds; forced liquidation assumes less than reasonable exposure [4]. Gross appraised value is not equity value. The analyst must deduct secured and unsecured claims in priority order, sale commissions, severance, lease termination, remediation, taxes, professional fees, and the cash consumed while operations wind down. Control rights and a credible catalyst also matter to a minority investor: a theoretical liquidation surplus may remain inaccessible while management continues destroying value [4].

### NCAV is a screen, not a complete liquidation model

Net current asset value is calculated as current assets minus total liabilities and senior equity claims, commonly including preferred stock. Graham's classic purchase rule sought shares below two-thirds of this amount per share [2][12]. Fixed assets and future earnings receive zero value in the screen, which makes the test stricter than ordinary book value. The author's interpretation is that the discount is intended to absorb collection losses, inventory haircuts, omitted costs, and estimation error, but it does not prove that these risks are covered in a particular company [2][12].

NCAV should be rebuilt from the notes rather than copied mechanically. Cash may be restricted; receivables may be overdue or related-party; inventory may be obsolete; tax assets may not be cash-realizable; liabilities may omit guarantees, legal exposures, or shutdown obligations. Share count should include dilution that is economically senior to common shareholders. A business that is burning cash can consume an apparent discount before value is realized. Diversification was integral to Graham's use of the rule because individual failures were expected [12].

The method is associated with inventory- and receivable-heavy companies, but it is not logically unavailable to an asset-light company. A software or service business with enough unrestricted cash or marketable securities and few liabilities can have positive NCAV; whether its market capitalization falls below two-thirds of that value is a separate price test. The correct limitation is that NCAV assigns no value to most intangible earning assets, so it is usually uninformative for a successful asset-light going concern trading far above liquid assets [12].

### Asset value and EPV should be compared, not blindly added

Greenwald's framework uses the relationship between adjusted asset value and EPV as a diagnostic [1][5]. If EPV is materially below reproduction value, the assets may be earning inadequate returns, management may be poor, capacity may be excessive, or the asset estimate may be too high. Liquidation, restructuring, or replacement-cost write-downs may be more relevant than a growth forecast. If EPV and asset value are similar, the business may be earning roughly its cost of capital in a competitive industry. If EPV materially exceeds reproduction value, the difference can indicate franchise value, but only after the analyst has ruled out peak earnings, omitted assets, understated replacement cost, and an understated discount rate.

This comparison is not an identity and the estimates need not share the same valuation premise. Reproduction value is an entry-cost benchmark, EPV is a going-concern income value, and liquidation value is an exit-proceeds estimate. The author's assessment is that calling the lowest number a "floor" can be misleading when the shareholder cannot cause a sale, assets deteriorate, claims are incomplete, or the business consumes cash. The estimates are evidence about different states of the world; their usefulness lies in making disagreements visible [1][3][4].

### Growth creates value only through excess returns

A no-growth EPV does not assert that the company will literally stop changing. It isolates the value of current sustainable economics. Growth adds value only when incremental investment is expected to earn more than its opportunity cost after allowing for the capital required. In stable-growth mathematics, growth equals the reinvestment rate multiplied by return on invested capital. If return on invested capital equals WACC, a higher growth rate requires proportionally more reinvestment and does not add value under the model; if the return is below WACC, growth reduces value [10].

The author's interpretation is to value growth separately. The analyst should identify the addressable reinvestment opportunity, incremental return on capital, duration of competitive advantage, and financing required. A market price above EPV may be justified by valuable growth, non-operating assets, or an EPV estimate that is too low. It is not proof of overvaluation. Conversely, a price below EPV may reflect a correct market judgment that normalized earnings will decline, WACC is higher, liabilities are missing, or control holders will not distribute value. EPV frames the question; it does not answer it without business analysis [1][5][10].

## Choosing Between the Three Approaches

The choice among adjusted asset value, EPV, and DCF follows the economics of the subject rather than a fixed hierarchy. CFA Institute's general rule is to match the model to the company's characteristics, data quality, valuation purpose, and analyst confidence, and to use more than one model when no single approach is sufficient [3]. The author's synthesis is that each method should be assigned a job before calculation: asset value tests resources and claims, EPV tests current sustainable operations, and DCF tests changing cash flows and reinvestment.

Asset-based methods are strongest when material assets are separable, observable, and transferable. Examples include holding companies, investment portfolios, real estate vehicles, and businesses being liquidated or restructured. They can also inform distressed analysis when earnings are negative, but only after marketability, creditor priority, taxes, contingent liabilities, and wind-down costs are modeled [3][4]. They are weaker as the sole method for an operating company whose value depends on a workforce, network, brand, data, or interconnected assets that cannot be sold separately without losing their earning function.

EPV is strongest when a representative operating state can be estimated: a mature company, a cyclical business at mid-cycle, or a temporarily disrupted business whose sustainable revenue, margin, maintenance investment, tax rate, and risk can be defended. It is weak when the business model is changing rapidly, current economics are structurally negative, maintenance and growth spending cannot be separated, or a small change in scale would alter unit economics. In those cases, "normalization" can become an undisclosed forecast rather than an observation [1][6][13].

DCF is strongest when value depends on a transition that must be modeled explicitly, such as a new project, finite-life asset, restructuring, high-growth company, or changing capital intensity. Its terminal value can be a large share of present value without making the method invalid; Damodaran notes that this is normal for long-lived going concerns. The model fails when terminal growth, reinvestment, return on capital, and discount-rate assumptions are internally inconsistent, especially when growth is assumed without the investment needed to produce it [10].

The author's reconciliation rule is to keep claim levels consistent. Enterprise EPV and enterprise DCF should be reconciled to equity with the same non-operating assets, debt, leases, pensions, preferred claims, noncontrolling interests, and diluted share count. An asset value already calculated for common equity should not have debt deducted twice. A liquidation estimate should not be compared with a going-concern market price without explaining control, timing, and realization risk. Differences among methods should be explained by premises and inputs, not averaged mechanically into an apparently precise target [3][4][6].

## Evidence

### Oppenheimer's NCAV portfolios

Henry Oppenheimer examined U.S. securities meeting Graham's net current asset criterion over 1970-1983. The study formed portfolios from companies priced below net current assets and assessed both full-period and 30-month holding-period performance. CFA Institute's abstract reports that the portfolios had higher mean returns than market benchmarks, that full-period risk-adjusted returns were significantly greater, and that individual 30-month outcomes were widely variable even though the portfolios as a group outperformed [7]. An AAII review reports an average annual return of 29.4 percent for qualifying shares over the period and describes the purchase threshold as no more than two-thirds of NCAV [12].

The evidence supports a historical return anomaly in that sample; it does not establish the cause claimed in the prior version of this topic. Oppenheimer's abstract does not show that market beta was the only relevant risk, that institutions were unable by mandate to own the shares, or that every apparent NCAV discount was realizable. The variability of 30-month portfolios and Graham's diversification rule are important qualifications [7][12]. The author's assessment is that transaction costs, bid-ask spreads, taxes, delisting treatment, liquidity, and the ability to trade small distressed companies must be tested before treating a backtested return as investor-capturable [7][9][12].

### Longer-horizon NCAV evidence is positive but conditional

Mohanty and Oxman study the U.S. NCAV strategy from 1969 through 2019 using 648 unique firms and a criterion of price below two-thirds of current assets minus total liabilities. Their value-weighted NCAV portfolio earned an average 1.94 percent per month. After controlling for the Fama-French five factors, the Pastor-Stambaugh liquidity factor, and the January effect, they report alpha of 1.09 percent per month, which compounds to approximately 13.9 percent annually [9]. Industry- and size-matched controls did not show abnormal returns [9].

The same paper reports that profitability declined during 2004-2019 [9]. That result corrects the stronger claim that the effect persisted unchanged into recent decades or had been fully unexplained by standard factor models. The evidence is consistent with persistence over the full historical sample, but the documented weakening in the later subperiod makes the result conditional rather than timeless [9]. A backtest of qualifying securities is also not evidence that reported NCAV equals cash available to common shareholders in each company.

### Book-to-market evidence is related, not equivalent

Fama and French studied NYSE, AMEX, and later NASDAQ stocks from July 1963 through December 1990. In one-dimensional book-to-market sorts, average equal-weighted monthly returns rose from 0.30 percent for the lowest book-to-market portfolio to 1.83 percent for the highest, a difference of 1.53 percentage points per month [8]. In two-dimensional tests, size and book-to-market helped describe the cross-section of average returns, while market beta alone did not [8].

This is evidence about a historical relation between price relative to accounting book equity and subsequent returns. It is not a direct test of EPV, reproduction value, or liquidation value, and Fama and French did not conclude that mispricing was the only explanation. Their paper discusses book-to-market as a possible proxy for distress-related risk and says investment prescriptions depend on whether the pattern persists and whether its origin is rational risk pricing or irrational pricing [8]. The previous assertion that the cheapest quintile beat the most expensive by only four to five percent annually misstated the paper's reported portfolio construction and result.

### A practitioner case shows the mechanics, not validation

The CFA Institute Hospira case begins with operating earnings, normalizes margins and recurring charges, estimates maintenance capital expenditure rather than treating all capital expenditure as growth, applies a sustainable tax rate, capitalizes the result at WACC, and then reconciles debt and cash to equity [6]. This is useful evidence of how practitioners implement EPV and where judgment enters. It also shows why EPV cannot be described as forecast-free: the analyst must decide which disruption is temporary, which restructuring cost recurs, what maintenance investment is required, and which tax rate and WACC are sustainable [6].

A single case cannot validate EPV as a generally superior predictor of market value or investment return. Its role here is methodological. Peddireddy's separate empirical work adds evidence that the depreciation-maintenance distinction is economically material: estimated under-depreciation is associated with later write-offs and lower future earnings in a large firm-year sample [13]. That finding supports scrutiny of the numerator, not any specific EPV estimate.

### Practitioner records do not isolate one method

Warren Buffett's 1984 essay reports Walter Schloss's limited partners at 16.1 percent compounded annually versus 8.4 percent for the S&P over the 28.25-year period shown; the partnership's pre-allocation result was 21.3 percent [11]. A later AAII profile reports 15.7 percent for Schloss's fund versus 11.2 percent for the market from 1956 through 2000 and describes his emphasis on low price-to-book shares, low prices, financial statements, and broad diversification [14]. These figures support the existence of a long successful record using a price-versus-value discipline.

They do not prove that a pure NCAV strategy, EPV, or asset-based valuation alone caused the record. Schloss owned many issues and used criteria broader than net-nets; Buffett's essay was an argument using selected value-oriented records, not a controlled test [11][14]. The prior version's presentation of Graham-Newman, Schloss, and Buffett partnership returns as direct empirical confirmation of one asset-based method therefore overstated what practitioner histories can establish.

### Terminal-value evidence narrows the comparison with DCF

Damodaran's terminal-value analysis shows both why EPV is attractive and why the contrast must be stated carefully. In a perpetual-growth DCF, value becomes unstable as the growth rate approaches the discount rate, and stable growth must be tied to reinvestment and return on capital [10]. Those constraints prevent growth from being treated as free. Damodaran also states that a large terminal-value share is normal for a long-lived going concern and is not by itself proof that DCF is flawed [10].

EPV avoids an explicit terminal-growth rate by using a zero-growth steady state, but its value remains the capitalized present value of an indefinite earnings stream. It inherits sensitivity to normalized earnings and WACC and adds the difficult separation of maintenance from growth investment. The author's assessment is that the empirical and practitioner evidence supports EPV and asset value as useful anchors and diagnostic tools, but does not support the universal claim that demonstrable existing value is systematically mispriced, that growth forecasts always fail, or that the lowest asset estimate is a guaranteed downside floor [1][6][8][9][10][13].

## Implications

### A reviewable valuation workflow

The author's synthesis is that an analyst should build the methods as an auditable sequence rather than choose a favorite formula. First, define the claim being valued: operating enterprise, invested capital, or common equity. Second, state the premise: going concern at constant scale, replacement or reproduction, orderly liquidation, forced liquidation, or an explicit transition. Third, normalize the relevant operating and balance-sheet inputs. Fourth, calculate more than one case. Fifth, reconcile enterprise values to common equity claim by claim. Sixth, compare the result with price and identify exactly what price assumes [1][3][4].

The author's recommended EPV audit trail shows reported EBIT, every normalization adjustment, the sustainable tax rate, depreciation and amortization, maintenance capex, maintenance working capital, WACC, non-operating assets, debt-like claims, and diluted shares. Sensitivity should vary both normalized earnings and WACC because the denominator remains consequential even with zero growth. A range based on peak, mid-cycle, and trough economics is more informative for a cyclical company than capitalizing one historical year [1][6][13].

For adjusted asset value, the audit trail should proceed asset by asset and claim by claim. It should identify the valuation date, standard of value, sale premise, market-exposure period, source of appraisals, expected collection or sale haircuts, restricted assets, unrecorded assets and liabilities, taxes, transaction costs, wind-down cash use, and creditor priority. A separate orderly and forced case is preferable to one undefined "liquidation value" because the International Valuation Glossary treats them as different premises [4].

### Deep-value investing requires realization analysis

A discount to NCAV or liquidation value is an investigative signal, not realized profit. The investor needs to ask how fast the asset pool is changing, who controls capital allocation, whether management can consume the surplus, which creditors rank ahead of common equity, and what catalyst could cause distribution, sale, or operating improvement. A cash-burning company can destroy a statistical discount; a restricted cash balance can be unavailable; an obsolete inventory balance can disappear under a forced-sale haircut. The two-thirds rule is a portfolio screen that supplies room for error, not a substitute for the asset and claim schedule [7][9][12].

The author's assessment is that control and time distinguish corporate liquidation value from minority-share value. A controlling owner may be able to sell assets, close operations, or replace management. A minority holder may own the same proportional legal claim but lack the power to realize it. The market can rationally discount an asset surplus for delay, agency costs, taxes, litigation, or the risk that operations erode the assets before a catalyst occurs. Accordingly, "floor" should be reserved for a scenario calculation with explicit realization assumptions, not used as a synonym for book value or NCAV [3][4][12].

### EPV reduces one forecast problem but exposes others

EPV is a useful defense against paying implicitly for indefinite high growth because it reports the value of current steady-state economics separately. A price materially above a well-supported EPV makes the growth component visible. The next question is then testable: what reinvestment rate, incremental return on capital, and competitive-advantage period are required to justify the gap? Damodaran's linkage of growth to reinvestment and return on capital supplies the consistency check [10].

The method does not remove forecasting. Normalization predicts what current earnings are sustainable; maintenance capex predicts the spending required to preserve them; WACC estimates the opportunity cost appropriate to their risk; and the perpetual form assumes the operating state can persist. These may be narrower judgments than a ten-year operating forecast, but they remain judgments. The disciplined response is to expose them, use scenarios, and compare them with asset value and a properly constructed DCF rather than declare EPV automatically conservative [1][6][13].

### Corporate managers can use the same separation

For managers, the asset/EPV/growth separation distinguishes maintaining the existing business from expanding it. The author's synthesis is that a capital request should state how much spending preserves current capacity, how much creates additional capacity, and what incremental return the growth component is expected to earn. Growth whose return on invested capital is below the cost of capital reduces value in the valuation model even if revenue rises [10]. This converts "growth" from a goal into a capital-allocation hypothesis.

The same framework can identify strategic problems. EPV below reproduction value can indicate underutilized assets, poor operations, excess capacity, or an inflated asset estimate. EPV above reproduction value can indicate competitive advantage, but the gap should be tested against entry barriers, customer behavior, and the durability of margins rather than capitalized twice through both higher earnings and a separate arbitrary franchise premium [1][5]. The author's recommendation is that management compare divestment, repair, reinvestment, and distribution alternatives using consistent claim and cash-flow definitions.

### Model choice should follow the failure mode

The worst error in asset valuation is usually a false floor: overstated sale proceeds or omitted senior claims create apparent protection that does not exist. The defense is a complete asset-and-claim schedule, explicit liquidation costs, and a forced as well as orderly case [4]. The worst error in EPV is usually false normalization: peak earnings, inadequate maintenance spending, or too-low WACC is capitalized forever. The defense is through-cycle evidence, maintenance-capex analysis, and two-dimensional sensitivity [6][13]. The worst error in DCF is usually internally inconsistent growth: cash flow grows without the reinvestment and competitive returns required to support it. The defense is to tie growth to reinvestment and return on capital [10].

The author's synthesis is that these methods are strongest as mutual error detectors. If liquidation value exceeds EPV, the analyst should ask whether continued operation destroys value and whether liquidation is feasible. If EPV exceeds reproduction value, the analyst should test for a durable franchise and for omitted reproduction costs. If DCF greatly exceeds EPV, the analyst should isolate the reinvestment and excess-return assumptions responsible. The result is not a mechanical average but a map of which economic state must occur for each value to be realized [1][3][4][10].

### Connection to the wider brain

This topic is the quantitative counterpart to the margin-of-safety philosophy in the value-investing domain. The cost-of-capital topic supplies the denominator and claim-matching rules for EPV. The DCF topic supplies the explicit-growth alternative and the consistency rules for cash flow, reinvestment, risk, and terminal state. The Graham-screening topic covers mechanical balance-sheet screens, while the valuation-multiples and magic-formula topics provide market-relative and earnings-yield comparisons. Together they separate philosophy, measurement, screening, and portfolio action rather than allowing one conservative-looking ratio to stand in for the entire investment case.

## Sources

1. Greenwald, B.C.N., Kahn, J., Sonkin, P.D., and van Biema, M. (2001).
   "Value Investing: From Graham to Buffett and Beyond." Wiley.
   https://books.google.com/books/about/Value_Investing.html?id=gvCzlskpZxoC
   Primary exposition of asset value, earnings power, franchise value, and growth analysis. [high]

2. Graham, B. and Dodd, D.L. (1934). "Security Analysis: Principles and
   Technique." McGraw-Hill.
   https://books.google.com/books/about/Security_Analysis.html?id=eAZDAAAAIAAJ
   Foundational primary text for balance-sheet-based security analysis and net current asset methods. [high]

3. CFA Institute (2026). "Equity Valuation: Concepts and Basic Tools" and
   "Equity Valuation: Applications and Processes."
   https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/equity-valuation-concepts-basic-tools
   https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/equity-valuation-applications-and-processes
   Defines model categories, asset-based equity value, going-concern value, liquidation value, and model-selection criteria. [high]

4. CBV Institute, ASA, RICS, TAQEEM, and partner organizations (2022).
   "International Valuation Glossary -- Business Valuation."
   https://cbvinstitute.com/wp-content/uploads/2021/11/Practice-Bulletin-2_EN.pdf
   Professional definitions for asset approach, liquidation value, forced and orderly liquidation, and replacement cost. [high]

5. Columbia Business School (2005). "Greenwald Explains Value Investing
   Principles."
   https://business.columbia.edu/insights/chazen-global-insights/greenwald-explains-value-investing-principles
   Describes Greenwald's comparison of asset value and earnings-power value before assessing competitive advantage and growth. [high]

6. Pavese, C.R., CFA (2013). "Hospira: A Case Study for Strategic
   Valuation." CFA Institute Inside Investing.
   https://blogs.cfainstitute.org/insideinvesting/2013/06/06/hospira-a-case-study-for-strategic-valuation
   Practitioner case showing operating normalization, maintenance-capex adjustment, taxes, WACC capitalization, and equity reconciliation. [medium]

7. Oppenheimer, H.R. (1986). "Ben Graham's Net Current Asset Values: A
   Performance Update." Financial Analysts Journal, 42(6), 40-47.
   https://rpc.cfainstitute.org/research/financial-analysts-journal/1986/ben-grahams-net-current-asset-values-a-performance-update
   Peer-reviewed test of NCAV portfolios over 1970-1983, including risk-adjusted and 30-month holding-period results. [high]

8. Fama, E.F. and French, K.R. (1992). "The Cross-Section of Expected Stock
   Returns." Journal of Finance, 47(2), 427-465.
   https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1992.tb04398.x
   Peer-reviewed evidence on size, book-to-market equity, beta, and average U.S. stock returns over 1963-1990. [high]

9. Mohanty, S.K. and Oxman, J.J. (2026). "Does Ben Graham's Net Current
   Asset Value Investing Continue to Generate Excess Returns?" Review of
   Financial Economics, 44(1).
   https://onlinelibrary.wiley.com/doi/full/10.1002/rfe.70034
   Long-horizon U.S. NCAV study covering 1969-2019, factor controls, matched portfolios, and declining recent-period profitability. [high]

10. Damodaran, A. (2020). "Terminal Value: The Tail That Wags the Dog?"
    New York University Stern School of Business.
    https://pages.stern.nyu.edu/~adamodar/pdfiles/country/TerminalValue.pdf
    University valuation notes linking stable growth to reinvestment and return on capital and explaining terminal-value interpretation. [high]

11. Buffett, W.E. (1984). "The Superinvestors of Graham-and-Doddsville."
    Columbia Business School.
    https://business.columbia.edu/insights/chazen-global-insights/superinvestors-graham-and-doddsville
    Primary essay and performance tables for several value-oriented investors, including Walter Schloss. [high]

12. Thorp, W.A. (2010). "Benjamin Graham's Net Current Asset Value
    Approach." American Association of Individual Investors.
    https://www.aaii.com/journal/article/benjamin-graham-s-net-current-asset-value-approach
    Secondary explanation of the NCAV formula, two-thirds purchase rule, diversification, and Oppenheimer result. [medium]

13. Peddireddy, V. (2021). "Estimating Maintenance CapEx." Columbia
    Business School Center for Excellence in Accounting and Security Analysis.
    https://business.columbia.edu/sites/default/files-efs/imce-uploads/CEASA/Events%20Page/estimating-maintenance-capex.pdf
    Research paper estimating maintenance capex and testing under-depreciation against future write-offs, earnings, and returns. [medium]

14. Scatizzi, C. (2009). "Finding Value Among the Lows: The Walter J.
    Schloss Approach." American Association of Individual Investors.
    https://www.aaii.com/journal/article/finding-value-amoung-the-lows-the-walter-j-schloss-approach
    Secondary account of Schloss's long-run results, price-to-book emphasis, and portfolio rules. [medium]

## See Also

- `library/valuation-screening/discounted-cash-flow-dcf-methodology.md` -- the explicit-growth valuation method against which EPV's steady-state assumptions should be compared.
- `library/valuation-screening/graham-number-quantitative-value-screens.md` -- Graham-style mechanical screens and their limitations.
- `library/valuation-screening/cost-of-capital-capm-wacc-erp.md` -- the cost of capital and claim-matching rules used in enterprise EPV.
- `library/valuation-screening/valuation-multiples-pe-ev-ebitda-pb-analysis.md` -- market-relative price-to-book and earnings comparisons.
- `library/valuation-screening/magic-formula-screen.md` -- an earnings-yield and return-on-capital screen that separates cheapness from operating quality.
- `library/value-investing/anchor-value-investing.md` -- the philosophy of margin of safety that motivates conservative valuation anchors.
