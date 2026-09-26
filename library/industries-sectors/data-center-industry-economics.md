---
name: data-center-industry-economics
id: 20260926T070653Z
tier: library-topic
domain: industries-sectors
author: Librarian
tags: [data-centers, industry-economics, artificial-intelligence, colocation, power-capacity, capital-cycle, profit-pools]
links: [library/industries-sectors/capital-cycle-analysis.md, library/industries-sectors/industry-profit-pools.md, library/industries-sectors/semiconductor-industry-structure-and-economics.md, library/technology/cloud-computing.md, library/engineering-infrastructure/telecommunications-physical-infrastructure.md]
---

# Data Center Industry Economics -- Power Rights and Utilization Determine Returns Before Compute Demand Does

Data centers turn demand for computing into a location-bound business built from power, land, connectivity, equipment, and long-lived capital. AI is increasing prospective demand, but industry returns depend first on whether an operator can secure deliverable power, contract customers, fill capacity, and recover both operating cost and continuing investment without accepting excessive concentration or financing risk [1][6][7].

## Background

A data center is economically different from the computing service that runs inside it. The facility supplies a controlled place for information technology equipment, together with electrical capacity, cooling, physical security, and network access; the servers may belong to the facility owner, a cloud provider, an enterprise, or a tenant [3][6][7]. This distinction defines the industry boundary. Cloud software architecture, semiconductor design, and the engineering details of power and cooling matter as inputs, but data center industry analysis asks who owns capacity, who bears utilization and construction risk, how contracts divide costs, and which scarce links capture profit.

The sector developed from enterprise facilities toward larger shared and hyperscale estates. Masanet and coauthors estimated that global compute instances rose by roughly 550 percent between 2010 and 2018 while total data center electricity use rose by about 6 percent, because server efficiency, virtualization, and migration toward large cloud and hyperscale sites sharply improved resource use [5]. The historical lesson is not that demand stops growing. It is that workload growth, physical capacity growth, and electricity growth can follow different paths when equipment performance and utilization change.

Three operating models now coexist. An enterprise-owned facility is built or controlled for one organization's internal workloads; the owner retains capital, occupancy, technology, and operating risk. A hyperscaler integrates large facilities with its own cloud or digital platform and earns revenue primarily from services above the building. A colocation provider sells space, power, and connectivity to outside customers. Retail colocation serves deployments from cabinets through smaller suites, while wholesale or hyperscale colocation supplies dedicated halls or multi-megawatt capacity under longer contracts [6][7]. Digital Realty reported general contract lengths of two to five years for deployments up to one megawatt and five to ten years or more for larger deployments [7]. Equinix described fixed-duration infrastructure contracts billed according to space and power that generate monthly recurring revenue [6].

AI intensified the demand cycle by increasing both investment and power density. The International Energy Agency reported that capital expenditure by five large technology companies exceeded $400 billion in 2025, that global data center electricity demand grew 17 percent that year, and that electricity use by AI-focused centers grew 50 percent [1]. The IEA nevertheless treats the outlook as uncertain because efficiency, adoption, model capability, grid connections, chip supply, equipment supply, capital, permitting, and social acceptance are changing at different speeds [1]. Announced projects therefore measure ambition, not completed and economically utilized supply.

The physical bottleneck has shifted toward deliverable power. A prospective site is not valuable merely because it has land or a utility line nearby. It needs a credible quantity of electricity, a connection date, transmission and distribution capability, equipment, permits, fiber routes, and a customer configuration that can use the delivered capacity [1][3][9]. The US Department of Energy's advisory group reported connection requests for individual hyperscale facilities of 300 to 1,000 megawatts or more, with requested lead times of one to three years that stretched local grids' ability to respond [3]. The IEA separately identified a mismatch between fast data center development and slower energy investment [1].

The business is therefore both industrial and financial. Developers commit capital before all demand is visible, lease or own long-lived sites, fund construction with operating cash, debt, equity, and joint ventures, and then recover investment through recurring contracts [6][7]. Power and network density can create location-specific scarcity, while standardized construction and purchasing can create scale economies [7]. The same fixed-cost structure creates downside: an empty or underpowered building still incurs financing, depreciation, maintenance, taxes, and staffing costs, while capacity designed for yesterday's rack density may not serve tomorrow's demand without more investment [6][7].

