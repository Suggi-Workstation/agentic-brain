---
name: pension-accounting-assumptions
id: 20260929T082259Z
tier: library-topic
domain: accounting-financial-shenanigans
author: Librarian
tags: [pension-accounting, defined-benefit-plans, actuarial-assumptions, earnings-quality, funded-status, forensic-accounting]
links: [library/accounting-financial-shenanigans/forensic-accounting-methodology.md, library/accounting-financial-shenanigans/cookie-jar-reserves-and-expense-manipulation.md, library/valuation-screening/enterprise-value-equity-value-reconciliation.md, library/portfolio-risk-management/liability-driven-investing.md]
---

# Pension Accounting Assumptions -- How Discount Rates and Expected Returns Reshape Earnings and Obligations

Defined-benefit accounting converts a long stream of contingent payments into a present obligation, a funded-status asset or liability, and periodic cost. Discount rates, expected asset returns, salary growth, mortality, and health-care trends can move those reported amounts without producing the same-period cash movement, so the forensic task is to reconcile assumptions, roll-forwards, accumulated other comprehensive income, and contributions before deciding whether a change is ordinary estimation or aggressive reporting.[1][3][4]

## Background

A defined-benefit plan promises benefits through a formula rather than limiting the employer's obligation to a fixed contribution. The eventual payments can depend on years of service, compensation, retirement age, mortality, and plan provisions, while assets set aside in a trust earn returns that need not match the assumptions used in financial reporting. The sponsor therefore bears actuarial and investment risk that a defined-contribution sponsor generally transfers to participants after making the required contribution. Accounting has to attribute the promise to periods of employee service even though the benefit may be paid decades later and its final amount is not known at the reporting date.[4]

The measurement problem has three distinct outputs. First, the benefit obligation estimates the present value of benefits attributed to service under the accounting model. Second, the fair value of plan assets is compared with that obligation to produce funded status. Third, periodic benefit cost allocates service, financing, expected or actual asset-return effects, plan amendments, and actuarial experience across income and other comprehensive income. FASB Statement No. 158 requires a US employer to recognize funded status as the difference between plan assets at fair value, with limited exceptions, and the benefit obligation, while recognizing specified unamortized items in other comprehensive income. IAS 19 similarly recognizes a net defined-benefit liability or asset, but its income and remeasurement mechanics differ materially from US GAAP.[1][4]

The obligation is not a bank balance or a bill already presented for payment. It is an actuarial present value built from projected benefit cash flows and assumptions about when, how much, and to whom the plan will pay. A pay-related plan must estimate future compensation if that compensation enters the benefit formula. Every plan must model demographic events such as death, retirement, and employee turnover to the extent they affect promised payments. The resulting cash-flow schedule is discounted, which means a change in the rate can alter the obligation even when the plan text, participant population, and nominal benefits are unchanged.[3][4]

US pension accounting historically paired this long-horizon measurement with delayed recognition in periodic cost. Economic changes in plan assets and obligations could first enter other comprehensive income and then affect earnings through amortization rules. Statement No. 158 moved funded status onto the balance sheet but explicitly did not replace the basic measurement of plan assets, benefit obligations, or annual net periodic benefit cost. The result is an important analytical split: the balance sheet can reflect a current funded-status deficit while the income statement still reflects an expected asset return and amortization of older gains, losses, or prior service costs.[1]

FASB Accounting Standards Update 2017-07 sharpened another split. It requires the service-cost component to be presented with other compensation costs arising from employee service, while the other components of net periodic benefit cost are presented outside that subtotal in the income statement. It also limits capitalization into inventory or other assets to service cost. Interest cost, expected return on plan assets, and amortization can therefore improve or weaken reported net income without representing current employee labor cost or current operating cash flow.[2]

IAS 19 uses a different pattern. It separates defined-benefit cost into service cost, net interest on the net defined-benefit liability or asset, and remeasurements. Remeasurements include actuarial gains and losses and the return on plan assets excluding the amount included in net interest; they are recognized in other comprehensive income and are not recycled through profit or loss. This model does not use a separate management-selected expected return on plan assets to reduce profit-or-loss pension cost in the same way as US GAAP. Comparing pension expense across US GAAP and IFRS without rebuilding the components therefore mixes different recognition systems.[2][4]

The accounting model also differs from funding law and cash policy. Contributions transfer cash to the plan and increase plan assets, but they are not the same as service cost, interest cost, expected return, or actuarial remeasurement. A company can contribute more cash while reporting pension income, contribute little while reporting pension expense, or improve funded status because asset prices or discount rates moved. Ameren's 2025 filing, for example, separately reports assumptions, actual asset returns, funded status, accumulated other comprehensive income, and expected future contributions. Ecolab likewise separates plan assumptions and sensitivity from the obligation and expected cash funding.[8][9]

