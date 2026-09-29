---
name: sequence-of-returns-risk-and-withdrawal-portfolios
id: 20260929T121312Z
tier: library-topic
domain: portfolio-risk-management
author: Librarian
tags: [sequence-of-returns-risk, retirement-decumulation, withdrawal-rates, dynamic-spending, portfolio-survival, longevity-risk, model-risk]
links: [library/portfolio-risk-management/drawdown-analysis-and-management.md, library/portfolio-risk-management/portfolio-rebalancing-strategies.md, library/portfolio-risk-management/liability-driven-investing.md, library/portfolio-risk-management/portfolio-stress-testing-and-scenario-analysis.md, library/portfolio-risk-management/behavioral-aspects-of-risk-tolerance.md, library/mathematics-statistics/monte-carlo-methods.md]
---

# Sequence Risk Makes Withdrawal Portfolios Depend on Return Order, Not Average Return Alone

Sequence-of-returns risk arises when contributions or withdrawals make otherwise identical return sets produce different wealth paths. In retirement decumulation, a large early loss can combine with continuing withdrawals to deplete capital before later gains arrive, so portfolio survival depends on the order of returns, spending policy, inflation, longevity, allocation, costs, and model assumptions rather than on average return alone [1][7].

## Background

Retirement portfolio research changed when advisers stopped asking only what stocks and bonds had earned on average and asked whether a retiree could keep withdrawing through the actual order in which returns and inflation had occurred. William Bengen's 1994 historical analysis applied rolling United States stock and intermediate-term Treasury returns to portfolios making inflation-adjusted withdrawals. Under his data, allocation, and withdrawal convention, he concluded that a first-year withdrawal equal to 4 percent of initial wealth, followed by inflation adjustments to the dollar amount, should support at least 30 years; the finding was a result from specified historical paths, not a contractual guarantee about every future market [2].

Philip Cooley, Carl Hubbard, and Daniel Walz reframed the same planning problem as a portfolio success rate. They defined success as a portfolio retaining a positive balance through a selected payout period and counted the percentage of historical periods that met that condition across withdrawal rates, horizons, and stock-bond allocations [3]. This shifted attention from one worst historical case to a distribution of past cases, but it did not remove dependence on the chosen country, sample, securities, inflation series, timing convention, or definition of failure [3][5][16].

The term "4 percent rule" can therefore conceal several decisions. In its classic form, four percent is the first year's withdrawal as a share of starting wealth; subsequent withdrawals are the same real amount, not four percent of the current balance [2][3]. The portfolio is rebalanced under a specified stock-bond policy, the planning horizon is fixed, and failure means the balance reaches zero before that horizon. Taxes, fees, guaranteed income, changing consumption, mortality, and bequest preferences may be omitted or handled separately [3][14]. Changing any of these inputs changes the question and can change the answer.

Sequence risk explains why the path matters. Andrew Clare, Simon Glover, James Seaton, Peter Smith, and Stephen Thomas separate a withdrawal portfolio's cumulative return from a sequence-risk term. The cumulative product of a set of gross returns is unchanged when the returns are reordered, but each withdrawal removes capital before some later returns can act on it. Their worked example uses three ten-year paths with the same 5 percent compound return. When a 50 percent loss arrives in year one and a 120 percent gain in year ten, the perfect withdrawal rate is 6.28 percent; reversing those two returns raises it to 22.77 percent [1]. The example is deliberately extreme, but the algebra is general.

Sequence risk also exists during accumulation, with a different vulnerable period. Contributions mean that early returns apply to relatively little accumulated capital, while returns near retirement act on a much larger balance. A severe loss shortly before retirement can therefore erase a large amount when few future contributions remain. Clare and coauthors define sequence risk around both maximum accumulation and the beginning of decumulation, while emphasizing that ordinary risk-adjusted measures such as the Sharpe ratio do not encode return order [1].

The decumulation problem adds inflation and longevity. A fixed real withdrawal rises in nominal terms with consumer prices, so high inflation can increase the cash claim while real asset returns are weak. A fixed horizon also converts an uncertain lifetime into one deterministic endpoint. If the retiree survives beyond that endpoint, a plan that was successful by its original definition can still fail economically. Research comparing phased withdrawals and life annuities therefore evaluates not only terminal wealth but also expected shortfall while alive, lifetime payouts, liquidity, and bequest value [12][13].