The author's synthesis is that a data center is best understood as a portfolio of time-bound capacity rights rather than as generic real estate. Land, grid access, electrical and cooling capability, network access, permits, and customer commitments mature on different schedules. Economic value appears only when those rights converge into capacity that can be delivered, billed, and renewed at returns above the full cost of capital.

## Core Concepts

### Business models allocate ownership and demand risk

Enterprise, hyperscale, retail colocation, and wholesale colocation models allocate the same underlying risks differently. An enterprise facility gives its owner direct control and can fit specialized operational or regulatory needs, but the enterprise must forecast future load, finance the entire build, and absorb unused capacity. Uptime Institute's 2025 survey continued to find on-premises facilities central to hybrid information technology strategies, showing that enterprise ownership has not disappeared even as outsourcing has expanded [10]. The economic test is not whether ownership is modern or old-fashioned; it is whether the organization can use enough of the facility, for long enough, to justify the capital and operational specialization.

A hyperscaler combines the facility with a higher-layer service business. The building is an input into cloud, advertising, commerce, social media, or AI products, so the return on the facility may not be visible as stand-alone rent. Scale supports custom design, standardized procurement, broad workload pooling, and high equipment utilization, but it also exposes the owner to a very large, continuing capital program [1][5]. A hyperscaler can self-build when demand is predictable and time permits, lease from wholesale providers to accelerate deployment or enter constrained markets, and combine both routes across regions.

A colocation operator converts shared infrastructure into contracted capacity. Retail colocation can diversify customers and earn additional interconnection revenue because many networks, clouds, enterprises, and service providers occupy the same campus. Equinix describes its IBX facilities as carrier-neutral, multi-tenant sites and its xScale facilities as hyperscale-oriented capacity developed through joint ventures [6]. Wholesale colocation trades some diversification and interconnection intensity for larger commitments, longer terms, and a potentially faster path to filling a building. Digital Realty's portfolio spans deployments from one cabinet to multi-megawatt halls, illustrating how one operator can hold several risk profiles within the same platform [7].

The models are complements as well as competitors. A hyperscaler may own core capacity, lease surge or market-entry capacity, and place network-heavy nodes in carrier-dense colocation sites. An enterprise may retain selected facilities while moving other workloads to colocation or cloud. The author's synthesis is that build-versus-lease is an option-allocation decision: ownership can lower long-run unit cost at stable scale, while leasing transfers construction timing and partial utilization risk to a specialist in exchange for rent and contractual dependence.

### The economic unit is deliverable, sellable power

Floor area is an incomplete capacity measure because racks require different power densities and because electrical, cooling, and network limits may bind before a room is physically full. Industry disclosures therefore increasingly describe capacity in megawatts, cabinets, leased percentage, or combinations of these measures [6][7][9]. Each denominator answers a different question. Planned megawatts measure a development ambition; utility-awarded megawatts measure a right with conditions; energized megawatts measure physical availability; sellable megawatts reflect facility configuration; contracted megawatts reflect customer commitments; and utilized megawatts reflect actual load.

Confusing these stages creates false precision. A signed lease can precede delivery by months or years. A completed shell can await electrical equipment or a grid connection. A tenant can reserve more power than it initially draws. A billed cabinet can be constrained by total site power, while spare floor space remains unusable for a dense deployment. Equinix defines cabinet utilization as billed cabinet space divided by total cabinet capacity while taking power limitations into account; at year-end 2025 it reported regional utilization of 73 to 79 percent for the consolidated IBX portfolio [6]. Digital Realty reported its portfolio, including unconsolidated entities, as approximately 84.7 percent leased at the same date [7]. These figures are company-specific and not directly comparable, but both show why the denominator must accompany a utilization claim.

Utilization creates operating leverage because many facility costs are committed before the final customer arrives. Construction, utility infrastructure, property cost, baseline staffing, security, and much maintenance do not vary proportionately with near-term load [6][7]. Lease-up can therefore improve unit economics materially, while slow absorption can leave capital earning below its hurdle rate. The strongest development model links construction phases to credible demand and preserves the ability to stop, resize, or repurpose later phases.

