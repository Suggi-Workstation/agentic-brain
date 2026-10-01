---
name: forensic-accounting-methodology
id: 20260920T193417Z
tier: library-topic
domain: accounting-financial-shenanigans
author: Librarian
tags: [forensic-accounting, financial-statement-fraud, red-flags, earnings-quality, fraud-detection, analytical-procedures, evidence-triangulation]
links: [library/accounting-financial-shenanigans/beneish-m-score.md, library/accounting-financial-shenanigans/cash-flow-shenanigans.md, library/accounting-financial-shenanigans/revenue-recognition-shenanigans.md, library/accounting-financial-shenanigans/non-gaap-metrics-and-pro-forma-manipulation.md, library/accounting-financial-shenanigans/restatement-analysis.md, library/accounting-financial-shenanigans/related-party-transactions.md, library/accounting-financial-shenanigans/acquisition-accounting-tricks.md, library/accounting-financial-shenanigans/off-balance-sheet-shenanigans.md]
reviewed: 2026-10-01
---

# Forensic Accounting Methodology -- Detection Requires Converging Evidence, Not a Single Red Flag

Forensic accounting methodology is a structured process for moving from an anomalous financial pattern to a testable explanation and then to corroborating evidence. No ratio, checklist item, or statistical score proves manipulation by itself; reliable detection combines incentives, time-series and common-size analysis, cross-statement reconciliation, transaction economics, disclosures, counterparties, and independent evidence. This topic presents that integrated detection process for analysts using public financial information, not a procedure for conducting an external audit. [1][2][3][4][5][10][11]

## Background

Financial statement fraud creates a special evidence problem. The analyst observes reports prepared by the same organization whose conduct is being tested, while legitimate business change can produce many of the same numerical symptoms as manipulation. Rapid growth can increase receivables, and an acquisition or other structural change can alter margins, asset composition, and accruals without manipulation. Those outcomes become suspicious only when the stated explanation conflicts with accounting relationships, transaction terms, later reversals, nonfinancial activity, or independent records. The methodological problem is therefore not to compile the longest list of red flags. It is to distinguish an explainable anomaly from a reporting claim that fails several independent tests. [2][3][4][5]

Early forensic practice was largely case based. Practitioner taxonomies and enforcement records document recurring mechanisms: premature or fictitious revenue, capitalization of operating costs, financing presented as operating cash, misleading non-GAAP measures, and acquisition-accounting distortions. Schilit, Perler, and Engelhart organized these mechanisms into earnings, cash-flow, key-metric, and acquisition-accounting shenanigans. That taxonomy remains useful because it links a suspicious outcome to the journal entries, classifications, estimates, or transactions that could produce it. A taxonomy is not yet a complete method, however; it says what can go wrong but does not determine which lead deserves attention or what evidence would falsify the allegation. [1][12][13][14]

Auditing standards supply an evidence discipline even though forensic analysis and a financial statement audit have different objectives. PCAOB AS 2401 distinguishes intentional fraud from error, identifies fraudulent financial reporting and asset misappropriation as relevant categories, and describes incentives or pressures, opportunities, and attitudes or rationalizations as conditions generally present when fraud occurs. PCAOB AS 2305 defines analytical procedures as evaluations of plausible relationships among financial and nonfinancial data and requires expectations to reflect knowledge of the company and industry. These principles support hypothesis formation and corroboration, but an analyst should not describe a public-filings review as an audit or claim audit assurance from analytical work alone. [2][3]

Academic research converted parts of the forensic taxonomy into reproducible screens. Beneish combined eight financial statement variables associated with distortions or preconditions for manipulation into the M-Score, while Dechow, Ge, Larson, and Sloan developed F-Score models from firms alleged in SEC enforcement releases to have misstated and from financial, market, and nonfinancial variables. Sloan separately studied earnings persistence and stock-price response, not fraud classification, and showed that the accrual and cash components of earnings have different implications for future earnings. Lee, Ingram, and Howard tested the earnings-minus-operating-cash-flow relation as a fraud indicator. Collectively, this literature supports quantitative triage. It does not support treating a model output as a finding of fraud, because the classifications generate false positives and the samples are selected. [4][5][6][7]

The enforcement record explains why an integrated method is necessary. COSO analyzed Accounting and Auditing Enforcement Releases issued from January 1998 through December 2007 and identified 347 companies involved in alleged fraudulent financial reporting. Improper revenue recognition appeared in 61 percent of cases. Asset overstatement, excluding receivable overstatements arising from revenue fraud, appeared in 51 percent; 46 percent of cases involved overvaluing existing assets or capitalizing expenses. The releases named the CEO, the CFO, or both as associated with the fraud in 89 percent of cases. Companies often used more than one technique, so the category percentages exceed 100 percent. A review limited to one statement or one ratio can therefore miss both the multi-account structure of a scheme and the organizational incentives that sustain it. [8]