The evidence also broadened geographically and methodologically. Wade Pfau used 109 years of data for 17 developed markets and found that a 4 percent real withdrawal was safe under his favorable perfect-foresight design in only 4 countries; a fixed 50/50 stock-bond allocation failed at least once in all 17 [5]. Aizhan Anarkulova, Scott Cederburg, Michael O'Doherty, and Richard Sias later used returns from 38 developed countries and methods intended to reduce survivor and easy-data bias. Their published estimate for a 65-year-old couple accepting a 5 percent chance of financial ruin was 2.31 percent under the studied constant-percentage withdrawal class [6]. These results do not replace one universal number with another. They show that data selection, mortality, market survival, and the policy definition are outcome-governing assumptions.

Research on dynamic withdrawals addressed the opposite weakness of fixed real spending: a retiree may prefer some spending variation to either ruin or systematic underspending. Guyton and Klinger tested rules that freeze or reduce withdrawals after adverse paths and raise them after favorable paths. Their Monte Carlo results supported higher initial withdrawals under the tested guardrails, but the improvement came with conditional future spending rather than an unchanged real-income promise [4]. Scott, Sharpe, and Watson attacked the problem from the other side, showing that a conservative fixed rule can reserve substantial wealth for unused surpluses and can buy an inefficient spending pattern [8]. The planning problem is therefore not merely to minimize failure probability. It is to allocate uncertain wealth among current consumption, future consumption, essential floors, flexibility, and bequests.

## Core Concepts

### Cash flows make return order economically active

Let `K_(t-1)` be real portfolio wealth before period `t`, `r_t` the real portfolio return during the period, and `W_t` the real withdrawal at its end. A simple recurrence is [1]:

```text
K_t = K_(t-1) * (1 + r_t) - W_t.
```

With no contributions or withdrawals, terminal wealth is initial wealth multiplied by the product of all gross returns. Multiplication is commutative, so rearranging a fixed set of returns does not change the product. With withdrawals, each `W_t` is multiplied only by the gross returns that occur after it when the recurrence is expanded. Reordering returns therefore changes the future value of the amounts already removed and changes terminal wealth [1].

For a constant real withdrawal `W` and no terminal bequest, the maximum sustainable withdrawal can be expressed as the cumulative return term divided by a denominator containing successive products of later gross returns. Clare and coauthors call that denominator the sequence-risk term [1]. The precise indexing depends on whether withdrawals occur at the beginning or end of each period, which is why withdrawal timing must be stated. The central relation does not depend on the label used: a poor return before many future withdrawals is more damaging than the same return after most withdrawals have already been funded [1].

This mechanism is sometimes described as forced sale after a loss, but no explicit discretionary sale is required. A mutual fund can meet a scheduled withdrawal automatically; economically, units still leave the portfolio at the depressed value. Later gains compound on fewer remaining units. A subsequent return that restores an index to its prior level does not restore the retiree's account to the no-withdrawal counterfactual because capital left during the decline [1].

### Accumulation and decumulation reverse the cash-flow sign

During accumulation, contributions add units. A poor return early in a career acts on a small balance and can allow later contributions to buy more units, while a poor return near retirement acts on a large balance with little saving time left. During decumulation, withdrawals subtract units. A poor return immediately after retirement acts on a large balance and is followed by many withdrawals, while the same loss late in retirement acts after much of the planned consumption has already been funded [1].

The boundary is not the retirement date alone. A worker who stops contributing before formal retirement has already lost part of the accumulation buffer. A retiree who earns labor income or delays portfolio withdrawals retains a contribution-like offset. The author's synthesis is that exposure should be mapped to net cash flow: the vulnerable interval is when the portfolio is large, external additions are small or negative, and future required withdrawals remain substantial [1][14].

### Sequence risk is not volatility, drawdown, longevity, or LDI

Volatility measures dispersion around a mean without identifying which return occurs before a cash flow. Sequence risk measures the consequence of a realized ordering when cash enters or leaves. Greater volatility generally permits more extreme paths, but identical volatility can coexist with different serial dependence, tails, inflation regimes, and stock-bond relationships. Collins, Lam, and Stampfli show that changing the return process and its assumptions can move modeled retirement failure rates from 4 percent to 49 percent [7].

Drawdown is the decline from a prior peak and is one observable channel through which sequence risk acts. A deep early drawdown can be damaging because withdrawals continue from the reduced base. Yet drawdown alone does not specify the withdrawal amount, horizon, income floor, or recovery path. Two retirees with the same market drawdown can have different sequence exposure because one has a pension covering essentials and the other funds all consumption from the portfolio [9].

Longevity risk is the uncertainty of how long withdrawals must continue. Sequence risk concerns the path of assets and cash flows over that uncertain life. A life annuity transfers part of longevity risk through pooling and supplies income that does not require selling portfolio assets, but it can reduce liquidity and bequest flexibility and depends on contract terms and insurer performance [12][13]. The risks interact: a longer life gives a damaged portfolio more years in which it must fund consumption.

