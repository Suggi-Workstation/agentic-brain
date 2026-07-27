---
name: cost-of-capital-capm-wacc-erp
id: 20260727T103113Z
tier: library-topic
domain: valuation-screening
author: Researcher-1
tags: [cost-of-capital, capm, wacc, equity-risk-premium, beta, discount-rate, fama-french]
links: [library/valuation-screening/discounted-cash-flow-dcf-methodology.md, library/valuation-screening/valuation-multiples-pe-ev-ebitda-pb-analysis.md, library/valuation-screening/anchor-valuation-screening.md]
---

# Cost of Capital -- Why the Discount Rate Is Both the Most Important and Most Uncertain Number in Valuation

Cost of capital is the minimum return a company must earn on its
investments to satisfy its providers of capital -- both debt holders
and equity investors. It serves as the discount rate in every
discounted cash flow model, translating future cash flows into present
value. The Capital Asset Pricing Model (CAPM) and the Weighted Average
Cost of Capital (WACC) framework together form the standard toolkit
for estimating this number, yet every input is contested: the equity
risk premium lacks consensus across a 4-6% range, beta is unstable
across estimation windows, and the WACC circularity means the discount
rate depends on the very value it is meant to determine. CAPM fails
key empirical tests -- Fama and French showed that size and value
explain returns better than beta alone -- yet practitioners keep using
it because the alternatives, while theoretically richer, introduce
their own estimation problems. The cost of capital is the place where
valuation theory collides with irreducible uncertainty, and
understanding its limits is more valuable than computing it to two
decimal places.

## Background

The concept of a required return on capital is as old as lending
itself, but its modern theoretical foundations were laid in the
mid-20th century. Harry Markowitz, in his 1952 paper "Portfolio
Selection," introduced the idea that rational investors should care
about the risk and return of their entire portfolio, not individual
securities in isolation. This was the birth of modern portfolio theory
(MPT): diversification reduces idiosyncratic risk for free, so the
only risk that should be priced is systematic risk -- the risk that
cannot be diversified away.

Building on Markowitz, William Sharpe (1964) and John Lintner (1965)
independently developed the Capital Asset Pricing Model, which
translated portfolio theory into a single-factor pricing equation: a
stock's expected return equals the risk-free rate plus a premium
proportional to its sensitivity to the market portfolio, measured by
beta. Sharpe received the 1990 Nobel Prize in Economics for this work.

The Weighted Average Cost of Capital (WACC) framework emerged as the
practical bridge between CAPM's cost of equity and the blended cost of
all capital sources. By weighting the after-tax cost of debt and the
cost of equity by their respective proportions in the capital
structure, WACC provides a single discount rate for enterprise-level
free cash flows. This framework was codified in corporate finance
practice through McKinsey's "Valuation: Measuring and Managing the
Value of Companies" (Copeland, Koller, and Murrin, 1990), now in its
seventh edition and the closest thing valuation has to a standard
reference text.

## Core Concepts

### The Capital Asset Pricing Model

CAPM expresses the cost of equity as a linear function of three
inputs:

```
Cost of Equity = Risk-Free Rate + Beta x Equity Risk Premium
```

The risk-free rate is the return on a default-free government security
whose maturity matches the investment horizon. Because DCF models
project cash flows decades into the future, practitioners typically
use the 10-year government bond yield in the currency of the cash
flows. This is the one input that is directly observable from market
prices -- though even here there is debate about whether to use the
current spot rate (volatile and potentially distorted by central bank
policy) or a normalized long-run rate (stable but subjective).

Beta measures a stock's co-movement with the market portfolio. A beta
of 1.0 means the stock moves in lockstep with the market; a beta of
1.5 means it amplifies market moves by 50 percent; a beta below 1.0
means it dampens them. Beta is estimated by regressing a stock's
historical returns against a broad market index, typically over two to
five years of data. In practice, raw regression betas are adjusted
toward 1.0 using the Bloomberg adjustment (0.67 x raw beta + 0.33 x
1.0), reflecting the empirical tendency of betas to mean-revert over
time.

