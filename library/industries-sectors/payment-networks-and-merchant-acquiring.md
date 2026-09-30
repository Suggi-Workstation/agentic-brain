---
name: payment-networks-and-merchant-acquiring
id: 20260930T121350Z
tier: library-topic
domain: industries-sectors
author: Librarian
tags: [payment-networks, merchant-acquiring, interchange, card-routing, two-sided-markets, tokenization, regulation]
links: [library/industries-sectors/network-effects-platform-economics.md, library/industries-sectors/industry-profit-pools.md, library/industries-sectors/value-chain-analysis.md, library/case-studies/berkshire-american-express-investment.md, library/macro-micro/market-structures.md]
---

# Payment Network Economics -- Acceptance Scale Creates Value, but Routing and Regulation Decide Who Captures It

A card payment turns a brief checkout into coordinated authorization, clearing, settlement, fraud control, and dispute management across merchants, acquirers, networks, and issuers [3][14]. The industry's profits are not distributed in proportion to visible transaction volume: networks supply rules and connectivity, issuers usually receive interchange, and acquirers combine merchant access with processing and risk services while passing through much of the fee stack [6][7][13]. Acceptance scale is valuable, but routing choice, tokenization, vertical integration, regulation, and account-to-account alternatives determine whether that value becomes durable bargaining power or migrates to another link [4][9][10].

## Background

Payment cards developed as a way to replace bilateral trust between each buyer and seller with a reusable credential accepted under common rules. A merchant need not assess every customer's bank or creditworthiness directly; it submits a transaction through an acquiring relationship, the relevant network identifies and contacts the issuer, and the issuer approves or declines under its account and risk rules. The network then supports clearing, which calculates obligations, and settlement, which moves value among participating institutions. The process separates the commercial sale from the financial institutions and technical services that authenticate the payer, route messages, allocate risks, and deliver funds [3][14].

Two architectures organize most card systems. In a four-party model, the cardholder deals with an issuer, the merchant deals with an acquirer, and a network connects those institutions under shared technical and commercial rules. Visa and Mastercard are prominent examples. In a three-party or closed-loop model, the network provider also performs the issuing and acquiring roles, so the simplified model contains the cardholder, merchant, and integrated provider. American Express and Discover have historically illustrated this architecture, although real systems can include partner issuers, third-party acquirers, processors, and other delegated functions. The labels therefore describe the governing economic structure, not a promise that exactly three or four legal entities touch every transaction [14].

The four-party architecture created specialization. Issuers could compete for cardholders through credit, deposits, rewards, service, and risk management. Acquirers could compete for merchants through onboarding, terminals, gateways, settlement, reporting, fraud tools, and price. Networks could invest in interoperability, rules, brand acceptance, authorization links, clearing, and settlement without carrying every consumer loan or owning every merchant relationship. The Federal Reserve Bank of Philadelphia described four recurring acquiring functions: signing and underwriting merchants, enabling authorization, facilitating clearing and settlement, and providing associated information services. It also observed that standard processing functions made price and scale important competitive variables for acquirers [3].

This division of labor introduced a transfer payment between the two financial sides. In a typical four-party transaction, the acquirer pays interchange to the issuer. Both issuers and acquirers can also pay network or scheme and processing fees. The merchant pays its provider a merchant service charge, or MSC, that combines interchange, scheme and processing fees, and the acquirer's own costs and margin. The network generally sets default interchange schedules, but interchange is not network revenue: it normally passes from acquirer to issuer. Visa and Mastercard both state this distinction in their filings, while their own network revenue arises principally from volume, switching, processing, cross-border, and value-added services [11][12].

Payment cards are also a canonical two-sided market. A card is useful to a cardholder only where merchants accept it, while acceptance is useful to a merchant only if enough customers want to pay with it. Rochet and Tirole formalized the resulting problem: a platform must attract both sides, and economic outcomes depend on the allocation of prices between them, not only on the total price charged across both sides. A platform can therefore subsidize one side and recover more from the other when that structure expands participation or transaction volume. The framework explains why cardholder rewards or low direct cardholder fees can coexist with merchant-paid interchange and acceptance fees without proving that any observed fee level is socially optimal [1].

Merchant acquiring itself has broadened. Traditional acquiring banks remain the institutions directly connected to schemes and responsible for sponsored merchant activity, but processors, gateways, independent sales organizations, payment facilitators, and software platforms can perform parts of the commercial and technical relationship. A payment facilitator or sub-acquirer may aggregate smaller merchants under access obtained through an acquirer rather than connect directly to every network. Aurazo's BIS model separates this market into an upstream connection supplied by the acquirer and a downstream merchant service in which the acquirer and sub-acquirer can compete. The model shows why payment facilitators can extend acceptance into small or specialized markets while also creating an access-pricing problem when the upstream acquirer competes against its downstream customer [2].

Digitization changed the interface without necessarily changing the underlying rail. A consumer may tap a card, type credentials into a website, use a wallet, or authorize an application, while the transaction still reaches an acquirer, network, and issuer. EMV payment tokenization replaces the primary account number with a constrained token that can move from the purchase point through the acquirer and network to the issuer. The token can be limited to a merchant, device, or use case and managed over its lifecycle, reducing the usefulness of stolen credentials while preserving compatibility with existing acceptance infrastructure [10]. A wallet funded by a card can improve checkout while leaving the original card fee and routing structure underneath it [7][10].

