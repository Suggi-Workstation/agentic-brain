---
name: buildings-and-urban-infrastructure
id: 20260902T020053Z
tier: library-topic
domain: engineering-infrastructure
author: Librarian
tags: [buildings, urban-infrastructure, structural-systems, building-codes, hvac, lifecycle-cost, green-building, fazlur-khan]
links:
  - library/engineering-infrastructure/reliability-engineering-failure-analysis.md
  - library/engineering-infrastructure/infrastructure-resilience-climate-adaptation.md
  - library/engineering-infrastructure/power-grid-infrastructure-generation-transmission-distribution.md
  - library/engineering-infrastructure/transport-infrastructure-roads-railways-ports-airports.md
  - library/engineering-infrastructure/water-and-wastewater-systems.md
  - library/engineering-infrastructure/manufacturing-systems-industrial-engineering.md
reviewed: 2026-09-23
---

# Buildings and Urban Infrastructure -- Engineered Systems That Shape the Vertical City

A building is simultaneously a structure, an environmental-control system, a long-lived asset, and a node in urban infrastructure. Its performance depends on coordinated decisions about loads, materials, mechanical services, energy, information, maintenance, and connections to power, water, transport, waste, and communications networks. This topic explains those engineering relationships and why optimizing one subsystem in isolation can reduce the performance of the whole ([1] [3] [13] [18]).

## Background

Modern building engineering emerged as structural framing separated the load-carrying skeleton from the enclosure. The Home Insurance Building in Chicago, completed in 1885, used an early skeletal metal frame and is generally recognized as one of the first skyscrapers, although historians continue to debate the priority and extent of its structural innovation. The important engineering change was not a single disputed title but the move from thick load-bearing walls toward skeletal metal framing and reinforced concrete, which permitted larger openings, more usable floor area, and greater height. Later tall buildings exposed a new constraint: gravity loads did not disappear, but lateral wind and seismic effects increasingly governed stiffness, drift, member size, and occupant comfort as height increased ([1]).

Fazlur Rahman Khan supplied a durable conceptual response. In 1961 he described the increasing structural penalty imposed by lateral loads as a "premium for height." His framed-tube concept used closely spaced perimeter columns connected by deep spandrel beams to create a stiff exterior system; braced tubes used diagonal members to mobilize more of the perimeter through axial action. The DeWitt-Chestnut Apartments introduced the framed-tube concept, the John Hancock Center demonstrated the steel braced tube, and the Sears Tower, now Willis Tower, demonstrated the bundled tube. These systems did not create one universal height rule. They expanded the set of ways in which engineers could distribute gravity and lateral resistance across the full building section ([1] [2]).

Subsequent systems combined cores, perimeter frames, outriggers, belt trusses, and diagonal grids. Ali and Moon's reviews place these systems in a broader history of tall-building design and emphasize that structural efficiency depends on geometry, material, load path, construction sequence, and local wind and seismic conditions. Taipei 101 is a documented example: the 508 m tower uses a braced core, multiple outriggers, perimeter moment frames, and a rooftop pendulum tuned mass damper. Such examples show why historical structural-system charts are useful screening tools but not prescriptive height limits ([2] [5]).

Codes and standards converted accumulated engineering knowledge into repeatable minimum design procedures. ASCE/SEI 7-22 prescribes design loads for dead, live, soil, flood, tsunami, snow, rain, atmospheric ice, seismic, wind, and fire hazards and specifies how loads are combined. It is a loading standard rather than a complete building design method: engineers must still select an appropriate structural system, use the applicable material standard, detail a continuous load path, and exercise professional judgment. For unusual tall buildings, the PEER Guidelines present a performance-based alternative to prescriptive seismic procedures in ASCE 7 and the International Building Code ([3] [4]).

Building engineering also became an environmental-control discipline. ASHRAE standards address thermal environmental conditions, ventilation and acceptable indoor air quality, and minimum energy-efficiency requirements. The applicable edition depends on the jurisdiction or certification program, so a current standalone standard cannot be assumed to be the edition incorporated by a particular code. This distinction matters because a building can satisfy structural safety requirements while performing poorly in comfort, air quality, energy use, maintainability, or carbon emissions ([7]).

