---
name: credit-analysis-default-risk
id: 20260827T061637Z
tier: library-topic
domain: finance
author: Librarian
tags: [credit-analysis, default-risk, creditworthiness, credit-ratings, five-cs-of-credit, leverage-ratios, coverage-ratios, altman-z-score, merton-model, basel-irb]
links: [library/finance/bond-pricing-and-fixed-income-markets.md, library/finance/financial-statement-analysis.md, library/finance/capital-structure-modigliani-miller.md, library/finance/banking-maturity-transformation.md]
reviewed: 2026-10-01
---

# Credit Analysis -- Why Assessing Default Risk Is the Discipline That Makes Lending Possible

Credit analysis evaluates whether an obligor can and will perform as promised, how much exposure will exist if default occurs, and how much value may be recovered. It combines cash-flow capacity, business and financial risk, instrument structure, collateral, covenants, market evidence, and quantitative models; no single ratio, rating, or model is a complete credit decision [1][2][3][11]. Its purpose is not to eliminate uncertainty but to make lending, pricing, limit, and monitoring decisions with explicit assumptions and loss consequences.

## Background

Modern credit analysis developed from the need to compare borrowers and securities whose financial information, contractual protections, and economic conditions differed. John Moody introduced ratings to the U.S. bond market in 1909 through his analysis of railroad securities, translating detailed issuer information into an ordinal opinion that investors could compare [5]. The later spread of agency ratings did not remove the need for independent analysis. A rating is an opinion about relative creditworthiness, not a guarantee, an investment recommendation, or a complete measure of price, liquidity, or recovery [4][5]. The distinction remains fundamental: a lender owns a particular exposure with particular terms, while a rating compresses only specified dimensions of risk.

Bank lending developed a parallel underwriting shorthand in the Five Cs: character, capacity, capital, collateral, and conditions. The Office of the Comptroller of the Currency describes these as basic components of effective lending decisions, while also requiring quantitative criteria such as debt or income ratios, loan-to-value measures, credit scores where used, maturity, and pricing [1]. The Five Cs therefore organize questions rather than provide an algorithm. Interagency small-business guidance expands the inquiry to the borrower's business plan, use and repayment of funds, competition, local conditions, current and expected cash flow, financial strength, management, guarantors, collateral, and ability to contribute additional capital [2]. This broader list shows why credit analysis cannot be reduced to a score or a collateral value.

Statistical failure prediction gave the discipline a reproducible empirical branch. Beaver's 1966 univariate work tested whether individual accounting ratios separated failed firms from nonfailed firms. Altman's 1968 study then used multiple discriminant analysis on 66 U.S. manufacturing firms, split equally between bankrupt and nonbankrupt groups, to combine five accounting and market-value ratios into the original Z-Score [6][7]. These studies established that financial statements contain information about later failure, but they did not create timeless laws. Their samples, accounting definitions, industries, estimation methods, and classification cutoffs limit direct use in populations unlike those on which the models were fitted [6][7]. A discriminant score ranks or classifies risk; it is not a probability of default unless separately mapped to observed default frequencies and validated.

Merton's 1974 structural model supplied a different intellectual foundation. Under its simplified capital structure, equity is a contingent claim on firm assets and default occurs at debt maturity when asset value is insufficient to meet the promised payment [8]. The framework connects leverage and asset volatility to credit risk through option-pricing mathematics. Later distance-to-default implementations infer unobservable asset value and volatility from equity-market information and compare the estimated asset value with a default boundary [9]. The economic insight is durable, but the literal model assumes a simple liability structure, continuous asset dynamics, and a specified default boundary. Real firms have coupons, multiple maturities, secured and unsecured claims, liquidity needs, and the possibility of default before final maturity.

