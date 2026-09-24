---
name: dividend-discount-models
id: 20260831T133137Z
tier: library-topic
domain: valuation-screening
author: Librarian
tags: [dividend-discount-model, gordon-growth-model, h-model, multi-stage-ddm, dividend-yield, intrinsic-valuation, cost-of-equity]
links: [library/valuation-screening/discounted-cash-flow-dcf-methodology.md, library/valuation-screening/cost-of-capital-capm-wacc-erp.md]
reviewed: 2026-09-24
---

# Dividend Discount Models -- Observable Payout Can Clarify Equity Value

Dividend discount models (DDMs) value common equity as the present value of
expected future dividends. The general model can accommodate any expected
dividend path, but its practical usefulness is greatest when payout policy is
observable and connected to profitability; free-cash-flow or residual-income
models are often more informative when dividends are absent or materially
different from cash available to equity holders. The model's value is therefore
not universal applicability but a transparent connection among distributions,
growth, risk, and price [4][5].

## Background

John Burr Williams set out the dividend-present-value principle in *The Theory
of Investment Value* in 1938. He defined the investment value of common stock
in terms of the present worth of its future net dividends and treated retained
earnings as valuable only insofar as they increased later dividend-paying power
[1]. Berkshire Hathaway's 1992 shareholder letter quoted Williams' broader
formulation: the value of a stock, bond, or business is determined by cash
inflows and outflows expected over the asset's remaining life, discounted at an
appropriate rate [7]. That quotation supports discounted-cash-flow logic; the
more specific dividend formulation comes from Williams' book [1].

A shareholder can receive cash during a finite holding period through dividends
and the sale price. The sale price is not an independent source of value in the
infinite-horizon model: repeated substitution of each future resale price leaves
the present value of the dividends ultimately paid by the firm, provided the
terminal-price term vanishes rather than containing a speculative bubble. The
CFA curriculum presents both forms: value for a finite horizon equals discounted
dividends plus discounted terminal price, while the general infinite-horizon DDM
is the discounted stream of expected dividends [4]. This derivation also explains
why a company paying no dividend today is not logically unvalued by the general
DDM; it may have value if investors reasonably expect distributions later. The
practical difficulty is forecasting when and how those distributions will occur
[4][5].

Myron J. Gordon and Eli Shapiro's 1956 *Management Science* article developed
the required-return relation associated with a perpetually growing stream. The
closed form now called the Gordon growth model is P0 = D1 / (r - g), where D1
is the next-period dividend, r is the required equity return, and g is the
constant perpetual growth rate [2][4]. The formula made an infinite dividend
series operational, but only under restrictive conditions: a stable growth rate,
a required return exceeding that rate, and internally consistent payout, growth,
and risk assumptions. Damodaran accordingly identifies stable firms with stable
leverage and dividends that approximate free cash flow to equity as the model's
best practical candidates [5].

Constant growth is a steady-state abstraction, not a claim that a business can
preserve an exceptional growth rate indefinitely. A perpetual growth assumption
must be compatible with the currency, inflation, and the long-run growth of the
economy in which the firm operates. A company cannot indefinitely grow faster
than its economic base without eventually becoming implausibly large [5]. Mature
regulated businesses can sometimes approximate the stable case, but even there
payout rules, capital requirements, and risk can change. The analyst must test the
assumption rather than infer stability from an industry label [4][5].

Multistage models arose because firms can pass from an unusual growth phase to a
mature one. A two-stage DDM forecasts dividends explicitly during an initial
period and then uses a stable-growth terminal value. Its weakness is the abrupt
step between regimes. Fuller and Hsia's 1984 H-model assumes that the growth rate
declines or increases linearly from an initial rate to a normal long-term rate
over 2H periods. Their stated objective was a model more practical than the
general DDM and more realistic than constant growth, while retaining simple
arithmetic and allowing direct solution for the discount rate [3]. A three-stage
model adds an explicit high-growth stage before a transition and stable stage
[4][5].

Modern model selection separates theoretical equivalence from forecasting
convenience. Dividends, free cash flow, and residual income can represent the same
equity claim when forecasts, financing, accounting relations, and terminal values
are mutually consistent. In finite-horizon applications they need not produce the
same estimate because analysts forecast different attributes with different
precision and place different amounts of value in the terminal period [10][13].
CFA Institute therefore recommends DDM for dividend-paying firms with a
discernible policy tied to profitability and a minority-investor perspective; it
identifies FCFE as more suitable when dividends materially differ from FCFE or
the investor has a control perspective, and residual income as useful when free
cash flow is negative or difficult to forecast [4].