Regulation entered because the same network effects that support wide acceptance can reduce merchants' practical ability to refuse a popular card or negotiate around a default fee. The United States regulates covered debit interchange and requires routing access to at least two unaffiliated networks, including for card-not-present transactions under the Federal Reserve's 2022 clarification. The European Union caps consumer-card interchange, separates scheme from processing activities, and restricts practices that impede card-brand, application, or acquiring choice. The United Kingdom has separately reviewed acquiring, scheme, and processing competition. These regimes differ, but each treats the technical route, commercial rules, and price structure as connected features of the industry's competitive architecture [4][7][8].

This topic analyzes the playing field rather than any named security. It focuses on how fees, risk, routing, scale, integration, and regulation distribute economic value among networks, issuers, acquirers, processors, facilitators, merchants, and alternative rails. Consumer-credit underwriting belongs to finance, detailed protocol engineering belongs to technology, and an investment judgment about a particular company belongs in company-specific research.

## Core Concepts

### A transaction is a sequence of promises, not one data message

Authorization, clearing, and settlement solve different problems. Authorization asks whether the issuer will approve a proposed transaction under the credential, account status, available funds or credit, fraud controls, and applicable rules. The merchant's terminal, application, or gateway sends transaction data to its processor or acquirer, which selects an available network and forwards the request to the issuer. The response returns through that chain. Approval is a commitment under network rules; it is not yet final movement of all funds [3][14].

Clearing assembles approved transactions, applies fees and adjustments, and calculates what participating institutions owe. Settlement moves the resulting obligations, commonly on a net basis, through designated settlement arrangements. The acquirer then credits the merchant according to its contract, less the MSC or other agreed deductions. Chargebacks, reversals, refunds, delayed presentment, reserves, and disputes can alter the final economics after the original approval. The author's synthesis is that a merchant is buying more than message transport: it is buying a governed path from uncertain customer intent to usable funds, with specified recourse when the path fails [3][13][14].

The economic principal can differ at each stage. The issuer owns the cardholder account and normally makes the authorization decision. The network supplies addressing, rules, processing, and institutional connectivity. The acquirer owns or sponsors the merchant relationship and must ensure that the merchant and its transactions satisfy network and regulatory requirements. A gateway or processor can supply technology without being the entity that ultimately carries settlement or merchant default exposure. Mapping legal responsibility separately from the visible software brand prevents a common analytical error: treating the company that presents the checkout page as the owner of every risk behind it.

### The merchant service charge contains three different profit questions

The MSC is not synonymous with interchange. The Payment Systems Regulator defines the merchant's charge as interchange plus scheme and processing fees plus acquirer net revenue, where acquirer net revenue contains the acquirer's other costs and margin [6][7]. The United States Government Accountability Office uses a similar decomposition: interchange goes to the issuer, network fees compensate the network, and processor or acquirer fees cover routing and other merchant services [13]. Each component should therefore be assigned to the participant that receives it before margin or market power is inferred.

Interchange changes incentives on both sides. A higher interchange payment can support issuer economics, including account service, rewards, fraud management, or credit-related costs, and can make issuance or card use more attractive. The same payment raises the cost passed through the acquiring side and can weaken merchant acceptance or increase retail prices. A lower interchange rate reverses part of that balance. Two-sided-market theory establishes why the distribution of prices can affect participation and transaction volume; it does not supply one universal optimal interchange rate because demand, merchant benefits, costs, competitive alternatives, surcharging, and market maturity differ [1][15].

Scheme and processing fees are economically distinct from interchange. They pay for participation, transaction processing, rule administration, security, brand, and optional or value-added services. A network may charge both issuers and acquirers and may also return substantial incentives to win or retain portfolios, volume, acceptance, or routing. Visa's 2025 filing says client incentives are paid to financial institutions, sellers, and other partners to grow volume, acceptance, use, and innovation. Mastercard reported USD 20.522 billion of payment-network rebates and incentives in 2025 and states that its network revenue is recognized net of such amounts [11][12]. Gross fee schedules therefore overstate the revenue retained by a network unless incentives and rebates are reconciled.

The acquirer sets the commercial package offered to the merchant. Under blended pricing, the merchant pays one or a few simplified rates even though underlying interchange and scheme costs vary by card, authentication, geography, merchant category, and transaction channel. Under interchange-plus pricing, interchange is passed through and the acquirer adds its price. Under interchange-plus-plus pricing, interchange and scheme or processing fees are separately passed through before the acquirer adds its own charge [7][13]. Simplicity can help a small merchant predict cost, but it can also conceal the difference between pass-through expense and provider margin. Granular pricing improves attribution but increases reconciliation and operational burden.

Economic incidence need not follow the invoice. A merchant formally pays the MSC, but it can attempt to recover the cost through higher prices, steer customers toward another method, negotiate with its acquirer, change its acceptance policy, or absorb the cost in margin. An issuer receives interchange, but competition for accounts can return part of it through rewards, service, or lower direct fees. A network can lose part of a nominal fee increase through client incentives. The author's assessment is that the relevant question is not "who writes the check?" but "whose behavior or retained surplus changes after all contractual and competitive responses?" [8][13][15].

### Network effects and economies of scale protect different layers

A card network experiences cross-side network effects: more usable credentials attract merchants, and more acceptance makes each credential more useful [1][9]. It also experiences processing economies of scale because common infrastructure, certification, security, rule administration, and connections can support more transactions at a declining average cost over relevant ranges. These forces reinforce one another but are conceptually separate. Network effects raise customer value; scale economies lower unit cost. A network can possess one more strongly than the other.