Power usage effectiveness, or PUE, measures total facility energy divided by energy delivered to information technology equipment [2][10][11]. It helps identify facility overhead, but it does not measure useful computation, revenue, utilization, carbon intensity, water use, or return on capital. Google reported a 2025 fleet-wide PUE of 1.09 for stabilized large-scale centers, while Uptime's 2025 survey reported a respondent average of 1.54 [10][11]. The figures demonstrate operating dispersion, not a universal cost advantage, because fleets, climates, workloads, measurement boundaries, and maturity differ.

### Contracts redistribute construction, power, and volume risk

Contracts are the bridge between physical capacity and finance. The provider may charge for reserved power, used power, floor area, cabinets, cross-connects, installation, managed services, or combinations of these items [6][7]. Fixed-duration recurring revenue can stabilize cash flow, but the economics depend on escalation clauses, renewal rights, service-level obligations, power pass-throughs, minimum commitments, credit quality, and the timing between signing and commencement.

Retail contracts tend to diversify revenue across customers and products. Interconnection can add a service with low physical footprint and high customer relevance where a dense ecosystem already exists [6][7]. Larger wholesale contracts can finance substantial capacity with fewer sales, but they increase customer concentration and renewal exposure. Digital Realty disclosed that its 20 largest customers represented about 51 percent of portfolio annualized recurring revenue at year-end 2025 and that the top three represented about 26 percent [7]. No single customer exceeded approximately 11.7 percent, but a diversified customer count did not eliminate concentration among the largest buyers [7].

Power pricing terms determine who bears utility volatility. Digital Realty states that it negotiates operating-expense pass-through provisions, including power costs and certain capital expenditure [7]. Such clauses can protect nominal margins, but they do not remove demand risk: a customer still evaluates its total delivered cost, and high power prices can weaken the attractiveness of a location. Service-level commitments transfer reliability risk back to the operator through credits, damages, termination rights, and reputation exposure [7].

Preleasing transfers part of volume risk before construction finishes. CBRE reported that 74.3 percent of capacity under construction in major North American markets was committed in the first half of 2025 [9]. This supported financing and reduced initial vacancy risk, but it also showed customers competing for future rather than current supply. The author's synthesis is that a backlog must be graded by counterparty, cancellation terms, commencement conditions, pricing, pass-throughs, and remaining construction obligations; a signed megawatt is not automatically an earned return.

### Location is a bundle of bottlenecks and network effects

Data centers cluster because location affects electricity, fiber, latency, customer access, land, construction, taxes, permitting, regulation, and workforce [4][8]. Northern Virginia illustrates cumulative advantage: JLARC identified fiber, reliable and comparatively inexpensive energy, available land, proximity to major customers, and tax incentives as contributors to the region's scale [4]. Once networks and customers cluster, additional participants can value proximity because direct connections reduce latency and operational complexity [6][7].

Clustering also concentrates constraints. A region can have abundant prospective demand but insufficient near-term generation, substations, transmission, transformers, switchgear, or public acceptance [1][3][4]. CBRE reported that power availability and infrastructure delivery timelines were decisive site-selection factors across major US markets in the first half of 2025, while constrained supply supported low vacancy, preleasing, and higher pricing [9]. Scarcity shifts bargaining power toward holders of deliverable power, but only while customers cannot obtain adequate substitutes elsewhere.

Network density can create a separate moat from power capacity. A carrier-rich facility lets tenants connect to multiple networks, cloud on-ramps, exchanges, and counterparties without rebuilding external routes [6][7]. This can support switching costs and interconnection revenue even when basic space becomes more available. By contrast, a remote AI training campus may place greater value on large power blocks and construction speed than on a dense local customer ecosystem. The industry's profit pools therefore differ by workload and location rather than following one universal ranking.

### Capital intensity creates barriers and a financing cycle

A data center project commits capital across land, site work, utility connections, buildings, electrical and cooling systems, network access, equipment procurement, and tenant fit-out [6][7]. Some assets have long physical lives, but technology and power-density requirements can shorten their economic usefulness. Equinix warned that high-density equipment can prevent full use of older facilities whose designed electrical capacity is lower than current demand [6]. Depreciation is noncash in a given period, yet it reflects that invested assets are consumed or become obsolete; ignoring both depreciation and required replacement capital can overstate economic profit.