The scale of building energy and carbon effects makes those operational decisions consequential. The 2025-2026 Global Status Report for Buildings and Construction reports that the buildings and construction sector used 28% of global energy in 2024. Building operations emitted 9.9 GtCO2, approximately 26% of global energy-related CO2 emissions, while the wider buildings and construction sector accounted for about 37% of global carbon emissions when construction and materials were included. These measures have different boundaries and must not be collapsed into one percentage ([6]).

Green-building systems increasingly address both operational and embodied carbon. The requirements used here are from the July 2026 LEED v5 Reference Guide for Building Design and Construction. For New Construction and Core and Shell projects, its embodied-carbon prerequisite requires quantification of cradle-to-gate emissions for structure, enclosure, and hardscape materials, identification of the three largest sources, and consideration of project-specific reduction strategies. Its operational-carbon procedure also uses a 25-year business-as-usual projection; the guide does not state that a universal 3.8% annual decline is equivalent to a 95% reduction over that period ([8]).

Finally, buildings cannot be understood only at the parcel boundary. Princeton's civil and environmental engineering program describes cities through linked land, building, energy, water, food, mobility, climate, and environmental systems. Urban infrastructure research likewise shows that transport, water, and solid-waste systems can transmit disruptions and environmental effects across organizational boundaries. The building is therefore both an engineered object and a participant in larger networks whose failures, capacities, and recovery times shape whether the building can perform its intended function ([9] [18]).

## Core Concepts

### Structural System Selection and the Premium for Height

Structural system selection establishes the principal load paths from floors and enclosure to foundations. A low- or mid-rise building may obtain lateral resistance from moment frames, braced frames, or structural walls. As height, slenderness, or exposure increases, designers may use framed or braced tubes, core-outrigger systems, diagrids, or hybrids. These are system families, not fixed recipes. The appropriate choice depends on building form, material, floor planning, foundation conditions, wind climate, seismic demand, construction capability, fire protection, robustness, and the acceptable limits for drift, acceleration, and damage ([1] [2]).

A framed tube uses closely spaced perimeter columns joined by deep spandrel beams so that the exterior participates as a stiff three-dimensional system. A braced tube uses diagonal bracing to increase perimeter participation and transfer lateral actions mainly through axial forces. A bundled tube joins several framed tubes so that they act together and can terminate at different elevations. An outrigger links a central core to perimeter columns, increasing the effective structural depth and using perimeter axial forces to resist overturning. A diagrid uses perimeter diagonal members efficiently in axial action. Each arrangement changes stiffness, force distribution, connection demand, constructability, usable area, and the interaction between architecture and structure ([1] [2]).

Taipei 101 illustrates why tall buildings commonly combine mechanisms rather than rely on one label. Its braced core and outriggers engage perimeter columns, its perimeter moment frames provide an additional load path, and its tuned mass damper limits motion under wind. The engineering lesson is not that every supertall building should copy this arrangement. It is that gravity strength, lateral strength, stiffness, redundancy, dynamic response, foundation behavior, and construction sequence must be checked as one interacting system ([5]).

Historical charts relating system type to height remain useful for concept comparison, but they should not be treated as current design limits or evidence that one system is always optimal at a stated story count. Modern analysis, wind-tunnel testing, nonlinear response assessment, high-strength materials, damping devices, digital fabrication, and project-specific construction methods can change feasible ranges ([2]). The author's assessment is that a defensible selection process compares alternatives against explicit performance criteria and records the assumptions that would reverse the choice.

### Loads, Codes, and Performance Objectives

A building code establishes minimum public-safety requirements; it does not guarantee zero damage, uninterrupted operation, or economic optimality. ASCE/SEI 7-22 supplies a coordinated basis for evaluating environmental and occupancy-related loads and their combinations. The standard includes multiple hazards because a safe load path must consider both routine actions and rare events, and because the governing combination can change by component, direction, limit state, and stabilizing or destabilizing effect. Strength design applies prescribed load factors rather than uniformly increasing every load ([3]).

The distinction between strength, serviceability, and functional recovery is central. A member may have adequate nominal strength while the building experiences excessive drift, acceleration, vibration, cracking, water intrusion, equipment damage, or loss of utilities. Essential functions may therefore require objectives beyond ordinary life safety. Performance-based design makes those objectives explicit and uses analysis, testing, review, and acceptance criteria suited to the project. The PEER tall-building guidelines provide one documented alternative framework for seismic design where prescriptive procedures are not sufficient for the intended system or performance question ([4]).

