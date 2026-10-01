---
name: classification-shifting-and-special-item-abuse
id: 20261001T093704Z
tier: library-topic
domain: accounting-financial-shenanigans
author: Librarian
tags: [classification-shifting, special-items, core-earnings, restructuring-charges, discontinued-operations, non-gaap, forensic-accounting]
links: [library/accounting-financial-shenanigans/non-gaap-metrics-and-pro-forma-manipulation.md, library/accounting-financial-shenanigans/forensic-accounting-methodology.md, library/accounting-financial-shenanigans/acquisition-accounting-tricks.md, library/accounting-financial-shenanigans/cookie-jar-reserves-and-expense-manipulation.md, library/accounting-financial-shenanigans/restatement-analysis.md, library/accounting-financial-shenanigans/segment-reporting-shenanigans.md]
reviewed: 2026-10-01
---

# Classification Shifting -- Special-Item Labels Can Inflate Core Earnings Without Changing Net Income

Classification shifting moves recurring costs out of the operating lines that users treat as core and into categories users exclude from continuing performance, so reported core earnings can improve even when GAAP net income does not. Academic evidence directly documents this mechanism in special items and discontinued operations.[1][2][3] The forensic task is to reconstruct where the cost economically belongs, test whether the label agrees with the underlying activity, and correct the reported performance map without treating every unusual item as manipulation.[5][7][8][10][12]

## Background

Classification shifting is earnings management through presentation rather than through a change in the total amount of earnings. In the canonical form studied by McVay, a company moves expenses that economically belong in cost of goods sold or selling, general, and administrative expense into income-decreasing special items. The same total expense remains in the income statement and bottom-line earnings remain unchanged, but reported core operating earnings and analyst-defined earnings before special items can look stronger.[1] This distinguishes classification shifting from an unsupported accrual that changes net income and from a real operating action, such as cutting research or delaying maintenance, that changes both reported earnings and business activity.[1][2][4]

The mechanism matters because users distinguish recurring earnings from items they expect not to persist. McVay found evidence consistent with managers using special-item classification to meet analyst forecast benchmarks, with special items tending to be excluded from pro forma and analyst earnings definitions. Fan, Barua, Cready, and Thomas reported related quarterly evidence, subject to the model qualification discussed below.[1][2] Management can therefore improve the earnings subtotal that analysts follow without necessarily changing audited net income.

The label "special item" is an analytical and data-provider category rather than a universal line defined by one current U.S. GAAP rule. It can include restructuring charges, impairments, merger and integration costs, litigation items, gains or losses on disposals, and other amounts presented separately or disclosed in notes.[5][6] The category is economically heterogeneous. A factory destroyed by a rare event, a genuinely abandoned product line, and ordinary labor moved into an integration project can all appear outside a user's preferred definition of core earnings, but they do not have the same persistence, cash consequences, or evidentiary quality.[5][7][8]

A special item is not a current U.S. GAAP "extraordinary item." FASB ASU 2015-01 eliminated the extraordinary-item concept for fiscal years, and interim periods within those years, beginning after December 15, 2015. The change removed separate extraordinary-item classification and presentation while retaining applicable presentation or disclosure requirements for events that are unusual, infrequent, or both.[15] Analysts must therefore separate three questions: where GAAP presents the amount, how management labels or excludes it in a supplemental measure, and whether its economics recur.

Regulatory concern predates the modern academic term. In the SEC speech "The Numbers Game," Chairman Arthur Levitt identified big-bath restructuring charges, creative acquisition accounting, cookie-jar reserves, immaterial misapplications, and premature revenue recognition as recurring earnings-management devices. He explained that an overstated restructuring charge can create a cushion that later returns to income when estimates change or future results fall short.[11] The SEC staff's 1999 Staff Accounting Bulletin No. 100 addressed recognition, presentation, and disclosure for restructuring, impairment, and business-combination costs.[10] SAB 103 later removed superseded recognition guidance; the current Staff Accounting Bulletin Codification, Topic 5.P, retains staff views on income-statement classification and disclosure while referring registrants to ASC Topic 420.[12] Under the current ASC 420 model, an exit or disposal liability is recognized and initially measured at fair value when incurred; adopting an exit plan alone does not create the liability, and expected future operating losses are recognized in the periods in which they are incurred.[14]

The reporting rules also constrain particular destinations. FASB ASU 2014-08 amended ASC 205-20 so that an ordinary component disposal is reported in discontinued operations only when it represents a strategic shift with a major effect on operations and financial results, such as disposal of a major geographical area or major line of business. The guidance also requires disclosure of major income and expense classes and reconciliation to the reported after-tax result.[9] There is a separate exception for a business or nonprofit activity classified as held for sale on acquisition; ASU 2023-05 extended that exception to a qualifying activity upon formation of a joint venture for formations on or after January 1, 2025.[13] A routine cost does not become economically discontinued merely because it can be associated with an operation being sold, and costs assigned to a discontinued operation still must belong to that component.

Non-GAAP reporting creates a second classification layer. A cost may be correctly recognized in GAAP operating expense yet removed again from adjusted EBITDA, adjusted operating income, or adjusted EPS. The SEC staff states that excluding normal, recurring cash operating expenses necessary to operate the business can make a non-GAAP performance measure misleading. It also warns about inconsistent treatment across periods and asymmetry, such as excluding nonrecurring charges while retaining comparable gains.[7] Accordingly, a clean GAAP statement does not end the analysis: the reconciliation and the narrative around the excluded item must be tested separately.