Scale also accumulates operating data, partner integrations, brand recognition, fraud patterns, and compliance routines. Visa reported that 329 billion payments and cash transactions carrying its brands were processed by Visa or other networks in fiscal 2025, of which 258 billion were processed by Visa. Mastercard reported that approximately 40 percent of its transactions were tokenized in 2025. These company disclosures show the operating scale available for investment and learning, but they do not by themselves prove that every incremental service improves competition or social welfare [11][12].

Large networks spend part of their economics defending participation. Issuer portfolios can be won through long-term rebates and incentives, and merchants or acquirers can receive routing or acceptance incentives. These payments are not incidental to the moat; they are one cost of maintaining it. Mastercard's 2025 filing reported that its five largest customers generated about 21 percent of net revenue, while Visa recorded USD 10.4 billion of client-incentive liabilities at September 30, 2025. The author's synthesis is that a strong network can have low physical capital intensity yet require substantial commercial reinvestment to preserve issuer, acquirer, and merchant alignment [11][12].

Multi-homing limits exclusivity. Merchants commonly accept more than one card brand, issuers can issue credentials on different networks, and customers can carry several cards or use bank-transfer alternatives. Yet multi-homing does not eliminate network power when one brand is sufficiently important that refusal would cause lost sales or checkout friction. The UK PSR found that alternatives imposed only limited constraints on acquiring-side scheme and processing fees because most merchants could not costlessly reject cards or steer spontaneous consumer payments elsewhere. It also noted that card-funded wallets can leave the underlying scheme fees in place [7]. The strength of a payment network therefore depends not only on the number of alternatives but on merchants' ability and incentive to redirect actual transactions.

### Merchant acquiring combines commodity processing with merchant-specific risk

Acquirers appear to sell a standardized result - acceptance and settlement - but the work begins with merchant selection. The provider verifies identity, business model, expected volumes, refund patterns, delivery timing, prohibited activities, financial capacity, and fraud exposure. It then configures acceptance channels, routes authorization, handles files and settlement, supports disputes, and supplies statements or data. The same transaction technology can have different risk when one merchant delivers goods immediately and another takes advance payment for future travel or subscriptions. Merchant underwriting and reserve policy are therefore part of acquiring economics, not administrative overhead [3].

The acquiring market contains both scale and differentiation. Transaction processing can become commodity-like, placing pressure on the provider's residual margin and favoring operators that spread fixed infrastructure across large volumes. Differentiation can arise from authorization performance, geographic coverage, local methods, fraud tools, payment orchestration, reconciliation, settlement speed, software integration, customer support, or expertise in a merchant vertical. The Philadelphia Fed paper identified price and scale as central competitive variables, while the UK PSR found that third-party processing can reduce some scale advantages even though processing costs and scheme-fee structures still favor larger acquirers in places [3][6].

Merchant size changes bargaining power and service cost. A large merchant can spread integration effort across high volume, operate several acquirers, optimize routing, and negotiate bespoke terms. A small merchant may prefer a payment facilitator that bundles onboarding, hardware or software, compliance, and one simple price. The PSR's 2021 review found that many smaller and medium-sized merchants did not regularly search or switch, that new customers often paid less than existing ones, and that nearly 90 percent of merchants in its evidence that tried to negotiate obtained a better deal. The regulator linked weak engagement to unpublished and non-comparable prices, indefinite contracts, and terminal-related switching frictions [6]. These findings are jurisdiction-specific, but they illustrate how merchant inertia can preserve acquiring margin even where many providers nominally exist.

Payment facilitators alter the minimum efficient scale for acceptance. They can aggregate micro-merchants, use one sponsor connection, standardize onboarding, and embed payments inside software. Aurazo's model shows two possible effects. Entry into an underserved niche can expand acceptance and produce additional upstream revenue for the acquirer. Entry against the acquirer's own merchant service can instead induce the acquirer to set an access fee that deters competition. The author's synthesis is that "more fintechs" does not automatically mean more effective competition: contestability depends on neutral access, sponsor economics, data portability, and the ability to switch the underlying acquirer [2].

Vertical integration changes both coordination and foreclosure risk. A firm that owns gateway, processor, acquirer, network, issuer, wallet, or merchant software can reduce handoffs, pool data, and coordinate fraud and service. The same firm can bundle fees, privilege its own route, raise a rival's access cost, or make switching harder. The correct assessment compares measurable coordination gains with the practical ability of merchants, issuers, and downstream providers to use alternatives. Integration is not a moat by definition; it is an architecture whose value depends on conduct, interoperability, and counterparty choice.

### Fraud, credit, and disputes move through the chain differently

A card transaction can fail through stolen credentials, account takeover, counterfeit use, friendly fraud, merchant non-delivery, processing error, insufficient funds, issuer credit loss, or operational outage. Network rules and law assign each category differently among issuer, acquirer, merchant, and consumer. Authentication, card-present status, token use, merchant controls, and procedural deadlines can alter liability. The acquirer may fund the merchant before a dispute resolves and may hold reserves or recover a chargeback later. The issuer can approve a fraudulent transaction or suffer cardholder credit loss, which is distinct from transaction fraud.

The Federal Reserve's 2023 debit study shows why channel and network type matter. Card-not-present transactions reached 34.4 percent of US debit volume in 2023, up from 9.6 percent in 2009. Dual-message transactions had a much larger share of total volume than single-message transactions and continued to exhibit higher fraud incidence than single-message transactions. These are aggregate US debit findings, not universal loss rates for every merchant or network, but they establish that channel mix can change fraud and routing economics even when total card use grows [5].