Liability-driven investing, or LDI, begins with the timing and sensitivity of obligations and builds assets around them. A bond ladder or inflation-linked asset can match selected cash flows, while an LDI program can also manage duration, inflation, currency, and collateral. Sequence risk is narrower: it is the path-dependent depletion created when volatile assets fund withdrawals. A liability-matching allocation may reduce sequence exposure for matched payments, but LDI is not synonymous with one retirement withdrawal rule [18].

### Withdrawal rules allocate risk between wealth and consumption

A fixed real rule withdraws a first-year amount and increases it with inflation. It provides stable purchasing power until the portfolio can no longer support it, concentrating adjustment in the failure state. Its advantage is planning stability; its disadvantage is that spending ignores current funded status [2][3][8].

A fixed-percentage rule withdraws a constant share of the current balance. If the percentage remains below 100 percent, the rule does not mechanically exhaust the account in one withdrawal, but consumption moves directly with markets. It transfers much of sequence risk from terminal depletion to year-to-year spending. An actuarial rule also uses current wealth but raises the fraction as remaining life or planning horizon shortens [13].

Guardrails occupy the middle. Guyton and Klinger's capital-preservation rule reduces the withdrawal by 10 percent when the current withdrawal rate rises more than 20 percent above its initial rate, while their prosperity rule permits increases after favorable outcomes; the capital-preservation rule stops during the final 15 years of the modeled horizon [4]. Their reported initial rates of 5.2 to 5.6 percent at a 99 percent confidence standard applied to portfolios with at least 65 percent equities under their simulations. Those values are evidence about that rule set, calibration, and spending flexibility, not a direct substitute for Bengen's fixed-real historical result [2][4].

Ceiling-and-floor rules limit how much spending may rise or fall in one year. Funded-ratio rules compare current assets with the present value of desired remaining spending and adjust when the ratio leaves a band. Blanchett modeled a maximum annual real change of 5 percent and found that dynamic withdrawals affected safe-rate estimates, although guaranteed income had a larger impact [9]. The common principle is feedback: adverse investment outcomes lead to some combination of lower spending, delayed increases, or reduced discretionary consumption before the portfolio reaches zero.

### Inflation, longevity, fees, and taxes change the effective cash claim

Inflation affects both sides of the recurrence. It raises nominal withdrawals needed to preserve purchasing power and changes real asset returns. A plan that assumes fixed nominal spending is not testing the same liability as a plan that raises withdrawals with consumer prices [2][3]. Inflation can also change stock-bond covariance and cause nominal bonds to lose alongside equities, so an allocation that diversified a disinflationary recession may not diversify an inflation shock.

Longevity changes the number of cash flows. A 30-year horizon is a planning convention, not a mortality guarantee. Dus, Maurer, and Mitchell compare annuities with phased withdrawal rules using expected shortfall while alive, payouts, and bequest potential; they find that one phased rule and delayed annuitization can be attractive under their German data and that results are similar in their United States case [13]. Horneff and coauthors solve a dynamic utility model and find value in combining equity exposure with longevity insurance rather than requiring complete immediate annuitization under their assumptions [12].

Fees reduce returns each period, while taxes can raise the gross withdrawal required to deliver a target after-tax amount. Cooley and coauthors' classic historical study explicitly excluded taxes and transaction costs [3]. Research comparing sustainability determinants warns that internal fund expenses and external advisory fees are often omitted and that tax effects depend on account type, basis, turnover, and how the spending target is defined [14]. A gross 4 percent withdrawal is not four percent of spendable consumption when taxes are paid from the same account.

### Allocation and rebalancing cannot remove the trade-off

More equities can raise long-run expected real return and median terminal wealth, but they also widen the distribution of early outcomes. More cash or high-quality bonds can reduce near-term price exposure, but they can lower expected real growth and remain exposed to inflation, interest-rate, and reinvestment risk. Historical safe-rate tables often show an interior allocation because too little growth and too much volatility can each shorten portfolio life under fixed withdrawals [2][3][5].

Rebalancing restores a chosen risk allocation. It can fund withdrawals from appreciated assets and buy assets that have fallen, but it can also create taxes and transaction costs. Withdrawal sourcing is part of the rule: selling winners, spending bonds first, maintaining bands, or drawing pro rata produce different paths. Research on rising equity glide paths reports that starting more conservatively and increasing equity can reduce failure in some adverse-sequence designs, but historical tests did not show the approach dominating a consistently high fixed allocation in every setting [15].

