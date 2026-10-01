---
name: classification-shifting-and-special-item-abuse
id: 20261001T093704Z
tier: library-topic
domain: accounting-financial-shenanigans
author: Librarian
tags: [classification-shifting, special-items, core-earnings, restructuring-charges, discontinued-operations, non-gaap, forensic-accounting]
links: [library/accounting-financial-shenanigans/non-gaap-metrics-and-pro-forma-manipulation.md, library/accounting-financial-shenanigans/forensic-accounting-methodology.md, library/accounting-financial-shenanigans/acquisition-accounting-tricks.md, library/accounting-financial-shenanigans/cookie-jar-reserves-and-expense-manipulation.md, library/accounting-financial-shenanigans/restatement-analysis.md, library/accounting-financial-shenanigans/segment-reporting-shenanigans.md]
---

# Classification Shifting -- Special-Item Labels Can Inflate Core Earnings Without Changing Net Income

Classification shifting moves recurring costs out of the operating lines that users treat as core and into special, discontinued, acquisition-related, restructuring, or other excluded categories, so reported core performance improves even when GAAP net income does not.[1][2][3] The forensic task is to reconstruct where the cost economically belongs, test whether the label agrees with the underlying activity, and normalize recurring economics without treating every unusual item as manipulation.[5][7][8][10]

## Background

Classification shifting is earnings management through presentation rather than through a change in the total amount of earnings. In the canonical form studied by McVay, a company moves expenses that economically belong in cost of goods sold or selling, general, and administrative expense into income-decreasing special items. The same total expense remains in the income statement and bottom-line earnings remain unchanged, but operating margin, core earnings, earnings before special items, and management-defined adjusted results can all look stronger.[1] This distinguishes classification shifting from an unsupported accrual that changes net income and from a real operating action, such as cutting research or delaying maintenance, that changes both reported earnings and business activity.[1][2][4]

The mechanism matters because financial-statement users do not weight every income-statement line equally. Core or recurring earnings are commonly used to forecast sustainable profitability, while a charge described as special or nonrecurring is more likely to be excluded from forecasts and valuation multiples. McVay found evidence consistent with managers using this difference in treatment to meet analyst forecast benchmarks, and Fan, Barua, Cready, and Thomas later found broader quarterly evidence, especially in the fourth quarter and when other forms of accrual management appeared constrained.[1][2] The attraction is therefore simple: management can improve the subtotal that investors emphasize without necessarily changing the audited bottom line.

The label "special item" is an analytical and data-provider category rather than a universal line defined by one current U.S. GAAP rule. It can include restructuring charges, impairments, merger and integration costs, litigation items, gains or losses on disposals, and other amounts presented separately or disclosed in notes.[5][6] The category is economically heterogeneous. A factory destroyed by a rare event, a genuinely abandoned product line, and ordinary labor moved into an integration project can all appear outside a user's preferred definition of core earnings, but they do not have the same persistence, cash consequences, or evidentiary quality.[5][7][8]

Regulatory concern predates the modern academic term. In the SEC speech "The Numbers Game," Chairman Arthur Levitt identified big-bath restructuring charges, creative acquisition accounting, cookie-jar reserves, immaterial misapplications, and premature revenue recognition as recurring earnings-management devices. He explained that an overstated restructuring charge can create a cushion that later returns to income when estimates change or future results fall short.[11] Staff Accounting Bulletin No. 100 then addressed recognition, income-statement placement, and disclosure of restructuring, impairment, and business-combination costs. It emphasized disaggregation, precise labeling, the classification of inventory write-downs in cost of goods sold, and disclosure of amounts accrued, paid, and charged against exit liabilities.[10]

The reporting rules also constrain particular destinations. FASB Accounting Standards Update 2014-08 narrowed discontinued-operation presentation to a disposal that represents a strategic shift with a major effect on operations and financial results, such as disposal of a major geographical area or major line of business. It also requires disclosure of the major income and expense classes within a discontinued operation and reconciliation to the reported after-tax result.[9] A routine cost does not become economically discontinued merely because it can be associated with an operation that is being sold, and a disposal that fails the strategic-shift threshold does not qualify for discontinued-operation presentation under that guidance.[9]

Non-GAAP reporting creates a second classification layer. A cost may be correctly recognized in GAAP operating expense yet removed again from adjusted EBITDA, adjusted operating income, or adjusted EPS. The SEC staff states that excluding normal, recurring cash operating expenses necessary to operate the business can make a non-GAAP performance measure misleading. It also warns about inconsistent treatment across periods and asymmetry, such as excluding nonrecurring charges while retaining comparable gains.[7] Accordingly, a clean GAAP statement does not end the analysis: the reconciliation and the narrative around the excluded item must be tested separately.

