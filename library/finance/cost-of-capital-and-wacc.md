---
name: cost-of-capital-and-wacc
id: 20260827T053149Z
tier: library-topic
domain: finance
author: Librarian
tags: [cost-of-capital, wacc, capm, capital-structure, corporate-finance, discount-rate, hurdle-rate]
links: [library/finance/capital-structure-modigliani-miller.md, library/finance/financial-statement-analysis.md, library/finance/bond-pricing-and-fixed-income-markets.md, library/finance/dividend-policy-and-share-buybacks.md]
reviewed: 2026-09-30
---

# Cost of Capital and WACC -- A Discount Rate Is Valid Only When Claims, Risk, and Financing Match

The cost of capital is the opportunity return required by the providers of funds for bearing risks comparable to those of the cash flows being evaluated [7][9]. Weighted average cost of capital (WACC) combines the required returns on debt, equity, and any other material financing claims in proportions consistent with their economic values [7][8]. Its central limitation is also its governing rule: WACC is not a universal hurdle rate, and it is valid only when the cash-flow claim, currency, risk, tax treatment, and financing policy match the rate [6][7][9].

## Background

The modern cost-of-capital problem joined investment policy to security valuation. Modigliani and Miller began their 1958 paper by asking what capital costs when assets produce uncertain returns and a firm can issue claims ranging from fixed debt to residual equity. They replaced an ad hoc comparison with the interest rate on debt by a market-value test: an investment is worthwhile if it increases the market value of the firm. Under their idealized assumptions, including perfect capital markets, homogeneous risk classes, and the ability of investors to reproduce corporate leverage, Proposition I states that the value of a firm is independent of its financing mix. Proposition II states that the required return on equity rises with leverage because equity becomes a riskier residual claim [1].

The 1958 result did not say that real financing choices never matter. It established a benchmark: if changing the labels on claims leaves total cash flows unchanged and investors can reproduce the same payoffs, financing alone cannot create value. The useful questions therefore concern departures from that benchmark, including taxes, distress costs, contracting frictions, information differences, and agency conflicts. Modigliani and Miller also connected the benchmark to investment policy. Their Proposition III says that, within the model, a project should be accepted when its expected return reaches the capitalization rate for investments in the same risk class; the project's financing instrument does not by itself determine the cutoff [1].

Corporate taxes created the best-known departure. Modigliani and Miller's 1963 correction showed that an interest deduction can add value because it raises after-tax cash available to capital providers under the paper's assumptions [2]. The familiar after-tax debt term in WACC descends from that logic, but it is not an unconditional subsidy. A deduction has value only when applicable law permits it and the firm can use it. Current U.S. rules illustrate the qualification: Internal Revenue Code section 163(j) can limit deductible business interest to business interest income plus 30 percent of adjusted taxable income plus floor-plan financing interest, subject to exceptions and further rules [10]. The tax factor in a model must therefore represent the expected usable marginal benefit, not a statutory rate copied without analysis.

A second lineage addressed the required return on equity. Sharpe's 1964 equilibrium model built on portfolio selection and related expected return to systematic risk. His model assumes, among other restrictions, a common pure interest rate at which investors can borrow or lend and homogeneous investor expectations. Under those assumptions, prices adjust so that expected return is linearly related to exposure that cannot be diversified away; the regression response later expressed as beta is the quantity of that systematic exposure [3]. The standard CAPM equation, `Re = Rf + beta x ERP`, became a compact way to estimate an otherwise unquoted cost of equity.

The compact equation did not make its inputs observable constants. A risk-free proxy depends on currency, horizon, and default assumptions. Beta depends on the market proxy, estimation period, return frequency, business mix, and leverage. The equity risk premium is an expected return above the risk-free rate and must be estimated from historical or forward-looking evidence. Damodaran therefore treats cost of capital as a framework with multiple uses and multiple estimation choices, not as a directly quoted market price [7]. CFA Institute guidance likewise emphasizes that there is no single right method for every component and that target capital structure and the marginal tax rate require judgment [9].

Practice adopted the framework even as research documented its limits. Graham and Harvey surveyed 392 chief financial officers and found that 73.5 percent of respondents always or almost always used CAPM to estimate cost of equity. The same survey found that many firms used a company-wide discount rate for a project whose risk likely differed from the firm's existing assets [6]. Adoption therefore demonstrates institutional usefulness, not empirical truth or correct application.

