---
name: foreign-exchange-markets-and-currency-risk
id: 20261001T073337Z
tier: library-topic
domain: finance
author: Librarian
tags: [foreign-exchange, currency-risk, fx-swaps, currency-hedging, covered-interest-parity, settlement-risk, corporate-treasury]
links: [library/finance/derivatives-and-risk-transfer.md, library/finance/financial-market-microstructure.md, library/macro-micro/currency-and-exchange-rates.md, library/portfolio-risk-management/currency-hedging-in-global-portfolios.md]
---

# Foreign Exchange Markets Convert Currency Mismatches Into Funding, Pricing, and Settlement Risks

Foreign exchange markets connect payments and financing across monetary boundaries, but no contract simply removes currency risk: each changes its amount, timing, owner, or cash-flow path. A sound FX decision therefore begins with the exposure and settlement obligation, not a forecast, and tests whether spot, forwards, swaps, options, natural offsets, and accounting treatment together reduce the risk the institution can least afford to bear [1][4][8].

## Background

Foreign exchange is the financial machinery through which a claim denominated in one currency becomes a payment, asset, or liability denominated in another. Trade creates currency needs when an importer must pay a foreign supplier or an exporter receives foreign-currency revenue. Cross-border borrowing and investment create them when the funding currency differs from the asset, income, or reporting currency. Dealers, asset managers, banks, non-financial firms, central banks, hedge funds, and trading firms meet in a largely over-the-counter market to exchange currencies now, commit to exchange them later, or exchange funding streams across time [1][2]. The market is therefore both a conversion market and a funding market. Treating it only as a venue for directional bets misses the transactions that allow international trade, banking, investment, and reserve management to settle.

The market's scale reflects these overlapping functions. The Bank for International Settlements surveyed reporting dealers in more than 50 jurisdictions and estimated average OTC FX turnover of $9.6 trillion per day in April 2025 on a net-net basis. Spot accounted for $3.0 trillion, outright forwards for $1.8 trillion, FX swaps for $4.0 trillion, currency swaps for $172 billion, and options and other products for $634 billion [1]. Turnover is not the same as outstanding exposure, market value, profit, or final settlement: it records transactions entered during the survey month and adjusts for specified inter-dealer double counting [1]. The dominance of FX swaps is economically important because their paired spot and forward legs are widely used to obtain one currency against another for a limited period, so much of the largest FX category is short-term funding and liquidity management rather than a simple view on where a spot rate will move [1][2].

Foreign exchange trading is decentralized rather than organized around one consolidated order book. Banks quote customers, offset positions with other dealers, trade on electronic venues, provide prime brokerage, and manage inventory and balance-sheet limits. The BIS found that inter-dealer activity represented 46 percent of global turnover in April 2025, while transactions with other financial institutions represented 50 percent; non-financial customers accounted for the remainder [1]. Earlier BIS analysis documented how bank funding, portfolio hedging, prime brokerage, and electronic trading changed both volumes and the mix of participants [2]. The Global Foreign Exchange Committee's FX Global Code responds to this institutional structure with voluntary principles on ethics, governance, execution, information sharing, risk management, and confirmation and settlement. The Code supplements rather than replaces law and regulation [3].

The contract families developed around different timing and payoff needs. A spot trade exchanges two currencies for near-term value. An outright forward fixes today the rate for a future exchange. An FX swap combines an initial exchange with a reverse exchange at a later date. A cross-currency swap generally exchanges longer streams of interest and, under its terms, principal. An option gives its buyer a right rather than a symmetric obligation, in return for a premium [1][4]. Non-deliverable forwards settle a cash difference rather than exchanging both principals and are important when currencies are restricted or delivery is impractical [1]. These labels are not interchangeable. A treasury that needs currency today and will reverse the need next month faces a funding problem suited to a swap; a known invoice due in three months is a future conversion problem suited to a forward; an uncertain tender may call for a contingent payoff rather than a fixed obligation.

Settlement made the market's operational risk visible long before electronic trading. In 1974, Bankhaus Herstatt was closed after counterparties had paid Deutsche marks in Frankfurt but before receiving dollars in New York. The episode demonstrated principal risk: one party can irrevocably deliver the currency sold while the other payment remains uncertain [5]. Payment-versus-payment, or PvP, addresses that failure mode by making final payment of one currency conditional on final payment of the other. It does not eliminate replacement-cost risk or the liquidity loss caused by a delayed receipt [4][5]. The Basel Committee accordingly treats FX settlement as a system of principal, replacement-cost, liquidity, operational, legal, and capital risks rather than as a clerical step after the economic trade [4].