Bank regulation formalized credit-risk parameters. Basel I, released in 1988, established a broad risk-weighted capital framework and an 8 percent minimum total-capital ratio for internationally active banks. Basel II, released in 2004 and consolidated in 2006, introduced a three-pillar framework and internal ratings-based approaches. The current Basel Framework is not simply Basel II plus higher capital. The Basel Committee completed major post-crisis reforms in 2017, constrained internal-model use, added input floors, and introduced a standardized output floor [11]. Current IRB risk components are probability of default (PD), loss given default (LGD), exposure at default (EAD), and, where applicable, effective maturity (M). Foundation IRB generally uses a bank estimate of PD and supervisory values for other components; advanced IRB permits more internal estimates only for eligible portfolios and subject to approval, floors, and validation [11].

The post-crisis changes matter because the 2007-2009 crisis exposed model, governance, and incentive failures. The SEC's 2008 examination of major rating agencies found weaknesses in staffing, documentation, surveillance, model governance, and the treatment of assumptions used in residential mortgage-backed securities and collateralized debt obligations [12]. Structured-finance models depended on default, recovery, and correlation assumptions drawn from short and unusually benign histories. Common exposure to falling house prices and deteriorating underwriting made apparently diversified pools more dependent than estimated [12]. Dodd-Frank subsequently strengthened NRSRO controls and disclosures and directed federal agencies to remove references to credit ratings from their regulations where required; the SEC's 2023 Regulation M amendments were one implementation of that mandate [16]. These reforms reinforce, rather than replace, the central rule of credit analysis: understand the cash flows, contract, data, and failure mechanism behind every summary measure.

## Core Concepts

### The Five Cs are a map, not a scoring formula

**Character** concerns evidence about a borrower's reputation and willingness to meet obligations. Payment history, prior restructurings, transparency, governance, and management conduct can inform the assessment, but subjective impressions require consistent policy and documentation. Character is neither synonymous with willingness nor automatically more important than the other dimensions [1][2].

**Capacity** asks whether the primary repayment source can meet contractual obligations under a reasonable range of conditions. For most operating-business loans, this means analyzing current and expected business cash flow, its volatility, working-capital needs, capital expenditure, taxes, and competing claims. A forecast should connect operating drivers to debt service and should not depend only on an optimistic base case [2][3].

**Capital** measures the borrower's own financial commitment and the resources available to absorb stress. Equity can protect creditors from moderate asset losses, but book equity is not automatically realizable loss protection. Asset quality, hidden liabilities, distributions, valuation uncertainty, and structural subordination determine how much capital is economically available [1][3].

**Collateral** concerns assets and enforceable rights that support repayment or recovery. In conventional cash-flow lending, collateral and guarantees are commonly secondary repayment sources; in revolving asset-based lending, conversion of receivables or inventory may be the intended primary source. An analyst must examine eligibility, valuation, advance rates, lien perfection, prior claims, control of proceeds, liquidation time, and costs rather than quote loan-to-value alone [1][2].

**Conditions** include the purpose of the loan and external circumstances affecting performance: industry economics, competition, local and national demand, regulation, rates, currencies, commodity inputs, customer concentration, and the broader cycle [1][2]. The same balance sheet can support different risk conclusions when a borrower faces stable recurring demand, a cyclical commodity market, or a single refinancing date in a closed capital market.

The Five Cs are deliberately broad. They help prevent omission, but they do not determine how factors should be weighted, how default is defined, or what price compensates for risk. The author's synthesis is that the framework is most useful as a completeness test placed around, not instead of, cash-flow modeling and contract analysis.

### Leverage and coverage require definitions and context

Leverage ratios compare a defined debt measure with equity, assets, earnings, or cash flow. The numerator must state whether it includes leases, preferred stock, pensions, guarantees, securitization support, and undrawn commitments, and whether cash is netted. Debt-to-equity can illuminate the creditor-versus-equity financing mix, while debt-to-capital and debt-to-assets provide related balance-sheet views. None mechanically determines default or recovery because asset quality, cash generation, maturity, collateral, priority, and jurisdiction can dominate the same headline ratio [3].