DXC Technology illustrates this second layer. The SEC found that DXC negligently classified tens of millions of dollars of internal labor, data-center relocation, audit, lease-standard implementation, and other expenses as transaction, separation, and integration costs even though the items were inconsistent with the company's public description of that adjustment. The classifications did not alter GAAP net income, but they increased the non-GAAP result that management said represented core performance.[8] The case is especially useful because the order identifies both the expense mechanism and the control failure: no adopted non-GAAP policy, weak documentation, incomplete review, ambiguous responsibility between financial planning and controllership, and recurring classifications that rolled forward without reassessment.[8]

Classification shifting is not established by the presence of a large charge, a restructuring, a discontinued operation, an acquisition, or a non-GAAP adjustment alone. Businesses genuinely close facilities, dispose of major operations, settle litigation, impair failed assets, and integrate acquisitions. The author's synthesis is that the forensic question has three layers: whether the accounting classification complies with the governing rule, whether a supplemental performance measure describes the adjustment accurately and consistently, and whether an analyst should treat the cost as part of sustainable economics. A company can pass one layer and fail another; a recurring acquisition cost can be correctly expensed under GAAP yet still be misleadingly removed from the measure used to present core performance.[7][8][9][12][14]

## Core Concepts

### The unchanged bottom line can conceal a changed performance story

Classification shifting exploits the difference between a control total and the components inside it. Suppose a company incurs 100 of ordinary operating expense but reports 30 inside a separately identified restructuring charge. Total pre-tax expense remains 100 and pre-tax net income is unchanged. Reported core operating expense, however, is lower by 30, so core operating profit is higher by 30. If analysts exclude the restructuring charge, the expense disappears from their adjusted bridge and management-adjusted earnings rise by 30. This numerical example is the author's illustration of the mechanism documented in the classification-shifting literature.[1][2]

The unchanged total makes the tactic less visible to tests focused only on net income, total accruals, or cash. A balance-sheet reconciliation can tie, the income statement can add correctly, and total cash can remain unchanged while the location of expense produces a false margin or persistence signal. The analytical object is therefore the line-item map: which function consumed the resource, which line reported the cost, which subtotal excluded it, and which periods ultimately absorbed it.[1][4][5]

The first protection is to preserve several earnings views rather than accept one label. The reported GAAP view shows the official control total. The management-adjusted view reproduces the company's reconciliation exactly. The forensic corrected view restores amounts whose economic function appears recurring or whose stated adjustment category is unsupported, while keeping legitimate transitory items separate. That corrected view is an analyst construction and must remain reversible; it is not a substitute for audited amounts.[5][6][7]

### Special-item abuse can operate through several destinations

The classic destination is an income-decreasing special item. McVay's model tests whether unexpected core earnings rise with such special charges, consistent with ordinary expenses being moved below the core subtotal.[1] Fan and Liu model cost of goods sold and selling, general, and administrative expense separately. They find that cost-of-goods-sold, but not selling, general, and administrative, misclassification is associated with just beating gross margin from four quarters earlier. Both source categories are associated with just beating zero core earnings and prior-year core earnings; the analyst-forecast association is reported for the fourth fiscal quarter.[4]

Restructuring charges create a broad event label under which employee termination, facility closure, contract exit, asset write-down, inventory, consulting, and implementation costs may be grouped. For exit or disposal costs within its scope, ASC 420 recognizes a liability when incurred, not merely when a plan is announced, and recognizes expected future operating losses in the periods in which they occur.[14] Employee benefits, leases, impairments, inventory write-downs, and other components may instead be governed by other applicable Topics; the event label does not override those requirements.[14] The SEC staff's current Topic 5.P states that income-statement classification depends on the nature of each cost and the assets and operations to which it relates; material operating costs generally remain operating expense, with disaggregated disclosure of the plan, liability, classification, cash use, and continuing activities.[12] The forensic risk is not the word "restructuring" itself. It is that future operating costs, ordinary inventory write-downs, costs benefiting continuing operations, or unrelated projects are swept into the event and then excluded from core performance.[10][12][14]

Acquisition and integration categories can perform the same function. Transaction fees can be genuinely deal-specific, but a serial acquirer may incur them as a recurring cost of its operating model. Integration labels can also absorb internal labor, systems work, facility moves, consulting, and other expenses that would have occurred without the deal. DXC's data-center relocation is a direct example: the SEC order states that relocation was required because the landlord would not renew a pre-merger lease, yet the costs were classified as integration expenses in six consecutive quarters.[8] The author's synthesis is that a separate acquisition-accounting analysis remains necessary because purchase allocation, reserves, and later releases can shift expense across periods rather than only across lines.

Discontinued operations place qualifying results below continuing operations. Barua, Lin, and Sbaraglia find evidence consistent with firms moving operating expenses into income-decreasing discontinued operations to increase core earnings and meet or beat analyst forecasts.[3] Current ASC 205-20 generally requires a strategic shift with a major effect, subject to the held-for-sale exceptions for a qualifying business or nonprofit activity on acquisition or joint-venture formation described above.[9][13] The forensic test must address both perimeter and content: whether the component qualifies under the applicable route and whether costs allocated to it were caused by or belong to that component rather than to the continuing business.

### Recurrence is an economic property, not a wording choice

A cost can occur irregularly and still recur as part of the business model. The SEC staff expressly treats an operating expense that occurs repeatedly or occasionally, including at irregular intervals, as recurring for its non-GAAP analysis.[7] A retailer may close stores every year but never the same store twice; a serial acquirer may integrate a different target each year; a technology company may reorganize a different function each quarter. Each event is individually distinct, yet the program can be structurally recurring.