This topic is therefore not a general guide to pension standards. Its focus is the forensic boundary identified by the accounting-financial-shenanigans anchor: how discretion in pension and postretirement assumptions can change reported earnings, obligations, and presentation; how delayed recognition can obscure the timing of economic losses; and how an analyst can reconstruct the result. The central discipline is to treat every reported pension number as one part of a connected system rather than as an isolated asset, liability, expense, or cash flow.[1][5][6]

## Core Concepts

### Reconcile three ledgers before interpreting any result

The first ledger is the benefit obligation. A simplified annual bridge begins with the opening projected benefit obligation, adds service cost and interest cost, adds or subtracts the effect of plan amendments and actuarial changes, and subtracts benefits paid and obligations settled or transferred. Foreign exchange, acquisitions, curtailments, and other plan events may create additional lines. The bridge explains whether an ending obligation changed because employees earned more benefits, time passed, the plan promise changed, an assumption changed, experience differed from assumptions, or benefits were paid.[3][4]

The second ledger is plan assets. It begins with opening fair value, adds employer and participant contributions and actual investment return, and subtracts benefit payments, settlements, and plan expenses paid from the trust. The same benefit payment generally reduces both plan assets and the obligation when it satisfies a promised benefit, so it does not by itself change funded status. A contribution increases plan assets and uses sponsor cash but does not create an equivalent income-statement expense at that moment. Actual asset return changes economic funded status, while US periodic cost can use an expected return and delayed recognition instead of passing the full actual return through current earnings.[1][7]

The third ledger is periodic benefit cost. Under US GAAP its disclosed components include service cost, interest cost, expected return on plan assets, amortization of prior service cost or credit, amortization of actuarial gain or loss, and settlement or curtailment effects when applicable. Expected return is presented as a reduction of cost. Under ASU 2017-07, service cost belongs with employee compensation, whereas the other components are presented outside that operating subtotal. The exact labels and line locations matter because a company can report operating-margin improvement from classification even when total pre-tax pension cost is unchanged.[2][3]

The author's synthesis is to maintain three control equations: an obligation roll-forward, an asset roll-forward, and an AOCI-to-expense roll-forward. Funded status must reconcile to fair-value assets minus the recognized obligation. Periodic cost must reconcile to its disclosed components. Cash contributions must reconcile to cash flow and the asset roll-forward, not to pension expense. If those controls cannot be completed from the notes, the missing disclosure is itself a limitation on the confidence of any normalization.[1][3][8]

### Discount rates change present value, not the nominal promise

The discount rate converts projected future payments into a reporting-date present value. Under IAS 19, the rate is determined by reference to market yields at the reporting date on high-quality corporate bonds, with government bonds used when there is no deep market in such corporate bonds; currency and estimated term must be consistent with the obligation. US practice likewise uses rates reflecting effective settlement, commonly implemented through a high-quality corporate-bond yield curve matched to projected benefit payments. Ameren describes a theoretical settlement portfolio of high-quality corporate bonds, and Ecolab describes a yield curve built from high-quality non-callable corporate bonds across maturities.[4][8][9]

Holding projected payments constant, a higher discount rate produces a lower present value and a lower rate produces a higher present value. That direction is mathematical, but interpretation is not automatic. A year-end rate increase can create an actuarial gain and improve funded status even though no benefit was cut and no cash entered the plan. A lower rate can create an actuarial loss even when plan assets performed well. The analyst should therefore separate the change in nominal projected benefits from the change in the price assigned to those benefits by the discount curve.[4][8]

A single weighted-average rate can hide the curve-fitting process. The obligation may contain near-term retiree payments and long-dated active-employee payments, so the selected bond universe, treatment of outliers, interpolation, currency, and cash-flow duration all matter. A company can use an externally developed curve and still exercise judgment in mapping its cash flows to that curve. The forensic test is not whether the rate changed in the favorable direction; it is whether the method was applied consistently, used relevant market information at the measurement date, and matched the plan's actual payment pattern.[5][8][9]

### Salary growth, mortality, retirement, and health-care trends shape the cash-flow numerator

A final-pay pension formula requires a salary-growth assumption because future compensation affects the benefit ultimately earned. Higher projected salary growth generally increases a projected obligation for active employees when the formula uses final or career-average pay. A frozen plan may have little or no future salary exposure, which is why disclosures should be read with the plan terms rather than compared mechanically. FASB disclosure guidance identifies compensation increase as one of the assumptions that usually has a significant effect on the obligation and periodic cost.[3]

Mortality assumptions determine the probability and duration of benefit payments. Lower mortality, or greater longevity, generally extends the expected payment stream for a lifetime annuity. The choice is not one universal table: base mortality, participant status, occupation, sex where permitted, and future mortality improvement can matter. The Society of Actuaries' study of US public-plan valuations found wide variation in mortality methods and projection approaches, including generational, static, and no projection. Although that study concerns public-plan funding rather than corporate financial accounting, it demonstrates why an apparently technical table choice can materially change an annuity value and why plan-specific experience must be distinguished from obsolete assumptions.[10]

