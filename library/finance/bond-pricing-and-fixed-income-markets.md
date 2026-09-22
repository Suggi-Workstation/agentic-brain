---
name: bond-pricing-and-fixed-income-markets
id: 20260726T181601Z
tier: library-topic
domain: finance
author: Researcher-1
tags: [bond-pricing, fixed-income, duration, convexity, yield-to-maturity, credit-ratings, credit-spreads]
links: [library/finance/anchor-finance.md, library/macro-micro/monetary-policy-and-central-banking.md, library/finance/financial-statement-analysis.md]
reviewed: 2026-09-22
---

# Bond Pricing and Fixed Income Markets -- Cash-Flow Timing, Rates, Credit, and Liquidity Jointly Determine Value

A bond is a contract for future cash flows, but its market value is not fixed by the contract alone. Price changes as discount rates, expected payment amounts, embedded options, and trading conditions change, so sound fixed income analysis must separate interest-rate risk, credit risk, liquidity risk, and reinvestment risk rather than treating yield as a complete return forecast. This framework applies at enormous scale: SIFMA reported $160.7 trillion of global fixed income debt outstanding at year-end 2025 ([1]).

## Background

Debt securities connect borrowers that need capital with investors willing to exchange money today for promised payments later. Governments issue bills, notes, and bonds to finance public operations; companies issue bonds to fund assets, acquisitions, and working capital; and financial institutions create securities backed by loans or other receivables. A conventional fixed-rate bond specifies a principal amount, a coupon schedule, and a maturity date. Treasury notes and bonds, for example, pay interest every six months and repay face value at maturity, while Treasury bills are issued at par or a discount and pay face value when they mature ([2]). Those contractual differences create different cash-flow patterns, but all can be analyzed by discounting future payments.

The basic present-value logic long predates modern electronic markets. What developed during the twentieth century was a more systematic language for comparing instruments whose coupons and maturities differed. Frederick Macaulay's 1938 NBER study organized a large historical record of interest rates, bond yields, and stock prices and gave fixed income analysis the duration concept now bearing his name ([9]). Later work distinguished Macaulay duration, modified duration, effective duration, key-rate duration, and convexity. These measures do not replace full valuation. They compress a bond's response to specified rate changes into useful approximations and make exposures comparable across securities and portfolios ([5] [6] [7] [8]).

Market institutions developed alongside the mathematics. Credit ratings provide standardized opinions about an issuer's or instrument's creditworthiness, while market prices and spreads continuously incorporate investors' required compensation. Regulation once embedded rating categories directly into many rules. Section 939A of the Dodd-Frank Act required federal agencies to remove references to credit ratings and substitute other standards of creditworthiness; the SEC's 2023 Regulation M amendments are one implementation of that mandate ([14]). The change did not make ratings irrelevant. It clarified that a rating is one input to analysis rather than a substitute for independent assessment of default, liquidity, market-value, and option risk.

Trading transparency also changed materially. Most bonds trade over the counter rather than on a centralized stock exchange. FINRA introduced the Trade Reporting and Compliance Engine, or TRACE, in July 2002 for eligible corporate-bond transactions and later expanded reporting to agency debt, securitized products, and Treasury securities. TRACE publishes price, yield, volume, and execution-time information for eligible instruments, reducing the information gap between dealers and customers without turning every bond into an exchange-traded security ([16]). Price discovery therefore depends on both valuation models and observable transactions.

The size of the market makes these distinctions consequential. SIFMA's 2026 Fact Book reported that global fixed income debt outstanding rose 10.6 percent to $160.7 trillion in 2025, slightly above the reported $157.8 trillion capitalization of global equity markets. It also reported $29.9 trillion of global long-term fixed income issuance and $11.5 trillion of U.S. long-term fixed income issuance during 2025 ([1]). These totals combine instruments with very different sovereign, corporate, mortgage, municipal, inflation, currency, and option exposures. Calling all of them "bonds" identifies a legal form, not a common risk profile.

Benchmark securities organize comparison but do not eliminate analytical choices. U.S. Treasuries provide observable maturity-specific yields and are commonly used as reference rates, while a corporate bond adds issuer and security risks and may trade with different liquidity. Even Treasury instruments vary: bills, nominal notes and bonds, floating-rate notes, and inflation-protected securities promise different cash-flow patterns ([2]). The benchmark must therefore match the timing, currency, and rate structure of the cash flow being valued.

Fixed income analysis therefore evolved around four linked questions. First, what cash flows can occur and when? Second, which discount curve is appropriate for those cash flows? Third, what probability and severity of nonpayment, prepayment, or early redemption should be assigned? Fourth, how much compensation is required for risks that remain, including illiquidity and uncertainty? Price is the output of those assumptions. Yield, duration, convexity, spread, and rating are summaries of different parts of the same valuation problem, not interchangeable answers ([4] [6] [7] [18]).

