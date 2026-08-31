---
name: dividend-discount-models
id: 20260831T133137Z
tier: library-topic
domain: valuation-screening
author: Library Runner
tags: [dividend-discount-model, gordon-growth-model, h-model, multi-stage-ddm, dividend-yield, intrinsic-valuation, cost-of-equity]
links: [library/valuation-screening/discounted-cash-flow-dcf-methodology.md, library/valuation-screening/cost-of-capital-capm-wacc-erp.md]
---

# Dividend Discount Models -- Why the Oldest Valuation Method Still Applies Where Others Fail

Dividend discount models (DDM) value a stock as the present value of all
expected future dividends paid to shareholders. Originating with John
Burr Williams in 1938 and formalized as the Gordon Growth Model by
Myron Gordon and Eli Shapiro in 1956, the DDM is the oldest and most
intuitive branch of intrinsic valuation: a stock is worth what it
returns to its owners in cash. The model is narrow in its applicability
-- it works only for mature, stable dividend-paying companies -- but
within that domain it provides a clean, transparent, and theoretically
grounded estimate of intrinsic value that free cash flow models often
obscure behind layers of assumptions about reinvestment and capital
expenditure.

## Background

The intellectual foundation of the dividend discount model traces to
John Burr Williams, a Harvard doctoral student who wrote his 1938
dissertation, "The Theory of Investment Value," during the Great
Depression. Williams confronted a practical problem: how to determine
the intrinsic value of a stock when market prices had collapsed and
speculative methods had failed. His answer was to treat a common stock
as a perpetuity -- a stream of cash flows extending indefinitely into
the future -- and to value it by discounting those cash flows to their
present worth. For Williams, the relevant cash flow was the dividend.
He wrote that the value of any stock, bond, or business is determined
by the cash inflows and outflows discounted at an appropriate rate that
can be expected during the remaining life of the asset. Warren Buffett
would later cite this exact formulation in Berkshire Hathaway's 1992
annual report as the foundational equation of value.

Williams was not the first to use present value calculations -- the
concept of discounting future cash flows dates back centuries in bond
and annuity pricing -- but he was the first to apply it rigorously to
equities and to argue that dividends, not earnings, are the relevant
cash flow for shareholders. This distinction matters: earnings can be
manipulated through accounting choices, retained indefinitely, or
reinvested at poor returns, but dividends are actual cash leaving the
company and arriving in shareholder accounts. Williams argued that
retained earnings not paid out as dividends should eventually produce
dividends; if they do not, they are money lost.

The mathematical formalization came in 1956, when Myron J. Gordon and
Eli Shapiro published "Capital Equipment Analysis: The Required Rate of
Profit" in Management Science, introducing what became known as the
Gordon Growth Model (GGM). Gordon, working across MIT, the University
of Rochester, and the University of Toronto, borrowed heavily from
Williams' theoretical framework but provided the closed-form solution
that made the model practically usable: P0 = D1 / (r - g), where D1 is
next year's dividend, r is the required return, and g is the constant
dividend growth rate. Gordon referenced the model again in his 1959
paper "Dividends, Earnings, and Stock Prices," which explored the
empirical relationship between dividends, growth, and equity prices.

The Gordon Growth Model introduced a critical simplification: it
assumed dividends grow at a single constant rate forever. This made
the infinite sum of discounted dividends collapse into a single
elegant formula, but it also embedded a strong assumption -- that a
company's dividend policy, growth trajectory, and risk profile remain
unchanged in perpetuity. For mature, stable companies like regulated
utilities or consumer staples firms, this assumption is approximately
reasonable. For companies in transition, growth phases, or declining
industries, it is not.