Other postretirement benefits add health-care trend assumptions. These project medical costs from a current trend rate toward an ultimate rate over time, interacting with participant age, coverage, cost sharing, and claims. FASB disclosure guidance has required specified entities to show the effect of a one-percentage-point change in health-care cost trend rates on the obligation and the service-plus-interest components. The sensitivity is not a forecast of the most likely error; it is a controlled way to show how strongly the measurement depends on one assumption while holding the others constant.[3]

The assumptions must also be internally coherent. Salary growth should relate sensibly to inflation and the company's workforce outlook; retirement and turnover assumptions should agree with plan incentives and experience; mortality tables should not conflict with known population characteristics; and health-care trends should not converge to an ultimate rate that contradicts the long-run inflation framework without explanation. PCAOB AS 2501 directs auditors to evaluate significant assumptions individually and in combination and to compare them with external factors, company strategy, market information, historical experience, and other assumptions used by the company.[5]

### Expected asset return affects US earnings without changing fair-value funded status

Under US pension accounting, the long-term expected return on plan assets reduces net periodic pension cost. It is an assumption applied to an asset measure for the cost calculation, not the actual investment gain or loss realized during the year. The Federal Reserve Bank of San Francisco explained the consequence directly: a plan can use an assumed positive return in net periodic pension cost even when actual asset value fell. Actual and expected return differences enter the gain-or-loss mechanism rather than current cost in full.[1][7]

This creates two simultaneous asset narratives. Fair value determines the plan-assets side of funded status under Statement No. 158. Expected return helps determine current US pension cost. A company can therefore report a weaker balance-sheet funded position while expected return still reduces earnings expense. The difference is not automatically improper; it is part of the prescribed smoothing model. It becomes analytically dangerous when users treat the expected return as cash income, recurring operating performance, or proof that the plan actually earned the assumption.[1][7]

The expected rate should be tested against strategic asset allocation, plausible long-run returns by asset class, fees, diversification, and the plan's de-risking path. Ameren reports a 6.75 percent expected return for 2025 and describes a process using historical and projected returns for current and planned asset classes. Ecolab reports that its assumption reflects asset allocation, investment strategy, inflation, expected real returns, active management, and adviser views. These descriptions provide inputs for challenge, but they do not validate the number by themselves.[8][9]

The most revealing comparison is not simply expected return versus one-year actual return. Long-horizon assumptions will differ from volatile annual outcomes. The analyst should instead compare the assumption with changes in target allocation, bond yields, capital-market assumptions, actual returns over rolling periods, fees, and management's response when evidence changes. A stable high assumption alongside a progressively de-risked portfolio or falling forward-looking returns deserves more scrutiny than an assumption that misses one unusual year.[5][6][9]

### AOCI stores timing differences that can later enter earnings

Statement No. 158 records specified actuarial gains and losses and prior service costs or credits in other comprehensive income when they are not yet recognized in net periodic benefit cost. Amounts in accumulated other comprehensive income are adjusted as they later enter periodic cost under the recognition and amortization provisions. The balance sheet can thus recognize funded status immediately while the income statement recognizes some components gradually.[1]

US gain-or-loss amortization historically uses a corridor. The minimum amortization threshold is 10 percent of the greater of the market-related value of plan assets or the benefit obligation; amounts outside the corridor are amortized over a service-based period under the applicable rules. Plan sponsors can also use a market-related asset value in the expected-return mechanism, which can spread asset gains and losses rather than use only current fair value for cost. These devices reduce income-statement volatility but create a backlog that an analyst must map from AOCI into future expense.[1][6][7]

Prior service cost arises when a plan amendment changes benefits attributed to service already rendered. Under US GAAP it can first enter OCI and then be amortized. A benefit reduction can create a prior service credit that lowers future cost; a benefit enhancement can create future expense. A plan amendment therefore changes employee economics, funded status, AOCI, and the future cost path, even if near-term contributions do not move proportionately. The note should be read for the substance of the amendment, not only the favorable or unfavorable accounting label.[1][3]

Under IAS 19, remeasurements are recognized in OCI and are not recycled to profit or loss. Net interest is calculated on the opening net defined-benefit liability or asset using the specified discount rate, adjusted for relevant cash flows and plan events. The absence of recycling means an IFRS company and a US GAAP company can have similar economics but different future earnings effects from the same actuarial loss. A cross-company screen must normalize the recognition model before treating a pension benefit as higher-quality earnings.[2][4]

### Classification can change performance narratives

After ASU 2017-07, US service cost is presented in the same line or lines as other compensation cost for the affected employees. Interest cost, expected return, amortization, and other non-service components are presented separately outside that subtotal. Only service cost is eligible for capitalization in inventory or another asset. This separation improves visibility but also means a company can report pension income below operating profit while a service-cost increase remains inside operating expense.[2]

