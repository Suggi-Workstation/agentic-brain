---
name: related-party-transactions
id: 20260829T120143Z
tier: library-topic
domain: accounting-financial-shenanigans
author: Library Runner
tags: [related-party-transactions, self-dealing, tunneling, asc-850, ias-24, forensic-accounting]
links: [library/accounting-financial-shenanigans/off-balance-sheet-shenanigans.md, library/accounting-financial-shenanigans/revenue-recognition-shenanigans.md, library/accounting-financial-shenanigans/restatement-analysis.md, library/accounting-financial-shenanigans/beneish-m-score.md]
---

# Related-Party Transactions -- How Insiders Hide Self-Dealing in Plain Sight

Related-party transactions (RPTs) are deals between a company and the
people who control it -- its management, directors, controlling
shareholders, and their families and affiliated entities. Because one
party to the deal can influence both sides of the table, the arm's-
length assumption that anchors fair-value logic and market pricing
does not apply, and the accounting standards say so explicitly. RPTs
are therefore the most direct instrument of self-dealing in corporate
finance: insiders can shift profits to themselves, hide losses inside
affiliated vehicles, and extract value from shareholders without ever
stealing cash outright, which makes detecting the manipulation -- not
merely reading the disclosure -- the core forensic task.

## Background

The related-party disclosure regime exists because of a simple
economic fact: a transaction with an insider is not a market
transaction. When a company buys goods from an independent supplier,
the price is set by competition and by the threat that either side
will walk away. When it buys from an entity controlled by its chief
executive, the CEO sits on both sides of the negotiation, and the
price is whatever the CEO decides it should be. US GAAP codifies this
insight in ASC 850, Related Party Disclosures, whose underlying
principle -- traceable to Statement of Financial Accounting Standards
No. 57, issued by the FASB in 1982 -- is that related party
transactions cannot be presumed to be carried out on arm's-length
terms (GAAP Dynamics; SouthPeak SEC order citing SFAS 57). The
IFRS equivalent, IAS 24, was first issued by the International
Accounting Standards Committee in July 1984, adopted by the IASB in
April 2001, revised in December 2003, and amended in 2009 to address
state-controlled entities (IFRS Foundation). The standards differ in
detail -- IAS 24 requires key management personnel compensation
disclosure and commitments to related parties, and provides an
exemption for some government-related transactions, while ASC 850
does not -- but they share the same objective: force companies to
draw attention to the possibility that their reported financial
position and performance were shaped by non-market dealings (KPMG).

The securities-law layer adds teeth on top of the accounting layer.
SEC Regulation S-X Rule 4-08(k) requires related party transactions
that affect the financial statements to be identified with amounts
stated on the face of the balance sheet, income statement, or
statement of cash flows, and requires receivables due from related
parties to be presented separately (GAAP Dynamics). Regulation S-K
Item 404(a) requires disclosure of any transaction in which any
related person -- a director, executive officer, nominee, or greater-
than-5-percent shareholder, plus immediate family members -- has or
will have a direct or indirect material interest, with a quantitative
threshold of $120,000 for the standard disclosure test (Sigma
Journal; SEC order in Co-Diagnostics). Banks carry an additional
layer: Federal Reserve Regulation O governs loans to executive
officers, directors, and principal shareholders and entities they
control (SEC order in Eagle Bancorp).

The academic literature supplied the economic theory behind these
rules. Johnson, La Porta, Lopez-de-Silanes, and Shleifer coined the
term "tunneling" in a 2000 American Economic Review paper to
describe the transfer of assets and profits out of firms for the
benefit of those who control them, and argued that tunneling -- legal
and illegal, self-dealing and outright theft -- is the central
agency problem in corporate governance worldwide, and that its
prevalence explains why civil-law jurisdictions with weak investor
protection have smaller, more concentrated capital markets. The
enforcement history of the early 2000s proved the theory's practical
relevance. Enron's collapse in 2001 was built on special purpose
entities secretly controlled by CFO Andrew Fastow (SEC Litigation
Release 17762), Tyco's 2002 fraud was built on undisclosed insider
loans and related-party real estate deals (SEC Litigation Release
17722), and Sarbanes-Oxley responded in part with Section 402's
prohibition on personal loans to directors and officers (Grid Oasis).
The PCAOB's dedicated related-parties auditing standard -- now AS
2410 -- exists because the profession recognizes RPTs as one of the
highest-risk areas in any audit (PCAOB; LegalClarity). For the
forensic analyst, the lineage matters: every rule, standard, and
prosecution above exists because insiders kept finding ways to move
value through entities they controlled, and the disclosure regime is
the trailing indicator of a pattern that never stops evolving. The
enforcement cadence confirms the sequence: an aggressive transaction
appears in a proxy, a short seller or whistleblower maps the
counterparties, and the restatement follows -- a chain documented in
each of the cases in the Evidence section below.