The recognition that companies move through lifecycle phases -- initial
high-growth expansion, transitional maturation, and steady-state
mature growth -- led to the development of multistage models. Nicholas
Molodovsky, former editor of the Financial Analysts Journal, was among
the first to propose substituting earnings-based growth patterns for
the constant-growth assumption. The two-stage DDM split valuation into
an explicit high-growth period and a Gordon Growth terminal value.
Fuller and Hsia introduced the H-Model in 1984 in their paper "A
Simplified Common Stock Valuation Model," which smoothed the transition
from high growth to stable growth by assuming a linear decline in the
growth rate. Three-stage models followed, combining explicit
high-growth projections with a linear transition phase and a Gordon
Growth terminal value.

The CFA Institute's curriculum, the primary professional training
program for equity analysts, presents the DDM as a core valuation
method in its Level II Equity Valuation module, covering the Gordon
Growth Model, multistage models, the H-Model, and spreadsheet-based
dividend forecasting. The DDM remains a standard part of the equity
valuation toolkit, taught alongside free cash flow models and residual
income models. Its continued relevance in professional education signals
that despite its narrow applicability, the model captures a fundamental
truth about equity valuation that broader cash flow models can
sometimes obscure: at the end of the analysis, shareholders receive
cash, and the value of their ownership claim is the present value of
that cash.

The historical trajectory of the DDM also reflects a broader debate in
finance about what constitutes the correct cash flow for equity
valuation. Williams argued for dividends. Modigliani and Miller argued
for earnings (under their dividend irrelevance proposition). Modern
practitioners increasingly argue for free cash flow to equity, which
captures cash available to shareholders regardless of whether it is
distributed as dividends, used for buybacks, or reinvested. The DDM
represents the most conservative and most transparent branch of this
debate: it values only what shareholders actually receive, and it
forces the analyst to confront the relationship between dividend
policy, growth, and required return directly.

## Core Concepts

### The Gordon Growth Model (Constant-Growth DDM)

The Gordon Growth Model is the simplest and most widely used form of
the DDM. It values a stock as the present value of a perpetually
growing stream of dividends:

  P0 = D1 / (r - g)

where P0 is the intrinsic value per share today, D1 is the expected
dividend per share one year from now, r is the required rate of return
(cost of equity), and g is the constant annual dividend growth rate.
The model requires that r > g strictly. If the growth rate equals or
exceeds the required return, the denominator becomes zero or negative,
and the formula produces a meaningless or infinite value. A company
cannot permanently grow faster than the economy, so the perpetual
growth rate should not exceed the long-term GDP growth rate plus
inflation.

A worked example illustrates the model. A company paid a dividend of
$2.00 per share last year and is expected to grow its dividend at 4%
per year in perpetuity. The required return is 9%. D1 = $2.00 * 1.04 =
$2.08. P0 = $2.08 / (0.09 - 0.04) = $2.08 / 0.05 = $41.60. If the
current market price is below $41.60, the model implies the stock is
undervalued. If it trades above, the implied return falls short of the
required rate.

The Gordon Growth Model has three key properties worth understanding.
First, when g = 0, the model reduces to a simple perpetuity: P0 = D /
r, capitalizing the dividend at the required return. Second, the model
can be rearranged to estimate the cost of equity: r = D1 / P0 + g,
which states that a stock's total return equals its dividend yield
plus its growth rate. This identity is foundational: total return
equals income return plus capital gains return. Third, the model is
extremely sensitive to the spread between r and g. If r = 9% and g
increases from 4% to 5%, the denominator shrinks from 0.05 to 0.04,
and the valuation increases by 25% -- from $41.60 to $52.00. A
half-percentage-point change in the growth rate moves intrinsic value
by 10-20% or more, especially when the spread is narrow.

### The Two-Stage DDM

The two-stage DDM addresses the Gordon Growth Model's key limitation --
constant growth forever -- by splitting valuation into two phases. In
Stage 1, dividends grow at a high (supernormal) rate for a finite
number of years, and each dividend is discounted individually. In
Stage 2, growth steps down to a sustainable mature rate, and the
Gordon Growth Model is applied to calculate a terminal value, which is
then discounted back to the present.

  V0 = sum(Dt / (1+r)^t for t=1 to n) + Pn / (1+r)^n