Tokenization changes the credential exposed, not the need for authorization or governance. EMV tokenization replaces the primary account number with a token constrained to an intended device, merchant, or use case and carries that token through acquirer, network, and issuer authorization. Lifecycle controls can update or deactivate a token without exposing the original account number. This can reduce the value of stolen data and preserve recurring payments when credentials change [10]. It can also make the token service and its interoperability part of routing competition, because an alternative route must receive enough information and certification to process the token correctly. The author's synthesis is that security design and competitive access should be evaluated together rather than treating either as an external side issue [4][10].

Authorization data can produce a reinforcing loop. More transactions can improve risk models, which can raise approval rates for legitimate customers and reduce losses, making the service more valuable to merchants and issuers. Yet data advantages are bounded by privacy law, model error, common standards, issuer control, and rivals' access to similar signals. A false-decline reduction creates merchant value through higher conversion; an aggressive approval strategy can simply move fraud or chargeback cost elsewhere. The proper metric is risk-adjusted approved volume and retained merchant economics, not approval rate alone.

### Four-party, closed-loop, and account-to-account models allocate control differently

A four-party network specializes in coordination among independent issuers and acquirers. This can maximize reach and distribute capital requirements, but it also creates multiple fee layers and bargaining relationships. A closed-loop provider directly links sellers and consumers and can coordinate underwriting, rewards, merchant pricing, service, and transaction data more tightly. It also carries more concentrated credit, funding, regulatory, and acceptance-building responsibility. Visa identifies American Express, Discover, private-label systems, and certain digital platforms as closed-loop competitors with direct connections to both sellers and consumers [11].

The distinction is not absolute. A nominally closed-loop scheme can use partner issuers and third-party acquirers, while a four-party network can buy processors, token services, fraud tools, and open-banking capabilities. Wallets can sit above either architecture. The author's assessment is that analysts should map five control points instead of relying on the label: the customer credential, merchant contract, authorization decision, transaction rail, and final credit or deposit account. Control of those points determines data, risk, price, and switching power.

Account-to-account payments move funds between bank or stored-value accounts without requiring a card transaction. Fast-payment systems such as Pix, UPI, and TIPS can provide an alternative back-end rail, while open-banking interfaces or merchant applications can create the front-end initiation experience. BIS research reports that A2A transactions dominate digital-payment growth in many emerging economies, while card payments remain a major growth driver in advanced economies. The same research cautions that new entry does not guarantee effective competition because interoperability, scale, consumer habits, fraud management, and incumbent positions still matter [9].

A2A and cards are not identical bundles. Cards can combine acceptance, instant authorization, issuer-funded credit, rewards, standardized disputes, fraud allocation, and a recognizable credential. A2A can offer direct settlement, rich messages, lower marginal rail cost, and reduced dependence on card interchange, but the merchant or service provider must still solve customer authentication, authorization certainty, refunds, fraud, error resolution, and conversion at checkout. The author's synthesis is that an alternative wins when its total commercial proposition is superior for a use case, not merely because its raw transfer fee is lower [7][9].

### Regulation can move the profit pool rather than shrink it

Interchange caps directly reduce one transfer, but the resulting savings need not pass immediately or completely to merchants and consumers. The European Commission's review found that regulated consumer-card interchange declined and merchant charges fell after the EU Interchange Fee Regulation. It also estimated gradual pass-through, increased cross-border acquiring, and some offset from higher scheme fees and acquirer retention. Cross-border acquiring reached 15 percent of debit-card transaction value and 16.8 percent of credit-card transaction value in the evidence reviewed, showing integration without complete market transformation [8].

Routing rules attack a different mechanism. US Regulation II requires at least two unaffiliated debit networks and protects merchant routing choice. The Federal Reserve's 2022 rule clarified that each debit transaction type, including card-not-present transactions, must have that network choice. The merchant's preference is commonly implemented by its acquirer or processor, so nominal network enablement matters only when the technical chain can actually route the transaction [4]. Routing competition can lower price or improve service, but it also creates certification, token, fraud, liability, and operational comparisons that a simple network count does not capture.

Scheme and processing fees can become more important after interchange is capped. The UK PSR's 2025 review separated the acquiring and issuing sides and concluded that Visa and Mastercard faced much stronger competitive constraints when competing for issuer portfolios than when supplying core scheme and processing services to acquirers. It found limited evidence that alternative payment methods constrained acquiring-side fees for spontaneous consumer payments, because merchants often could not steer customers without friction or lost conversion. It also found little evidence that the largest acquiring-side fee changes were driven by detailed cost analysis or competitive pressure [7]. These findings illustrate fee migration and asymmetric bargaining; they do not prove that every individual fee lacks service value.

The author's synthesis is that regulation should be audited across the full stack. A successful cap on interchange can fail to reduce merchant cost if scheme fees or acquirer margins rise. A routing mandate can fail if tokens, processors, merchant configurations, or issuer enablement make the alternative unusable. Transparency can fail if fee schedules are technically disclosed but too complex to reconcile. Conversely, a rule can lower merchant costs while also reducing issuer-funded rewards or changing fraud investment. The relevant assessment records who pays, who receives, what service changes, and how participation responds.

## Evidence

### US debit data show scale, channel migration, and uneven routing

