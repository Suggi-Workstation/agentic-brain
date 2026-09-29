---
name: liability-driven-investing
id: 20260929T023358Z
tier: library-topic
domain: portfolio-risk-management
author: Librarian
tags: [liability-driven-investing, asset-liability-management, duration-hedging, inflation-hedging, collateral-liquidity, pension-risk, insurance-portfolios]
links: [library/portfolio-risk-management/portfolio-stress-testing-and-scenario-analysis.md, library/portfolio-risk-management/hedge-fund-risk-management.md, library/investment-vehicles-fund-structures/fund-liquidity-design-redemption-terms-asset-liquidity-and-forced-selling-risk.md]
---

# Liability-Driven Investing Makes Obligations the Portfolio Benchmark, but Leverage Turns Hedging Into Liquidity Risk

Liability-driven investing, or LDI, constructs a portfolio around the timing, sensitivity, and uncertainty of future obligations rather than judging assets against an asset-only benchmark. This change can make pension and insurance funding more stable, but derivatives and borrowing can convert an effective long-horizon hedge into an immediate collateral and liquidity problem unless leverage, cash, and governance are designed as one system [1][3][6][7].

## Background

A conventional asset-only portfolio asks how much return its holdings may earn and how volatile those returns may be. An institution with promised future payments has a different problem: assets are useful only insofar as they support benefits, claims, expenses, or other obligations when due. The economically relevant balance is therefore assets minus liabilities, and the relevant risk is deterioration in funded status or inability to make payments, not asset volatility by itself. OECD guidance accordingly states that pension investment objectives should reflect the retirement-income objective and liability characteristics, and that assets and liabilities should be managed coherently through techniques including maturity, duration, and currency matching [4].

Defined-benefit pension liabilities are streams of projected payments extending across many years. Their present value changes when the discount curve changes, while benefit formulas may also expose the stream to inflation, salary growth, longevity, and member behavior [3]. Insurance liabilities create a related asset-liability management problem: life and annuity obligations can be exceptionally long-dated, cash-flow estimates can change, and the assets backing them must remain sufficient across relevant states [6][7]. The liability is therefore not a fixed number. It is a model-generated value and cash-flow schedule whose sensitivities depend on assumptions, valuation rules, and the obligations themselves.

LDI emerged from asset-liability management as a way to make those sensitivities the reference portfolio. The Society of Actuaries describes liability hedging as designing asset movements to offset major liability risks, either fully or partially [3]. The Pensions Regulator similarly defines matching assets as holdings intended to reduce funding-level volatility, prepare for a liability transaction, generate cash flows near benefit outflows, or match long-term scheme cash flows [2]. Under this framework, a long bond may be less risky than cash even though its market price is more volatile, because its value can move in the same direction as a long-duration liability when yields change.

The simplest ideal is cash-flow dedication: hold assets whose contractual payments match the amount, currency, and date of each obligation. Exact dedication is often unavailable or expensive because liability cash flows are uncertain, suitable bonds may be scarce, and institutions may be underfunded. Duration matching offers a less exact alternative by aligning the first-order sensitivity of asset and liability values to interest-rate changes. Convexity and key-rate duration extend the hedge to curvature and nonparallel yield-curve movements, while inflation-linked bonds and inflation swaps can address benefits linked to prices [3][5]. These tools reduce selected risks; they do not eliminate uncertainty in mortality, salary growth, credit spreads, basis relationships, or future benefit experience.

An underfunded institution also faces a return problem. Investing every asset in a low-risk matching portfolio may stabilize funded status but lock in an existing deficit or require larger sponsor contributions. Many LDI programs therefore divide capital conceptually between a liability-hedging portfolio and a return-seeking portfolio. The hedging sleeve targets interest-rate, inflation, currency, and cash-flow sensitivities. The return-seeking sleeve holds equities, credit, private assets, or other exposures intended to close a deficit, reduce contribution needs, or create surplus. Academic LDI research describes this as a risk-budget choice: greater risk aversion produces more investment in the liability-hedging portfolio, lower extreme funding risk, and lower expected performance [5].