## Core Concepts

### Present Value and the Discount Curve

For a fixed-rate, option-free bond with coupon cash flow C, face value F, and n payment periods, the simplest price representation is ([2] [8]):

Price = Sum from t = 1 to n of C / (1 + r_t)^t, plus F / (1 + r_n)^n

Each r_t is the discount rate appropriate to the timing and risk of that cash flow. A simplified textbook calculation often uses one yield for every period. A more precise valuation uses spot rates from a benchmark zero-coupon curve and then adds any required credit, liquidity, tax, or option adjustments. The distinction matters because the yield curve is rarely flat. Two bonds with the same maturity can also deserve different discount rates if their payment priority, call provisions, currencies, or liquidity differ ([2] [4] [18]).

The inverse relation between price and yield follows directly from discounting. Raising the discount rate reduces the present value of each fixed payment; lowering it increases present value. TreasuryDirect states the auction relationship explicitly: when a note's or bond's yield to maturity exceeds its coupon rate, price is below par; when yield equals the coupon rate, price is at par; and when yield is below the coupon rate, price is above par ([2]). The SEC gives the same economic result for secondary-market fixed-rate bonds: higher market rates make older low-coupon bonds less competitive and push their prices down, while lower rates make their coupons more valuable and push prices up ([3]).

The yield curve adds a maturity dimension because cash flows due at different dates can respond differently to changing rates. Curve shifts need not be parallel. The IMF notes that duration is only an approximation because movements in the term structure are usually not parallel, while CFA Institute identifies the parallel-shift assumption as a limitation of common portfolio duration and convexity calculations. A single uniform yield shock is therefore a useful scenario, not a complete model of curve risk ([7] [8]).

### Coupon, Current Yield, Yield to Maturity, and Realized Return

The coupon rate is set against face value and determines contractual coupon payments. Current yield divides annual coupon income by the current market price. Yield to maturity, or YTM, is the single discount rate that makes the present value of promised coupons and principal equal the observed price. These measures answer different questions. Coupon identifies promised cash income relative to par; current yield relates annual coupon income to today's price; and YTM summarizes price, coupons, and the maturity payment under a set of assumptions ([4]).

YTM is not a guarantee of realized return. FINRA notes that it assumes promised principal and coupon payments occur on time, generally assumes coupons can be reinvested at the computed rate, and excludes taxes and brokerage costs. Because reinvestment rates change, YTM and yield to call are estimates rather than ex post total returns ([4]). A sale before maturity introduces a market price that may be above or below the purchase price. A default changes the cash flows. A call can terminate coupons early. Inflation changes purchasing power. The analyst should therefore describe YTM as a standardized internal rate of return on promised cash flows, not as a forecast that absorbs every risk.

Callable bonds require additional measures. Yield to call uses a call date and call price instead of final maturity. Yield to worst compares modeled redemption outcomes and reports the lowest applicable yield under the stated assumptions. FINRA explains that issuers often exercise calls when rates fall because refinancing becomes cheaper; the investor then loses the above-market coupon and must reinvest at lower rates ([4] [19]). That asymmetry means an apparently attractive coupon can partly compensate for an option owned by the issuer.

Holding-period return is a better framework when the investment horizon differs from maturity. It combines coupon income, reinvestment income, and the sale or terminal price over the selected horizon. Price risk and reinvestment risk move in opposite directions: rising rates reduce a fixed-rate bond's immediate market value but permit coupons and principal to be reinvested at higher yields; falling rates raise price but reduce reinvestment income. Matching the investment horizon to Macaulay duration can balance these effects under restrictive assumptions, but changes in credit spreads, curve shape, or cash flows can still alter the result ([6]).

### Duration as First-Order Rate Sensitivity

Macaulay duration is the present-value-weighted average time at which an option-free bond's cash flows are received. A zero-coupon bond has one payment, so its Macaulay duration equals its maturity. A coupon bond returns some value earlier and therefore has a Macaulay duration shorter than final maturity. Modified duration converts the timing measure into an approximate price sensitivity to a change in YTM. CFA Institute describes modified duration as the first derivative, or slope, of bond price with respect to YTM ([6] [8]).

For a small change in yield, the first-order approximation is:

Percentage price change approximately equals -Modified Duration times Change in Yield

If modified duration is 6 and yield rises 1 percentage point, the approximation is a 6 percent price decline. FINRA presents the same rule of thumb and emphasizes that longer maturity and lower coupon generally raise duration ([5]). The negative sign represents the inverse price-yield relation. Duration is stated in years but, when used as modified duration, its practical interpretation is percentage price sensitivity per unit change in yield.