The equity risk premium (ERP) is the most consequential and most
debated input. It represents the extra return investors demand for
bearing equity risk rather than holding risk-free bonds. Unlike the
risk-free rate, the ERP cannot be directly observed -- it must be
estimated, and the estimation method drives the result. Three
approaches dominate:

The historical approach measures realized excess returns of stocks
over bonds and assumes the future will resemble the past. Depending on
the time period, country, and whether the arithmetic or geometric mean
is used, historical US ERP estimates range from roughly 4 to 7
percent. The problem is that historical ERP is path-dependent: a
century of data dominated by a few outlier decades (the post-war boom,
the 1970s stagflation) may not represent future expectations.

The forward-looking approach, also called the implied ERP, backs out
the discount rate that equates current stock prices with expected
future cash flows. This produces an ERP that varies over time with
market conditions -- it was elevated during the 2008-2009 financial
crisis and compressed during the late-1990s dot-com bubble. Kroll
(formerly Duff and Phelps), the leading provider of cost of capital
data, publishes regularly updated ERP recommendations based on this
methodology. As of mid-2026, Kroll recommended a US ERP of 5.0 percent,
down from 5.5 percent in early 2024.

The survey approach simply asks practitioners, academics, and CFOs
what ERP they use. Pablo Fernandez's annual surveys reveal persistent
disagreement: in any given year, ERP estimates from surveyed
professionals span a range of 4 to 8 percent, even within the same
country.

### The Weighted Average Cost of Capital

WACC blends the cost of equity with the after-tax cost of debt:

```
WACC = (E/V) x Re + (D/V) x Rd x (1 - t)
```

Where E is the market value of equity, D is the market value of debt,
V = E + D is total enterprise value, Re is the cost of equity, Rd is
the pre-tax cost of debt, and t is the marginal corporate tax rate.

The tax adjustment on debt is critical: because interest payments are
tax-deductible, the effective cost of debt is lower than its nominal
rate. This tax shield creates the primary channel through which capital
structure affects the discount rate. All else equal, adding debt lowers
WACC because cheap, tax-advantaged debt replaces expensive equity --
up to the point where financial distress costs offset the tax benefit.

Debt is inherently cheaper than equity because debt holders have
priority claims and contractual payments. A company borrowing at 5
percent with a 25 percent tax rate has an after-tax cost of debt of
3.75 percent -- typically well below its cost of equity. This is why
moderate leverage reduces WACC, a fact that creates tension with the
Modigliani-Miller theorem's prediction that capital structure is
irrelevant in a frictionless world.

### The WACC Circularity Problem

The WACC framework contains a logical circularity that bedevils
valuation practitioners: WACC requires market-value weights for debt
and equity, but the market value of equity is the very output the DCF
model is calculating. The discount rate depends on the value, and the
value depends on the discount rate.

Three practical resolutions exist. The simplest is to use the current
market capitalization for the equity weight, accepting the market's
pricing of the capital structure even if the DCF will produce a
different intrinsic value. This is standard in investment banking and
works for publicly traded companies.

For private companies, or when the analyst believes the market is
significantly mispricing the stock, practitioners use the median
capital structure of a peer group. This breaks the circularity by
importing external weights and produces a WACC that reflects
industry-typical financing.

The rigorous approach is iteration: guess initial weights, calculate
WACC, run the DCF, use the implied equity value to recalculate
weights, and repeat until convergence. Convergence is usually rapid
because WACC's sensitivity to modest weight changes is low -- an
initial guess that is 20 percent off typically produces a WACC error
of only about 30 basis points.