Funding structure changes who bears the cycle. Public operators use retained cash, debt, equity, leases, asset sales, and joint ventures [6][7]. Joint ventures can bring outside capital and isolate large hyperscale projects, but they also divide control and economics. REIT structures can provide access to real-estate capital while imposing distribution and qualification constraints [6][7]. Debt can lower the initial equity requirement, but fixed interest and refinancing needs amplify slow lease-up, construction delay, or a fall in asset values.

The relevant hurdle is return on incremental capital after sustaining investment, not growth in megawatts alone. Digital Realty explicitly frames development around positive spreads over its cost of capital and reports a balance-sheet strategy designed to preserve funding flexibility [7]. The author's synthesis is that cheap capital can become a competitive advantage when projects are disciplined, but it can also accelerate industry overbuilding when financing rewards announced capacity before demand, connection, and construction risks are resolved.

### AI demand collides with a delayed supply response

AI changes facility requirements through accelerated hardware, higher rack density, large power blocks, and uncertain training and inference patterns [1][2][3]. The IEA projects global data center electricity use to rise from about 485 TWh in 2025 to about 950 TWh in 2030, while AI-focused demand grows faster than the total [1]. LBNL's 2025 US update likewise reports a wide 2030 range because shipments, accelerator lives, idle power, utilization, facility mix, and PUE remain uncertain [2]. These are scenarios, not contracted revenue forecasts.

Supply responds with delay. Grid studies, permits, equipment, construction, commissioning, and customer installation take time [1][3][9]. When scarcity raises rents and compresses vacancy, many operators may expand simultaneously. Capacity can then arrive after efficiency improves, demand shifts by location, customers self-build, financing costs rise, or projected AI workloads fail to appear. The mechanism is the capital cycle: high expected returns attract supply, delayed projects cluster in time, and the later utilization outcome determines whether scarcity rents persist.

Efficiency complicates the cycle rather than canceling it. Masanet and coauthors documented how efficiency and consolidation restrained energy growth during the 2010s [5]. Google reports that its data centers delivered more than three times as much compute performance per unit of energy in 2025 as five years earlier [11]. LBNL nevertheless concludes that expected growth in computation can more than offset hardware efficiency, causing absolute electricity use to rise [2]. The author's synthesis is that investors must model both effects: efficiency lowers energy per task and may delay some builds, while lower task cost and new capabilities can expand total use.

### Profit follows the binding constraint, not the largest spending line

The value chain includes chips, servers, networking, electrical equipment, construction, utilities, data center owners, interconnection services, cloud platforms, software, and end users. Revenue and profit need not concentrate in the same link. A building owner can face high capital requirements and customer bargaining power even during a compute boom, while a scarce chip, grid connection, network ecosystem, or cloud service captures more of the incremental value [1][6][7].

The author's synthesis is that the binding constraint determines near-term bargaining power. When grid-ready sites are scarce, holders of secured power and permits can obtain better terms. When facilities are plentiful but accelerators are scarce, chip and system suppliers capture more. When capacity and hardware are available but customer demand is concentrated, hyperscalers can demand owner-like economics from lessors. When a carrier-dense ecosystem is difficult to reproduce, interconnection can remain valuable despite wider building supply.

This allocation is dynamic. A power reservation can lose value if it cannot be energized; a remote site can lose pricing power if customers need latency or network density; a dense urban site can lose relevance for a workload optimized for large low-cost campuses. The durable advantage is not ownership of one input in isolation but control of a hard-to-reproduce combination that customers need and competitors cannot deliver on the same schedule.

## Evidence

### Efficiency and consolidation changed the historical energy relationship

Masanet and coauthors combined bottom-up estimates and newer equipment, server, storage, network, and facility-efficiency data to reassess global data center energy use between 2010 and 2018 [5]. They estimated that compute instances increased roughly sixfold while global data center electricity use moved from about 194 TWh to about 205 TWh. Their explanation included more efficient servers, lower idle power, virtualization that hosted more compute instances per server, migration to large cloud and hyperscale sites, storage efficiency, and lower PUE [5].