Restatements provide another empirical foundation. GAO identified 919 restatement announcements involving accounting irregularities from January 1997 through June 2002 and reported that revenue recognition accounted for almost 38 percent. Annual announcements rose from 92 in 1997 to 225 in 2001, an increase of approximately 145 percent; GAO identified another 125 announcements in the first half of 2002. For 689 announcements with usable market data, GAO estimated a 9.5 percent average market-adjusted loss from the trading day before through the trading day after the announcement and a $95.6 billion aggregate market-adjusted loss. Palmrose, Richardson, and Scholz later examined 403 restatements announced from 1995 through 1999 and found a mean abnormal return of negative 9.2 percent over announcement day and the following day. More negative reactions were associated with fraud indications, more affected accounts, more negative changes in reported income, and attribution to auditors or management, but not to the SEC. Detection matters because a correction changes both reported history and confidence in the reporting process. [9][16]

SEC staff speeches document the regulator's use of risk-based analytics without making the tools proof of misconduct. In 2012, Craig Lewis described the Accounting Quality Model as being designed to identify peer-relative anomalies and generate risk rankings. In 2016, Scott Bauguess described the Corporate Issuer Risk Assessment program as providing more than 230 custom metrics, including measures of earnings smoothing, auditor activity, tax treatments, financial ratios, and managerial actions. Bauguess stated that a high-risk classification was not a clear indicator of wrongdoing and that expert inquiry remained necessary. Both speeches expressly represented the speakers' views rather than formal Commission positions. The methodological boundary is still useful: screening allocates attention; evidence establishes what happened. [10][11]

The author's synthesis is that modern forensic accounting should be organized as a funnel. It begins broadly with reporting incentives, longitudinal and peer comparisons, and quantitative screens. It narrows to the accounts and assertions that generated the anomaly, reconstructs the economic transaction across statements and periods, and then seeks evidence independent of management's preferred narrative. The process ends with an explicitly graded conclusion -- explained, unresolved, likely error, aggressive reporting, or evidence consistent with manipulation -- rather than a binary accusation based on one number. This synthesis combines the practitioner taxonomy, auditing evidence principles, academic screens, and regulator analytics described above. [1][2][3][4][5][6][7][8][9][10][11]

## Core Concepts

### 1. Define the question, boundary, and comparison set

A forensic review should begin with a specific reporting question: whether revenue was earned in the stated period, whether an expense created a qualifying asset, whether operating cash arose from customers rather than financing, whether a reserve reflects a supportable obligation, or whether a non-GAAP adjustment is recurring. The question determines the accounts, periods, disclosures, and nonfinancial measures required. A vague objective such as "find fraud" encourages confirmation bias because every unusual number can be made to look suspicious after the fact. PCAOB standards similarly tie procedures to assessed risks and relevant assertions rather than treating analytics as free-standing proof. [2][3]

The comparison set must also be fixed before interpreting the output. Use several annual and quarterly periods, a consistent accounting basis, economically comparable peers, and industry conditions that affect the relationship being tested. Horizontal analysis compares a line item across periods; vertical analysis expresses statement items relative to a base such as revenue or total assets; ratio analysis tests relationships across accounts or statements. All three are triage devices. A percentage change that looks extreme against one base year may disappear across a full cycle, and a peer comparison can mislead when business mix, acquisition timing, or accounting policy differs. [3][17]

### 2. Map incentives and reporting pressure without inferring guilt

Incentives explain where reporting risk may concentrate, but they do not prove intent. Relevant pressures include a need for debt or equity financing, compensation tied to financial targets, commitments to aggressive forecasts, and management interest in maintaining the share price or earnings trend. Opportunities include subjective estimates, ineffective controls, complex or unusual transactions near period end, related parties, and concentrated authority. Attitudes may appear in repeated failure to correct control problems or attempts to justify marginal accounting. AS 2401 classifies example fraud risk factors as incentives or pressures, opportunities, and attitudes or rationalizations, while COSO's case evidence shows frequent senior-executive association with alleged fraud. [2][8]

The correct use of incentive evidence is Bayesian rather than accusatory. A covenant threshold makes a quarter-end classification more important to test; it does not make the classification false. An earnings-linked bonus raises the cost of relying on management's estimate; it does not establish that the estimate was manipulated. The author's synthesis is to record incentives before examining the detailed numbers, then require transaction-level or disclosure-level evidence before upgrading concern. This sequence prevents a favorable result from erasing a known conflict and prevents a known conflict from becoming a substitute for proof. [2][8][15]

### 3. Build horizontal, vertical, and expectation-based diagnostics

Horizontal analysis should calculate absolute and percentage changes for revenue, receivables, contract assets, inventory, payables, reserves, capitalized costs, goodwill, operating cash flow, and major non-GAAP adjustments across enough periods to expose reversals. Vertical analysis should common-size income-statement items to revenue and balance-sheet items to total assets, then compare the resulting structure through time and against relevant peers. Expectation-based analysis extends those tools by predicting one measure from another plausible driver: units sold and average price for revenue, headcount and compensation for payroll, occupied area and contract rates for rent, or production volume and input prices for cost of sales. AS 2305 recognizes prior periods, budgets, industry information, within-period financial relationships, and nonfinancial information as possible expectation inputs. [3][17]

The result should be an anomaly register rather than a verdict. Each row records the metric, expected relationship, observed difference, threshold, affected period, possible innocent explanations, possible manipulation mechanisms, and evidence needed to distinguish them. Disaggregation is essential. Annual revenue may look normal while one geography, channel, customer, or final month contains the entire deviation. Gross margin may look stable because an overstated revenue account offsets an understated expense account. AS 2401 gives disaggregated comparisons by location, business line, or month as examples of responses to fraud risk, and AS 2305 explains that detailed expectations and disaggregation reduce the risk that offsetting factors conceal misstatements. [2][3]