## Core Concepts

### What Counts as a Related Party

ASC 850 defines related parties to include affiliates, equity-method
investees, trusts for the benefit of employees, principal owners and
management, and members of their immediate families -- any family
member who might control or influence, or be controlled or
influenced by, the insider because of the family relationship --
plus "other parties that can significantly influence the management
or operating policies of the transacting parties or that have an
ownership interest in one of the transacting parties and can
significantly influence the other to an extent that one or more of
the transacting parties might be prevented from fully pursuing its
own separate interests" (GAAP Dynamics; SEC order in Eagle Bancorp).
Two properties make this definition an enforcement minefield rather
than a settled rule. First, it is judgment-based: determining who
counts as a related party "requires a significant amount of judgment
on the part of management," which means the insider doing the
transaction is also the party drawing the boundary around what must
be disclosed (GAAP Dynamics). Second, it is broader than it looks:
Eagle Bancorp's failure arose precisely because the bank applied the
narrower Regulation O definition -- loans to officers, directors, and
entities they control -- instead of the ASC 850 definition, and so
excluded loans to family trusts where the chairman was a practical
decision-maker even though the trustee was formally an employee of
the chairman's real estate company (SEC order in Eagle Bancorp). IAS
24 takes a comparable approach, defining a related party as a person
or entity that can exercise control, joint control, or significant
influence over the reporting entity, key management personnel
included, but differs from US GAAP in ways that matter for
cross-border analysis -- for instance, entities are not related under
IAS 24 merely because they share a director or are both associates of
the same third party (KPMG).

### Why Arm's-Length Terms Cannot Be Presumed

ASC 850-10-50-1 states that transactions between related parties
"cannot be presumed to be carried out on an arm's-length basis," and
that representations of arm's-length terms may be disclosed only if
they can be substantiated (CapinCrouse; GAAP Dynamics). The economic
logic is the same one the tunneling literature formalized: with no
adversarial bargaining, price is a choice variable of the insider,
not an emergent property of competition. This is why the phrase
"on terms substantially similar to arm's-length" is hedge language:
it asserts market pricing without evidencing it (Basis Report). The
testable consequence for forensic work is that every RPT must be
treated as mispriced until evidence -- competitive bids, independent
appraisal, third-party benchmarking -- shows otherwise, and the
absence of such evidence is itself a finding, not a neutral gap
(Pomegra).

### Tunneling -- the Economics of Self-Dealing

Johnson, La Porta, Lopez-de-Silanes, and Shleifer define tunneling
as the transfer of assets and profits out of firms for the benefit of
those who control them, and identify two broad forms: self-dealing
transactions (asset sales, transfer pricing, loans, and guarantees
at insider-favorable terms) and financial transactions that dilute
or freeze out minority shareholders. Their case evidence from civil-
law countries showed courts declining to police intra-group
transactions, and they concluded that the legal treatment of
minority shareholders explains cross-country differences in market
depth (Johnson et al.). The mirror image -- "propping" -- was
documented by Cheung, Rau, and Stouraitis using connected-
transaction data from Hong Kong-listed companies in 1998-2000: the
same insiders who tunnel resources out of healthy firms sometimes
inject resources into distressed ones, because both directions serve
the insider's objective of maximizing the value of control
(Cheung et al.). For the analyst, the practical upshot is that
related-party flows must be read as a system: an insider-friendly
supply contract in one year, a subsidized loan in another, and a
rescue capital injection in a third are not three unrelated events
but one recurring program of value transfer with the sign changing
as circumstances dictate.

### The Disclosure Regime -- What Must Be Shown and Where