A cash buffer can prevent an immediate sale of depressed risky assets, but it is not free protection. Cash changes the total allocation and has an opportunity cost; a refill rule can later require sales; and a bucket that is economically equivalent to a rebalanced total-return portfolio cannot create a new return distribution merely through labels. Estrada compared three bucket rules with static strategies across 21 countries over 1900-2014 and found the static rebalanced strategies superior under four performance measures [10]. Pfeiffer, Salter, and Evensky found benefits for a one-year cash-flow reserve under their transaction-cost design and emphasized behavioral benefits from a known spending source [11]. The evidence supports evaluating the exact rule, not declaring either "buckets" or "total return" universally superior.

### Historical and stochastic models answer conditional questions

A historical rolling-window test preserves realized returns, inflation, and cross-asset comovement. It is transparent and auditable, but overlapping windows are statistically dependent, one observed history cannot contain every future regime, and a surviving country's record may contain favorable selection [5][6][16]. A result that never failed historically means no failure occurred in the tested windows; it does not estimate a literal zero probability.

Bootstrap simulation resamples historical observations to create more paths. Simple one-period resampling preserves the empirical marginal distribution but breaks serial dependence and regimes. Block methods preserve more local order but require a block-length decision. Cooley, Hubbard, and Walz compare Monte Carlo and overlapping-period success rates and find that results can differ substantially; similarity requires treatment of mean reversion and serial correlation consistent with the historical process [16].

Parametric Monte Carlo draws from a modeled distribution and can incorporate mortality, inflation, fees, taxes, changing allocations, and decision rules. Its apparent precision is conditional on expected returns, volatility, correlation, tails, serial dependence, and regime behavior. Collins, Lam, and Stampfli show that common retirement models with different assumptions can produce sharply different sustainability results and warn that an oversimplified model can distort risk [7]. A simulation count measures numerical sampling from the model, not confidence that the model represents reality.

### Failure probability is not a sufficient welfare measure

A binary success rate gives the same label to a one-dollar balance at the horizon and a large surplus. It also gives the same failure label to a small final-year shortfall and severe early depletion. Expected shortfall incorporates both probability and magnitude, and mortality adjustment weights shortfalls by the chance the retiree is alive to experience them [13]. Consumption volatility, the probability and depth of spending cuts, time of first shortfall, terminal wealth, and bequest outcomes answer additional questions.

A high success target can also cause avoidable underspending. Scott, Sharpe, and Watson estimate that a typical 4 percent rule can allocate 10 to 20 percent of initial wealth to surpluses and another 2 to 4 percent to overpayments for its spending policy under their financial-economics framework [8]. Their finding does not prove that every retiree should spend more; bequests and precautionary wealth can be deliberate goals. It establishes that "money left" is not automatically wasted and that "never depleted" is not automatically optimal. The objective must state how current consumption, future consumption, flexibility, and legacy are valued.

## Evidence

### Historical United States studies established the problem, not a universal constant

Bengen simulated rolling retirement starts using United States stock, intermediate-term Treasury, and inflation histories. His central case withdrew a percentage of initial wealth in year one and raised the dollar amount with inflation thereafter. He found that 4 percent survived at least 30 years in the historical cases he examined and recommended substantial stock exposure within the tested two-asset framework [2]. The method's strength is path realism: the poor equity returns and high inflation around 1973-1974 remain joined rather than being averaged away.

Cooley, Hubbard, and Walz used 1926-1995 United States returns, withdrawal rates from 3 to 12 percent, horizons from 15 to 30 years, and several stock-bond mixes. They defined success as a positive terminal balance and tabulated the fraction of historical payout periods that succeeded [3]. Their study shows that a withdrawal rate cannot be evaluated without horizon, allocation, inflation treatment, and risk tolerance. It also states that taxes and transaction costs were excluded, limiting direct translation to net household spending [3].

These studies are often summarized as proof of a constant. Their actual evidence is conditional. Bengen's worst-case approach and Cooley's success-rate approach answer different risk questions. Cooley and coauthors' later comparison of overlapping historical periods with Monte Carlo simulation found that the two procedures can be close under some conditions and far apart under others, especially when the stochastic method does not reproduce temporal features of returns [16].

### Sequence algebra isolates the effect of order

Clare and coauthors develop a perfect withdrawal rate that exhausts a portfolio at the end of a fixed period under known returns. They decompose it into an order-invariant cumulative return term and an order-sensitive denominator [1]. In their ten-year example, every path compounds at 5 percent. Moving a 50 percent loss from the first year to the final year while moving a 120 percent gain in the opposite direction changes the perfect withdrawal rate from 6.28 percent to 22.77 percent [1].

