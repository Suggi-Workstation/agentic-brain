---
name: risk-adjusted-performance-measurement
id: 20260928T170400Z
tier: library-topic
domain: portfolio-risk-management
author: Librarian
tags: [risk-adjusted-performance, sharpe-ratio, sortino-ratio, information-ratio, treynor-ratio, benchmark-selection, manager-evaluation, performance-attribution]
links: [library/portfolio-risk-management/modern-portfolio-theory.md, library/portfolio-risk-management/drawdown-analysis-and-management.md, library/portfolio-risk-management/volatility-targeting.md, library/portfolio-risk-management/value-at-risk-risk-measurement-frameworks.md]
---

# Risk-Adjusted Performance Measurement -- No Single Ratio Proves Investment Skill

Risk-adjusted performance measures compare return with a specified definition of risk, but each ratio answers a different question and inherits the weaknesses of its data, benchmark, and model [2][6][7]. A defensible evaluation therefore uses several compatible measures, tests the return history for sampling and smoothing problems, and connects the statistics to drawdowns, attribution, leverage, liquidity, costs, and qualitative evidence about the investment process [8][9][11][12].

## Background

Investment performance cannot be evaluated from return alone because a manager can usually seek more return by accepting more exposure, leverage, concentration, or downside risk. The central measurement problem is therefore comparative: determine what return was earned, identify the risk that made it possible, and ask whether another portfolio, benchmark, or financing mix could have produced a similar outcome. Modern risk-adjusted measurement developed as portfolio theory supplied explicit definitions of total and systematic risk. Treynor's 1965 work evaluated performance after accounting for market-related variation, while Sharpe's 1966 mutual-fund study introduced the reward-to-variability ratio, the predecessor of the Sharpe ratio [1][3].

Sharpe's original formulation compared average return above a risk-free alternative with total return variability. The measure made performance ranking more informative than raw return ranking because it charged a portfolio for the full standard deviation of its return history [1]. Sharpe later clarified that the ratio should be understood through a zero-investment strategy: a differential return is earned by holding the fund and financing it with an appropriate benchmark or risk-free position. He also emphasized that historical, or ex post, measures are commonly used to support expectations about future, or ex ante, performance even though that inference requires an assumption that the historical relationship has predictive value [2].

Treynor and Sharpe used different denominators. The Treynor ratio charges excess return for beta, the portfolio's sensitivity to a selected market benchmark, whereas the Sharpe ratio charges it for total standard deviation. The distinction follows the Capital Asset Pricing Model: a diversified investor should not be rewarded for idiosyncratic risk that could have been removed, so systematic risk is the relevant denominator in a Treynor evaluation. A concentrated or poorly diversified portfolio can nevertheless have substantial total risk that beta does not capture, which can cause Treynor and Sharpe rankings to diverge [3].

Jensen extended the benchmark-relative approach in 1968. Jensen's alpha estimates the portion of return left after subtracting the return implied by the risk-free rate, market premium, and portfolio beta. His study applied the measure to 115 open-end mutual funds over observations drawn from 1945 through 1964 and found little evidence that the average fund forecast security prices well enough to outperform a buy-and-hold market policy after expenses [4]. The lasting contribution is not that one historical fund sample settled the active-management question; it is that performance could be represented as a regression intercept and subjected to statistical inference rather than described only by a raw return ranking [4].

Later measures changed the definition of risk or comparison. Sortino and Price placed a minimum acceptable return, or other target, in the numerator and downside deviation in the denominator, so returns above the target are not treated as harmful volatility [5]. The information ratio compares active return with tracking error relative to a benchmark and is therefore designed for benchmark-aware active management [6]. Modigliani and Modigliani rescaled a Sharpe ratio to the volatility of a benchmark, translating an abstract ratio into a return at a common risk level [13]. Keating and Shadwick's Omega measure compared probability-weighted gains above a threshold with probability-weighted losses below it and used more of the return distribution than mean and variance alone [14].

These measures did not eliminate the original problem; they divided it into better-defined questions. Total volatility, downside shortfall, benchmark-relative variability, market beta, maximum drawdown, and the full return distribution are not interchangeable concepts. A strategy may rank well under one and poorly under another because the measures penalize different return paths. That disagreement is useful evidence when the evaluation asks why the rankings differ rather than selecting the most flattering statistic [3][5][14].

Measurement practice also became more explicit about benchmark governance. The Global Investment Performance Standards require an appropriate total-return benchmark when one is available and make fair representation and full disclosure governing principles. Their benchmark guidance states that benchmark selection and review should be documented; it also recognizes broad indexes, style indexes, blends, target returns, factor models, returns-based benchmarks, and leveraged benchmarks as distinct choices whose construction affects interpretation [11]. The benchmark is therefore part of the measurement claim, not an incidental input.