ASC 850 requires disclosure of material RPTs other than ordinary
compensation arrangements: the nature of the relationships, a
description of the transactions and any other information necessary
to understand their effects, dollar amounts and changes in the
method of establishing terms, amounts due to or from related parties
with terms and manner of settlement, and current and deferred tax
expense allocations for entities in consolidated tax groups (GAAP
Dynamics). Receivables from officers, employees, or affiliated
entities must be shown separately on the balance sheet, not buried
under general headings (CapinCrouse). SEC registrants additionally
file Item 404 disclosures in the proxy statement and Form 10-K --
the disclosure must state the nature of the relationship, the amount,
and the terms -- and Regulation S-X requires amounts stated on the
face of the financial statements (GAAP Dynamics; SEC order in
Co-Diagnostics). IAS 24 goes further in three respects: it mandates
key management personnel compensation disclosure in total and by
category, mandates disclosure of commitments to related parties, and
contains a government-related-entity exemption with no US GAAP
analogue (KPMG; GAAP Dynamics). For the forensic reader, the
practical map is: the 10-K footnotes and Item 13 for amounts and
terms, the proxy for the process, and the balance sheet for due-
from and due-to related-party balances that show whether value is
piling up inside the affiliated entities rather than returning to
shareholders (Pomegra).

### The Structural Anatomy of Self-Dealing Vehicles

The vehicles insiders use to transact with themselves have a
recurring anatomy. Shell and nominee companies: Enron's RADR scheme
used individuals selected by Fastow as nominal investors in
windmill-farm entities, funded by secret loans from Fastow, to
create the appearance of third-party ownership where none existed
(SEC Litigation Release 17762). Management-fee and consulting
contracts: Manitex's CFO approved payments on fictitious "consulting"
invoices from a related shell company (RCSC) that existed solely to
recycle the company's own money into covering a related customer's
financing obligations (SEC order 33-10863). Family trusts and
family-owned businesses: Eagle Bancorp lent hundreds of millions to
trusts whose practical decision-maker was the chairman, and Satyam's
founder attempted to have his own company acquire his sons' real
estate firms (SEC order in Eagle Bancorp; Reuters). Loans and
forgiveness: Tyco's CEO and CFO granted themselves undisclosed low-
interest and interest-free loans, then arranged forgiveness, then
falsified books and records to bury the compensation (SEC Litigation
Release 17722). Leases and property deals: Kozlowski purchased a
Tyco-owned apartment for his wife with company-loaned funds, and a
Tyco subsidiary purchased the CFO's New Hampshire property for more
than fair value (SEC Litigation Release 17722). Cross-guarantees
and circular funding: Manitex guaranteed the financing of its
related customer's purchases and then paid the financing obligations
itself, so that cash left the company and returned as reported
revenue from a sale that was economically a loan (SEC order
33-10863). The common thread is circularity -- money that leaves the
company through one instrument and returns through another -- and
the circular shape is what the forensic analyst should be looking
for, because honest transactions are rarely circular (Sigma Journal).

### The Red-Flag Anatomy of a Suspicious Deal

Enforcement patterns across SEC actions and short-seller research
converge on a compact set of indicators that separate routine RPTs
from self-dealing (Sigma Journal; StockAlpha; Basis Report). First,
pricing that fails the smell test: an asset sold to an insider's
vehicle above appraisal, a subsidiary sold to a founder's family
office at a discount, a lease from an executive's spouse on premium
terms. Second, repetition: one odd deal is noise; a series of
recurring deals with the same counterparty is culture. Third,
process failure: no independent committee, no recusal, no external
pricing or fairness analysis, or retroactive approval after the deal
is already done. Fourth, vague description: round-dollar amounts,
"consulting services" and "management fees" without deliverables,
and "substantially similar to arm's-length" language without
supporting terms. Fifth, disclosure-clock problems: material RPTs
announced in 8-Ks after year-end that never appeared in the prior
10-K or proxy. Sixth, circular cash: guarantees, side letters, and
funding flows that return to the company as revenue or as payments
to the insider. Seventh, opacity of structure: multiple layers,
special purpose vehicles, and counterparties that are hard to map.
None of these alone proves fraud -- RPTs are a normal part of
corporate life, and many are benign -- but each one is a research
trigger, and several together shift the burden of proof onto the
company to show why the pattern is innocent (Basis Report;
StockAlpha).

## Evidence

The enforcement record supplies the strongest evidence that RPTs are
a primary fraud vector rather than a compliance footnote.