The analytical response is to preserve both reported presentation and an economic bridge. Operating analysis should generally retain service cost as employee compensation. Financing and expected-return components should be shown separately rather than buried in operating margin. A valuation using EBIT or EBITDA should state how pension service cost, non-service cost, contributions, and funded status are treated. The related enterprise-to-equity reconciliation topic explains why deducting an underfunded plan while also forecasting catch-up contributions can double count the same burden.[2]

Non-GAAP presentations require the same control. Excluding settlement charges, actuarial amortization, or all non-service pension cost may improve comparability in one context, but an exclusion does not erase the underlying claim or cash need. A recurring exclusion that always removes losses while retaining favorable pension income is asymmetric. The author's synthesis is to show reported operating profit, reported total pension cost, a clearly defined normalized pension cost, and cash contributions as four separate measures.[1][2][7]

### Aggressive accounting is a process conclusion, not a rate comparison

A favorable assumption is not by itself evidence of manipulation. Discount rates can rise with market yields; mortality can improve or deteriorate relative to an older table; salary growth can fall after a plan freeze; and an equity-heavy plan can reasonably have a higher long-run expected return than a duration-matched bond portfolio. Measurement uncertainty is unavoidable because the obligation spans future events and because standards require estimates rather than hindsight.[4][5][10]

Concern increases when several facts converge: an assumption changes near an earnings threshold; the method changes without comparable economic change; the selected point sits persistently at the favorable edge of a defensible range; the assumption conflicts with asset allocation, plan experience, or other company forecasts; favorable changes enter a performance measure while unfavorable changes are deferred or excluded; or disclosures prevent reconstruction. Bergstresser, Desai, and Rauh found systematic associations between return assumptions, earnings sensitivity, acquisitions, option exercise, and asset allocation, but their evidence is statistical and does not prove intent at every firm.[6]

PCAOB AS 2501 provides a useful evidentiary standard. Test management's method, data, and significant assumptions; develop an independent expectation when appropriate; and evaluate later events or transactions that bear on the estimate. Assumptions should be assessed both separately and together because individually plausible choices can produce an aggregate result consistently favorable to earnings. A forensic conclusion should preserve the distinction among reasonable estimation, aggressive selection within a range, accounting error, and intentional manipulation.[5]

## Practical Forensic Reconciliation

Begin by extracting at least five annual tables: the obligation roll-forward, plan-asset roll-forward, funded-status reconciliation, periodic-cost components, and AOCI amounts not yet recognized in cost. Add the assumptions used for the year-end obligation and those used for the following year's cost, because they can differ by measurement date and purpose. Record contributions, benefits paid, expected future contributions, asset allocation, fair-value hierarchy, plan amendments, settlements, and sensitivity disclosures in the same schedule.[1][3][8][9]

The minimum quantitative bridge is:

`ending obligation = beginning obligation + service cost + interest cost + amendments + actuarial loss - benefits paid - settlements +/- other changes`

`ending plan assets = beginning plan assets + contributions + actual return - benefits paid - settlements - expenses +/- other changes`

`funded status = fair value of plan assets - benefit obligation`

`US periodic cost = service cost + interest cost - expected return + prior-service amortization + gain-or-loss amortization +/- settlement and other components`

The equations are simplified control identities. The published note governs the exact signs and additional lines for each company.[1][2][3]

Next, construct an assumption history with columns for the obligation discount rate, cost discount rate, expected asset return, salary growth, mortality table and projection scale, health-care trend path, and any interest-crediting rate. Add the plan's target asset allocation and the duration or liability-hedging description. A change should be tied to a stated method and contemporaneous evidence. If the company changes both the rate and the curve method, preserve the separate effects rather than treating the total actuarial gain as one market movement.[3][5][8][9]

Then isolate the earnings effect. For expected return, multiply the disclosed rate change by the disclosed asset base only when the note makes that base and convention clear; otherwise use the company's sensitivity disclosure. For discount rates, use the disclosed obligation sensitivity rather than a linear estimate when available because duration and convexity make the response nonlinear. For salary, mortality, and health-care trends, use company sensitivities or actuarial disclosure rather than inventing a universal factor. Label every scenario as an analyst estimate, not as an audited correction.[3][4][9]

Reconcile AOCI as a queue of deferred items. Start with opening actuarial gain or loss and prior service cost or credit, add current-period remeasurements and amendments, subtract amounts amortized or otherwise recognized, and tie to ending AOCI before tax. Compare the disclosed amount expected to enter next year's cost with the current amortization. This exposes whether current earnings are receiving relief from old gains, carrying old losses, or approaching a future step-up in amortization.[1][3][8]

Separate cash from accounting. Contributions should tie to the plan-asset roll-forward and financing disclosures. Benefits paid should appear consistently in both obligation and asset bridges when paid from the trust. Expected return is not a contribution, and service cost is not the current cash funding requirement. Compare the company's stated contribution policy with funded status, regulatory minimums, benefit payments, liquidity, and any plan freeze or annuity transfer. Ameren's filing illustrates the necessary separation by reporting funded status, actual return, AOCI, a transfer gain, and forecast contributions independently.[8]