### 4. Reconcile earnings, cash flow, and balance-sheet movements

Every reported performance claim should be traced through all three primary statements. Revenue growth normally produces some combination of cash, receivables, contract assets, deferred revenue changes, inventory movement, and tax effects. Expense capitalization records current spending as an asset rather than current expense and creates depreciation or amortization in later periods. A reserve release increases earnings while reducing a liability; the cash consequence depends on whether and when the underlying obligation is settled. The author's synthesis is to write the expected journal-entry logic before reading management's explanation, because the debit-credit structure identifies which accounts must carry the other side of the claim. [1][3][13]

Cash is corroborating evidence, not an untouchable truth source. The SEC alleged that Delphi's linked inventory sale and repurchase agreements represented financing rather than genuine sales and inflated operating cash flow. Factoring can accelerate customer cash into the current period, while a supplier-finance program can alter working-capital, liquidity, and cash-flow interpretation. FASB ASU 2022-04 requires U.S. GAAP disclosures of supplier-finance program terms, outstanding confirmed obligations, balance-sheet location, and an annual roll-forward, but it does not change recognition, measurement, or presentation. The analyst should reconcile those disclosures to payment terms, accounts payable, cash flow, and subsequent settlement rather than infer classification from the program label. [12][22]

### 5. Use quantitative models as ranked screens

The Beneish M-Score combines eight variables related to receivables, margins, asset quality, sales growth, depreciation, selling and administrative expense, accruals, and leverage. In the reported model, the receivables, gross-margin, asset-quality, sales-growth, and total-accrual variables were significant; depreciation, selling and administrative expense, and leverage were not. The original study found a systematic relationship between those financial characteristics and manipulation and presented the model as a screening device requiring investigation of whether a distortion came from manipulation or another structural cause. In a holdout sample of 24 manipulators and 624 controls at the commonly cited score cutoff above -1.78, the model missed 50 percent of manipulators and falsely flagged 7.2 percent of controls. A high score should therefore direct the analyst to the contributing variables and their underlying accounts, not be repeated as a probability that a particular company committed fraud. [4]

The Dechow F-Score broadens the screen to material accounting misstatements alleged in SEC enforcement releases. Its inputs capture accrual quality, changes in receivables and inventory, cash-sales relationships, performance, and other reporting features, with model variants adding nonfinancial, off-balance-sheet, and market information. In the published Model 1 classification sample, an F-Score cutoff of 1.00 identified 339 of 494 misstating firm-years, a sensitivity of 68.62 percent, but falsely classified 48,282 of 132,967 nonmisstating firm-years, a false-positive rate of 36.31 percent. Selection may limit generalizability, and both models produce false classifications. The author's synthesis is to run more than one screen, retain the raw variables, and investigate only signals supported by account-level anomalies or qualitative evidence. Agreement among models increases priority; it does not convert correlation into proof. [4][5][10][11]

Accrual measures deserve special treatment because they connect reported earnings to cash realization. Sloan's 40,679-firm-year study examined earnings persistence and stock-price response, not fraud classification; it found pooled persistence coefficients of 0.765 for the accrual component and 0.855 for the cash component. Lee, Ingram, and Howard compared 56 fraud cases from 1978 through 1991 with 60,453 COMPUSTAT firm-years and found that the excess of earnings over operating cash flow added discrimination when considered with other fraud-risk factors. Growth, acquisitions, and other structural changes can produce legitimate accrual differences. The author's synthesis is to decompose accruals into receivables, inventory, payables, reserves, capitalization, and acquisition effects, then ask which component lacks a persuasive economic explanation. [4][6][7]

### 6. Test revenue, expenses, reserves, and non-GAAP bridges separately

Revenue testing should connect contract terms, transfer of control, billing, shipping or service evidence, cash collection, returns, credit notes, and subsequent-period reversals. Period-end concentration, receivables growing faster than revenue, unusual customer terms, distributor inventory growth, and cash that circulates through a counterparty are research triggers. They become stronger when several point to the same transaction population. COSO's finding that revenue recognition was the most common technique in its enforcement sample justifies a high default priority, while the scope and exact test must still reflect the company's business model. [2][8]

Expense and reserve testing starts from recognition criteria and subsequent use. For a capitalized cost, identify the asset, future benefit, useful life, authorization, and cash classification. For a reserve, reconstruct the opening balance, additions, usage, releases, and closing balance, and compare the roll-forward with claims, restructuring actions, warranty activity, or other operational evidence. WorldCom demonstrates the direct mechanism: the SEC alleged that approximately $3.8 billion of ordinary line costs were transferred to capital accounts, deferring expense and overstating income. The transaction did not need a complex ratio to be understood once the account entries and capitalization treatment were reconstructed. [13]