Repurchases add a modern payout complication without overturning the general
DDM. Grullon and Michaely document that US firms increasingly used repurchases
and that repurchases partly substituted for dividend increases [6]. A per-share
DDM can already reflect repurchases through fewer shares and higher future
per-share dividends, so mechanically adding a current repurchase yield to both
payout and growth can double count value. Conversely, a dividend forecast that
ignores a persistent change in payout policy can be biased. The correct response
is an internally consistent forecast of dividends per share, issuance,
repurchases, and growth, not an automatic adjustment in one direction [8][11].

The DDM remains part of CFA Institute's professional curriculum because it makes
cash-flow definition, timing, growth, and discount-rate assumptions explicit [4].
Its historical importance does not establish empirical superiority. Its present
use is narrower and more disciplined: select it when distributions are forecastable,
model the transition to a sustainable state, and compare its output with another
equity-valuation representation when payout policy may obscure cash available to
owners [4][5][10].

## Core Concepts

### General DDM and the Finite-Horizon Bridge

The general DDM is:

  V0 = sum(E[Dt] / (1+r)^t for t=1 to infinity)

where V0 is value today, E[Dt] is the expected dividend per share in period
t, and r is the return required for the risk of those dividends. For a finite
holding period n, the corresponding expression is the present value of dividends
through n plus the present value of the expected sale price Pn. The infinite form
follows only after recursively replacing future sale prices and imposing the
condition that the discounted terminal-price term converges to zero [4]. This
logic prevents two common errors: treating the sale price as value created apart
from future corporate distributions, and concluding that a current nonpayer must
have zero value even when credible future dividends are expected.

The discount rate and the cash flow must refer to the same claim. Dividends are
cash flows to common equity, so they are discounted at the cost of common equity,
not at the weighted average cost of capital. Forecasts should be per share and
should reconcile expected issuance and repurchases because aggregate dividends
can rise while dividends per share follow a different path [4][5]. When the risk
of the dividend stream changes across stages, a single r can be an approximation;
a detailed model may use stage-consistent required returns rather than preserve a
high-growth beta in maturity [5].

### The Gordon Growth Model

For dividends expected to grow at a constant rate forever, the infinite series
reduces to:

  P0 = D1 / (r - g)

D1 is the expected next-period dividend, r is the required equity return, and g
is the perpetual dividend growth rate. The convergence condition is r > g. If
g equals or exceeds r, the closed form is undefined or economically unusable;
that result is a failed assumption, not evidence of infinite or negative business
value [2][4]. The stable growth rate must also be compatible with the long-run
nominal growth of the relevant economy and with the currency's expected inflation
[5]. "Nominal GDP plus inflation" would double count inflation; nominal growth
already combines real growth and inflation.

A worked example shows both the calculation and its limits. Suppose the most
recent annual dividend was $2.00, the next dividend is expected to be $2.08, the
required return is 9%, and the perpetual growth rate is 4%. Then P0 = $2.08 /
(0.09 - 0.04) = $41.60. The result is an estimate conditional on those inputs,
not an automatic buy signal. Price below $41.60 implies an expected return above
9% only if the dividend path and other model assumptions prove accurate [4][5].

The formula has useful limiting and inverse forms. When growth is zero, value is
a level perpetuity, D/r. Rearranging gives r = D1/P0 + g: the required or implied
return equals the forward dividend yield plus constant growth. The term D1/P0 is
a forward yield; substituting a trailing dividend without adjustment mixes time
periods. Under the stable-growth assumptions, price grows at g, so g is also the
modeled capital-gain rate. The identity does not assert that realized returns must
equal the estimate or that a changing valuation multiple has no effect over a
finite horizon [4].

Sensitivity comes from the denominator. Holding D1 at $2.08 and r at 9%, moving
g from 4% to 5% changes value from $41.60 to $52.00, a 25% increase. That is a
mechanical result verified from the formula. It also shows why analysts should
report a range across plausible r and g rather than a point estimate. As g
approaches r, small input changes create increasingly large value changes; a
narrow r-g spread is a warning about model leverage, not evidence that the highest
value is the most accurate [4][5].

### Two-Stage and Three-Stage Models