The empirical record makes that distinction necessary. Fama and French's review concluded that the observed relation between beta and average return is flatter than the Sharpe-Lintner CAPM predicts and that other variables capture return differences left unexplained by beta. They described the model's empirical record as poor enough to invalidate many literal applications [4]. In a separate study of 48 U.S. industries, they found cost-of-equity estimates to be highly imprecise under both CAPM and a three-factor model, with typical annual standard errors above 3 percentage points even before moving from industries to individual firms or projects [5].

The resulting discipline is neither to discard WACC nor to treat it as measured fact. WACC remains a useful bridge between operating cash flows and the required returns of the claims financing those operations. Its value comes from forcing the analyst to state assumptions about risk, debt cost, tax capacity, and capital weights in a common framework. Its danger comes from allowing those assumptions to disappear behind one percentage. A defensible cost of capital is therefore an auditable estimate tied to a stated use, valuation date, and risk class [5][7][9].

## Core Concepts

### Start with the cash-flow claim

The discount-rate decision begins with the cash flow, not with a formula. Free cash flow to the firm is measured before distributions to debt and common equity and is ordinarily discounted at WACC, producing the value of operations available to all financing claims. Free cash flow to equity and dividends are residual cash flows after debt obligations and are discounted at a cost of equity. Applying WACC to an equity cash flow mixes a pre-debt rate with an after-debt claim; applying cost of equity to firm cash flow omits the required return of debt providers [7][8].

Units must also match. Nominal cash flows require nominal rates, while real cash flows require real rates. Cash flows and discount rates must use the same currency because expected inflation and currency-specific risk-free inputs affect both sides of the valuation. The issuer's domicile does not by itself choose the rate: a dollar forecast requires a dollar-consistent rate, and a euro forecast requires a euro-consistent rate. A long-lived stream also spans a term structure, so using one government yield is a modeling convention that must be disclosed rather than proof of a perfect maturity match [7].

Risk must be attached once. Diversifiable or event-specific risks that can be represented through scenarios may belong in expected cash flows, while market-wide exposure may belong in the discount rate. Charging the same downside through both a probability-weighted cash-flow reduction and an added discount-rate premium double counts it. The analyst should identify where each material risk enters and label any synthesis or judgment explicitly [7].

### The WACC equation and its scope

For a simple structure containing only interest-bearing debt and common equity, the standard equation is:

```
WACC = (E / V) x Re + (D / V) x Rd x (1 - T)
V = D + E
```

`E` and `D` are economic or market values, `Re` is the required return on common equity, `Rd` is the current pre-tax cost of debt, and `T` is the expected usable marginal tax rate on interest. The equation weights required returns according to the values of the claims that share the operating cash flows [7][8]. It is a compact representation of assumptions, not a rule that every firm has only two kinds of capital.

Material preferred stock, convertible securities, noncontrolling interests, or other hybrid claims require separate treatment or a defensible decomposition. Damodaran recommends separating a convertible bond into a debt component and an equity option when the distinction is material, while preferred stock may warrant a separate component because its fixed distribution resembles debt but its legal and tax treatment can resemble equity [7]. The objective is not to force every claim into two labels; it is to make the cash-flow rights and required returns consistent.

Lease obligations require the same consistency. IFRS 16 requires a lessee to recognize a lease liability for leases within its scope and subsequently increases that liability for interest while reducing it for payments; the discount rate is the implicit rate when readily determinable or otherwise the lessee's incremental borrowing rate [11]. The author's assessment is that a valuation decision to classify a lease liability as debt must be coordinated across enterprise cash flow, debt value, operating profit, and the cost-of-debt weight. Under that treatment, adding the liability to debt while leaving lease-related cash flows and earnings definitions unchanged would create a mismatch [7][11].

### Cost of equity is an estimate, not an invoice

Equity has no contractual coupon, so its cost is the return investors require for bearing the equity claim's risk. The standard CAPM estimate is:

```
Re = Rf + beta x ERP
```

`Rf` is a risk-free rate consistent with the cash-flow currency and nominal or real treatment. `Beta` estimates the equity's exposure to movements in a chosen market portfolio. `ERP` is the expected return on that market above the risk-free rate. Sharpe's theory supplies the systematic-risk logic, while Fama and French document why the empirical estimate should not be confused with a law of nature [3][4].