Debt/EBITDA is a gross leverage multiple, not a literal estimate of years required to repay debt. EBITDA precedes cash interest, taxes, working-capital investment, capital expenditure, distributions, and principal amortization. S&P's corporate methodology therefore analyzes core leverage measures alongside cash-flow measures such as funds from operations, cash flow from operations, free operating cash flow, discretionary cash flow, and interest coverage; it also warns that EBITDA can overstate financial strength for capital-intensive or working-capital-intensive businesses [3]. A 4.0x multiple means defined debt equals four times defined EBITDA. It does not mean the borrower can extinguish debt in four years.

Coverage ratios compare an earnings or cash-flow numerator with a contractual burden. EBIT/interest and EBITDA/interest are useful but omit principal and may treat leases or capitalized interest differently. In commercial real estate, debt-service coverage commonly divides net operating income by scheduled principal and interest. Fixed-charge coverage is contract-specific and may include rent, taxes, capital expenditure, distributions, or other charges. A result below 1.0x means the stated numerator does not cover the stated denominator; a result above 1.0x supplies arithmetic headroom. There is no universal threshold that by itself defines investment grade, distress, or an acceptable covenant. Sector volatility, accounting adjustments, amortization, maturity, and the agreement's exact definitions control the interpretation [3][15].

### Repayment capacity is a time path, not a ratio snapshot

A complete cash-flow analysis reconciles historical results, current liquidity, and forward obligations. It identifies the primary repayment source, schedules interest and principal, maps maturities and refinancing needs, models working capital and maintenance investment, and separates cash earnings from accruals or add-backs. It then applies downside cases to the operating drivers that actually threaten repayment. Interagency guidance specifically calls for current and expected cash flows across a reasonable range of future conditions and cautions against relying excessively on collateral values [2].

Liquidity and solvency must be tested separately. A borrower can have positive long-run enterprise value but fail because cash is unavailable on a due date. Another can meet near-term payments while its assets and earnings are insufficient to support the debt eventually. Revolver availability, restricted cash, collateral borrowing bases, margin requirements, supplier terms, and legal-entity location determine whether reported liquidity can serve the relevant obligation. The author's synthesis is that every credit memorandum should state both the expected repayment path and the earliest plausible point at which that path can fail.

### PD, LGD, EAD, and maturity separate different questions

Probability of default is the likelihood that a defined obligor meets a defined default criterion over a stated horizon. In the Basel IRB framework, corporate, sovereign, and bank PD is the one-year PD associated with an internal borrower grade, estimated as a long-run average of observed one-year default rates [11]. A rating migration, missed payment, distressed exchange, bankruptcy filing, and regulatory default can be related but are not automatically the same event. The analyst must state the definition, horizon, population, and whether the estimate is point-in-time or through-the-cycle.

Loss given default is economic loss as a percentage of EAD if default occurs. Basel's own-LGD concept includes material discounting and direct and indirect collection costs; LGD equals one minus recovery only when both use the same denominator, valuation date, discounting, and cost conventions [11]. Seniority and collateral generally improve expected recovery, but neither implies a fixed percentage. Enterprise value, collateral coverage, priority debt, guarantees, jurisdiction, restructuring tactics, and the credit cycle all affect realization [14].

Exposure at default is the gross facility exposure expected when the obligor defaults. For a term loan it begins with the drawn balance; for a revolver or commitment it must consider additional drawings before default. Effective maturity captures the timing of contractual cash flows and enters relevant IRB capital formulas [11]. These variables belong at different levels: PD is principally an obligor question, while LGD and EAD are strongly facility-specific.

For nondefaulted corporate, sovereign, bank, and retail IRB exposures, the Basel expected-loss rate is PD x LGD and the currency expected-loss amount is PD x LGD x EAD [11]. This identity is an expectation, not the worst-case loss and not a complete accounting impairment method. Unexpected loss, concentration, parameter uncertainty, and dependence among obligors require capital and stress analysis beyond expected loss.

### Ratings, market measures, and internal grades answer different questions

Credit ratings are forward-looking ordinal opinions about relative creditworthiness. S&P's long-term scale generally treats BBB- and above as investment grade and lower categories as speculative grade; Moody's uses Baa3 as its lowest investment-grade category [4][5]. The symbols are comparable shorthand, not identical probabilities or universal legal classifications. Issuer ratings, issue ratings, national scales, recovery ratings, and short-term ratings have different scopes.