Derivatives and repurchase agreements made that division easier to implement. Interest-rate swaps, inflation swaps, gilt repos, futures, and swaptions can supply substantial liability sensitivity for less initial cash than an outright long-bond purchase [1][2][7][9]. The remaining capital can then support return-seeking assets. This arrangement is not free. Derivatives require collateral, repos create financing and rollover exposure, and market moves can generate cash demands long before liabilities are paid. The Pensions Regulator explicitly distinguishes leveraged and unleveraged LDI and states that leveraged arrangements increase allocation through instruments that require collateral as security [1].

The September 2022 UK gilt episode made that hidden clock visible. Rapid increases in long-dated gilt yields reduced the value of leveraged LDI positions and triggered collateral or margin calls. When pooled funds and pension clients could not transfer cash quickly enough, funds sold gilts to reduce leverage; those sales added pressure to gilt prices and yields, generating further calls [8][9][10]. The Bank of England intervened because the feedback threatened market functioning, not because the basic objective of matching pension assets to liabilities had suddenly become invalid [8]. The episode therefore distinguishes LDI as an asset-liability discipline from one fragile implementation: leveraged, liquidity-constrained, and operationally slow pooled structures.

This distinction sets the scope of the topic. LDI is portfolio construction organized around obligations. It includes physical matching assets, derivatives, collateral, liquidity reserves, and return-seeking assets. It can be used by pension schemes and insurers and can be leveraged or unleveraged [1][6][7]. Leveraged pooled UK pension funds are an important case, but treating that case as the definition of LDI would confuse a broad risk-management objective with one vehicle, financing method, and crisis mechanism.

## Core Concepts

### The liability is the benchmark

LDI begins by specifying the obligation rather than choosing assets first. The specification includes projected payments, timing, currency, inflation linkage, contingent options, discount basis, and uncertainty. For a defined-benefit pension, relevant uncertainty can include longevity, salary growth, member retirement, benefit commutation, and sponsor contributions. For an insurer, lapse behavior, guarantees, claims development, and policyholder options can alter both timing and amount [3][6][7]. The benchmark is therefore a modeled liability portfolio: a representation of how the present value and cash flows of the obligations respond to relevant risk factors.

A funded-status measure compares assets with this liability value. A scheme can report a positive asset return while its funding position worsens if falling discount rates increase the liability by more than the assets rise. Conversely, rising rates can reduce the present value of liabilities by more than assets decline, improving economic solvency even while leveraged hedge positions require cash [3][10]. This separation between economic value and immediate liquidity is fundamental. The institution can be better funded in present-value terms and still face a near-term collateral emergency.

The liability benchmark depends on the purpose and valuation basis. A pension may track technical-provisions liabilities, accounting liabilities, buyout pricing, or a cash-flow objective; these are not identical. Corporate-bond discounting creates spread sensitivity different from government-bond discounting, while inflation caps and floors create nonlinear exposure. The author's synthesis is that trustees should not request a generic percentage hedge without first stating which liability measure, risk factors, and decision horizon the percentage refers to. Otherwise, an apparently precise hedge ratio can target the wrong benchmark.

### Cash-flow matching, duration, convexity, and key-rate exposure

Cash-flow matching is the closest approximation to dedication. The institution buys bonds or other contractual assets whose coupons and principal correspond to expected payments. If every payment were certain and an exactly matching default-free instrument existed, reinvestment and liquidation needs could be minimized. In practice, cash-flow uncertainty and missing maturities make exact matching incomplete, so institutions combine dedication over nearer horizons with sensitivity matching over longer horizons [2][3].