Each input requires provenance. The risk-free source, observation date, currency, and maturity convention should be recorded. Historical ERP estimates depend on the sample period, the return average, and the risk-free comparator; implied estimates depend on current prices, expected distributions, and growth assumptions. A beta estimate depends on the market index, frequency, window, and corporate events during the sample. Reporting the resulting cost of equity to several decimal places cannot recover information that the inputs do not contain [5][7].

A bottom-up beta can reduce noise and align the estimate with the business being valued. The analyst identifies comparable operating businesses, removes the effect of their leverage from equity betas under a stated model, averages or otherwise synthesizes the business-risk estimates, and then applies the target's financing policy. The process can be more transparent than accepting a vendor's single-company regression beta, but it remains sensitive to peer selection, business mix, debt treatment, and the relevering equation [7].

CAPM is not the only possible model. Multifactor models can represent size, value, profitability, investment, or other return patterns, while build-up approaches make extra premiums explicit. More factors do not automatically produce a more reliable company rate because every factor requires an exposure and an expected premium. Fama and French's industry evidence shows that uncertainty about factor premiums can dominate the apparent precision of estimated sensitivities [5]. Any added premium should therefore identify a distinct risk, explain why that risk is priced, and show that it is not already captured in beta or expected cash flows.

### Cost of debt and the usable tax benefit

The cost of debt is the return lenders currently require on claims of comparable currency, seniority, maturity, security, and default risk. It is not necessarily the coupon on an old bond or interest expense divided by book debt. A company may have issued low-coupon debt when rates and credit quality differed from conditions at the valuation date. A current borrowing cost can be estimated from traded debt, a current credit spread over a same-currency risk-free rate, or comparable borrowers when direct observations are unavailable [7].

The after-tax debt term must follow expected law and taxable capacity. In the simple formula, multiplying `Rd` by `(1 - T)` assumes that interest creates a contemporaneous tax saving at rate `T`. That assumption can fail when the firm has losses, when deductions are deferred, or when law caps deductible interest. Section 163(j) is a current U.S. example of a limit that can make the usable benefit differ from the statutory rate and shift it across periods [10]. A detailed model can forecast actual tax savings by period rather than burying a delayed or uncertain shield inside one constant factor [8][10].

Debt risk changes with leverage. Replacing equity with debt does not leave `Re` and `Rd` fixed: additional fixed claims make common equity more exposed to operating outcomes and can raise lender spreads as default risk increases. Tax benefits can also become less usable. A spreadsheet that increases the debt weight while holding the costs of debt and equity constant will mechanically push WACC down and manufacture an optimum that the assumptions themselves created [1][2][7].

### Capital weights, target policy, and circularity

WACC uses economic weights because it represents current required returns on the claims financing operating assets. Book equity records historical transactions and accounting adjustments; it is not a current price for the equity claim. For a listed firm, observed market capitalization and a defensible estimate of debt value can provide a starting point. For a private company, a division, or a transaction that changes financing, a supportable target capital structure based on policy and comparable businesses may be more relevant than the current mix [7][9].

Target weights do not eliminate judgment. They should describe a financing policy that can be maintained with the forecast's cash flows, credit risk, and maturity structure. If leverage is expected to change materially, one constant WACC can hide the transition. Period-specific WACCs, adjusted present value, or capital cash flow methods can expose changing debt balances and tax effects more clearly [7][8].

Market weights can create circularity because equity value is needed to calculate WACC while WACC is used to calculate equity value. Velez-Pareja and Tham show that this simultaneous relationship can be solved by iteration and that the weights belong to the relevant period's market values [8]. An adjusted present value method can instead value unlevered operations and financing effects separately. Neither method removes assumptions; the choice should make material assumptions more visible and produce internally consistent values.

### WACC is a risk-matched hurdle, not a company-wide commandment

A project creates value when its expected incremental cash flows have positive net present value after discounting at a rate appropriate to their risk. Company WACC is a suitable starting point only when the project has risk and financing exposure comparable to the assets represented by that WACC. A regulated utility project and a speculative biotechnology project inside one group should not inherit the same rate merely because they share a parent [6][7].