The wrong approach, sometimes used by inexperienced analysts, is to
substitute book-value weights. This can produce catastrophically
misleading results. A technology company with 2 billion dollars in
book equity and 20 billion in market cap would show dramatically
different capital structure weights depending on which measure is
used, producing WACC errors of 2 to 3 percentage points.

## Evidence -- Why CAPM Fails Empirical Tests

The empirical record of CAPM is poor enough that Eugene Fama and
Kenneth French, in their 2004 survey published in the Journal of
Economic Perspectives, concluded that "the empirical record of the
model is poor -- poor enough to invalidate the way it is used in
applications."

The foundational challenge came from Fama and French's 1992 paper "The
Cross-Section of Expected Stock Returns," which demonstrated that
beta -- CAPM's sole risk measure -- does a poor job of explaining the
cross-section of stock returns. Instead, two simple company
characteristics -- market capitalization (size) and the ratio of book
value to market value (value) -- captured far more of the variation in
returns. Small stocks outperformed large stocks, and value stocks
(high book-to-market) outperformed growth stocks, even after
controlling for beta. This was a direct violation of CAPM's core
prediction that beta should be sufficient to explain expected returns.

In response, Fama and French (1993) proposed the three-factor model,
which adds size (SMB, small minus big) and value (HML, high minus low)
factors alongside the market factor. The three-factor model explained
the anomalies that CAPM could not, and it became the standard asset
pricing model in academic research. Fama and French later extended it
to a five-factor model (2015), adding profitability (RMW, robust minus
weak) and investment (CMA, conservative minus aggressive) factors.

An equally damaging anomaly is the low-beta puzzle: contrary to CAPM's
prediction that higher beta should command higher returns, low-beta
stocks have historically outperformed high-beta stocks on a
risk-adjusted basis. This was first documented by Black, Jensen, and
Scholes in 1972. Baker, Bradley, and Wurgler (2011) provided an
explanation rooted in institutional constraints: fund managers
benchmarked to market indices cannot fully exploit the anomaly because
buying low-beta, high-alpha stocks would create tracking error relative
to their benchmark, and shorting high-beta, low-alpha stocks is costly
and risky.

More broadly, a large body of empirical evidence accumulated through
the 1980s and 1990s showed that variables like the price-earnings
ratio, cash flow yield, dividend yield, and momentum all predicted
returns in ways CAPM could not explain. Each anomaly chipped away at
the model's claim to be a complete description of expected returns.

The practical consequence of CAPM's empirical failure is that the cost
of equity estimated from CAPM is an approximation -- sometimes a
reasonable one, sometimes wildly off. Fama and French's own work on
industry costs of equity (1997) showed that CAPM-based estimates had
large standard errors, often spanning 3 percentage points or more. An
analyst who estimates a 10 percent cost of equity may in reality be
looking at a range of 7 to 13 percent.

## Implications

For the practicing valuation analyst, the most important implication
of the cost of capital debate is that precision is an illusion. A DCF
that produces an intrinsic value of 52.37 dollars per share based on a
9.25 percent WACC is less honest than one that shows a valuation range
of 40 to 60 dollars based on WACC assumptions of 8 to 11 percent. The
discount rate is not a fact to be discovered but a judgment to be
exercised, and the first discipline of valuation is acknowledging what
you do not know.

This has concrete consequences. Because WACC is so sensitive to small
input changes, a well-structured valuation model includes a
sensitivity table showing how intrinsic value changes across
reasonable ranges of WACC and terminal growth assumptions. The analyst
who presents a single point estimate without sensitivity analysis is
misleading the reader about the model's precision.

For value investors following the Graham-and-Buffett tradition, the
cost of capital framework reinforces the centrality of margin of
safety. If the discount rate is inherently uncertain, the only
rational response is to demand a substantial gap between price and
estimated intrinsic value. A 30 percent margin of safety on a
valuation built from a roughly-estimated WACC is not paranoia; it is a
direct acknowledgment that the denominator of every discounting
calculation is a best-guess judgment.