Duration depends on the instrument and the model. Longer maturity, lower coupon, and lower starting yield generally increase duration for an otherwise comparable fixed-rate bond. Duration falls as a bond approaches maturity. Money duration scales modified duration by market value, while price value of a basis point estimates the currency change for a one-basis-point move. Portfolio duration can aggregate security-level exposures, but the result remains conditional on the assumed rate movement ([6]).

Effective duration is more appropriate when interest-rate changes can alter cash flows. A callable bond may be redeemed when rates fall, and mortgage borrowers may prepay. Instead of holding cash flows fixed, effective duration reprices the instrument after upward and downward shifts in a benchmark curve while allowing the option model to change expected cash flows. Key-rate duration measures sensitivity to a benchmark-yield change at a specific maturity. These tools address different failures of a single modified-duration number: option-dependent cash flows and nonparallel curve shifts ([20]).

Duration is local, not universal. It is most accurate for small changes around the starting curve and for securities whose cash flows stay fixed. It does not by itself measure default, spread, liquidity, inflation, or currency risk. A short-duration speculative bond can have much more loss risk than a long-duration Treasury. FINRA therefore warns that low duration does not mean low total risk ([5]).

### Convexity as the Second-Order Correction

The true price-yield relation of an option-free fixed-rate bond is curved. Convexity measures the second-order effect that duration omits. A common approximation is ([7] [8]):

Percentage price change approximately equals
-Modified Duration times Change in Yield
+ 0.5 times Convexity times Change in Yield squared

For a bond with modified duration 6 and convexity 40, a 1 percentage point rise in yield gives a duration estimate of -6.0 percent and a convexity adjustment of +0.2 percent, for an estimated change of -5.8 percent. The same convexity term is positive for a 1 percentage point fall, making the estimated gain 6.2 percent. The arithmetic illustrates why an option-free bond's gain from a given yield decline is larger than its loss from an equal yield increase, all else equal ([7] [8]).

CFA Institute states that convexity is positive for an option-free fixed-rate bond and becomes more important for larger yield moves and longer maturities. Higher convexity improves the local price estimate but is not free: investors normally pay a higher price, accept a lower yield, or give up something else for a more favorable price response. Convexity calculations also inherit assumptions about curve movement and cash flows ([7]).

Embedded options can reverse the simple result. As rates fall, a callable bond's probability of redemption rises, limiting price appreciation. Mortgage-backed securities can experience faster prepayment, returning principal when reinvestment opportunities are less attractive. Effective convexity can therefore become low or negative in relevant rate ranges. The correct analysis prices the option and models changing cash flows rather than applying option-free duration and convexity mechanically ([7] [19]).

### Credit Spreads, Expected Loss, and Risk Premia

A corporate bond is commonly compared with a government or swap benchmark of similar maturity. The yield difference is a spread, but it is not a pure estimate of default probability. It can include expected default loss, compensation for uncertainty about that loss, liquidity, tax effects, option risk, and supply-demand conditions. The BIS documented a historical "credit spread puzzle": for one sample of three-to-five-year BBB bonds, an average spread of about 170 basis points compared with average annual default loss of about 20 basis points, indicating that other components materially affected spreads ([18]).

A simple expected-loss approximation multiplies probability of default by loss given default. Loss given default equals one minus recovery rate. If annual default probability is 2 percent and expected recovery is 40 percent, expected loss is 2 percent times 60 percent, or 1.2 percent. This estimate is an average expectation, not a complete required spread. Defaults cluster, recovery varies with seniority and the economic cycle, and losses are negatively skewed. Investors may require compensation for systematic and hard-to-diversify credit risk beyond the arithmetic expected loss ([12] [18]).

Option-adjusted spread, or OAS, attempts to compare a bond with a benchmark curve after accounting for embedded options. FRED describes the ICE BofA U.S. Corporate Index OAS as the market-capitalization-weighted spread between constituent option-adjusted spreads and a spot Treasury curve for investment-grade U.S. dollar corporate debt ([13]). OAS is model-dependent because option valuation requires assumptions about rate paths, volatility, and borrower or issuer behavior. It is more informative than a nominal spread for option-bearing bonds, but it is not model-free truth.

Credit ratings organize ordinal credit opinions. S&P identifies BBB- and above as investment grade and BB+ and below as speculative grade, while Moody's identifies Baa3 as its lowest investment-grade rating and Ba1 as its highest speculative-grade rating. Moody's also states that lower-rated entities and obligations default at higher average frequencies than more highly rated ones, but that a rating is an opinion rather than a guarantee against default. A rating should therefore inform default analysis while market spreads, covenants, seniority, collateral, and issuer fundamentals complete the assessment ([12] [21]).