Risk classification, site hazards, structural configuration, and material detailing are interdependent. A design team cannot infer a permitted system or detailing requirement from seismic category alone, and it should not transfer a factor or equation from one standard edition to another without checking scope and adoption. The practical control is a documented code basis: governing jurisdiction, adopted code and amendments, referenced standard editions, risk category, hazard parameters, analysis method, material standards, performance objectives, and independent-review requirements where applicable. This is a synthesis of the standards process rather than a claim that one checklist replaces professional judgment ([3] [4]).

### Mechanical Systems, Indoor Conditions, and Energy

Mechanical systems maintain indoor conditions by moving heat, air, and sometimes moisture while supplying ventilation and controlling contaminants. ASHRAE Standard 55 addresses thermal environmental conditions for human occupancy; Standard 62.1 addresses ventilation and acceptable indoor air quality; and Standard 90.1 addresses minimum energy efficiency for sites and buildings except low-rise residential buildings. These standards define different performance questions. More ventilation is not automatically better if distribution, filtration, humidity, controls, and energy recovery are neglected, and lower energy use is not acceptable if it compromises indoor environmental quality ([7]).

System configuration and control determine how closely delivered capacity follows changing loads. Variable-air-volume systems adjust zone airflow, while variable-refrigerant-flow systems modulate refrigerant delivery to indoor units. Demand-controlled ventilation changes outdoor-air delivery in response to occupancy-related signals. Economizers use favorable outdoor conditions to reduce mechanical cooling. Heat-recovery devices transfer energy between exhaust and supply streams. The engineering objective is coordinated part-load performance, not maximum component efficiency at a single rating point ([10] [11] [12]).

Published percentages require their original denominator and boundary. Cuce and Cuce summarize a university-building case in which modeled monthly consumption was 18,549.6 kWh for the existing split-system configuration and 9,626.9 kWh for a VRF alternative, a 48.1% reduction in the reported monthly totals. The same case reported a 36.6% reduction in energy-performance index, from 12.67 to 8.03 kWh/m2-month. These are different metrics and a case-specific modeling result, not a universal VRF guarantee ([10]).

Control studies likewise should not be combined into a single performance promise. Dharmasena and Nassif tested a split-signal economizer damper strategy in a chilled-water VAV system. Laboratory tests reported 0.2-5% fan-energy savings depending on ventilation-air fraction, while simulations for selected U.S. climate zones indicated possible reductions of 15-20% in energy use, operating cost, and CO2 emissions. Rashid et al. review separate studies reporting up to 88% energy savings for one optimized demand-controlled-ventilation case, approximately 90% heat-recovery effectiveness for one exchanger under stated flow conditions, and up to 19% heating-energy savings for a different combined system. None of these maxima should be transferred to an unevaluated building ([11] [12]).

### Lifecycle Cost, Information, and Facility Management

Initial cost is only one part of an asset decision. NIST GCR 04-867 describes a typical commercial-building life cycle of about 45-50 years. In its example, planning and design plus construction and commissioning account for 30-40% of total life-cycle cost, while operations, maintenance, and renewal account for 60-70%, in constant dollars. Those ranges are historical and scope-specific, but they show why decisions about access, durability, controls, replacement, commissioning, and documentation belong in design rather than being deferred to operations ([13]).

Life-cycle cost analysis compares alternatives over a common study period by discounting relevant initial, replacement, residual, energy, water, operating, maintenance, repair, and disposal costs. A credible analysis discloses service lives, timing, escalation, discount rate, residual values, and the treatment of uncertainty. Sensitivity or break-even analysis is necessary when a result depends strongly on uncertain energy prices, maintenance intervals, failure rates, or equipment lives. The least initial-cost option and the least life-cycle-cost option can therefore differ without either calculation being internally inconsistent ([14]).

NBIMS-US Version 4 defines a building information model as a shared digital representation of a built asset's physical and functional characteristics. BIM workflows can support design authoring, coordination, quantity extraction, construction documentation, record information, asset management, space management, and performance monitoring. A model does not automatically produce those outcomes. Owners must define information requirements, exchange formats, validation responsibilities, identifiers, and the destination systems that will use the data ([15]).

