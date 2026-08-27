---
name: cost-of-capital-and-wacc
id: 20260827T053149Z
tier: library-topic
domain: finance
author: Library-Runner
tags: [cost-of-capital, wacc, capm, capital-structure, corporate-finance, discount-rate, hurdle-rate]
links: [library/finance/capital-structure-modigliani-miller.md, library/finance/financial-statement-analysis.md, library/finance/bond-pricing-and-fixed-income-markets.md, library/finance/dividend-policy-and-share-buybacks.md]
---

# Cost of Capital and WACC -- Why the Price of Funding Determines Every Investment Decision

The cost of capital is the minimum return a company must earn on its
investments to satisfy the investors and lenders who provide its
funding. The weighted average cost of capital (WACC) blends the cost
of equity and the after-tax cost of debt into a single discount rate,
weighted by how much of each source the company uses. WACC is the
hurdle rate for capital budgeting, the discount rate in discounted
cash flow valuation, and the dial that tunes a firm's optimal mix of
debt and equity -- making it, as Aswath Damodaran puts it, the "Swiss
Army knife of finance."

## Background

The concept of a cost of capital emerged from a deceptively simple
question: what discount rate should a company use when evaluating
whether a new project is worth pursuing? Before the 1950s, the
answer was ad hoc. Companies used rules of thumb, historical
averages, or whatever rate their banker quoted. There was no
unifying theory that connected the cost of debt, the cost of equity,
and the mix between them into a single coherent framework.

The intellectual foundation was laid by Franco Modigliani and Merton
Miller in their landmark 1958 paper, "The Cost of Capital,
Corporation Finance, and the Theory of Investment," published in the
American Economic Review. Their central insight was that in a
frictionless world with no taxes, no bankruptcy costs, and no
information asymmetry, the value of a firm is independent of how it
finances itself. Capital structure -- the mix of debt and equity --
is irrelevant to firm value. This proposition, now known as the
Modigliani-Miller theorem, earned both authors Nobel Prizes and
fundamentally changed how finance was taught and practiced.

The implication was profound: if capital structure does not matter
in a perfect world, then the things that make it matter in the real
world -- taxes, bankruptcy costs, agency costs, asymmetric
information -- are precisely what finance theory must study. The
Modigliani-Miller theorem was not the end of the debate but the
beginning. It told the field exactly which frictions to model.

The other pillar of cost of capital theory arrived in 1964 when
William Sharpe published "Capital Asset Prices: A Theory of Market
Equilibrium under Conditions of Risk" in the Journal of Finance.
Building on Harry Markowitz's portfolio theory from 1952, Sharpe
developed the Capital Asset Pricing Model (CAPM), which provided a
formula for the cost of equity: the risk-free rate plus beta times the
equity risk premium. Sharpe, Markowitz, and Merton Miller jointly
received the 1990 Nobel Prize in Economic Sciences for this body of
work. Jack Treynor, John Lintner, and Jan Mossin independently
developed similar models around the same time, but Sharpe was the
first to publish.

The CAPM answered a question that had vexed corporate finance since
before Modigliani and Miller: how do you estimate the cost of equity?
Unlike debt, equity has no contractual interest rate. Shareholders do
not hand you a bill. The cost of equity is an opportunity cost -- the
return shareholders could earn on an investment of equivalent risk
elsewhere. CAPM made that abstract concept computable: you need a
risk-free rate (typically the 10-year Treasury yield), a measure of
the stock's sensitivity to market risk (beta), and an estimate of the
equity risk premium (the extra return the market delivers over the
risk-free rate).

The WACC formula itself was derived by Modigliani and Miller in their
original 1958 paper. It combines the cost of equity and the cost of
debt, weighted by their proportions in the capital structure, with
the cost of debt adjusted for the tax deductibility of interest
payments. The formula is simple to state but notoriously difficult to
apply correctly, because each input requires estimation choices that
can swing the final number by several percentage points -- and a
one-percentage-point change in WACC can shift a DCF valuation by 15
to 25 percent, as practitioners have observed.