Corporate rating methodologies combine business risk, financial risk, liquidity, capital structure, financial policy, management and governance, and other modifiers. S&P first combines business and financial risk into an anchor, then applies modifiers to determine a stand-alone credit profile and, where relevant, a support framework to determine the issuer rating [3]. A ratio can therefore be weak without dictating a speculative-grade rating, or strong without overcoming a vulnerable business profile.

Market prices supply faster but noisier evidence. Bond spreads, credit default swap spreads, and equity volatility can respond before financial statements, but they include liquidity, risk premia, technical flows, and model assumptions as well as expected credit loss. Internal grades may incorporate private information and facility monitoring but can become stale or optimistic without independent review. The analyst should reconcile ratings, internal grades, market measures, and fundamentals, investigate material disagreements, and avoid treating any one signal as ground truth [4][9].

### Statistical and structural models rank risk under assumptions

The original Altman Z-Score is [6][7]:

Z = 1.2X1 + 1.4X2 + 3.3X3 + 0.6X4 + 1.0X5

where X1 is working capital/total assets, X2 retained earnings/total assets, X3 EBIT/total assets, X4 market value of equity/book value of total liabilities, and X5 sales/total assets [6][7]. The familiar 1.81 and 2.99 boundaries came from the original public-manufacturing context. Applying the equation to private firms, financial companies, nonmanufacturers, or a different accounting regime without recalibration can misclassify risk. The score is transparent and useful as a screen, but it does not by itself estimate a calibrated PD.

In the Merton model, equity behaves like a call option on firm assets under a simplified debt structure, and default at maturity occurs when asset value falls below the promised debt payment [8]. Distance to default standardizes the gap between estimated asset value and a default point by estimated asset volatility. Translating that distance into a physical default probability requires additional assumptions or empirical calibration; an option-pricing probability is risk-neutral when it uses risk-neutral inputs [8][9]. Thin equity trading, changing liabilities, jumps, early default, and complex priority structures weaken the mapping.

Reduced-form and hazard models estimate default from observed covariates without requiring the Merton capital-structure mechanism. Accounting profitability and leverage, market capitalization, recent return, equity volatility, cash holdings, and valuation variables have all appeared in empirical failure models [9][10]. The methods are complementary rather than hierarchically complete. Accounting data describe accumulated operating and financing results; market data update rapidly; structural models impose an economic mechanism; statistical models exploit historical associations. Combining signals can improve discrimination, but every combination still needs out-of-sample validation, stable definitions, and governance.

### Covenants and security structure govern what happens before and after default

Maintenance covenants are tested periodically or when a specified springing trigger activates. Incurrence covenants are tested when the borrower proposes an action such as issuing debt, making a restricted payment, or completing an acquisition. Debt/EBITDA, interest coverage, debt-service coverage, and fixed-charge coverage can all appear, but their definitions, thresholds, testing dates, cure rights, baskets, add-backs, and remedies are contractual [15]. A generic market threshold cannot substitute for reading the agreement.

Security analysis maps each claim through the legal entity and capital structure. It identifies obligor and guarantor coverage, collateral, lien priority, intercreditor terms, structural subordination, permitted priority debt, transfer restrictions, and enforcement jurisdiction. Covenant headroom is an early-warning measure, not itself a recovery rate. A breach can create information, repricing, waiver, amendment, acceleration, or enforcement rights; bargaining power depends on the contract, liquidity, sponsor support, and alternatives available to both sides [14][15].

## Evidence

### Altman's original result was strong in-sample and horizon-dependent

Altman's 1968 discriminant study selected 33 bankrupt and 33 nonbankrupt U.S. manufacturing firms and combined five ratios from an initial candidate set into the Z-Score [6][7]. On the original sample, the model correctly classified 95 percent of all firms using statements one year before failure. Correct assignment fell to 72 percent two years before failure, 48 percent three years before failure, 29 percent four years before failure, and 36 percent five years before failure [7]. These results demonstrate that multivariate financial information can discriminate imminent failure in a matched historical sample. They do not establish those percentages as current out-of-sample accuracy, and the sharp horizon decline argues against treating the score as a long-range forecast.