### Liquidity, Market Structure, and Observed Prices

A model value assumes the investor can transact at or near that value. Actual bonds may trade infrequently, with limited dealer inventory and meaningful bid-ask spreads. Liquidity risk is the possibility that a position cannot be bought or sold promptly in the desired size without a material price concession. Because many bonds trade over the counter, the last transaction may not represent an executable price for a different trade size or time ([8]).

TRACE improves evidence by publishing transaction price, yield, volume, and time data for eligible securities. FINRA says that this information helps investors compare execution quality and helps regulators monitor pricing and market conduct ([16]). Transparency does not eliminate liquidity risk. It allows analysts to observe it more directly through trade frequency, dispersion, size, and price impact.

Liquidity can deteriorate even in markets normally treated as safe. In March 2020, Federal Reserve researchers documented wider Treasury bid-ask spreads, lower market depth, greater price impact, heavy client selling, and constrained dealer intermediation. The episode shows that credit safety and trading liquidity are separate properties. A Treasury can have negligible expected credit loss while still experiencing impaired market functioning under exceptional demand for cash ([11]).

## Evidence and Empirical Foundation

### Market Scale and Financing Function

SIFMA's 2026 Capital Markets Fact Book provides a current measure of scale. It reported $160.7 trillion of global fixed income debt outstanding at year-end 2025, up 10.6 percent from the prior year, and $29.9 trillion of global long-term fixed income issuance during 2025. U.S. long-term fixed income issuance was $11.5 trillion, including $4.8 trillion of long-term Treasury issuance, $2.2 trillion of corporate bonds, $1.9 trillion of mortgage-backed securities, $587.3 billion of municipal bonds, and $517.4 billion of asset-backed securities ([1]). The categories demonstrate that fixed income is not a homogeneous asset class: public funding, corporate financing, housing credit, local-government borrowing, and securitized receivables coexist under one label.

The evidence supports two conclusions within this topic's scope. First, small changes in required yields can revalue very large pools of assets and liabilities. Second, different sectors transmit rate and credit changes through different cash-flow rules. A fixed-rate Treasury transfers duration risk to the holder; a floating-rate instrument resets coupons; TIPS adjust principal with inflation and deflation; and a mortgage-backed security's duration changes as refinancing and payoff incentives change. The BIS describes the broader transfer explicitly: longer-maturity bonds reduce refinancing risk for issuers but increase creditors' duration exposure, and mark-to-market losses can induce selling or hedging that pushes prices lower ([2] [8] [10] [17]).

### A Measured Duration Case: The Federal Reserve Portfolio

The Federal Reserve's SOMA portfolio supplies a documented application of duration. Board staff reported that the par-weighted average duration of SOMA securities rose from 4.7 years in March 2020 to 5.8 years in December 2021. They interpreted 5.8 duration as implying an approximately 5.8 percent unrealized loss for a parallel 100-basis-point rate increase. By March 31, 2022, as yields had risen, the portfolio had an unrealized loss of $330 billion, about 4 percent of par value ([10]).

This case validates duration as a first-order sensitivity measure while also showing its limits. The portfolio contained both Treasuries and agency mortgage-backed securities; MBS duration changed as higher mortgage rates reduced refinancing incentives. The realized curve did not move as one parallel shock, and the reported accounting loss depended on the portfolio's purchase prices, holdings, and rate path. Board staff also distinguished market-value losses from realized income effects: securities held to maturity converge toward face value, whereas sales would crystallize gains or losses ([10]). Duration described exposure; it did not by itself determine accounting treatment, cash-flow realization, or policy consequences.

### A Liquidity Case: The March 2020 Treasury Disruption

The March 2020 Treasury disruption tests the assumption that a deep market is always liquid. Federal Reserve researchers reported sharp deterioration in bid-ask spreads, depth, and price impact as investors sold Treasuries and dealers absorbed inventory. Their collateral multiplier, measuring secured-financing activity relative to dealer Treasury positions, fell to 5.5 in the second week of March from a 2019 average of 7.5. Dealer secured-financing volumes rose, but not in proportion to the inventory dealers had to finance ([11]).

The study interpreted the decline as impaired intermediation rather than a deterioration in U.S. contractual credit quality. Federal Reserve repo operations and asset-purchase announcements coincided with subsequent improvement, with the sharper multiplier increase following expanded asset purchases. The authors appropriately limited the claim: the evidence supported dealer constraints and reduced collateral re-use as a mechanism, but did not exclude all alternative explanations ([11]). For bond valuation, the lesson is that observed spreads and prices can incorporate balance-sheet capacity and urgency to trade, not only expected cash flows.

### Current Credit Outcomes and Spread Measurement