DXC Technology illustrates this second layer. The SEC found that DXC negligently classified tens of millions of dollars of internal labor, data-center relocation, audit, lease-standard implementation, and other expenses as transaction, separation, and integration costs even though the items were inconsistent with the company's public description of that adjustment. The classifications did not alter GAAP net income, but they increased the non-GAAP result that management said represented core performance.[8] The case is especially useful because the order identifies both the expense mechanism and the control failure: no adopted non-GAAP policy, weak documentation, incomplete review, ambiguous responsibility between financial planning and controllership, and recurring classifications that rolled forward without reassessment.[8]

Classification shifting is not established by the presence of a large charge, a restructuring, a discontinued operation, an acquisition, or a non-GAAP adjustment alone. Businesses genuinely close facilities, dispose of major operations, settle litigation, impair failed assets, and integrate acquisitions. The author's synthesis is that the forensic question has three layers: whether the accounting classification complies with the governing rule, whether a supplemental performance measure describes the adjustment accurately and consistently, and whether an analyst should treat the cost as part of sustainable economics. A company can pass one layer and fail another; a recurring acquisition cost can be correctly expensed under GAAP yet still be misleadingly removed from the measure used to sell the earnings story.[7][8][9][10]

## Core Concepts

### The unchanged bottom line can conceal a changed performance story

Classification shifting exploits the difference between a control total and the components inside it. Suppose a company incurs 100 of ordinary operating expense but reports 30 inside a separately identified restructuring charge. Total pre-tax expense remains 100 and pre-tax net income is unchanged. Reported core operating expense, however, is lower by 30, so core operating profit is higher by 30. If analysts exclude the restructuring charge from adjusted earnings, the same 30 also disappears from the denominator used for a valuation multiple. This numerical example is the author's illustration of the mechanism documented in the classification-shifting literature.[1][2]

The unchanged total makes the tactic less visible to tests focused only on net income, total accruals, or cash. A balance-sheet reconciliation can tie, the income statement can add correctly, and total cash can remain unchanged while the location of expense produces a false margin or persistence signal. The analytical object is therefore the line-item map: which function consumed the resource, which line reported the cost, which subtotal excluded it, and which periods ultimately absorbed it.[1][4][5]

The first protection is to preserve several earnings views rather than accept one label. The reported GAAP view shows the official statement. The management-adjusted view reproduces the company's reconciliation exactly. The forensic view restores amounts whose economic function appears recurring or whose stated adjustment category is unsupported. The normalized valuation view then separates errors or aggressive classifications from legitimate but transitory items. The last two are analyst constructions and must remain reversible; they are not substitutes for audited amounts.[5][6][7]

### Special-item abuse can operate through several destinations

The classic destination is an income-decreasing special item. McVay's model tests whether unexpected core earnings rise with such special charges, consistent with ordinary expenses being moved below the core subtotal.[1] Fan and Liu disaggregate the source lines and find different benchmark patterns for cost of goods sold and selling, general, and administrative expense. Cost-of-goods-sold shifting is particularly relevant to gross-margin benchmarks, while both expense classes are implicated around core-earnings and analyst-forecast benchmarks.[4]

Restructuring charges create a broad event label under which employee termination, facility closure, contract exit, asset write-down, inventory, consulting, and implementation costs may be grouped. SAB No. 100 states that the charge must follow the accounting applicable to each underlying cost and calls for disaggregated disclosure of the plan, liability, expense classification, cash use, and continuing activities.[10] The forensic risk is not the word "restructuring" itself. It is that costs benefiting continuing operations, future operating costs, ordinary inventory write-downs, or unrelated projects are swept into the event and then excluded from core performance.[10][11]

Acquisition and integration categories can perform the same function. Transaction fees can be genuinely deal-specific, but a serial acquirer may incur them as a recurring cost of its operating model. Integration labels can also absorb internal labor, systems work, facility moves, consulting, and other expenses that would have occurred without the deal. DXC's data-center relocation is a direct example: the SEC order states that relocation was required because the landlord would not renew a pre-merger lease, yet the costs were classified as integration expenses in six consecutive quarters.[8] The dedicated acquisition-accounting analysis remains necessary because purchase allocation, reserves, and later releases can also shift expense across periods rather than merely across lines.

Discontinued operations place qualifying results below continuing operations. Barua, Lin, and Sbaraglia find evidence consistent with firms moving operating expenses into income-decreasing discontinued operations to increase core earnings and meet or beat analyst forecasts.[3] Current U.S. guidance makes the classification boundary more restrictive: the disposal must represent a strategic shift with a major effect, and major income and expense classes must be disclosed.[9] The forensic test must therefore address both perimeter and content: whether the disposed component qualifies, and whether costs allocated to it were caused by or belong to that component rather than to the continuing business.