A two-stage DDM separates an explicit period from stable growth:

  V0 = sum(Dt / (1+r)^t for t=1 to n) + Pn / (1+r)^n

  Pn = D(n+1) / (r - gL)

The analyst forecasts each dividend through year n, estimates D(n+1) using the
stable-state payout and growth assumptions, computes the terminal value at n,
and discounts all cash flows to the present. This is appropriate when an initial
regime can be forecast with some confidence and a later stable state is plausible.
Its visible weakness is the immediate jump from the initial regime to gL [4][5].
The terminal dividend must be a stable-state dividend; mechanically extending a
high-growth payout ratio into maturity can make growth, reinvestment, and payout
internally inconsistent.

A three-stage DDM adds a transition phase between explicit high growth and stable
growth. It can accommodate declining growth, changing payout, and changing risk,
but the extra realism requires more estimates. Damodaran emphasizes that stable
growth should bring stable-firm characteristics, including a payout ratio and
risk profile consistent with the mature growth rate [5]. The model should not
retain a high-growth reinvestment need while simultaneously assuming a mature
payout, or use a high-growth beta forever simply because it was observed at the
valuation date.

### The H-Model

The H-model is a compact approximation for a linear transition in growth over
2H periods. Its common form is:

  V0 = [D0 * (1 + gL)] / (r - gL)
       + [D0 * H * (gS - gL)] / (r - gL)

D0 is the current dividend, gS the initial growth rate, gL the stable rate, and
H half the transition length. The first term is the value of immediate stable
growth; the second is the present value attributed to growth above or below the
stable rate during the linear transition. Fuller and Hsia describe the model as
more practical than a fully specified general DDM and more realistic than a
constant-growth model, while producing results similar to a more elaborate
three-phase model under compatible assumptions [3].

The simplification is also its limitation. The model assumes a linear growth
transition and, in its standard form, constant payout and cost of equity. Those
conditions can be poor descriptions of a firm whose payout ratio rises as growth
slows, whose risk changes materially, or whose transition is discontinuous. The
H-model is therefore a structured approximation, not a general cure for
uncertain growth [3][5]. Banco de Espana's use of a Fuller-Hsia specification for
a broad market index illustrates a second application: solving for an implied
market equity premium before mapping that estimate to financial institutions
[12].

### Growth, Retention, and Payout Consistency

A stable dividend growth forecast must be connected to the economics that produce
it. Under a simplified clean relationship, sustainable earnings growth is the
retention ratio b multiplied by return on equity: g = b * ROE. The corresponding
payout ratio is 1 - b. This is not an empirical law for every period; it assumes
that retained earnings earn the stated ROE and that financing and accounting
relations remain consistent. It is nevertheless a useful audit: a model cannot
simultaneously assume a high payout, high perpetual growth, and ordinary ROE
without explaining another source of financing or improvement [5].

The reinvestment question determines whether increasing payout creates or destroys
value. If retained equity can earn a return above the cost of equity, retaining a
dollar can support value even though current dividends fall. If reinvestment earns
less than the cost of equity, distribution is preferable, all else equal. The
DDM captures this only when lower current payout is translated into plausible
higher future dividends. Raising D1 without reducing reinvestment or growth is
not a free value increase; it changes two linked assumptions as though they were
independent [1][5].

### Repurchases, Issuance, and Total Payout

A repurchase transfers cash to selling shareholders and reduces shares
outstanding. All else equal, continuing shareholders own a larger proportion of
the firm, but whether a repurchase creates value for them depends on the price
paid and on the alternative use of cash. Grullon and Michaely's 1972-2000 US
sample documents substitution toward repurchases, including increased use by
firms initiating payouts and funding that otherwise might have increased
dividends [6][14]. That evidence establishes a change in payout practice, not that
ordinary dividends ceased to matter.

There are two internally consistent routes. A dividend-per-share model can project
future dividends after explicitly modeling net share-count changes; repurchases
then affect per-share growth. A total-payout model can value aggregate dividends
plus net repurchases and divide equity value by the appropriate share count.
Mixing them can double count repurchases. CFA Institute's digest of research on
expected-return estimation argues that buybacks are reflected in per-share
dividend growth and cautions that net repurchases are hard to measure because
shares are also reissued [11]. By contrast, PwC's 2019 market DDM for Ofwat used
a buyback-yield adjustment and tested sensitivities around it [8]. These are not
contradictory formulas so much as different implementations; each must reconcile
its yield, growth, and share-count assumptions.