S&P Global's 2025 annual corporate default study reported 117 global corporate defaults in 2025, down from 145 in 2024. The global speculative-grade default rate declined to 3.08 percent from 3.95 percent, but remained above the five-year average of 2.88 percent and close to the ten-year average of 3.13 percent ([12]). These are issuer outcomes for a defined rated universe, not loss rates for every bond portfolio. Security-level losses still depend on recovery, seniority, collateral, and purchase price.

Market spreads provide a different and faster-moving measure. FRED reported the ICE BofA U.S. Corporate Index OAS at 0.77 percent, or 77 basis points, on September 18, 2026. The series covers qualifying investment-grade, U.S. dollar-denominated corporate debt and measures option-adjusted spreads against a spot Treasury curve ([13]). It should not be compared mechanically with S&P's speculative-grade default rate because the populations and quantities differ. The comparison instead illustrates a methodological rule: define the universe, denominator, horizon, benchmark, and loss concept before interpreting any credit statistic.

The BIS evidence explains why a spread cannot be reduced to expected default loss. In addition to expected loss, investors price uncertainty, systematic risk, liquidity, taxes, and the difficulty of diversifying a negatively skewed loss distribution. A spread can widen because default expectations rise, because risk-bearing capacity falls, because benchmark liquidity changes, or because several channels move together ([18]). Analysts should decompose the signal rather than label every spread move "credit deterioration."

### Ratings as Opinions, Not Complete Valuations

Moody's May 16, 2025 downgrade of the United States to Aa1 from Aaa is a useful boundary case. Moody's cited a long deterioration in debt and interest-payment ratios while also emphasizing U.S. economic resilience and the dollar's reserve-currency role. The action changed an agency opinion on long-term issuer and senior-unsecured credit quality; it did not convert Treasury securities into a single new market price or measure their liquidity and duration ([15]).

Moody's action occurred in 2025. More generally, rating actions from S&P, Fitch, or Moody's should not be described as mechanically determining yields. A bond's price reflects market participants' cash-flow, benchmark, liquidity, option, and risk-premium assessments. Regulatory reforms that replace automatic rating references reinforce the need for independent credit analysis, while ratings remain a standardized and economically important information input ([14] [15]).

### Transparency Evidence

FINRA's TRACE history provides evidence that fixed income opacity is not static. Corporate-bond reporting began in 2002, and the system expanded across additional product classes. FINRA reports that eligible corporate and agency transactions must be reported within 15 minutes and that more than 80 percent are available within five minutes. Public data include execution time, price, yield, and sales volume ([16]).

The author's assessment from the scope of the data FINRA describes is that TRACE materially improves post-trade transparency but does not supply continuous executable quotes, eliminate dealer intermediation, or guarantee that a small historical trade represents the price for a large current order. Fixed income valuation therefore still needs both model-based cash-flow analysis and market-structure evidence ([16]).

## Implications

### For Investors and Portfolio Managers

The first practical implication is to begin with liabilities or objectives rather than with the highest displayed yield. An investor with a known payment date can match cash-flow timing, maturity, and credit quality to that obligation. A pension plan or insurer should examine asset and liability duration together; an individual funding a near-term purchase should not accept large mark-to-market exposure merely to earn a modestly higher long yield. The relevant question is whether the bond's cash flows and risks fit the horizon, not whether its coupon looks attractive ([5] [6] [17]).

Second, separate sources of return. The author's decomposition is coupon income, reinvestment income, rolldown as maturity shortens, price change from benchmark rates, price change from spreads, option effects, and credit loss. This decomposition prevents a common error: attributing every bond-price move to "rates." A corporate bond can fall while Treasury yields decline if its credit spread widens enough. A mortgage-backed security can lag an option-free Treasury when falling rates accelerate prepayment. A floating-rate note can have low duration but meaningful issuer credit risk ([4] [6] [20]).

Third, use duration and convexity as scenario tools. A manager can estimate the first-order effect of small rate moves with duration, add convexity for larger moves, and use key-rate measures for curve-shape scenarios. The manager should then run spread, liquidity, and cash-flow scenarios separately. The Federal Reserve portfolio case shows that duration can summarize a large exposure accurately enough to guide risk discussion, while the March 2020 case shows why liquidity and dealer capacity need their own stress tests ([10] [11]).

Fourth, judge yield against loss and optionality. A high yield can compensate for default risk, illiquidity, call risk, subordination, or an unusually unfavorable cash-flow profile. Expected loss analysis should combine probability of default with loss given default, then add a required premium for uncertainty and systematic exposure. The S&P default study and BIS spread research show why neither a rating nor an average historical default rate is sufficient on its own ([12] [18]).