The example controls for the return set, so the outcome difference cannot be attributed to a different arithmetic or compound mean. It demonstrates the mechanism more cleanly than a comparison of unrelated historical retirements. The authors then use 1926-2018 real United States stock and bond data and 20,000 resampled paths for each allocation to compare perfect-withdrawal distributions and proposed sequence-risk measures [1]. The model remains conditional on its sample and resampling method, but the algebraic decomposition is not sample-specific.

### Flexible spending buys resilience with variable consumption

Guyton and Klinger apply Monte Carlo analysis calibrated to 1973-2004 and 1928-2004 data, test 50, 65, and 80 percent equity allocations, and assess 40-year horizons. Their capital-preservation and prosperity rules create spending guardrails around the initial withdrawal rate [4]. They report sustainable initial rates of 5.2 to 5.6 percent at their 99 percent confidence standard for portfolios with at least 65 percent equities, with lower maximum rates for 50 percent equity [4].

The method does not show that a fixed 5.6 percent real withdrawal is as safe as a fixed 4 percent withdrawal. It shows that conditional reductions and freezes can support a higher starting amount under the simulated policy. The trade-off is visible in their own design: capital preservation rescues the portfolio by reducing purchasing power, and the rule is discontinued in the final 15 years because continued cuts provided little corresponding success improvement [4].

Blanchett uses a utility-informed framework with nondiscretionary spending, guaranteed income, projected returns, and dynamic withdrawals. Among the variables tested, guaranteed income had the largest effect on estimated safe initial withdrawal rates, moving them by more than four percentage points between the studied low- and high-guarantee cases; dynamic spending also mattered [9]. The result supports evaluating portfolio failure through its consumption consequence. A depleted account is not the same welfare event when essential income is already secured.

### International data and model choice weaken certainty

Pfau's historical simulations use 1900-2008 asset and inflation data for 17 developed countries and retirement starts ending in 1979 to permit 30-year outcomes. Even with perfect foresight used to choose each country's fixed allocation for each retirement, a 4 percent real withdrawal was safe in only 4 countries; a fixed 50/50 allocation failed at least once in every country [5]. The favorable assumption makes the negative result more, not less, informative about the limits of a United States-only rule.

Anarkulova, Cederburg, O'Doherty, and Sias use a broader 38-country asset-class dataset and explicitly address survivor and easy-data biases. In the peer-reviewed 2025 article, their studied policy yields a 2.31 percent rate for a 65-year-old couple accepting a 5 percent ruin probability [6]. Their number differs from Pfau's and classic United States studies because the data, spending rule, mortality, and statistical method differ. The evidence supports assumption disclosure and international stress testing rather than adoption of 2.31 percent as another universal constant.

Collins, Lam, and Stampfli compare historical backtests, bootstrap methods, simple normal or lognormal Monte Carlo models, non-normal simulations, vector autoregressions, and regime-switching models. Across the models they examine, estimated failure ranges from 4 percent to 49 percent [7]. The spread is direct evidence of model risk: adding simulation paths cannot compensate for an implausible return distribution, correlation matrix, inflation process, or regime assumption.

### Buckets and annuities solve different parts of the problem

Estrada tests three bucket rules and eleven static strategies across 21 countries for 1900-2014 using a 30-year retirement and inflation-adjusted withdrawals. Static rebalanced strategies outperform the tested buckets across failure and shortfall measures [10]. His explanation is mechanical: buckets may avoid selling risky assets after a loss but, without symmetric rebalancing, can also fail to buy them when cheap. The result applies to the specified bucket rules, not to every cash reserve or liability-matching plan.

Pfeiffer, Salter, and Evensky compare reverse dollar-cost averaging with a one-year cash-flow reserve. They report transaction-cost and survival benefits under their refill design and describe the behavioral value of knowing the next year's spending source [11]. Read together with Estrada, the evidence separates three claims: cash can fund near-term payments, a reserve can change trading costs and behavior, and the word "bucket" does not by itself improve return economics.

Horneff and coauthors solve a dynamic retirement model in which a retiree chooses financial assets and variable payout annuities. Their retiree benefits from equity exposure and longevity insurance, does not fully annuitize immediately under the modeled conditions, and often obtains much of the modeled welfare benefit from a simpler 60/40 variable annuity [12]. Dus, Maurer, and Mitchell compare phased withdrawals with life annuities using German data and expected shortfall; they find an attractive phased rule and potential benefits from delayed annuitization, with similar United States results [13]. Both studies show that guaranteed lifetime income, liquid portfolio wealth, and bequests are joint design variables rather than isolated products.