Enron is the canonical case. SEC Litigation Release 17762 details
how CFO Andrew Fastow built the company's off-balance-sheet
architecture on undisclosed self-dealing: he selected nominee
investors for the RADR windmill entities, funded their stakes with
secret personal loans, and collected kickbacks through a "gifting"
program of annual $10,000 non-taxable transfers to his family
members; he secretly controlled the Chewco entity through Michael
Kopper while nominally at arm's length from it; in the Southampton
transaction he told Enron that NatWest demanded $20 million for its
LJM1 partnership interest, paid $1 million, and pocketed the
difference, with $4.5 million routed to a foundation in his family's
name; and in the Nigerian barges sham sale he gave a financial
institution an oral buyback promise, then fulfilled it through his
controlled partnership LJM2. The company collapsed into bankruptcy
in December 2001, and Fastow was criminally charged. The detection
path is instructive: the self-dealing was invisible in Enron's
consolidated statements until investigators reconstructed the
related-party web from documents and testimony -- which is why
cross-referencing the off-balance-sheet topic is essential for any
Enron study.

Tyco shows the same mechanism without any special purpose entities.
SEC Litigation Releases 17722 and 21129 recount how CEO Dennis
Kozlowski and CFO Mark Swartz granted themselves hundreds of
millions of dollars in undisclosed low-interest and interest-free
loans, arranged forgiveness of tens of millions of those loans,
engaged in undisclosed related-party real estate transactions
including a subsidiary's purchase of Swartz's New Hampshire property
above fair value, and falsified books and records to bury the
compensation against unrelated gains -- all while selling company
stock with the self-dealing undisclosed. The outcome: criminal
sentences of 8-1/3 to 25 years, approximately $134 million in
restitution, fines of $70 million and $35 million, and permanent
officer-and-director bars (SEC Litigation Release 21129).

Satyam demonstrates the failed related-party exit strategy. In
December 2008, founder B. Ramalinga Raju attempted to have Satyam
Computer Services acquire Maytas Infrastructure and Maytas
Properties -- firms owned by his sons, with "Maytas" as "Satyam"
reversed -- for $1.6 billion, a deal that would have swapped real
family assets for Satyam's fake ones; the board's approval collapsed
within about 12 hours under shareholder revolt, and Reuters reported
the deal was abandoned on that basis (Reuters). On January 7, 2009,
Raju resigned and confessed to inflating Satyam's cash and bank
balances by more than $1 billion, in a letter describing a
manipulation that had begun as a small gap between actual and
reported profit and grown until it was unmanageable (Wikipedia,
Mahindra Satyam). The attempted RPT was the moment the fraud became
public: a brazenly conflicted transaction is itself a confession
about what the insider believes the true numbers are.

The smaller-scale enforcement orders show the pattern in routine
form. Manitex (SEC order 33-10863): the company booked roughly $12
million of "bill and hold" crane sales to SVW, a related entity
with no operations, revenue, or ability to pay, while guaranteeing
SVW's financing and secretly paying those obligations through
fictitious consulting invoices from a shell subsidiary; the fraud
overstated 2016 net revenues by 6.91 percent and gross profit by
8.19 percent and forced an April 2018 restatement, with the CFO
sanctioned for approving invoices he knew were fake. Eagle Bancorp
(SEC order 33-11092): the bank omitted hundreds of millions of
dollars of loans to family trusts affiliated with its chairman from
its related-party loan disclosures by applying the wrong definition
of related party, and when it finally disclosed in March 2019,
related-party loan balances jumped from $61 million to $238 million
as of year-end 2017 -- an understatement of nearly four times. The
bank's own auditor had flagged the failure as a significant
deficiency in internal control over financial reporting. Co-
Diagnostics (SEC order 34-97835): a company with no related-party
policies or procedures failed to disclose Item 404 transactions
including over $1.1 million in annual compensation paid to the
CEO's son and over $1.1 million to the CFO's son, plus consulting
fees to a firm co-owned by the CFO's son; the CFO was sanctioned for
signing certifications he had not meaningfully supported.