The Federal Reserve's biennial network and issuer collection provides a broad transaction-level view of US debit economics. Payment networks processed 100.7 billion debit and general-use prepaid purchase transactions worth USD 4.7 trillion in 2023. Dual-message networks accounted for 71.4 percent of volume and 72.9 percent of value, while single-message networks accounted for the remainder. Card-not-present transactions represented 34.4 percent of volume, up from 9.6 percent in 2009 [5]. The method aggregates reports required from networks and covered issuers, so it measures the regulated system more directly than a merchant or company survey.

The fee evidence separates regulated and exempt activity. Average interchange on covered 2023 transactions was USD 0.24 over single-message networks and USD 0.22 over dual-message networks, while transactions exempt from the cap averaged USD 0.52. The same report records USD 5.68 billion of network payments and incentives to issuers and acquirers or merchants, including USD 3.71 billion paid to the acquiring or merchant side. These figures demonstrate that list fees and statutory caps coexist with bilateral or multilateral incentives; net economics cannot be inferred from the default interchange schedule alone [5].

The routing pattern is equally important. The Federal Reserve's 2022 rulemaking reported that single-message networks exceeded 40 percent of card-present debit transactions in 2019 but held only a low aggregate share of card-not-present transactions. It therefore required issuers to enable at least two unaffiliated networks for card-not-present use as well as card-present use. The evidence supports a narrow conclusion: legal routing choice had not automatically produced equivalent technical contestability online. It does not show that the lowest-fee route is always best, because fraud, authorization, reliability, and merchant configuration also differ [4].

### UK acquiring evidence separates provider entry from effective merchant choice

The PSR's 2021 card-acquiring review examined provider structure, merchant contracts, fee pass-through, and merchant behavior. It defined the MSC as interchange plus scheme fees plus acquirer net revenue and found that the supply of acquiring did not work well for smaller and medium-sized merchants and for large merchants up to the review's GBP 50 million annual card-turnover threshold. The regulator identified unpublished and non-comparable pricing, indefinite contracts, and terminal arrangements as search and switching frictions. It also found that nearly 90 percent of merchants that tried to negotiate obtained a better deal [6].

This is evidence of behavioral and contractual frictions, not proof of a natural monopoly. Payment facilitators and other entrants had expanded, and third-party processing reduced some infrastructure barriers. The result instead shows that nominal supplier count and realized competitive pressure can diverge when merchants have difficulty comparing total cost or triggering a switch. Large merchants can operate different economics because their volume supports direct integration, bespoke pricing, and greater bargaining leverage [6].

The PSR's 2025 scheme and processing review examined the upstream layer. It concluded that alternatives did not effectively constrain Mastercard and Visa on the acquiring side for most spontaneous consumer payments, even though wallets, bank transfers, buy-now-pay-later, and other methods existed. Card-funded wallets often preserved the underlying card fee, and steering could add friction or reduce conversion. The regulator found stronger competition for issuer portfolios than for acquiring-side core scheme and processing services [7]. Together, the two reviews show two bottlenecks: merchants can face friction in changing acquirers, while acquirers can face limited alternatives to the major scheme connected to a customer's chosen card.

### EU regulation reduced interchange but did not make the rest of the stack disappear

The European Commission's 2020 review assessed the Interchange Fee Regulation after caps and business rules took effect. It reported that consumer-card interchange fell, merchant service charges declined, and cross-border acquiring increased. The underlying study estimated annual interchange savings of about EUR 2.68 billion to the acquiring side and merchant savings of about EUR 1.2 billion, with acquirers retaining part of the initial reduction and scheme fees offsetting part of the effect [8]. These figures were modelled from the review period and should not be treated as a permanent annual law.

The evidence supports two qualified findings. First, a direct cap can reduce the targeted fee and pass at least part of the benefit through to merchants. Second, pass-through depends on acquiring competition, contract renewal, merchant bargaining, and changes elsewhere in the stack. The Commission also reported that cross-border acquiring remained a minority of transaction value despite growth, and it called for further monitoring where post-reform data were limited [8]. Regulation changed bargaining conditions without eliminating the network, processor, or acquirer functions that still required payment.

### Company filings reveal a high-scale network with material commercial reinvestment

Visa's fiscal 2025 filing reported 329 billion Visa-branded payment and cash transactions processed by Visa or other networks and 258 billion processed by Visa itself. It describes payments volume as the principal driver of service revenue and processed transactions as the principal driver of data-processing revenue. It also reports that net revenue rose with payments volume, cross-border volume, and processed transactions, partly offset by higher client incentives, and that value-added-services revenue reached USD 10.9 billion [11]. The filing is a primary description of Visa's economics, not an independent estimate of market welfare.

Mastercard's 2025 filing makes the transfer distinction explicit. It says interchange is generally collected from acquirers and paid to issuers and that Mastercard does not earn interchange revenue. Mastercard instead earns payment-network revenue from volume, switching, and related services, plus value-added services. Payment-network rebates and incentives reached USD 20.522 billion in 2025, and approximately 40 percent of Mastercard transactions were tokenized [12]. The filings together show why a network's economic moat should be tested after client incentives and continuing security investment, not from gross transaction scale alone.

The two filings also show strategic convergence. Both networks invest beyond card switching in fraud, tokenization, open banking, account-to-account movement, data, and advisory services [11][12]. This broadening can defend the franchise when a new rail emerges, but it complicates market definition: an incumbent can compete with an alternative, supply technology to it, or integrate it into a network-of-networks strategy. The author's assessment is that analysts should separate organic card-rail economics from adjacent services before attributing all growth to the original moat.