For facility management, GSA guidance treats the record BIM and associated asset information as turnover deliverables that can support an equipment inventory, warranty and maintenance information, analysis, and integration with a computerized maintenance-management system. It also emphasizes defining facility-management data requirements early and validating delivered information. Abideen et al.'s systematic review found that BIM-O&M research is still emerging and that practical return-on-investment evidence and clear facility-management information requirements remain limited. Claims of universal percentage savings therefore exceed the evidence; operational value is conditional on useful, validated, maintained data and adopted work processes ([16] [17]).

The economic cost of poor information exchange is documented but should not be mislabeled as a BIM saving. NIST estimated that inadequate software interoperability cost the U.S. capital-facilities industry $15.8 billion in 2002. Owners and operators bore about $10.6 billion, or two-thirds, and incurred most of that burden during ongoing operations and maintenance. The estimate is historical, covers commercial and institutional buildings and industrial facilities, and quantifies interoperability costs rather than the return from any one software platform ([13]).

### Urban Infrastructure Integration

Integration and decentralization answer different questions. Integration concerns whether two or more infrastructure systems are planned and operated with explicit awareness of one another. Decentralization concerns the spatial and organizational distribution of production, treatment, storage, and control. The engineering problem is not to maximize either characteristic without limit, but to choose an arrangement that meets required service, safety, maintainability, cost, and recovery objectives ([18]).

Jayasinghe, Derrible, and Kattan identify concrete links among urban transport, water, and solid-waste systems. Road and gas-station runoff can affect water quality; de-icing agents can enter water systems; water-pipe work can close streets and disrupt transport; and road access affects waste collection. Water and waste systems are linked through treatment sludge, water used in waste processing, wastewater from waste treatment, and landfill leachate. Their review is qualitative and calls for more quantification, so these pathways establish interdependence but do not prove a universal percentage gain from integration ([18]).

Power-water coupling supplies another example. Water and wastewater systems require electricity for pumping, treatment, monitoring, and control, while many electricity-generation processes require water. Argonne National Laboratory describes this as a physical interdependence: loss of one service can constrain the other, with timing and severity determined by system configuration and backup capacity. Such dependencies can create cascading failures, but the word "cascade" should not erase direction, duration, or the difference between a dependency and a reciprocal interdependency ([19]).

Grid-interactive buildings add a controlled form of coupling. The IEA describes efficient grid-interactive buildings as potential low-carbon prosumers able to produce, consume, store, buy, and sell energy and provide flexibility to the electricity system. That capability can include on-site generation, storage, controllable loads, and digital coordination. It does not mean that every equipped building reduces required grid capacity; the effect depends on coincidence with system needs, control performance, tariffs, aggregation, and network constraints ([20]).

Princeton's research framing extends the systems boundary to land, buildings, energy, water, food, mobility, climate, heat, flooding, wind, and pollution. The author's assessment is that building-level resilience measures should therefore be evaluated twice: first for the building's own function, and second for their effect on connected networks. Backup generation, storage, rainwater management, or load flexibility can be valuable, but each shifts capital cost, maintenance burden, resource use, and failure modes rather than eliminating them ([9]).

## Evidence

### Structural Systems Demonstrated in Built Work

The development of tube systems is supported by built projects rather than by a single controlled experiment. Ali and Al-Kodmany identify the DeWitt-Chestnut Apartments as the project that introduced the framed-tube concept. Sources disagree on whether to count 42 or 43 stories and whether to assign 1965 or 1966 as the completion year, so the structural fact is more reliable than a mixed date-and-story label. The same review identifies the 100-story John Hancock Center as the first steel braced-tube structure and the Sears Tower, completed in 1974, as the first steel bundled-tube structure. At the Sears Tower, nine framed tubes are bundled at the base and terminate at different elevations ([1]).

These projects validate distinct load-path ideas. Closely spaced columns and spandrels formed the framed tube; exterior diagonal bracing increased perimeter participation at the John Hancock Center; and bundled cells allowed the Sears Tower plan and elevation to step while preserving collective action. Ali and Moon's later review documents how tall-building systems subsequently incorporated outriggers, diagrids, mega-columns, and other combinations. The evidence supports an expanding design vocabulary, not the claim that most buildings above one story threshold use one system or that a fixed percentage of steel is always saved ([1] [2]).