The history of these measures supports a bounded conclusion. Ratios compress return and one risk definition into a summary statistic, while alpha and attribution compare realized performance with a model or policy benchmark. None directly observes skill. Skill is a causal explanation for a repeatable decision process; a ratio is an estimate from a finite, path-dependent return sample. The author's synthesis is that risk-adjusted performance measurement is strongest as a diagnostic system: it narrows the questions that due diligence must answer, but it cannot replace due diligence [2][7][9].

## Core Concepts

### Begin with a measurement contract

A meaningful calculation requires a measurement contract established before rankings are examined. It specifies the portfolio, investor objective, return series, currency, fee basis, cash flows, valuation method, risk-free proxy, benchmark, target return, observation frequency, evaluation horizon, and treatment of leverage. GIPS guidance treats documented benchmark selection, fair representation, and disclosure as part of valid performance presentation rather than as optional commentary [11]. The author's synthesis is that the same discipline should govern every input: an evaluator who changes the benchmark, target, or sampling interval after seeing the answer is selecting a narrative, not measuring a stable proposition.

Returns must be comparable. Portfolio and benchmark returns should cover the same dates, use the same periodicity and currency convention, and be stated consistently before or after fees. A gross return can describe investment implementation, while a net return describes what an investor retained; the label cannot be omitted because fees can change both the numerator and the ranking. Illiquid holdings require particular scrutiny because appraised or stale values can move risk across reporting periods and reduce measured volatility without reducing economic risk [8].

The horizon also belongs in the contract. Sharpe showed that the ratio depends on the period over which differential returns are measured, and Goodwin compared alternative annualization methods for the information ratio [2][6]. A daily, monthly, and annual statistic need not describe the same path. The evaluator should retain the base-frequency series, disclose the conversion rule, and avoid combining a return numerator from one frequency with a risk denominator from another.

### Sharpe ratio: excess return per unit of total variability

For periodic portfolio return R_p and periodic risk-free return R_f, the ex post Sharpe ratio is:

```
Sharpe = mean(R_p - R_f) / standard-deviation(R_p - R_f)
```

The numerator is average differential return and the denominator is the standard deviation of that differential return. The ratio asks how much average excess return accompanied each unit of total variability in the financing-adjusted strategy [1][2]. It is most directly useful when the investor is evaluating a complete risky portfolio rather than a small sleeve inside a larger portfolio, because the denominator includes systematic and idiosyncratic variation.

Under ideal linear financing with one risk-free rate, multiplying a portfolio's exposure and excess return by the same positive leverage factor leaves the Sharpe ratio unchanged. This property permits comparison at a common scale in theory, but actual borrowing spreads, margin calls, exposure caps, nonlinear derivatives, and forced liquidation violate the simple scaling assumption. Sharpe's 1994 discussion uses leverage to show how the optimal position size changes even when the ratio is unchanged [2]. The author's synthesis is that leverage invariance is a normalization property, not evidence that leverage is harmless.

The denominator treats upside and downside deviations symmetrically. That treatment is appropriate when variance is the decision maker's intended risk measure or when the return distribution is sufficiently well described by mean and variance. It can mislead when a strategy has option-like or strongly skewed payoffs. A strategy that collects many small gains and occasionally suffers a large loss can report a stable mean and low ordinary volatility before the tail event, so its Sharpe ratio must be read with skewness, tail-loss, and drawdown measures [9][10][14].

### Sortino ratio: excess over a target per unit of downside deviation

For minimum acceptable return MAR and target downside deviation DD, the Sortino ratio is:

```
Sortino = (mean(R_p) - MAR) / DD
DD = square-root(mean(min(0, R_p - MAR)^2))
```

The average inside DD uses all observations, with zero contribution from returns at or above the target. This convention matters: dividing only by the number of observations below MAR produces a different denominator and can overstate or understate the intended risk statistic [5]. The ratio asks how much return above the investor's target was earned per unit of observed shortfall variability.

MAR is an economic choice, not a universal constant. It may represent zero, inflation, a liability growth rate, a cash rate, or a market benchmark. Comparisons require the same target and the same downside-deviation convention. CFA Institute's review notes that downside deviation can be understated when most sample returns are positive and that changing monthly versus annual measurement can change the result materially [5]. The Sortino ratio is therefore a complement to, not a replacement for, total volatility and direct tail-loss measures.

### Information ratio: active return per unit of benchmark-relative risk

For active return A_t = R_p,t - R_b,t relative to benchmark R_b, the information ratio is:

```
Information-ratio = mean(A_t) / standard-deviation(A_t)
```

The denominator is tracking error. The measure asks how efficiently an active manager converted deviations from the benchmark into average excess return. Goodwin emphasized both calculation ambiguity and the relationship between the information ratio and a t-statistic; the same ratio can have different evidential strength when track-record lengths differ [6]. A ratio based on twelve monthly observations should not be treated as equally precise as the same ratio based on one hundred twenty comparable observations.

Benchmark choice governs the answer. A global equity manager can have low tracking error against one global index and high tracking error against a domestic index. A style-drifting manager may look skilled against an inappropriate broad benchmark because the benchmark fails to represent the strategy's actual opportunity set. GIPS guidance therefore requires benchmark descriptions and recommends a documented selection process; it recognizes that leveraged or benchmark-agnostic strategies may require leveraged, target-return, or other purpose-built comparisons [11].

The information ratio is especially useful for a funded active mandate whose policy benchmark is fixed in advance. It is less informative for a total-return strategy whose exposures move across asset classes and whose stated objective is not benchmark-relative. The author's synthesis is that a low information ratio can mean poor decisions, excessive active risk, or the wrong benchmark; attribution and exposure analysis are needed to distinguish those explanations [6][11][12].

### Treynor ratio and Jensen's alpha: performance relative to systematic risk

The Treynor ratio uses beta rather than total standard deviation:

```
Treynor = (mean(R_p) - mean(R_f)) / beta_p
beta_p = covariance(R_p, R_b) / variance(R_b)
```

It asks how much excess return was earned per unit of market-related sensitivity. Because beta excludes idiosyncratic variation, the measure is most relevant for a diversified portfolio evaluated against an appropriate market benchmark. CFA Institute notes that a poorly diversified portfolio with low beta but high total risk can look superior under Treynor even when its Sharpe ratio is weak [3]. A very small or negative beta can also make the ratio unstable or difficult to rank economically.

Jensen's alpha uses the same beta model but reports abnormal return in return units:

```
Jensen-alpha = mean(R_p - R_f) - beta_p * mean(R_b - R_f)
```

A positive estimate means the portfolio earned more than the single-factor CAPM relation would predict for its beta; a negative estimate means it earned less [3][4]. This interpretation is conditional on the model. A positive CAPM alpha can disappear under a style or multifactor model if the return came from persistent exposure to value, size, momentum, credit, duration, or another compensated factor. CFA Institute's discussion therefore treats benchmark fit and R-squared as relevant checks on whether beta describes the portfolio well [3].

### M-squared, Calmar, and Omega: translations and alternative risk questions

Modigliani-Modigliani performance, commonly called M-squared, rescales the portfolio's Sharpe ratio to benchmark volatility and adds the risk-free return:

```
M-squared = R_f + Sharpe_p * standard-deviation(R_b - R_f)
```

The result is a return at the benchmark's volatility rather than a dimensionless ratio. It preserves the ranking implied by Sharpe under consistent inputs, but makes the comparison easier to communicate in percentage-return units [13]. It does not solve the Sharpe ratio's problems with non-normality, serial correlation, or a misspecified financing rate.

The Calmar ratio divides compound annual growth by maximum drawdown over the same period. It maps return to the worst observed peak-to-trough decline rather than to average variability [15]. Maximum drawdown is path dependent and sample dependent: one extreme event can dominate the denominator, while a short history may simply not contain a severe event. Calmar should therefore be reported with drawdown depth, duration, recovery time, and the exact window rather than as an isolated ranking number [15].

Omega compares probability-weighted gains above a threshold with probability-weighted losses below it. Keating and Shadwick designed the measure to incorporate the return distribution beyond mean and variance and to let the decision threshold distinguish gains from losses [14]. Omega can reveal differences that a mean-variance statistic suppresses, but it remains threshold and sample dependent. Sparse tail observations make any full-distribution estimate uncertain, so a complex measure does not eliminate the need for a long, representative history.

### Annualization, autocorrelation, and effective sample size

The familiar square-root rule annualizes a ratio only under restrictive conditions. If periodic returns are independently and identically distributed and the one-period Sharpe ratio is S, a q-period ratio scales by square-root(q). Sharpe explicitly stated the zero-serial-correlation condition in his time-dependence discussion [2]. Lo derived the general stationary-return adjustment and showed that the correct multiplier depends on return autocorrelations; ordinary square-root annualization can materially overstate or understate the ratio [7].