Corporate, unallocated, or "other" columns can create a related but distinct presentation effect. A recurring shared cost may be removed from a promoted segment while remaining in consolidated GAAP expense. That does not necessarily change company-wide core earnings, but it can inflate the margin of a business unit that management highlights. Segment-reporting analysis therefore complements special-item analysis: reconcile the consolidated total, then test whether allocation, aggregation, and non-GAAP exclusions move burdens away from the business presented as the growth engine.[8]

### Recurrence is an economic property, not a wording choice

A cost can occur irregularly and still recur as part of the business model. The SEC staff expressly treats an operating expense that occurs repeatedly or occasionally, including at irregular intervals, as recurring for its non-GAAP analysis.[7] A retailer may close stores every year but never the same store twice; a serial acquirer may integrate a different target each year; a technology company may reorganize a different function each quarter. Each event is individually distinct, yet the program can be structurally recurring.

The recurrence test should therefore operate at more than one level. At the exact-label level, track "restructuring" or "integration" across periods. At the economic-family level, combine synonymous labels such as transformation, optimization, strategic realignment, portfolio action, productivity program, and footprint rationalization. At the resource level, ask whether the excluded cost is labor, occupancy, information technology, marketing, supply chain, or another input the continuing business repeatedly consumes. A label change does not reset the economic history. This three-level test is the author's synthesis of the SEC's recurrence standard, the special-item literature, and the DXC control failure.[5][7][8]

Cash status is separate from recurrence. A noncash impairment may reveal a past capital-allocation loss even though it does not require current cash. A cash severance payment may be temporary for one plan but recurrent across a company that continually restructures. An acquisition-related professional fee can be nonrecurring for an occasional buyer and ordinary for a roll-up whose growth depends on deals. The analytical treatment should follow the question being answered: current-period cash, sustainable margin, maintenance investment, or stewardship of prior capital.[5][7]

### Classification shifting differs from accrual and real-activity management

Accrual management changes the timing or measurement of recognized earnings, such as by understating a reserve or extending an asset life. Real-activity management changes operating decisions, such as cutting advertising or overproducing inventory. Classification shifting can leave both the underlying activity and bottom-line earnings unchanged while changing where the result appears.[1][2][4] The three mechanisms can coexist. A company can first capitalize a cost, later impair the asset inside a special charge, and then exclude that charge from adjusted earnings.

This distinction affects detection. A total-accrual model may not identify a pure line-item shift because total expense and total accruals are unchanged. A cash-flow test may not identify it because the same cash outflow occurred. A core-earnings expectation model can identify a statistical pattern, but model specification matters. Fan and colleagues noted that the relation in the original design can be sensitive to how contemporaneous accruals enter expected core earnings, and Abdalla and Clubb later proposed a modified approach to address mechanical association and separate shifted core expense from adjusted special items.[2][6]

No statistical model identifies a particular journal entry or proves intent. Industry shifts, genuine restructurings, acquisition cycles, declining performance, and large asset disposals can produce special items and unusual core margins together. The proper use of a model is triage: identify companies or periods where reported core earnings and special charges are inconsistent with ordinary drivers, then inspect the underlying disclosures, projects, functions, and subsequent outcomes.[2][5][6]

### Benchmarks and compensation create incentives but not proof

Classification shifting is attractive near a performance threshold because a small change in a preferred subtotal can alter the reported story without changing net income. McVay reports evidence around analyst forecast benchmarks.[1] Fan and colleagues find stronger evidence in fourth quarters, when annual targets become visible, and when accrual manipulation appears constrained.[2] Fan and Liu report that cost-of-goods-sold and selling, general, and administrative shifting varies with gross-margin, zero-core-earnings, prior-year, and analyst-forecast benchmarks.[4]

An analyst should calculate performance before every disputed classification. Determine whether restoring the cost causes the company to miss guidance, reverse margin expansion, fall below prior-year core earnings, miss a compensation target, or lose covenant headroom. The benchmark effect increases investigative priority, but it does not establish that the classification is wrong. A legitimate charge can happen to move a company across a target. Escalation requires evidence that the economic function, rule, disclosure, or internal approval does not support the chosen line.[4][8]

The control environment matters because line-item classification often begins outside the financial-reporting group. Business units code projects, financial planning approves internal adjustments, controllership aggregates the data, and the disclosure committee approves the published reconciliation. DXC demonstrates the danger of divided responsibility: employees assumed another group had performed the substantive review, while thousands of inadequately described line items rolled into the adjustment.[8] The author's assessment is that a classification control must name the owner of the definition, require project-level evidence, and force periodic reassessment rather than let a historical code renew itself.

### Asymmetry exposes a performance objective

A neutral normalization policy should treat economically similar gains and losses consistently. The SEC staff warns that excluding nonrecurring charges while retaining nonrecurring gains can make a non-GAAP measure misleading.[7] The same principle applies across time. If management excludes integration labor during an acquisition but includes favorable contract settlements, reserve releases, or disposal gains in adjusted earnings, the measure is designed directionally rather than analytically.