Taipei 101 provides a detailed combined-system case. Chang's structural-design presentation documents the tower's core, outriggers, perimeter framing, and tuned mass damper, while the CTBUH building record gives a height of 508 m. The author's assessment is that the project illustrates how a supertall design can coordinate strength, stiffness, dynamic response, and redundancy through interacting systems ([5]).

### HVAC Case Studies and Review Evidence

The HVAC literature demonstrates both potential savings and the danger of transferring a best-case percentage. In the university-building case summarized by Cuce and Cuce, the reported monthly totals fall from 18,549.6 to 9,626.9 kWh, a calculated reduction of 48.1%. The reported energy-performance index falls by 36.6%. The review also notes that much advanced-HVAC evidence remains simulation-based and calls for longitudinal field validation that can capture degradation, commissioning defects, maintenance, and real operating behavior ([10]).

Dharmasena and Nassif provide a narrower control experiment. Their 2024 study tested a split-signal economizer damper strategy under laboratory conditions in a chilled-water VAV system and then modeled annual operation. The laboratory result was 0.2-5% fan-energy savings, while the annual simulations indicated 15-20% potential reductions in energy use, operating cost, and CO2 emissions for selected climates. The separation between tested fan energy and simulated whole-year outcomes is essential to interpreting the evidence ([11]).

Rashid et al.'s 2025 review assembles ventilation studies with different buildings, controls, climates, and endpoints. One optimized demand-controlled-ventilation study reported savings up to 88%; another school study kept CO2 below 1000 ppm for 76% of the year; one heat exchanger approached 90% effectiveness at lower mass-flow rates; and a different combined stove and heat-recovery-ventilation system saved up to 19% of heating energy over a heating season. The review supports the value of controls and recovery, but the numbers describe separate systems and conditions rather than one combined result ([12]).

### Lifecycle Cost and Information Evidence

NIST's 2004 interoperability study supplies two distinct findings. First, its illustrative commercial-building life cycle assigns 30-40% of cost to planning, design, construction, and commissioning and 60-70% to operations, maintenance, and renewal. Second, it estimated $15.8 billion in U.S. capital-facilities interoperability costs for 2002, with $10.6 billion borne by owners and operators. The first finding motivates life-cycle analysis; the second measures the cost of fragmented information exchange. Neither proves a particular BIM return on investment ([13]).

The BIM evidence is correspondingly conditional. GSA's facility-management guide describes required asset information, validation, repositories, links to maintenance systems, and analysis functions. Abideen et al. systematically reviewed BIM use in operations and maintenance and found research clusters around information management, maintenance and asset management, visualization, performance assessment, and advanced technologies. They also identified unclear information requirements and limited practical return-on-investment evidence. These sources support early owner involvement and explicit data governance, not unsupported claims of 10-15% maintenance savings or automatic annual savings as a share of asset value ([16] [17]).

### Carbon and Network Evidence

The GlobalABC report distinguishes operational emissions from the broader construction-sector boundary. Its 2024 values show why both efficient operation and lower-emission materials matter, while preventing the common error of calling the sector's approximately 37% share an operational-building statistic. LEED v5 BD+C operationalizes that broader view by requiring embodied-carbon quantification for specified material categories and a separate operational-carbon projection. Certification is not evidence that every design choice is optimal, but the requirements make carbon boundaries and hot spots visible to project teams ([6] [8]).

Jayasinghe et al. build an interdependency matrix from a comprehensive review of transport, water, and solid-waste links and analyze those relationships qualitatively. Their examples include contaminated runoff, road disruption caused by water work, transport dependence of waste collection, treatment sludge, waste-processing water demand, wastewater, and landfill leachate. The study shows identifiable pathways for cascading disruption and coordinated planning, while explicitly leaving quantitative benefit estimates for future work ([18]).

The Argonne analysis gives the power-water example a physical basis: pumps and treatment processes depend on electricity, while power generation may depend on water for steam and cooling. The IEA's grid-interactive-building framework shows a different relationship in which flexible building loads and distributed resources can provide grid services. Together, these cases demonstrate that urban integration can create both vulnerability and optionality; whether the net effect is beneficial depends on controls, reserves, communication, maintenance, and recovery design ([19] [20]).

## Implications

### For Structural Engineers and Architects