Non-GAAP analysis should reproduce every reconciliation from the comparable GAAP measure, track each adjustment through time, and classify it by recurrence, cash effect, control by management, and economic necessity. The SEC's current interpretations warn that individually tailored recognition or measurement principles, unclear or inappropriate labels, inconsistent presentation between periods, and asymmetric exclusion of nonrecurring charges while retaining same-period gains can make a measure misleading. Detailed disclosure does not necessarily cure a materially misleading measure, and the comparable GAAP measure must receive equal or greater prominence where Item 10(e) applies. The forensic question is whether the adjusted measure clarifies a transitory item or constructs a hypothetical business that excludes ordinary costs. Recurring restructuring, stock compensation, acquisition costs, impairment, or litigation adjustments should be evaluated across several periods rather than accepted one quarter at a time. [1][14]

### 7. Trace transaction substance, counterparties, and time boundaries

Many manipulations rely on a boundary: year-end, consolidation perimeter, related-party definition, operating-versus-financing classification, current-versus-future period, or GAAP-versus-non-GAAP presentation. The author's synthesis is to map legal form and economic substance on the same page, identifying the ultimate counterparty, funding source, repurchase or return rights, guarantees, side agreements, transfer of risk, settlement after period end, and any person who can influence both sides. A transaction that crosses several boundaries deserves more attention because each boundary can hide one part of the economic whole. [1][2][12]

Subsequent events are especially valuable because manipulation often borrows from a later period. Receivables that reverse, goods that return, inventory that is repurchased, reserves that are released, bills that are paid immediately after year-end, and non-GAAP definitions that change can test the original explanation. The SEC alleged that Delphi repurchased inventory after year-end under linked arrangements and hid up to $325 million of factoring in 2003-2004, materially overstating its Street Net Liquidity measure and producing a false $30 million boost to Street Operating Cash Flow in one quarter. The sequence exposed financing and timing that the period-end presentation obscured. [12]

### 8. Triangulate evidence and grade the conclusion

The author's evidence-ranking rule gives more weight to evidence that is independent of management and close to the disputed claim. Contract terms, bank or customer records, regulator filings, contemporaneous transaction documents, and subsequent cash settlement generally bear more directly on a transaction than management commentary. Audited statements and footnotes are essential starting points but are not independent of management's reporting process. Press reports, short-seller allegations, and anonymous claims can generate leads but require corroboration. PCAOB AS 1105 defines audit evidence to include information that both corroborates and contradicts management assertions, and a 2022 SEC Office of the Chief Accountant staff statement urged auditors to consider public information and evaluate whether it contradicts information received from management. The same discipline improves public-source forensic work without turning it into an audit. [15][18]

The author's synthesis is a five-level conclusion scale. "Explained" means the anomaly reconciles to documented economics. "Unresolved" means evidence is insufficient. "Likely error" means the accounting appears inconsistent but intent is not supported. "Aggressive reporting" means a permissible or disputed choice predictably favors the reported narrative and warrants adjustment. "Evidence consistent with manipulation" means multiple independent facts support intentional distortion, while the legal conclusion remains for competent authorities. Every conclusion should list contrary evidence, missing evidence, affected periods, and the conditions that would change the assessment. [2][10][11][15]

### 9. Backtest estimates and inventory gatekeeper disclosures

Estimate testing should be longitudinal rather than confined to whether a current assumption appears reasonable. Build an estimate register for allowances, impairments, useful lives, reserves, variable consideration, fair values, acquisition estimates, pension assumptions, and tax valuation allowances. Record each estimate's method, data, assumptions, sensitivity, and directional earnings effect; compare prior estimates with actual outcomes or later re-estimation; and test changes in methods, data sources, and assumptions. AS 2401 requires auditors to compare prior-year estimates in significant accounts and disclosures with actual results when performing its retrospective review. AS 2810 adds that individually reasonable estimates can indicate bias when their differences consistently increase earnings or when cumulative changes in estimates swing to achieve an expected result. A public-source analyst can adapt those tests to disclosed estimates without claiming audit evidence or audit assurance. [2][19]

Before running screens, create a dated inventory of the highest-signal public records. It should cover Forms 10-K and 10-Q, amended filings, Form 8-K Items 4.01 and 4.02, the auditor's report, critical audit matters, and the controls and auditor-disagreement disclosures in Items 9 and 9A. SEC investor guidance identifies auditor changes and disagreements as possible red flags and requires Item 4.02 disclosure when previously issued statements or related audit reports should no longer be relied upon. AS 3101 defines a critical audit matter as a material-account or disclosure matter communicated to the audit committee that involved especially challenging, subjective, or complex auditor judgment. None of these items proves a misstatement; each narrows the accounts, periods, assertions, and gatekeeper evidence that require testing. [20][21][23]

## Evidence

### Statistical screens identify risk, not guilt

Beneish's 1999 study profiled earnings manipulators and developed a model whose variables represented financial statement distortions or preconditions associated with manipulation. The published summary reports that the model identified approximately half of the manipulators before public discovery and explicitly states that users must determine whether the numerical distortions arose from manipulation or another structural root. In the holdout sample at a score cutoff above -1.78, the model missed 12 of 24 manipulators and falsely flagged about 45 of 624 controls. That qualification is methodologically decisive: the M-Score is evidence that a company resembles the estimation sample, not evidence of the hidden transaction or managerial intent. [4]