Positive autocorrelation reduces the amount of independent information in a reported series. Illiquid holdings, stale prices, discretionary marks, and return smoothing can spread one economic price move across several reporting periods. That process lowers measured monthly volatility, raises conventional Sharpe ratios, and can reduce measured beta even though the underlying economic exposure has not disappeared [7][8]. The evaluator should inspect autocorrelation, valuation lags, holdings liquidity, and the gap between appraisal and transaction data before accepting any annualized ratio.

Sampling error remains even without autocorrelation. Expected return and volatility are unknown and must be estimated from realized data, so every ratio is an estimate with uncertainty [7]. Confidence intervals, block bootstrap methods, heteroskedasticity-and-autocorrelation-consistent errors, and minimum track-record tests are more informative than a point estimate alone. When many strategies, parameters, or managers were screened, the selected maximum also contains multiple-testing bias; the Deflated Sharpe Ratio was designed to adjust for selection bias and non-normal returns in that setting [10].

### A ratio map prevents category errors

The ratios can be organized by the question they answer:

| Measure | Numerator | Risk or comparison | Best-fit question | Primary vulnerability |
|:--|:--|:--|:--|:--|
| Sharpe | Excess return over cash | Total differential-return volatility | How efficient was a complete risky portfolio? | Skew, smoothing, sampling, financing assumptions |
| Sortino | Return over MAR | Downside deviation below MAR | How efficiently was a target exceeded? | Target and downside convention |
| Information | Active return | Tracking error to benchmark | How efficient was benchmark-relative active risk? | Benchmark choice and short histories |
| Treynor | Excess return over cash | Market beta | How much return accompanied systematic risk? | Diversification, beta instability, benchmark fit |
| Jensen alpha | Model-adjusted excess return | CAPM or factor-model expectation | Was return above the model-implied requirement? | Model and factor omission |
| M-squared | Sharpe rescaled to benchmark risk | Benchmark volatility | What return corresponds to a common volatility? | Inherits Sharpe assumptions |
| Calmar | Compound return | Maximum drawdown | What return accompanied the worst observed loss path? | Window and path dependence |
| Omega | Gains above threshold | Losses below threshold | How did the full sample distribute gains and losses? | Threshold and tail-sample uncertainty |

The author's synthesis is that the map should be selected before the numbers are calculated. Choosing a denominator because it produces the highest rank reverses the logic of measurement. The correct measure follows from the investor's risk, mandate, and decision context [3][5][6][11].

## Evidence

### Serial correlation can change both the level and ranking of Sharpe ratios

Lo derived sampling distributions for Sharpe-ratio estimators under independently distributed and stationary returns and examined time aggregation. His empirical hedge-fund example found that ignoring serial correlation could overstate an annual Sharpe ratio by as much as 65 percent, and correcting the dependence could change fund rankings materially [7]. The result directly rejects automatic multiplication of a monthly ratio by square-root(12) when returns are serially correlated.

Getmansky, Lo, and Makarov developed an econometric model in which observed returns are smoothed versions of unobserved economic returns. They connected serial correlation in alternative-investment returns to illiquidity and smoothed marks, then showed analytically and empirically that smoothing can reduce measured beta and inflate the Sharpe ratio [8]. Their reported model examples produced large increases in conventional Sharpe ratios as more of an economic return was distributed across reporting periods [8]. The evidence implies that a smooth return series can be a liquidity warning rather than proof of superior control.

These studies distinguish two problems. Lo's time-aggregation result shows that even genuine serial dependence invalidates naive annualization. Getmansky, Lo, and Makarov show that the dependence may itself be evidence of stale valuation or illiquidity. A corrected ratio addresses the statistical symptom, while holdings, valuation, and redemption analysis address the economic cause [7][8].

### Downside measures add information but can have sparse denominators

CFA Institute's examination of the Sortino ratio uses the Japanese equity market from 1980 through 1989 to illustrate sample sensitivity: all ten calendar-year returns were positive, although the same period contained thirty-six negative months, and the market then fell sharply in 1990 [5]. An annual downside-deviation calculation over the first period would have had little or no negative annual evidence, while a monthly calculation would have recorded many shortfalls. The economic asset did not change; the frequency and sample boundary changed the denominator.

The same review identifies a recurring calculation error: some implementations divide squared shortfalls by the number of below-target observations instead of by all observations. It also states that the Sortino ratio should compare funds under the same MAR [5]. This evidence supports disclosure of the formula, target, and frequency rather than reporting the ratio name alone.

### Benchmarks determine what active performance means

Goodwin documented continuing confusion about information-ratio calculation, interpretation, and annualization. He connected the ratio with a t-statistic and examined empirical distributions by investment style, demonstrating that a ratio needs both statistical and peer context [6]. A manager's active return cannot be interpreted independently of the benchmark that defines both the numerator and tracking-error denominator.