Fifth, distinguish nominal safety from purchasing-power safety. A fixed contractual payment can be highly certain in nominal terms but worth less after inflation. TIPS alter principal with the Consumer Price Index, while ordinary fixed-rate bonds do not. Investors comparing them must separate real yield, expected inflation, and inflation risk premium rather than comparing coupons alone ([2]).

Diversification also requires regime awareness. Government bonds can offset equity losses when disinflationary growth shocks lower rates, but they can fall with equities when inflation raises discount rates across asset classes. The author's synthesis is that bonds are not an automatic hedge: diversification depends on the shock, maturity, inflation exposure, and credit quality. Portfolio construction should test inflation, recession, and liquidity scenarios rather than extrapolate one historical correlation.

### For Issuers and Corporate Finance

For issuers, bond pricing converts market conditions into financing cost. The benchmark curve sets a base rate, and the issuer's spread adds compensation for credit, liquidity, options, and other security features. Higher required yield lowers the price investors will pay for a given coupon. A company can issue at par by setting a coupon near the required yield, issue at a discount, or alter maturity, security, covenants, and call terms to change investor demand ([2] [4] [18]).

Maturity choice transfers risk. Long fixed-rate debt protects the issuer from near-term refinancing and rate-reset risk but transfers more duration risk to investors. Short debt or floating-rate debt lowers initial duration exposure for investors but leaves the issuer more exposed to refinancing conditions or rising reference rates. The BIS evidence frames this as a balance-sheet trade: reducing borrower maturity mismatch can increase creditor duration exposure ([17]). There is no maturity that removes risk for both sides.

Call provisions add flexibility for issuers at a cost. A callable bond allows refinancing if rates fall or credit quality improves, but investors recognize that favorable price appreciation and coupon income may be truncated. They may demand a higher coupon, call premium, or spread. Treasury teams should evaluate the option's value rather than assume that a lower initial coupon or longer stated maturity alone defines the cheapest financing ([4] [19]).

Observed secondary-market spreads also affect primary issuance. They influence investor price discovery, but they are not a complete measure of new-debt cost because issue size, covenants, underwriting conditions, and market capacity matter. TRACE can improve comparable-trade analysis, while financial statement and credit analysis determine whether observed peer spreads are economically applicable to the issuer ([16]).

The author's synthesis for capital budgeting is that a company should evaluate a new project against current marginal borrowing terms rather than the coupon on legacy debt. If benchmark rates or the issuer's spread rise, the present value of project cash flows discounted at a correspondingly higher required return falls, all else equal. This applies the same present-value and spread logic used in bond valuation; one observed spread does not by itself establish why financing conditions changed ([2] [4] [18]).

### For Banks, Insurers, and Liability-Driven Investors

Institutions should manage assets and liabilities jointly. A bank funded by short-term deposits but holding long fixed-rate assets faces both market-value and income sensitivity when rates rise. An insurer holding long bonds against long contractual liabilities may reduce economic mismatch even when the assets show accounting losses. Duration gaps, convexity gaps, optionality, and liquidity needs matter more than the standalone duration of either side ([8] [10]).

The Federal Reserve example illustrates the separation between market value and income. Rising rates reduced SOMA market values while higher liability rates affected interest expense more quickly than asset income reset. Board staff traced that exposure to the duration mismatch between longer-term assets and short-term interest-bearing liabilities ([10]). Commercial institutions have different accounting and solvency rules, but the risk mechanism is comparable: the timing of asset and liability repricing determines sensitivity.

Liquidity reserves must also be tested against forced-sale scenarios. March 2020 showed that even Treasury market depth can deteriorate when dealers absorb large inventories and balance-sheet capacity becomes scarce. A portfolio that is solvent on a hold-to-maturity basis can still create a liquidity problem if redemptions, margin calls, or collateral demands force sales into a stressed market ([11]). Sound risk management therefore combines cash-flow projections, collateral rules, contingent funding, and market-depth assumptions.

### For Credit Analysts and Regulators

Credit analysts should separate issuer default risk from security-level recovery and market pricing. A rating or estimated probability of default addresses only part of the loss distribution. Seniority, collateral, covenants, guarantees, jurisdiction, and capital structure affect recovery. Spread analysis then adds liquidity and risk-premium questions. The simple identity "wide spread equals high default probability" is inadequate ([12] [15] [18]).

Regulators face a parallel problem. Automatic reliance on ratings can concentrate model and governance risk, but removing every standardized signal can reduce comparability. Section 939A's approach was to replace mandatory rating references with alternative creditworthiness standards, not to prohibit ratings as information ([14]). The durable principle is independent verification: institutions should understand the methods, scope, and limitations of external ratings and market-based measures.