A practical red-flag matrix can organize the review:

| Observation | Benign explanation to test | Aggressive explanation to test |
|:--|:--|:--|
| Higher discount rate | Market yields and matched duration rose | Selected curve or bond universe moved beyond comparable evidence |
| Higher expected return | Strategic asset mix became riskier or forward returns improved | Earnings target drove the rate despite de-risking or weak forward evidence |
| Lower salary growth | Plan freeze or changed workforce economics | Short-term weakness was extrapolated to suppress a long-term obligation |
| Mortality change | New credible experience study or updated table | Favorable table was selected without relevant participant evidence |
| Large actuarial gain | Market and demographic experience genuinely improved | Multiple favorable assumptions changed together without transparent attribution |
| Lower pension expense | Service, interest, return, and amortization moved consistently | Expected return or old AOCI gains masked current funded-status deterioration |

The table is the author's synthesis of the standards, audit requirements, empirical research, and company disclosures.[1][3][5][6][8][9][10]

The final output should show reported values and normalized scenarios rather than one accusation. A useful range includes the company's case, a market- or peer-consistent assumption case, and a stress case. State which lines affect funded status immediately, which affect earnings now, which remain in OCI or AOCI, and which require cash. If the notes do not support a defensible estimate, widen the range and report the disclosure gap. False precision would repeat the same weakness being investigated.[5]

## Evidence

### FASB recognition rules expose funded status but preserve timing differences

Statement No. 158 changed balance-sheet recognition by requiring the overfunded or underfunded status of a defined-benefit plan to be recognized as an asset or liability. The funded status is based on fair-value plan assets, with limited exceptions, and the benefit obligation. The statement also requires gains, losses, and prior service costs or credits not yet included in periodic cost to be recognized through OCI and adjusted as they later enter cost. The method therefore makes the balance-sheet deficit visible without eliminating income-statement deferral and amortization.[1]

FASB's later presentation amendment documents the cost components in a way that can be tested. Its examples show service cost, interest cost, expected return, prior-service amortization, and gain-or-loss amortization as separate lines. ASU 2017-07 requires the non-service components to be presented outside the service-cost line and allows only service cost to be capitalized. ASU 2018-14 retains weighted-average assumption disclosures and shows obligation and plan-asset roll-forwards, contributions, periodic cost, and amounts expected to be amortized from AOCI. These are not optional analytical inventions; they are the reporting architecture that supports reconstruction.[2][3]

### IFRS supplies a contrasting recognition experiment

IAS 19 measures the defined-benefit obligation using actuarial assumptions about demographic and financial variables and a market-based discount rate. It records service cost and net interest in profit or loss, while actuarial gains and losses and the return on plan assets outside net interest are remeasurements in OCI without recycling. It also requires disclosure of significant actuarial assumptions and sensitivity analysis for reasonably possible changes. The method provides a useful comparison because it removes the US-style expected-return credit and subsequent recycling from OCI while retaining the same underlying need to estimate long-lived benefits.[4]

The comparison supports a bounded conclusion: pension economics can be similar while reported periodic cost differs because recognition rules differ. It does not show that IFRS measurements are assumption-free or that US smoothing is necessarily deceptive. Both systems require judgment over discounting, demographics, salary, plan terms, and asset measurement. The evidence instead shows why an analyst must identify the accounting regime before comparing expense, OCI, and funded status.[1][2][4]

### The FRBSF historical analysis shows smoothing in operation

Kwan's 2003 Federal Reserve Bank of San Francisco analysis decomposed aggregate net periodic pension cost for large plan sponsors over 1991-2002. It described how service and interest costs were offset by expected return and other components and reported that aggregate pension cost turned negative in 1999, fell sharply in 2000, remained negative in 2001, and was only mildly positive in 2002. Expected return continued to affect cost even as stock prices retreated.[7]

The method's value is temporal. It follows the accounting components through a market boom and decline rather than inferring smoothing from one company-year. Kwan explains that expected return can be used when actual return is negative and that market-related asset values can spread a gain or loss over five years. The finding is that the mechanism cushions immediate earnings effects after an asset decline. The limitation is that the letter analyzes the historical FAS 87 environment; Statement No. 158 and ASU 2017-07 later changed balance-sheet recognition and presentation but did not erase the expected-return and amortization logic documented in current FASB materials.[1][2][7]

### Bergstresser, Desai, and Rauh link assumption choices to incentives

Bergstresser, Desai, and Rauh used corporate financial and pension data, acquisition records, executive option data, and pension asset-allocation data to examine long-term expected-return assumptions. They measured how sensitive reported operating income was to the pension return assumption and tested whether assumption choices varied with that sensitivity and with managerial events. The published study reports that firms with greater earnings sensitivity used more aggressive return assumptions and that assumptions were higher around acquisitions and executive option exercises.[6]