Duration measures the first-order percentage change in value for a small yield change. Matching asset and liability duration reduces the effect of a small parallel shift in the discount curve. Dollar duration, rather than duration alone, is required because equal percentage sensitivity on unequal asset and liability values does not produce equal value changes. Convexity describes how duration changes as yields move and matters for larger shifts. The Society of Actuaries also emphasizes key-rate duration because equal aggregate duration and convexity do not protect against twists or other nonparallel curve movements [3].

These metrics are approximations, not guarantees. Duration is local to a yield level and assumed movement. Liability cash flows can change with inflation or behavior, corporate-bond and government curves can move differently, and the hedge may have option-like terms. IAIS guidance notes that duration and convexity can be used to immunize assets and liabilities from interest-rate fluctuations, while also placing them among a wider set of ALM measurement tools rather than treating them as complete protection [7]. The hedge should therefore be monitored and rebalanced as yields, cash flows, and funding status change.

### Inflation, currency, credit, and basis risk

Nominal duration does not hedge a benefit linked to inflation. Inflation-linked government bonds can supply real-rate and inflation exposure, while inflation swaps can more precisely tailor tenor and index sensitivity [2][3][5][9]. The New York Fed-hosted research by Amenc, Martellini, and Ziemann describes customized liability-hedging portfolios using inflation-protected securities and over-the-counter inflation derivatives suited to the institution's liability profile [5]. EIOPA reports that insurers use derivatives in matching portfolios to manage interest-rate, foreign-exchange, and inflation risks [6].

A hedge can still fail through basis risk. The liability may use one inflation index while the available bond or swap references another; benefit caps and lags may differ from traded contracts; the accounting discount curve may move differently from sovereign yields; or corporate bonds may introduce credit-spread exposure that does not mirror the obligation. Currency mismatch creates another layer when assets and payments are denominated differently. OECD guidance identifies currency alongside maturity and duration as a characteristic that should be considered in asset-liability matching [4]. The correct question is not whether an instrument is conventionally called a hedge but which liability sensitivity it actually offsets and what residual basis remains.

### Physical matching and derivative overlays

Physical LDI holds fixed or index-linked government bonds, high-quality corporate bonds, and potentially long-dated contractual assets whose cash flows or price sensitivities resemble liabilities [2][3]. The advantages are transparency, direct ownership, and absence of daily derivative margin on the physical holding. Limits include shortage of sufficiently long maturities, imperfect cash-flow shapes, credit exposure, and the capital required to obtain enough duration.

A derivative overlay uses interest-rate swaps, inflation swaps, futures, options, swaptions, or repo-financed bonds to add sensitivity without committing the full cash value of the exposure [1][2][7][9]. This capital efficiency lets the institution retain return-seeking holdings. It also creates multiple notions of exposure: invested capital, notional hedge exposure, sensitivity, and potential collateral need. Leverage should be measured against the economic sensitivity created and the liquid resources available, not only against accounting assets.

Repo and swaps create different cash-flow paths. A repo finances a bond against collateral and must be rolled or repaid. A cleared or bilateral swap exchanges fixed and floating or inflation-linked payments and can require variation margin when its value changes. Both can be sound hedging instruments, but neither eliminates financing risk. The author's synthesis is that leverage is best understood as borrowing future liquidity to obtain present sensitivity. The hedge remains viable only if the institution can supply that liquidity through the adverse path.

### Hedge ratio and capital allocation

The hedge ratio compares the asset sensitivity with the liability sensitivity for a specified risk. A 100 percent interest-rate hedge seeks equal and opposite value changes for the selected curve movement; a partial hedge deliberately leaves exposure. The appropriate ratio depends on funding status, sponsor capacity, liability uncertainty, collateral resources, and the expected return required from the remaining assets [1][3][5]. A higher ratio can reduce funded-status volatility while increasing collateral needs when implemented with leverage.