where Pn = Dn(1+gL) / (r - gL) is the terminal value at the end of
Stage 1, Dt are the individual dividends during Stage 1, gS is the
Stage 1 supernormal growth rate, gL is the Stage 2 stable growth rate,
and n is the length of Stage 1.

The two-stage model is more realistic for companies transitioning from
rapid growth to maturity. A mid-sized financial services company
experiencing 10% dividend growth for five years before stabilizing at
3% would be valued by discounting the five high-growth dividends
individually, then applying the Gordon Growth Model at year 5 to
capture the terminal value of the stable-growth phase. The limitation
is the abrupt transition: growth drops instantly from the supernormal
rate to the stable rate, which few companies actually experience.

### The H-Model (Linear Growth Transition)

The H-Model, introduced by Fuller and Hsia in 1984, solves the abrupt
transition problem of the two-stage DDM by assuming the dividend growth
rate declines linearly from an initial high rate to a stable mature
rate over a transition period of 2H years. The model combines the
baseline mature value (as if the stable growth rate applied
immediately) with an additional value from the high-growth transition:

  V0 = [D0 * (1 + gL)] / (r - gL) + [D0 * H * (gS - gL)] / (r - gL)

where D0 is the current dividend, gS is the initial supernormal growth
rate, gL is the long-term stable growth rate, r is the required
return, and H is the half-life of the transition period (if the
transition spans 10 years, 2H = 10, so H = 5).

The first term is the baseline Gordon Growth value at the mature rate.
The second term captures the extra value from the period of
above-mature growth. The H-Model assumes that the dividend payout
ratio and cost of equity remain constant across both phases, and that
the growth rate decline is linear. This makes it suitable for
companies experiencing competitive lifecycle decay -- where profit
margins and market share gradually normalize -- but less suitable for
companies with volatile or unpredictable growth patterns.

### Three-Stage DDM

The three-stage DDM extends the lifecycle modeling further. It
combines explicit high-growth projections in Stage 1 (each dividend
discounted individually), a linear transition phase in Stage 2 (modeled
as an H-Model), and a stable mature growth phase in Stage 3 (Gordon
Growth terminal value). This model captures the full corporate
lifecycle: supernormal growth, gradual maturation, and steady-state.

The three-stage model requires more inputs but provides the most
flexibility in matching the model to the company's actual expected
trajectory. Stage 1 might last 3-5 years for a company with visible
near-term catalysts, Stage 2 might last 5-10 years for the competitive
fading period, and Stage 3 applies the Gordon Growth Model at a rate
consistent with long-term GDP plus inflation. The added complexity
increases the number of assumptions the analyst must justify, which is
both the model's strength (realism) and its weakness (sensitivity to
inputs).

### The Dividend Identity: Yield Plus Growth Equals Return

A fundamental insight embedded in all DDM variants is the relationship
between dividend yield, growth, and required return. Rearranging the
Gordon Growth Model yields:

  r = D1 / P0 + g

This states that a stock's total return equals its dividend yield
(D1/P0) plus its dividend growth rate (g). The dividend yield is the
income return; the growth rate is the capital gains return. Together
they compose total return. This identity is not an assumption of the
model but a mathematical consequence of its structure, and it connects
the DDM directly to the equity risk premium.

Applied to the market as a whole, this formula estimates the equity
risk premium implied by current market prices. If the S&P 500 has a
dividend yield of 3%, an expected growth rate of 5%, and the risk-free
rate is 4%, the implied equity return is 8%, and the implied equity
risk premium is 4%. Aswath Damodaran of NYU Stern publishes widely
cited annual implied ERP estimates using this approach, with values
typically ranging between 4-6% in recent years. When buybacks are
included alongside dividends (as a modified "total payout" yield), the
implied ERP estimate increases, reflecting the reality that modern
firms return cash through both channels.

### Required Return and the Cost of Equity

The discount rate in all DDM variants is the cost of equity -- the
minimum return investors require for bearing the risk of holding the
stock. The standard estimation method is the Capital Asset Pricing
Model (CAPM), which sets the cost of equity as:

  r = rf + beta * (E(Rm) - rf)