The academic evidence generalizes the cases. Johnson, La Porta,
Lopez-de-Silanes, and Shleifer (2000), building on legal cases from
France, Italy, Belgium, and elsewhere, showed that controlling
shareholders expropriate minority shareholders through legal and
illegal self-dealing, and that civil-law systems with weak
investor protection tolerate substantially more of it -- with the
predictable result that outside equity financing remains scarce and
markets stay concentrated. Cheung, Rau, and Stouraitis (2006)
provided direct evidence using Hong Kong connected-transaction
disclosures from 1998-2000: transactions between listed companies
and their controlling shareholders or directors were systematically
associated with minority-shareholder expropriation, with certain
transaction types -- asset acquisitions and disposals between listed
firms and their controllers -- predictably transferring value away
from outside shareholders, while a minority of transactions
flowed the other way as propping. The consistency between the case
record and the academic findings is the point: self-dealing is not
the pathology of a few spectacular frauds but a structural hazard
whose intensity varies with governance quality and the strength of
investor protection. The audit profession's standards
independently confirm the risk level: PCAOB AS 2410 requires the
auditor to obtain an understanding of the company's process for
identifying, authorizing, approving, accounting for, and disclosing
related-party relationships and transactions precisely because, as
LegalClarity summarizes, RPTs "often lack the objective pricing and
terms found in arm's-length dealings" and sit among the highest
fraud-risk areas of a financial statement audit.

## Implications

### For Analysts and Investors

Related-party disclosure is the cheapest high-yield screen in
forensic accounting, because it is readable in minutes and it
measures the one variable no ratio captures: whether insiders
behave like owners or like counterparties (Grid Oasis). The working
method: read every disclosed RPT in the proxy and 10-K, ask whether
each transaction could plausibly have been executed with an
unrelated third party at similar terms, count the transactions and
their aggregate value, check whether the same counterparties recur
year after year, and evaluate the quality of the review process --
independent committee, advance approval, external pricing -- rather
than the presence of a policy statement (Grid Oasis; StockAlpha).
Treat the absence of specificity as information: "substantially
similar to arm's-length" without terms, competitive bids, or
appraisals is evidence that the company wants the legal benefit of
disclosure without the burden of showing its work (Basis Report).
Compare the balance-sheet related-party balances (due from and due
to affiliates) over time; balances that grow while the company's
cash stays flat suggest value is accumulating outside the reach of
outside shareholders (Pomegra). The Eagle lesson applies directly:
verify which definition of related party the company actually used,
because process errors of definition produce systematic
under-disclosure that looks like competence and acts like fraud
(SEC order in Eagle Bancorp).

### For Boards and Governance

The enforcement record shows that most RPT fraud could have been
prevented by administrative competence: maintaining a related-party
register, routing transactions through a real audit-committee review
with recusals, obtaining external pricing, and filing on time
(Sigma Journal). The difference between advance approval and
retroactive ratification is substantive, not cosmetic -- a
transaction already executed cannot have its terms improved by a
committee that sees it afterward (Grid Oasis). Boards should treat
a growing related-party section of the proxy as a governance
finding in its own right: the volume, recurrence, and complexity of
RPTs is a revealed measure of the boundary between insiders'
personal economics and the company's resources, and firms like
Berkshire Hathaway demonstrate that scale does not require
entanglement (Grid Oasis). For value investors specifically -- and
this is the author's synthesis rather than a sourced assertion --
management integrity is the first filter before any valuation work,
because every number in the model is a management claim, and an
insider who transacts with the company at non-market terms has
demonstrated that their interest and the shareholders' interest are
not the same variable. The audit committee's related-party review
is one of the few places where that variable is directly observable
from public filings.

### For Forensic Detection in This Domain

RPTs rarely operate alone; they are the connective tissue between
the other shenanigan categories in this domain. Manitex was a
related-party case implemented as a bill-and-hold revenue
recognition fraud; Enron was a related-party case implemented as an
off-balance-sheet consolidation fraud; Tyco was a related-party
case implemented as undisclosed compensation. The forensic
sequence that follows from this is: when an RPT pattern appears,
test it against the domain's other instruments -- revenue
recognition quality, off-balance-sheet structures, restatement
history, and quantitative screens such as the Beneish M-Score --
because the RPT is frequently the motive that explains the
manipulation found elsewhere (cross-references below). Circular
funding is the highest-priority pattern to trace: money that leaves
the company and returns as revenue, investment, or loan repayment
is the signature of the self-dealing structures documented in
Manitex, Enron's RADR, and the Nigerian barges sham sale (SEC order
33-10863; SEC Litigation Release 17762; Sigma Journal). The same
discipline applies to counterparty mapping: for every material RPT,
identify the ultimate beneficiary, the funding source, and the
history of the relationship, because the cases show the public
filings usually contain enough detail to reconstruct the web before
the regulator finishes -- Eagle Bancorp's short-seller report on its
related-party loans was initially dismissed on the chairman's false
assertions, and the bank's own auditor then determined that the
failure to disclose the loans was a significant deficiency in
internal control over financial reporting (SEC order in Eagle
Bancorp). The other detection inputs are auditor inquiry and
documentary reconstruction: Manitex's restatement followed
consultations with its external auditor, and the related-party
origin of the fraud was visible in the financing guarantees and the
fictitious invoices once anyone examined them (SEC order 33-10863).
An auditor change, a surprise restatement, or an enforcement inquiry
that follows an RPT disclosure is therefore a confirmation signal,
not a coincidence.

