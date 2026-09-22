---
name: banking-maturity-transformation
id: 20260726T213149Z
tier: library-topic
domain: finance
author: Researcher-1
tags: [banking, maturity-transformation, bank-runs, capital-adequacy, basel-iii, liquidity-risk, shadow-banking]
links: [library/finance/bond-pricing-and-fixed-income-markets.md, library/finance/financial-statement-analysis.md]
reviewed: 2026-09-22
---

# Banking -- Maturity Transformation Creates Useful Credit and Runnable Balance Sheets

Banks create economic value by funding longer-term loans and securities with deposits and other liabilities that are payable sooner. The same maturity and liquidity transformation that supplies borrowers with committed credit gives depositors a reason to run when they doubt a bank's capacity to pay, so sound banking requires capital, liquidity, stable funding, operational readiness, and confidence rather than any one ratio in isolation ([1] [2] [7]).

## Background

English banking before 1694 was concentrated among London goldsmiths. By the second half of the seventeenth century, goldsmiths were not merely safeguarding money and valuables; they were also using entrusted funds to make loans. The Bank of England was founded in 1694 as a private bank and banker to the government. These institutions established the basic intermediation pattern: customers held claims that could be presented for payment, while bankers invested part of the funding in longer-lived and less immediately realizable assets ([3] [4]).

This arrangement solved a coordination problem between savers and borrowers, but periodic panics exposed its weakness. A bank could own assets whose eventual cash flows exceeded its obligations and still fail if too many obligations came due before those assets could be sold or pledged. Mid-nineteenth-century Bank of England records show that its crisis behavior broadly conformed to the rule later associated with Walter Bagehot: lend freely during a panic, generally at rates above pre-crisis levels and against eligible securities. The historical evidence varies across the crises of 1847, 1857, and 1866, so Bagehot's rule is better understood as a crisis-management principle than as an exact description of every transaction ([5]).

The United States developed a related safety architecture after repeated banking panics. The Panic of 1907 began among New York financial institutions, spread nationally and internationally, and helped produce the monetary reform movement that culminated in the Federal Reserve System. The Federal Reserve Act was signed in 1913, and the Reserve Banks opened in 1914. The system supplied a mechanism for mobilizing reserves and emergency liquidity that had been absent from the fragmented pre-Fed system ([6]).

That architecture remained incomplete. Banking panics in 1930-31 turned a recession into the opening phase of the Great Depression, while the divided member and nonmember structure limited access to reserves in many communities. The Banking Act of 1933 created federal deposit insurance, and the Federal Deposit Insurance Corporation began operations that year. In the present US framework, coverage is generally $250,000 per depositor, per insured bank, for each ownership category. Insurance covers deposits rather than stocks, bonds, mutual funds, or other investment products ([7] [8]).

International capital rules became another layer of defense. Basel I, issued in 1988, established a common risk-weighted capital framework and an 8 percent minimum total capital ratio for internationally active banks. Basel II, published in 2004, made the treatment of credit risk more sensitive to external ratings and, with supervisory approval, banks' internal estimates; it also organized supervision around minimum capital, supervisory review, and market disclosure. The global financial crisis then showed that risk-weighted capital alone did not control leverage, trading-book exposures, funding fragility, or the system-wide consequences of forced sales ([9] [10]).

Basel III responded with a higher-quality capital definition, a non-risk-based leverage backstop, capital buffers, and two liquidity standards. The core global minima include Common Equity Tier 1 equal to 4.5 percent of risk-weighted assets, a 2.5 percent capital conservation buffer above minimum requirements, and a 3 percent Tier 1 leverage ratio. The Liquidity Coverage Ratio requires high-quality liquid assets sufficient for modeled net cash outflows over 30 days, while the Net Stable Funding Ratio addresses structural funding over a longer horizon. These are international standards implemented through national law, not a single statute that applies identically to every bank ([10] [11]).