The return-seeking allocation is not outside the LDI framework. It represents a deliberate decision to accept asset risk relative to the liability benchmark. Equities may help close a deficit over time but can fall when liquidity is needed. Private assets may offer return or cash-flow characteristics but cannot reliably meet a short margin call. Credit may supply spread and duration, yet its market liquidity and default risk can deteriorate together. The useful portfolio map therefore separates each holding's role: liability hedge, return generator, collateral reserve, benefit-payment reserve, or contingent liquidity source. One asset should not be counted at full value in several roles simultaneously.

A dynamic de-risking path can move capital from return-seeking assets to matching assets as funding improves. Such a rule locks in gains in funded status rather than preserving the same risk indefinitely. It also depends on measurement and execution: the trigger, valuation basis, rebalancing band, market capacity, and governance authority must be specified before the funding threshold is crossed. The author's assessment is that a glide path is only as reliable as the liquidity and decision process that can execute it.

### Collateral and liquidity form a second balance sheet

A long-term liability schedule and a derivative margin schedule operate on different clocks. Pension benefits may be paid over decades, while variation margin can be due daily or intraday. LDI resilience therefore requires a collateral waterfall: immediately available cash, eligible liquid collateral, assets that can be converted within the call period, and slower assets that should not be assumed available [1][11]. The waterfall must be net of assets already pledged, settlement delays, haircuts, transaction costs, and other competing cash needs.

The collateral buffer is the yield or market move that the arrangement can absorb before its liquid resources are exhausted. A buffer is necessary but not sufficient. The FCA states that LDI liquidity should withstand severe but plausible gilt stress, meet margin and collateral calls without adding to market stress, and cover foreseeable demands [11]. Operational speed matters because a large theoretical pool of assets does not meet a call if trustees, custodians, managers, and counterparties cannot transfer or sell them in time.

Liquidity should be tested at the whole-scheme level and at the legal vehicle that receives the call. A pension may own enough liquid assets in aggregate while a pooled LDI fund lacks authority or operational access to them. Assets can also be encumbered or held in vehicles with different dealing terms. The 2022 evidence shows why legal segmentation and transfer frictions matter as much as consolidated solvency [10][12]. A robust program specifies who can issue a call, who authorizes payment, which assets are eligible, how long transfer takes, and what happens if the first source is unavailable.

### Pooled and segregated implementation

A segregated mandate serves one institution and can be tailored to its liability profile, collateral pool, and governance. A pooled fund aggregates schemes, making sophisticated hedging accessible to smaller investors. Pooling can reduce unit costs but introduces standard hedge terms, fund-level dealing rules, collective recapitalization, and coordination among clients [1][10][12]. The institution must understand both its own resources and the pooled vehicle's threshold for deleveraging.

The 2022 crisis does not prove that pooling is inherently unsound. It demonstrates that pooled structures require credible ex ante rules for buffers, capital calls, defaulting participants, dealing frequency, communication, and forced deleveraging. The FCA notes that some pooled clients might have benefited from greater operational flexibility while also recognizing reasons schemes may continue to prefer pooled funds [11]. Vehicle choice is therefore part of risk design, not a minor implementation detail.

### Governance, model risk, and the irreducible remainder

LDI depends on models of cash flows, discount curves, inflation linkage, option behavior, hedge effectiveness, and market liquidity. Those inputs can be wrong together. Governance should assign ownership for the liability model, hedge mandate, collateral policy, stress tests, counterparty limits, and emergency decisions. The OECD prudent-person framework places investment policy and integrated asset-liability risk management under the governing body's responsibility [4]. TPR guidance similarly emphasizes strategy, collateral resilience, governance, and monitoring [1].

No hedge removes every liability risk. Longevity can change the amount and duration of pension payments; sponsor credit can weaken; benefit rules can change; inflation caps create nonlinearities; and the traded hedge can diverge from the valuation basis. The author's synthesis is that LDI should be judged by transparent reduction of specified risks, not by a claim that obligations are fully immunized. Residual risk, hedge cost, liquidity usage, and conditions for failure belong in the mandate alongside the target hedge ratio.

## Evidence