### Required Return and Implied Return

The DDM requires a cost of equity. CAPM is one possible estimator:

  r = rf + beta * (E[Rm] - rf)

where rf is the risk-free rate, beta measures exposure to market risk, and the
parenthesized term is the expected market risk premium. CAPM inputs are estimates,
not observed certainties, and a model should preserve consistency between nominal
or real cash flows and discount rates [4][5]. A mature-stage required return may
differ from an initial-stage rate if leverage or operating risk changes.

The Gordon model can also be inverted to infer the return embedded in a price:
r = D1/P0 + g. Regulatory and market applications use variants of this
forward-looking yield-plus-growth logic. PwC's Ofwat work estimated total-market
return from market dividend data, growth assumptions, and sensitivity to buyback
treatment; Banco de Espana combined an H-model market premium estimate with a
factor framework for individual financial institutions [8][12]. Such outputs are
conditional estimates and can be highly sensitive to the growth, transition, and
payout choices embedded in the model.

### Terminal Value and Model Diagnostics

In a multistage DDM, terminal value often represents a substantial part of total
value because the firm is assumed to continue beyond the explicit forecast. The
proper diagnostic is not a universal percentage cutoff. It is to disclose the
terminal-value share, stress r and g, and verify that terminal payout, growth,
risk, and reinvestment describe the same steady state. Finite-horizon research
shows why this matters: truncation and terminal-value assumptions can cause
valuation techniques that are theoretically equivalent to perform differently in
practice [10][13].

A robust implementation therefore reports a sensitivity table, an implied-return
calculation, and a reconciliation with at least one alternative equity model. A
large DDM-FCFE or DDM-residual-income gap is evidence that assumptions differ; it
does not by itself identify which model is correct. Trace the gap to payout,
reinvestment, accounting, risk, share count, or terminal value before drawing an
investment conclusion [4][5][10].

## Evidence

### Foundational Models and Their Scope

Williams' 1938 book is the primary historical evidence for the dividend-present-
value formulation. It states that the investment value of common stock is the
present worth of future net dividends and analyzes rapid-then-slow dividend
growth as well as constant growth. The source establishes the conceptual model;
it is not a modern out-of-sample test of forecasting accuracy [1]. Berkshire's
1992 letter independently confirms Williams' influence on value-investing
practice by quoting his discounted-cash-flow equation, but it broadens the cash
flow language beyond dividends and therefore should not be cited as proof that
Buffett prescribed a literal dividend-only model [7].

Gordon and Shapiro's 1956 article is the primary source for the required-return
framework associated with the constant-growth relation. The later textbook form
P0 = D1/(r-g) is supported by CFA Institute and Damodaran, which also state the
conditions under which it is usable [2][4][5]. This chain of evidence supports
formula identity, chronology, and assumptions. It does not establish that a
single-stage model estimates every firm's value accurately.

Fuller and Hsia's 1984 article presents the H-model and describes its method: the
growth rate moves linearly from an above- or below-normal initial rate to a normal
long-term rate. The article compares this simplified construction with a
three-phase approach and emphasizes that the H-model can solve directly for price
or discount rate with simpler arithmetic [3]. Banco de Espana later used a
Fuller-Hsia specification to estimate a market equity premium in a study of the
cost of equity for European financial institutions, showing that the model also
functions as an implied-return tool rather than only a stock-price calculator
[12]. Neither application eliminates sensitivity to the assumed initial growth,
transition length, stable growth, and risk-free rate.

### Portfolio Ranking Evidence

Sorensen and Williamson tested whether greater DDM structure added information in
security selection. They used consensus earnings-growth forecasts and four
valuation models, ranging from a P/E model to a three-period DDM, to rank 150
stocks from the S&P 400 into five portfolios. Subsequent returns followed the
rankings for each model, all top-ranked portfolios outperformed the market
average, and discrimination improved as model complexity increased. The annual
return of the top-ranked three-period-DDM portfolio exceeded that of the
top-ranked P/E portfolio by 3.5 percentage points; the best-worst return spread
was 35.63 percentage points for the three-period model versus 22.26 for P/E [9].

The study supports the proposition that a systematically implemented multistage
DDM can contribute to ranking securities in the tested sample and period. It does
not establish a universal 3.5-point advantage, because the inputs were consensus
forecasts, the universe was a historical subset of US stocks, and model rankings
were evaluated against subsequent returns rather than an unobservable true
intrinsic value [9]. A reviewer should therefore preserve the method, sample, and
comparison whenever quoting the result.