The financial crisis of 2007-09 also demonstrated that bank-like fragility exists outside insured depositories. Money market funds, securities dealers, repurchase agreements, asset-backed commercial paper vehicles, and securities-lending cash pools created short-term claims that investors treated as cash equivalents while funding longer-term or less liquid positions. When confidence fell, lenders withdrew or demanded more collateral. One study estimates that net repo financing to US banks and broker-dealers fell by about $1.3 trillion from the second quarter of 2007 to the first quarter of 2009, more than half its pre-crisis total ([12] [13]).

The 2023 turmoil joined this long history but added two modern features: highly concentrated uninsured deposits and digitally accelerated withdrawals. Silicon Valley Bank (SVB) failed after rapid growth, weak governance and risk management, large long-duration securities holdings, and an extraordinary run. Credit Suisse met applicable capital and liquidity requirements yet was driven to the brink of insolvency by a long-running loss of confidence and rapid outflows. These cases did not make maturity transformation obsolete; they showed why its risks must be assessed through the joint behavior of assets, funding, operations, regulation, and depositor incentives ([14] [15] [16]).

## Core Concepts

### Maturity, Liquidity, and Credit Transformation

Maturity transformation means financing assets whose contractual or expected cash flows arrive later than the cash flows promised to creditors. Liquidity transformation is related but distinct: it means issuing claims that can be redeemed or transferred readily while holding assets that may be costly or slow to sell. A thirty-year mortgage funded by demand deposits has both mismatches. A bank can also face liquidity transformation without a large contractual maturity gap if an asset becomes hard to sell in stress, or maturity transformation without immediate distress if funding is behaviorally stable ([1] [9]).

Credit transformation adds another layer. Deposits are contractual claims on the bank, whereas loans and securities expose the bank to borrower default and changes in market value. Equity absorbs losses before deposits do. Liquidity therefore answers whether the bank can pay on time; solvency answers whether the economic value of assets exceeds liabilities; capital measures a loss-absorbing layer under accounting and regulatory definitions. A solvent bank can be illiquid, an apparently liquid bank can be insolvent, and accounting or regulatory capital can differ from economic value because recognition and risk-weight rules differ ([11] [14]).

### The Income Mechanism and the Deposit Franchise

A bank's net interest margin is broadly the yield earned on loans and securities minus the cost of deposits and other funding, scaled by earning assets. Maturity transformation can contribute to that margin when longer-dated assets yield more than shorter-dated funding. An IMF study using Italian bank data found that greater contractual maturity transformation was generally associated with a higher net interest margin in normal times, especially with a steeper yield curve; it also found that transformation beyond the former Italian prudential limit increased risk without improving the margin ([17]).

Deposits are not mechanically equivalent to overnight wholesale borrowing. Retail deposit rates usually adjust less than one-for-one with market rates, a response summarized by the deposit beta. Banks incur branch, technology, service, compliance, and marketing costs to acquire and retain these balances. Drechsler, Savov, and Schnabl model the resulting franchise as funding whose total cost can behave more like long-term fixed-rate debt than its legal maturity suggests, and they document that banks with less rate-sensitive deposits hold longer-duration assets ([18]).

That hedge is neither universal nor riskless. Later work argues that fixed-rate lending spreads and operating costs can offset the supposed negative duration of a deposit franchise, leaving franchise value exposed when rates rise. A separate model treats the uninsured part of the franchise as a runnable asset: the low-cost funding has value only while deposits remain, and a run destroys that value. The synthesis is that legal maturity, rate sensitivity, withdrawal behavior, and franchise value are different dimensions; treating all deposits as stable because they were stable historically is a modeling error ([19] [20]).

### Duration and Repricing Risk

Interest rate risk arises because asset and liability cash flows reprice at different speeds and because changes in discount rates change present values. A fixed-rate bond loses market value when rates rise. A floating-rate loan may reprice quickly but can create credit stress for its borrower. Noninterest-bearing deposits may preserve current income when market rates rise, yet the bank can lose balances to money market funds, Treasury bills, or competitors unless it raises deposit rates ([18] [19]).