Transparency infrastructure improves oversight but does not eliminate valuation judgment. TRACE gives investors and regulators transaction evidence, while FRED and similar systems make benchmark and spread series accessible. Users must still inspect index eligibility, units, frequency, date, and revisions. The 0.77 percent investment-grade OAS observation from September 2026, for example, is a daily index statistic for a defined universe, not a universal corporate borrowing spread ([13] [16]).

### A Practical Analysis Sequence

The author's practical sequence is to proceed in a fixed order. First, map every possible cash flow, including calls, puts, sinking funds, prepayments, and recovery assumptions. Second, select the benchmark curve and discount promised cash flows. Third, measure rate sensitivity with duration, key-rate duration, and convexity appropriate to the cash-flow model. Fourth, analyze issuer credit, security priority, and recovery. Fifth, measure liquidity from transaction evidence and realistic trade size. Sixth, compare modeled value, market price, YTM, spread, OAS, and holding-period scenarios. Finally, test whether the security fits the investor's liabilities and loss capacity.

The author's synthesis is that this sequence prevents the worst analytical failure: accepting one summary statistic as the investment thesis. YTM can hide call and reinvestment risk; duration can hide credit loss; rating can hide market and liquidity risk; spread can combine several premia; and a model price can ignore transaction costs. A bond is adequately analyzed only when the cash-flow, curve, option, credit, liquidity, and portfolio views reconcile.

## Criticism and Limitations

Present-value formulas are identities conditional on their inputs, not evidence that the inputs are correct. A small change in the discount curve, default probability, recovery, prepayment behavior, or volatility can materially change price. Model precision should therefore be reported with scenarios and assumptions rather than as a point estimate that implies false certainty ([7] [8] [20]).

YTM compresses a term structure into one rate and assumes promised cash flows. It can be useful for standardized comparison, but it does not describe the path of reinvestment rates, taxes, transaction costs, or early sale prices. For callable securities, YTM may describe a cash-flow path that the issuer is unlikely to permit when it is favorable to the investor ([4] [19]).

Duration and convexity are local approximations. Standard portfolio aggregation often assumes parallel curve shifts even though such shifts are rare, and option-free measures fail when rates alter cash flows. CFA Institute explicitly identifies the parallel-shift assumption as a limitation of common portfolio duration and convexity calculations ([6] [7]). Analysts should use full repricing and multiple curve scenarios when the exposure is consequential.

Credit spreads are also ambiguous. Expected default loss is only one component, and benchmark choice can introduce its own liquidity premium. The BIS credit-spread evidence shows that taxes, risk premia, liquidity, and undiversified unexpected loss can explain large portions of observed spreads ([18]). A spread model should state what it attributes to each component and acknowledge residual uncertainty.

Ratings simplify communication, and category boundaries can matter when regulations, mandates, or contracts refer to them. Moody's defines a rating as an opinion of credit quality, not a recommendation or a guarantee that default will not occur. The SEC's removal of mandatory rating references and Moody's stated limits both support treating ratings as inputs rather than delegated decisions ([14] [21]).

Finally, transparent trade data do not make all bonds liquid. TRACE records completed transactions; it does not guarantee depth for the next order. March 2020 demonstrated that even a benchmark government market can suffer large declines in depth when intermediation capacity is constrained ([11] [16]). The practical limit of fixed income mathematics is therefore institutional: valuation can estimate what a cash-flow stream is worth under assumptions, but actual realization depends on payment performance and the market's capacity to transfer risk.

## Sources

1. SIFMA Research. "2026 Capital Markets Fact Book." August 13, 2026.
   https://www.sifma.org/research/statistics/fact-book [high]

2. U.S. Department of the Treasury, Bureau of the Fiscal Service.
   "Understanding Pricing and Interest Rates."
   https://www.treasurydirect.gov/marketable-securities/understanding-pricing
   [high]

3. U.S. Securities and Exchange Commission, Office of Investor Education
   and Advocacy. "Interest Rate Risk -- When Interest Rates Go Up, Prices
   of Fixed-Rate Bonds Fall." June 2013.
   https://www.investor.gov/sites/default/files/ib_interestraterisk.pdf
   [high]

4. FINRA. "Understanding Bond Yield and Return." August 11, 2022.
   https://www.finra.org/investors/insights/bond-yield-return [high]

5. FINRA. "Brush Up on Bonds: Interest Rate Changes and Duration."
   September 19, 2024.
   https://www.finra.org/investors/insights/bonds-interest-rate-changes-duration
   [high]

6. CFA Institute. "Yield-Based Bond Duration Measures and Properties."
   2026 CFA Program Level I Fixed Income curriculum.
   https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/yield-based-bond-duration-measures-and-properties
   [high]

7. CFA Institute. "Yield-Based Bond Convexity and Portfolio Properties."
   2026 CFA Program Level I Fixed Income curriculum.
   https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/yield-based-bond-convexity-and-portfolio-properties
   [high]