CFA Institute's GIPS benchmark guidance makes that dependence operational. It requires an appropriate total-return benchmark when available, a description of the benchmark, and documented policies for benchmark selection and maintenance. The guidance discusses style, blended, returns-based, factor-based, target-return, and leveraged benchmarks because different mandates require different reference portfolios [11]. A benchmark that omits leverage or uses the wrong opportunity set can make relative performance appear better or worse without any change in the portfolio.

Treynor ratios and Jensen alpha share the same dependency. CFA Institute notes that beta gains interpretive weight when portfolio and benchmark returns have a high R-squared, while low R-squared indicates that the selected benchmark explains little of the portfolio's variation [3]. The evidence does not create a universal R-squared cutoff. It establishes that beta-based claims require evidence that the benchmark represents the portfolio's risk drivers.

### Popular measures can be gamed

Goetzmann, Ingersoll, Spiegel, and Welch analyzed incentives created when a principal rewards a manager according to a performance measure. They showed that popular measures can be manipulated even with high transaction costs and developed conditions for a manipulation-proof alternative based on average power utility [9]. They argued that the issue is especially relevant to hedge funds because broad derivative authority and nonlinear compensation create both the means and incentive to reshape reported return distributions [9].

The mechanism is broader than deliberate misconduct. Selling deep out-of-the-money options, concentrating in illiquid credit, or taking contingent leverage can produce many quiet gains and rare losses. A sample ending before the loss can show high Sharpe and Sortino ratios because the negative tail is unobserved. The author's synthesis is that an apparently exceptional ratio should trigger examination of payoff shape, derivatives, collateral, liquidity, and stress loss before it triggers admiration [8][9].

### Multiple testing inflates the winner

Bailey and Lopez de Prado addressed performance inflation from backtest overfitting and selection bias. When researchers test many strategy variants and report the best one, the selected Sharpe ratio is conditioned on winning a search rather than on being a single prespecified test. Their Deflated Sharpe Ratio adjusts for multiple testing and non-normal returns to help distinguish an empirical finding from a statistical fluke [10].

This evidence applies to manager selection as well as quantitative backtests. Screening a large universe and choosing the manager with the highest recent ratio creates an implicit multiple-comparison problem even when no code was optimized. The exact correction depends on the search process, but the governance lesson is stable: retain the number and dependence of trials, separate research from holdout evaluation, and do not interpret the selected maximum as an unbiased estimate of future performance [10].

### Attribution answers a different question from a ratio

Brinson, Hood, and Beebower decomposed pension-plan performance into investment policy, market timing, and security selection relative to a passive policy portfolio. In their sample of 91 large US pension plans from 1974 through 1983, policy explained most time-series variation in total plan returns, and average actual return was below the policy benchmark [12]. The specific percentage from that historical sample should not be universalized, but the framework demonstrates why a ratio cannot identify which decisions produced performance.

A high information ratio can arise from security selection, tactical allocation, factor exposure, or a benchmark mismatch. A high Sharpe ratio can reflect diversification, implicit market exposure, leverage, smoothing, or genuine forecasting. Attribution connects return to decisions, while stress tests and drawdown analysis connect those decisions to adverse paths. The author's synthesis is that a performance claim becomes stronger when the ratio, attribution, holdings, and process evidence point to the same mechanism [8][11][12].

### Historical success is not direct proof of future skill

Sharpe's 1994 formulation explicitly distinguishes ex post computation from ex ante justification and notes that using historical measures for decisions assumes some predictive ability [2]. Lo shows that estimation error surrounds the ratio even before persistence is considered [7]. Jensen's original fund study used a long sample and statistical tests yet still framed the result as evidence about a defined historical population and model [4]. Together these sources support calibrated language: a return history can be consistent with skill, inconsistent with skill, or too imprecise to decide; the statistic does not observe skill directly.

## Implications

### Use a staged evaluation rather than a leaderboard

The first practical implication is procedural. Begin with the mandate and write the measurement contract before viewing rankings. State whether success means absolute compounding, preservation above a liability rate, benchmark-relative return, drawdown control, or contribution to a larger portfolio. That objective selects the numerator, denominator, benchmark, and target. A benchmark-aware equity mandate naturally calls for active return, tracking error, information ratio, factor alpha, and attribution; an absolute-return strategy requires cash-relative return, total and downside risk, liquidity, leverage, and tail analysis [3][6][11].