Accounting categories do not eliminate economic losses. Available-for-sale securities generally reflect changes in fair value in accumulated other comprehensive income, subject to the applicable accounting and regulatory-capital rules. Held-to-maturity treatment avoids recurring fair-value recognition in earnings when the criteria are met, but the cash flows remain fixed and the securities still lose economic value when rates rise. If withdrawals force a bank to sell assets, previously unrealized losses can become realized and can weaken both capital and confidence. Managers therefore need both earnings-at-risk analysis, which focuses on near-term income, and economic-value sensitivity, which focuses on the present value of longer-lived positions ([14] [15]).

### The Diamond-Dybvig Coordination Problem

Diamond and Dybvig formalized why useful liquidity creation can produce runs. In their three-period model, an intermediary invests in a long-term technology that pays more if held to maturity but yields less if liquidated early. Depositors do not initially know who will need early consumption. By pooling funds and promising withdrawals, the bank improves risk sharing compared with isolated investors ([1] [2]).

The same contract can support more than one equilibrium. If only depositors with early needs withdraw, long-term investment remains intact. If depositors expect others to withdraw first, even those able to wait have an incentive to join because assets may be exhausted before their claims are served. A run can therefore be self-fulfilling rather than a simple verdict that loan losses already exceeded capital. Deposit insurance can remove the insured depositor's incentive to run, while a lender of last resort can convert eligible collateral into cash; neither tool makes bad assets good or removes the need for supervision ([1] [2] [5]).

### Capital, Liquidity, and Stable-Funding Safeguards

Capital requirements constrain the share of losses borne before creditors. Basel III's risk-based ratios weight exposures by regulatory measures of risk, while the leverage ratio supplies a non-risk-based backstop. Buffers above the minimum can absorb stress and, when breached, constrain distributions. Capital is essential for solvency and confidence, but it is not a vault of cash: a bank can report capital above its requirement while lacking operationally available funds for a sudden run ([10] [11] [14]).

The LCR and NSFR address different horizons. The LCR compares qualifying liquid assets with modeled net outflows during a 30-day stress period. The NSFR compares available stable funding with the amount required by the liquidity characteristics and maturities of assets and off-balance-sheet exposures. Both improve discipline, but both depend on assumptions about outflow rates, asset monetization, legal entities, and scope of application. The Basel Committee's 2023 and 2024 reviews emphasized that observed outflow speeds, digital access, and the treatment of interest rate risk and held-to-maturity assets merit continued attention ([11] [16]).

### Insurance, Emergency Liquidity, and Moral Hazard

Deposit insurance protects eligible depositors and reduces the coordination motive behind retail runs. In the United States, the Deposit Insurance Fund is financed principally by assessments on insured institutions and income on its investments; the FDIC states that no depositor has lost insured funds since the agency was created. Coverage is limited by institution and ownership category, so a large operating account can remain substantially uninsured ([8]).

Emergency central bank lending addresses timing rather than ultimate asset quality. A prepared bank can pre-position collateral, test its ability to borrow, maintain settlement access, and diversify contingent sources. SVB had limited collateral pledged to the discount window, had not completed test transactions, and could not move securities quickly enough from custodians and other lenders during its run. The Federal Reserve concluded that better operational capacity probably would not have prevented failure, given the scale of outflows, but the deficiency still reduced available options ([14]).

Insurance and central bank access also alter incentives. Protection can reduce monitoring by depositors, and anticipated public support can encourage banks or investors to take more risk. Regulation, risk-based insurance assessments, resolution planning, management accountability, and losses for shareholders and eligible creditors are intended to contain this moral hazard. The design problem is therefore not to choose between stability and discipline, but to provide credible liquidity protection while preserving consequences for unsafe risk taking ([1] [8] [16]).

### Shadow Banking Is the Same Function under Different Contracts