8. Papaioannou, M. "A Primer for Risk Measurement of Bonded Debt from
   the Perspective of a Sovereign Debt Manager." IMF Working Paper
   WP/06/195, August 2006.
   https://www.imf.org/external/pubs/ft/wp/2006/wp06195.pdf [high]

9. Macaulay, F. R. "Some Theoretical Problems Suggested by the Movements
   of Interest Rates, Bond Yields and Stock Prices in the United States
   Since 1856." NBER, 1938.
   https://www.nber.org/books-and-chapters/some-theoretical-problems-suggested-movements-interest-rates-bond-yields-and-stock-prices-united
   [high]

10. Anderson, A., Na, D., Schlusche, B., and Senyuz, Z. "An Analysis of
    the Interest Rate Risk of the Federal Reserve's Balance Sheet, Part
    1: Background and Historical Perspective." Federal Reserve Board
    FEDS Notes, July 15, 2022.
    https://www.federalreserve.gov/econres/notes/feds-notes/an-analysis-of-the-interest-rate-risk-of-the-federal-reserves-balance-sheet-part-1-20220715.html
    [high]

11. Infante, S. and Saravay, Z. "Treasury Market Functioning During the
    COVID-19 Outbreak: Evidence from Collateral Re-use." Federal Reserve
    Board FEDS Notes, December 4, 2020.
    https://www.federalreserve.gov/econres/notes/feds-notes/treasury-market-functioning-during-the-covid-19-outbreak-evidence-from-collateral-re-use-20201204.html
    [high]

12. S&P Global Ratings. "Default, Transition, and Recovery: 2025 Annual
    Global Corporate Default and Rating Transition Study." March 18,
    2026.
    https://www.spglobal.com/ratings/en/regulatory/article/default-transition-and-recovery-2025-annual-global-corporate-default-and-rating-transition-study-s101673333
    [high]

13. ICE Data Indices, LLC. "ICE BofA US Corporate Index Option-Adjusted
    Spread (BAMLC0A0CM)." FRED, Federal Reserve Bank of St. Louis.
    https://fred.stlouisfed.org/series/BAMLC0A0CM [high]

14. U.S. Securities and Exchange Commission. "Removal of References to
    Credit Ratings From Regulation M." Release No. 34-97657, June 7,
    2023.
    https://www.sec.gov/rules-regulations/2023/06/34-97657 [high]

15. Moody's Ratings. "Moody's Ratings Downgrades United States Ratings
    to Aa1 from Aaa; Changes Outlook to Stable." May 16, 2025.
    https://ratings.moodys.com/ratings-news/443154 [high]

16. FINRA. "What Is TRACE and How Can It Help Me?" August 17, 2023;
    updated July 18, 2024.
    https://www.finra.org/investors/insights/what-is-TRACE [high]

17. Chan, T., von Peter, G., and Wooldridge, P.
    "International Finance Through the Lens of BIS Statistics: Bond
    Markets, Domestic and International." BIS Quarterly Review,
    September 2025.
    https://www.bis.org/publ/qtrpdf/r_qt2509e.pdf [high]

18. Amato, J. D. and Remolona, E. M. "The Credit Spread Puzzle."
    BIS Quarterly Review, December 2003.
    https://www.bis.org/publ/qtrpdf/r_qt0312e.pdf [high]

19. FINRA. "Callable Bonds: Be Aware That Your Issuer May Come Calling."
    April 19, 2024.
    https://www.finra.org/investors/insights/callable-bonds-your-issuer-may-come-calling
    [high]

20. CFA Institute. "Curve-Based and Empirical Fixed-Income Risk
    Measures." 2026 CFA Program Level I Fixed Income curriculum.
    https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/curve-based-and-empirical-fixed-income-risk-measures
    [high]

21. Moody's Investors Service. "Moody's Rating System in Brief."
    March 12, 2009.
    https://www.moodys.com/sites/products/ProductAttachments/Moody%27s%20Rating%20System.pdf
    [high]

## See Also

- `library/finance/anchor-finance.md` -- domain anchor defining the
  finance topic boundaries.
- `library/finance/yield-curve.md` -- how maturity-specific benchmark
  rates form the term structure used in bond pricing.
- `library/finance/credit-analysis-default-risk.md` -- issuer and
  security analysis underlying default probability and recovery.
- `library/finance/financial-market-microstructure.md` -- how trading,
  dealer intermediation, and transparency affect observed prices.
- `library/macro-micro/monetary-policy-and-central-banking.md` -- how
  policy rates and balance-sheet actions influence benchmark curves.
- `library/valuation-screening/discounted-cash-flow-dcf-methodology.md`
  -- the parallel present-value framework used for business valuation.