The finding rejects a simple one-for-one link between digital activity and energy use. Its limitation is temporal: the study predates the current accelerated-computing buildout, and the authors explicitly treated continued efficiency as a policy and technology challenge rather than a permanent guarantee [5]. The appropriate inference is that efficiency can materially change capacity demand, not that AI demand will have no physical consequences.

### Bottom-up US scenarios show that utilization assumptions dominate the range

The LBNL 2025 Update uses a bottom-up model based on projected equipment shipments, per-device annual electricity use, cooling-performance simulations, facility types, and locations [2]. It estimates that data centers could account for 11.8 percent of US electricity in 2030 in its reference case, with a compounded uncertainty range of 9.5 to 15.3 percent [2]. Sensitivities include accelerator shipments and lifetime, idle power, training and inference utilization, and PUE [2].

This method is useful because it begins with equipment capable of consuming power rather than summing every announced real-estate project. It can still be wrong if shipments, deployment, retirement, operating behavior, or facility efficiency differ from assumptions. For industry analysis, the range demonstrates that utilization is not a detail: small differences in how intensively a large accelerator base runs can alter electricity demand, utility needs, and the amount of economically useful facility capacity.

### The IEA tracks a demand surge alongside physical bottlenecks

The IEA's 2026 update combines market analysis with satellite-based tracking of AI-focused facility development [1]. It reported that AI-factory capacity had more than tripled in 18 months, global data center electricity demand grew 17 percent in 2025, and AI-focused consumption grew 50 percent [1]. Its central projection roughly doubles total data center electricity use between 2025 and 2030, but the report lowers the plausibility of the most aggressive near-term cases because electricity, grid connections, manufacturing capacity, chips, capital, permitting, and community acceptance are bottlenecks [1].

This evidence supports both sides of the industry thesis. Demand is not hypothetical, yet a large pipeline cannot be translated directly into delivered capacity or profit. The IEA also finds that efficiency per AI task is improving rapidly while more intensive use cases proliferate [1]. The interaction makes a single exponential extrapolation analytically weak.

### Public operator filings reveal different capacity products and risk profiles

Equinix's 2025 Form 10-K identifies two distinct products: multi-tenant IBX centers built around colocation and interconnection, and xScale centers aimed at a targeted group of hyperscalers through joint-venture structures [6]. Infrastructure contracts are typically based on space and power, have fixed duration, and generate monthly recurring revenue [6]. The company reported 392,300 total cabinets and 299,300 billed cabinets across its consolidated IBX portfolio at year-end 2025, with regional cabinet utilization between 73 and 79 percent after considering power limits [6].

Digital Realty's 2025 Form 10-K describes a portfolio from cabinets through multi-megawatt deployments, with general terms of two to five years for smaller deployments and five to ten years or more for larger ones [7]. It reported approximately 84.7 percent of its portfolio leased, about 770 MW under construction, and more than 5 GW of future development capacity at year-end 2025 [7]. It also disclosed material customer concentration and stated that operating agreements can pass through power and some capital costs [7].

These filings are primary company disclosures, not controlled comparisons. Product definitions, consolidation, capacity measures, and accounting differ, so the metrics should not be ranked without reconciliation. Their value is in showing the actual economic levers: billed versus available capacity, contract duration, customer concentration, development pipeline, power costs, recurring revenue, joint ventures, and capital structure.

### Market evidence shows scarcity can persist despite rapid construction

CBRE's first-half 2025 survey of primary North American wholesale markets reported 8,155 MW of supply, up 43.4 percent year over year, while vacancy fell to 1.6 percent and 74.3 percent of under-construction capacity was already committed [9]. It also reported higher pricing for large requirements in constrained markets and identified power availability and delivery timelines as decisive site-selection factors [9]. The method is a commercial real-estate market survey, and its coverage does not represent every enterprise or hyperscale-owned facility.

The case demonstrates that rapid supply growth and tightening availability can coexist when demand grows faster and customers prelease future capacity. It does not prove permanent shortage. High preleasing can encourage more construction, and a market measured during exceptional demand may not describe the stabilized economics of projects delivered several years later.

### Virginia shows both agglomeration benefits and stranded-cost risk