Structural system selection should be treated as a multi-criteria comparison rather than a story-count lookup. Historical systems and charts identify useful families, but the project team must compare gravity and lateral load paths, stiffness, dynamic response, robustness, foundations, fire protection, construction sequence, architecture, and cost. Early comparison is valuable because the chosen system affects column spacing, core size, facade support, mechanical distribution, rentable area, and foundation demand. The author's assessment is that each alternative should state its controlling performance criteria and the assumptions under which another system would become preferable ([1] [2]).

The code basis should remain traceable throughout design. Teams should record the jurisdiction, adopted code and amendments, referenced standard editions, risk classification, hazards, analysis methods, material standards, and performance objectives. Equations or factors should not be copied between editions without verification, and a code-minimum strength check should not be represented as proof of comfort, continued operation, or rapid recovery. Where performance-based seismic design is used, the objectives, analysis, acceptance criteria, and review process need to be explicit and project-specific ([3] [4]).

Coordination with architecture and mechanical design is an engineering requirement, not only a documentation task. Openings through cores, plant loads, facade anchors, penetrations, equipment vibration, smoke-control paths, and maintenance access can alter structural behavior or serviceability. BIM can expose geometric conflicts, but only engineering review can determine whether a resolved clash also preserves load paths, access, fire separation, commissioning, and future replacement. The model is therefore a coordination medium, not a substitute for responsible design decisions ([15] [16]).

### For Owners and Facility Managers

Owners influence life-cycle performance most effectively by defining operational requirements before procurement. A request for a model without specified asset data, identifiers, validation, handover format, destination system, and update responsibility produces a file, not an operational capability. GSA's guidance supports early definition of equipment, warranty, maintenance, spatial, and performance information and integration with the owner's maintenance processes. The owner's acceptance test should address completeness, accuracy, usability, and responsibility for future changes ([16]).

Life-cycle cost analysis should compare alternatives over the same study period and with transparent assumptions. Higher initial cost can be justified when discounted reductions in energy, maintenance, replacement, disruption, or disposal exceed the premium, but the conclusion depends on service life, timing, price escalation, discount rate, residual value, and uncertainty. Sensitivity analysis is especially important for long-lived buildings because small changes in repeated operating costs can dominate an initial difference, while optimistic maintenance or equipment-life assumptions can reverse the ranking ([14]).

The NIST interoperability estimate is a warning about fragmented information, not a promised BIM dividend. Owners should therefore measure outcomes that relate to their own processes: time to locate asset records, preventive-maintenance completion, repeat visits, failure duration, energy variance, commissioning defects, data-validation errors, and cost of updating records. Abideen et al.'s finding that practical ROI evidence remains limited means that investment decisions should use local baselines and controlled pilots rather than imported percentage claims ([13] [17]).

### For Mechanical Engineers and Building Operators

HVAC design should be judged across annual and part-load operation, indoor environmental quality, maintainability, and control stability. Peak equipment efficiency alone does not show how a system performs with real schedules, simultaneous heating and cooling, sensor drift, fouled filters, disabled heat recovery, poor balancing, or operator overrides. The reported VRF, economizer, demand-control, and heat-recovery results demonstrate possible gains but also show why evidence must preserve whether an outcome was measured, simulated, or summarized from another study ([10] [11] [12]).

Commissioning and ongoing verification connect design intent to actual operation. Useful metrics include zone conditions, ventilation delivery, fan and pump power, heating and cooling energy, simultaneous loads, control sequences, alarm quality, and persistence after occupancy changes. The author's assessment is that control complexity should be accepted only when staff, sensors, documentation, and maintenance can sustain it; a simpler system that remains commissioned may outperform a nominally superior system whose controls degrade or are routinely bypassed ([10]).

### For Urban Planners and Infrastructure Engineers

A building permit or site design that considers only parcel-level capacity can miss network effects. Water work can disrupt roads; road runoff can impair water quality; road access can constrain waste collection; electricity loss can interrupt pumping and treatment; and water constraints can affect some power-generation processes. Planning should therefore map directional dependencies, common corridors, shared control systems, backup duration, restoration priorities, and the organizations responsible for each interface ([18] [19]).

Integration can improve coordination, but it can also create new common-mode failures. Digital control may allow buildings to shift demand and provide grid flexibility, while a communication or control failure can disable that service. On-site generation and storage may preserve selected functions during an outage, while adding equipment, fire-safety, replacement, and maintenance obligations. The author's assessment is that centralized, decentralized, and hybrid arrangements should be compared against required function, outage duration, network reliability, lifecycle cost, available space, maintenance capacity, and recovery objectives rather than selected by a universal rule ([20]).