SEC filing rules also impose a narrower labeling test. Item 10(e)(1)(ii)(B), summarized in the staff's Question 102.03, prohibits describing an adjustment as nonrecurring, infrequent, or unusual when a similar charge or gain occurred within the prior two years or is reasonably likely to recur within the next two years.[7] That two-year test governs the label used in filings; it is not a complete economic test of recurrence, which may require a longer history and analysis of differently named but similar costs.

The recurrence test should therefore operate at more than one level. At the exact-label level, track "restructuring" or "integration" across periods. At the economic-family level, combine synonymous labels such as transformation, optimization, strategic realignment, portfolio action, productivity program, and footprint rationalization. At the resource level, ask whether the excluded cost is labor, occupancy, information technology, marketing, supply chain, or another input the continuing business repeatedly consumes. A label change does not reset the economic history. This three-level test is the author's synthesis of the SEC's recurrence standard, the special-item literature, and the DXC control failure.[5][7][8]

Cash status is separate from recurrence. A noncash impairment may reveal a past capital-allocation loss even though it does not require current cash. A cash severance payment may be temporary for one plan but recurrent across a company that continually restructures. An acquisition-related professional fee can be nonrecurring for an occasional buyer and ordinary for a roll-up whose growth depends on deals. The analytical treatment should follow the question being answered: current-period cash, sustainable margin, maintenance investment, or stewardship of prior capital.[5][7]

### Classification shifting differs from accrual and real-activity management

Accrual management changes the timing or measurement of recognized earnings, such as by understating a reserve or extending an asset life. Real-activity management changes operating decisions, such as cutting advertising or overproducing inventory. Classification shifting can leave both the underlying activity and bottom-line earnings unchanged while changing where the result appears.[1][2][4] The three mechanisms can coexist. A company can first capitalize a cost, later impair the asset inside a special charge, and then exclude that charge from adjusted earnings.

This distinction affects detection. A total-accrual model may not identify a pure line-item shift because total expense and total accruals are unchanged. A cash-flow test may not identify it because the same cash outflow occurred. A core-earnings expectation model can identify a statistical pattern, but model specification matters. Fan and colleagues removed contemporaneous accruals from expected core earnings and interpreted a less-negative fourth-quarter special-item coefficient as stronger evidence of shifting. Abdalla and Clubb argue that total accruals are an important performance control and instead modify the coefficient to correct the separate upward bias caused when accruals related to shifted expense also enter total accruals.[2][6]

No statistical model identifies a particular journal entry or proves intent. Industry shifts, genuine restructurings, acquisition cycles, declining performance, and large asset disposals can produce special items and unusual core margins together. The proper use of a model is triage: identify companies or periods where reported core earnings and special charges are inconsistent with ordinary drivers, then inspect the underlying disclosures, projects, functions, and subsequent outcomes.[2][5][6]

### Benchmarks and compensation create incentives but not proof

Classification shifting is attractive near a performance threshold because a small change in a preferred subtotal can alter the reported story without changing net income. McVay reports evidence around analyst forecast benchmarks.[1] Fan and colleagues interpret their less-negative special-item coefficient in fourth quarters, together with tests where accrual manipulation appears constrained, as evidence of stronger shifting incentives in those settings.[2] Fan and Liu find that cost-of-goods-sold, but not selling, general, and administrative, misclassification is associated with just beating gross margin from four quarters earlier. Both source categories are associated with zero and prior-year core-earnings benchmarks, and with analyst forecasts in the fourth fiscal quarter.[4]

An analyst should calculate performance before every disputed classification. Determine whether restoring the cost causes the company to miss guidance, reverse margin expansion, fall below prior-year core earnings, miss a compensation target, or lose covenant headroom. The benchmark effect increases investigative priority, but it does not establish that the classification is wrong. A legitimate charge can happen to move a company across a target. Escalation requires evidence that the economic function, rule, disclosure, or internal approval does not support the chosen line.[4][8]

The control environment matters because line-item classification often begins outside the financial-reporting group. Business units code projects, financial planning approves internal adjustments, controllership aggregates the data, and the disclosure committee approves the published reconciliation. DXC demonstrates the danger of divided responsibility: employees assumed another group had performed the substantive review, while thousands of inadequately described line items rolled into the adjustment.[8] The author's assessment is that a classification control must name the owner of the definition, require project-level evidence, and force periodic reassessment rather than let a historical code renew itself.

### Asymmetry exposes a performance objective

A neutral adjustment policy should treat economically similar gains and losses consistently. The SEC staff warns that excluding nonrecurring charges while retaining nonrecurring gains can make a non-GAAP measure misleading.[7] The same principle applies across time. If management excludes integration labor during an acquisition but includes favorable contract settlements, reserve releases, or disposal gains in adjusted earnings, the author's assessment is that the measure is directionally biased and less analytically credible; the pattern does not by itself establish intentional design.

Build an asymmetry matrix with four cells: recurring charges excluded, recurring gains included, nonrecurring charges excluded, and nonrecurring gains excluded. Add a fifth column for definition changes. A measure becomes less credible as unfavorable items migrate out while favorable items remain, especially when the rule changes after the amount becomes large. This matrix is the author's proposed forensic control derived from the SEC's consistency and symmetry guidance.[7]

### Subsequent periods test the original label

Special items create future traces. Restructuring liabilities are paid, reversed, or re-estimated. Facilities close or remain open. Employees depart or are replaced. Integration projects finish or become permanent functions. Impaired assets disappear from the productive base. Discontinued operations stop contributing cash and expense, or continuing involvement persists. Current ASC 420 and the SEC staff's Topic 5.P make restructuring recognition, classification, liability movement, and cash use testable; ASC 205-20 disclosures expose major classes and continuing involvement for discontinued operations.[9][12][14]