### Comparisons with Other Valuation Representations

Francis, Olsson, and Oswald compared dividend, free-cash-flow, and abnormal-
earnings estimates using Value Line five-year forecasts. Their sample used
third-quarter Value Line reports from 1989 through 1993, and their tests compared
model estimates with observed prices and cross-sectional price variation. The
abnormal-earnings estimates had smaller absolute deviations from observed prices
and explained more price variation than the dividend or free-cash-flow estimates;
free cash flow also outperformed dividends on median accuracy in the reported CFA
summary [10]. The authors attribute the abnormal-earnings advantage to the
information in book value and to greater precision and predictability in abnormal-
earnings forecasts [10].

Penman and Sougiannis examine a related problem: all going-concern models require
payoffs to infinity, while practical forecasts stop after a finite horizon. They
compare dividend, cash-flow, and accrual-earnings approaches using average ex post
payoffs over alternative horizons, with and without terminal value. Valuation
errors were lower for accrual-earnings techniques than for cash-flow and dividend
discounting in their tests, and the paper identifies accounting conditions under
which some methods require longer forecast horizons [13]. These findings do not
refute theoretical equivalence. They show that finite-horizon truncation, terminal
value, and forecastability matter to observed implementation error [10][13].

Taken together, these studies reject two easy claims: that DDM is empirically
superior merely because dividends are observable, and that one model must always
produce the correct number. Model performance depends on the forecast horizon,
quality of the forecasted attribute, terminal assumptions, and accounting
relations. DDM can add ranking information, while an accrual-based model can be
more accurate in another design [9][10][13]. The evidence supports disciplined
model selection and triangulation rather than a permanent hierarchy.

### Repurchases and the Measurement of Payout

Grullon and Michaely study US corporate distributions over 1972-2000. Their
methods include comparisons of payout behavior and regressions relating dividend
forecast errors to repurchase yields. They report that the share of repurchasing
firms increased from 31% in 1972 to 80% in 2000, repurchase dollars grew faster
than cash-dividend dollars, repurchases became a common way to initiate payout,
and firms appeared to fund repurchases with cash that otherwise might have raised
dividends [6]. These findings establish substitution in payout practice and the
need to model share count and distribution policy explicitly.

They do not prove that a conventional per-share DDM necessarily understates value.
If repurchases reduce share count and the model forecasts future dividends per
remaining share consistently, the effect can enter dividend growth. CFA
Institute's digest of expected-return research makes this point and warns that
adding repurchase yield can be difficult because companies may repurchase shares
and later reissue them. It argues that a total-yield model can double count the
repurchase effect when the per-share growth rate already includes it [11]. The
evidence therefore corrects the simple prescription to "add buyback yield" in all
cases.

PwC's 2019 note for Ofwat shows a legitimate alternative implementation. It
updated a market DDM for the PR19 water-price review and separately analyzed
buyback trends. The report treated dividend yield, growth, and a buyback-yield
adjustment as explicit inputs and presented sensitivity results [8]. This is an
official regulatory application to market-return estimation, not direct evidence
that every individual-company DDM should add gross repurchases. The relevant test
is whether the chosen implementation reconciles net issuance, per-share growth,
and aggregate payout without omission or duplication [8][11].

### Regulatory and Financial-Institution Applications

Banco de Espana's 2021 article estimated cost of equity for a large sample of
listed European financial institutions using two broad approaches. One combined
a broad-market Fuller-Hsia DDM estimate with a single-factor framework for
individual stocks; the other used multifactor time-series models. The authors
explain that the DDM is calibrated to market-average conditions and may miss
institution-specific differences, and they report sensitivity to model
assumptions [12]. The study supports DDM as one input to cost-of-equity estimation
for regulated or balance-sheet businesses while cautioning against interpreting a
market-average result as a precise company-specific hurdle rate.

CFA Institute's suitability guidance supplies the practical boundary around these
applications. A discounted-dividend approach is most suitable when a company pays
dividends under a discernible policy related to profitability and the valuation
adopts a minority-shareholder perspective. FCFE is more appropriate when payout
materially diverges from cash available to equity or the investor has control;
residual income can be useful when dividends are absent or free cash flow is
negative [4]. This guidance is not an empirical return test, but it turns the
research findings into a falsifiable selection rule: before using DDM, compare
observed and forecast payout with underlying distributable capacity.