The design also explains important limits. The sample was small, balanced by construction, and confined to manufacturing firms, unlike the true population in which defaults are rare and industry structures differ. Multiple discriminant analysis imposed a linear score and fixed coefficients. Later variants changed variables or coefficients for private and nonmanufacturing firms, confirming that the original equation was not universal [7]. The appropriate lesson is methodological: validate the model on the target population and report false-negative and false-positive errors, not only total accuracy.

### Market-based structure helps, but the Merton solution is not sufficient

Bharath and Shumway tested the Merton distance-to-default model in hazard models and out-of-sample forecasts covering 1980-2003. They compared the full Merton implementation with a simpler predictor using its functional form but not solving for implied asset value and volatility. The simple alternative performed slightly better than the Merton model in their hazard and out-of-sample tests, and an expanded hazard model using additional predictors outperformed Merton default probabilities [9]. Their conclusion was not that structural information is useless: the functional form and inputs were informative, but the full model was not a sufficient statistic for default probability.

Campbell, Hilscher, and Szilagyi used U.S. data from 1963-2003 in a dynamic logit framework [10]. Their model combined accounting and market variables and found higher failure risk associated with higher leverage, lower profitability, smaller market capitalization, weaker recent stock returns, higher equity volatility, lower cash, higher market-to-book ratios, and lower share prices. Persistent variables became more important at longer horizons, and the model captured much of the time variation in aggregate failure rates [10]. Together, these studies support a combined information set and contradict the claim that one structural or accounting score dominates in all settings.

### Rating default studies require exact populations and horizons

S&P's 2025 global corporate study counted 117 defaults and reported a 3.08 percent issuer-weighted speculative-grade default rate, down from 3.95 percent in 2024 [13]. In its 1981-2025 global corporate history, the issuer-weighted average one-year default rate was 0.13 percent for BBB and 2.87 percent for B; the corresponding cumulative rates rose materially over longer horizons [13]. Those values replace generic claims that BBB defaults at roughly 0.3 percent and B at 5 percent or more each year.

The methodological qualification is as important as the numbers. A realized historical rate for an agency-rated cohort is not the current PD of a particular issuer. Rating category, starting date, issuer versus issue weighting, treatment of withdrawals and distressed exchanges, geography, sector, and horizon all affect the statistic [13]. Rating transitions also matter because deterioration can precede default and change refinancing access before any payment is missed.

### Recovery varies with structure, measurement, and cycle

S&P's review of recent U.S. leveraged-finance restructurings used ultimate nominal recoveries from bankruptcy documents. In its limited 2023-2025 sample, first-lien recoveries averaged about 60 percent, below more than 70 percent in earlier cohorts, while an overwhelming majority of unsecured creditors recovered less than 10 percent [14]. The report linked weaker outcomes to changing debt structures, more priority debt, thinner junior cushions, and restructuring tactics. These are sample-specific nominal outcomes, not Basel economic LGDs, which discount recovery cash flows and include collection costs [11][14].

The evidence rejects fixed rules such as "senior secured recovers 60-80 percent" or "unsecured recovers 30-50 percent." Priority and collateral matter, but realized recovery depends on the amount and quality of collateral, enterprise value, debt ahead of the claim, guarantees, jurisdiction, costs, time, and whether the measurement uses trading price, emergence value, or ultimate cash [14]. A defensible LGD estimate therefore states its population, date, weighting, valuation basis, and downturn treatment.

### The structured-finance failure showed why model governance is credit analysis

The SEC's 2008 examination found that rating agencies used distinct structured-finance models, but some inputs and performance assumptions relied on corporate-bond experience and short mortgage histories [12]. Default probability, recovery, and correlation were central inputs. Agencies did not consistently document model departures, rating-committee decisions, or surveillance processes, and staffing did not always keep pace with volume [12]. The failure was therefore not simply "bad math." It combined limited data, model sensitivity, deteriorating underwriting, common housing exposure, incentive conflicts, and weak governance.