Pricing theory supplied a benchmark for linking spot, forward, and money markets. Covered interest parity, or CIP, states that comparable borrowing and lending in two currencies, combined with a forward exchange, should not leave a riskless return difference after matching credit, tenor, collateral, transaction, and funding terms [6]. Before the global financial crisis, analysts often treated small CIP deviations as implementation noise. Du, Tepper, and Verdelhan documented persistent post-crisis deviations across major currencies and particularly strong effects for contracts crossing quarter ends, consistent with bank balance-sheet costs affecting the price of intermediation [6]. BIS research separately connects FX swap liquidity to spot liquidity, funding conditions, and dealer capacity [13]. A forward rate is therefore not merely a market forecast of the future spot rate: it embeds the interest-rate relationship under the applicable funding convention and can include a cross-currency basis and dealer costs [6][13].

Corporate currency management adds another distinction. Transaction exposure arises from contractual or highly probable foreign-currency cash flows; translation exposure arises when foreign operations and balances are converted into a reporting currency; and economic exposure is the broader sensitivity of future cash generation and competitive position to exchange rates [8]. IAS 21 formalizes the accounting boundary by distinguishing an entity's functional currency from foreign currencies and by specifying how foreign-currency transactions, monetary items, and foreign operations are translated [11]. IFRS 9 separately governs many derivatives and the conditions under which hedge accounting can align parts of the accounting result with documented risk-management relationships [12]. Accounting presentation, contractual cash flow, and economic exposure can therefore move differently even when they originate from the same foreign operation.

Synthesis: the finance problem is not to predict every exchange-rate movement. It is to map currencies, amounts, dates, legal entities, counterparties, funding sources, and accounting consequences, then choose a combination of contracts and operating decisions that remains workable through settlement and stress. Macroeconomic exchange-rate determination belongs to the adjacent macro-micro topic, while portfolio-level currency allocation belongs to portfolio-risk-management. This topic stays with the operational layer identified by the finance anchor: how the FX market prices, intermediates, funds, settles, and reports cross-currency obligations.

## Core Concepts

### A quotation is a ratio with a direction

An exchange rate has meaning only after both currencies and the quotation direction are specified. Let `S` denote domestic-currency units per one unit of foreign currency. A rise in `S` then means that the foreign currency appreciates and the domestic currency depreciates. Under the reciprocal quote, the same event appears as a fall. Bid and offer must also be kept distinct: a dealer buys at one side and sells at the other, so the executable conversion differs from a mid-market indication. The difference can widen with order size, volatility, time zone, currency liquidity, counterparty terms, and dealer capacity [2][3][13]. Synthesis: every exposure report and hedge instruction should state the quote convention once and carry it through valuation, sensitivity, and performance attribution; otherwise even a correct formula can be applied with the wrong sign.

Cross rates link two currencies through a third. Because the US dollar was on one side of 89.2 percent of OTC FX trades in April 2025, many currency pairs are priced or hedged through dollar legs rather than through a deep direct market [1]. Triangular consistency provides an arbitrage benchmark among executable quotes, but actual execution must account for all bid-offer spreads, timing, credit, and settlement legs. A calculated cross rate from midpoints is not automatically a tradable profit. The same discipline applies to effective rates and baskets: weights and rebalance rules must be specified before a multi-currency index can define an exposure.

### Spot solves immediate conversion, not future uncertainty

A spot transaction is a single outright exchange for value within the market's near-term settlement convention; the BIS turnover definition generally uses delivery within two business days and reports the spot leg of a swap as part of the swap rather than as separate spot turnover [1]. Spot is appropriate when the currency need is known and immediate. It does not protect a receivable due next quarter, a foreign subsidiary's future earnings, or the cost of rolling short-term funding. A firm that buys currency only when an invoice matures remains exposed between the commercial commitment and the spot purchase.

Spot execution also creates settlement obligations. The customer may trade with one bank while its currencies move through correspondent accounts, time zones, and payment systems. A competitive price does not by itself establish that both principals will exchange safely. Confirmation accuracy, standard settlement instructions, cutoff times, sanctions screening, nostro liquidity, and PvP eligibility determine whether the quoted trade becomes final cash as intended [3][4][5]. Synthesis: the all-in quality of a spot transaction includes both execution price and the probability, timing, and liquidity cost of successful settlement.

### A forward fixes a rate while creating a future obligation

An outright forward commits the parties to exchange specified currencies, amounts, and value date at an agreed rate. It can turn a known future foreign-currency receipt or payment into a known home-currency amount. If a euro-functional firm will receive dollars in three months, selling those dollars forward can reduce the uncertainty in euro proceeds. The contract also creates a symmetric obligation: if the underlying sale is cancelled or the amount changes, the forward remains unless it is closed, resized, or offset. A hedge of an uncertain forecast can therefore become a standalone currency position [8][12].

Under a domestic-currency-per-foreign-currency quote and simple matched-tenor rates, a frictionless CIP benchmark can be written as follows [6]:

```text
F / S = (1 + i_domestic * T) / (1 + i_foreign * T)
```