Build an asymmetry matrix with four cells: recurring charges excluded, recurring gains included, nonrecurring charges excluded, and nonrecurring gains excluded. Add a fifth column for definition changes. A measure becomes less credible as unfavorable items migrate out while favorable items remain, especially when the rule changes after the amount becomes large. This matrix is the author's proposed forensic control derived from the SEC's consistency and symmetry guidance.[7]

### Subsequent periods test the original label

Special items create future traces. Restructuring liabilities are paid, reversed, or re-estimated. Facilities close or remain open. Employees depart or are replaced. Integration projects finish or become permanent functions. Impaired assets disappear from the productive base. Discontinued operations stop contributing cash and expense, or continuing involvement persists. SAB No. 100's disclosure framework and ASU 2014-08's reconciliation requirements make some of these traces visible.[9][10]

A backtest should compare the original plan with later cash spending, liability use, headcount, capacity, margins, savings, and new charges. An unused restructuring accrual can indicate changed circumstances, but repeated releases that support earnings require explanation. A program described as complete while similar costs reappear under a new name weakens the one-time claim. A major disposal whose costs continue inside the surviving business may show that allocations were incomplete or that transition services create continuing economics. The author's synthesis is that the original classification becomes more credible when the forecasted operational change occurs and less credible when only the label changes.[5][8][9][10]

### Legitimate unusual items require the same discipline

A valid unusual item should have an identifiable event, a defined perimeter, a supportable amount, a clear relationship between the event and the cost, and a plausible end date. Its disclosure should distinguish cash from noncash effects, show the income-statement location, reconcile opening and closing liabilities when relevant, and explain continuing involvement or future savings without netting unlike effects.[9][10]

The decisive question is not whether the item is large or rare. It is whether the continuing business would have incurred the cost absent the identified event. If yes, exclusion requires a stronger economic rationale. If no, the analyst should still test recurrence at the strategy level: repeated acquisitions, annual restructurings, or continuous portfolio turnover can make event-specific costs part of the business model. The author's assessment is that legitimate classification is established by causation and evidence, not by management's adjective.

## Practical Forensic Framework

### 1. Fix the perimeter and preserve every reported view

Collect at least several annual and quarterly periods of the GAAP statements, footnotes, management discussion, earnings releases, investor presentations, segment tables, acquisition disclosures, discontinued-operation notes, restructuring roll-forwards, and GAAP-to-non-GAAP reconciliations. Preserve the exact definition of every adjusted metric for each period. Do not overwrite old definitions when management changes a label or combines categories.[7][8][9][10]

Create a line-item map from revenue to net income. For each period, record cost of goods sold, each operating-expense class, operating income, separately presented charges, nonoperating items, discontinued operations, taxes, and net income. Then reproduce every management subtotal. If the arithmetic cannot be reproduced, stop and resolve the missing amount before interpreting recurrence or intent.

### 2. Build an adjustment dictionary at the project level

For every special or excluded item, record the public label, internal or footnote description, transaction or plan, responsible function, start date, expected end date, cash status, GAAP line, non-GAAP treatment, segment allocation, tax effect, and prior-period analogues. A broad category such as "transformation" is not a unit of analysis. Split it into labor, consulting, systems, facilities, severance, impairment, legal, marketing, and other components where disclosure permits.[8][10]

Apply a causation test: would this resource have been consumed without the named event? Apply a qualification test: does the destination meet the governing reporting rule? Apply a recurrence test at the exact-label, economic-family, and resource levels. Apply a symmetry test to gains and losses. An item that fails one test is a lead, not yet a conclusion.[7][8][9][10]

### 3. Reconstruct core margins before and after disputed shifts

Restore suspected cost to the functional line from which it appears to have moved. Internal labor returns to the function employing the labor; inventory write-downs remain in cost of goods sold when the applicable presentation requires that treatment; continuing-business technology or occupancy cost returns to the operating line that consumes it.[8][10] Show reported gross margin, operating margin, management-adjusted margin, and forensic normalized margin side by side.

Do not place every special charge into selling, general, and administrative expense by default. Fan and Liu show why source-line identification matters: cost-of-goods-sold and selling, general, and administrative shifting can target different benchmarks.[4] Use payroll function, vendor scope, asset location, project ownership, segment usage, and prior classification to determine the most supportable destination. If the source line is uncertain, present a range and state which subtotals change under each allocation.

### 4. Build a multi-period recurrence ledger

Sum exclusions by label, economic family, and resource over three to five years or a full business cycle. Calculate each category as a percentage of revenue, reported operating expense, operating income, acquisition spending, and management-adjusted earnings. Record whether the company would have missed an announced target without the exclusion. A cost that is individually small can still be decision-relevant when it closes a benchmark gap.[1][2][4]