Shadow banking performs credit, maturity, and liquidity transformation through securities rather than insured deposits. A money market fund offers redeemable shares; a dealer finances inventories with repo; a securitization vehicle funds longer-dated assets with short-term paper. These claims can appear cash-like in normal conditions but lack the same combination of deposit insurance, routine central bank access, capital rules, and supervision as banks ([12] [13]).

Runs in this system occur through redemptions, refusal to roll funding, larger haircuts, or collateral calls. In 2008, the Reserve Primary Fund's losses were followed by nearly $200 billion of withdrawals from prime money market funds in two days, and official insurance and liquidity facilities helped stop the run. In March 2020, the Federal Reserve again created facilities for money market funds, commercial paper, and primary dealers; its later financial-stability review said Federal Reserve action was required to slow redemptions and restore short-term funding-market functioning ([13] [21]).

## Evidence

### Profitability and the Limits of More Transformation

Bologna's IMF study constructed a contractual maturity-mismatch measure for Italian banks and related it to net interest margin, balance-sheet composition, and the removal of a prudential limit that had operated from 1993 to 2005. The estimated relationship was not simply "more mismatch is always better." Higher transformation was associated with higher margins in ordinary ranges, while transformation above the former limit increased interest-rate exposure without a corresponding margin benefit. This supports a risk-reward interpretation rather than the claim that maturity mismatch mechanically creates profit ([17]).

Drechsler, Savov, and Schnabl reach a complementary result from US evidence: deposit-rate stickiness and the fixed operating costs of maintaining a franchise can make long assets a cash-flow hedge for deposit expenses. DeMarzo, Krishnamurthy, and Nagel challenge the stronger valuation claim, estimating that franchise value can fall as rates rise once fixed-rate lending spreads and operating costs are modeled. Together, these studies show that a bank's risk cannot be inferred from the contractual maturity table alone; the answer changes with the empirical behavior of deposit rates, deposit outflows, asset coupons, costs, and capitalization ([18] [19]).

### Credit Booms and Crisis Severity

Schularick and Taylor assembled long-run data for 14 advanced economies from 1870 through 2008 and found that credit growth is a powerful predictor of financial crises. Jorda, Schularick, and Taylor examined more than 200 recession episodes over the same broad historical span and found that financial-crisis recessions were more costly than normal recessions and that credit-intensive expansions were followed by deeper recessions and slower recoveries. These studies concern system-wide leverage rather than a single bank's liquidity, but they document why maturity transformation becomes more dangerous when many institutions expand balance sheets together ([22] [23]).

The mechanism is amplification. Credit growth raises the quantity of claims whose safety depends on borrower performance, collateral values, and continued funding. When losses or funding pressure force several intermediaries to shrink at once, asset sales depress prices and tighter lending weakens borrowers, producing feedback between market liquidity, credit losses, and the real economy. This paragraph is a synthesis of the historical findings and the balance-sheet mechanisms documented in the cited studies ([16] [22] [23]).

### Runs beyond Deposits in 2008 and 2020

Gorton and Metrick combined official data with a market survey to examine the 2007-09 repo contraction. They estimated that net repo funding to US banks and broker-dealers fell by approximately $1.3 trillion from 2007:Q2 to 2009:Q1 and found that foreign financial institutions, hedge funds, and other unregulated cash pools drove much of the withdrawal. The finding matters because data confined to regulated institutions would miss important runnable funding providers ([12]).

Money market funds provide a second case. After the Reserve Primary Fund failed to maintain its stable net asset value in September 2008, nearly $200 billion left prime funds in two days and official support helped stabilize the market. In March 2020, redemptions and market dysfunction again led the Federal Reserve to create the Money Market Mutual Fund Liquidity Facility and other emergency facilities. The repeated pattern supports a functional test: if an intermediary promises near-money claims while holding assets that cannot be sold at par in stress, it performs bank-like liquidity transformation regardless of its legal label ([13] [21]).