A backtest should compare the original plan with later cash spending, liability use, headcount, capacity, margins, savings, and new charges. An unused restructuring accrual can indicate changed circumstances, but repeated releases that support earnings require explanation. A program described as complete while similar costs reappear under a new name weakens the one-time claim. A major disposal whose costs continue inside the surviving business may show that allocations were incomplete or that transition services create continuing economics. The author's synthesis is that the original classification becomes more credible when the forecasted operational change occurs and less credible when only the label changes.[5][8][9][12][14]

### Legitimate unusual items require the same discipline

A valid unusual item should have an identifiable event, a defined perimeter, a supportable amount, a clear relationship between the event and the cost, and a plausible end date. Its disclosure should distinguish cash from noncash effects, show the income-statement location, reconcile opening and closing liabilities when relevant, and explain continuing involvement or future savings without netting unlike effects.[9][12][14]

The decisive question is not whether the item is large or rare. It is whether the continuing business would have incurred the cost absent the identified event. If yes, exclusion requires a stronger economic rationale. If no, the analyst should still test recurrence at the strategy level: repeated acquisitions, annual restructurings, or continuous portfolio turnover can make event-specific costs part of the business model. The author's assessment is that legitimate classification is established by causation and evidence, not by management's adjective.

## Practical Forensic Framework

The following eight-step framework is the author's synthesis of the academic findings, current SEC guidance, FASB amendments, and the DXC enforcement record cited throughout this section. It is designed for public-source forensic review, not as an audit program or a substitute for authoritative accounting analysis.[1][2][4][6][7][8][9][12][13][14]

### 1. Fix the perimeter and preserve every reported view

Collect at least several annual and quarterly periods of the GAAP statements, footnotes, management discussion, earnings releases, investor presentations, acquisition disclosures, discontinued-operation notes, restructuring roll-forwards, and GAAP-to-non-GAAP reconciliations. Preserve the exact definition of every adjusted metric for each period. Do not overwrite old definitions when management changes a label or combines categories.[7][8][9][12]

Create a line-item map from revenue to net income. For each period, record cost of goods sold, each operating-expense class, operating income, separately presented charges, nonoperating items, discontinued operations, taxes, and net income. Then reproduce every management subtotal. If the arithmetic cannot be reproduced, stop and resolve the missing amount before interpreting recurrence or intent.

### 2. Build an adjustment dictionary at the project level

For every special or excluded item, record the public label, internal or footnote description, transaction or plan, responsible function, start date, expected end date, cash status, GAAP line, non-GAAP treatment, tax effect, and prior-period analogues. A broad category such as "transformation" is not a unit of analysis. Split it into labor, consulting, systems, facilities, severance, impairment, legal, marketing, and other components where disclosure permits.[8][12][14]

Apply a causation test: would this resource have been consumed without the named event? Apply a qualification test: does the destination meet the governing reporting rule? Apply a recurrence test at the exact-label, economic-family, and resource levels. Apply a symmetry test to gains and losses. An item that fails one test is a lead, not yet a conclusion.[7][8][9][12][13][14]

### 3. Reconstruct core margins before and after disputed shifts

Restore suspected cost to the functional line from which it appears to have moved. Internal labor returns to the function employing the labor. Historical SAB 100 explicitly placed inventory write-downs in cost of goods sold, while current Topic 5.P applies the broader rule that classification follows the nature of the charge and the assets and operations to which it relates.[10][12] Continuing-business technology or occupancy cost returns to the operating line that consumes it. Show reported gross margin, operating margin, management-adjusted margin, and forensic corrected margin side by side.[8]

Do not place every special charge into selling, general, and administrative expense by default. Fan and Liu show why source-line identification matters: cost-of-goods-sold and selling, general, and administrative shifting can target different benchmarks.[4] Use payroll function, vendor scope, asset location, project ownership, segment usage, and prior classification to determine the most supportable destination. If the source line is uncertain, present a range and state which subtotals change under each allocation.

### 4. Build a multi-period recurrence ledger

The author's proposed review horizon is three to five years or a full business cycle. Sum exclusions by label, economic family, and resource over that period. Calculate each category as a percentage of revenue, reported operating expense, operating income, acquisition spending, and management-adjusted earnings. Record whether the company would have missed an announced target without the exclusion. A cost that is individually small can still be decision-relevant when it closes a benchmark gap.[1][2][4]

Track programs through renaming. "Restructuring," "optimization," "transformation," and "strategic actions" may be separate plans or successive names for the same operating adaptation. The ledger should preserve both management's categories and the analyst's economic groupings. The latter must be explicitly labeled as synthesis.

### 5. Reconcile notes, cash flow, and balance-sheet traces

Trace cash spending to operating, investing, and financing sections and reconcile noncash charges separately. Build liability roll-forwards for restructuring, severance, contract exits, and other accrued programs: opening balance, new charges, cash use, noncash use, reversals, acquisition effects, reclassifications, and ending balance.[12][14] Compare asset impairments with asset disposals, depreciation, capacity, and later operating performance.

The author's synthesis is that cash does not validate classification by itself. A recurring operating cost can be cash or noncash; a genuine unusual event can consume cash over several years. The purpose of cash reconciliation is to identify whether management's narrative matches settlement and whether adjusted earnings exclude costs that the continuing business repeatedly pays.

### 6. Test acquisition and discontinued-operation boundaries