`F` is the forward rate for tenor `T`; `i_domestic` and `i_foreign` are comparable funding rates under the stated convention. The precise equation changes with compounding, day count, collateral, and quote direction. Forward points, `F - S`, therefore reflect the interest-rate relationship under that convention; they are not by themselves a fee and do not prove where spot will trade at maturity [6]. An executable forward can also include bid-offer spread, credit and capital charges, liquidity premia, and cross-currency basis. Comparing a forward with an unhedged position requires separating these components rather than labeling the entire premium or discount as hedge cost.

A non-deliverable forward, or NDF, fixes a reference exchange rate but settles the difference in an agreed settlement currency instead of delivering both currencies [1]. It can reduce price risk where delivery is restricted, but it leaves the firm with the task of obtaining or disposing of the underlying currency through local channels. Fixing-source, timing, convertibility, and capital-control risks can make the NDF payoff differ from the actual cash need. Synthesis: deliverability is a design variable, not a minor contract detail.

### An FX swap is a collateralized funding transformation in economic substance

An FX swap exchanges two currencies on one value date and reverses the exchange on a later date at a rate fixed at inception. The paired legs largely remove directional currency exposure for the contract period when notionals and dates match, but they create an obligation to return full principal at maturity. BIS analysis describes the instrument as economically similar to borrowing one currency against another as collateral [2][7]. Banks use swaps to manage currency liquidity; investors and firms use them to fund assets, bridge mismatched cash dates, or roll hedges [1][2].

The distinction between an FX swap and an outright forward matters. A forward has one future exchange. An FX swap has an initial exchange and a reversing exchange. After the first leg settles, the remaining second leg resembles a forward obligation, but the transaction has already changed both parties' cash positions. A treasury with dollars today and a euro payment today can use a swap to obtain euros temporarily while locking the dollar reversal. A treasury that already has the needed euros and only wants to fix a future dollar receipt generally does not need the initial spot leg [1][7].

Short maturities make FX swaps flexible and liquid, but repeated rolling turns a long exposure into a sequence of refinancing decisions. BIS data show that large volumes of swaps and forwards mature within one year, while off-balance-sheet payment obligations can be enormous relative to the cash initially exchanged or reported as conventional debt [7]. If the basis widens, dealers reduce capacity, collateral terms tighten, or a market closes at the roll date, the next swap may be expensive or unavailable. A hedge or funding plan that works at the final asset horizon can therefore fail at an intermediate maturity.

### Cross-currency swaps match longer cash-flow streams but add more dimensions

A cross-currency swap generally exchanges cash flows in different currencies over multiple periods and may exchange principal at inception and maturity [1][7]. A firm that issues debt in dollars but earns euros can use a swap to transform dollar principal and coupons into euro obligations. The result can match a long-dated funding profile more closely than repeated short FX swaps. It is still a second contract layered on the original debt: if the swap counterparty fails, the bond remains; if coupon dates, benchmark rates, or principal schedules differ, basis remains.

Valuation combines two interest-rate curves, spot FX, forward FX, cross-currency basis, collateral terms, and counterparty adjustments. A quote that looks cheaper than direct foreign-currency borrowing may compensate the intermediary for balance-sheet capacity or a scarce funding direction [6][13]. Synthesis: the correct comparison is the all-in, stress-tested cash-flow schedule across both the original financing and the swap, not the coupon on either instrument viewed alone.

### Options trade certainty for asymmetric protection

A currency option gives the holder the right, but not the obligation, to exchange currencies at a strike on specified terms. A call on the foreign currency can cap the home-currency cost of a foreign payment while allowing benefit if the foreign currency weakens; a put can place a floor under the home-currency value of a foreign receipt. The buyer pays a premium for this asymmetry. Unlike a forward, the option does not lock both favorable and unfavorable outcomes into a symmetric exchange [1].

The premium depends on spot, strike, time, interest rates, expected volatility, and contract terms. Protection can still be mismatched if the commercial amount, timing, or fixing differs from the option. A collar can reduce upfront premium by purchasing one option and selling another, but the sold leg gives up part of the favorable outcome and can add contingent obligations. Synthesis: options are useful when exposure itself is uncertain or management needs a floor rather than a fixed rate, but an option is not free flexibility; its premium, strike, liquidity, and exercise mechanics must be compared with the loss the firm is actually trying to prevent.

### Dealer intermediation links customer flow, price discovery, and balance-sheet capacity

Customers commonly access the wholesale market through dealers rather than through one public central order book. Dealers quote two-way prices, warehouse some risk, internalize offsetting customer orders, and hedge residual positions in inter-dealer spot, forward, option, and swap markets [2][3]. Electronic platforms can match or stream prices, while prime brokers allow clients to trade with multiple executing dealers under a consolidated credit relationship [2]. These arrangements improve access and netting but concentrate operational, credit, data, and liquidity dependencies.