Dechow, Ge, Larson, and Sloan developed their F-Score from 2,190 SEC Accounting and Auditing Enforcement Releases covering firms alleged to have misstated. Their analysis found that accrual and performance variables, changes in receivables and inventory, and other financial and nonfinancial features help rank misstatement risk. Average F-Scores were approximately 1.5 before the misstatement, 1.9 during misstated years, and 1.0 afterward. At a cutoff of 1.00, Model 1 achieved 68.62 percent sensitivity but a 36.31 percent false-positive rate in the published classification sample. The SEC speeches on AQM and CIRA reach the same operational boundary: anomaly detection can direct expert attention, but a high-risk classification does not identify a violation. [5][10][11]

The accrual literature supports decomposition rather than a single cash-versus-income rule. Sloan's 40,679-firm-year study showed that the accrual component of earnings was less persistent than the cash component on average and that market prices did not fully reflect the difference until it affected later earnings; it did not test fraud classification. Lee, Ingram, and Howard compared 56 fraud cases from 1978 through 1991 with 60,453 COMPUSTAT firm-years and found that adding earnings minus operating cash flow substantially improved the fraud model's predictive ability. Lee and colleagues concluded that the relation should be considered with other fraud-risk factors. Growth, credit sales, inventory investment, and acquisitions can produce legitimate accrual differences, so the analyst must trace the specific accounts and later realization. [4][6][7]

### Enforcement cases show why cross-statement reconstruction works

The SEC's WorldCom complaint supplies a clean alleged example of a manipulation that affected more than one statement. The SEC alleged that WorldCom capitalized approximately $3.8 billion of line costs that should have been expensed, overstating pretax income by about $3.055 billion in 2001 and $797 million in the first quarter of 2002. The alleged entries moved ordinary operating costs into capital asset accounts. A forensic review that connected the income statement, capital expenditures, asset additions, capitalization policy, and supporting documentation could test the treatment; a review limited to reported earnings growth could not. [13]

The SEC's Delphi complaint demonstrates why operating cash flow is not self-validating. The SEC alleged that Delphi sold about $270 million of inventory to third parties near year-end while agreeing to repurchase it in the next quarter at the original price plus interest and fees. Treating the linked arrangements as sales rather than financing allegedly inflated operating cash flow by $200 million, reduced inventory by $270 million, and increased reported net income by $80 million. The SEC also alleged that Delphi hid up to $325 million of factoring in 2003-2004, materially overstated Street Net Liquidity, and produced a false $30 million boost to Street Operating Cash Flow in one quarter. The detection method is transaction linkage: read the sale, repurchase, fees, cash classification, and reversal as one economic arrangement. [12]

The two cases also show why a checklist must be translated into falsifiable tests. "Capital expenditures rose" is only a red flag; the WorldCom question was whether the recorded assets met capitalization criteria and had support. "Operating cash flow improved" is only a red flag; the Delphi question was whether the cash came from a sale with transferred risk or a financing with a repurchase obligation. The strongest evidence was not the abnormal ratio but the contract and journal-entry structure that explained how the ratio was produced. This is the author's synthesis from the enforcement records. [12][13]

### Population evidence sets priorities and consequences

COSO's 2010 study reviewed SEC Accounting and Auditing Enforcement Releases issued from January 1998 through December 2007 and identified 347 companies involved in alleged fraudulent financial reporting. Improper revenue recognition occurred in 61 percent of cases. Asset overstatement, excluding receivables affected by revenue fraud, occurred in 51 percent, while 46 percent specifically involved overvaluing existing assets or capitalizing expenses. The SEC releases named the CEO, the CFO, or both as associated with the fraud in 89 percent. Fraud periods averaged 31.4 months, with a median of 24 months. These findings justify three priorities in a general methodology: test revenue and asset recognition early, include management incentives and override risk, and examine a multi-period sequence rather than one annual snapshot. [8]

GAO's study of 919 restatement announcements from January 1997 through June 2002 found that revenue recognition accounted for almost 38 percent. Annual announcements rose from 92 in 1997 to 225 in 2001, an increase of approximately 145 percent. GAO's analysis of 689 announcements with usable market data found an average market-adjusted return of negative 9.5 percent over the trading day before through the trading day after the announcement and an aggregate market-adjusted loss of $95.6 billion. Palmrose, Richardson, and Scholz's event study of 403 announcements measured a mean abnormal return of negative 9.2 percent over announcement day and the following day; more negative reactions were associated with fraud indications, more affected accounts, more negative changes in reported income, and attribution to auditors or management, but not to the SEC. The evidence supports treating breadth, direction, prompter, and management intent as severity dimensions after a potential misstatement is found. [9][16]

### Standards support expectation building and contradictory-evidence tests

PCAOB AS 2305 describes analytical procedures as comparisons of recorded amounts or ratios with auditor-developed expectations based on plausible relationships. It identifies prior-period data, budgets or forecasts, within-period financial relationships, industry information, and relevant nonfinancial information as expectation sources. It also warns that apparently related data may not be related and that unexpected relationships can provide important evidence when scrutinized. These requirements support a method that documents the expected relationship and tests its reliability before treating a deviation as meaningful. [3]

AS 2401 adds the response logic. It discusses fraud risk factors, journal entries and period-end adjustments, significant unusual transactions, management estimates, revenue analytics, and the possibility that collusion or fabricated evidence can defeat ordinary controls. A 2022 SEC Office of the Chief Accountant staff statement, which expressly has no legal force and creates no new obligations, said auditors should consider public information, objectively evaluate its effect on risk assessment and the audit response, and evaluate whether it contradicts information received from management. For a public-source analyst, these sources support disaggregation, boundary testing, evidence from outside the reporting narrative, and an explicit search for contradictory facts. They do not confer audit assurance on the analyst's work. [2][15][18]