where rf is the risk-free rate, beta is the stock's sensitivity to
market movements, and E(Rm) - rf is the equity risk premium. The cost
of equity is the second critical input to the DDM (after the growth
rate), and the model is highly sensitive to it. Because the Gordon
Growth Model divides by (r - g), small changes in r produce large
changes in valuation, particularly when the spread is narrow.

The DDM can also be inverted to estimate the cost of equity: given a
market price, a forecast dividend, and a growth rate, the implied
required return is r = D1/P0 + g. This is the yield-plus-growth approach
and is widely used in regulatory settings (such as UK utility
regulation, where Ofwat uses a DDM-based approach to estimate the
allowed cost of equity for regulated water companies).

### Terminal Value and Sensitivity

In multistage DDMs, the terminal value -- the Gordon Growth value
applied at the end of the explicit forecast period -- typically
accounts for a large fraction of total valuation. When the terminal
value exceeds 75% of total value, the model is signaling high
dependence on the long-term growth and discount rate assumptions. This
is the same sensitivity that affects all DCF models, but the DDM makes
it particularly transparent because the terminal value formula is a
single closed-form expression rather than a complex spreadsheet
calculation.

## Evidence

### The Williams Foundation: Dividends as the Relevant Cash Flow

John Burr Williams' 1938 "The Theory of Investment Value" established
the theoretical case for dividend-based valuation. Williams argued
that the value of a common stock equals the present value of all
future dividends the investor will receive. For companies without
current dividends, Williams theorized that retained earnings should
ultimately become dividends: if earnings not paid out are successfully
reinvested, they produce dividends later; if not, they are money lost.
This principle -- that value derives from cash returned to owners, not
from accounting earnings -- remains the theoretical bedrock of all
DDM variants. The CFA Institute's curriculum traces the DDM directly to
Williams, noting that beginning with his 1938 work, analysts developed
the insight that common stockholders have an equity ownership claim on
future cash flows into a group of valuation models.

### Gordon and Shapiro (1956): The Constant-Growth Formalization

Gordon and Shapiro's 1956 paper provided the mathematical form that
made Williams' theory computationally tractable. By assuming dividends
grow at a constant rate g and are discounted at rate r, the infinite
sum of discounted dividends collapses to P0 = D1 / (r - g). The
model's elegance is matched by its restrictiveness: it requires r >
g, constant growth forever, and stable payout and risk characteristics.
Gordon's subsequent 1959 paper "Dividends, Earnings, and Stock Prices"
provided empirical support for the relationship between dividends,
growth, and equity prices. The Gordon Growth Model became the standard
textbook formula for equity valuation and remains the most widely taught
single-equation valuation model in finance curricula worldwide.

### Fuller and Hsia (1984): The H-Model for Transitional Growth

Fuller and Hsia's 1984 paper "A Simplified Common Stock Valuation
Model" addressed the unrealistic abrupt transition in the two-stage
DDM. Their H-Model assumes the dividend growth rate declines linearly
from a supernormal rate to a stable rate over a transition period of
2H years. Empirical application of the H-Model shows it produces values
that fall between the pure two-stage DDM (with its step-down) and a
pure Gordon Growth Model (with no high-growth phase at all). The
model's advantage is realism: most companies do not experience instant
growth rate drops, and the linear decline approximates the gradual
competitive fading that characterizes maturing industries. The CFA
Institute curriculum presents the H-Model as one of the primary
multistage DDM variants, alongside the two-stage and three-stage
models, and teaches analysts to justify the selection of each model
based on the company's growth trajectory.

### Sensitivity Analysis: The r-g Spread