For acquisition exclusions, tie each cost to a named transaction, contract, workstream, and expected integration period. Separate transaction execution from continuing operations and from projects that predated or would have occurred without the deal. For serial acquirers, compare cumulative excluded acquisition costs with acquisition activity and post-deal operating results.[8]

For discontinued operations, test the strategic-shift route and the acquisition or joint-venture-formation exceptions, then reconcile major income and expense classes to the after-tax result.[9][13] Compare transition-service agreements, stranded overhead, continuing guarantees, and shared systems with the allocation between disposed and continuing operations.

### 7. Backtest promised savings and subsequent reversals

Record management's stated savings, timing, headcount reduction, facility closures, and completion date. In later periods, compare actual cash use, expense run rate, staffing, capacity, and new special charges with the original plan. A charge can be legitimate even if savings disappoint, but an unsupported liability, unrelated cost, or recurring replacement program changes the classification assessment.[8][10][12][14]

Preserve the original information set to avoid hindsight bias. Later underperformance does not prove the original estimate was dishonest. Stronger evidence includes contemporaneous internal or contractual descriptions that contradict the public label, costs known to be necessary without the stated event, unsupported approvals, or repeated exceptions that consistently improve the same subtotal.[8]

### 8. Preserve a reversible corrected earnings bridge

Begin with reported GAAP earnings and reproduce management's own adjusted bridge. Then show a separate forensic correction that returns only evidence-supported amounts to the functional line from which they were shifted. Keep cash, noncash, tax, and period effects visible. A recurring expense may belong in corrected core earnings even when its GAAP recognition is valid; a valid impairment may remain outside current operating cash while still informing the interpretation of earlier capital allocation.[5][7]

Do not invent a precise source line when disclosure is insufficient. Present a bounded allocation range, identify which subtotals change under each case, and state the missing evidence that would resolve the range. Preserve the reported, management-adjusted, and forensic corrected views so another reader can reverse every analytical decision. The objective is to reconstruct economic function and reporting location, not to replace one opaque adjusted measure with another.

## Evidence

### McVay established the modern classification-shifting test

McVay examined income-statement classification as an earnings-management tool. Her study reports evidence consistent with managers moving expenses from cost of goods sold and selling, general, and administrative expense into special items. The movement leaves bottom-line earnings unchanged but overstates core earnings. The study also reports that the behavior appears associated with meeting analyst forecast benchmarks because special items tend to be excluded from pro forma and analyst earnings definitions.[1]

The design estimates expected core earnings and tests whether unexpected core earnings increase with income-decreasing special items. The interpretation is intuitive: if a charge contains ordinary expense that would otherwise reduce core earnings, reported core earnings will be unusually high when the charge is large. The limitation is equally important. Performance and accruals can mechanically connect special items with core profitability, so the statistical relation is evidence of a population pattern rather than identification of a particular company's shifted invoice or payroll entry.[1][2][6]

### Quarterly evidence identifies timing and substitution incentives

Fan, Barua, Cready, and Thomas remove contemporaneous accruals from their expected-core-earnings model because the original positive relation disappears under that specification. Their aggregate special-item coefficient is negative; they interpret its less-negative value in fourth quarters, along with stronger relative results when accrual management appears constrained and around several earnings benchmarks, as evidence consistent with classification shifting.[2] Abdalla and Clubb later argue that omitting total accruals removes an important performance control and propose a separate correction for shifted-expense accruals within total accruals.[6] The evidence is therefore specification-sensitive and should not be described as an unqualified positive coefficient.

The fourth-quarter result supports the author's targeted procedure: compare annual results with the first three quarters, calculate the implied fourth quarter, and inspect year-end special charges. It does not establish that every fourth-quarter charge is opportunistic. Annual testing, audit completion, acquisition timing, and real year-end decisions can also concentrate legitimate charges in that quarter; those alternatives must be tested against the underlying event rather than assumed.[2]

### Discontinued operations and source expense lines broaden the mechanism

Barua, Lin, and Sbaraglia apply a method similar to McVay's to discontinued operations. They find evidence consistent with companies shifting operating expenses into income-decreasing discontinued operations to increase core earnings and meet or beat analyst forecasts. They also report that discontinued-operation reporting became more frequent after SFAS 144 while the magnitude of estimated shifting declined.[3] The author's synthesis is that classification analysis must inspect any category placed outside continuing performance, while recognizing that this study directly tests discontinued operations rather than every possible exclusion.

Fan and Liu separate cost of goods sold from selling, general, and administrative expense. They find that cost-of-goods-sold, but not selling, general, and administrative, misclassification is associated with just beating gross margin from four quarters earlier. Both source categories are associated with just beating zero core earnings and prior-year core earnings, and with analyst forecasts in the fourth fiscal quarter.[4] This evidence supports function-specific reconstruction rather than a single adjustment to total operating expense.

### Opportunistic special items predict weaker future outcomes

Cain, Kolev, and McVay document that special-item frequency increased over time and propose a method that predicts a normal level of special items from economic drivers, treating the excess as an opportunistic component. They report that this opportunistic portion is associated with lower future earnings, future cash flows, and future stock returns, consistent with recurring expenses being inappropriately classified as nonrecurring.[5] The finding is directly relevant to corrected core earnings: removing the entire charge can overstate sustainable earnings when part of the amount belongs to the continuing cost base.

The author's methodological assessment is that the model remains a screen rather than a transaction audit. A statistically excessive special item can reflect an omitted economic driver, unusual industry shock, or measurement error. The forensic response is to inspect the components and backtest them, not to label the residual fraudulent. Conversely, the absence of a statistical flag does not validate the classification of a material item whose contract, function, or disclosure is contradictory.