Track programs through renaming. "Restructuring," "optimization," "transformation," and "strategic actions" may be separate plans or successive names for the same operating adaptation. The ledger should preserve both management's categories and the analyst's economic groupings. The latter must be explicitly labeled as synthesis.

### 5. Reconcile notes, cash flow, and balance-sheet traces

Trace cash spending to operating, investing, and financing sections and reconcile noncash charges separately. Build liability roll-forwards for restructuring, severance, contract exits, and other accrued programs: opening balance, new charges, cash use, noncash use, reversals, acquisition effects, reclassifications, and ending balance.[10] Compare asset impairments with asset disposals, depreciation, capacity, and later operating performance.

The author's synthesis is that cash does not validate classification by itself. A recurring operating cost can be cash or noncash; a genuine unusual event can consume cash over several years. The purpose of cash reconciliation is to identify whether management's narrative matches settlement and whether adjusted earnings exclude costs that the continuing business repeatedly pays.

### 6. Test acquisition, segment, and discontinued-operation boundaries

For acquisition exclusions, tie each cost to a named transaction, contract, workstream, and expected integration period. Separate transaction execution from continuing operations and from projects that predated or would have occurred without the deal. For serial acquirers, compare cumulative excluded acquisition costs with acquired revenue, acquisition cash spending, and post-deal margins.[8]

For segment allocations, determine whether the excluded amount sits in a corporate column, is allocated away from a promoted segment, or is omitted from the segment profit measure. For discontinued operations, test the strategic-shift criteria and reconcile major income and expense classes to the after-tax result.[9] Compare transition-service agreements, stranded overhead, continuing guarantees, and shared systems with the allocation between disposed and continuing operations.

### 7. Backtest promised savings and subsequent reversals

Record management's stated savings, timing, headcount reduction, facility closures, and completion date. In later periods, compare actual cash use, expense run rate, staffing, capacity, and new special charges with the original plan. A charge can be legitimate even if savings disappoint, but an unsupported liability, unrelated cost, or recurring replacement program changes the classification assessment.[8][10][11]

Preserve the original information set to avoid hindsight bias. Later underperformance does not prove the original estimate was dishonest. Stronger evidence includes contemporaneous internal or contractual descriptions that contradict the public label, costs known to be necessary without the stated event, unsupported approvals, or repeated exceptions that consistently improve the same subtotal.[8]

### 8. Normalize valuation without inventing precision

Begin with reported GAAP earnings. Reverse only classifications supported by evidence, then separately normalize legitimate transitory items. For a recurring exclusion, restore the expected annual cost to operating expense and adjust taxes. For a truly event-specific item, exclude only the portion not necessary to maintain the business or execute its recurring strategy. Keep cash, noncash, and capital-allocation consequences separate.[5][7]

Use at least three cases when evidence is incomplete: management's adjusted view, a base case that restores clearly recurring amounts, and a conservative case that restores disputed amounts. Apply valuation multiples to a denominator defined consistently across periods and peers. A multiple on adjusted EBIT is not comparable when one company excludes recurring transformation labor and another does not. In a discounted-cash-flow model, the same normalized operating costs must appear in margins, reinvestment, and cash flow; they cannot be omitted from earnings and ignored in cash requirements.

## Evidence

### McVay established the modern classification-shifting test

McVay examined income-statement classification as an earnings-management tool. Her study reports evidence consistent with managers moving expenses from cost of goods sold and selling, general, and administrative expense into special items. The movement leaves bottom-line earnings unchanged but overstates core earnings. The study also reports that the behavior appears associated with meeting analyst forecast benchmarks because special items tend to be excluded from pro forma and analyst earnings definitions.[1]

The design estimates expected core earnings and tests whether unexpected core earnings increase with income-decreasing special items. The interpretation is intuitive: if a charge contains ordinary expense that would otherwise reduce core earnings, reported core earnings will be unusually high when the charge is large. The limitation is equally important. Performance and accruals can mechanically connect special items with core profitability, so the statistical relation is evidence of a population pattern rather than identification of a particular company's shifted invoice or payroll entry.[1][2][6]

### Quarterly evidence identifies timing and substitution incentives

Fan, Barua, Cready, and Thomas modify the expected-core-earnings model so it is not dependent on special-item accruals. They report that classification shifting is more likely in the fourth quarter than in interim quarters, more evident when managers appear constrained in their ability to manipulate accruals, and associated with a range of earnings benchmarks. They conclude that the evidence broadly supports the classification-shifting interpretation while clarifying the conditions under which it is more likely.[2]

The fourth-quarter result supports a targeted forensic procedure: compare annual results with the first three quarters, calculate the implied fourth quarter, and inspect year-end restructuring, impairment, acquisition, litigation, and other special charges. It does not establish that every fourth-quarter charge is opportunistic. Annual testing, audit completion, acquisition timing, and real year-end decisions can also concentrate legitimate charges in that quarter.[2]