Using one company-wide rate systematically favors projects riskier than the existing business because their cash flows are discounted too lightly, while penalizing safer projects because they are discounted too heavily. Graham and Harvey's survey documents that this mismatch occurs in practice, and Damodaran explains how it can make a firm progressively riskier by accepting high-risk projects and rejecting low-risk ones [6][7]. A division or project rate should therefore be built from comparable operating risk and a financing policy appropriate to that risk class.

The author's assessment is that a hurdle rate may include a decision reserve for forecast optimism or scarce managerial capacity, but that reserve should not be mislabeled as the market cost of capital. Combining risk adjustment, strategic ranking, and organizational bias in one opaque percentage prevents reviewers from knowing why a project failed. Governance improves when the market-required rate, any policy buffer, and any capital-rationing rule are shown separately.

### A transparent calculation

Consider a hypothetical firm financed at target market weights of 80 percent common equity and 20 percent debt. Assume a 10.00 percent required return on equity, a 6.00 percent current pre-tax debt cost, and a 25 percent usable marginal tax rate. The after-tax debt cost is 4.50 percent, and tool-recalculated WACC is 8.90 percent:

```
WACC = 0.80 x 10.00% + 0.20 x 6.00% x (1 - 0.25)
     = 8.90%
```

The arithmetic follows the standard formula [8]. The 8.90 percent result is not evidence that the assumptions are correct. A defensible model would attach a date and source to the risk-free rate, ERP, beta, debt spread, tax usage, and target weights; test alternative estimates; and use the rate only for cash flows matching those assumptions [5][7][9].

## Evidence

### The Modigliani-Miller benchmark and its early tests

Modigliani and Miller's 1958 paper is a theoretical benchmark supported by an arbitrage argument, not a general empirical proof. Proposition I states that firms in the same risk class should have the same average cost of capital regardless of leverage under the model's conditions. Proposition II derives a higher expected equity return as debt-to-equity rises. Proposition III then ties the investment cutoff to the risk-class capitalization rate rather than to the interest rate on the particular financing instrument [1]. These propositions establish consistency conditions: cheaper debt cannot lower total capital cost for free because risk is transferred to equity.

The paper also reported preliminary tests using data assembled for 43 electric utilities in 1947-1948 and 42 oil companies in 1953. The authors regressed an approximation of after-tax return divided by market value on leverage. They reported correlation coefficients of 0.12 for utilities and 0.04 for oil companies, neither statistically significant, and found no evidence of the declining or U-shaped relation expected by the traditional view in those samples [1]. The method had serious limits that the authors acknowledged: tiny and old samples, crude risk-class definitions, actual earnings used as a proxy for expected earnings, and potentially biased ratio regressions. The result is historically informative but cannot establish a timeless capital-structure law.

The 1963 correction isolated corporate interest tax deductibility as a financing effect that can add value under specified assumptions [2]. Later practice often compresses that result into the `(1 - T)` term. Current tax rules show why the compression needs qualification. The IRS states that section 163(j), when applicable, limits deductible business interest to business interest income, 30 percent of adjusted taxable income, and floor-plan financing interest; disallowed amounts can be carried forward under the applicable rules [10]. The evidence therefore supports modeling an expected tax benefit, not assuming that every dollar of interest immediately earns the full statutory shield.

### CAPM gives a clear hypothesis that the data do not fully support

Sharpe's model derives a relationship between expected return and systematic exposure under restrictive equilibrium assumptions. It distinguishes total variability from the part associated with movements in an efficient market combination and argues that only the nondiversifiable component should be priced [3]. This is a testable organizing hypothesis and explains why beta, rather than standalone volatility, enters the standard cost-of-equity equation.

Fama and French's 2004 review compared that prediction with decades of tests. For ten beta-sorted portfolios using 1928-2003 data, they reported a beta-return relation much flatter than the Sharpe-Lintner line: the lowest-beta portfolio had a predicted annual return of 8.3 percent and an actual return of 11.1 percent, while the highest-beta portfolio had a predicted 16.8 percent and an actual 13.7 percent [4]. They also reviewed evidence that size and valuation ratios explain average-return differences not captured by beta. Their conclusion was not that required return is unnecessary; it was that CAPM's simple beta relation is an empirically weak literal description and that market-proxy problems affect both tests and applications [4].

The implication for WACC is model risk. CAPM remains transparent and widely understood, but a calculated cost of equity should be treated as a model-based estimate. A reviewer should ask whether the chosen beta, market proxy, and ERP are appropriate and whether alternative specifications change the decision. Familiarity with the equation is evidence of coordination value, not evidence that the estimate is exact [4][6].