### Non-GAAP rules provide a reproducible reconciliation test

The SEC's non-GAAP interpretations make part of the forensic process directly testable. A registrant must consider whether adjustments, labels, period-to-period consistency, and presentation are misleading. The interpretations warn about individually tailored recognition and measurement principles, unclear labels, inconsistent adjustment of similar items between periods, asymmetric treatment of same-period gains and charges, and exclusion of normal recurring cash operating costs. Item 10(e) separately requires the most directly comparable GAAP measure to receive equal or greater prominence where it applies. A reviewer can rebuild the bridge from GAAP, compare definitions across periods, identify excluded recurring cash costs, test whether gains and losses are treated symmetrically, and compare adjusted profit with cash realization. This procedure converts a narrative concern about "adjusted earnings" into a documented series of differences. [14]

The method still requires economic judgment. A recurring line item can be non-core, and a one-time item can reveal a permanent capital-allocation loss. The relevant questions are whether the item is necessary to operate the business, whether it recurs by another label, whether management controls its occurrence, whether it consumed cash, and whether excluding it improves prediction of sustainable economics. The author's synthesis is to present both reported GAAP and analyst-normalized results, with every adjustment reversible, rather than replace management's opaque measure with another opaque measure. [1][14]

## Implications

### For investors and credit analysts

The practical output of a forensic review should be an evidence map that can change a valuation or credit decision. Begin with reported figures, list each anomaly, identify the account and assertion at risk, quantify a reversible adjustment range, and show the effect on revenue, margin, operating cash flow, leverage, and normalized earning power. Do not collapse all concerns into a single "quality" score. A suspected revenue cutoff problem changes receivables and sustainable sales; a capitalization issue changes current earnings, assets, future depreciation, and operating cash flow; a financing classification changes liquidity interpretation without changing total cash. The adjustment must follow the mechanism. [1][12][13]

A margin of safety should reflect both numerical downside and epistemic uncertainty. If evidence supports a corrected number, use it. If evidence is incomplete, model a range and increase the required return or decline the investment when the unresolved amount could eliminate the thesis. The author's assessment is that accounting opacity is not diversified away merely by lowering a point estimate: opaque reporting also weakens confidence in management representations, working-capital forecasts, debt capacity, and terminal economics. This assessment follows the documented market consequences of restatements and the cross-account nature of enforcement cases. [8][9][12][13][16]

The review should continue after purchase. Update the anomaly register each quarter, test whether promised reversals occur, compare cash collection with revenue, roll reserves forward, reconcile acquisitions, and preserve prior non-GAAP definitions so that changes cannot rewrite history. A one-period anomaly that resolves with documented economics should be downgraded. A red flag that repeats, migrates to another account, or requires a new explanation should be escalated. This longitudinal discipline is consistent with COSO's finding that alleged fraud periods averaged 31.4 months and had a 24-month median. [8]

### For boards, audit committees, and management

The author's governance recommendation is that boards require management to explain the economic mechanism behind material accounting estimates and unusual period-end transactions, not merely confirm compliance. For each significant estimate, the record should show the responsible owner, external evidence, sensitivity, subsequent outcome, and whether the same judgment consistently favored reported performance. For each unusual transaction, the board should understand counterparties, funding, guarantees, repurchase or return rights, and cash-flow classification. AS 2401's focus on management override, estimates, and unusual transactions, together with COSO's finding that the CEO, CFO, or both were named in 89 percent of cases, supports an independent governance layer. [2][8][19]

The author's control-design recommendation is to preserve evidence that can falsify management's position. Examples include independently controlled customer confirmations, automated links among shipping, billing, and revenue records, approval limits for manual journal entries, reserve roll-forwards tied to claims data, and acquisition models compared with subsequent performance. PCAOB standards require attention to contradictory evidence and warn that collusion can make apparently persuasive evidence false. Protected escalation channels and investigators outside the implicated reporting chain are additional governance safeguards, not requirements established by the cited auditing standards. [2][18]

The author's disclosure recommendation is to make material bridges reproducible: identify factoring and supplier-finance effects, distinguish organic from acquired growth, reconcile non-GAAP measures consistently, explain changes in capitalization or estimates, and quantify unusual period-end activity. FASB ASU 2022-04 now requires buyers using supplier-finance programs to disclose key terms, outstanding confirmed obligations, balance-sheet location, and an annual roll-forward, which lets analysts test changes in program magnitude and payment activity. Transparency does not prove that the accounting is correct, but it makes the claim testable and lowers the number of unsupported assumptions an external reader must make. [14][22]

### For auditors and forensic investigators

An external audit seeks reasonable assurance that the financial statements are free of material misstatement. The author's scope distinction is that a forensic investigation may pursue a narrower allegation, a different evidence threshold, and potential intent. The activities can share risk assessment, analytical procedures, journal-entry testing, confirmation, and contradictory-evidence analysis without being conflated. A public-source analyst should not claim access to audit evidence, and an auditor should not treat a statistical flag as a substitute for sufficient appropriate evidence. [2][3][15][18]