Dealer capacity is not unlimited. BIS research using tick-level spot and swap data finds liquidity spillovers between the two markets and associates dealer balance-sheet conditions with pricing and depth [13]. Du, Tepper, and Verdelhan find that quarter-end balance-sheet reporting is associated with larger CIP deviations, consistent with regulation and scarce intermediary balance sheet affecting forward prices [6]. Synthesis: a wider forward spread or basis can reflect both customer demand and the marginal cost of dealer capital, funding, collateral, and risk. It should not automatically be interpreted as a directional signal about the currency.

Order flow also connects capital flows and official activity to market prices. Asset purchases, debt issuance, trade settlement, reserve transactions, and hedge adjustments generate buy and sell instructions that dealers must intermediate [1][2]. Central-bank intervention is operationally an FX transaction or set of transactions, even when its policy purpose is macroeconomic. This topic does not judge the macroeconomic effectiveness of intervention; its finance implication is that a large official order can change dealer inventory, spot demand, swap funding, and liquidity at the time it enters the market. Synthesis: the same currency view can have different execution and funding consequences depending on market depth, timing, counterparties, and whether other participants must rebalance simultaneously.

### Currency exposure has several non-equivalent layers

Transaction exposure begins when a firm commits to receive or pay a foreign-currency amount and ends when that amount is settled or otherwise offset. It includes receivables, payables, debt service, dividends, and other contracted monetary items [8][11]. Translation exposure arises when an entity converts foreign operations or balances into a presentation currency for consolidated reporting [8][11]. Economic exposure is broader: currency changes can alter sales volume, local and imported costs, competitors' prices, and the long-run cash-generating capacity of a business even when no current invoice is denominated in the foreign currency [8].

A natural hedge offsets currency cash flows without a derivative. Examples include paying local costs from local revenue, borrowing in the currency of a durable foreign asset, or netting receivables and payables that occur in the same legal entity and time window. Natural offsets can reduce gross trading, but they are valid only when currency, amount, timing, entity, and convertibility align. Revenue in one subsidiary cannot necessarily fund a payment in another during capital controls or legal ring-fencing. Forecast sales may disappear while debt service remains. Synthesis: report gross and net exposure; net only the cash flows that can legally and operationally offset in the stressed state.

A financial hedge can target a narrower exposure than management intends. A three-month forward can fix a known invoice but cannot preserve market share after competitors reprice. A foreign-currency loan can offset the translated net assets of a foreign operation but adds interest, refinancing, and covenant risk. A swap can transform debt service while creating counterparty, collateral, and principal-settlement obligations. An option can protect a floor while leaving premium and basis risk. The correct hedge ratio is therefore exposure-specific rather than a universal percentage [8][10].

### Accounting can change reported timing without changing cash economics

IAS 21 requires an entity to identify its functional currency, initially recognize a foreign-currency transaction using the spot exchange rate at the transaction date, retranslate specified monetary items at the closing rate, and translate foreign operations into a presentation currency under the Standard's rules [11]. Transaction exchange differences can affect profit or loss, while translation of a foreign operation can create components in other comprehensive income under applicable circumstances [11]. These categories describe financial reporting. They do not by themselves identify the cash flow or competitive exposure management should hedge.

IFRS 9 hedge accounting is designed to represent qualifying risk-management relationships in financial statements, but it requires eligible items and instruments, documentation, and an economic relationship that meets the applicable requirements [12]. A hedge can be economically sensible but fail to qualify, creating reported volatility. A qualifying hedge can reduce an accounting mismatch while leaving liquidity, basis, or forecast-volume risk. Synthesis: treasury should choose the economic hedge first, then model accounting effects and documentation before execution; accounting treatment is a constraint and reporting consequence, not proof that the risk has disappeared.

### Settlement and liquidity determine whether the hedge survives the path

For a deliverable FX trade, principal risk begins when the sold currency can no longer be unilaterally cancelled and ends when the purchased currency is received with finality [4]. PvP eliminates the specific risk that one principal is finally paid without the other, but it does not eliminate replacement cost, operational failure, funding delay, or all intraday liquidity needs [4][5]. Pre-settlement netting reduces gross payments but depends on legally enforceable agreements and still leaves net amounts to settle [5]. Collateral reduces replacement-cost exposure but can generate cash calls before the offsetting commercial receipt or asset sale occurs [4].

The 2025 BIS settlement survey classifies a hierarchy of methods: PvP; pre-settlement netting; intragroup settlement; settlement over accounts with timing controls; and gross bilateral settlement [5]. Each method changes the amount or probability of loss, but only PvP makes final payment of one currency conditional on final payment of the other. Synthesis: a complete trade ticket should identify not only rate, amount, and value date, but settlement method, cutoff, payment account, counterparty, collateral terms, failure procedure, and source of contingency liquidity.

## Evidence

### The 2025 turnover survey shows that FX is primarily an OTC funding and hedging system