### Silicon Valley Bank: Several Risks, Not One Cause

SVB combined rapid balance-sheet growth with concentrated technology and venture-capital customers, a very high uninsured-deposit share, long-maturity securities, and deficient governance, liquidity, and interest-rate risk management. At year-end 2022, approximately 94 percent of SVB Financial Group deposits were uninsured. On March 8, 2023, the company announced that it had sold about $21 billion of available-for-sale securities for a $1.8 billion after-tax loss and planned a $2.25 billion capital raise ([14] [15]).

On March 9, customers withdrew about $42 billion, roughly 25 percent of the bank's approximately $166 billion of deposits, and requests for the following day totaled another $100 billion. Regulators closed the bank on March 10. The Federal Reserve's review attributed the failure to management, supervisory, and regulatory weaknesses; its counterfactual estimates indicated that under the pre-2019 regime SVB Financial Group would have faced the full LCR, with an estimated ratio of about 91 percent in December 2022 and 83 percent in February 2023, below the 100 percent requirement. Its estimated NSFR would have remained above 100 percent, demonstrating that one favorable liquidity ratio would not have cured every vulnerability ([14] [15]).

The original simplified account that the securities sale itself "wiped out capital" is incorrect. SVB reported regulatory capital above applicable minimums before the run, and the announced after-tax sale loss was part of a broader attempt to restructure the balance sheet and raise capital. The failure resulted from the interaction of economic losses, concentrated runnable funding, weak risk management, inadequate contingency-funding operations, ineffective communication, and an unprecedented outflow rate. Digital banking and social networks accelerated coordination, but official reviews do not treat technology as the sole cause ([14] [15] [16]).

### Credit Suisse: Compliance Did Not Preserve Confidence

Credit Suisse illustrates a different route to acute liquidity distress. FINMA traced the crisis to repeated scandals, losses, unstable strategy, governance and control weaknesses, and a prolonged erosion of market and client confidence. It reported that the group met regulatory capital requirements and continued to meet core liquidity requirements, including the NSFR, during the crisis. Nevertheless, clients withdrew CHF 138 billion of deposits in the fourth quarter of 2022, and March 2023 outflows accelerated sharply after further adverse disclosures and market events ([24]).

FINMA concluded that rapid, widespread outflows, exacerbated by digital communication, brought the bank close to insolvency despite its formal ratios. The Swiss authorities supported its merger with UBS and supplied extraordinary liquidity facilities. This case does not show that capital or liquidity rules are useless; it shows that minimum ratios are necessary constraints, not guarantees against a confidence crisis, operational friction, business-model failure, or outflows outside modeled assumptions ([24]).

### Current Condition and Implementation Status

The Basel Committee's implementation dashboard reported that, as of September 30, 2025, most member jurisdictions had published rules for the final Basel III elements, whose target effective date was January 1, 2023 with a five-year phase-in for some components. In March 2026, the Committee's oversight body welcomed further implementation progress. The United States had not simply completed a uniform 2025 phase-in: on March 19, 2026, the federal banking agencies issued new proposals, including a proposal to implement final Basel III components for the largest and most internationally active banks. A global standard, an adopted national rule, and a proposed rule are therefore different states and must not be conflated ([9] [25]).

The latest available FDIC Quarterly Banking Profile at this review date, covering 2026:Q2, reported that 4,238 insured institutions earned $90.1 billion, domestic deposits rose for an eighth consecutive quarter, and capital and liquidity remained strong in aggregate. It also reported that unrealized securities losses remained elevated and that the industry still faced weakness in certain loan portfolios. Aggregate resilience does not establish that each institution is safe; the distribution of duration, uninsured funding, credit concentration, and operational liquidity remains decisive ([26]).

## Implications

### For Bank Boards and Management