### Discontinued operations and source expense lines broaden the mechanism

Barua, Lin, and Sbaraglia apply a method similar to McVay's to discontinued operations. They find evidence consistent with companies shifting operating expenses into income-decreasing discontinued operations to increase core earnings and meet or beat analyst forecasts. They also report that discontinued-operation reporting became more frequent after SFAS 144 while the magnitude of estimated shifting declined.[3] The study shows that classification shifting is not limited to a line explicitly called a special item; any category treated as outside continuing performance can become a destination.

Fan and Liu separate cost of goods sold from selling, general, and administrative expense. They find that cost-of-goods-sold shifting, but not selling, general, and administrative shifting, is more prominent when firms just beat the prior-year-quarter gross-margin benchmark. Both source categories are more prevalent around small core earnings, small core-earnings increases, and fourth-quarter analyst forecast benchmarks.[4] This evidence supports function-specific reconstruction rather than a single adjustment to total operating expense.

### Opportunistic special items predict weaker future outcomes

Cain, Kolev, and McVay document that special-item frequency increased over time and propose a method that predicts a normal level of special items from economic drivers, treating the excess as an opportunistic component. They report that this opportunistic portion is associated with lower future earnings, cash flows, and returns, consistent with recurring expenses being inappropriately classified as nonrecurring.[5] The finding is directly relevant to valuation: removing the entire charge can overstate sustainable earnings when part of the amount belongs to the continuing cost base.

The author's methodological assessment is that the model remains a screen rather than a transaction audit. A statistically excessive special item can reflect an omitted economic driver, unusual industry shock, or measurement error. The forensic response is to inspect the components and backtest them, not to label the residual fraudulent. Conversely, the absence of a statistical flag does not validate the classification of a material item whose contract, function, or disclosure is contradictory.

### Later research refines measurement and links shifting to restatements

Abdalla and Clubb analyze 72,568 firm-year observations from 1989 through 2017 and develop a modified model intended to address mechanical association between income-decreasing special items, accruals, and unexpected core earnings. Their estimated shifted core expenses have forecasting properties statistically indistinguishable from earnings before special items and are associated with future accounting restatements linked to special items. Their adjusted special items, after removing estimated shifted expense, have much weaker forecasting ability and no significant association with those future restatements.[6]

This partition supports a bounded conclusion: a special charge can contain both a recurring core component and a genuinely transitory component. Treating the entire amount as either recurring or nonrecurring destroys information. The research also reinforces model risk. Results depend on expected-core-earnings specification, industry estimation, accrual controls, and the assumption that shifted costs leave measurable statistical traces. Transaction-level evidence remains necessary for a company-specific conclusion.[6]

### The DXC order shows the mechanism in operating detail

The SEC's settled DXC order provides primary evidence of classification abuse in non-GAAP reporting. The Commission found that DXC negligently misclassified tens of millions of dollars as transaction, separation, and integration costs and thereby overstated non-GAAP net income by at least $29 million in the second quarter of fiscal 2019, $30 million in the fourth quarter of fiscal 2019, and $24 million in the first quarter of fiscal 2020. Reported non-GAAP net income for those quarters was $573 million, $589 million, and $472 million, respectively.[8]

The underlying costs expose the forensic tests. DXC included internal labor and tax expense, more than $38 million of data-center relocation cost over six consecutive quarters, required audit fees, implementation cost for a new lease standard, potential-divestiture expenses, and part of a litigation settlement. The data-center move was required because a pre-merger landlord would not renew the lease, so the expense would have arisen regardless of the merger.[8] Contract scope, pre-event history, recurrence, and ordinary operating necessity contradicted the integration label.

The order also documents process evidence. Business units were not required to document how proposed costs related to a transaction, how long they would continue, or why they qualified. Financial planning and controllership held inconsistent assumptions about which group performed the substantive review. Reviewers received spreadsheets with tens of thousands of line items, incomplete descriptions, and insufficient time, while questions about unsupported classifications remained unresolved before filing.[8] This evidence supports project-level approval, clear ownership, written rationale, and periodic reassessment as controls against classification drift.

### Reporting guidance makes several tests reproducible

The SEC's non-GAAP interpretations make recurrence, consistency, symmetry, description, and presentation testable. Excluding a normal recurring cash operating expense may mislead; an occasional operating expense can still be recurring; changing the treatment of similar items across periods requires explanation and possibly recasting; and excluding charges while retaining similar gains can violate Regulation G.[7] Detailed disclosure does not necessarily cure a measure that is materially misleading.[7]

ASU 2014-08 makes the discontinued-operation perimeter and reconciliation testable. The disposal must represent a strategic shift with a major effect, and the company must disclose major income and expense classes and reconcile them to the after-tax result.[9] SAB No. 100 makes restructuring analysis similarly concrete by requiring cost-specific recognition, precise classification, disaggregated plan disclosure, and roll-forward information about liabilities and cash use.[10] These sources do not eliminate judgment, but they convert a vague concern about "one-time items" into a defined evidence request.