Virginia's Joint Legislative Audit and Review Commission used interviews, state and utility data, economic-impact modeling, and commissioned grid modeling to examine the country's largest data center cluster [4]. It attributed Northern Virginia's position to a combination of fiber, power, land, customers, incentives, and an established ecosystem [4]. The same concentration created very large prospective generation and transmission needs and raised the risk that utilities could build infrastructure for demand that arrives late, arrives elsewhere, or does not materialize [4].

The regional case clarifies why connection rights and cost allocation affect industry economics. If developers fund more network upgrades or accept minimum commitments, they absorb more forecast risk. If utilities socialize those costs, other customers may bear more of the downside. JLARC found that existing Virginia rates generally allocated current costs appropriately while still identifying future stranded-investment risk from the scale and uncertainty of load growth [4]. The finding is jurisdiction-specific, but the underlying contracting problem applies wherever one customer class requests unusually large and fast load additions.

## Implications

### For investors: underwrite capacity conversion, not AI headlines

An industry model should begin with a capacity bridge. Start with land under control, then separate requested power, awarded power, funded utility work, expected energization, facility construction, sellable capacity, signed leases, commenced billing, and actual load. Apply probabilities and dates to every stage. Do not count the same megawatt in a developer pipeline, a tenant commitment, and a utility forecast as three independent demand observations [1][2][7].

The revenue model should distinguish retail colocation, wholesale capacity, interconnection, managed services, utility pass-throughs, and nonrecurring installation work [6][7]. Each stream has different margin, churn, capital, and concentration characteristics. Reported recurring revenue is valuable, but the investor must inspect contract duration, renewal exposure, escalation, cancellation, credit support, service-level liability, and power-price treatment. A long contract with an investment-grade customer can reduce volume risk; it can also cap upside or lock the operator into technology and cost obligations.

Utilization needs several denominators. Track leased percentage, billed cabinets or megawatts, actual load, and facility PUE separately [2][6][7][10]. High lease percentage with low load can still create power-reservation and commencement risk. High PUE indicates facility overhead, but a low PUE does not prove high server utilization or attractive return on capital. The economic measure is cash generated per unit of total capital after power, operating cost, tenant improvements, maintenance, replacement, and financing.

Capital expenditure should be split into land and power access, shell and core, electrical and cooling plant, customer fit-out, expansion, and recurring maintenance. Depreciation should not be dismissed merely because analysts use funds-from-operations measures for REITs. Some initial construction is long-lived, but density upgrades, electrical equipment, cooling systems, and customer configurations can require fresh capital before the building reaches the end of its physical life [6][7]. Compare cash return with both accounting depreciation and a reasoned sustaining-capital estimate.

Customer concentration can change bargaining power. A wholesale operator may fill a campus efficiently with a few hyperscalers, but those customers understand owner economics and can self-build or solicit competing markets. Digital Realty's disclosure that its top 20 customers produced about half of portfolio annualized recurring revenue illustrates why a large total customer count is not enough [7]. Evaluate revenue concentration, leased megawatts, renewal dates, and customer capital plans together.

Financing deserves a through-cycle test. Model construction delay, slower lease-up, lower renewal rent, higher interest, utility deposits, and required equity at the same time. Joint ventures can reduce balance-sheet capital but may also share the best project economics and constrain decisions [6][7]. A sound downside case asks whether the operator can finish committed projects and service debt without assuming that capital markets remain open on favorable terms.

The author's investment synthesis is a five-part dashboard: deliverable power, contracted and actual utilization, return after sustaining capital, customer and geographic concentration, and funding runway. AI demand improves the opportunity set, but only this conversion chain determines whether a developer creates economic profit or merely constructs expensive capacity.

### For operators and customers: buy optionality where uncertainty is highest

Operators should phase projects around the slowest irreversible commitment. Land options, modular buildings, staged electrical infrastructure, and customer-backed expansion can preserve upside while limiting stranded capital. The worst outcome is a fully committed campus that cannot be energized on time or cannot support the density customers require. That outcome is prevented by treating the utility schedule, equipment procurement, and customer acceptance conditions as core commercial milestones rather than as engineering details [1][3][6].