### What the Evidence Does and Does Not Establish

The combined record supports four bounded conclusions. First, the dividend-
present-value identity is theoretically coherent when the terminal-price condition
and cash-flow timing are respected [1][4]. Second, multistage structures can carry
useful ranking information, but performance is sample- and forecast-dependent
[9]. Third, alternative theoretically equivalent models diverge in finite
applications because forecast precision and terminal assumptions differ
[10][13]. Fourth, repurchases require consistent per-share or aggregate-payout
modeling rather than an automatic add-on [6][8][11].

The evidence does not validate any single value estimate, fixed terminal-value
threshold, universal DDM-FCFE tolerance, or permanent model-performance ranking.
Those claims require separate data and definitions. The most defensible use of
the literature is procedural: state the model's cash-flow definition, document
forecast and terminal assumptions, reconcile share-count changes, report
sensitivity, and compare the result with an alternative representation of the
same equity claim [4][5][10][13].

## Implications

### For Long-Term and Value Investors

DDM is useful when it forces an investor to name the distributions, timing, and
required return that justify the price. It is not automatically conservative.
An optimistic dividend-growth path, an understated cost of equity, or an
inconsistent terminal payout can inflate a DDM just as optimistic free-cash-flow
assumptions can inflate another DCF. The value-investing discipline is to use
conservative but economically linked assumptions, calculate a range, and require
a market price that remains attractive under adverse cases [4][5].

Start with payout capacity rather than dividend history alone. Reconcile net
income to cash available to common equity; examine capital expenditure, working
capital, debt service, regulatory capital, and net share issuance; then ask whether
the board's payout policy has an understandable connection to those resources.
CFA Institute's model-selection rule makes this relationship central to DDM
suitability [4]. A long history of dividends is evidence about past policy, not a
guarantee that the next dividend is affordable.

For a stable payer, construct at least three linked cases. Each case should state
D1, the initial growth path, stable g, the transition period, r, and the resulting
payout and retention ratios. Test g = retention * ROE rather than choosing growth
independently of reinvestment [5]. A downside case should model a dividend cut
when cash generation or regulatory capital requires it; merely raising r while
leaving distributions untouched can miss the mechanism by which owners suffer.
The author's synthesis is that the worst-case test should ask which assumption
breaks first -- payout, growth, or capital -- and then alter the cash flows before
altering the valuation label [4][5].

A current nonpayer is not worth zero under dividend theory if future distributions
are credible, but the long deferral makes DDM heavily dependent on terminal
assumptions [4]. In that situation, FCFE or residual income may expose operating
and reinvestment economics more directly. Use DDM as a cross-check only when the
path from reinvestment to eventual distributions can be specified. A vague claim
that "dividends will come later" is not a forecast.

Repurchases require special care. Model either future dividends per share after
net share-count changes or total net payout at the aggregate level. Do not add
gross repurchase yield to a dividend-growth model whose per-share growth already
reflects buybacks [11]. Also distinguish cash spent from value transferred: a
repurchase executed above intrinsic value can disadvantage continuing owners even
though aggregate payout rises [14]. The DDM addresses distribution timing; it does not
by itself judge whether the repurchase price was favorable.

### For Equity Analysts and Model Governance

Model selection should precede calculation. Use DDM when dividend policy is
discernible, connected to profitability, and relevant to a minority holder. Use
FCFE when distributions diverge materially from cash available to equity or when
control over payout is part of the valuation. Consider residual income when cash
flow is negative or forecastability is better in earnings and book value [4][10].
This sequence avoids selecting DDM merely because a dividend number is easy to
retrieve.

For a multistage model, document the bridge from the explicit period to the stable
state. The terminal-year payout, ROE, retention, growth, leverage, and cost of
equity must describe one coherent firm. An H-model is appropriate only when a
linear transition and approximately constant payout and required return are
reasonable simplifications [3][5]. When a business faces a regulatory reset,
patent expiry, recapitalization, or discontinuous competitive change, explicit
scenarios may be preferable to a smooth H-model transition.

Always show sensitivity to r and g and identify the share of value arising after
the explicit forecast. There is no evidence-backed universal rule that a terminal
share above a particular percentage invalidates the model. The relevant questions
are whether the stable state is economically defensible and whether plausible
input changes erase the margin of safety. Penman and Sougiannis' finite-horizon
results and Francis, Olsson, and Oswald's model comparison show why terminal
assumptions and forecast precision deserve as much scrutiny as formula choice
[10][13].