Damodaran, in his 2016 paper "The Cost of Capital: The Swiss Army
Knife of Finance," argued that the cost of capital is the single most
used and most misunderstood number in all of finance. It serves as
the hurdle rate for investment decisions, the discount rate for
valuation, the optimizing variable for capital structure decisions,
and the signal for whether to return cash to shareholders via
dividends or buybacks. No other number in finance plays so many
roles simultaneously.

## Core Concepts

### The WACC Formula

The weighted average cost of capital blends the cost of each capital
source by its share of total capital:

    WACC = (E/V) * Re + (D/V) * Rd * (1 - T)

Where E is the market value of equity, D is the market value of
debt, V equals E plus D (total capital), Re is the cost of equity, Rd
is the pre-tax cost of debt, and T is the marginal corporate tax rate.
The equity weight E/V and debt weight D/V must always use market
values, not book values. A company with 30 billion in book equity but
a 200 billion market capitalization is overwhelmingly equity-financed
on a market basis, and its WACC must reflect that. Using book values
inflates the debt weight, understates WACC, and produces inflated
valuations -- this is the single most common error in practical WACC
calculation, as identified by practitioners and academic reviewers
alike.

The tax adjustment on the debt component -- multiplying Rd by (1 - T)
-- reflects the interest tax shield. Interest payments are
tax-deductible in the United States and most developed economies.
The government effectively subsidizes corporate debt by allowing
interest to reduce taxable income. If a company borrows at 6 percent
pre-tax and faces a 25 percent tax rate, the after-tax cost of debt
is 6 percent times 0.75, or 4.5 percent. This tax shield is what makes
debt cheaper than equity on an after-tax basis and is the reason the
Modigliani-Miller theorem with taxes (1963) concludes that, in the
absence of bankruptcy costs, a firm should borrow as much as possible.

### The Cost of Equity and CAPM

The cost of equity is the return shareholders require for bearing the
risk of holding the company's stock. Unlike debt, equity has no
contractual yield. The most widely used method to estimate it is the
Capital Asset Pricing Model:

    Re = Rf + beta * (Rm - Rf)

Where Rf is the risk-free rate (typically the 10-year Treasury
yield), beta measures the stock's sensitivity to market movements,
and (Rm - Rf) is the equity risk premium -- the extra return investors
demand for holding the market portfolio rather than a risk-free
asset.

Each input carries estimation challenges. The risk-free rate must
match the duration of the cash flows being discounted. For a DCF with
a 10-year horizon, the 10-year Treasury is appropriate. Using the
3-month T-bill rate inflates the equity risk premium and produces a
structurally inconsistent WACC. The equity risk premium can be
estimated historically (the S&P 500's average excess return over
Treasuries, roughly 5 to 7 percent over long periods) or as an
implied premium (Damodaran publishes monthly implied ERP estimates,
currently around 5 percent as of 2026).

Beta itself requires careful estimation. A raw regression of the
stock's returns against the market index is noisy. Practitioners
adjust raw beta using the Blume adjustment (which shrinks beta toward
1.0, reflecting the empirical observation that extreme betas tend to
revert) or the Vasicek method (a Bayesian shrinkage weighted by
estimation uncertainty). When valuing a private company or a division
with no traded equity, analysts use the bottom-up beta approach:
calculate unlevered betas for a peer group, average them, then relever
to the target company's capital structure using the Hamada equation.

### The Cost of Debt

The cost of debt is the yield to maturity on the company's
outstanding debt, adjusted for taxes. For a company with publicly
traded bonds, this yield is directly observable in the market. For a
private company, analysts add a credit spread to the risk-free rate
based on the company's credit rating or the rating of comparable
borrowers.

A critical decision is whether to use the rate on existing debt or
the rate on new debt. WACC measures the marginal cost of capital --
what it would cost to raise new financing today. A company that
locked in low rates years ago should not use those rates for WACC
purposes, because they reflect a sunk cost, not the current cost of
capital. The relevant question for a new investment is: what would we
pay to borrow today?

Post-IFRS 16 and ASC 842, operating leases appear on the balance
sheet as right-of-use assets and corresponding liabilities. These are
interest-bearing obligations and must be included in total debt for a
complete WACC calculation. Excluding them understates the debt weight
and overstates WACC.

### Capital Structure Weights