### Tokenization and payment facilitation show that technical architecture affects entry

EMVCo's specification makes tokenization an end-to-end credential framework. A constrained token can travel from purchase through acquirer and network to issuer, coexist with merchant or acquirer tokens, and support lifecycle management without repeatedly exposing the PAN. More than one hundred organizations from across the payment ecosystem contribute to EMV specifications, which supports interoperability while leaving implementation to market participants [10]. The evidence establishes the security and coordination function; it does not prove that every token service is competitively neutral.

Aurazo's BIS working paper supplies the analogous access model for payment facilitators. A sub-acquirer can serve merchants without a direct network connection by purchasing upstream access from an acquirer. Entry can raise welfare when it reaches a niche the acquirer did not serve, while direct downstream competition can give the acquirer an incentive to set a prohibitive access fee. The paper is a theoretical model rather than a market-wide causal estimate, so its importance is diagnostic: it identifies the conditions and contract terms that should be measured when payment-facilitator growth is cited as evidence of competition [2].

BIS evidence on fast payments broadens the comparison. Its 2026 review identifies Pix, UPI, and TIPS as A2A alternatives and finds that digitalization and new entrants have increased contestability in many economies. It nevertheless reports that incumbent banks and card networks retain dominant positions in key markets and that fragmentation, interoperability, risk, and access remain policy concerns [9]. New rails can challenge card economics, but network effects reappear around whichever system achieves widespread use.

## Implications

### For investors: map retained economics, not gross payment volume

An investor should begin with the industry's value chain rather than a total-addressable-market claim. Record the parties that control the credential, merchant contract, authorization, network route, settlement account, fraud decision, dispute rule, and customer relationship. Then assign each fee: interchange to the issuer, scheme or processing fees to the network or processor, and residual acquiring revenue to the merchant provider. This prevents interchange growth from being mistaken for network revenue or total merchant fees from being mistaken for acquirer margin [6][11][12][13].

The next step is a per-transaction profit bridge. For a network, decompose revenue by domestic volume, transaction processing, cross-border activity, and value-added services, then subtract client incentives and required technology, security, legal, and regulatory spending. For an acquirer, start with the MSC, remove interchange and network pass-throughs, and then deduct processing, sales, onboarding, hardware or software, fraud, chargebacks, reserves, customer support, and compliance. For an issuer, separate interchange from interest, account fees, rewards, funding, credit loss, fraud, and servicing. The author's synthesis is that only the retained, risk-adjusted amount belongs in a margin or moat analysis.

Scale deserves two tests. First, does higher volume lower unit cost or improve fraud and authorization enough to create economic value? Second, how much of that value must be returned through incentives to retain issuers, acquirers, merchants, or routes? Visa's and Mastercard's filings show both high processing scale and substantial client incentives [11][12]. A business can have a formidable network effect and still face a rising commercial-reinvestment burden. Gross margin without incentive intensity, customer concentration, and contract duration can overstate durability.

Cross-border volume should be isolated because network revenue and merchant cost can differ materially from domestic activity. Currency conversion, regional routing, regulation, and local acquiring relationships can change the economics. Visa and Mastercard both identify cross-border volume as an important revenue driver [11][12]. A normalized valuation should therefore distinguish durable travel and commerce flows from temporary mix, currency volatility, or post-disruption recovery.

Value-added services require a stand-alone test. Fraud tools, tokenization, authentication, data, advisory work, open banking, and merchant software can deepen relationships and diversify revenue. They can also be bundled with the core rail, subsidized to defend it, or acquired at a price that transfers future returns to the seller. The investor should ask whether the service wins when sold independently, whether it improves core retention, who owns the underlying data, and whether regulation can require interoperability or separation. Reporting one combined growth rate can hide a slowing network and a growing acquired-service portfolio.

The downside case should combine pressures rather than vary one at a time. Lower interchange can change issuer incentives; routing rules can shift volume; scheme-fee scrutiny can constrain network pricing; an A2A rail can reduce some card use; a large issuer can demand higher incentives; and fraud or outages can require more investment. At the same time, acceptance and credential scale can preserve volume. The author's assessment is that the moat fails economically when the incremental cost of retaining both sides and meeting regulation rises faster than the retained revenue per transaction, even if nominal payment volume continues to grow.

### For merchants and acquirers: optimize total acceptance economics

A merchant should compare payment methods on total contribution, not the posted acceptance rate alone. Relevant variables include authorization, conversion, fraud, chargebacks, refunds, settlement delay, customer preference, average order value, support, reconciliation, and working capital. A cheaper rail can be more expensive if it increases abandonment or shifts fraud liability; a higher-fee method can be uneconomic if rewards or customer preference do not create incremental sales. The author's synthesis is that the correct denominator is profitable completed commerce, not attempted payment count.

Pricing format should match analytical capacity. A small merchant may rationally accept a simple blended rate in exchange for predictable cost and bundled service. A larger merchant may benefit from interchange-plus-plus pricing, transaction-level reporting, multiple acquirers, and routing optimization. The PSR evidence shows that non-comparable prices and weak switching triggers can leave merchants on inferior terms, while negotiation often improved the deal for those that tried [6]. A recurring procurement review should therefore reconcile pass-through components, provider margin, terminal or gateway contracts, and termination conditions.