### Later research refines measurement and links shifting to restatements

Abdalla and Clubb use 72,568 firm-year observations from 1989 through 2017 as their full classification-shifting estimation sample and develop a modified model that retains total accruals as a performance control while correcting the separate bias created by shifted-expense accruals within total accruals.[6] Their future-earnings tests use 38,118 observations and find that estimated shifted core expenses have forecasting relevance statistically indistinguishable from current earnings before special items. Their principal restatement tests use 27,704 observations from 2000 through 2017; estimated shifted core expense is associated with later restatement of the current firm-year, while adjusted special charges are not significant. The special-item-linked subset is identified from keywords in Audit Analytics descriptions, not from transaction-level proof.[6]

This partition supports a bounded conclusion: a special charge can contain both a recurring core component and a more transitory component. Treating the entire amount as either recurring or nonrecurring destroys information. The research also reinforces model risk. Results depend on expected-core-earnings specification, industry estimation, accrual controls, bounding assumptions, and the keyword-based restatement classification. Transaction-level evidence remains necessary for a company-specific conclusion.[6]

### The DXC order shows the mechanism in operating detail

The SEC's settled DXC order provides primary evidence of classification abuse in non-GAAP reporting. The Commission found that DXC negligently misclassified tens of millions of dollars as transaction, separation, and integration costs and thereby overstated non-GAAP net income by at least $29 million in the second quarter of fiscal 2019, $30 million in the fourth quarter of fiscal 2019, and $24 million in the first quarter of fiscal 2020. Reported non-GAAP net income for those quarters was $573 million, $589 million, and $472 million, respectively.[8]

The underlying costs expose the forensic tests. DXC included internal labor and tax expense, more than $38 million of data-center relocation cost over six consecutive quarters, required audit fees, implementation cost for a new lease standard, potential-divestiture expenses, and part of a litigation settlement. The data-center move was required because a pre-merger landlord would not renew the lease, so the expense would have arisen regardless of the merger.[8] Contract scope, pre-event history, recurrence, and ordinary operating necessity contradicted the integration label.

The order also documents process evidence. Business units were not required to document how proposed costs related to a transaction, how long they would continue, or why they qualified. Financial planning and controllership held inconsistent assumptions about which group performed the substantive review. Reviewers received spreadsheets with tens of thousands of line items, incomplete descriptions, and insufficient time, while questions about unsupported classifications remained unresolved before filing.[8] This evidence supports project-level approval, clear ownership, written rationale, and periodic reassessment as controls against classification drift.

### Reporting guidance makes several tests reproducible

The SEC's non-GAAP interpretations make recurrence, consistency, symmetry, description, and presentation testable. Excluding a normal recurring cash operating expense may mislead; an occasional operating expense can still be recurring; changing the treatment of similar items across periods requires explanation and possibly recasting; and excluding charges while retaining similar gains can violate Regulation G.[7] Detailed disclosure does not necessarily cure a measure that is materially misleading.[7]

ASU 2014-08 supplies the strategic-shift route, major-class disclosures, and reconciliation requirements for discontinued operations; ASU 2023-05 confirms the separate held-for-sale route for a qualifying business or nonprofit activity on acquisition or joint-venture formation.[9][13] Current ASC 420 supplies the recognition model for exit and disposal liabilities, while the SEC staff's Topic 5.P retains classification and disclosure guidance for restructuring charges.[12][14] Together these sources make the plan, liability, cost function, cash use, and discontinued-operation perimeter testable. They do not eliminate judgment, but they convert a vague concern about "one-time items" into a defined evidence request.

## Implications

The implications below are the author's synthesis of the academic evidence, reporting guidance, and enforcement record. They concern detection, correction, and control of classification shifting; they do not prescribe an audit or a general valuation method.[1][2][4][5][6][7][8][9][12][14]

### Investors should preserve a corrected earnings bridge

For investors, the central implication is that adjusted earnings should be reconstructed rather than accepted or rejected wholesale. A useful adjustment isolates a genuinely transitory event. Classification abuse instead asks users to treat ordinary burdens as if they were outside the continuing operation. The distinction requires evidence about the resource consumed, the line in which the cost appeared, the exclusion used in the promoted subtotal, recurrence under other labels, cash settlement, and subsequent operating outcomes.[5][7][8]

The review should preserve three views. The first is reported GAAP, which supplies the control total. The second reproduces management's adjusted measure exactly, including every label and tax effect. The third is a forensic correction that returns only supported shifted amounts to their economic function. If internal labor was described as integration work even though employees would have performed the work without the transaction, the corrected view returns that labor to the operating function. If part of a restructuring charge represents a qualifying closure obligation and another part represents future operating work, the two components should not receive one treatment.[8][12][14]

The corrected bridge should show which subtotals change and which do not. A pure line-item shift can leave GAAP net income, total expense, and total cash unchanged while overstating core operating earnings.[1] A non-GAAP exclusion can leave the GAAP statement correct while making the supplemental measure misleading.[7][8] A discontinued-operation shift can move cost outside continuing results while leaving consolidated net income unchanged.[3] Keeping these mechanisms separate prevents an analyst from converting a presentation problem into an unsupported allegation that total earnings or cash were misstated.

Recurrence should be tested by resource and economic family, not only by public label. Repeated employee, facility, systems, or transaction work remains visible when "restructuring" becomes "optimization" or "transformation." The SEC staff's two-year labeling rule provides a minimum filing test, but economic recurrence can extend beyond that window or appear under different names.[7] Cain, Kolev, and McVay's finding that estimated opportunistic special items are associated with lower future earnings, future cash flows, and future stock returns supports treating recurring exclusions as a signal requiring component-level review rather than automatic removal from core performance.[5]