The quantitative results show economic relevance. A firm at the 90th percentile of pension sensitivity had an expected-return assumption about 40 basis points higher than a firm at the 10th percentile. Instrumental-variables analysis associated a 25-basis-point increase in the assumed return with roughly a 5-percentage-point increase in equity allocation. The authors interpret the combined results as evidence that reporting incentives influenced assumptions and investment decisions.[6]

The study does not make every high return assumption fraudulent. Its sample period, incentive measures, and identification strategy support population-level associations, not a finding about an individual filing. It nevertheless strengthens a forensic hypothesis when a company's assumption is unusually favorable precisely where earnings are highly sensitive, management has a transaction or compensation incentive, and asset allocation changes in the direction needed to justify the rate.[5][6]

### Current filings show the reconstruction inputs in practice

Ameren's 2025 disclosure provides a current company case. It reports a 5.75 percent year-end pension discount rate, a 6.75 percent expected return used in pension cost, actual plan-asset return, projected compensation and cash-balance crediting assumptions, funded status, AOCI items, and expected contributions of about $45 million to $50 million annually for five years. It also reports that an annuity-transfer transaction produced a $15 million actuarial gain to be amortized over ten years beginning in 2026. One event therefore affects plan assets and obligations now, while part of its earnings effect is spread into later periods.[8]

Ecolab's 2025 filing provides a second implementation case. It describes a discount-rate yield curve built from high-quality non-callable corporate bonds, links expected return to asset mix and long-run capital-market inputs, links salary growth to experience, outlook, and inflation, and presents sensitivity to lower discount and expected-return assumptions. It reports a US projected benefit obligation of $1.818 billion and an 8.25 percent expected return for US pension cost. The case demonstrates why materiality depends on both the selected rate and the size of the plan relative to company earnings and equity.[9]

These filings are examples, not allegations. Their evidentiary value is the set of observable controls: method, rate, asset mix, actual return, obligation, AOCI, sensitivity, and contribution policy. A company that supplies those inputs permits a reasoned challenge. A company with an apparently moderate rate but no usable roll-forward can be harder to evaluate than one with an aggressive-looking rate and complete supporting disclosure.[5][8][9]

### Mortality evidence demonstrates legitimate heterogeneity and model risk

The Society of Actuaries compared mortality assumptions used in 2016 valuations for 114 state-based and 56 large local public pension plans. It standardized comparison through annuity factors based on RP-2014 tables and a common projection scale. The study found wide variation by job category and projection method; 58 percent used generational projection, about 37 percent used static projection, and 5 percent used no mortality projection. Roughly one-third had adopted RP-2014 base rates or a variation.[10]

This is not direct evidence about corporate US GAAP earnings management because the population and measurement purpose are public-plan funding. Its value is methodological: mortality choices can differ for legitimate reasons such as occupation, geography, socioeconomic characteristics, and plan experience, while older or weakly supported projection methods can lag evidence. A forensic review must therefore ask whether the chosen table fits the participants and was updated through a credible experience process, not merely whether it produces a favorable obligation.[5][10]

## Implications

### Investors should separate obligation, earnings, OCI, and cash

The first investor implication is that no single pension number answers every question. Funded status measures the balance-sheet difference between fair-value assets and the recognized obligation. Periodic cost measures selected current service, financing, expected-return, and amortization components. OCI or AOCI stores remeasurements and prior-service items under the applicable regime. Contributions measure cash transferred to the plan. These four measures can move in opposite directions without an accounting error.[1][2][4]

An earnings-quality review should begin with service cost because it represents compensation for current employee service. Interest and expected-return components should be separated from operating performance under the US presentation model. Amortization should be traced to the AOCI backlog, and settlements should be identified as event-specific. The author's synthesis is to report both GAAP pension cost and a normalized operating pension cost that retains service cost, then explain every excluded component rather than labeling all non-service cost nonrecurring.[1][2][3]

Balance-sheet analysis should use funded status but test its sensitivity. A lower discount rate, updated mortality, weaker assets, or a plan amendment can enlarge a deficit. An apparent pension asset may also be constrained in its economic availability, particularly under IFRS asset-ceiling rules or plan restrictions. The value attributable to common shareholders should therefore reflect the claim that is not already captured in forecast cash flows, avoiding the double count of deducting a deficit and also subtracting the same future catch-up contributions.[1][4]

The same logic applies to valuation multiples. If operating profit includes service cost but excludes other pension components, the enterprise-value numerator and earnings denominator should use consistent treatment. A pension benefit generated by a high expected return should not receive the same multiple as recurring revenue-derived operating profit without analysis. Conversely, a settlement charge should not be capitalized as though it recurs annually when it transfers a defined block of obligations. The normalization must follow the mechanism.[2][8]

### Lenders should focus on cash timing and claim priority