Contract design should assign each risk to the party best able to manage it. Operators control facility delivery and reliability; utilities control portions of the connection process; customers control workload ramp and equipment choice. Minimum payments, phased commencements, power pass-throughs, cancellation payments, performance credits, and upgrade provisions should make those responsibilities explicit [6][7]. A contract that hides uncertainty does not eliminate it; it converts uncertainty into later dispute or margin volatility.

Customers should compare ownership and colocation on matched assumptions. Include utilization, financing, land, grid delay, staff, resilience, network access, taxes, maintenance, refresh, and exit cost. Large stable workloads may support ownership economics, while uncertain or geographically distributed demand can make leased capacity valuable as an option. Network-dense colocation can command a premium when counterparties and carriers matter; a remote power-rich campus can be superior for workloads that tolerate location flexibility.

Both sides should test density and retrofit paths. AI hardware can increase power per rack faster than an older site's electrical design can accommodate [1][6]. Reserving nominal floor area without a credible power and cooling path can strand both tenant and provider. Conversely, designing every hall for the most extreme forecast density can overcapitalize capacity that serves conventional workloads for years. A portfolio approach can segment high-density and conventional capacity rather than force one expensive specification everywhere [10].

### For utilities and public decision-makers: make queue rights and cost obligations credible

Large load requests differ from ordinary incremental demand because individual projects can be hundreds of megawatts and can request service faster than generation and networks are built [3]. Utilities and regulators therefore need transparent milestones for site control, financing, customer commitments, deposits, construction progress, and withdrawal. Speculative projects should not indefinitely block credible ones, while developers need enough schedule certainty to finance construction.

Cost allocation should follow causation and risk. If a project triggers dedicated infrastructure, minimum bills, security, staged service, and exit provisions can reduce the chance that other customers pay for abandoned capacity. The precise tariff is jurisdiction-specific, but the principle is general: the party controlling the uncertain expansion should retain meaningful exposure to forecast error [1][4]. At the same time, a predictable high-load customer can improve use of existing infrastructure where genuine spare capacity exists, so every project should not be treated as a cost by default [1].

Public incentives should distinguish economic activity from durable net benefit. Construction can create a large temporary effect while operations use fewer direct workers; tax exemptions can influence location while reducing public revenue; and local tax gains can coexist with transmission, generation, land, water, noise, or environmental costs [4]. Evaluation should state the geographic boundary, time period, counterfactual location, infrastructure cost, and who bears each cost. Gross investment is not a complete welfare measure.

Transparency improves planning. Facility-level PUE alone is insufficient, but standardized reporting of electricity, water, capacity, utilization, emissions, and flexibility can make forecasts and comparisons less speculative [2][8][10]. Confidential customer data can be protected while aggregate operating evidence is disclosed. Better evidence lowers the risk that policy is set by either exaggerated demand projections or outdated efficiency assumptions.

### For strategists: map the profit pool as bottlenecks move

Data center strategy should identify which link is scarce in each market. In one region the bottleneck may be a utility connection; in another, fiber routes, permits, skilled construction labor, high-density equipment, low-cost capital, or a tenant with credible long-term demand. Scarcity that can be copied within two years is not a durable moat. Scarcity embedded in network density, hard-to-replicate rights, trusted operations, or a multi-market customer relationship may last longer [6][7].

Profit-pool analysis should include adjacent suppliers without collapsing the topic into semiconductor or cloud analysis. When accelerators are scarce, chip vendors can capture much of the value. When power-ready sites are scarce, land and connection rights gain value. When customers need many counterparties, interconnection services can earn attractive incremental economics. When hyperscalers dominate leasing, they can force facility providers toward lower owner-like returns. The data center owner captures durable profit only where its contribution remains both necessary and difficult to substitute.

Scenario analysis should separate secular compute growth from the capacity cycle. A base case can assume strong demand and still produce weak owner returns if too much supply arrives, financing is expensive, or customers bargain away scarcity rents. A downside case should combine efficiency gains, slower AI monetization, customer self-build, delayed energization, and synchronized capacity delivery. An upside case should require evidence of signed demand, connection progress, disciplined competing supply, and returns above replacement cost rather than relying only on workload forecasts [1][2][5][9].