This case supplies a general test for credit models. Ask whether the calibration period contains the adverse state being priced, whether dependence rises in that state, whether underwriting or contract terms have changed since the data were generated, and whether overrides are documented and independently challenged. The author's synthesis is that a model is part of the credit process only when its data lineage, assumptions, validation, use, and failure conditions are visible.

### Basel's current constraints acknowledge model risk

The current Basel Framework requires initial and continuing supervisory approval, independent credit-risk control, at least annual internal-audit review, comparison of estimated parameters with realized outcomes, and documented validation across varied economic conditions [11]. It limits advanced IRB use for specified exposures, applies PD, LGD, and EAD floors, and anchors aggregate model-based risk-weighted assets to standardized calculations through the output floor [11]. At the Basel level, the transitional floor is 65 percent in 2026 and is scheduled to reach 72.5 percent in 2028, subject to jurisdictional implementation [11]. These controls do not prove model accuracy. They constrain how far unverified or unusually favorable internal estimates can reduce regulatory capital.

## Implications

### For lenders and banks

The author's practical sequence begins with the obligation, not the ratio. First, identify the legal borrower, guarantors, purpose, amount, currency, amortization, maturity, and contingent drawings. Second, identify primary and secondary repayment sources. Third, normalize historical earnings and cash flow, reconcile debt definitions, and build a base case tied to operating drivers. Fourth, test downside cases that connect revenue, margin, working capital, capital expenditure, rates, currencies, and refinancing to payment capacity. Fifth, map collateral, liens, covenants, baskets, cure rights, and remedies. Sixth, estimate PD, EAD, and LGD with definitions and horizons that match the decision. Finally, set price, limit, structure, conditions, and monitoring triggers [1][2][3][11].

The author's assessment is that this sequence prevents two recurring errors. The first is lending against a multiple while ignoring the cash bridge between EBITDA and debt service. The second is lending against collateral while ignoring control, prior liens, liquidation cost, or time. A sound approval should explain how repayment occurs in the base case and what protects the lender when that case fails. If neither explanation is coherent, a high spread does not repair the structure.

Portfolio management adds dependence and concentration. Individually plausible PD and LGD estimates can understate portfolio loss when borrowers share a commodity, region, customer, sponsor, funding market, or macro shock. Limits should therefore aggregate direct loans, commitments, derivatives, guarantees, warehouse lines, and correlated collateral. Stress testing should combine higher defaults, lower recoveries, larger revolver drawings, and reduced market liquidity rather than move one parameter at a time [11][12].

Model governance is an operating requirement, not a documentation exercise. Input definitions, overrides, missing data, validation samples, realized default and recovery outcomes, and version changes should be traceable. Independent review should have authority to challenge both statistical performance and business use. Basel's ongoing validation requirements provide a regulatory minimum; management remains responsible for risks that a model omits [11].

### For bond and loan investors

Credit returns are asymmetric because contractual upside is limited while principal loss can be large. Yield must therefore be decomposed into expected loss, uncertainty, liquidity, optionality, and other risk premia. A rating or spread does not reveal all components. Investors should analyze the issuer's repayment capacity and then the instrument's priority, collateral, guarantees, covenants, call features, and recovery path [3][4][14].

The investment-grade boundary matters because mandates, index rules, and regulatory-capital treatment can induce concentrated selling after a downgrade. A fallen angel is not automatically sold by every institution, but investors subject to investment-grade constraints can create weaker liquidity and wider spreads. The refinancing effect reaches the issuer when new debt must be sold at the wider market spread; it does not mechanically change the coupon on an outstanding fixed-rate bond [4][13]. An investor should distinguish a temporary technical discount from a deterioration in expected cash flows or recovery and should be able to hold through the period required for that distinction to resolve.