The BIS Triennial Survey collects dealer-reported transactions across participating jurisdictions, applies defined adjustments for local and cross-border inter-dealer double counting, and reports average daily turnover for a common month [1]. In April 2025, total OTC FX turnover was $9.595 trillion per day: $2.957 trillion spot, $1.847 trillion outright forwards, $3.986 trillion FX swaps, $172 billion currency swaps, and $634 billion options and other products [1]. FX swaps remained the largest category at 42 percent, while spot and outright forwards represented 31 and 19 percent. The dollar appeared on one side of 89.2 percent of trades, and the four largest trading jurisdictions accounted for three quarters of turnover on the survey's net-gross location measure [1].

The method supports market-structure comparisons but has limits. Turnover counts contracted activity during April, not the stock of open positions, gross principal at risk, or realized profit. The survey month followed major trade-policy announcements and elevated volatility, so the level should not be treated as an ordinary-day forecast for every period [1]. Even with those qualifications, the instrument mix rejects the picture of FX as mostly immediate currency exchange. Swaps and forwards together represented more than three fifths of activity, consistent with a market whose core functions include future conversion, hedging, and currency funding [1][2].

The counterparty data also identify intermediation. Reporting dealers traded 46 percent of turnover with other reporting dealers and 50 percent with other financial institutions [1]. BIS analysis of the 2019 survey links activity to bank funding liquidity, portfolio hedging, prime brokerage, and electronic execution [2]. This is evidence about who trades and through which institutional relationships, not about whether each trade is a hedge or speculation; the survey does not observe the complete balance sheet or motive behind every contract [1][2].

### Covered interest parity deviations reveal the price of constrained balance sheets

Du, Tepper, and Verdelhan compare spot, forward, and funding prices across major currencies and construct CIP deviations using several interest-rate measures, including unsecured rates, repo rates, and bonds issued by the same highly rated borrower in different currencies [6]. They document persistent post-crisis deviations and especially large effects for contracts that cross quarter-end reporting dates [6]. The design addresses simple explanations based only on one credit market, and the timing pattern points to bank regulation and balance-sheet management as contributors to the pricing wedge [6].

The finding does not establish a free arbitrage available without capital, collateral, shorting, execution, or counterparty constraints. It shows that the textbook equality must be tested against the actual instruments and institutional balance sheet needed to execute it. BIS spot-and-swap research adds high-frequency evidence that liquidity can spill between the markets and that large-dealer behavior matters for pricing [13]. Together, the studies support a bounded conclusion: forward points and cross-currency basis reflect not only policy-rate differences but also the scarcity and cost of intermediary balance sheet, especially under concentrated funding or reporting pressure [6][13].

### Settlement evidence separates trade volume from principal at risk

The BIS 2025 settlement study used a new classification supplied by reporting dealers in 49 jurisdictions and covered actual settlement of two-way FX payments during April rather than inferring settlement from turnover [5]. More than $14 trillion of gross obligations settled on an average day. PvP handled $5.2 trillion, or 36 percent, and eliminated FX principal risk for those payments. Pre-settlement netting, intragroup settlement, and accounts with timing controls covered much of the remainder, while more than $1.4 trillion, or 10 percent, settled gross bilaterally and remained exposed for full principal [5].

The survey also identifies why risk remained. Of gross bilateral settlement, 25 percent was eligible for PvP despite not using it; among transactions with ineligibility issues, counterparty access, currency coverage, and trade type were material constraints [5]. Gross bilateral risk was more common with other financial institutions and non-financial customers than in external inter-dealer trades [5]. The study measures settlement method rather than expected loss, and gross principal at risk is not the same as a forecast default loss. Its contribution is to show that a small percentage of a very large system remains a large daily exposure and that infrastructure access, not only price choice, determines risk.

The evidence also clarifies what mitigation does not accomplish. PvP prevents one-sided final principal delivery but leaves replacement cost and liquidity risk. Pre-settlement netting compressed about $2.2 trillion of daily obligations to $337 billion in the survey, yet those net amounts still required settlement [5]. The Basel Committee's guidance therefore recommends PvP where practicable, enforceable netting and collateral for replacement-cost risk, and explicit controls for liquidity, operational, legal, and capital consequences [4].

### FX swaps and forwards create debt-like payment obligations outside conventional debt measures

Borio, McCauley, and McGuire combine BIS OTC derivatives statistics with international banking data to estimate dollar payment obligations embedded in FX swaps, forwards, and currency swaps [7]. Using 2022 data, they reported more than $80 trillion of outstanding obligations to pay dollars, much of it short-term, exceeding the combined stocks of dollar Treasury bills, repo, and commercial paper [7]. These are gross payment obligations rather than mark-to-market losses or conventional on-balance-sheet debt. The comparison is intended to reveal rollover and payment scale, not to claim that the whole notional will be lost.