### Cost-of-equity estimates are statistically imprecise

Fama and French's 1997 study examined monthly returns for 48 U.S. industry groups from 1963 through 1994 using CAPM and a three-factor model. They evaluated uncertainty from both factor sensitivities and the expected factor premiums used to convert those sensitivities into required returns [5]. The industry level is important: pooling companies should be easier than estimating one firm or one project, so large uncertainty there is a warning against company-specific precision.

The study reported that typical annual standard errors exceeded 3 percentage points for cost-of-equity estimates under both models. Uncertainty about market and factor premiums contributed more than the apparent precision of full-period regression slopes suggested. The authors described industry cost-of-equity estimates as distressingly imprecise and stated that firm and project estimates would be less precise still [5]. This evidence directly contradicts presentation of WACC to the nearest basis point without a sensitivity range.

### Corporate practice combines adoption with inconsistent risk matching

Graham and Harvey sent a broad corporate-finance survey to approximately 4,440 firms and received 392 completed responses, a response rate near 9 percent. The survey measured reported practices and beliefs rather than audited decisions, and the authors explicitly identified that limitation [6]. Within that design, 74.9 percent of CFOs reported always or almost always using net present value, 75.7 percent reported the same for internal rate of return, and 73.5 percent of firms that estimated cost of equity reported always or almost always using CAPM [6].

The project-risk questions expose the gap between method and application. For a hypothetical overseas project, 58.8 percent of respondents said they would always or almost always use the company-wide discount rate, while 51.0 percent said they would always or almost always use a risk-matched rate considering country and industry; the responses were not mutually exclusive [6]. More than half using the firm rate for a project likely to have different risk is evidence that a theoretically standard WACC can be applied inconsistently. The survey also found greater use of risk-matched rates among larger firms, but it did not verify realized project choices or outcomes [6].

### Financial statements changed, but economic consistency remains necessary

IFRS 16 requires a lessee to recognize lease liabilities for leases within its scope and to recognize interest on the remaining liability [11]. The author's assessment is that this improves visibility but does not settle every valuation classification. A WACC model that treats the liability as debt should use cash flows and operating measures that treat the related financing consistently. The standard is evidence about recognized claims; the valuation model remains responsible for matching those claims to its numerator and denominator.

Taken together, the evidence supports a limited conclusion. Cost-of-capital frameworks organize the relationship among operating risk, financing claims, taxes, and valuation. The evidence does not support a universally correct CAPM beta, a basis-point-precise WACC, one rate for all projects, or an automatic tax shield. The strongest use of WACC is as an explicit, testable set of assumptions whose alternatives are shown, not as a single authoritative number [4][5][6][7].

## Implications

### For capital budgeting

A capital-budgeting committee should build the hurdle rate backward from the proposed cash flows. It should first identify whether the forecast is a firm or equity claim, then specify currency and nominal or real treatment, then classify the project's operating risk using relevant comparables, and only then apply a financing policy and tax treatment. This sequence prevents a project sponsor from starting with the parent company's WACC and adjusting it until a preferred decision appears acceptable [6][7].

The committee should show three layers separately. The first is the market-required rate for the project's risk. The second is any explicit scenario adjustment to expected cash flows. The third is any policy buffer for optimism, capital scarcity, or execution capacity. A project can fail because market value is negative, because the organization lacks resources, or because management distrusts the forecast; those are different findings. The author's assessment is that combining them in one undisclosed premium weakens both accountability and learning.

The review should also compare project return and rate on consistent bases. Accounting ROIC can be a useful operating diagnostic, but it must use an invested-capital definition aligned with the after-tax operating profit being measured. Project NPV is more direct because it values incremental cash flows at a matching rate. A positive accounting profit does not establish value creation if the capital committed could earn more at comparable risk elsewhere [1][7].

Post-investment review should preserve the original rate bridge and forecast. Actual outcomes can then be separated into operating forecast error, financing changes, tax changes, and market-rate changes. Without that record, a company cannot tell whether a failed project reflected a bad business forecast or a discount rate that never matched the project. Graham and Harvey's evidence of company-wide rate use makes this control especially important [6].

### For valuation