The controlling question is not whether a bank transforms maturities, but whether it can survive adverse combinations of rate moves, credit losses, and withdrawals. Asset-liability management should integrate contractual maturities, behavioral deposit assumptions, deposit betas, hedges, prepayment options, off-balance-sheet commitments, collateral requirements, and legal-entity constraints. Earnings-at-risk and economic-value measures answer different questions and should be stressed together rather than allowing a favorable near-term income result to obscure a large present-value loss ([14] [18] [19]).

Contingency funding must be executable, not a spreadsheet total. Management should identify which assets can be sold without impairing the franchise, which can be pledged, where they are held, how quickly liens can be released, whether borrowing lines are legally and operationally available, and whether test transactions have succeeded. The SVB review shows the cost of counting theoretical borrowing capacity that could not be mobilized at the required speed ([14] [15]).

Funding concentration deserves the same attention as asset concentration. A deposit base can look diverse by account count while remaining concentrated by industry, common investors, treasury advisers, geography, or communication network. Boards should examine insured shares, account sizes, depositor purpose, rate sensitivity, transfer speed, and correlated behavior under named scenarios. The relevant denominator is not merely total deposits but the amount that can leave before cash and credible contingent funding arrive ([15] [20]).

### For Regulators and Standard Setters

Capital, leverage, liquidity, interest-rate risk, and supervision are complements. Risk weights can understate duration or concentration; a leverage ratio ignores differences in asset risk; a 30-day liquidity ratio can miss outflows compressed into hours; stable-funding measures do not guarantee operational monetization; and reported compliance can coexist with weak governance. Supervisors therefore need authority, information, skilled judgment, timely escalation, and credible remediation tools in addition to rules ([11] [14] [16]).

Scope matters. The Basel framework applies internationally to internationally active banks, while jurisdictions decide how broadly to extend it. The 2023 turmoil showed that distress at institutions outside the full Basel scope can still have systemic consequences. Thresholds based mainly on size can create delayed transitions or abrupt differences in requirements even when a fast-growing bank has concentrated funding and complex risks. A risk-sensitive regime should consider growth, funding structure, business-model concentration, substitutability, and contagion channels alongside assets ([14] [16]).

Run-speed assumptions require empirical updating. This does not imply that every bank should hold cash against every deposit; doing so would largely eliminate the credit-creation function. It does imply scenario sets that include intraday and multiday withdrawals, correlated uninsured accounts, online transfer capacity, margin and collateral calls, and degradation in asset monetization. Resolution and emergency-liquidity plans should be executable at the same speed as the liabilities they are meant to stabilize ([16] [24]).

### For Bank Investors and Credit Analysts

A capital ratio is a starting point, not an investment conclusion. Analysis should reconcile regulatory capital with tangible common equity, accumulated other comprehensive income, unrealized gains and losses, credit marks, and plausible liquidation discounts. It should compare asset duration with both contractual and behavioral funding duration, and it should distinguish securities that can be pledged from those operationally trapped or already encumbered ([14] [15] [19]).

The deposit franchise should be valued as both an asset and a contingent liability. Low-rate deposits generate spread income, but that value can disappear when customers demand market rates or move balances. Relevant indicators include insured percentage, top depositor and industry concentrations, noninterest-bearing balances, deposit beta, runoff history, digital transfer capability, brokered funding, and the gap between modeled and observed behavior. A low historical beta is favorable only if the balances remain when competitors offer higher returns ([18] [20]).

Profitability quality also matters. A wide margin created by taking unhedged duration or relying on uninsured funding is not equivalent to a margin supported by diversified relationships, sound underwriting, and resilient operations. The IMF evidence suggests that excessive maturity transformation can add risk without adding margin. An investor should therefore ask what risk produced the return, whether the bank can retain the funding through a cycle, and how much capital protects the claim if the model fails ([17]).

### For Depositors and Corporate Treasurers

Deposit insurance rules should be applied to legal ownership rather than assumed from a bank's brand. In the United States, the standard amount is $250,000 per depositor, per insured bank, per ownership category. Corporate treasurers should know which balances are insured, how payroll and payment operations continue if a bank is closed, what alternative accounts and signatories are ready, and whether cash-management structures create operational or counterparty concentration ([8]).