Multi-acquiring can provide redundancy, geography, and routing choice, but it creates integration and reconciliation cost. A merchant or payment orchestrator must maintain token portability, consistent fraud controls, settlement matching, refunds, and dispute records across providers. Concentrating volume can earn a better rate, while diversifying it can improve resilience and bargaining power. The reversible design is to preserve portable credentials and data interfaces before shifting meaningful volume; otherwise the apparent option to switch exists only on paper.

Acquirers should evaluate merchant profitability by cohort rather than by headline volume. A fast-growing merchant can create losses through fraud, non-delivery, refunds, or chargebacks that emerge after revenue is booked. Payment facilitators must align rapid onboarding with sponsor-bank and network obligations. The author's synthesis is that merchant risk should be priced through reserves, limits, monitoring, and contract terms rather than hidden in a uniform take rate. Good underwriting protects both the acquirer and sound merchants from losses created by a risky minority.

Routing should be treated as a governed decision engine. Price matters, but so do acceptance, issuer reach, token support, latency, uptime, fraud performance, dispute rules, and incentive thresholds. Regulation II makes the acquirer or processor the practical implementer of many merchant routing choices in US debit [4]. A routing table that cannot explain why a transaction selected one rail is difficult to audit for both economics and compliance. Merchants should retain transaction-level evidence sufficient to compare expected and realized route outcomes.

### For networks and issuers: participation must remain jointly attractive

A network cannot maximize one side indefinitely while assuming the other remains captive. Higher issuer economics can encourage credentials, rewards, or use, but excessive merchant cost can produce political intervention, steering, or investment in alternatives. Lower merchant cost can improve acceptance while weakening issuer participation or rewards. Rochet and Tirole's central lesson is that the price structure coordinates both sides [1]. The practical extension is that the structure must remain legitimate enough to survive regulation and transparent enough for participants to understand what they buy.

Tokenization illustrates the design obligation. Security improves when exposed PANs are replaced with constrained, lifecycle-managed tokens [10]. Competition improves when authorized routes can process those credentials without artificial exclusion. The author's synthesis is that a durable token service should publish clear access, certification, portability, and error-resolution rules while preserving domain controls. A network that uses security as a pretext for avoidable lock-in may strengthen short-term routing share while increasing regulatory risk.

Issuer economics should be separated by function. Interchange can help fund account service, fraud controls, and rewards, but consumer credit returns also depend on interest, funding, losses, and capital. A reduction in interchange therefore does not translate mechanically into an equal reduction in service, nor is it costless. Management should identify which benefits are marginally supported by interchange and which are strategic customer-acquisition spending. This distinction becomes essential when regulators cap a fee or merchants route to a lower-cost network.

Networks should measure the return on incentives as rigorously as capital expenditure. Long-term issuer, acquirer, seller, and routing agreements can stabilize volume, but they can also conceal declining organic preference. Useful measures include gross and net revenue per transaction, incentive duration, renewal step-ups, concentration, incremental volume, cross-sell, and performance after the incentive expires. The author's assessment is that incentives build a moat only when they create durable participation or service integration; recurring payments that merely prevent defection are a maintenance expense.

### For regulators: test the complete response to each rule

Price regulation should track fee migration. The EU evidence shows that interchange caps reduced the targeted fee and merchant charges, but acquirers initially retained part of the savings and scheme fees offset part of the effect [8]. A review should therefore monitor interchange, scheme fees, optional services, acquirer margins, issuer incentives, cardholder charges, rewards, acceptance, fraud, and retail pass-through under consistent definitions. Declaring success from one falling line item can miss redistribution elsewhere.

Routing mandates should be tested transaction by transaction. The relevant question is not whether a card displays two network marks but whether each important transaction type can actually be processed over two unaffiliated routes with usable tokens, issuer enablement, acquirer support, merchant configuration, and comparable liability rules. The Federal Reserve's card-not-present clarification addressed precisely this gap [4]. Compliance evidence should include successful production routing, not only contractual eligibility.

Access rules should distinguish network connection from downstream service. Payment facilitators can broaden acceptance, especially for small merchants, but dependence on a competing acquirer for upstream access can allow foreclosure through price or technical restrictions [2]. Regulators should identify which functions are natural shared infrastructure, which can support competition, and where non-discriminatory access is feasible without shifting unmanaged settlement or fraud risk to the system.

Alternative rails should be judged on substitution at the point of commerce. A wallet funded by a card may create front-end competition while leaving the card network's back-end economics intact. An A2A system can bypass the card rail but still needs adoption, interoperability, fraud controls, and merchant integration. BIS and PSR evidence both show that the mere existence of another method does not guarantee an effective constraint [7][9]. Policy should therefore measure successful steering, conversion, merchant cost, fraud, refunds, and consumer use rather than counting payment applications.

Competition and resilience can conflict. A single widely accepted network reduces fragmentation and can support common security investment; concentration can also permit fees or rules that participants cannot discipline. Opening access can improve contestability while adding operational, cyber, fraud, and participant-default risks [9]. The author's synthesis is that the least harmful intervention is usually the one that preserves interoperability and service continuity while making price, route, and participation rules contestable.

### A disciplined industry assessment

The author's synthesis is a ten-step framework. First, draw the authorization, clearing, settlement, refund, and dispute flows. Second, identify the legal party responsible at each stage. Third, decompose the MSC into interchange, network, processor, and acquirer components. Fourth, reconcile gross fees with incentives and rebates. Fifth, measure acceptance, credentials, transactions, and volume without treating them as interchangeable. Sixth, separate card-present, card-not-present, domestic, and cross-border economics. Seventh, map fraud, credit, chargeback, and merchant-default exposure. Eighth, test technical and contractual routing options, including tokens. Ninth, compare closed-loop, four-party, wallet, and A2A alternatives as complete service bundles. Tenth, run regulatory and fee-migration scenarios across every participant [4][5][7][9][10][11][12].