## Implications

### For retirees: define the spending liability before selecting a rate

The first decision is not a withdrawal percentage. It is a spending map that separates essential from discretionary consumption, identifies inflation linkage, records guaranteed income, and states the intended planning horizon and bequest floor. Blanchett's evidence shows why: the same portfolio balance has a different safe-rate implication when guaranteed income covers most essential spending than when the portfolio is the only income source [9].

A practical map can divide annual spending into an essential floor, flexible lifestyle spending, and one-time contingencies. Social Security, pensions, or annuity income can be assigned to the floor only to the extent their indexation, survivor terms, and credit protections match the liability. The liquid portfolio then funds the residual. This does not eliminate sequence risk; it limits the consumption damage if the risky account experiences a bad early path [9][12][13].

The retiree should also state what adjustment is acceptable. A fixed real rule prioritizes stable consumption. A percentage rule prioritizes account continuity. Guardrails exchange some stability for a higher initial amount. No rule dominates without a preference over cuts, surplus, and bequest [4][8]. A plan that assumes discretionary spending is flexible should specify the amount, trigger, duration, and restoration rule rather than describe flexibility only after failure.

### For portfolio design: manage the vulnerable path, not one average

Allocation should be tested against at least four adverse mechanisms: an immediate equity loss, persistent low real returns, an inflation shock that lowers stocks and nominal bonds together, and a rapid recovery after defensive assets were increased. Each scenario should include withdrawals, rebalancing, taxes, fees, and available guaranteed income. The point is not to predict which regime will occur; it is to identify whether one plausible sequence forces an unacceptable spending cut or sale [5][7].

A near-term reserve is defensible when it matches a real cash need, improves behavior, or reduces costly trading. It should be counted as part of total allocation and evaluated with its refill rule. If the reserve is continually restored by selling risky assets after losses, it may postpone rather than remove the sale. If it is never restored, the portfolio follows a rising-risk glide path as safe assets are spent. The reserve's value must therefore be attributed to liquidity, behavior, or an intentional allocation path, not to the bucket label [10][11].

Rebalancing should be integrated with withdrawals. Contributions from pensions or other income, dividends, interest, and sales of overweight assets can fund spending before pro rata sales. Bands can reduce unnecessary turnover, while taxable accounts require basis and tax-lot analysis. The correct test is after-tax household cash and total-portfolio risk; a gross model that ignores fees and taxes can overstate spendable support [3][14].

### For dynamic spending: write decision rules before stress

A guardrail policy should state the reference withdrawal rate, upper and lower triggers, size of cuts and raises, inflation rule, remaining-horizon treatment, and which expenses can change. Guyton and Klinger show that the benefit arises because spending responds before depletion; removing the cuts while keeping the higher initial rate removes the mechanism [4].

Funded-ratio monitoring offers a more direct alternative. At each review, calculate current investable assets divided by the present value of desired remaining portfolio withdrawals under stated real-return and longevity assumptions. A deteriorating ratio can trigger a smaller inflation increase, a discretionary cut, delayed spending, or a review of allocation. An improving ratio can permit a raise or bequest transfer. The author's synthesis is that a range is preferable to exact annual optimization because return and mortality estimates are uncertain [7][9].

Rules should not react to every monthly move. Horan's Monte Carlo and historical tests find that dividing an otherwise equivalent withdrawal into more frequent intervals does not itself improve sustainability [17]. The material controls are the total cash claim, policy response, allocation, and path, not whether the same annual amount is mechanically split into twelve pieces.

### For modelers: treat every probability as a model output

A defensible analysis should preserve a model ledger containing the return source, period, country universe, inflation process, taxes, fees, mortality, withdrawal timing, rebalancing, correlation, tail behavior, and regime assumptions. It should distinguish historical windows, bootstrap paths, and parametric simulation rather than presenting them as interchangeable estimates [7][16].

At least three model families should be compared. Historical replay shows how the current plan handles observed joint paths. A block or regime-aware bootstrap recombines history while preserving more dependence than independent one-year draws. A forward-looking simulation tests current expected returns and alternative inflation and correlation regimes. If conclusions change materially, the disagreement is not noise to be averaged away; it identifies the assumption that controls the plan [5][7].

Model output should include more than success probability. Report the distribution of real consumption, frequency and depth of cuts, year of first shortfall, mortality-adjusted expected shortfall, terminal wealth, and bequest attainment. A binary failure rate can encourage both false safety and excessive underspending [8][13]. Sensitivity should cover lower expected returns, higher inflation, longer life, higher costs, and an early joint stock-bond loss.