### For Regulators and Standard-Setters

Three gaps deserve attention. First, definitional drift: Eagle
Bancorp shows that companies fail disclosure obligations by applying
the wrong standard (Regulation O instead of ASC 850), which
suggests enforcement should treat the process of related-party
identification -- not just the disclosure output -- as the
compliance object (SEC order in Eagle Bancorp). Second, cross-
regime inconsistency: IAS 24 and ASC 850 diverge on key management
compensation, commitments, and government-related exemptions, so a
multinational's related-party exposure is not comparable across
reporting regimes, and dual reporters must reconcile both (KPMG).
Third, threshold gaming: the Item 404 quantitative threshold ($120k
or, for smaller reporting companies, the lesser of $120k and one
percent of average total assets) is a floor that invites
structuring -- the Co-Diagnostics order shows the family-employment
channel running to seven figures while the company's own
disclosure controls simply did not exist (SEC order 34-97835).
Sarbanes-Oxley Section 402's ban on personal loans to executives
closed the most blatant Tyco-era channel, but loans remain legal to
related entities that are not the executive personally, and the
forensic frontier is exactly there: the family trust, the
consulting firm, the special purpose vehicle (Grid Oasis; SEC order
33-11092).

## Sources

1. SEC Administrative Proceeding File No. 3-19856, In the Matter of
   Michael Schneider, CPA (Manitex International, Inc.), Release No.
   33-10863 (2020). Related-party bill-and-hold revenue fraud and
   fictitious consulting invoices.
   https://www.sec.gov/files/litigation/admin/2020/33-10863.pdf [high]

2. SEC Administrative Proceeding File No. 3-21425, In the Matter of
   Reed L. Benson (Co-Diagnostics, Inc.), Release No. 34-97835 (2023).
   Item 404 related-person disclosure failures.
   https://www.sec.gov/files/litigation/admin/2023/34-97835.pdf [high]

3. SEC Administrative Proceeding File No. 3-21029, In the Matter of
   Eagle Bancorp, Inc., Release No. 33-11092 (2022). Undisclosed
   related-party loans under ASC 850 and Regulation O.
   https://www.sec.gov/files/litigation/admin/2022/33-11092.pdf [high]

4. SEC Administrative Proceeding File No. 3-14380, In the Matter of
   SouthPeak Interactive Corporation and Patrice K. Strachan, Release
   No. 34-64320 (2011). Undisclosed related-party inventory payment;
   SFAS 57 and Regulation S-X requirements.
   https://www.sec.gov/files/litigation/admin/2011/34-64320.pdf [high]

5. SEC Litigation Release No. 17762, SEC v. Andrew S. Fastow (Oct. 2,
   2002). RADR, Chewco, Southampton, Nigerian barges, and LJM
   self-dealing allegations.
   https://www.sec.gov/enforcement-litigation/litigation-releases/lr-17762 [high]

6. SEC Litigation Release Nos. 17722 (Sept. 12, 2002) and 21129 (July
   14, 2009), SEC v. L. Dennis Kozlowski, Mark H. Swartz, and Mark A.
   Belnick. Undisclosed insider loans, loan forgiveness, and
   related-party real estate at Tyco.
   https://www.sec.gov/enforcement-litigation/litigation-releases/lr-21129 [high]

7. Johnson, S., La Porta, R., Lopez-de-Silanes, F., & Shleifer, A.
   (2000). "Tunneling." American Economic Review, 90(2), 22-27.
   https://www.nber.org/digest/sep00/tunneling-directs-profits-controlling-shareholders [high]