The author's proposed inversion is to ask what cost must actually cease for the promoted margin to persist. If the answer is continuing employees, facilities, systems, compliance work, or repeated deal execution, the burden has not disappeared; only its reporting or analytical location changed. If the answer is a closed plant, settled claim, or disposed major operation with no replacement cost, exclusion is more defensible. When disclosure cannot resolve the split, the correct output is a range with stated missing evidence, not a fabricated point estimate.

### Boards and management need a classification control, not a vocabulary list

Management can make legitimate adjustments more credible by defining them before the result is known. The author's proposed non-GAAP policy specifies eligible and ineligible cost types, evidence requirements, approval authority, duration, treatment of internal labor and gains, tax effects, and recasting rules when definitions change. Each adjustment links to a project, contract, ledger population, accountable owner, and expected completion date. A recurring project code should require reassessment rather than automatic renewal. These controls respond directly to the weak documentation, absent policy, divided responsibility, and unreassessed classifications documented in the DXC order.[8]

The disclosure committee should receive gross components rather than only an aggregated adjustment. For each component, it should see the GAAP line, amount, cash status, prior-period analogue, stated reason for exclusion, and effect on every published measure. It should also see contrary evidence and unresolved questions. DXC's order shows why informal explanations and assumptions that another group performed the substantive review are not adequate classification controls.[8] The SEC staff's guidance adds objective checks for recurring cash operating costs, interperiod consistency, symmetry between charges and gains, clear labels, and prominence of the comparable GAAP measure.[7]

Boards should connect restructuring approval with later evidence. The original record should identify the plan, liability, cost types, income-statement location, expected cash use, completion criteria, and continuing operations. Later reviews should compare actual liability use, cash spending, staffing, facility closure, and new programs with that record. Current ASC 420 recognition occurs when a qualifying liability is incurred rather than when management merely commits to a plan, while the SEC staff's Topic 5.P preserves classification and disclosure tests based on the nature of each cost.[12][14] The purpose of backtesting is not to punish an estimate that changed honestly; it is to detect unsupported accruals, unrelated costs, repeated replacement programs, and labels whose operational premise never occurred.

Compensation committees should determine whether a bonus or performance target depends on a subtotal that management can change through classification. A metric that excludes management-approved special items gives the same decision makers influence over both the target and the adjustments. Independent approval, pre-defined rules, symmetric treatment, and a complete bridge to GAAP reduce that conflict. Evidence that classification shifting is associated with analyst, core-earnings, gross-margin, and fourth-quarter benchmarks makes this governance question material, while proximity to a target alone remains insufficient to prove misconduct.[1][2][4]

### Regulators and public-source reviewers should screen, then corroborate

Regulators and public-source reviewers can screen longitudinal filings for recurring exclusions, fourth-quarter concentration, benchmark-closing amounts, widening gaps between GAAP and adjusted results, renamed adjustment families, discontinued-operation allocations, and changed non-GAAP definitions. Statistical models can also rank unusual relationships between special items and core earnings. These screens allocate attention; they do not identify a false journal entry or managerial intent. The model evidence is sensitive to expected-core-earnings specification, accrual controls, industry estimation, bounding choices, and restatement classification.[2][6]

A stronger conclusion connects the public label to underlying work. Relevant evidence includes the named plan or transaction, contract scope, cost function, timing, cash settlement, later reversals, continuing use of the resource, and consistency with the applicable reporting rule. The DXC order demonstrates this progression: the classification concern became supportable because the underlying data-center move, internal labor, audit fees, lease-standard work, incomplete documentation, and repeated approvals contradicted the public transaction-and-integration description.[8] The enforcement lesson is not that every integration cost is ordinary; it is that the label requires evidence of causation.

Reviewers should also search for disconfirming evidence. A discrete external event, a closed and settled plan, a cost population that ends, symmetric treatment of gains and losses, and operations that no longer consume the resource all support an unusual-item description.[7][9][12] Later underperformance alone does not prove that the original classification was wrong. The evidence should be evaluated as it existed at the classification date, then updated with later settlement and operating facts.

### Analysts must distinguish correction from interpretation

The author's synthesis separates three decisions. First, GAAP classification may require correction when the amount was placed outside the line or period required by the governing accounting. Second, a GAAP-correct expense may still be misleadingly described or excluded in a non-GAAP measure under Regulation G or Item 10(e).[7] Third, a supportable reported and supplemental classification may still be economically recurring, which affects the interpretation of core performance without establishing a reporting violation. These decisions should never be collapsed into one accusation.

Use graded outcomes. "Supported unusual item" means the event, perimeter, amount, line, and end date reconcile. "Recurring economic burden" means reporting is supportable but the cost family continues and should remain visible in core-performance analysis. "Aggressive presentation" means judgments and labels repeatedly favor the promoted subtotal within an arguable range. "Likely error" means the classification conflicts with the reporting rule or underlying function. "Evidence consistent with manipulation" requires converging facts such as unsupported coding, contradictory contracts, target-sized entries, concealed recurrence, or a deliberate mismatch between policy and disclosure.[7][8][9][12][14]

The final safeguard is reversibility. A forensic method that returns every charge to core earnings is as unreliable as a management measure that excludes every unfavorable charge. Preserve reported amounts, management adjustments, the forensic correction, contrary evidence, and uncertainty separately. The objective is a reproducible map of economic function and reporting location, not a predetermined lower earnings number.

## Sources