The most efficient investigation moves from broad analytics to precise populations. A revenue anomaly may narrow to one region, final-week transactions, or customers with extended terms. An accrual flag may narrow to a reserve release or capitalized cost center. A cash-flow anomaly may narrow to factoring, a repurchase agreement, or supplier-finance balances. Once narrowed, select evidence that directly tests existence or occurrence, completeness, valuation or allocation, rights and obligations, and presentation and disclosure. The author's synthesis is to stop expanding the checklist once a transaction-level hypothesis can be tested, because more generic indicators add less information than direct evidence. [2][3][12][13][18]

The author's disconfirmation rule requires recording facts that weigh against the working allegation. If cash was independently confirmed, goods were delivered, the customer had capacity to pay, no return right existed, and subsequent collection occurred without circular funding, those facts weigh against fictitious revenue even if receivables grew quickly. If a capitalized project has documented technical feasibility, approved costs, a functioning asset, and consistent amortization, those facts weigh against improper capitalization. PCAOB AS 1105 states that audit evidence includes information that corroborates and information that contradicts management assertions. A methodology that preserves only incriminating facts is selection bias. [2][3][15][18]

### For regulators and data-driven surveillance

SEC staff speeches describe analytics that compare filings, calculate peer-risk measures, rank issuers, extract words and phrases, apply topic modeling across tens of thousands of narrative disclosures, and analyze filing tone. They also state the boundary: a high-risk classification is not a clear indicator of wrongdoing, and expert inquiry remains necessary. The author's model-governance recommendation is to document the target, estimation sample, false-positive cost, data quality, drift, and human review required before escalation. [10][11]

Combining structured filing data with nonfinancial evidence can make surveillance more discriminating. Revenue can be compared with units, locations, customers, or capacity; payroll with headcount; capital spending with physical assets; and reserves with claims or operational incidents. AS 2305 requires economically plausible relationships and reliable data. The author's synthesis is that more data do not cure a weak causal premise and that management-controlled inputs can reproduce the reporting claim a model is supposed to test. [3][10][11]

### Limits and safeguards

Forensic methodology cannot eliminate uncertainty. Public disclosures may omit the contract, customer record, bank confirmation, or internal communication needed to determine intent. Accounting standards permit judgment, business models change, and enforcement databases contain only detected and selected cases. A responsible conclusion separates accounting inconsistency from fraud, states the missing evidence, and avoids converting a red flag into an allegation. [2][4][5][10][11][15]

The worst failure is a confident accusation produced by a mechanically applied screen. It can harm innocent parties, distract from the actual anomaly, and teach users to ignore future warnings. The preventive rule is simple: no conclusion of manipulation without converging evidence from at least two independent classes -- for example, a financial anomaly plus transaction documentation, a model signal plus a subsequent reversal, or a disclosure inconsistency plus counterparty evidence. This two-class rule is the author's proposed safeguard, not an auditing standard. It operationalizes the common warning in academic models, PCAOB evidence requirements, and SEC analytics that detection tools initiate investigation rather than complete it. [2][3][4][5][10][11][15]

## Sources

1. Schilit, H. M., Perler, J., and Engelhart, Y. (2018). "Financial
   Shenanigans: How to Detect Accounting Gimmicks and Fraud in Financial
   Reports," 4th edition. McGraw-Hill Education.
   https://www.mheducation.com/highered/mhp/product/financial-shenanigans-fourth-edition-how-detect-accounting-gimmicks-fraud-financial-reports.html [high]

2. Public Company Accounting Oversight Board. "AS 2401: Consideration of
   Fraud in a Financial Statement Audit."
   https://pcaobus.org/oversight/standards/auditing-standards/details/AS2401 [high]

3. Public Company Accounting Oversight Board. "AS 2305: Substantive
   Analytical Procedures."
   https://pcaobus.org/oversight/standards/auditing-standards/details/AS2305 [high]

4. Beneish, M. D. (1999). "The Detection of Earnings Manipulation."
   Financial Analysts Journal, 55(5), 24-36.
   https://doi.org/10.2469/faj.v55.n5.2296 [high]

5. Dechow, P. M., Ge, W., Larson, C. R., and Sloan, R. G. (2011).
   "Predicting Material Accounting Misstatements." Contemporary
   Accounting Research, 28(1), 17-82.
   https://doi.org/10.1111/j.1911-3846.2010.01041.x [high]

6. Sloan, R. G. (1996). "Do Stock Prices Fully Reflect Information in
   Accruals and Cash Flows About Future Earnings?" The Accounting Review,
   71(3), 289-315. https://doi.org/10.2308/TAR-9608042309 [high]

7. Lee, T. A., Ingram, R. W., and Howard, T. P. (1999). "The Difference
   between Earnings and Operating Cash Flow as an Indicator of Financial
   Reporting Fraud." Contemporary Accounting Research, 16(4), 749-786.
   https://doi.org/10.1111/j.1911-3846.1999.tb00603.x [high]

8. Beasley, M. S., Carcello, J. V., Hermanson, D. R., and Neal, T. L.
   (2010). "Fraudulent Financial Reporting: 1998-2007, An Analysis of
   U.S. Public Companies." Committee of Sponsoring Organizations of the
   Treadway Commission.
   https://egrove.olemiss.edu/cgi/viewcontent.cgi?article=1534&context=aicpa_assoc [high]