8. Cheung, Y.-L., Rau, P. R., & Stouraitis, A. (2006). "Tunneling,
   propping, and expropriation: evidence from connected party
   transactions in Hong Kong." Journal of Financial Economics, 82(2),
   343-386.
   https://www.sciencedirect.com/science/article/abs/pii/S0304405X06001462 [high]

9. PCAOB AS 2410, "Related Parties" (effective for fiscal years
   beginning on or after December 15, 2024).
   https://pcaobus.org/oversight/standards/auditing-standards/details/as-2410--related-parties-(effective-for-fiscal-years-beginning-on-or-after-12-15-2024) [high]

10. IFRS Foundation. IAS 24, Related Party Disclosures -- standard
    history and objective.
    https://www.ifrs.org/issued-standards/list-of-standards/ias-24-related-party-disclosures/ [high]

11. KPMG IFRS Institute. "Related party disclosures: IFRS Standards
    vs US GAAP." Top-10 identification and disclosure differences.
    https://kpmg.com/us/en/articles/2023/related-party-disclosures.html [medium]

12. GAAP Dynamics (Mike Walworth, CPA). "Swear to Properly Disclose
    Related Party Transactions (ASC 850/IAS 24)." May 2, 2017.
    https://www.gaapdynamics.com/insights/blog/2017/05/02/swear-to-properly-disclose-related-party-transactions-asc-850-ias-24 [medium]

13. Reuters. "Maytas denies getting funds from fraud-hit Satyam."
    January 20, 2009.
    https://www.reuters.com/article/maytas-satyam-idINBOM41702820090120 [medium]

14. CapinCrouse LLP. "New Related Party Disclosure Requirements for
    Higher Education Institutions." ASC 850-10-50 disclosure
    requirements summary. 2024.
    https://capincrouse.com/wp-content/uploads/2024/07/CapinCrouse-New-Related-Party-Disclosure-Requirements-for-Higher-Education-Institutions.pdf [medium]

15. Sigma Journal (insiders-trades.com). "Seven Self-Dealing
    Patterns Regulators Monitor Closely." Enforcement-pattern review
    of self-dealing cases.
    https://insiders-trades.com/blog/self-dealing-red-flags-7-patterns-regulators-watch/ [low]

16. Grid Oasis. "Red Flags in Related-Party Transactions." Corporate
    governance screen discussion.
    https://gridoasis.com/guides/corporate-governance/related-party-transactions/ [low]

17. Basis Report. "10-K Red Flags Checklist." Related-party
    transactions at non-arm's-length terms and hedge language.
    https://www.basisreport.com/resources/10k-red-flags-checklist [low]

18. StockAlpha. "Related-Party Transactions: A Beginner's Red-Flag
    Checklist." Filing-location and checklist guidance.
    https://stockalpha.ai/alpha-learning/related-party-transactions-a-beginners-red-flag-checklist [low]

19. Pomegra Learn Library. "Related-party transactions as a red
    flag." Financial statement red-flag discussion.
    https://pomegra.io/learn/library/track-b-stock-market-core/financial-statements/chapter-13-red-flags-in-statements/related-party-transactions-rf [low]

20. Wikipedia. "Mahindra Satyam." Satyam's January 2009 confession
    of over $1 billion in inflated cash assets.
    https://en.wikipedia.org/wiki/Mahindra_Satyam [low]

21. LegalClarity. "Audit Standard 18: Related Parties and
    Transactions" (AS 18, now codified as AS 2410).
    https://legalclarity.org/audit-standard-18-related-parties-and-transactions [low]

## See Also

- `library/accounting-financial-shenanigans/anchor-accounting-financial-shenanigans.md` -- domain anchor; lists related-party transactions among the In-scope shenanigan vectors.
- `library/accounting-financial-shenanigans/off-balance-sheet-shenanigans.md` -- Enron's SPE architecture; the Fastow related-party web overlaps directly with this topic's Enron evidence.
- `library/accounting-financial-shenanigans/revenue-recognition-shenanigans.md` -- bill-and-hold fraud; the Manitex case is a related-party implementation of this revenue pattern.
- `library/accounting-financial-shenanigans/restatement-analysis.md` -- forced corrections; Manitex, Eagle Bancorp, and Satyam all ended in restatements after their related-party activity surfaced.
- `library/accounting-financial-shenanigans/beneish-m-score.md` -- quantitative manipulation screen; a companion to the qualitative related-party checklist.