Second, reconstruct returns on a consistent basis. Align dates, currencies, cash flows, valuation points, fees, and financing. Report gross and net results when both investment implementation and investor experience matter. Separate actual live results from simulated, model, or linked predecessor records. GIPS standards make fair representation, full disclosure, consistent calculation policies, and appropriate benchmarks core performance-presentation principles [11].

Third, inspect the return-generating process before annualizing. Plot the distribution and cumulative wealth path; calculate skewness, kurtosis, drawdowns, autocorrelations, and missing observations; compare reported marks with holdings liquidity. If autocorrelation is material, use an adjustment consistent with the dependence structure and show both conventional and adjusted results. If valuations are appraisal based, do not treat a lower reported standard deviation as automatically lower economic risk [7][8].

Fourth, calculate a small dashboard whose components answer nonredundant questions. A useful minimum is net compound return, Sharpe ratio, Sortino ratio under a stated MAR, information ratio against a prespecified benchmark, factor alpha with confidence intervals, maximum drawdown and recovery duration, and a tail-loss or stress measure. Treynor or Jensen statistics are appropriate when beta and benchmark fit are economically meaningful; M-squared can translate the Sharpe comparison into return units [3][13]. The dashboard should not expand until one favorable statistic appears.

Fifth, attach uncertainty. Report observation count, base frequency, track-record length, confidence interval or standard error, and autocorrelation method. For a strategy selected from many trials, record the search space and use a multiple-testing adjustment or genuine holdout. For a manager chosen from a large peer universe, treat the selected ratio as an extreme order statistic rather than an ordinary estimate [7][10].

Sixth, move from measurement to explanation. Attribute active return to allocation, selection, currency, factor, and interaction effects as appropriate to the mandate. Compare those effects with stated process and portfolio holdings. Brinson-style attribution can separate policy from active decisions, while factor models can separate common exposures from residual alpha [3][12]. A manager who claims security-selection skill but whose return is explained by a persistent factor tilt has produced a different result from the one advertised.

Seventh, test survival rather than average elegance. Pair ratios with maximum and average drawdown, time under water, expected shortfall, scenario analysis, financing stress, redemption terms, collateral demands, and market capacity. The single worst error is to reward a smooth, high ratio created by hidden illiquidity or short-tail exposure; it can concentrate capital in a strategy whose measured risk is lowest immediately before forced loss. Autocorrelation checks, independent valuation, holdings transparency, and nonlinear stress tests directly address that failure mode [8][9].

### For asset owners and investment committees

An asset owner should evaluate managers relative to the role each mandate plays in the total fund. A low-volatility liability hedge, a benchmark-relative equity sleeve, and an unconstrained diversifier should not be ranked by one universal ratio. The first may be judged by hedge effectiveness and funding risk, the second by information ratio and attribution, and the third by cash-relative compounding, drawdown, liquidity, and crisis behavior. GIPS guidance supports mandate-relevant benchmark selection and explicit treatment of leveraged or target-return strategies [11].

Committee materials should show the same metric definitions through time. Benchmark changes, target changes, or restated histories must be disclosed rather than silently spliced. A rolling window can reveal changing performance, but it should accompany the full history because a window can remove a major loss from the denominator or from maximum drawdown. The committee should ask what aged out, not only what improved.

Ratios should inform capital allocation only after capacity and correlation are considered. Two managers with identical stand-alone Sharpe ratios can contribute differently to the total portfolio if one diversifies existing risks and the other duplicates them. Sharpe's framework notes that a stand-alone ratio does not incorporate every correlation relevant to the investor's other holdings [2]. The portfolio decision therefore requires marginal contribution to total risk and stress loss, not a manager leaderboard alone.

### For manager due diligence

Due diligence should reconcile four records: the numerical return history, current holdings, historical exposures, and the documented decision process. If the return series is smoother than the holdings imply, investigate stale marks, nonsynchronous pricing, side pockets, and valuation discretion. If beta or factor exposure changes through time, a full-period alpha can average unlike regimes and hide style drift. If a strategy uses options, examine scenario payoffs rather than infer tail behavior from ordinary standard deviation [3][8][9].

The evaluator should request the formula implementation, not only the reported label. For Sortino, obtain MAR, observation frequency, denominator convention, and treatment of returns exactly at the target. For Sharpe, obtain the risk-free series, compounding and annualization rules, and autocorrelation adjustment. For information ratio, obtain the benchmark, rebalancing method, treatment of fees and cash, and tracking-error convention. For alpha, obtain factors, regression frequency, intercept annualization, standard errors, and whether model selection preceded or followed result inspection [5][6][7][10].