The persistence of CAPM in practice, despite decades of academic
criticism, has its own lesson. CAPM survives not because it is correct
but because it is simple, standardized, and everyone uses it. A CAPM
with a judgment call on beta and ERP produces a number that can be
defended in an investment committee. A five-factor Fama-French model
with factor loadings and premiums for five separate risk dimensions
produces multiple numbers that must be estimated, each with its own
uncertainty. The elegance of a single risk factor collapses into the
messiness of multi-factor estimation. CAPM's parsimony is a feature,
not a bug: it forces the analyst to confront the irreducible kernel of
uncertainty in a single number rather than spreading it across five.

The build-up method represents a pragmatic middle ground. Starting
from the risk-free rate, the analyst adds explicit premiums for equity
risk, company size, and company-specific factors (customer
concentration, key-person risk, leverage, business model maturity).
The advantage is transparency: each premium is a visible, debatable
judgment rather than a regression coefficient buried in a beta. For a
small-cap company with concentrated customers, the build-up might
produce: risk-free rate 4 percent + ERP 5 percent + size premium 2
percent + company-specific premium 1 percent = 12 percent cost of
equity. CAPM might assign the same company a beta of 1.1 and produce
4 percent + 1.1 x 5 percent = 9.5 percent, missing the risks the
build-up makes explicit.

Finally, the cost of capital is the point where valuation connects to
the wider world of monetary policy and macroeconomic conditions. When
central banks raise rates, the risk-free rate rises, every CAPM cost
of equity rises with it, and fair values across the market compress
mechanically -- without any change in the underlying businesses. The
analyst who does not understand cost of capital is blind to one of the
most powerful forces driving market valuations.

## Sources

1. Sharpe, W. (1964). "Capital Asset Prices: A Theory of Market
   Equilibrium under Conditions of Risk." Journal of Finance, 19(3),
   425-442. [high]

2. Lintner, J. (1965). "The Valuation of Risk Assets and the Selection
   of Risky Investments in Stock Portfolios and Capital Budgets."
   Review of Economics and Statistics, 47(1), 13-37. [high]

3. Fama, E. & French, K. (2004). "The Capital Asset Pricing Model:
   Theory and Evidence." Journal of Economic Perspectives, 18(3),
   25-46.
   https://www.aeaweb.org/articles?id=10.1257/0895330042162430 [high]

4. Fama, E. & French, K. (1992). "The Cross-Section of Expected Stock
   Returns." Journal of Finance, 47(2), 427-465. [high]

5. Baker, M., Bradley, B. & Wurgler, J. (2011). "Benchmarks as Limits
   to Arbitrage: Understanding the Low-Volatility Anomaly." Financial
   Analysts Journal, 67(1), 40-54.
   https://doi.org/10.2469/faj.v67.n1.4 [high]

6. KPMG (2024). "Cost of Capital Study 2024."
   https://assets.kpmg.com/content/dam/kpmgsites/ch/pdf/cost-of-capital-study-2024.pdf
   [high]

7. Kroll. "Recommended U.S. Equity Risk Premium and Corresponding
   Risk-Free Rates." Updated regularly.
   https://www.kroll.com/en/reports/cost-of-capital/recommended-us-equity-risk-premium-and-corresponding-risk-free-rates
   [high]

8. Wall Street Prep. "Cost of Capital: Formula and Calculator."
   https://www.wallstreetprep.com/knowledge/cost-of-capital [medium]

## See Also

- `library/valuation-screening/discounted-cash-flow-dcf-methodology.md` --
  the DCF framework that uses cost of capital as its discount rate.
- `library/valuation-screening/valuation-multiples-pe-ev-ebitda-pb-analysis.md` --
  multiples-based valuation as an alternative to discount-rate-dependent DCF.
- `library/portfolio-risk-management/anchor-portfolio-risk-management.md` --
  how cost of capital connects to portfolio-level risk and return.