Buildings should also be represented accurately in network models. A building is not merely an annual energy or water total; its peak timing, flexibility, storage, quality requirements, discharge characteristics, occupancy, and failure tolerance determine network impact. Princeton's linked-systems research framing is useful because it places building decisions within land, mobility, energy, water, food, climate, heat, flooding, and pollution constraints. This broader boundary helps distinguish a local optimization from a system improvement ([9]).

### For Carbon and Green-Building Programs

Operational and embodied carbon require separate inventories and coordinated decisions. Efficient equipment and controls can reduce operational emissions, but material quantities, product emissions, construction processes, replacement cycles, and grid evolution change the total. The GlobalABC boundary distinction and LEED v5 BD+C requirements help prevent operational energy, operational CO2, embodied carbon, and whole-sector emissions from being treated as interchangeable indicators ([6] [8]).

LEED's embodied-carbon prerequisite makes the structure, enclosure, and hardscape visible as material systems with measurable A1-A3 emissions and identifiable hot spots. The engineering value comes from using those results to compare feasible alternatives while preserving safety, durability, constructability, moisture control, fire performance, and service life. The author's assessment is that a low initial material footprint can be a false economy if premature replacement or poor durability shifts emissions later in the life cycle ([8]).

The 25-year operational-carbon projection similarly requires assumptions about energy use, grid conditions, and location. It should be reported with its boundary and assumptions rather than compressed into an unsupported annual decline or cumulative percentage. The author's assessment is that carbon analysis is most useful when it informs reversible design choices early, identifies decisions that lock in long-lived emissions, and remains linked to measured operation after occupancy ([8]).

The author's assessment is that a building performs as a system embedded in other systems. Structural efficiency, indoor conditions, life-cycle economics, information quality, carbon, and urban resilience cannot all be maximized independently. Good engineering makes the trade-offs explicit, verifies claims with the correct denominator and source boundary, and preserves enough operational evidence to learn whether the built result met the design objective.

## Sources

1. Ali, M. M. and Al-Kodmany, K. (2022). "Structural Systems for Tall
   Buildings." Encyclopedia, 2(3), 1260-1286.
   https://doi.org/10.3390/encyclopedia2030085 [high]

2. Ali, M. M. and Moon, K. S. (2018). "Advances in Structural Systems
   for Tall Buildings: Emerging Developments for Contemporary Urban
   Giants." Buildings, 8(8), 104.
   https://doi.org/10.3390/buildings8080104 [high]

3. American Society of Civil Engineers. "ASCE/SEI 7-22: Minimum Design
   Loads and Associated Criteria for Buildings and Other Structures."
   https://www.asce.org/publications-and-news/codes-and-standards/asce-sei-7-22 [high]

4. Hamburger, R. et al. (2017). "Guidelines for Performance-Based
   Seismic Design of Tall Buildings, Version 2.03." PEER Report
   2017-06, Pacific Earthquake Engineering Research Center.
   https://peer.berkeley.edu/publications/2017-06 [high]

5. Chang, C.-C. "Structural Design of Taipei 101 Tower." Evergreen
   Consulting Engineering presentation hosted by Taiwan's National
   Center for Research on Earthquake Engineering; building record from
   the Council on Tall Buildings and Urban Habitat.
   https://conf.ncree.org.tw/download/i0981026-structural%20design%20of%20taipei%20101%20tower.pdf
   https://www.skyscrapercenter.com/building/taipei-101/117 [high]

6. United Nations Environment Programme and Global Alliance for
   Buildings and Construction. (2026). "Global Status Report for
   Buildings and Construction 2025-2026."
   https://globalabc.org/sites/default/files/resources/2026-05/global-status-report-for-buildings-and-construction-2025_2026.pdf [high]

7. ASHRAE. "Standards 55, 62.1, and 90.1" official scope and edition
   pages for thermal conditions, ventilation and indoor air quality,
   and building energy efficiency.
   https://www.ashrae.org/technical-resources/bookstore/standard-55-thermal-environmental-conditions-for-human-occupancy
   https://www.ashrae.org/technical-resources/bookstore/standards-62-1-62-2
   https://www.ashrae.org/technical-resources/bookstore/standard-90-1 [high]