Diversification can reduce a firm's exposure to one bank but can also add operational complexity. The objective is not to react to every rumor; it is to establish pre-agreed limits, verified account access, payment contingencies, and escalation criteria before stress. This paragraph is a practical synthesis of the insurance limits and the operating-account problems observed in the 2023 resolutions ([8] [14] [15]).

### For the Financial System

Restricting maturity transformation in insured banks can move it toward funds, dealers, securitization vehicles, or private credit structures. The 2008 repo contraction and the 2020 money-market interventions show that risk relocation is not risk elimination. Functional regulation asks what liquidity promise is being made, how the assets behave under sale, who supplies emergency cash, and where losses land, rather than relying only on an institution's legal category ([12] [13] [21]).

The author's synthesis is that durable banking rests on five linked capacities: enough loss-absorbing capital to remain credible, enough liquid assets and borrowing capacity to pay, stable and diversified funding, operational ability to mobilize resources, and governance that acts before confidence breaks. Weakness in one capacity can impair the others. Maturity transformation remains socially useful because it converts savings into committed credit, but its private return is inseparable from a public and institutional architecture designed to prevent a liquidity shock from becoming a solvency and economic crisis ([1] [11] [16]).

## Sources

1. Diamond, D. W. and Dybvig, P. H. (1983). "Bank Runs, Deposit Insurance,
   and Liquidity." Journal of Political Economy, 91(3), 401-419.
   https://www.minneapolisfed.org/research/quarterly-review/bank-runs-deposit-insurance-and-liquidity [high]

2. Royal Swedish Academy of Sciences (2022). "The Prize in Economic Sciences
   2022: Popular Information."
   https://www.nobelprize.org/prizes/economic-sciences/2022/popular-information/ [high]

3. Bank of England (1969). "The Bank of England Note - A Short History."
   https://www.bankofengland.co.uk/quarterly-bulletin/1969/q2/the-bank-of-england-note---a-short-history [high]

4. Bank of England. "Our History."
   https://www.bankofengland.co.uk/about/history [high]

5. Anson, M., Bholat, D., Kang, M. and Thomas, R. (2017). "The Bank of
   England as Lender of Last Resort: New Historical Evidence from Daily
   Transactional Data." Bank of England Working Paper No. 691.
   https://www.bankofengland.co.uk/working-paper/2017/the-bank-of-england-as-lender-of-last-resort-new-historical-evidence-from-daily-transactional-data [high]

6. Federal Reserve History. "The Panic of 1907" and "Federal Reserve Act
   Signed into Law."
   https://www.federalreservehistory.org/essays/panic-of-1907
   https://www.federalreservehistory.org/essays/federal-reserve-act-signed [high]

7. Federal Reserve History. "Banking Panics of 1930-31."
   https://www.federalreservehistory.org/essays/banking-panics-1930-31 [high]

8. Federal Deposit Insurance Corporation. "Understanding Deposit Insurance."
   https://www.fdic.gov/deposit/deposits [high]

9. Basel Committee on Banking Supervision. "RCAP on Timeliness: Basel III
   Implementation Dashboard" and GHOS press release, March 9, 2026.
   https://www.bis.org/bcbs/implementation/rcap_reports.htm
   https://www.bis.org/press/p260309.htm [high]

10. Basel Committee on Banking Supervision (2004). "International Convergence
    of Capital Measurement and Capital Standards: A Revised Framework."
    https://www.bis.org/publ/bcbs107.pdf [high]

11. Basel Committee on Banking Supervision (2022). "Evaluation of the Impact
    and Efficacy of the Basel III Reforms."
    https://www.bis.org/bcbs/publ/d544.pdf [high]

12. Gorton, G. B. and Metrick, A. (2012). "Who Ran on Repo?" NBER Working
    Paper 18455.
    https://www.nber.org/papers/w18455 [high]