Cross-checking should diagnose assumptions rather than average answers. A DDM and
FCFE model need not fall within a fixed percentage band. If FCFE value exceeds
DDM value, trace whether the dividend forecast fails to distribute accumulated
cash, whether reinvestment is value-creating, or whether terminal payout differs.
If DDM value exceeds FCFE value, test whether distributions require borrowing,
asset sales, or equity issuance. If residual income differs, reconcile book-value
roll-forward and terminal residual returns [4][5][10]. Do not conclude that the
higher model is right merely because it supports the thesis.

Analyst communication should expose the conditional statement. For example:
"At D1 of $2.08, r of 9%, and perpetual g of 4%, the Gordon estimate is $41.60."
Then show the value at alternative r and g and identify the evidence supporting
each range. The simplicity of the formula improves auditability only when the
inputs and their dates are visible. A precise output without input uncertainty is
false precision [4][5].

### For Regulators and Corporate Finance

A reverse DDM can estimate an implied cost of equity or total market return from
price, yield, and growth assumptions. PwC's Ofwat work and Banco de Espana's
financial-institution analysis demonstrate real regulatory and institutional
applications [8][12]. The output is not an observed required return; it is the
return that makes the chosen payout path consistent with the market price. Policy
users should publish the dividend series, averaging window, growth construction,
repurchase treatment, transition, and sensitivity so affected parties can
reproduce the estimate.

Buyback treatment is especially consequential at market level. An aggregate
model that ignores a structural substitution from dividends to repurchases may
misread payout, but a model that adds repurchase yield to per-share growth can
double count it. Gross buybacks can also differ materially from net buybacks after
employee issuance and capital raising [11]. Ofwat's implementation is evidence
that buyback adjustments can be modeled explicitly; the CFA digest is evidence
that they are not automatically superior. Regulators should present both the
mechanical adjustment and the consistency test [8][11].

For corporate managers, the Gordon relation does not imply that raising the
current dividend always raises value. A higher payout leaves less to reinvest, and
sustainable growth depends on retention and the return earned on retained equity
[5]. If incremental investments earn above the cost of equity, lower near-term
payout can support higher future distributions. If they earn below it, retention
can destroy value. The decision is governed by investment opportunity and payout
capacity, not by maximizing D1 or g separately.

Financial institutions require an additional capital bridge. Their reported
earnings may not be distributable if regulatory capital must support asset growth
or absorb risk. Damodaran identifies DDM as useful when FCFE is difficult to
measure for financial firms, but Banco de Espana cautions that a market-average
DDM cost of equity can miss firm-specific conditions [5][12]. Forecast dividends
only after modeling retained capital, balance-sheet growth, losses, and regulatory
constraints.

### For Portfolio Construction and Screening

Yield-plus-growth can organize expected-return thinking, but it is not a complete
portfolio rule. Under stable assumptions, r = D1/P0 + g separates forward income
from modeled price growth [4]. A screen based on that sum should also flag payout
coverage, leverage, transition risk, and r-g sensitivity. Otherwise it can select
high yields created by falling prices and threatened dividends or high growth
assumptions unsupported by reinvestment economics.

The Sorensen-Williamson result justifies further research into systematic DDM
rankings: their more complex DDM produced stronger return discrimination than the
P/E model in the tested 150-stock sample [9]. It does not justify extrapolating the
same performance to every market or period. A portfolio process should define the
universe, record point-in-time forecasts, avoid survivorship bias, include
transaction costs, and test results out of sample before treating the ranking as
an investment signal.

DDM screens naturally emphasize firms with visible payout and may underrepresent
companies that retain cash or use repurchases. That tilt can be intentional, but
it should not be mislabeled as a complete value screen. Run a companion FCFE or
residual-income screen where appropriate, and compare whether omitted companies
lack value or merely use a different distribution policy [4][10]. The author's
assessment is that DDM is strongest as a transparent hypothesis generator and
weakest as a single-number portfolio mandate.

### A Reproducible DDM Review Sequence

A defensible review can be executed in seven steps. First, define whether the
model uses dividends per share or aggregate total payout. Second, reconcile
historical distributions with cash available to equity and net share-count
changes. Third, select constant, two-stage, H-model, or explicit multistage growth
based on the expected transition, not convenience. Fourth, tie stable growth to
retention and ROE. Fifth, estimate a claim-consistent cost of equity. Sixth,
disclose terminal contribution and sensitivity. Seventh, compare with FCFE or
residual income and explain every material difference [3][4][5][10][11].