## Implications

### Investors should value the business that repeatedly exists

For investors, the central implication is that adjusted earnings must be rebuilt rather than accepted or rejected wholesale. A useful adjustment answers a real question: what did the continuing operation earn absent a genuinely transitory event? Classification abuse answers a different question: how profitable would the company look if ordinary burdens were assigned to categories users ignore? The distinction requires line-item causation, recurrence, and subsequent-event evidence.[5][7][8]

A valuation model should begin with the reported GAAP result and show every bridge. Restore recurring labor, facility, systems, integration, and restructuring costs to the operating function that consumes them. Remove related tax effects consistently. If a charge includes both legitimate closure cost and recurring continuing-business cost, split it rather than accepting the management total. If disclosure does not permit a precise split, use a range and increase the margin of safety instead of inventing a point estimate.

Multiples must match the normalized perimeter. An enterprise-value-to-adjusted-EBIT multiple is overstated when the denominator excludes recurring costs, even if the exclusion is reconciled. Peer comparison is unreliable when adjustment policies differ, so the analyst should create a common rule for restructuring, acquisition, stock compensation, litigation, impairment, and disposition items. Cain, Kolev, and McVay's evidence that opportunistic special items predict lower future earnings and cash flows explains why a seemingly cheap adjusted multiple can be a classification artifact.[5]

The author's valuation synthesis is that discounted-cash-flow analysis does not automatically solve the problem. If the forecast starts from inflated core margins, the error compounds through every forecast year and terminal value. The cash-flow model should restore recurring costs, reflect actual cash settlement, and treat acquisition or restructuring spending as maintenance when the strategy requires it. Noncash impairments can be excluded from current free cash flow while still informing capital-allocation quality and the amount of reinvestment previously destroyed.

The author's proposed inversion is to ask what cost must disappear for management's margin to be sustainable. If the answer is continuing employees, facilities, systems, regulatory work, or repeated deal execution, the burden has not disappeared; only its accounting or analytical location has changed. If the answer is a closed plant, settled claim, or disposed major business with no recurring replacement, exclusion is more defensible.

### Credit analysts should preserve debt capacity before adjusted narratives

The author's credit-analysis synthesis is that credit analysis should test earnings and cash before exclusions used in leverage or coverage measures. A borrower can comply with a management-defined adjusted EBITDA target while recurring restructuring or integration cash drains liquidity. The analyst should reconcile covenant definitions separately because a contractual addback may be legally permitted even when it overstates sustainable debt service capacity.

Build coverage under reported, permitted-covenant, and economically normalized cases. Track cash paid against restructuring and transaction liabilities, and compare recurring exclusions with free cash flow after interest. A cost that migrates among labels can preserve EBITDA while continuing to consume cash. The correct conclusion is not that every permitted addback is deceptive; it is that contractual permissibility and repayment capacity answer different questions.

### Boards and management need a classification control, not a vocabulary list

Management can make legitimate adjustments credible by defining them before the result is known. A non-GAAP policy should specify eligible and ineligible cost types, required evidence, approval authority, duration, treatment of internal labor, treatment of gains, tax effects, and rules for recasting changed definitions. Each adjustment should link to a project, contract, ledger account, business owner, and expected completion date. The policy should also require reassessment when a project repeats or extends beyond its original period.[7][8]

The disclosure committee should receive gross components, not only an aggregated adjustment. It should see the GAAP line, amount, cash status, prior-period analogue, reason for exclusion, and effect on each published metric. Questions raised by controllers or sub-certifiers should be resolved before release, with contrary evidence preserved. DXC's order shows why informal oral explanations and divided assumptions about review ownership are not adequate controls.[8]

Boards should connect restructuring approval with later performance. Review the original plan, charge composition, cash budget, expected savings, affected headcount and facilities, and completion criteria. In later meetings, compare actual use and savings with the plan and explain new programs. The purpose is not to prohibit restructuring. It is to prevent a recurring operating adaptation from becoming a permanent adjusted-earnings exemption.[10][11]

Compensation committees should examine whether bonuses depend on a subtotal that management can alter by classification. A metric that excludes management-approved special items gives the same people influence over both the target and the adjustments. Independent approval, pre-defined rules, symmetric treatment, and a reconciliation to normalized economics reduce that conflict. Evidence that classification shifting concentrates near benchmarks makes this governance link material even though benchmark proximity alone does not prove misconduct.[1][2][4]

### Auditors and regulators should follow function, evidence, and reversal