9. U.S. General Accounting Office (2002). "Financial Statement
   Restatements: Trends, Market Impacts, Regulatory Responses, and
   Remaining Challenges." GAO-03-138.
   https://www.gao.gov/products/gao-03-138 [high]

10. Lewis, C. M. (2012). "Risk Modeling at the SEC: The Accounting
    Quality Model." U.S. Securities and Exchange Commission staff speech;
    the speaker stated that the views were his own.
    https://www.sec.gov/newsroom/speeches-statements/2012-spch121312cmlhtm [high]

11. Bauguess, S. W. (2016). "Has Big Data Made Us Lazy?" U.S. Securities
    and Exchange Commission staff speech; the speaker stated that the views
    were his own.
    https://www.sec.gov/newsroom/speeches-statements/bauguess-american-accounting-association-102116 [high]

12. U.S. Securities and Exchange Commission (2006). "SEC Charges Delphi
    Corporation and Nine Individuals" and related complaint. Litigation
    Release No. 19891.
    https://www.sec.gov/enforcement-litigation/litigation-releases/lr-19891 [high]

13. U.S. Securities and Exchange Commission (2002). "SEC Charges
    WorldCom with $3.8 Billion Fraud." Litigation Release No. 17588.
    https://www.sec.gov/enforcement-litigation/litigation-releases/lr-17588 [high]

14. U.S. Securities and Exchange Commission, Division of Corporation
    Finance. "Non-GAAP Financial Measures: Corporation Finance
    Interpretations." Issued June 7, 2021; last updated December 13, 2022.
    https://www.sec.gov/corpfin/non-gaap-financial-measures [high]

15. Munter, P. (2022). "The Auditor's Responsibility for Fraud Detection."
    U.S. Securities and Exchange Commission Office of the Chief Accountant
    staff statement, October 11, 2022; last reviewed January 5, 2024.
    https://www.sec.gov/newsroom/speeches-statements/munter-statement-fraud-detection-101122 [high]

16. Palmrose, Z.-V., Richardson, V. J., and Scholz, S. (2004).
    "Determinants of Market Reactions to Restatement Announcements."
    Journal of Accounting and Economics, 37(1), 59-89.
    https://doi.org/10.1016/j.jacceco.2003.06.003 [high]

17. Franklin, M., Graybeal, P., and Cooper, D. (2019). "Financial
    Statement Analysis." Principles of Accounting, Volume 1: Financial
    Accounting. OpenStax.
    https://openstax.org/books/principles-financial-accounting/pages/a-financial-statement-analysis [high]

18. Public Company Accounting Oversight Board. "AS 1105: Audit Evidence."
    https://pcaobus.org/oversight/standards/auditing-standards/details/AS1105 [high]

19. Public Company Accounting Oversight Board. "AS 2810: Evaluating Audit
    Results."
    https://pcaobus.org/oversight/standards/auditing-standards/details/AS2810 [high]

20. Public Company Accounting Oversight Board. "AS 3101: The Auditor's
    Report on an Audit of Financial Statements When the Auditor Expresses an
    Unqualified Opinion."
    https://pcaobus.org/oversight/standards/auditing-standards/details/AS3101 [high]

21. U.S. Securities and Exchange Commission, Office of Investor Education
    and Advocacy. "How to Read an 8-K."
    https://www.sec.gov/resources-for-investors/investor-alerts-bulletins/how-read-8-k [high]

22. Financial Accounting Standards Board (2022). "Accounting Standards
    Update 2022-04: Disclosure of Supplier Finance Program Obligations."
    https://storage.fasb.org/ASU%202022-04.pdf [high]

23. U.S. Securities and Exchange Commission, Office of Investor Education
    and Advocacy. "How to Read a 10-K/10-Q."
    https://www.sec.gov/resources-for-investors/investor-alerts-bulletins/how-read-10-k10-q [high]

## See Also

- `library/accounting-financial-shenanigans/beneish-m-score.md` -- the
  quantitative manipulation screen used as one triage layer in this method.
- `library/accounting-financial-shenanigans/cash-flow-shenanigans.md` --
  classification, financing, acquisition, and working-capital mechanisms
  that can distort reported operating cash flow.
- `library/accounting-financial-shenanigans/revenue-recognition-shenanigans.md` --
  transaction patterns and cutoff tests for the most common fraud category.
- `library/accounting-financial-shenanigans/non-gaap-metrics-and-pro-forma-manipulation.md` --
  reconciliation and recurrence tests for management-defined performance.
- `library/accounting-financial-shenanigans/restatement-analysis.md` --
  how later corrections reveal the type, magnitude, period, and prompter of
  prior misstatements.
- `library/accounting-financial-shenanigans/related-party-transactions.md` --
  counterparty mapping, circular funding, and non-arm's-length transaction
  tests.
- `library/accounting-financial-shenanigans/acquisition-accounting-tricks.md` --
  purchase allocation, reserve, earnout, and acquired-growth mechanisms.
- `library/accounting-financial-shenanigans/off-balance-sheet-shenanigans.md` --
  consolidation, guarantees, and economic-substance tests for hidden
  obligations.