An enterprise DCF should reconcile the operating cash flow, WACC, and claims bridge. Free cash flow to the firm discounted at WACC produces operating enterprise value; debt, lease obligations treated as financing, preferred claims, noncontrolling interests, excess cash, and other nonoperating items must then be handled consistently to reach common equity value. An equity DCF instead discounts residual equity cash flow at cost of equity. The two approaches should tell compatible economic stories when assumptions are aligned [7][8][11].

Sensitivity analysis is not optional when the discount rate is uncertain. Consider a tool-recalculated hypothetical perpetuity with next-period cash flow of 100 and constant growth of 3 percent. Using `Value = FCF1 / (WACC - g)`, value is 2,000.00 at an 8 percent rate, 1,666.67 at 9 percent, and 1,428.57 at 10 percent. Moving from 8 to 10 percent reduces the illustrated value by 28.57 percent even though cash flow and growth are unchanged. The calculation illustrates denominator sensitivity; it is not an estimate for any company [7].

A two-way WACC and terminal-growth table is useful for local sensitivity, but scenarios should also vary assumptions that share an economic cause. Inflation, nominal growth, risk-free rates, credit spreads, margins, and refinancing costs may move together. Holding every other input fixed while moving WACC can identify mathematical exposure, but it is not a complete economic scenario. The author's assessment is that both a local grid and coherent scenarios are needed when terminal value is material.

Rate provenance should be reproducible. A valuation file should record the date and source of the risk-free rate, the ERP method and vintage, beta or comparable set, current debt spread, tax limitation assumptions, lease treatment, and market or target capital weights. Fama and French's uncertainty estimates and the time-varying inputs described by Damodaran explain why an unlabeled percentage becomes stale or irreproducible [5][7].

### For capital-structure policy

Management should not search for an optimal debt ratio by mechanically increasing the debt weight in a fixed WACC formula. As leverage rises, common equity becomes riskier, debt spreads can rise, tax deductions can become less usable, and distress can reduce operating cash flows. All material components must respond. Modigliani and Miller's benchmark shows why merely replacing a higher quoted equity return with a lower quoted debt return cannot create value without changing total cash flows or exploiting a real friction [1][2][7].

A target capital structure should be an economic policy rather than a copied peer median. It should be consistent with cash-flow volatility, asset durability, covenant headroom, refinancing needs, and the ability to use tax deductions. CFA Institute guidance identifies long-term target structure and marginal tax rate as central assumptions, while U.S. interest limitations demonstrate that statutory tax rates do not guarantee contemporaneous shields [9][10].

When leverage is expected to change materially, period-specific WACC or adjusted present value can be clearer than one constant rate. Adjusted present value separates the value of unlevered operations from financing effects, while a period-specific WACC incorporates the changing claim weights and costs directly. Velez-Pareja and Tham show that consistent methods can reconcile when cash flows, tax savings, values, and timing assumptions are aligned [8]. The preferred method is the one that exposes rather than conceals the financing forecast.

### For boards, investors, and lenders

Boards should treat WACC as a governed assumption. Approval materials should state who owns each input, when it was updated, what source supports it, how project risk differs from firm risk, and how the decision changes across a defensible range. A round-number hurdle rate can be a policy choice, but it should not be represented as a current market estimate unless its construction supports that claim [5][6][9].

Investors can use the spread between return on invested capital and WACC as a diagnostic, not a standalone verdict. Both sides contain measurement choices: acquisitions, leases, goodwill, excess cash, capitalization policy, and tax treatment affect invested capital and operating return, while risk models and financing assumptions affect WACC. A sustained positive spread under consistent definitions suggests that operations earn more than the modeled opportunity cost, but it does not prove that every incremental investment creates value [7].

A simple illustration shows the unit discipline. If one additional unit of capital produces a one-period after-tax operating return of 12 percent and its matching capital charge is 8 percent, tool-recalculated economic profit for that period is 0.04 unit. The 4-percentage-point spread does not mean that any firm with reported 12 percent ROIC creates four cents forever; duration, reinvestment, fade, and risk still determine value. The example is interpretation, not a company finding.

Lenders and credit analysts should focus on the pre-tax debt cost and repayment capacity before treating debt as a cheap WACC input. A low coupon can reflect an old issuance, collateral, or seniority rather than the current marginal borrowing cost. Increasing leverage can raise both default spreads and equity risk, while interest limitations can defer the assumed tax benefit [7][10]. The debt term should therefore be read as a market-required return on a specified claim, not as evidence that more borrowing necessarily lowers total capital cost.