This framework produces the central conclusion. Payment networks create real value by coordinating acceptance, information, rules, and settlement across institutions that would otherwise need bilateral arrangements. Their scale can become a durable advantage, but the value is shared and contested: issuers seek economics for credentials and risk, merchants seek conversion at acceptable cost, acquirers seek margin after pass-through expenses, and regulators seek competition without undermining reliability. The industry's attractive profit pools persist where a participant controls a necessary, hard-to-reproduce function while keeping access, risk allocation, and price acceptable to the rest of the system.

## Sources

1. Rochet, J.-C., and Tirole, J. (2003). "Platform Competition in
   Two-Sided Markets." Journal of the European Economic Association,
   1(4), 990-1029.
   https://www.tse-fr.eu/publications/platform-competition-two-sided-markets [high]

2. Aurazo, J. (2024). "Interchange Fees, Access Pricing and
   Sub-Acquirers in Payment Markets." BIS Working Papers No. 1163.
   https://www.bis.org/publ/work1163.htm [high]

3. Cheney, J. S. (2007). "The Merchant-Acquiring Side of the Payment
   Card Industry: Structure, Operations, and Challenges." Federal
   Reserve Bank of Philadelphia Payment Cards Center Discussion Paper.
   https://www.philadelphiafed.org/-/media/frbp/assets/consumer-finance/discussion-papers/D2007OctoberMerchantAcquiring.pdf [high]

4. Board of Governors of the Federal Reserve System (2022). "Debit
   Card Interchange Fees and Routing," final rule amending Regulation II.
   https://www.federalreserve.gov/newsevents/pressreleases/files/bcreg20221003a1.pdf [high]

5. Board of Governors of the Federal Reserve System (2026). "2023
   Interchange Fee Revenue, Covered Issuer Costs, and Covered Issuer and
   Merchant Fraud Losses Related to Debit Card Transactions."
   https://www.federalreserve.gov/paymentsystems/2023-interchange-fee.htm [high]

6. Payment Systems Regulator (2021). "Market Review into
   Card-Acquiring Services: Final Report," MR18/1.8.
   https://www.psr.org.uk/media/p1tlg0iw/psr-card-acquiring-market-review-final-report-november-2021.pdf [high]

7. Payment Systems Regulator (2025). "Market Review of Card Scheme and
   Processing Fees: Final Report," MR22/1.10.
   https://www.psr.org.uk/media/sogjjvl4/mr22-110-card-sp-fees-mr-final-report-publication-redacted-mar-2025-updated.pdf [high]

8. European Commission (2020). "Report on the Application of Regulation
   (EU) 2015/751 on Interchange Fees for Card-Based Payment Transactions,"
   Commission Staff Working Document SWD(2020) 118 final.
   https://competition-policy.ec.europa.eu/system/files/2021-10/IFR_report_card_payment.pdf [high]

9. Natalizi, D., and Shreeti, V. (2026). "Competition in Retail Digital
   Payments." BIS Bulletin No. 127.
   https://www.bis.org/publ/bisbull127.pdf [high]

10. EMVCo. "EMV Payment Tokenisation." Technical framework overview,
    benefits, roles, and implementation resources.
    https://www.emvco.com/emv-technologies/payment-tokenisation [high]

11. Visa Inc. (2025). Form 10-K for the fiscal year ended September 30,
    2025. Primary disclosure on transaction processing, volume, client
    incentives, value-added services, tokenization, competition, and risk.
    https://www.sec.gov/Archives/edgar/data/1403161/000140316125000089/v-20250930.htm [high]

12. Mastercard Incorporated (2026). Form 10-K for the fiscal year ended
    December 31, 2025. Primary disclosure on network revenue,
    interchange, incentives, tokenization, value-added services, and risk.
    https://www.sec.gov/Archives/edgar/data/1141391/000114139126000013/ma-20251231.htm [high]

13. U.S. Government Accountability Office (2025). "Payment Cards:
    Costs and Benefits for Federal Entities," GAO-25-107298.
    https://www.gao.gov/assets/gao-25-107298.pdf [high]

14. Scott, A. P. (2024). "Credit Card Swipe Fees and Routing
    Restrictions." Congressional Research Service Report R48216.
    https://www.congress.gov/crs-product/R48216 [high]

15. Prager, R. A., Manuszak, M. D., Kiser, E. K., and Borzekowski, R.
    (2009). "Interchange Fees and Payment Card Networks: Economics,
    Industry Developments, and Policy Issues." Federal Reserve Board
    Finance and Economics Discussion Series 2009-23.
    https://www.federalreserve.gov/pubs/feds/2009/200923/index.html [high]

## See Also

- `library/industries-sectors/network-effects-platform-economics.md` -- the general two-sided-market and multi-homing framework behind card acceptance.
- `library/industries-sectors/industry-profit-pools.md` -- the method for separating transaction volume from retained profit across a value chain.
- `library/industries-sectors/value-chain-analysis.md` -- the activity map used to assign fees, risks, and bargaining power to each payment participant.
- `library/case-studies/berkshire-american-express-investment.md` -- a company case on an integrated issuer, acquirer, and network franchise.
- `library/macro-micro/market-structures.md` -- the industrial-organization framework for scale, entry barriers, oligopoly, and contestability.