Recovery analysis should precede a default forecast when downside protection is central to the thesis. The analyst should construct a legal-entity capital structure, value operating assets under stressed assumptions, deduct priority claims and costs, and allocate remaining value through liens and guarantees. S&P's recent recovery evidence shows why the label "first lien" is insufficient when priority debt has increased or junior support has disappeared [14].

### For corporate management

Credit analysis is also a financing-management discipline. Management should monitor gross and net leverage, cash interest, fixed charges, free operating cash flow, maturities, undrawn commitments, covenant headroom, collateral availability, rating sensitivities, and refinancing conditions. The objective is not to manage to one agency threshold. Corporate methodologies combine business and financial risk, and covenant definitions can differ materially from rating-agency adjustments [3][15].

A downgrade can matter before default through higher marginal borrowing costs, reduced investor eligibility, collateral terms, or counterparty limits [3][4][13]. Management should therefore preserve liquidity before markets close, not after a ratio crosses a public boundary. Extending maturity, reducing distributions, selling noncore assets, raising equity, or renegotiating covenants each transfers value and risk differently. The appropriate action depends on the source of stress and the durability of the business, not on cosmetic improvement in one metric.

Transparent disclosure improves the credit decision. Reconciliations between reported debt and adjusted debt, EBITDA and free cash flow, unrestricted and restricted cash, and covenant calculations reduce uncertainty. Hiding aggressive add-backs or near-term obligations can preserve a headline ratio briefly while increasing the premium demanded by informed creditors. The author's assessment is that credibility is itself a financing asset because it affects how quickly lenders accept forecasts and waivers, but it cannot substitute for cash.

### For regulators and financial stability

Regulators must balance risk sensitivity with comparability and cyclicality. Internal models can use granular borrower information, but they can also produce optimistic parameters, heterogeneous risk-weighted assets, and synchronized reactions when conditions deteriorate. The current Basel response combines long-run PD estimation, downturn-sensitive LGD and EAD where applicable, parameter floors, validation, capital buffers, and a standardized output floor [11]. These mechanisms mitigate model risk and procyclicality; they do not eliminate either.

External ratings create a similar trade-off. Standardized opinions reduce search costs and coordinate markets, but automatic regulatory reliance can concentrate decisions in a small number of methodologies. Dodd-Frank section 939A required covered federal agencies to review and remove regulatory references to ratings and substitute other creditworthiness standards where appropriate; it did not prohibit investors from using ratings as evidence [16]. Independent analysis means understanding the rating's scope and assumptions, not ignoring it.

Systemic risk emerges when many institutions share the same data, model, collateral, or funding assumption. The structured-finance experience showed that borrower-level diversification did not neutralize a common housing shock and that rating and liquidity errors could reinforce one another [12]. Reverse stress testing is therefore essential: identify the combination of defaults, drawings, collateral decline, recovery delay, margin calls, and market illiquidity that would exhaust capital or cash, then determine whether those events can cause one another.

The author's final assessment is that credit analysis is a disciplined argument about repayment and loss, not a search for a decisive metric. A complete analysis states the obligor, instrument, horizon, default definition, primary repayment source, downside path, exposure, recovery mechanism, model limits, and monitoring triggers. The decision remains uncertain, but its failure modes become explicit enough to price, structure, limit, and revisit.

## Sources

1. Office of the Comptroller of the Currency. "Installment Lending," Comptroller's Handbook, version 1.3, May 23, 2018, with March 20, 2025 edit notice.
   https://www.occ.treas.gov/publications-and-resources/publications/comptrollers-handbook/files/installment-lending/pub-ch-installment-lending.pdf [high]

2. Board of Governors of the Federal Reserve System, FDIC, OCC, OTS, NCUA, and state supervisors. "Interagency Statement on Meeting the Credit Needs of Creditworthy Small Business Borrowers." February 5, 2010.
   https://www.federalreserve.gov/bcreg20100205.pdf [high]

3. S&P Global Ratings. "Corporate Methodology." Current criteria article and August 2025 PDF.
   https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/12913251 [high]

4. S&P Global Ratings. "Guide to Credit Rating Essentials." 2024.
   https://www.spglobal.com/content/dam/spglobal/ratings/en/documents/pdfs/guide-to-credit-rating-essentials_2024.pdf [high]