For lenders, funded status and pension expense are incomplete without the contribution schedule. Regulatory minimums, voluntary contributions, benefit payments, plan freezes, asset performance, interest rates, and de-risking transactions can change cash needs. A plan can be underfunded but require limited near-term cash under applicable funding rules, or appear adequately funded and still require cash after a market decline. The note's expected contributions should be stressed rather than copied into a base case indefinitely.[8][9]

Credit analysis should treat an underfunded plan as a senior economic claim while preserving legal and timing differences from conventional debt. Interest expense on bonds is contractual; pension contributions depend on funding rules, sponsor policy, asset performance, and benefit experience. The author's synthesis is to include a separate pension liquidity schedule showing expected benefits, required and voluntary contributions, settlement transactions, and stress funding rather than hiding the plan inside net debt.[1][8]

Covenant and rating analysis should also remove classification illusions. Expected return can reduce net income without creating cash available for debt service. A contribution uses cash without matching current pension expense. A plan amendment can reduce future benefit cost while creating workforce or labor effects outside the pension note. Lenders should therefore reconcile EBITDA add-backs, operating cash flow, free cash flow, and pension funding under the exact covenant definition.[2][7]

### Audit committees should govern the process that selects assumptions

Audit committees should receive more than a list of rates. For each significant assumption, they should see the method, source data, reasonable range, selected point, prior-year value, quantitative financial-statement effect, and evidence contrary to management's choice. They should also see the aggregate effect of all assumption changes because several individually supportable choices can combine into a consistently favorable result. This follows the audit logic in AS 2501 rather than substituting committee intuition for actuarial work.[5]

The committee should ask why the obligation rate and cost rate changed, how the bond universe and cash-flow matching were applied, whether asset-return assumptions changed with strategic allocation, how mortality experience was studied, and whether salary and health-care assumptions agree with budgets used elsewhere. It should compare prior estimates with subsequent experience without using hindsight as proof of misconduct. Repeated one-directional errors aligned with incentives are more informative than one forecast miss.[5][6][10]

Plan amendments, settlements, and annuity purchases require event governance. The committee should review the economic change, cash or asset transfer, immediate funded-status effect, OCI effect, future amortization, and line-item presentation. Ameren's disclosed ten-year amortization of an actuarial gain from a transfer illustrates why an event can produce a future earnings stream after the legal transaction is complete. The relevant question is not only whether accounting follows the standard but whether users can see the timing bridge.[8]

### Management should not use accounting assumptions as investment targets

The expected-return assumption is a reporting input, not a command to make the portfolio risky enough to justify it. Bergstresser, Desai, and Rauh's evidence that higher assumptions were associated with higher equity allocations identifies the worst inversion: the accounting rate influences asset risk instead of asset strategy and liability needs informing a defensible rate. A pension portfolio should be governed by benefit security, funded status, liquidity, risk capacity, and fiduciary duties, while the accounting assumption reflects the resulting strategy.[6]

Management should also resist solving one assumption through another. A favorable mortality table should not be offset by an artificially low discount rate to reach a preferred aggregate liability, and an aggressive return assumption should not be defended only because a conservative salary assumption offsets it. Each significant assumption needs its own reasonable basis, and their combination must remain coherent. PCAOB guidance explicitly requires both individual and combined evaluation.[5]

The reversible choice is greater transparency. Disclose the method, change attribution, and sensitivity before a rate becomes controversial. Preserve the difference between actual and expected return, show the AOCI queue, and explain how the plan's investment strategy changed. This does not eliminate estimation risk, but it makes later errors diagnosable and reduces the chance that a reasonable range becomes an unobservable earnings plug.[3][5][8][9]

### Cross-company comparison requires regime and plan-term normalization

A US GAAP company's expected-return credit cannot be compared directly with IFRS net interest. A frozen plan cannot be compared with an open final-salary plan through one discount rate. A mature retiree-heavy plan and a young active plan have different durations and mortality exposure. A funded pension trust and an unfunded postretirement medical promise have different asset and cash structures. Peer analysis must therefore control for accounting regime, plan status, benefit formula, currency, duration, participant mix, and asset allocation.[2][4][10]

Rate comparison still has value when those controls are present. A company materially above peers on expected return despite similar assets, or materially above a matched discount curve despite similar duration and currency, deserves explanation. The conclusion should remain probabilistic: a difference identifies where to investigate, while the roll-forwards, method, incentives, and subsequent experience determine whether the choice was reasonable, aggressive, or erroneous.[5][6][9]

Sensitivity disclosures should not be added as though all assumptions can move independently and linearly. Discount rate, salary growth, inflation, health-care trend, and asset returns can be correlated, and the obligation response can be nonlinear. The author's synthesis is to use company one-factor sensitivities for local attribution, then design coherent multi-factor stress scenarios for solvency and valuation. The one-factor table explains the model; the scenario tests the business.[3][4]

### Postretirement health care deserves a separate track