1. McVay, S. E. (2006). "Earnings Management Using Classification
   Shifting: An Examination of Core Earnings and Special Items."
   The Accounting Review, 81(3), 501-531.
   https://doi.org/10.2308/accr.2006.81.3.501 [high]

2. Fan, Y., Barua, A., Cready, W. M., and Thomas, W. B. (2010).
   "Managing Earnings Using Classification Shifting: Evidence from
   Quarterly Special Items." The Accounting Review, 85(4), 1303-1323.
   https://doi.org/10.2308/accr.2010.85.4.1303 [high]

3. Barua, A., Lin, S., and Sbaraglia, A. M. (2010). "Earnings
   Management Using Discontinued Operations." The Accounting Review,
   85(5), 1485-1509.
   https://doi.org/10.2308/accr.2010.85.5.1485 [high]

4. Fan, Y., and Liu, X. K. (2017). "Misclassifying Core Expenses as
   Special Items: Cost of Goods Sold or Selling, General, and
   Administrative Expenses?" Contemporary Accounting Research, 34(1),
   400-426. https://doi.org/10.1111/1911-3846.12234 [high]

5. Cain, C. A., Kolev, K. S., and McVay, S. E. (2020). "Detecting
   Opportunistic Special Items." Management Science, 66(5), 2099-2119.
   https://doi.org/10.1287/mnsc.2019.3285 [high]

6. Abdalla, A. M., and Clubb, C. D. B. (2024). "Classification Shifting
   Using Income-Decreasing Special Items: Measurement and Valuation
   Issues." Review of Accounting Studies, 29, 2871-2926.
   https://doi.org/10.1007/s11142-023-09770-z [high]

7. U.S. Securities and Exchange Commission, Division of Corporation
   Finance. "Non-GAAP Financial Measures," Corporation Finance
   Interpretations. Page dated June 7, 2021; last updated December 13,
   2022. https://www.sec.gov/corpfin/non-gaap-financial-measures [high]

8. U.S. Securities and Exchange Commission (2023). "In the Matter of
   DXC Technology Company." Securities Act Release No. 11166; Exchange
   Act Release No. 97140; Accounting and Auditing Enforcement Release
   No. 4391. https://www.sec.gov/files/litigation/admin/2023/33-11166.pdf [high]

9. Financial Accounting Standards Board (2014). "Accounting Standards
   Update 2014-08: Presentation of Financial Statements (Topic 205) and
   Property, Plant, and Equipment (Topic 360), Reporting Discontinued
   Operations and Disclosures of Disposals of Components of an Entity."
   Historical update amending ASC 205-20.
   https://storage.fasb.org/ASU%202014-08.pdf [high]

10. U.S. Securities and Exchange Commission (1999). "Staff Accounting
    Bulletin No. 100 -- Restructuring and Impairment Charges." Historical
    staff guidance published at 64 FR 67154-67163.
    https://www.govinfo.gov/content/pkg/FR-1999-12-01/html/99-31160.htm [high]

11. Levitt, A. (1998). "The Numbers Game." Remarks to the NYU Center
    for Law and Business, September 28, 1998.
    https://www.sec.gov/newsroom/speeches-statements/spch220-numbers-game [high]

12. U.S. Securities and Exchange Commission, Office of the Chief
    Accountant. "Staff Accounting Bulletin Codification, Topic 5.P:
    Restructuring Charges." Current staff presentation and disclosure
    guidance, including references to ASC Topic 420.
    https://www.sec.gov/oca/sab-code-t5 [high]

13. Financial Accounting Standards Board (2023). "Accounting Standards
    Update 2023-05: Business Combinations -- Joint Venture Formations
    (Subtopic 805-60), Recognition and Initial Measurement." Amendment
    to ASC 205-20-45-1D effective for joint ventures formed on or after
    January 1, 2025.
    https://storage.fasb.org/ASU%202023-05.pdf [high]

14. Ernst & Young (2026). "Financial Reporting Developments: Exit or
    Disposal Cost Obligations." Current technical guide reproducing and
    explaining ASC Topic 420 recognition, measurement, presentation, and
    disclosure requirements.
    https://www.ey.com/content/dam/ey-unified-site/ey-com/en-us/technical/accountinglink/documents/ey-frdbb1072-05-28-2026.pdf [high]

15. Financial Accounting Standards Board (2015). "Accounting Standards
    Update 2015-01: Income Statement -- Extraordinary and Unusual Items
    (Subtopic 225-20), Simplifying Income Statement Presentation by
    Eliminating the Concept of Extraordinary Items."
    https://storage.fasb.org/ASU%202015-01.pdf [high]

## See Also

- `library/accounting-financial-shenanigans/non-gaap-metrics-and-pro-forma-manipulation.md` -- the broader framework for testing adjusted measures, recurring exclusions, and reconciliation quality.
- `library/accounting-financial-shenanigans/forensic-accounting-methodology.md` -- the evidence hierarchy and cross-statement process for moving from an anomaly to a supported conclusion.
- `library/accounting-financial-shenanigans/acquisition-accounting-tricks.md` -- purchase accounting, integration costs, reserves, and other acquisition boundaries that can shift reported expense.
- `library/accounting-financial-shenanigans/cookie-jar-reserves-and-expense-manipulation.md` -- reserve builds, releases, big baths, and capitalization that shift expense across periods rather than only across lines.
- `library/accounting-financial-shenanigans/restatement-analysis.md` -- how later corrections reveal the period, account, classification, and control failure behind prior reporting.
- `library/accounting-financial-shenanigans/segment-reporting-shenanigans.md` -- cost allocation and corporate columns that can flatter a promoted business without changing consolidated earnings.