Backtests must use information available at each decision date. A glide path, valuation overlay, or spending trigger tuned with the full sample has access to outcomes the retiree did not know. Kitces and Pfau's historical analysis shows that rising glide paths can protect some overvalued starting environments but did not dominate a high fixed equity allocation across every test [15]. The correct claim is conditional on the starting valuation, fixed-income choice, rule, and sample.

### For advisers and committees: govern the trade-off explicitly

Advice should distinguish a planning rate from a promise. The written policy should say whether withdrawals are gross or net of tax, whether fees are removed before return, whether inflation adjustments can be skipped, and what constitutes failure. A household that regards a 10 percent lifestyle cut as acceptable has a different plan from one whose entire withdrawal is essential, even if both begin at four percent [4][9][14].

The worst operational failure is an aggressive starting withdrawal supported by an unstated assumption that the retiree will cut later. Prevention requires consent before implementation: show the dollar cut under the guardrail, the historical or simulated frequency of such cuts, and the minimum essential-income floor. A rule the retiree will abandon during stress is not a risk control [4][9].

The committee should review the plan after material changes in wealth, spending, guaranteed income, tax law, health, household composition, or market assumptions. Review does not mean changing the model until it approves current spending. It means applying the same documented rule to new facts, retaining prior assumptions and outcomes for comparison, and recording why a policy change was made [7][9].

### A decision framework

A repeatable sequence-risk review can use eight steps, synthesized from the cited research [2][4][5][7][9][13]:

1. Define essential, flexible, and bequest objectives in real after-tax terms [9][13].
2. Map guaranteed income, liquid assets, account taxes, fees, and withdrawal restrictions [9][12][14].
3. Select a spending rule and state its timing, inflation, cut, raise, and horizon conventions [2][4].
4. Choose an allocation and rebalancing or glide-path rule; classify any cash bucket as part of total allocation [10][11][15].
5. Test historical, resampled, and forward-looking paths, including non-U.S. and adverse inflation regimes [5][6][7].
6. Report consumption and shortfall distributions as well as terminal success [8][13].
7. Identify the earliest observable warning and the pre-committed response [4][9].
8. Recalculate after material changes without erasing unfavorable prior evidence [7].

The author's synthesis is that sequence risk cannot be abolished while volatile assets fund withdrawals. It can be allocated. Lower withdrawals allocate more uncertainty to present consumption; flexible rules allocate it across future consumption; safer assets allocate it to lower expected growth and inflation exposure; annuities allocate longevity risk to an insurer and surrender liquidity; and cash reserves allocate capital to near-term certainty with opportunity cost [4][9][10][12][13]. The sound plan makes that allocation explicit and survivable rather than hiding it behind one average return or one success percentage.

## Sources

1. Clare, A., Glover, S., Seaton, J., Smith, P. N. & Thomas, S. (2020).
   "Measuring Sequence Returns Risk." Journal of Retirement, 8(1), 65-79.
   https://doi.org/10.3905/jor.2020.1.066 [high]

2. Bengen, W. P. (1994). "Determining Withdrawal Rates Using Historical
   Data." Journal of Financial Planning, 7(4), 171-180.
   https://www.financialplanningassociation.org/sites/default/files/2020-05/7%20Determining%20Withdrawal%20Rates%20Using%20Historical%20Data.pdf [high]

3. Cooley, P. L., Hubbard, C. M. & Walz, D. T. (1998). "Retirement
   Savings: Choosing a Withdrawal Rate That Is Sustainable." AAII Journal,
   20(2), 16-21.
   https://www.aaii.com/files/pdf/6794_retirement-savings-choosing-a-withdrawal-rate-that-is-sustainable.pdf [high]

4. Guyton, J. T. & Klinger, W. J. (2006). "Decision Rules and Maximum
   Initial Withdrawal Rates." Journal of Financial Planning, 19(3), 49-57.
   https://www.financialplanningassociation.org/article/journal/MAR06-decision-rules-and-maximum-initial-withdrawal-rates [high]

5. Pfau, W. D. (2010). "An International Perspective on Safe Withdrawal
   Rates: The Demise of the 4 Percent Rule?" Journal of Financial Planning,
   23(12), 52-61.
   https://www.financialplanningassociation.org/article/journal/DEC10-international-perspective-safe-withdrawal-rates-demise-4-percent-rule [high]

6. Anarkulova, A., Cederburg, S., O'Doherty, M. S. & Sias, R. W. (2025).
   "The Safe Withdrawal Rate: Evidence from a Broad Sample of Developed
   Markets." Journal of Pension Economics and Finance, 24(3), 464-500.
   https://doi.org/10.1017/S1474747225000010 [high]