Other postretirement health benefits share the actuarial architecture but add medical-cost trend, plan cost sharing, Medicare or other public-program interaction, and claims uncertainty. FASB's one-percentage-point sensitivity requirement shows that a seemingly small change in trend can affect both the obligation and service-plus-interest cost. Analysts should not merge health plans with pensions merely because both appear in one note.[3]

A separate bridge should show the accumulated postretirement benefit obligation, any dedicated assets, participant contributions, employer benefits paid, health-care trend path, and sensitivity. A plan amendment that caps employer cost or changes eligibility can reduce the obligation without improving the underlying medical-cost environment. Conversely, a higher trend assumption can increase the obligation without changing current cash benefits. The same distinction among promise, estimate, expense, and cash remains essential.[3][4]

### The final conclusion should preserve uncertainty

Pension accounting offers real discretion because the underlying promise is long-dated and contingent, not because every assumption is arbitrary. Standards constrain discounting, attribution, recognition, presentation, and disclosure; auditors test methods, data, and assumptions; actuarial evidence informs mortality and other demographics. Within those constraints, reasonable estimates can differ. A robust analysis reports the range and the evidence rather than replacing management's point estimate with another unexplained point estimate.[3][4][5][10]

The strongest case for aggressive reporting is converging evidence: a favorable assumption outside a defensible method, a material current earnings effect, an incentive to reach a threshold, inconsistency with plan assets or company forecasts, opaque attribution, and later reversals or corrections. The strongest case for ordinary uncertainty is a stable method, current external and plan-specific evidence, symmetric response to favorable and unfavorable changes, complete roll-forwards, and transparent sensitivity. Neither case can be established from the direction of one rate change alone.[5][6]

The practical rule is simple. Rebuild what changed in the obligation, what changed in assets, what entered earnings, what stayed in OCI or AOCI, and what consumed cash. Only after those five questions reconcile should the analyst decide whether pension assumptions clarified economic uncertainty or reshaped the reported story.[1][3][5][8][9]

## Sources

1. Financial Accounting Standards Board (2006). "Statement of Financial Accounting Standards No. 158: Employers' Accounting for Defined Benefit Pension and Other Postretirement Plans."
   https://storage.fasb.org/fas158.pdf [high]

2. Financial Accounting Standards Board (2017). "Accounting Standards Update No. 2017-07: Improving the Presentation of Net Periodic Pension Cost and Net Periodic Postretirement Benefit Cost."
   https://storage.fasb.org/ASU%202017-07.pdf [high]

3. Financial Accounting Standards Board (2018). "Accounting Standards Update No. 2018-14: Disclosure Framework - Changes to the Disclosure Requirements for Defined Benefit Plans."
   https://storage.fasb.org/ASU%202018-14.pdf [high]

4. IFRS Foundation (2026). "IAS 19 Employee Benefits."
   https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias19.html [high]

5. Public Company Accounting Oversight Board. "AS 2501: Auditing Accounting Estimates, Including Fair Value Measurements."
   https://pcaobus.org/oversight/standards/auditing-standards/details/AS2501 [high]

6. Bergstresser, D., Desai, M. A., and Rauh, J. (2006). "Earnings Manipulation, Pension Assumptions, and Managerial Investment Decisions." Quarterly Journal of Economics, 121(1), 157-195. NBER working-paper version.
   https://www.nber.org/system/files/working_papers/w10543/w10543.pdf [high]

7. Kwan, S. H. (2003). "Pension Accounting and Reported Earnings." Federal Reserve Bank of San Francisco Economic Letter 2003-19.
   https://www.frbsf.org/research-and-insights/publications/economic-letter/2003/07/pension-accounting-and-reported-earnings [high]

8. Ameren Corporation (2026). "2025 Form 10-K, Retirement Benefits Note." U.S. Securities and Exchange Commission.
   http://sec.gov/Archives/edgar/data/18654/000100291026000009/R23.htm [high]

9. Ecolab Inc. (2026). "2025 Form 10-K, Pension and Post-Retirement Benefit Plans." U.S. Securities and Exchange Commission.
   http://sec.gov/Archives/edgar/data/31462/000110465926018357/ecl-20251231x10k.htm [high]

10. Society of Actuaries (2018). "U.S. Public Pension Plan Mortality Assumptions."
    https://www.soa.org/globalassets/assets/Files/resources/research-report/2018/public-pension-mortality.pdf [high]

## See Also

- `library/accounting-financial-shenanigans/forensic-accounting-methodology.md` -- the evidence hierarchy and cross-statement method for moving from an accounting anomaly to a supported conclusion.
- `library/accounting-financial-shenanigans/cookie-jar-reserves-and-expense-manipulation.md` -- how estimate changes and delayed recognition can shift earnings among periods.
- `library/valuation-screening/enterprise-value-equity-value-reconciliation.md` -- how pension deficits and forecast contributions enter the enterprise-to-equity bridge without double counting.
- `library/portfolio-risk-management/liability-driven-investing.md` -- how pension assets, liabilities, duration, funding, and liquidity interact outside the financial-reporting model.