The evidence for LDI begins with established asset-liability mechanics rather than with the 2022 crisis. The Society of Actuaries' benchmark model formalizes duration, convexity, key-rate duration, cash-flow matching, inflation-linked assets, and liability-replicating portfolios as complementary tools. Its examples show why an asset portfolio with shorter duration than the liability can experience improving asset value yet worsening funded status after a yield decline [3]. This is model evidence: it demonstrates the transmission mechanism under stated cash flows and yield changes, not a universal optimal allocation. The model also separates value sensitivity from payment liquidity, preventing an interest-rate hedge from being mistaken for a complete cash-flow plan [3].

The Pensions Regulator provides institutional evidence about implementation. Its matching-assets guidance identifies physical assets including fixed and index-linked gilts and corporate bonds, while noting that swaps and repos can match liability characteristics more closely. Its worked example distinguishes fixed and inflation-linked liabilities with longer durations than the existing asset portfolio and notes that derivatives and leverage require collateral management [2]. The leveraged-LDI guidance then connects the hedge decision to expected return, cash calls, liquidity, strategic asset allocation, governance, and monitoring [1]. These documents are regulatory guidance, not controlled performance studies, but they verify that liability matching and collateral resilience are joint fiduciary concerns.

Evidence from insurance broadens the mechanism beyond UK pensions. EIOPA's survey of insurer asset-liability management reports that average liability duration affects investment decisions and that derivatives in UK matching portfolios manage interest-rate, foreign-exchange, and inflation risks [6]. IAIS describes duration and convexity matching, cash-flow analysis, scenario testing, and derivatives as tools for managing insurer asset-liability mismatches [7]. The cross-sector evidence supports the core claim that obligation-sensitive portfolio construction is not synonymous with leveraged pension funds. It is a general balance-sheet discipline whose instruments and constraints differ by institution.

The academic inflation evidence also shows why nominal bonds alone may be inadequate. Amenc, Martellini, and Ziemann examine a liability-hedging portfolio customized to inflation-sensitive obligations and describe TIPS and inflation swaps as instruments for matching institutional liability profiles. Their model treats the liability return through a long-duration inflation-linked instrument and analyzes the division of the risk budget between hedging and performance assets [5]. The study's assumptions about liability indexation and market dynamics limit direct translation to every plan, but its structure makes inflation sensitivity and horizon explicit.

The September 2022 UK episode provides event evidence about leverage and liquidity. The FCA records that the 30-year nominal gilt yield rose 160 basis points in four days. The repricing generated collateral demands, while earlier recapitalization calls had already reduced some investors' liquid holdings. LDI managers then faced difficulty restoring buffers rapidly enough [11]. The Bank of England's Financial Stability Report describes the result as a spiral of collateral calls and forced gilt sales that threatened market functioning and required temporary long-dated gilt purchases [8].

The Bank's transaction-based working paper traces the channel through repo and derivatives. It finds that LDI-pension-insurance firms with larger pre-crisis repo and swap exposure sold more gilts during the crisis, and that selling was concentrated among a few institutions [9]. This result links prior financing positions to observed sales rather than inferring the mechanism only from aggregate yields. It does not imply that every LDI user sold or that liability matching itself caused the initiating fiscal shock. It identifies leveraged balance sheets and collateral needs as amplifiers after yields began rising.

The BIS comparison separates pension solvency from LDI-fund liquidity. It reports that higher rates could improve the pension sector's net worth because the present value of incompletely hedged liabilities fell more than assets, even as the leveraged LDI vehicles faced losses and margin calls. It also contrasts slow pooled-fund recapitalization in the UK with other systems that relied less on pooled leverage or had more direct access to fund-wide liquidity [10]. The evidence rejects the simple statement that pension promises became insolvent because gilt yields rose. The immediate failure mechanism was cash and leverage inside the hedging implementation.