5. Moody's Investors Service. "Moody's Rating System in Brief." March 12, 2009.
   https://www.moodys.com/sites/products/ProductAttachments/Moody%27s%20Rating%20System.pdf [high]

6. Altman, E. I. "Financial Ratios, Discriminant Analysis and the Prediction of Corporate Bankruptcy." Journal of Finance 23(4), 1968, 589-609.
   https://doi.org/10.1111/j.1540-6261.1968.tb00843.x [high]

7. Altman, E. I. "Predicting Financial Distress of Companies: Revisiting the Z-Score and ZETA Models." In Bankruptcy, Credit Risk, and High Yield Junk Bonds, 2002.
   https://www.blackwellpublishing.com/content/bpl_images/content_store/sample_chapter/0631225633/altman.pdf [high]

8. Merton, R. C. "On the Pricing of Corporate Debt: The Risk Structure of Interest Rates." Journal of Finance 29(2), 1974, 449-470.
   https://doi.org/10.1111/j.1540-6261.1974.tb03058.x [high]

9. Bharath, S. T., and Shumway, T. "Forecasting Default with the Merton Distance to Default Model." Review of Financial Studies 21(3), 2008, 1339-1369.
   https://scholarsarchive.byu.edu/cgi/viewcontent.cgi?article=10178&context=facpub [high]

10. Campbell, J. Y., Hilscher, J., and Szilagyi, J. "In Search of Distress Risk." Journal of Finance 63(6), 2008, 2899-2939; NBER Working Paper 12362.
    https://www.nber.org/papers/w12362 [high]

11. Basel Committee on Banking Supervision. "Basel Framework," including CRE30, CRE32, CRE35, CRE36, RBC20, RBC30, and RBC90; current framework accessed October 1, 2026.
    https://www.bis.org/basel_framework/index.htm [high]

12. U.S. Securities and Exchange Commission. "Summary Report of Issues Identified in the Commission Staff's Examinations of Select Credit Rating Agencies." July 2008.
    https://www.sec.gov/news/studies/2008/craexamination070808.pdf [high]

13. S&P Global Ratings. "Default, Transition, and Recovery: 2025 Annual Global Corporate Default and Rating Transition Study." March 18, 2026.
    https://www.spglobal.com/ratings/en/regulatory/article/default-transition-and-recovery-2025-annual-global-corporate-default-and-rating-transition-study-s101673333 [high]

14. S&P Global Ratings. "U.S. Leveraged Finance Q4 2025 Update: Recovery Turbulence Triggered by Changing Debt Structures and Restructuring Tactics." 2026.
    https://www.spglobal.com/ratings/en/regulatory/article/us-leveraged-finance-q4-2025-update-recovery-turbulence-triggered-by-changing-debt-structures-and-restructuring-tactics-s101666426 [high]

15. Blickle, K., and Santos, J. A. C. "Private Equity and Debt Contract Enforcement: Evidence from Covenant Violations." Federal Reserve Finance and Economics Discussion Series 2023-018.
    https://www.federalreserve.gov/econres/feds/files/2023018pap.pdf [high]

16. U.S. Securities and Exchange Commission. "Removal of References to Credit Ratings From Regulation M." Release No. 34-97657, June 7, 2023.
    https://www.sec.gov/rules-regulations/2023/06/34-97657 [high]

## See Also

- `library/finance/bond-pricing-and-fixed-income-markets.md` -- credit analysis supplies the default and recovery components of bond valuation.
- `library/finance/financial-statement-analysis.md` -- statements and cash-flow reconciliations provide core borrower evidence.
- `library/finance/capital-structure-modigliani-miller.md` -- leverage and claim priority determine how operating risk reaches creditors.
- `library/finance/banking-maturity-transformation.md` -- bank lending combines credit risk with funding and liquidity transformation.
- `library/accounting-financial-shenanigans/anchor-accounting-financial-shenanigans.md` -- manipulated reporting can corrupt ratios, models, and covenant tests.