### A practical decision rule

A cost of capital is defensible when another informed reviewer can reconstruct it and when every component answers the same economic question. The cash flow and rate must match by claimant, currency, nominal or real treatment, horizon, and risk. Financing weights must be economic or target values appropriate to the forecast. Debt cost must be current, the tax shield must be legally and economically usable, and material hybrids or lease claims must be treated consistently [7][8][9][10][11].

The output should normally be a range or scenario set when the decision is sensitive to disputed inputs. CAPM can remain the transparent baseline because its equation and evidence are widely understood, while alternative betas, ERPs, or factor models reveal model risk. Fama and French's findings justify humility, not arbitrary premiums [4][5]. The final question is not whether the spreadsheet calculates WACC. It is whether the investment or valuation conclusion survives the set of assumptions that the available evidence can support.

## Sources

1. Modigliani, F. & Miller, M. H. (1958). "The Cost of Capital,
   Corporation Finance and the Theory of Investment." American Economic
   Review, 48(3), 261-297.
   https://www.aeaweb.org/aer/top20/48.3.261-297.pdf [high]

2. Modigliani, F. & Miller, M. H. (1963). "Corporate Income Taxes and
   the Cost of Capital: A Correction." American Economic Review, 53(3),
   433-443. https://www.jstor.org/stable/1809167 [high]

3. Sharpe, W. F. (1964). "Capital Asset Prices: A Theory of Market
   Equilibrium under Conditions of Risk." Journal of Finance, 19(3),
   425-442. https://doi.org/10.1111/j.1540-6261.1964.tb02865.x [high]

4. Fama, E. F. & French, K. R. (2004). "The Capital Asset Pricing
   Model: Theory and Evidence." Journal of Economic Perspectives, 18(3),
   25-46. https://doi.org/10.1257/0895330042162430 [high]

5. Fama, E. F. & French, K. R. (1997). "Industry Costs of Equity."
   Journal of Financial Economics, 43(2), 153-193.
   https://doi.org/10.1016/S0304-405X(96)00896-3 [high]

6. Graham, J. R. & Harvey, C. R. (2001). "The Theory and Practice of
   Corporate Finance: Evidence from the Field." Journal of Financial
   Economics, 60(2-3), 187-243.
   https://people.duke.edu/~jgraham/website/SurveyPaper.PDF [high]

7. Damodaran, A. (2016). "The Cost of Capital: The Swiss Army Knife of
   Finance." New York University Stern School of Business.
   https://pages.stern.nyu.edu/adamodar/pdfiles/papers/costofcapital.pdf
   [high]

8. Velez-Pareja, I. & Tham, J. (2009). "Market Value Calculation and
   the Solution of Circularity Between Value and the Weighted Average
   Cost of Capital WACC." RAM - Revista de Administracao Mackenzie,
   10(6), 101-131.
   https://www.redalyc.org/pdf/1954/195415661007.pdf [high]

9. CFA Institute (2025). "Cost of Capital: Advanced Topics."
   CFA Program Level II Corporate Issuers refresher reading.
   https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2025/cost-capital-advanced-topics
   [high]

10. Internal Revenue Service (2026). "Questions and Answers About the
    Limitation on the Deduction for Business Interest Expense." Updated
    August 19, 2026.
    https://www.irs.gov/newsroom/questions-and-answers-about-the-limitation-on-the-deduction-for-business-interest-expense
    [high]

11. IFRS Foundation (2024). "International Financial Reporting Standard
    16 Leases." Issued Standards.
    https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2024/issued/ifrs16.html
    [high]

## See Also

- `library/finance/capital-structure-modigliani-miller.md` -- the
  benchmark showing when financing claims do and do not change total
  value.
- `library/finance/financial-statement-analysis.md` -- the accounting
  inputs that must be reconciled before debt, tax, and invested-capital
  measures can enter a WACC model.
- `library/finance/bond-pricing-and-fixed-income-markets.md` -- the
  yield, spread, maturity, and credit concepts used to estimate current
  debt cost.
- `library/finance/dividend-policy-and-share-buybacks.md` -- the payout
  decision after investment opportunities have been compared with a
  risk-matched capital cost.
- `library/finance/yield-curve.md` -- the term-structure context for
  selecting a risk-free input.