7. Collins, P. J., Lam, H. & Stampfli, J. (2015). "How Risky Is Your
   Retirement Income Risk Model?" Financial Services Review, 24(3),
   193-216. https://doi.org/10.61190/fsr.v24i3.3335 [high]

8. Scott, J. S., Sharpe, W. F. & Watson, J. G. (2009). "The 4% Rule - At
   What Price?" Journal of Investment Management, 7(3), 31-48.
   https://www.gsb.stanford.edu/faculty-research/publications/4-percent-rule-what-price [high]

9. Blanchett, D. M. (2017). "The Impact of Guaranteed Income and Dynamic
   Withdrawals on Safe Initial Withdrawal Rates." Journal of Financial
   Planning, 30(4), 42-52.
   https://www.financialplanningassociation.org/article/journal/APR17-impact-guaranteed-income-and-dynamic-withdrawals-safe-initial-withdrawal-rates [high]

10. Estrada, J. (2019). "The Bucket Approach for Retirement: A Suboptimal
    Behavioral Trick?" Journal of Investing, 28(5), 54-68.
    https://doi.org/10.3905/joi.2019.1.093 [high]

11. Pfeiffer, S., Salter, J. & Evensky, H. (2013). "The Benefits of a Cash
    Reserve Strategy in Retirement Distribution Planning." Journal of
    Financial Planning, 26(9), 49-55.
    https://www.financialplanningassociation.org/article/journal/SEP13-benefits-cash-reserve-strategy-retirement-distribution-planning [high]

12. Horneff, W. J., Maurer, R. H., Mitchell, O. S. & Stamos, M. Z. (2007).
    "Money in Motion: Dynamic Portfolio Choice in Retirement." NBER
    Working Paper 12942. https://doi.org/10.3386/w12942 [high]

13. Dus, I., Maurer, R. & Mitchell, O. S. (2005). "Betting on Death and
    Capital Markets in Retirement: A Shortfall Risk Analysis of Life
    Annuities versus Phased Withdrawal Plans." Financial Services Review,
    14(3), 169-196. https://doi.org/10.3386/w11271 [high]

14. DeJong, J. C., Jr. & Robinson, J. H. (2017). "Determinants of
    Retirement Portfolio Sustainability and Their Relative Impacts."
    Journal of Financial Planning, 30(4), 54-62.
    https://www.financialplanningassociation.org/article/journal/APR17-determinants-retirement-portfolio-sustainability-and-their-relative-impacts [high]

15. Kitces, M. E. & Pfau, W. D. (2015). "Retirement Risk, Rising Equity
    Glide Paths, and Valuation-Based Asset Allocation." Journal of
    Financial Planning, 28(3), 38-48.
    https://www.financialplanningassociation.org/article/journal/MAR15-retirement-risk-rising-equity-glide-paths-and-valuation-based-asset [high]

16. Cooley, P. L., Hubbard, C. M. & Walz, D. T. (2003). "A Comparative
    Analysis of Retirement Portfolio Success Rates: Simulation versus
    Overlapping Periods." Financial Services Review, 12(2), 115-128.
    https://doi.org/10.61190/fsr.v12i2.4759 [high]

17. Horan, S. M. (2024). "Optimal Withdrawal Frequency for Sustainable
    Retirement Withdrawals." Financial Planning Review, 7(2), e1183.
    https://doi.org/10.1002/cfp2.1183 [high]

18. Society of Actuaries. (2019). "Liability-Driven Investment - Benchmark
    Model."
    https://www.soa.org/globalassets/assets/files/resources/research-report/2019/liability-driven-investment.pdf [high]

## See Also

- `library/portfolio-risk-management/drawdown-analysis-and-management.md` -- peak-to-trough loss, recovery arithmetic, and drawdown control.
- `library/portfolio-risk-management/portfolio-rebalancing-strategies.md` -- maintaining allocation while controlling taxes, turnover, and behavior.
- `library/portfolio-risk-management/liability-driven-investing.md` -- matching assets to the timing and sensitivity of obligations.
- `library/portfolio-risk-management/portfolio-stress-testing-and-scenario-analysis.md` -- testing joint market, inflation, liquidity, and cash-flow paths.
- `library/portfolio-risk-management/behavioral-aspects-of-risk-tolerance.md` -- whether the investor can execute a policy through loss and recovery.
- `library/mathematics-statistics/monte-carlo-methods.md` -- simulation design, uncertainty, and model validation.