Alfaro, Hong, Kim, and Li use detailed trade-level data covering gilt, repo, and derivative markets to estimate the fire-sale effect. Their BIS working paper finds that forced LDI sales caused price discounts on the order of 10 percent and accounted for roughly half of the total gilt-price decline during the crisis. Pooled LDI funds sold more and reduced repo borrowing more aggressively than single-client structures because balance-sheet segmentation, operational delays, and coordination problems slowed capital transfers [12]. The study supplies direct evidence that vehicle architecture and recapitalization frictions can transform a hedge adjustment into market-wide price pressure.

The combined evidence supports four bounded findings. First, matching duration, inflation, currency, and cash flows can reduce asset-liability risk [2][3][4][5][6][7]. Second, derivatives and repo can obtain that hedge more capital-efficiently but create collateral and financing obligations [1][9][10]. Third, aggregate solvency does not guarantee legal-entity liquidity or operational access to cash [10][12]. Fourth, the 2022 UK crisis was an implementation failure concentrated in leveraged structures, not evidence that all liability-aware investing is defective [8][9][10][11][12].

Important limitations remain. Duration and inflation hedges depend on the chosen liability valuation, and the literature does not provide one hedge ratio suitable for every pension or insurer. Crisis estimates come from one market structure, policy regime, and event. Regulatory buffers can reduce vulnerability but cannot make every extreme move harmless, as the FCA explicitly cautions [11]. The author's synthesis is that evidence justifies LDI as a framework for defining risk relative to obligations, while the safety of any program must be demonstrated through its specific instruments, leverage, collateral, legal structure, and governance.

## Implications

For pension trustees, the first implication is to begin with the benefit schedule and funding objective. Trustees should identify fixed and inflation-linked cash flows, relevant valuation bases, liability duration by curve segment, uncertainty in demographic assumptions, and near-term benefit payments. They should then decide which risks to hedge, how closely, and for what purpose: stabilize technical-provisions funding, prepare for a buyout, secure cash flows, or reduce sponsor contribution volatility [1][2]. A single headline hedge ratio without this decision context is not a complete policy.

The second implication is to separate the hedge portfolio from the collateral system even when the same assets support both. The hedge portfolio is designed to move with liabilities over time. The collateral system must supply eligible assets by specific deadlines. Trustees should map a daily or otherwise decision-relevant liquidity ladder that includes margin, repo maturity, benefit payments, expenses, and other hedges. Resources should be counted after haircuts and encumbrance, and assets whose sale depends on normal market depth should be stressed for delay and price impact [1][11].

A practical design can proceed in eight stages. First, define the liability benchmark and its interest-rate, inflation, currency, and cash-flow sensitivities. Second, measure current asset sensitivities on the same basis. Third, select a hedge ratio and identify the residual risk accepted. Fourth, choose physical assets and derivative overlays, recording basis and counterparty risk. Fifth, size the return-seeking allocation from the funding objective and sponsor capacity rather than from an asset-only return target. Sixth, construct collateral waterfalls at both scheme and vehicle levels. Seventh, stress the market, liquidity, and operational path together. Eighth, assign decision rights and rehearse recapitalization and deleveraging. This is the author's synthesis of the institutional frameworks rather than a separate regulatory formula [1][2][3][4][11].

Stress tests should invert the 2022 failure mechanism. Instead of asking only how much funded status changes after a yield shock, the test should ask which entity receives a call, how much eligible collateral it has at each hour or day, which transfers require approval, what can be sold without destabilizing the hedge, and when mandatory deleveraging occurs. Scenarios should include parallel and nonparallel rate moves, real-yield and inflation changes, wider repo haircuts, swap margin, loss of one counterparty, slower asset settlement, and simultaneous stress in return-seeking assets [3][9][11][12]. The worst credible outcome is a sound long-term hedge forced to unwind because its short-term funding path was not financed.