The weights in the WACC formula -- E/V and D/V -- reflect the
proportions of equity and debt financing. These should be based on
target capital structure, not the current spot mix. If a company
plans to shift its debt-to-equity ratio over time, the WACC should
reflect the long-term target, not a transient snapshot. The
Modigliani-Miller framework tells us that in a world with taxes but
no bankruptcy costs, the optimal capital structure is 100 percent
debt, because every additional dollar of debt generates a tax shield
without raising the cost of equity enough to offset it. In the real
world, bankruptcy costs, agency costs, and financial distress create
a U-shaped WACC curve: WACC falls as debt increases (due to the tax
shield), reaches a minimum, then rises as financial distress costs
overwhelm the tax benefit. The optimal capital structure is the point
where WACC is minimized, which maximizes firm value.

### The Hurdle Rate and Investment Decisions

WACC serves as the hurdle rate for capital budgeting. A project must
generate returns above WACC to create value. If a company's WACC is
8.5 percent, any new project funded with the same mix of equity and
debt must earn more than 8.5 percent to justify the capital it
consumes. Projects earning below WACC destroy value, even if they are
profitable in absolute terms.

Damodaran identifies a common mistake: using a single company-wide
WACC for all projects, even when divisions have very different risk
profiles. A mature utility division and a speculative biotech venture
inside the same holding company have radically different risk
characteristics. Applying the parent company's blended WACC to both
overstates the utility's hurdle (rejecting good safe projects) and
understates the venture's hurdle (accepting bad risky projects). Over
time, the company gets riskier because it systematically rejects its
safest investments and accepts its riskiest ones. The fix is to
estimate division-specific costs of capital using division-specific
betas and capital structures.

### The Tax Shield and Its Limits

The tax deductibility of interest is the primary reason debt lowers
WACC on an after-tax basis. But the tax shield has limits. If a
company generates net operating losses, it pays no taxes and cannot
immediately use the interest deduction. In that case, the effective
tax rate is zero, and the after-tax cost of debt equals the pre-tax
cost. Tax exhaustion -- the point at which a company has more
interest deductions than taxable income -- removes the tax advantage
of debt entirely. The marginal tax rate, not the average or statutory
rate, is the correct input for WACC, because WACC measures the cost
of the next dollar of capital raised.

### WACC as Opportunity Cost

For investors, the cost of capital is an opportunity cost: the return
they could earn on an investment of equivalent risk elsewhere. For
the company, it is a cost of financing: the company must deliver
returns that beat or match the cost of capital to keep investors
satisfied. This dual nature is what makes WACC simultaneously a
valuation input (the discount rate) and a performance benchmark (the
hurdle rate). When a company earns a return on invested capital above
its WACC, it creates economic value. When it earns below WACC, it
destroys value, regardless of whether it is profitable in accounting
terms.

## Evidence

### The Modigliani-Miller Propositions

The empirical foundation of cost of capital theory rests on the
Modigliani-Miller propositions. Their 1958 paper proved that in a
world without taxes, WACC is constant at all levels of gearing. As a
company adds debt, the decrease in WACC from cheaper debt is exactly
offset by the increase in the cost of equity due to higher financial
risk. No optimal capital structure exists.

Their 1963 follow-up, "Corporate Income Taxes and the Cost of
Capital: A Correction," admitted corporate taxes into the analysis.
With taxes, the tax shield makes debt cheaper on an after-tax basis,
and WACC falls monotonically as gearing increases. The optimal
capital structure becomes 100 percent debt -- an extreme result that
no real company follows, because the model omits bankruptcy costs.

The trade-off theory of capital structure reconciles the MM
propositions with observed behavior. It posits a U-shaped WACC curve:
WACC falls as debt increases (the tax shield dominates), reaches a
minimum, then rises as expected bankruptcy costs -- legal fees,
distress-sale discounts, lost customers, and damaged supplier
relationships -- outweigh the tax benefit. The optimal capital
structure is the debt level that minimizes WACC. Empirical studies
confirm that companies with stable, tangible cash flows (utilities,
real estate) carry more debt than companies with volatile, intangible
assets (technology, biotech), consistent with the trade-off model's
predictions about bankruptcy costs.