Qualitative process evidence matters because a ratio can be generated by luck. Relevant evidence includes whether the manager articulated the expected edge before the period, whether holdings expressed that edge, whether losses and gains occurred for predicted reasons, whether capacity and costs were modeled, whether decision rules were followed, and whether unsuccessful trials remain in the research archive. The author's synthesis is that process evidence cannot prove future outperformance, but inconsistency between story, holdings, and attribution can disprove the claimed mechanism.

### For individual investors

An individual investor can use a simpler version of the same framework. Compare funds over the same period, currency, and fee basis; use a benchmark that represents what the fund actually owns; inspect maximum drawdown and recovery; and avoid ranking short histories by one annualized ratio. A diversified total-portfolio fund may be compared with Sharpe and M-squared, while an active fund should also be compared with information ratio and benchmark-relative attribution [2][6][13].

The investor should translate statistical risk into behavioral and financial capacity. A favorable Sharpe ratio does not reveal whether a 35 percent drawdown would cause a sale, whether cash is needed during the recovery, or whether leverage can force liquidation. Direct drawdown and liquidity evidence should therefore sit beside the ratio [8][15]. A measure is useful only if its definition of risk matches the risk that can interrupt the investor's plan.

### Interpret disagreement as information

When ratios disagree, identify the denominator causing the disagreement. A strong Treynor ratio and weak Sharpe ratio suggest that idiosyncratic risk is material relative to beta. A strong Sortino ratio and weak Sharpe ratio can mean that much volatility occurred above MAR, although the downside sample may also be sparse. A strong Sharpe ratio and weak Calmar ratio can indicate an otherwise smooth series with one deep loss. A strong information ratio against one benchmark and a weak ratio against another signals that benchmark definition is governing the claim [3][5][6].

This diagnostic approach avoids declaring one measure universally superior. Each statistic is a deliberately compressed view. Agreement across measures based on different risk definitions is stronger evidence of robust historical efficiency than one exceptional number; disagreement is a prompt to inspect the return path, exposures, benchmark, and objective. The author's assessment is that unexplained disagreement is a due-diligence gap, not a reason to average the ratios.

### Keep the conclusion narrower than the data

The final report should distinguish description, inference, and decision. Description states the realized return, risk, drawdown, and exposure measures. Inference states uncertainty and the evidence for persistence or skill. Decision compares the result with the investor's objective, alternatives, and constraints. Sharpe, Lo, and Goodwin all show in different ways that calculation and interpretation are separate problems [2][6][7].

A defensible conclusion is conditional: over a stated period, under a stated benchmark and calculation convention, the portfolio earned a stated risk-adjusted result; the result is or is not robust to alternative frequencies, autocorrelation, costs, factors, and tail measures; and the observed mechanism is or is not consistent with the stated process. The conclusion should not say that one ratio proves skill. Skill remains a hypothesis tested by repeated, economically coherent evidence.

## Common Pitfalls

### Comparing incompatible inputs

Ratios cannot be compared when one portfolio is gross of fees and another is net, when currencies differ, when risk-free proxies differ, or when return and risk use different frequencies. Standardize inputs or label the comparison invalid [2][5][11].

### Selecting the benchmark after seeing performance

A manager can improve apparent active return, tracking error, beta, or alpha by changing the reference portfolio. Specify the benchmark before the evaluation period and document any later change with its economic reason [3][6][11].

### Treating square-root annualization as automatic

The square-root rule assumes conditions that positive or negative serial correlation violates. Test dependence and apply a consistent adjustment rather than hiding it inside a spreadsheet default [2][7][8].

### Rewarding smooth illiquid marks

Stale or discretionary valuations can reduce reported volatility and beta while raising conventional risk-adjusted ratios. Check liquidity, mark sources, appraisal lags, autocorrelation, and transaction evidence [8].

### Ignoring skew and nonlinear payoff

Mean and standard deviation can underdescribe strategies with derivatives, short volatility, or rare crash exposure. Add distributional, drawdown, expected-shortfall, and scenario measures; inspect the payoff directly [9][10][14].

### Ranking very short or selected records

A high ratio from a short sample has wide uncertainty, and the best ratio selected from many candidates is upward biased. Report uncertainty, the size of the search, and out-of-sample evidence [6][7][10].

### Confusing attribution with proof of skill

Attribution identifies where historical return came from; it does not establish that the source will persist. Combine attribution with process evidence, economic rationale, costs, and repeated out-of-sample results [12].

### Ratio shopping

Calculating many measures and reporting only the most favorable one creates selection bias. Define the dashboard in advance and preserve unfavorable metrics and failed variants [9][10].

## Sources

1. Sharpe, W. F. (1966). "Mutual Fund Performance." The Journal of
   Business, 39(1), 119-138. https://web.stanford.edu/~wfsharpe/art/mfp.pdf
   [high]