For insurers, LDI should remain integrated with product design, policyholder behavior, and solvency constraints. Long-duration insurance cash flows can be matched with bonds and derivatives, but lapse options, guarantees, mortality, and claim uncertainty make exact replication impossible [6][7]. An insurer should test economic surplus, accounting effects, liquidity, and regulatory capital separately rather than assume one duration number controls all four. EIOPA's evidence that insurers use derivatives for interest-rate, currency, and inflation management supports the applicability of the framework, while IAIS guidance confirms that hedging reduces but does not transfer away every original risk [6][7].

For asset managers, product design must reflect the operational capabilities of clients. A pooled LDI fund serving many smaller schemes should not assume that every investor can approve and transfer cash at the speed of a dealer margin call. Capital-call thresholds, notice channels, accepted collateral, dealing rules, default consequences, and automatic deleveraging should be explicit. Managers should also disclose how client actions interact: whether one participant's delay changes the risk borne by others and whether fund-level sales occur before all clients can respond [10][11][12]. The appropriate buffer depends not only on modeled yield moves but on this response time.

For investment committees, return-seeking assets should be evaluated by their contribution to the liability objective and by their availability in stress. A private asset may offer attractive expected return but little collateral value. Corporate bonds may contribute duration and spread return yet become less liquid when spreads widen. Equities may help close a deficit but can fall during a cash call. The portfolio report should therefore show each asset's expected return, liability-hedge contribution, stress loss, liquidation horizon, collateral eligibility, and competing uses. The author's assessment is that capital efficiency should be measured net of the liquidity reserve required to keep the hedge intact.

The 2022 episode also changes how leverage should be discussed. Leverage was not inherently irrational: it allowed schemes to hedge long-duration liabilities while retaining assets intended to earn return [1][9][10]. The failure arose when the cash and governance capacity supporting that leverage was insufficient for the speed and scale of the move. A responsible leverage limit should therefore be derived backward from stressed collateral, market depth, and operational response, not forward from a normal-period volatility estimate. If the scheme cannot or will not maintain the required liquid resources, TPR guidance says it should reconsider the balance of hedging, funding, and liquidity [1].

For policymakers, the unit of supervision should include the chain linking pension trustees, consultants, pooled vehicles, asset managers, custodians, counterparties, and core markets. Each entity may appear solvent while their combined timing assumptions create a feedback loop. The Bank, BIS, FCA, and trade-level evidence all show that legal segregation, concentrated positioning, slow recapitalization, and forced selling can turn institution-specific liquidity problems into market dysfunction [8][9][10][11][12]. Better data, cross-border coordination, and minimum resilience standards address this chain more directly than banning LDI as a category.

LDI also clarifies a broader portfolio principle for long-horizon investors: risk is relative to what the capital must accomplish. Cash is low-volatility in nominal terms but can be high-risk against a long real liability. A long bond can be volatile in isolation yet stabilizing against a duration-matched obligation. A high-return asset can improve expected funding while increasing the probability of needing contributions at a bad time. The correct benchmark changes the ranking of assets because it changes the definition of loss [2][3][4].

The framework should not be used to claim false precision. Liability projections, discount curves, inflation relationships, liquidity estimates, and correlations are all uncertain. A robust program uses ranges, key-rate measures, scenario analysis, and explicit residual-risk budgets. It preserves spare liquidity, diversification of counterparties and collateral, and reversible responses before relying on an optimized hedge. The author's synthesis is that the purpose of LDI is not to engineer a perfect match; it is to make the unavoidable mismatches visible, intentional, funded, and governable.

The final implication is semantic but consequential. LDI should not be equated with the leveraged pooled funds involved in the 2022 gilt crisis. Physical cash-flow matching, unleveraged long bonds, insurer ALM, segregated overlays, and pooled derivative funds all sit within the liability-driven family [1][2][6][7]. The useful distinction is between the objective and the implementation. The objective is to organize capital around obligations. The implementation is safe only when hedge effectiveness, return needs, leverage, collateral, liquidity, basis risk, and decision speed remain consistent under the same adverse scenario.