The evidence matters because an FX swap can look hedged in exchange-rate terms while depending on repeated access to dollar funding. If a non-bank owns a long-dated dollar asset and rolls short FX swaps, the asset and hedge may offset at the final economic horizon but the institution must still replace the swap and meet principal on each maturity date [7]. Synthesis: liquidity stress tests should include gross currency payments, maturity concentration, and access to alternative dealers; net market value alone cannot show whether the funding chain survives.

### Corporate studies support exposure-driven hedging but not mechanical full hedging

Allayannis and Ofek study S&P 500 non-financial firms and separate the decision to use currency derivatives from the amount used [9]. Their working-paper and published results find that foreign sales and foreign trade help explain derivative use and that use is associated with significantly lower exchange-rate exposure in the sample [9]. Foreign-currency debt also appears as an alternative hedge for some exposures [9]. The study is observational and based on 1993 firm data, so it does not prove that every derivative causes lower risk or that its estimated relationships are permanent. It does support the narrower proposition that firms tend to connect hedge use and size to identifiable foreign activity rather than selecting instruments independently of exposure.

Froot, Scharfstein, and Stein develop a corporate-finance model in which hedging can add value when external finance is more costly than internally generated funds and volatile internal cash flow can force the firm to forgo attractive investment [10]. Their method is theoretical rather than a randomized test. Its relevant implication is that the target is not minimum earnings volatility for its own sake; the hedge should preserve funds in states where investment and financing constraints make cash most valuable [10]. This explains why a full hedge of every measurable currency line can be wrong if the currency movement also changes operating opportunities, local costs, or financing needs.

Papaioannou's IMF review distinguishes transaction, translation, and economic exposure and compares measurement and management approaches for firms [8]. The categories are analytical rather than perfectly observable: forecast cash flows, pass-through, competitor response, and operational offsets introduce estimation error. Read with IAS 21 and IFRS 9, the evidence establishes that accounting translation, contractual transaction exposure, and economic sensitivity answer different questions [8][11][12]. A program can succeed against one and fail against another.

## Implications

### Corporate treasurers should hedge cash-flow failure, not cosmetic volatility

Synthesis: begin with a currency ledger by legal entity and date. Record committed receivables, payables, debt service, taxes, dividends, capital expenditure, intercompany balances, forecast operating flows, collateral calls, and available cash in each currency. Tag each item by certainty, cancellation terms, accounting treatment, and the business consequence if the currency moves. This implements the exposure distinctions in the corporate and accounting sources while preventing forecast revenue from being netted mechanically against fixed debt [8][11][12].

For a certain invoice, an outright forward can lock a home-currency amount with relatively little payoff complexity. For an uncertain bid or forecast, an option may prevent the hedge from becoming an equal-sized speculative position if the transaction does not occur, although the premium and strike must be justified. When foreign currency is needed today and reversed later, an FX swap addresses funding and conversion together. For a long-dated foreign-currency debt stream, a cross-currency swap or matched foreign-currency revenue may align principal and coupons more closely than repeated short swaps [1][7]. Synthesis: instrument choice should minimize mismatch across currency, amount, date, payoff, entity, settlement, and collateral, not merely obtain the narrowest quoted spread.

A policy should distinguish hedge layers. The first layer nets legally and operationally compatible cash flows. The second protects committed transactions. The third covers highly probable forecasts within limits based on forecast error. The fourth addresses structural net investment or financing mismatches. The fifth, if authorized, contains any directional currency position in a separate risk budget. This separation follows the evidence that complete position context determines whether a derivative is hedging and limits the ability to relabel an unsuccessful view after the result is known [8][9][10].

The single worst outcome is a hedge that prevents an exchange-rate loss at maturity but forces the firm into a liquidity failure first. Prevent it by projecting margin, collateral, option premium, principal settlement, and roll payments under joint shocks. Include a home-currency fall that creates derivative losses while foreign assets rise in reporting currency; a cancelled sale that leaves a forward uncovered; basis widening at a roll date; counterparty failure; and delayed commercial receipts [4][5][7]. The response may be more liquidity, longer maturities, staged rolls, additional counterparties, options, or a lower hedge ratio. None is free; each changes another risk.

### Finance teams should reconcile economic, cash, and accounting views

Synthesis: maintain three linked but separate reports. The economic report estimates how currency changes affect future margins, competitive position, and enterprise cash generation. The cash report shows contractual receipts, payments, collateral, and settlement by date. The accounting report applies functional-currency, translation, derivative, and hedge-accounting rules [11][12]. Differences are expected. A translation adjustment can arise without near-term cash, while a collateral call can consume cash before the hedged forecast affects earnings.

Hedge accounting should be evaluated before execution because designation, documentation, eligible instruments, timing, and effectiveness affect reported results [12]. It should not dictate an economically inferior hedge solely to reduce income-statement volatility. Conversely, ignoring accounting can make a sound program difficult to explain and can create avoidable volatility or control failures. Synthesis: approval should state the economic objective first, the expected accounting second, and the conditions under which either relationship stops being valid.