The stopping rule is equally important. Do not use a Gordon model when r is not
greater than g, when the stable state cannot be defined, or when payout bears no
understandable relation to profitability. Do not use an H-model when the expected
transition is discontinuous or payout and risk change too much for its simplifying
assumptions. In those cases, move to explicit scenarios or another valuation
representation rather than forcing a closed form to return a number [3][4][5].
The DDM's practical contribution is not that it never fails; it is that its
failure conditions can be stated and tested.

## Sources

1. Williams, J. B. (1938). *The Theory of Investment Value*. Harvard
   University Press. Primary source for net-dividend present value.
   https://archive.org/details/in.ernet.dli.2015.225177 [high]

2. Gordon, M. J., and Shapiro, E. (1956). "Capital Equipment Analysis:
   The Required Rate of Profit." *Management Science*, 3(1), 102-110.
   https://doi.org/10.1287/mnsc.3.1.102 [high]

3. Fuller, R. J., and Hsia, C. C. (1984). "A Simplified Common Stock
   Valuation Model." *Financial Analysts Journal*, 40(5), 49-56.
   https://www.jstor.org/stable/4478774 [high]

4. CFA Institute (2026). "Discounted Dividend Valuation." CFA Program
   Refresher Reading.
   https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/discounted-dividend-valuation [high]

5. Damodaran, A. (2012). "Dividend Discount Models." Chapter 13 in
   *Investment Valuation*, 3rd ed. Wiley / NYU Stern author copy.
   https://pages.stern.nyu.edu/~adamodar/pdfiles/val3ed/c13.pdf [high]

6. Grullon, G., and Michaely, R. (2002). "Dividends, Share Repurchases,
   and the Substitution Hypothesis." *Journal of Finance*, 57(4),
   1649-1684.
   https://doi.org/10.1111/1540-6261.00474 [high]

7. Berkshire Hathaway Inc. (1992). "Chairman's Letter to Shareholders."
   Primary quotation of Williams' discounted-cash-flow formulation.
   https://berkshirehathaway.com/letters/1992.html [high]

8. PwC for Ofwat (2019). "Updated Dividend Discount Model Analysis for
   PR19." Regulatory market-return application and buyback sensitivity.
   https://www.ofwat.gov.uk/wp-content/uploads/2019/07/PwC-Updated-Dividend-Discount-Model-analysis-for-PR19.pdf [high]

9. Sorensen, E. H., and Williamson, D. A. (1985). "Some Evidence on the
   Value of Dividend Discount Models." *Financial Analysts Journal*,
   41(6), 60-69.
   https://www.jstor.org/stable/4478886 [high]

10. Francis, J., Olsson, P., and Oswald, D. R. (2000). "Comparing the
    Accuracy and Explainability of Dividend, Free Cash Flow, and
    Abnormal Earnings Equity Value Estimates." *Journal of Accounting
    Research*, 38(1), 45-70.
    https://doi.org/10.2307/2672922 [high]

11. CFA Institute (2015). "Using Dividend Discount Models to Estimate
    Expected Returns." CFA Digest summary of repurchase and per-share
    growth consistency.
    https://rpc.cfainstitute.org/research/cfa-digest/2015/07/using-dividend-discount-models-to-estimate-expected-returns-digest-summary [high]

12. Fernandez Lafuerza, L., and Mencia, J. (2021). "Estimating the Cost
    of Equity for Financial Institutions." *Banco de Espana Financial
    Stability Review*, Issue 40.
    https://www.bde.es/f/webbde/Secciones/Publicaciones/InformesBoletinesRevistas/InformesEstabilidadFinanciera/21/2_Equity_FSR.pdf [high]

13. Penman, S. H., and Sougiannis, T. (1998). "A Comparison of Dividend,
    Cash Flow, and Earnings Approaches to Equity Valuation."
    *Contemporary Accounting Research*, 15(3), 343-383.
    https://doi.org/10.1111/j.1911-3846.1998.tb00564.x [high]

14. Berkshire Hathaway Inc. (2011). "Chairman's Letter to Shareholders."
    Primary discussion of repurchase price relative to intrinsic value.
    https://www.berkshirehathaway.com/letters/2011ltr.pdf [high]

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