## Sources

1. The Pensions Regulator. (2023, subsequently updated). "Using leveraged
   liability-driven investment."
   https://www.thepensionsregulator.gov.uk/en/document-library/scheme-management-detailed-guidance/funding-and-investment-detailed-guidance/liability-driven-investment [high]

2. The Pensions Regulator. "Matching DB assets."
   https://www.thepensionsregulator.gov.uk/en/document-library/scheme-management-detailed-guidance/funding-and-investment-detailed-guidance/db-investment/matching-db-assets [high]

3. Society of Actuaries. (2019). "Liability-Driven Investment - Benchmark
   Model."
   https://www.soa.org/globalassets/assets/files/resources/research-report/2019/liability-driven-investment.pdf [high]

4. Organisation for Economic Co-operation and Development. "Recommendation
   of the Council on Guidelines on Pension Fund Asset Management."
   https://legalinstruments.oecd.org/public/doc/103/103.en.pdf [high]

5. Amenc, N., Martellini, L. & Ziemann, V. (2009). "Inflation-Hedging
   Properties of Real Assets and Implications for Asset-Liability
   Management Decisions."
   https://www.newyorkfed.org/medialibrary/media/research/conference/2009/inflation/Amenc_Martellini_Ziemann.pdf [high]

6. European Insurance and Occupational Pensions Authority. (2019). "Report
   on Insurers Asset and Liability Management in Relation to the
   Illiquidity of Their Liabilities."
   https://www.eiopa.europa.eu/system/files/2019-12/eiopa_report_on_insurers_asset_and_liability_management_dec2019.pdf [high]

7. International Association of Insurance Supervisors. (2006). "Issues
   Paper on Asset-Liability Management."
   https://www.iais.org/uploads/2022/01/Issues_Paper_on_Asset_Liability_Management.pdf.pdf [high]

8. Bank of England. (2022). "Financial Stability Report - December 2022,"
   Section 5: The Resilience of Liability-Driven Investment Funds.
   https://www.bankofengland.co.uk/-/media/boe/files/financial-stability-report/2022/financial-stability-report-december-2022.pdf [high]

9. Pinter, G., Siriwardane, E. & Walker, D. (2023). "An Anatomy of the 2022
   Gilt Market Crisis." Bank of England Staff Working Paper No. 1019.
   https://www.bankofengland.co.uk/-/media/boe/files/working-paper/2023/an-anatomy-of-the-2022-gilt-market-crisis.pdf [high]

10. Aramonte, S. & Rungcharoenkitkul, P. (2022). "Leverage and Liquidity
    Backstops: Cues from Pension Funds and Gilt Market Disruptions." BIS
    Quarterly Review, December 2022.
    https://www.bis.org/publ/qtrpdf/r_qt2212v.htm [high]

11. Financial Conduct Authority. (2023). "Further Guidance on Enhancing
    Resilience in Liability Driven Investment."
    https://www.fca.org.uk/publications/multi-firm-reviews/further-guidance-enhancing-resilience-liability-driven-investment [high]

12. Alfaro, L., Hong, G. H., Kim, H. & Li, D. (2024). "Fire Sales of Safe
    Assets." BIS Working Papers No. 1233.
    https://www.bis.org/publ/work1233.pdf [high]

## See Also

- `library/portfolio-risk-management/portfolio-stress-testing-and-scenario-analysis.md` -- integrated market, collateral, liquidity, and governance scenarios for portfolio failure modes.
- `library/portfolio-risk-management/hedge-fund-risk-management.md` -- leverage, financing liquidity, counterparty exposure, and forced-sale controls that also govern leveraged LDI.
- `library/investment-vehicles-fund-structures/fund-liquidity-design-redemption-terms-asset-liquidity-and-forced-selling-risk.md` -- the vehicle-level timing and legal constraints that distinguish pooled liquidity from aggregate investor resources.