### CAPM Empirical Performance

The CAPM has been tested extensively since its introduction. Fama and
French (2004) surveyed the evidence in "The CAPM: Theory and
Evidence," published in the Journal of Economic Perspectives. They
found that while the CAPM's core intuition -- that higher beta should
command higher expected returns -- is directionally correct, the
model's quantitative predictions are poor. The security market line
(the relationship between beta and expected return) is too flat:
low-beta stocks earn more than CAPM predicts, and high-beta stocks
earn less. This empirical failure motivated the Fama-French
three-factor model, which adds size and book-to-market factors, and
subsequent multifactor models (Carhart's four-factor, Fama-French
five-factor).

Despite these empirical shortcomings, CAPM remains the dominant model
for estimating the cost of equity in practice. Its simplicity,
transparency, and wide acceptance in the CFA curriculum and corporate
finance textbooks sustain its dominance. Damodaran, who uses CAPM in
his own valuations, acknowledges its limitations but argues that the
alternatives (dividend discount model, build-up method) introduce
their own estimation errors without clearly improving accuracy.

### WACC Estimation Errors in Practice

Velez-Pareja (2013), in "WACC Calculations in Practice: Incorrect
Results due to Inconsistent Assumptions," published in Accounting and
Finance Research, documented systematic errors in how practitioners
compute WACC. The most common errors include: using book values
instead of market values for capital structure weights; assuming a
debt beta of zero while setting the pre-tax cost of debt above the
risk-free rate (an internally inconsistent assumption that biases
WACC upward); using the effective tax rate instead of the marginal
tax rate; and failing to include operating lease liabilities in total
debt. Velez-Pareja showed that these errors compound: a WACC computed
with book weights, a stale risk-free rate, and the wrong tax rate can
differ from a correctly computed WACC by 200 to 300 basis points --
enough to change a valuation by 30 to 50 percent.