8. U.S. Green Building Council. (2026). "LEED v5 Reference Guide for
   Building Design and Construction, July 2026 Edition."
   https://www.usgbc.org/sites/default/files/2026-07/LEED%20v5%20BD%2BC%20Rating%20System_July%202026.pdf [high]

9. Princeton University Department of Civil and Environmental
   Engineering. "Sustainable, Resilient Cities and Infrastructure
   Systems."
   https://cee.princeton.edu/research/sustainable-resilient-cities-and-infrastructure-systems [high]

10. Cuce, P. M. and Cuce, E. (2026). "Role of HVAC in Building Energy
    Consumption: A Critical Review." Journal of Thermal Analysis and
    Calorimetry, 151, 3059-3080.
    https://doi.org/10.1007/s10973-026-15322-9 [high]

11. Dharmasena, P. and Nassif, N. (2024). "Testing, Validation, and
    Simulation of a Novel Economizer Damper Control Strategy to Enhance
    HVAC System Efficiency." Buildings, 14, 2937.
    https://doi.org/10.3390/buildings14092937 [high]

12. Rashid, F. L. et al. (2025). "Mechanical Ventilation Strategies in
    Buildings: A Comprehensive Review of Climate Management, Indoor Air
    Quality, and Energy Efficiency." Buildings, 15, 2579.
    https://doi.org/10.3390/buildings15142579 [high]

13. Gallaher, M. P., O'Connor, A. C., Dettbarn, J. L., Jr., and Gilday,
    L. T. (2004). "Cost Analysis of Inadequate Interoperability in the
    U.S. Capital Facilities Industry." NIST GCR 04-867.
    https://nvlpubs.nist.gov/nistpubs/gcr/2004/nist.gcr.04-867.pdf [high]

14. Kneifel, J., Donmoyer, L., Sauder, V., and Parekh, P. D. K. (2025).
    "Building Life Cycle Cost (BLCC) User Guide." NIST Technical Note
    2346.
    https://doi.org/10.6028/NIST.TN.2346 [high]

15. National Institute of Building Sciences. "NBIMS-US Version 4: Terms
    and Definitions."
    https://nibs.org/nbims/v4/terms-and-definitions [high]

16. U.S. General Services Administration. "GSA BIM Guide Series 08:
    Facility Management."
    https://www.gsa.gov/system/files/largedocs/BIM_Guide_Series_Facility_Management.pdf [high]

17. Abideen, D. K., Yunusa-Kaltungo, A., Manu, P., and Cheung, C.
    (2022). "A Systematic Review of the Extent to Which BIM Is
    Integrated into Operation and Maintenance." Sustainability, 14(14),
    8692.
    https://doi.org/10.3390/su14148692 [high]

18. Jayasinghe, P. A., Derrible, S., and Kattan, L. (2023).
    "Interdependencies between Urban Transport, Water, and Solid Waste
    Infrastructure Systems." Infrastructures, 8(4), 76.
    https://doi.org/10.3390/infrastructures8040076 [high]

19. Gillette, J. L., Fisher, R. E., Peerenboom, J. P., and Whitfield,
    R. G. (2002). "Analyzing Water/Wastewater Infrastructure
    Interdependencies." Argonne National Laboratory conference paper.
    https://www.osti.gov/biblio/795840 [high]

20. International Energy Agency. (2026). "Efficient Grid-Interactive
    Buildings: Future of Buildings in ASEAN."
    https://www.iea.org/reports/efficient-grid-interactive-buildings [high]

## See Also

- `library/engineering-infrastructure/reliability-engineering-failure-analysis.md`
  -- failure modes and reliability analysis for structural and mechanical
  systems.
- `library/engineering-infrastructure/infrastructure-resilience-climate-adaptation.md`
  -- adaptation and resilience under changing hazards.
- `library/engineering-infrastructure/power-grid-infrastructure-generation-transmission-distribution.md`
  -- the electrical network on which most buildings depend.
- `library/engineering-infrastructure/transport-infrastructure-roads-railways-ports-airports.md`
  -- transport networks and their urban interfaces.
- `library/engineering-infrastructure/water-and-wastewater-systems.md`
  -- water supply, wastewater collection, and treatment dependencies.
- `library/engineering-infrastructure/manufacturing-systems-industrial-engineering.md`
  -- production and quality methods used for building components.