13. Tarullo, D. K. (2012). "Shadow Banking After the Financial Crisis."
    Board of Governors of the Federal Reserve System.
    https://www.federalreserve.gov/newsevents/speech/tarullo20120612a.htm [high]

14. Board of Governors of the Federal Reserve System (2023). "Review of the
    Federal Reserve's Supervision and Regulation of Silicon Valley Bank."
    https://www.federalreserve.gov/publications/files/svb-review-20230428.pdf [high]

15. Office of Inspector General, Board of Governors of the Federal Reserve
    System (2023). "Material Loss Review of Silicon Valley Bank."
    https://oig.federalreserve.gov/reports/board-material-loss-review-silicon-valley-bank-sep2023.pdf [high]

16. Basel Committee on Banking Supervision (2023, 2024). "Report on the 2023
    Banking Turmoil" and "The 2023 Banking Turmoil and Liquidity Risk: A
    Progress Report."
    https://www.bis.org/publications/report-2023-banking-turmoil.pdf
    https://www.bis.org/bcbs/publ/d582.pdf [high]

17. Bologna, P. (2018). "Banks' Maturity Transformation: Risk, Reward, and
    Policy." IMF Working Paper 18/45.
    https://www.imf.org/-/media/files/publications/wp/2018/wp1845.pdf [high]

18. Drechsler, I., Savov, A. and Schnabl, P. (2021). "Banking on Deposits:
    Maturity Transformation without Interest Rate Risk." Journal of Finance,
    76(3), 1091-1143.
    https://www.nber.org/papers/w24582 [high]

19. DeMarzo, P. M., Krishnamurthy, A. and Nagel, S. (2024). "Interest Rate
    Risk in Banking." NBER Working Paper 33308.
    https://www.nber.org/papers/w33308 [high]

20. Drechsler, I., Savov, A., Schnabl, P. and Wang, O. (2024). "Deposit
    Franchise Runs." NBER Working Paper 31138, revised September 2024.
    https://www.nber.org/papers/w31138 [high]

21. Board of Governors of the Federal Reserve System (2020). "Financial
    Stability Report, November 2020."
    https://www.federalreserve.gov/publications/files/financial-stability-report-20201109.pdf [high]

22. Schularick, M. and Taylor, A. M. (2012). "Credit Booms Gone Bust:
    Monetary Policy, Leverage Cycles, and Financial Crises, 1870-2008."
    American Economic Review, 102(2), 1029-1061.
    https://www.aeaweb.org/articles?id=10.1257/aer.102.2.1029 [high]

23. Jorda, O., Schularick, M. and Taylor, A. M. (2013). "When Credit Bites
    Back." Journal of Money, Credit and Banking, 45(s2), 3-28.
    https://www.nber.org/papers/w17621 [high]

24. Swiss Financial Market Supervisory Authority (2023). "Lessons Learned
    from the Credit Suisse Crisis."
    https://www.finma.ch/en/~/media/finma/dokumente/dokumentencenter/myfinma/finma-publikationen/cs-bericht/20231219-finma-bericht-cs.pdf?sc_lang=en [high]

25. Board of Governors of the Federal Reserve System, Federal Deposit Insurance
    Corporation, and Office of the Comptroller of the Currency (2026).
    "Agencies Request Comment on Proposals to Modernize the Regulatory Capital
    Framework and Maintain the Strength of the Banking System."
    https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260319a.htm [high]

26. Federal Deposit Insurance Corporation (2026). "Quarterly Banking Profile:
    Second Quarter 2026."
    https://www.fdic.gov/fdic-quarterly-banking-profile-second-quarter-2026.pdf [high]

## See Also

- `library/finance/bond-pricing-and-fixed-income-markets.md` -- duration,
  yield-curve, and bond-price mechanics behind securities valuation.
- `library/finance/financial-statement-analysis.md` -- balance-sheet,
  income-statement, and ratio analysis used to assess banks.