Practitioner sources (Corporate Finance Institute, Wall Street Prep,
Damodaran's teaching materials) consistently identify the same five
errors as the most common WACC mistakes: (1) using book value instead
of market value for equity, (2) using a short-term risk-free rate for
long-horizon valuations, (3) blending the effective and marginal tax
rates, (4) ignoring operating lease debt, and (5) using a single
company-wide WACC for divisions with different risk profiles. A
company with 30 billion in book equity and a 200 billion market
capitalization is overwhelmingly equity-financed on a market basis.
Using book value inflates the debt weight, understates WACC, and
produces inflated DCF valuations. Similarly, a company that locked
in debt at 3 percent during 2021 should not use that rate in a 2026
WACC calculation when current market rates are 5 to 6 percent. WACC
measures the marginal cost of capital -- what it would cost to raise
new financing today -- not the historical cost of existing funding.

### The Pecking Order as Competing Evidence

The pecking order theory, proposed by Stewart Myers and Nicolas
Majluf in 1984, offers an alternative to the trade-off model. They
argued that information asymmetry between managers and outside
investors makes external equity issuance signal overvaluation. As a
result, companies prefer internal funds first, then debt, and only
issue equity as a last resort. This prediction is empirically
supported: companies announce equity offerings and their stock prices
typically drop 2 to 3 percent on average, consistent with the signaling
interpretation. The pecking order implies that observed capital
structures are not the result of optimizing WACC but of cumulative
financing decisions driven by information costs. Companies with
strong cash generation tend to have low debt not because they have
reached an optimal WACC, but because they rarely need external
financing.

### The Equity Premium Puzzle and WACC Sensitivity

The equity risk premium is the single most consequential input in
WACC, because it is multiplied by beta and affects the cost of equity,
which typically carries the largest weight in the capital structure.
Historical estimates of the ERP range from 3 percent (forward-looking
implied estimates) to 7 percent (long-run historical averages). A
2-percentage-point difference in ERP translates directly into a
2-percentage-point change in cost of equity for a company with beta
of 1.0, which can swing WACC by 1.5 to 2 percentage points and a
10-year DCF valuation by 20 to 30 percent.

Damodaran publishes monthly implied ERP estimates derived from
current market prices and expected cash flows, arguing that
forward-looking implied premiums are more relevant than backward-
looking historical averages. As of 2026, his implied ERP for the
United States is approximately 5 percent, while the long-run
historical average (1928 to present) is closer to 6 percent. The
choice between these two approaches is not academic: it directly
determines whether a company's hurdle rate is set at 8 percent or 10
percent, which determines whether marginal projects are accepted or
rejected.

## Implications

### For Corporate Investment Decisions

WACC is the threshold that separates value creation from value
destruction. A company that consistently invests in projects earning
below its cost of capital will destroy shareholder value, even if
those projects are profitable in accounting terms. This is why
return on invested capital (ROIC) relative to WACC is the single best
measure of whether a company is creating or destroying economic value.
ROIC above WACC means the company earns more than its capital costs;
ROIC below WACC means it earns less. A company can grow earnings
every year and still destroy value if it grows by deploying capital
at returns below its cost of capital.

The discipline of hurdle rates prevents the most common form of
value destruction: empire building. Managers who want to increase
revenue, headcount, or market share have a natural incentive to lower
the hurdle rate to justify marginal acquisitions or expansions. A
rigorous WACC estimate, defended with market-value weights and a
current risk-free rate, is the institutional defense against this
bias. Companies that use a round-number WACC ("we use 10 percent for
everything") without re-examining it as rates change are likely using
a stale number that no longer reflects their actual cost of capital.
As rates rose from 2021 to 2024, a company that kept its 2021 WACC of
7 percent was understating its true cost of capital by 200 to 300
basis points, potentially accepting projects that destroy value.

### For Valuation

WACC is the discount rate in a free cash flow to firm (FCFF) DCF
model. The present value of a company's future cash flows, discounted
at WACC, minus net debt, equals equity value. Because DCF valuations
discount 10 or more years of cash flows, small WACC errors compound
dramatically. A 1 percentage point change in WACC can shift a
company's implied enterprise value by 15 to 25 percent, depending on
the duration and growth profile of the cash flows. Long-duration
growth stocks (high beta, most of the value in terminal value) are
most sensitive; mature, cash-generative businesses with most of their
value in near-term cash flows are less sensitive.

This sensitivity is why practitioners run WACC as a range, not a point
estimate. If two reasonable analysts would estimate cost of equity
between 9 and 11 percent, a valuation that only works at exactly 9.0
percent is not robust. Sensitivity analysis -- varying WACC by plus
or minus 100 basis points and observing the effect on fair value --
is standard practice in equity research and M&A modeling.

### For Capital Structure Decisions

WACC is the optimizing variable for capital structure. The search for
the optimal mix of debt and equity is the search for the lowest WACC,
because minimizing WACC maximizes firm value (firm value equals future
cash flows divided by WACC). The trade-off theory predicts an
interior optimum where the marginal tax benefit of debt equals the
marginal expected cost of financial distress. The pecking order
theory offers a competing view: companies prefer internal funds
first, then debt, then equity, because external financing signals
adverse information about valuation.

In practice, most companies target a debt-to-equity ratio well below
the theoretical optimum implied by the trade-off model, a phenomenon
known as the debt conservatism puzzle. Possible explanations include
the desire for financial flexibility (keeping dry powder for
acquisitions), the agency costs of debt (covenants restrict
management discretion), and the fact that financial distress costs
are difficult to quantify and managers are loss-averse. The cost of
capital framework provides the analytical lens for evaluating these
trade-offs: each increment of debt lowers WACC through the tax shield
but raises it through higher expected distress costs.

### For Dividend and Buyback Policy

The cost of capital determines whether a company should return cash to
shareholders or reinvest it. If a company's ROIC exceeds its WACC, it
should reinvest earnings because the return on new investment exceeds
the cost of capital. If ROIC is below WACC, the company destroys value
with every dollar it invests, and it should return cash to
shareholders via dividends or buybacks. This is the economic logic
behind the dividend policy decision: the cost of capital is the
benchmark against which investment opportunities are measured.

A company with a 12 percent ROIC and an 8 percent WACC should invest
as much as it profitably can, because every dollar deployed creates
4 cents of economic value. A company with a 6 percent ROIC and an 8
percent WACC should return all excess cash to shareholders, because
reinvesting it destroys 2 cents per dollar. The cost of capital is
thus inseparable from dividend policy -- it is the threshold that
determines whether reinvestment or distribution is the value-maximizing
choice. Warren Buffett's test for whether retained earnings are
justified -- does the company earn above its cost of capital on those
retained earnings? -- is a direct application of this principle.

### For Cross-Domain Connections

Cost of capital connects corporate finance to valuation, accounting,
and market microstructure. Financial statement analysis provides the
inputs (debt levels, tax rates, capital structure) that feed into
WACC. Bond pricing determines the cost of debt through yield to
maturity. Capital structure theory (the Modigliani-Miller framework)
explains why the mix matters and when it does not. Dividend policy is
the decision about what to do with cash once the hurdle rate has been
cleared. The yield curve provides the risk-free rate. Each of these
topics is a component of the cost of capital calculation, and WACC is
the synthesis that brings them together into a single actionable
number.

The cost of capital also connects to macroeconomics through the
risk-free rate. When central banks raise rates, the risk-free rate
rises, which raises the cost of equity through CAPM and raises the
cost of debt directly. The entire WACC curve shifts upward. This is
why rising-rate environments are generally negative for equity
valuations: the discount rate increases, reducing the present value
of future cash flows. Conversely, when rates fall, WACC falls and
valuations rise -- the mechanism behind the "TINA" (there is no
alternative) argument for equity allocation during periods of
ultra-low rates. The cost of capital is the transmission channel
through which monetary policy affects corporate investment and
asset pricing.

## Sources

1. Modigliani, F. & Miller, M. (1958). "The Cost of Capital,
   Corporation Finance, and the Theory of Investment." American
   Economic Review, 48(3), 261-297.
   https://www.jstor.org/stable/1809766 [high]

2. Modigliani, F. & Miller, M. (1963). "Corporate Income Taxes and
   the Cost of Capital: A Correction." American Economic Review,
   53(3), 433-443. [high]

3. Sharpe, W.F. (1964). "Capital Asset Prices: A Theory of Market
   Equilibrium under Conditions of Risk." Journal of Finance, 19(3),
   425-442. https://doi.org/10.1111/j.1540-6261.1964.tb02865.x [high]

4. Damodaran, A. (2016). "The Cost of Capital: The Swiss Army Knife
   of Finance." NYU Stern School of Business.
   https://pages.stern.nyu.edu/adamodar/pdfiles/papers/costofcapital.pdf
   [high]

5. Fama, E. & French, K. (2004). "The CAPM: Theory and Evidence."
   Journal of Economic Perspectives, 18, 25-46.
   https://doi.org/10.1257/0895330042162421 [high]

6. Velez-Pareja, I. (2013). "WACC Calculations in Practice: Incorrect
   Results due to Inconsistent Assumptions." Accounting and Finance
   Research, 2(2), 36-47. https://doi.org/10.5430/afr.v2n2p36 [high]

7. Corporate Finance Institute. "WACC Formula, Definition and Uses
   -- Guide to Cost of Capital."
   https://corporatefinanceinstitute.com/resources/valuation/what-is-wacc-formula
   [medium]

8. ACCA Global. "Optimum Capital Structure." F9 Financial Management
   Technical Article.
   https://www.accaglobal.com/gb/en/student/exam-support-resources/fundamentals-exams-study-resources/f9/technical-articles/optimum-capital-structure.html
   [medium]

## See Also

- `library/finance/capital-structure-modigliani-miller.md` -- the
  theory of how the mix of debt and equity affects firm value, which
  WACC measures.
- `library/finance/financial-statement-analysis.md` -- the source of
  the debt levels, tax rates, and capital structure data that feed
  into WACC.
- `library/finance/bond-pricing-and-fixed-income-markets.md` -- bond
  yields to maturity provide the cost of debt input to WACC.
- `library/finance/dividend-policy-and-share-buybacks.md` -- the
  decision of whether to reinvest at the hurdle rate or return cash to
  shareholders.
- `library/finance/yield-curve.md` -- the risk-free rate input to
  CAPM comes from the government bond yield curve.