What would change the author's assessment? Evidence that connection queues clear much faster without large cost, that standardized high-density capacity becomes abundant, that customer concentration falls, and that new capacity still earns attractive returns would weaken the current power-scarcity thesis while strengthening the sector's long-run volume outlook. Evidence that projects continue to secure power but fail to commence billing, or that efficiency and self-build reduce third-party leasing, would indicate that announced capacity has outrun demand.

The central implication is simple: compute demand is necessary but not sufficient. Data center economics compound only when a provider converts scarce inputs into contracted, utilized capacity at a return that survives depreciation, reinvestment, concentration, and financing. Growth measured before that conversion is a pipeline; value measured after it is a business.

## Sources

1. International Energy Agency. "Key Questions on Energy and AI: Executive Summary." 2026. Current demand, investment, bottlenecks, efficiency, and 2030 scenarios.
   https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary [high]

2. Lawrence Berkeley National Laboratory and US Department of Energy. "United States Data Center Energy Usage Report: 2025 Update." Bottom-up equipment and facility scenarios through 2030.
   https://www.energy.gov/documents/united-states-data-center-energy-usage-report-2025-update [high]

3. US Department of Energy, Secretary of Energy Advisory Board. "Recommendations on Powering Artificial Intelligence and Data Center Infrastructure." July 30, 2024.
   https://www.energy.gov/sites/default/files/2024-08/Powering%20AI%20and%20Data%20Center%20Infrastructure%20Recommendations%20July%202024.pdf [high]

4. Virginia Joint Legislative Audit and Review Commission. "Data Centers in Virginia." Report 598, December 2024. Industry, economic, utility, and regional evidence.
   https://jlarc.virginia.gov/pdfs/reports/Rpt598.pdf [high]

5. Masanet, E., Shehabi, A., Lei, N., Smith, S., and Koomey, J. (2020). "Recalibrating Global Data Center Energy-Use Estimates." Science, 367(6481), 984-986.
   https://doi.org/10.1126/science.aba3758 [high]

6. Equinix, Inc. "Annual Report on Form 10-K for the Year Ended December 31, 2025." Filed February 11, 2026. Primary disclosure on products, utilization, power constraints, capital, and risks.
   https://www.sec.gov/Archives/edgar/data/1101239/000110123926000032/eqix-20251231.htm [high]

7. Digital Realty Trust, Inc. and Digital Realty Trust, L.P. "Annual Report on Form 10-K for the Year Ended December 31, 2025." Primary disclosure on contracts, capacity, customers, development, financing, and risks.
   https://www.sec.gov/Archives/edgar/data/1494877/000110465926015365/dlr-20251231x10k.htm [high]

8. National Academies of Sciences, Engineering, and Medicine. (2025). "Implications of Artificial Intelligence-Related Data Center Electricity Use and Emissions: Proceedings of a Workshop." National Academies Press. DOI 10.17226/29101.
   https://www.nationalacademies.org/read/29101/chapter/4 [high]

9. CBRE. "North America Data Center Trends H1 2025." September 8, 2025. Commercial market survey of supply, vacancy, preleasing, pricing, and site constraints.
   https://www.cbre.com/insights/reports/north-america-data-center-trends-h1-2025 [medium]

10. Uptime Institute. "Global Data Center Survey 2025." Operator survey covering PUE, density, capacity planning, outages, hybrid deployment, and staffing.
    https://datacenter.uptimeinstitute.com/rs/711-RIA-145/images/2025.Annual.Survey.Report.pdf?version [medium]

11. Google. "Power Usage Effectiveness." Fleet-level PUE and compute-efficiency disclosures for 2025.
    https://www.google.com/about/datacenters/efficiency [high]

## See Also

- `library/industries-sectors/capital-cycle-analysis.md` -- the delayed supply response that can turn high expected returns into overcapacity.
- `library/industries-sectors/industry-profit-pools.md` -- how revenue and economic profit divide across a value chain.
- `library/industries-sectors/semiconductor-industry-structure-and-economics.md` -- the chip supply, utilization, and reinvestment economics adjacent to data centers.
- `library/technology/cloud-computing.md` -- the service and operating model built on rented computing infrastructure.
- `library/engineering-infrastructure/telecommunications-physical-infrastructure.md` -- the physical power, connectivity, and resilience systems on which facilities depend.