Performance attribution should decompose spot movement, forward carry, cross-currency basis, bid-offer and fees, option premium and volatility, hedge payoff, underlying cash-flow change, collateral funding, and forecast error [6][8]. Calling the entire forward discount a fee confuses the matched interest-rate relationship with execution cost. Calling every derivative loss a failed hedge ignores the offsetting gain in the underlying exposure. The combined position must be judged against the declared cash-flow or balance-sheet objective.

### Banks and dealers should treat capacity, conduct, and settlement as one service

Dealers intermediate customer risk through inventory, internalization, inter-dealer hedges, prime brokerage, collateral, and settlement networks [2][3][13]. Synthesis: risk limits should therefore combine market sensitivity with gross principal, potential future exposure, settlement method, intraday liquidity, maturity concentration, and wrong-way counterparty risk. A delta-neutral book can still create large same-day payments or replacement costs. A profitable client franchise can still be fragile if several clients require the same currency during a funding shock.

The FX Global Code makes transparency and fair execution part of market integrity but does not replace binding regulation [3]. Synthesis: clients should understand whether the dealer acts as principal or agent, how orders may be handled, what information may be used, which venues may receive the order, and how conflicts are controlled. Dealers should link this execution disclosure to confirmation and settlement procedures, because an attractive fill that cannot be confirmed or safely settled is not a complete service.

Quarter-end and stress behavior deserve explicit capacity plans. Evidence that CIP deviations widen around reporting dates and that spot and swap liquidity interact means ordinary-volume assumptions can fail precisely when hedge demand is one-sided [6][13]. Synthesis: dealers and clients should stagger large rolls where possible, pre-agree credit and collateral capacity, monitor basis and depth rather than only spot volatility, and identify fallback execution and settlement routes before the value date.

### Boards, lenders, and investors should ask what moved and what can demand cash

A derivative notional is a reference amount, not current value or expected loss, but the BIS evidence shows why it cannot be dismissed: full principal may have to be delivered, often at short maturities [7]. Synthesis: analysis should show notional by currency and maturity, mark-to-market value, netting set, collateral, settlement method, roll requirement, counterparty concentration, and the underlying exposure being offset. If management cannot connect a derivative to these fields, the label "hedge" carries little evidential value.

For non-financial firms, review foreign revenue and cost currencies, invoice currencies, debt denomination, hedge notionals, derivative maturities, sensitivity disclosures, translation reserves, and cash-flow hedge reserves [8][11][12]. Compare the change in derivative value with the underlying item and with cash movements. A large derivative gain may signal a larger operating loss; a reported translation loss may not create immediate cash need; a small net fair value may coexist with large gross settlement and rollover obligations.

Credit analysis should test whether the hedge works when the borrower is weakest. A foreign-currency loan may hedge a foreign asset under normal conditions but become dangerous if local revenue falls, controls trap cash, or the asset cannot be sold. A forward may protect an invoice yet require collateral when liquidity is scarce. A swap may reduce currency mismatch but create a concentrated maturity wall [4][7]. Synthesis: treat hedge value as conditional on counterparty performance, legal netting, continued market access, and the survival of the underlying exposure.

### Regulators and infrastructure providers should target the residual settlement gap

The 2025 settlement evidence provides a hierarchy for intervention. PvP eliminated principal risk for 36 percent of average daily settlement, other methods mitigated but did not eliminate risk for 54 percent, and $1.4 trillion per day remained gross bilateral [5]. The reasons include lack of counterparty access, ineligible currencies, ineligible trade types, cutoff constraints, and operational failure [5]. Synthesis: the most direct gains come from moving eligible trades into existing PvP, expanding indirect access, increasing currency and same-day coverage where legal and operational foundations permit, and using enforceable pre-settlement netting when PvP is not practicable.

Risk reduction should not be measured only by a lower gross-bilateral share. PvP can concentrate intraday liquidity needs; netting can depend on enforceability; longer operating hours can transfer staffing and nostro demands; and broader access can introduce participants with weaker operations [4][5]. Synthesis: infrastructure changes should be tested for principal risk, replacement cost, liquidity, operational resilience, and failure recovery together. The objective is not to move the same vulnerability into a less visible part of the payment chain.

Central banks also enter FX markets as reserve managers, liquidity providers, and policy authorities [1][2]. This topic does not prescribe intervention policy. Its operational implication is that authorities should understand how intervention routes through dealers, collateral, value dates, and payment systems, and how emergency currency liquidity interacts with private swap markets. The Herstatt history and modern settlement data show that confidence can be lost through payment uncertainty even when the original shock was a market or policy event [4][5].

### A practical FX decision test