Auditors should test the source population, not only the arithmetic reconciliation. Select items by size, recurrence, round amount, manual coding, late entry, internal labor, corporate origin, unsupported description, and proximity to performance targets. Inspect contracts, invoices, time records, project plans, facility history, acquisition documents, segment allocations, and subsequent settlement. A code labeled "integration" is management data, not evidence that the cost resulted from a merger.[8]

The audit should connect GAAP and non-GAAP reporting. A cost can be correctly recorded in GAAP but misleadingly described or excluded in a supplemental measure. Review procedures therefore need both accounting expertise and disclosure-control ownership. They should also test symmetry, definition changes, and whether the comparable GAAP measure has appropriate prominence under the applicable rules.[7]

Regulators can screen longitudinal filing data for recurring exclusions, fourth-quarter concentration, benchmark-closing amounts, growing differences between GAAP and adjusted margins, repeated changes in adjustment names, large corporate or unallocated columns, and discontinued-operation allocations. These screens allocate attention; they do not prove a violation. The strongest enforcement evidence connects the label to underlying work and shows that the public description, internal process, or governing rule did not support the classification.[6][8]

### Analysts must distinguish correction from normalization

The author's synthesis is that a classification violating GAAP or making a non-GAAP disclosure materially misleading requires correction. A legitimate unusual item can still require normalization for valuation. A recurring but correctly reported acquisition cost may belong in sustainable earnings even when no reporting violation exists. Conversely, a valid impairment charge may be removed from current operating cash flow but retained as evidence about acquisition discipline. These conclusions should not be collapsed into one accusation.

Use graded outcomes. "Supported unusual item" means the event, perimeter, amount, line, and end date reconcile. "Normalization risk" means accounting is supportable but recurrence makes exclusion economically questionable. "Aggressive presentation" means judgments and labels repeatedly favor core performance within an arguable range. "Likely error" means the classification conflicts with the reporting rule or underlying function. "Evidence consistent with manipulation" requires converging facts such as unsupported coding, contradictory contracts, target-sized entries, concealed recurrence, or deliberate mismatch between policy and disclosure.[7][8][9][10]

The final safeguard is disconfirmation. Search for evidence that the item is genuinely unusual: a discrete external event, a closed and settled plan, a major strategic disposal, a cost population that ends, consistent treatment of gains and losses, and later operations that no longer consume the resource. A forensic method that restores every charge to core earnings is as unreliable as management's method that excludes every unfavorable charge. The objective is a reversible map of economic function, not a predetermined lower earnings number.

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
   Finance. "Non-GAAP Financial Measures: Compliance and Disclosure
   Interpretations." Issued June 7, 2021; last updated December 13,
   2022. https://www.sec.gov/corpfin/non-gaap-financial-measures [high]

8. U.S. Securities and Exchange Commission (2023). "In the Matter of
   DXC Technology Company." Securities Act Release No. 11166; Exchange
   Act Release No. 97140; Accounting and Auditing Enforcement Release
   No. 4391. https://www.sec.gov/files/litigation/admin/2023/33-11166.pdf [high]

9. Financial Accounting Standards Board (2014). "Accounting Standards
   Update 2014-08: Presentation of Financial Statements (Topic 205) and
   Property, Plant, and Equipment (Topic 360), Reporting Discontinued
   Operations and Disclosures of Disposals of Components of an Entity."
   https://storage.fasb.org/ASU%202014-08.pdf [high]

10. U.S. Securities and Exchange Commission (1999). "Staff Accounting
    Bulletin No. 100 -- Restructuring and Impairment Charges." Federal
    Register, 64 FR 67154-67163.
    https://www.govinfo.gov/content/pkg/FR-1999-12-01/html/99-31160.htm [high]

11. Levitt, A. (1998). "The Numbers Game." Remarks to the NYU Center
    for Law and Business, September 28, 1998.
    https://www.sec.gov/news/speech/speecharchive/1998/spch220.txt [high]

## See Also

- `library/accounting-financial-shenanigans/non-gaap-metrics-and-pro-forma-manipulation.md` -- the broader framework for testing adjusted measures, recurring exclusions, and reconciliation quality.
- `library/accounting-financial-shenanigans/forensic-accounting-methodology.md` -- the evidence hierarchy and cross-statement process for moving from an anomaly to a supported conclusion.
- `library/accounting-financial-shenanigans/acquisition-accounting-tricks.md` -- purchase accounting, integration costs, reserves, and other acquisition boundaries that can shift reported expense.
- `library/accounting-financial-shenanigans/cookie-jar-reserves-and-expense-manipulation.md` -- reserve builds, releases, big baths, and capitalization that shift expense across periods rather than only across lines.
- `library/accounting-financial-shenanigans/restatement-analysis.md` -- how later corrections reveal the period, account, classification, and control failure behind prior reporting.
- `library/accounting-financial-shenanigans/segment-reporting-shenanigans.md` -- cost allocation and corporate columns that can flatter a promoted business without changing consolidated earnings.