The DDM's extreme sensitivity to the gap between the discount rate and
the growth rate is well documented. When r = 9% and g = 4%, the
denominator is 0.05 and the valuation multiple is 20 times next year's
dividend. If g increases to 5%, the denominator shrinks to 0.04 and the
multiple rises to 25 -- a 25% increase in value from a single
percentage point change in the growth assumption. This sensitivity is
not a flaw unique to the DDM; it is inherent in any perpetuity-based
valuation. But the DDM makes the sensitivity visible in a single
formula, whereas free cash flow models bury it in multi-year
spreadsheet projections. Practitioners routinely run sensitivity
analyses showing how valuation changes across a range of r and g
assumptions, often presenting the results as a two-way data table. The
Corporate Finance Institute and other practitioner resources
recommend flagging when terminal value exceeds 75% of total value, as
this signals that the model's output is dominated by the terminal
assumptions rather than the explicit forecast.

### The Buyback Challenge: DDM vs. Modern Payout

Since the 1980s, share repurchases have become an increasingly
important method of returning cash to shareholders, particularly in the
United States. Grullon and Michaely (2002) documented in "Dividends,
Share Repurchases, and the Substitution Hypothesis" that repurchases
have become the preferred form of payout among firms initiating cash
distributions, and that large-established firms have been gradually
substituting repurchases for dividends. This trend poses a structural
challenge to the DDM: if a company returns cash through buybacks rather
than dividends, the standard DDM (which counts only dividends) will
understate intrinsic value.