2. Sharpe, W. F. (1994). "The Sharpe Ratio." The Journal of Portfolio
   Management, 21(1), 49-58.
   https://web.stanford.edu/~wfsharpe/art/sr/sr.htm [high]

3. Kidd, D. (2011). "Measures of Risk-Adjusted Return: Let's Not Forget
   Treynor and Jensen." CFA Institute.
   https://rpc.cfainstitute.org/sites/default/files/-/media/documents/code/gips/measures-risk-adjusted-return.pdf
   [high]

4. Jensen, M. C. (1968). "The Performance of Mutual Funds in the Period
   1945-1964." The Journal of Finance, 23(2), 389-416.
   https://onlinelibrary.wiley.com/doi/full/10.1111/j.1540-6261.1968.tb00815.x
   [high]

5. Kidd, D. (2012). "The Sortino Ratio: Is Downside Risk the Only Risk
   That Matters?" CFA Institute.
   https://rpc.cfainstitute.org/sites/default/files/-/media/documents/code/gips/the-sortino-ratio.pdf
   [high]

6. Goodwin, T. H. (1998). "The Information Ratio." Financial Analysts
   Journal, 54(4), 34-43.
   https://rpc.cfainstitute.org/research/financial-analysts-journal/1998/the-information-ratio
   [high]

7. Lo, A. W. (2002). "The Statistics of Sharpe Ratios." Financial
   Analysts Journal, 58(4), 36-52.
   https://rpc.cfainstitute.org/research/financial-analysts-journal/2002/the-statistics-of-sharpe-ratios
   [high]

8. Getmansky, M., Lo, A. W. & Makarov, I. (2004). "An Econometric Model
   of Serial Correlation and Illiquidity in Hedge Fund Returns." Journal
   of Financial Economics, 74(3), 529-609.
   https://web.mit.edu/Alo/www/Papers/JFE2004Pub.pdf [high]

9. Goetzmann, W. N., Ingersoll, J. E., Spiegel, M. I. & Welch, I. (2007).
   "Portfolio Performance Manipulation and Manipulation-Proof Performance
   Measures." Review of Financial Studies, 20(5), 1503-1546.
   https://papers.ssrn.com/sol3/papers.cfm?abstract_id=302815 [high]

10. Bailey, D. H. & Lopez de Prado, M. (2014). "The Deflated Sharpe Ratio:
    Correcting for Selection Bias, Backtest Overfitting, and
    Non-Normality." The Journal of Portfolio Management, 40(5), 94-107.
    https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2460551 [high]

11. CFA Institute (2023). "Guidance Statement on Benchmarks for Firms."
    Global Investment Performance Standards.
    https://www.gipsstandards.org/wp-content/uploads/2023/08/gs_benchmarks_firms.pdf
    [high]

12. Brinson, G. P., Hood, L. R. & Beebower, G. L. (1986).
    "Determinants of Portfolio Performance." Financial Analysts Journal,
    42(4), 39-44.
    https://www.tandfonline.com/doi/abs/10.2469/faj.v42.n4.39 [high]

13. Modigliani, F. & Modigliani, L. (1997). "Risk-Adjusted Performance."
    The Journal of Portfolio Management, 23(2), 45-54.
    https://tsgperformance.com/wp-content/uploads/2020/11/modigliani-modigliani.pdf
    [high]

14. Keating, C. & Shadwick, W. F. (2002). "A Universal Performance
    Measure." The Journal of Performance Measurement, 6(3), 59-84.
    https://www.actuaries.org.uk/system/files/documents/pdf/keating.pdf
    [high]

15. Ramani, P. (2013). "Sculpting Investment Portfolios: Maximum
    Drawdown and Optimal Portfolio Strategy." CFA Institute Research and
    Policy Center.
    https://rpc.cfainstitute.org/blogs/enterprising-investor/2013/sculpting-investment-portfolios-maximum-drawdown-and-optimal-portfolio-strategy
    [high]

## See Also

- `library/portfolio-risk-management/modern-portfolio-theory.md` -- the
  mean-variance and beta frameworks from which several performance
  measures developed.
- `library/portfolio-risk-management/drawdown-analysis-and-management.md`
  -- path-dependent loss measures that complement average-return ratios.
- `library/portfolio-risk-management/volatility-targeting.md` -- how
  changing exposure can alter realized volatility, leverage, and Sharpe
  comparisons.
- `library/portfolio-risk-management/value-at-risk-risk-measurement-frameworks.md`
  -- quantile and expected-shortfall measures for risks not summarized by
  ordinary performance ratios.