Synthesis: a defensible FX decision can be tested in ten steps. First, state the functional, reporting, and payment currencies. Second, list gross contractual and forecast cash flows by date and legal entity. Third, distinguish transaction, translation, economic, and funding exposure. Fourth, identify valid natural offsets. Fifth, define the unacceptable outcome: cash shortfall, margin breach, covenant failure, earnings volatility, or loss of strategic investment capacity. Sixth, compare spot, forward, swap, option, cross-currency swap, and no-action cash flows under consistent quotations. Seventh, separate interest differential, basis, spread, premium, and collateral funding. Eighth, map counterparty, netting, settlement, and rollover. Ninth, document accounting and governance. Tenth, stress the combined exposure and name the conditions that trigger resize, closure, or escalation [4][5][6][8][10][11][12].

The framework's conclusion is deliberately conditional. Use a forward when amount and date are firm and symmetric locking serves the cash objective. Use a swap when temporary currency funding and reversal are both required. Use an option when exposure or desired protection is asymmetric. Use a cross-currency swap when a longer stream must be transformed and its complexity is supportable. Use natural offsets only when they remain available in stress. Leave exposure open only as an explicit, measured choice. Every choice should be evaluated as a package of price, funding, liquidity, counterparty, settlement, accounting, and rollover consequences rather than as a promise that currency risk has vanished [4][7][8].

## Sources

1. Bank for International Settlements. (2025). "OTC Foreign Exchange
   Turnover in April 2025." Triennial Central Bank Survey, September.
   https://www.bis.org/statistics/rpfx25_fx.pdf [high]

2. Packer, F., Schrimpf, A., and Sushko, V. (2019). "Sizing Up Global
   Foreign Exchange Markets." BIS Quarterly Review, December.
   https://www.bis.org/publ/qtrpdf/r_qt1912f.htm [high]

3. Global Foreign Exchange Committee. (2024). "FX Global Code," updated
   December 2024.
   https://www.globalfxc.org/fx_global_code.htm [high]

4. Basel Committee on Banking Supervision. (2013). "Supervisory Guidance
   for Managing Risks Associated with the Settlement of Foreign Exchange
   Transactions."
   https://www.bis.org/publ/bcbs241.htm [high]

5. Drehmann, M., McGuire, P., Shirakami, T., Conway, M., and Lovell, N.
   (2026). "Uncovering FX Settlement Risk: New Measures from the 2025 BIS
   Triennial Survey." BIS Quarterly Review, June.
   https://www.bis.org/publications/uncovering-fx-settlement-risk-new-measures-2025-bis-triennial-survey [high]

6. Du, W., Tepper, A., and Verdelhan, A. (2018). "Deviations from Covered
   Interest Rate Parity." Journal of Finance, 73(3), 915-957.
   Public working-paper version: https://www.nber.org/papers/w23170 [high]

7. Borio, C., McCauley, R. N., and McGuire, P. (2022). "Dollar Debt in FX
   Swaps and Forwards: Huge, Missing and Growing." BIS Quarterly Review,
   December.
   https://www.bis.org/publ/qtrpdf/r_qt2212h.htm [high]

8. Papaioannou, M. G. (2006). "Exchange Rate Risk Measurement and
   Management: Issues and Approaches for Firms." IMF Working Paper 06/255.
   https://www.imf.org/external/pubs/ft/wp/2006/wp06255.pdf [high]

9. Allayannis, G., and Ofek, E. (2001). "Exchange Rate Exposure, Hedging,
   and the Use of Foreign Currency Derivatives." Journal of International
   Money and Finance, 20(2), 273-296.
   Public working-paper version: https://archive.nyu.edu/handle/2451/26842 [high]

10. Froot, K. A., Scharfstein, D. S., and Stein, J. C. (1993). "Risk
    Management: Coordinating Corporate Investment and Financing Policies."
    Journal of Finance, 48(5), 1629-1658.
    Public working-paper version: https://www.nber.org/papers/w4084 [high]

11. IFRS Foundation. (2026). "IAS 21: The Effects of Changes in Foreign
    Exchange Rates."
    https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias21.html [high]

12. IFRS Foundation. "IFRS 9: Financial Instruments," including hedge
    accounting requirements and current standard history.
    https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/ [high]

13. Krohn, I., and Sushko, V. (2021). "FX Spot and Swap Market Liquidity
    Spillovers." BIS Working Papers No. 836, revised June.
    https://www.bis.org/publ/work836.pdf [high]

## See Also

- `library/finance/derivatives-and-risk-transfer.md` -- the general payoff,
  valuation, counterparty, collateral, and clearing mechanics of forwards,
  futures, swaps, and options.
- `library/finance/financial-market-microstructure.md` -- how dealers, order
  handling, venue design, liquidity, clearing, and settlement shape executable
  prices.
- `library/macro-micro/currency-and-exchange-rates.md` -- macroeconomic parity,
  exchange-rate regimes, policy transmission, crises, and dominant currencies.
- `library/portfolio-risk-management/currency-hedging-in-global-portfolios.md`
  -- portfolio hedge ratios, asset-currency covariance, collateral, and global
  asset-allocation policy.