The Investopedia analysis of DDM drawbacks notes that the model ignores
stock buybacks, which can make a vast difference in stock value being
returned to shareholders, and that this makes the DDM overly
conservative. McKinsey research cited in practitioner analyses found
that whether a company distributes excess cash as dividends or share
repurchases, the total value to shareholders remains the same -- the
only difference is the mix. This equivalence suggests that a modified
DDM incorporating both dividend yield and buyback yield (a "total
payout model") would more accurately capture the cash returned to
shareholders. The UK regulator Ofwat's DDM analysis for utility cost of
equity estimation explicitly incorporates share buyback yield alongside
dividend yield, finding that rising buyback yields have increased the
total market return implied by DDM models. For investors applying the
DDM to individual stocks, the implication is that the model should be
augmented with buyback yield or used alongside a free cash flow model
that captures total shareholder distributions.

### Damodaran's Practitioner Framework: When to Use the DDM

Aswath Damodaran of NYU Stern, a leading authority on valuation, has
published detailed guidance on when the DDM is appropriate versus free
cash flow models. His framework specifies: use the DDM when the firm
pays dividends (and repurchases stock) that are close to free cash flow
to equity over an extended period, or when FCFE is difficult to estimate
(as with banks and financial service companies). Use the FCFE model
when dividends differ significantly from FCFE (as a rule of thumb, if
dividends are less than 75% of FCFE or greater than FCFE), or when
dividends are not available (private companies, IPOs). This framework
provides a clear decision rule: the DDM is the right tool when
dividends are a reliable proxy for the cash available to equity
holders, which is true for mature, stable payout companies but not for
growth firms, companies with lumpy capital expenditure, or firms that
prefer buybacks over dividends.

## Implications

### For Value Investors: The DDM as a Conservative Screen

For value investors, the DDM serves as a conservative, transparent
screening tool. Because it counts only dividends -- actual cash
distributed to shareholders -- it cannot be inflated by optimistic
assumptions about reinvestment rates, capital expenditure efficiency, or
working capital management. A company that passes the DDM test is one
where the present value of expected dividends exceeds the current
price, meaning the investor is paying less than the cash they will
receive. This aligns with the Buffett and Munger emphasis on owner
earnings and the principle that intrinsic value is the discounted value
of cash that can be taken out of the business over its lifetime.

The DDM is particularly useful for valuing regulated utilities,
consumer staples, and mature financial institutions -- companies with
stable, predictable dividend policies and growth rates close to the
long-term economic average. For these firms, the Gordon Growth Model
provides a quick, defensible intrinsic value estimate. The sensitivity
to the r-g spread, while a limitation, is also a feature: it forces the
investor to confront whether their growth assumptions are reasonable.
If a small change in g swings the valuation by 25%, the investor must
ask whether they have high confidence in the growth rate, or whether
they are building margin of safety through a conservative discount
rate instead.

The DDM also connects to the margin of safety concept. A conservative
DDM -- using a discount rate above the CAPM estimate and a growth rate
below consensus -- produces a lower intrinsic value, widening the
required margin of safety before the investor commits capital. This
disciplined approach is exactly what the Buffett-Munger school
advocates: demand a price so low that even pessimistic assumptions
produce a positive expected return.

### For Equity Analysts: Model Selection and Cross-Checking

For professional equity analysts, the DDM is one tool in a valuation
toolkit that also includes free cash flow models (FCFF and FCFE),
residual income models, and relative valuation (multiples). The CFA
Institute curriculum teaches analysts to justify model selection based
on the company's characteristics: the DDM for stable dividend payers,
FCFE for companies where dividends differ from free cash flow, FCFF for
companies with changing capital structures, and residual income for
firms with negative free cash flow but meaningful book value.

The most robust practice is to run multiple models and compare. For a
mature dividend payer, DDM on dividends and FCFE on free cash flow
should produce values within 10-20% of each other. A larger gap is a
signal: if the FCFE model values the company higher than the DDM, the
company may be reinvesting at returns below the cost of capital or
hoarding cash. If the DDM values the company higher than FCFE, the
dividend may be funded from sources other than free cash flow -- debt,
asset sales, or a payout ratio above what the underlying cash
generation supports. This cross-checking discipline is more valuable
than relying on any single model, because each model's assumptions
become visible when they diverge.

The DDM's transparency is a strength in analyst communication. A
Gordon Growth valuation can be explained in a single sentence: "The
stock is worth $41.60 because next year's dividend is $2.08, the
required return is 9%, and the growth rate is 4%." Stakeholders can
immediately identify which assumption they disagree with and test
alternative values. A multi-stage free cash flow model, by contrast,
may require a 200-row spreadsheet to communicate its assumptions,
making it harder for clients and investment committees to challenge the
analyst's reasoning.

### For Corporate Finance: The Implied Cost of Equity

In corporate finance and regulatory settings, the DDM is used in
reverse to estimate the cost of equity. Given a market price, a
forecast dividend, and a growth rate, the implied required return is r
= D1/P0 + g. This yield-plus-growth approach is used by utility
regulators to set allowed returns on regulated assets. The UK water
regulator Ofwat uses a DDM-based approach to estimate the total market
return (and hence the allowed cost of equity) for regulated water
companies, incorporating both dividend yield and buyback yield from
the FTSE All-Share index.

For corporate managers, the DDM provides a framework for understanding
how dividend policy affects shareholder value. The Gordon Growth Model
shows that value depends on the level of dividends (D1), the growth
rate (g), and the required return (r). Increasing the dividend payout
ratio raises D1 but lowers g (because less is reinvested), and the net
effect on value depends on whether the company can reinvest retained
earnings at returns above the cost of equity. If return on equity
exceeds the cost of equity, retaining earnings (lower payout, higher
growth) increases value. If return on equity is below the cost of
equity, paying out more (higher payout, lower growth) increases value.
This is the fundamental trade-off in dividend policy that the DDM makes
explicit.

### For Portfolio Construction: Dividend Yield as a Return Component

The DDM's core identity -- total return equals dividend yield plus
growth -- has direct implications for portfolio construction. Investors
who require a minimum expected return can screen for stocks where the
sum of dividend yield and expected growth exceeds their target. This
is the theoretical basis for dividend growth investing strategies,
which seek companies with long histories of dividend increases and
project continued growth. The approach is most valid for companies
where the Gordon Growth assumptions hold: stable payout, moderate
growth, and low risk of dividend cuts.

The risk in dividend-based portfolio construction is that the DDM's
assumptions break down precisely when they matter most -- during
economic stress, when companies cut dividends, or during structural
shifts, when companies substitute buybacks for dividends. A portfolio
selected purely on DDM-based expected return will over-weight mature
dividend payers and under-weight or exclude companies that return cash
through buybacks or that reinvest for growth. The DDM is a necessary
but not sufficient input: it captures one component of expected return
(the dividend channel) but must be supplemented with free cash flow
analysis to capture the full picture of shareholder value creation.

## Sources

1. Williams, J.B. (1938). "The Theory of Investment Value." Harvard
   University Press. The original articulation of dividend-based
   valuation.
   https://en.wikipedia.org/wiki/John_Burr_Williams [high]

2. Gordon, M.J. & Shapiro, E. (1956). "Capital Equipment Analysis:
   The Required Rate of Profit." Management Science, 3(1), 102-110.
   Formalization of the constant-growth DDM (Gordon Growth Model).
   https://en.wikipedia.org/wiki/Dividend_discount_model [high]

3. Fuller, R.J. & Hsia, C.C. (1984). "A Simplified Common Stock
   Valuation Model." Financial Analysts Journal, 40(5), 49-56.
   Introduction of the H-Model for linear growth transitions.
   https://stablebread.com/h-model/ [high]

4. CFA Institute. "Discounted Dividend Valuation." CFA Program Level II
   Curriculum, 2026. Professional curriculum covering Gordon Growth,
   two-stage, H-Model, and three-stage DDM variants.
   https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/discounted-dividend-valuation [high]

5. Damodaran, A. "Valuation: Choosing the Right Model." NYU Stern
   School of Business. Practitioner framework for when to use DDM vs.
   FCFE vs. FCFF models.
   https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/basics.html [high]

6. Grullon, G. & Michaely, R. (2002). "Dividends, Share Repurchases,
   and the Substitution Hypothesis." Journal of Finance, 57(4),
   1649-1684. Documents the shift from dividends to buybacks.
   https://papers.ssrn.com/sol3/papers.cfm?abstract_id=222730 [high]

7. Investopedia. "The Downsides of Using the Dividend Discount Model
   for Valuation." Overview of DDM limitations including buyback
   exclusion and growth rate sensitivity.
   https://www.investopedia.com/ask/answers/042315/what-are-drawbacks-using-dividend-discount-model-ddm-value-stock.asp [medium]

8. Corporate Finance Institute. "What is the H-Model?" Explanation of
   H-Model formula, assumptions, and worked examples.
   https://corporatefinanceinstitute.com/resources/valuation/h-model/ [medium]

9. Ofwat / PwC (2019). "Updated Dividend Discount Model Analysis for
   PR19." Regulatory application of DDM incorporating buyback yield
   for cost of equity estimation.
   https://www.readkong.com/page/updated-dividend-discount-model-analysis-for-pr19-5203890 [medium]

10. Pomegra Learn Library. "Limitations of Dividend Models." Overview
    of DDM assumptions and their breakdown conditions.
    https://pomegra.io/learn/library/track-b-stock-market-core/stock-valuation/chapter-04-dividend-discount-model/limitations-of-dividend-models [medium]

## See Also

- `library/valuation-screening/discounted-cash-flow-dcf-methodology.md` --
  the broader DCF framework of which DDM is the dividend-based branch;
  DDM and FCF models share the same discounting logic but differ in
  their definition of cash flow.
- `library/valuation-screening/cost-of-capital-capm-wacc-erp.md` -- the
  cost of equity estimation methods (CAPM, build-up) that supply the
  discount rate r in all DDM variants.
- `library/valuation-screening/terminal-value-dcf-methods-and-biases.md` --
  the terminal value methods and biases that apply directly to the
  Gordon Growth terminal value in multistage DDMs.
- `library/valuation-screening/earnings-power-value-and-asset-based-valuation.md` --
  alternative intrinsic valuation approaches that complement the DDM
  for companies where dividends are not the relevant cash flow.
- `library/valuation-screening/valuation-multiples-pe-ev-ebitda-pb-analysis.md` --
  relative valuation methods used alongside the DDM for triangulation.