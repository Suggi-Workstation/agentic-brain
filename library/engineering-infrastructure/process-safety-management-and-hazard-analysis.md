---
name: process-safety-management-and-hazard-analysis
id: 20260923T000835Z
tier: library-topic
domain: engineering-infrastructure
author: Librarian
tags: [process-safety, hazard-analysis, barrier-management, inherent-safety, mechanical-integrity, management-of-change]
links: [library/engineering-infrastructure/reliability-engineering-failure-analysis.md, library/engineering-infrastructure/corrosion-and-materials-degradation.md, library/engineering-infrastructure/manufacturing-systems-industrial-engineering.md, library/engineering-infrastructure/systems-engineering-complex-systems-under-constraints.md]
---

# Process Safety Management Prevents Catastrophe by Governing Barriers Before Failure

Process safety management is a lifecycle engineering system for preventing and limiting catastrophic releases, fires, explosions, and other major accidents in hazardous processes. Its central claim is prospective: organizations reduce high-consequence risk when they identify credible scenarios, choose inherently safer designs where feasible, install independent protective layers, and continuously verify that technical and organizational barriers remain effective ([1] [5] [11]).

## Background

### From equipment safety to a management system

Industrial facilities have always depended on pressure boundaries, relief systems, ventilation, isolation, and operating discipline. Process safety management, however, arose from recognition that sound individual components do not by themselves create a safe process. Catastrophic events can emerge through interactions among chemical properties, process conditions, equipment degradation, procedures, staffing, maintenance, design changes, and emergency response. OSHA therefore describes process safety management as an integrated program for preventing or minimizing catastrophic releases of toxic, reactive, flammable, or explosive chemicals, while the International Labour Organization treats major-accident control as a technical and administrative system protecting workers, surrounding populations, property, and the environment ([1] [18]).

This perspective differs from ordinary occupational safety. Personal safety programs commonly address higher-frequency events such as slips, falls, manual handling injuries, and routine exposures. Process safety addresses less frequent events whose energy or hazardous inventory can harm many people, damage critical assets, and produce offsite consequences. The two disciplines overlap but use different indicators and controls. A low recordable-injury rate does not demonstrate that pressure vessels are sound, alarms are rationalized, relief systems are adequate, or shutdown barriers will work when demanded. The BP Texas City investigation and the independent Baker Panel both found that reliance on personal injury measures obscured serious process-safety weaknesses ([12] [13]).

The modern regulatory structure in the United States reflects this system view. OSHA's 29 CFR 1910.119 establishes linked requirements for employee participation, process safety information, process hazard analysis, operating procedures, training, contractors, pre-startup review, mechanical integrity, hot work, management of change, incident investigation, emergency planning, and audits. EPA's 40 CFR part 68 adds accidental-release prevention and risk-management requirements oriented toward public health and environmental consequences, including hazard assessment, prevention programs, emergency response, and risk-management planning for covered stationary sources ([1] [3]). These rules define minimum legal coverage; the engineering logic is broader than the threshold quantities and jurisdictions that trigger them.

The Center for Chemical Process Safety subsequently organized risk-based process safety around four interacting pillars: commitment to process safety, understanding hazards and risk, managing risk, and learning from experience. This formulation turns compliance elements into a lifecycle control system. Hazard studies create scenarios and recommendations; design and operating programs implement controls; inspection and testing maintain them; indicators and audits reveal degradation; incidents and near misses revise the assumptions. The system fails when these activities become isolated documents rather than connected feedback loops ([5]).

### Hazard analysis as prospective failure analysis

Process hazard analysis is the disciplined examination of what can go wrong, how severe the consequences could be, what initiates the scenario, which safeguards interrupt it, and whether residual risk is acceptable. OSHA permits methods including What-If, Checklist, What-If/Checklist, Hazard and Operability Study, Failure Mode and Effects Analysis, Fault Tree Analysis, or an appropriate equivalent. The method must fit process complexity, and the analysis must address process hazards, prior incidents, engineering and administrative controls, consequences of control failure, facility siting, human factors, and the range of possible effects on employees ([1]).

The U.S. Department of Energy handbook expands the practical method. A qualified multidisciplinary team first assembles accurate chemical, technology, and equipment information. It divides the process into manageable systems, defines assumptions and boundaries, applies a structured method, documents scenarios and safeguards, and records recommendations in a form that is traceable and reviewable. The completed analysis is not finished when the workshop ends: findings require documented resolution, action ownership, schedules, communication to affected personnel, retention, and periodic update ([4]).

This prospective orientation distinguishes process hazard analysis from post-failure forensic analysis. Reliability and failure analysis ask why components fail and how failure probabilities can be reduced; process hazard analysis uses that knowledge before an event to construct complete cause-consequence scenarios and test defenses. Incident investigation then feeds observed weaknesses back into process information, hazard studies, mechanical integrity, procedures, and training. The result should be a learning cycle rather than two disconnected specialties ([5] [11]).

### The shift from compliance to barrier assurance

Major investigations showed that having nominal program elements is not enough. At Tesoro Anacortes, process hazard analyses listed safeguards against high-temperature hydrogen attack without evaluating or documenting whether those safeguards were effective. At Chevron Richmond, corrosion knowledge and proposed material upgrades did not produce a sufficiently rigorous damage-mechanism review or timely replacement of vulnerable piping. At Macondo, physical and operational barriers existed in concept, but the systems needed to ensure their functionality, availability, and reliability were inadequate ([14] [15] [16]).

These findings moved the field toward barrier assurance. A barrier is a technical, human, or organizational provision intended to prevent an initiating event from reaching a loss event or to reduce its consequences. The key question is not whether a barrier appears on a diagram, but whether it has a defined safety function, adequate capacity, independence from other credited layers, known failure modes, testable performance requirements, and an owner who responds to degraded status. Process safety management is effective only when that question can be answered throughout operation, maintenance, change, shutdown, and restart ([6] [10] [16]).

## Core Concepts

### Hazard, risk, scenario, and consequence

A hazard is an inherent potential for harm: flammability, toxicity, chemical reactivity, stored pressure, thermal energy, unstable materials, or another dangerous property. Risk combines possible consequences with their likelihood or frequency. A scenario connects them through a specific causal path: an initiating event occurs, preventive barriers succeed or fail, loss of containment or loss of control follows, and mitigating barriers shape the outcome. Keeping these terms separate prevents a common mistake in which a low estimated frequency is treated as if it removed the underlying hazard ([4] [5] [18]).

Scenario definition should be explicit enough to support decisions. "Pump failure" is too vague if it does not identify the failure mode, affected stream, process state, possible release, ignition or exposure conditions, and available safeguards. Conversely, an analysis can become unmanageable if every minute variation is treated as unique. The practical unit is a credible cause-consequence pair with stated assumptions, enabling the team to judge severity, initiating frequency, barrier independence, and uncertainty. CCPS defines layer of protection analysis around a single cause-consequence pair for this reason ([6]).

Consequences include more than immediate worker injury. A hazardous release can affect operators, contractors, emergency responders, neighboring communities, the environment, production assets, and connected infrastructure. EPA's Risk Management Program therefore requires covered facilities to consider offsite consequence scenarios and coordinate prevention with emergency response. OECD guidance similarly treats accident prevention, preparedness, response, and communication as linked responsibilities across facility management, public authorities, workers, responders, and communities ([3] [11]).

### Process safety information as the model of the plant

Hazard analysis is only as good as its process safety information. Required information includes chemical hazards, safe operating limits, process chemistry, maximum intended inventory, consequences of deviation, materials of construction, piping and instrumentation diagrams, relief-system design bases, electrical classification, design codes, material and energy balances where applicable, and safety systems. It should describe the actual plant rather than an idealized design that no longer exists ([1] [3]).

Accuracy matters because each analytic conclusion depends on it. An incorrect material specification can hide a corrosion mechanism; an obsolete piping diagram can omit a temporary connection; an undocumented alarm bypass can create false confidence; and an inaccurate relief basis can invalidate capacity calculations. Configuration control therefore connects process safety information to management of change, field verification, maintenance records, and pre-startup review. When a change alters equipment, chemistry, control logic, limits, or operating practice, the corresponding model must change as well ([1] [5]).

Process knowledge also includes uncertainty. Teams should identify missing data, disputed assumptions, and limits of models instead of filling gaps with confidence. Conservative screening may be appropriate until better evidence is obtained. Where an old asset was built to obsolete practices, EPA requires owners of covered processes to document that equipment is designed, maintained, inspected, tested, and operating safely; current-code gaps also form part of the Program 3 hazard-analysis inquiry ([3]).

### Selecting and conducting a process hazard analysis

Different methods expose different failure patterns. A checklist tests conformance with known requirements but may miss novel interactions. What-If analysis uses structured questions to explore deviations and unusual circumstances. A HAZOP study applies guide words to process parameters at defined nodes to reveal deviations such as no flow, reverse flow, high pressure, low temperature, or contamination. FMEA proceeds from component failure modes toward local and system effects, while fault-tree analysis works backward from a defined top event to combinations of causes. A combined strategy is often stronger than choosing one method by habit ([1] [4]).

Method quality depends on preparation and team composition. OSHA requires expertise in engineering and process operations, at least one participant experienced with the process, and a person knowledgeable in the chosen method. Useful teams include operations, maintenance, instrumentation and controls, process engineering, inspection or materials expertise, and people who understand relevant human and organizational conditions. The team needs current documents, defined scope, enough time, and facilitation that prevents status or familiarity from suppressing dissent ([1] [4]).

The study should test normal operation, startup, shutdown, temporary modes, maintenance, utilities failure, external events, simultaneous activities, and reasonably foreseeable human error. Startup and abnormal operation deserve particular attention because lineups, inventories, temperatures, staffing, and control modes differ from steady state. Human factors are not a label for operator error; the analysis should examine interface design, workload, alarm burden, procedures, competence, communications, fatigue, and the conditions under which an action is expected to succeed ([1] [12] [16]).

Recommendations must be actionable. A statement such as "operator to be careful" neither specifies a control nor establishes verifiable completion. A sound action identifies the scenario, desired risk reduction, responsible owner, technical or procedural change, due date, interim protection, and evidence needed for closure. OSHA requires a system to address findings promptly, document resolutions and actions, complete them as soon as possible, and communicate them to affected employees. DOE likewise emphasizes traceable reporting, technical review, and lifecycle retention of analyses and recommendation resolutions ([1] [4]).

### Inherently safer design and the hierarchy of controls

Inherently safer design changes the hazard itself rather than merely controlling exposure to it. Common strategies are minimization of hazardous inventory, substitution with less hazardous materials or chemistry, moderation of conditions or concentration, and simplification that reduces opportunities for error. A smaller inventory can reduce maximum release; a corrosion-resistant alloy can remove a degradation mechanism; lower pressure or temperature can reduce stored energy; and a simpler flow path can remove valves and lineups that create failure opportunities ([7] [11]).

Inherent safety is relative, not absolute. A substitution may reduce flammability while increasing toxicity, or lower inventory while increasing transfer frequency. The analysis must therefore consider the full lifecycle and avoid transferring risk to workers, transport, waste handling, or neighboring systems. Hendershot emphasizes that inherently safer design can be applied at every lifecycle stage and can be integrated into PHA, management of change, incident investigation, and mechanical integrity rather than reserved for greenfield design ([7]).

Where hazards cannot be eliminated, passive engineered protection is generally preferred over active systems, administrative controls, and personal protective equipment, subject to scenario-specific analysis. Passive containment, drainage, spacing, fireproofing, and robust materials act without detection or command. Active safeguards such as trips and isolation valves require sensors, logic, actuators, utilities, testing, and response. Procedures and operator action can be essential but depend on detection, diagnosis, time, access, training, and workload. The hierarchy does not make lower layers useless; it prevents analysts from crediting a large stack of fragile controls as equivalent to removing the hazard ([7] [18]).

### Layers of protection and barrier independence

Layer of protection analysis bridges qualitative hazard studies and detailed quantitative risk analysis. For one scenario, LOPA estimates initiating-event frequency, consequence severity, and the risk reduction provided by credited independent protection layers using conservative order-of-magnitude values. It then compares residual risk with an organizational criterion and identifies whether additional risk reduction is needed. The method supports decisions but does not convert uncertain inputs into precise truth ([6]).

An independent protection layer must prevent the scenario from reaching its undesired consequence independently of the initiating event and other credited layers. CCPS identifies attributes including independence, functionality, integrity, reliability, auditability, access security, and management of change. A high-pressure alarm and shutdown may not be independent if both depend on the same sensor, logic solver, power supply, valve, or maintenance failure. Two procedures may not be separate layers if both require the same operator to diagnose the same abnormal condition within the same short interval ([6]).

Independence is therefore a design property and a management property. Separate hardware can still share calibration practices, environmental vulnerability, or organizational neglect. Credited performance must be sustained through proof testing, inspection, bypass control, demand logging, defect correction, spare-parts quality, and change management. A barrier whose test interval is missed or whose bypass is uncontrolled is not the barrier assumed in the risk calculation ([5] [6] [16]).

Bow-tie representations can communicate the same logic. Threats and preventive barriers appear on the left of a top event; consequences and mitigating barriers appear on the right. The picture helps operations and leadership see which barriers protect multiple scenarios and where degradation factors create common-cause exposure. It should not replace the evidence behind the barrier: performance standards, maintenance tasks, test records, operating limits, and escalation rules are what make the diagram operational ([10] [16]).

### Safety instrumented systems and functional safety

A safety instrumented system detects specified conditions and takes the process to a safe state through sensors, logic solvers, and final elements. IEC 61511 establishes lifecycle requirements for specification, design, installation, operation, and maintenance of such systems in the process sector. The lifecycle matters because a correct integrity target can still be defeated by poor specification, hidden common cause, unsuitable hardware, programming errors, inadequate proof testing, unauthorized bypasses, or changes outside functional-safety review ([8]).

The process hazard analysis or LOPA identifies the safety function and required risk reduction; the safety requirements specification states what the function must do and under which conditions. Design then addresses architecture, independence, diagnostics, failure behavior, and environmental conditions. Validation demonstrates that the installed system meets the specification. Operation and maintenance preserve the function through testing, repair, records, competence, and management of modifications. Decommissioning also requires control so removal of one function does not expose another process ([6] [8]).

A safety instrumented function should not be treated as an excuse for weak basic process control or hazardous design. It is one layer in a hierarchy. The strongest arrangement uses stable process design and sound equipment, reduces hazards where practicable, prevents deviations through basic controls and operating discipline, and then provides independent protection for residual scenarios. This synthesis follows the relationship among inherent safety, barrier independence, and the IEC lifecycle rather than any claim that instrumentation alone makes a process safe ([6] [7] [8]).

### Mechanical integrity and damage-mechanism control

Mechanical integrity maintains the containment and function of pressure vessels, storage tanks, piping, relief and vent systems, emergency shutdown systems, controls, pumps, and other critical equipment. OSHA requires written procedures, trained maintenance personnel, inspection and testing consistent with good engineering practice and operating experience, documented results, correction of deficiencies, and quality assurance for new equipment and spare parts ([1]).

Effective programs are risk- and mechanism-informed. Inspection locations and intervals should reflect credible deterioration such as corrosion, erosion, fatigue, creep, embrittlement, high-temperature hydrogen attack, vibration, or external damage. Thickness measurements without a correct damage model may provide false reassurance. Process conditions, metallurgy, inspection capability, uncertainty, and consequence determine what to examine and how to interpret findings. The Tesoro and Chevron investigations show why hazard analysis and materials knowledge must be connected rather than assigned to separate systems ([14] [15]).

Temporary repairs, overdue inspections, disabled alarms, leaking seals, and unavailable shutdown devices are degraded barriers. Each should trigger a decision about operating limits, compensating measures, repair timing, and whether continued operation is permissible. Deferral is itself a risk decision and should be visible to accountable management. Barrier status is useful only if the organization has predetermined escalation rules and authority to reduce rate, restrict activities, or shut down ([10] [16]).

### Management of change and pre-startup verification

Change can invalidate every assumption in a hazard analysis. OSHA's management-of-change requirement covers changes to process chemicals, technology, equipment, procedures, and facilities affecting a covered process, except replacements in kind. Review before implementation addresses technical basis, safety and health impact, procedure changes, duration, and authorization; affected employees must be informed or trained, and process safety information and operating procedures must be updated where required ([1]).

The concept extends beyond capital projects. Changes in feed composition, software, alarm settings, inspection methods, staffing, organization, vendors, spare parts, temporary hoses, bypasses, maintenance strategy, or operating envelope can alter risk. A screening process should distinguish true replacement in kind from changes that merely look familiar. Cumulative small changes also deserve attention because their interaction can move the plant far from the analyzed configuration ([5] [11]).

Pre-startup safety review is the final verification before hazardous material is introduced into a new or significantly modified process. OSHA requires confirmation that construction matches design, procedures are in place and adequate, PHA recommendations are resolved or implemented as required, management-of-change obligations are met, and operator training is complete. The review is a field assurance activity, not a paperwork signature: discrepancies must be corrected or explicitly controlled before startup ([1] [2]).

### Procedures, competence, contractors, and operational discipline

Operating procedures translate the safety basis into repeatable action for startup, normal operation, temporary operation, emergency shutdown, emergency operation, normal shutdown, and startup after turnaround or emergency shutdown. They should state operating limits, consequences of deviation, corrective steps, safety-system functions, chemical hazards, control measures, and safe work practices. Procedures require periodic certification and update when change alters the work ([1] [2]).

Competence is demonstrated ability, not attendance at training. Operators and maintainers need the process model, hazards, limits, alarms, safeguards, abnormal-situation response, and practical skills for their tasks. Exercises and field observation can test whether procedures are usable under realistic conditions. Contractor controls are equally important because contractors may perform intrusive maintenance and turnaround work while being less familiar with site-specific hazards; host and contract employers have reciprocal duties to exchange hazard information and enforce safe practices ([1] [5]).

Operational discipline means carrying out safety-critical activities as designed while preserving a questioning attitude when conditions do not fit expectations. It includes shift handover, log quality, alarm response, permit control, line identification, independent verification, housekeeping around critical equipment, and stop-work authority. Discipline should not be reduced to blaming individuals. Leaders must provide staffing, time, tools, maintainable designs, current documents, and incentives that make the safe action practical ([5] [12] [13]).

### Learning, indicators, audits, and governance

Incident investigation should examine events that caused or could reasonably have caused catastrophic release. OSHA requires timely initiation, a knowledgeable team, documentation of contributing factors and recommendations, and a system to resolve findings. OECD guidance emphasizes underlying technical, human, and organizational causes, a factual chronology, discounted hypotheses, and dissemination of lessons rather than stopping at the immediate error ([1] [11]).

Near misses and weak signals are valuable because catastrophic events are sparse. Repeated alarm floods, demands on trips, excursions beyond safe limits, loss-of-containment events below reporting thresholds, overdue tests, open PHA actions, uncontrolled temporary changes, and impaired safety-critical equipment can reveal declining control before disaster. Their meaning depends on exposure and context; a falling report count may indicate improvement or suppressed reporting ([10] [17]).

API RP 754 organizes process safety indicators into four tiers. Tiers 1 and 2 are lagging loss-of-primary-containment measures suitable for public reporting, while Tiers 3 and 4 support facility-level monitoring of challenges to safety systems and operating discipline. HSE recommends selecting a manageable set of leading and lagging indicators tied to the facility's most important risk-control systems. The useful question is whether critical controls are present and effective, not how many activities were completed ([9] [10]).

Audits and management review close the loop. Audits test implementation through records, field conditions, interviews, and sampling across interconnected elements. Management review examines trends, unresolved risk, resource constraints, barrier impairments, and whether previous corrective action worked. Governance is strongest when leaders receive both lagging outcomes and forward-looking barrier-health evidence, ask how uncertainty is handled, and protect technical challenge from production pressure ([5] [13] [16]).

## Evidence

### BP Texas City: personal safety did not measure process risk

On March 23, 2005, explosions and fire at BP's Texas City refinery killed 15 people and injured many others during startup of an isomerization unit. The CSB investigation reconstructed the startup, equipment behavior, control-room information, work environment, and organizational history. It found deficiencies extending beyond the immediate overfilling and release: startup procedures and training were weak, instrumentation and equipment design were deficient, warnings from prior events were not effectively incorporated, and leadership and resource decisions had degraded process safety ([12]).

The case is especially important because performance signals were misleading. BP emphasized personal injury statistics and achieved improvement in those measures, but the CSB and Baker Panel found serious weaknesses in major-accident prevention. The independent panel used interviews, refinery visits, document review, workforce surveys, and comparisons across five U.S. refineries. It concluded that BP's system did not effectively measure and monitor process-safety performance and recommended stronger leadership, expertise, accountability, leading and lagging indicators, audits, and board oversight ([12] [13]).

The finding is not that personal safety is unimportant. It is that the causal chains differ. A program can reduce routine injuries while corrosive circuits, overfill protection, relief arrangements, alarm systems, startup procedures, and safety culture deteriorate. Process-safety indicators must therefore be tied to loss-of-containment events, demands on safeguards, excursions, overdue critical work, and management-system health. Texas City provides empirical evidence against using one convenient metric as a proxy for a different hazard class ([9] [10] [12] [13]).

### Tesoro Anacortes: listed safeguards were not demonstrated safeguards

An April 2010 heat-exchanger rupture and fire at the Tesoro Anacortes refinery killed seven workers. The CSB combined metallurgical examination, process and maintenance records, PHA history, standards review, and organizational analysis. It identified high-temperature hydrogen attack in carbon steel and found that prior PHAs had cited broad, judgment-based safeguards without evaluating or documenting their effectiveness ([14]).

This case tests the quality of hazard analysis directly. A safeguard entry in a worksheet can create an appearance of control even when its mechanism, performance standard, independence, or reliability has not been established. If inspection is credited, the team must show that the method can detect the relevant damage mechanism before failure, that locations and intervals are adequate, and that results trigger action. If operating limits are credited, measurement, alarm, response time, and enforcement need evidence. Tesoro demonstrates that counting safeguards is not equivalent to assessing barrier performance ([6] [14]).

The incident also illustrates the need to connect external technical knowledge with site decisions. Damage-mechanism guidance and operating experience must enter process safety information, PHA revalidation, inspection planning, and management of change. A program organized into administrative elements can miss risk at the boundaries between metallurgy, process engineering, inspection, and operations. Barrier ownership should span those boundaries and make unresolved assumptions visible ([5] [14]).

### Chevron Richmond: knowledge without implementation did not control corrosion

In August 2012, severely thinned carbon-steel piping in Chevron's Richmond refinery ruptured and released hot hydrocarbon process fluid, producing a large vapor cloud and fire. The CSB used physical evidence, corrosion and metallurgy analysis, company technical records, PHA and management-of-change records, inspection history, and interviews. It found missed opportunities to recognize sulfidation-corrosion risk and implement more corrosion-resistant materials and stronger damage-mechanism review ([15]).

The case shows the difference between information and control. Technical personnel had produced knowledge and recommendations, but organizational processes did not reliably convert them into broad preventive action. Local thickness calculations and inspection practices did not compensate for incomplete understanding of variability in the piping circuit. The CSB consequently emphasized documented damage-mechanism hazard reviews, effective analysis of safeguards, and consideration of inherently safer systems ([15]).

For hazard analysis, the lesson is that recommendations require decision quality and closure evidence. A rejected or narrowed recommendation should state assumptions, alternatives, residual risk, decision authority, and future review triggers. For mechanical integrity, the lesson is that measured thickness has meaning only inside a defensible degradation model. For management of change, the lesson is that material upgrades and work-scope decisions must be examined across the affected system rather than only at the failed component ([4] [7] [15]).

### Macondo: multiple barriers failed as a managed system

The 2010 Macondo well blowout and Deepwater Horizon explosion killed 11 people, injured others, and caused extensive environmental damage. The CSB investigation examined technical evidence, test interpretation, blowout-preventer performance, human and organizational factors, barrier management, indicators, governance, and regulatory systems. It found that barriers intended to prevent, control, or mitigate the blowout were improperly designed for conditions, constructed, tested, maintained, interpreted, or available, and that management systems did not ensure their effectiveness ([16]).

Macondo is evidence for treating safety-critical elements as a system rather than as isolated equipment. A barrier requires a defined function and performance requirements for functionality, availability, reliability, survivability, and interaction with other systems. The investigation also showed that human actions can be safety-critical barriers whose success depends on clear indications, valid test criteria, time, training, and organizational conditions. Calling such actions "operator response" without analyzing these dependencies overstates protection ([16]).

The event further supports real-time and slow-moving indicators. Equipment status, test anomalies, barrier availability, and operational deviations can guide immediate decisions; overdue actions, competence gaps, maintenance deferrals, and governance weaknesses develop over longer periods. Both types matter. A lagging count of completed incidents cannot tell a crew whether a critical barrier is currently degraded, while a dashboard of current status cannot replace learning from systemic trends ([10] [16] [17]).

### Research on effective management systems

Behie and colleagues reviewed process-safety-management practice and major-accident lessons to identify recurring weaknesses and improvement opportunities in operating facilities. Their synthesis connects leadership decisions, competence, communication, process knowledge, management of change, pre-startup review, incident learning, barrier monitoring, and leading indicators. They argue that data on safety-system challenges, bypasses, management-of-change performance, planned work on critical components, and other barrier-health variables can support proactive dashboards ([17]).

This literature does not prove that any single PSM architecture eliminates accidents. Facilities, technologies, regulatory regimes, and reporting quality differ, while catastrophic events are infrequent and hard to use for simple statistical comparison. The evidence is stronger at the mechanism level: major investigations repeatedly identify inaccurate process knowledge, ineffective hazard studies, weak barrier assurance, uncontrolled change, mechanical-integrity gaps, poor learning, and distorted performance signals. Independent official investigations across refining and offshore operations provide convergent evidence despite different initiating mechanisms ([12] [14] [15] [16] [17]).

The author's synthesis is that effective PSM should be evaluated as a control loop. It must identify scenarios, implement risk reduction, verify barrier health, detect deviations, learn from events, and correct assumptions. A facility may have all required documents yet have an open loop if actions are not closed, field configuration diverges from records, barrier impairments are tolerated, or management review does not change priorities. Evidence from the cases supports testing these connections rather than scoring administrative completeness alone ([5] [10] [12] [14] [15] [16]).

## Implications

### For designers and project teams

Process safety begins before detailed design. Project teams should define hazardous inventories and energy sources, identify credible major-accident scenarios, and apply inherent-safety options while layout, chemistry, materials, capacity, and process conditions remain flexible. Later protective layers are still necessary, but early hazard elimination avoids lifelong dependence on inspection, instrumentation, procedures, and emergency response. Design reviews should preserve rejected alternatives and assumptions so future teams can revisit them when technology or context changes ([7] [11]).

Hazard analysis should develop with design maturity. Early reviews compare concepts and site choices; later HAZOP or equivalent studies examine detailed flows, controls, safeguards, and human interfaces; LOPA or quantitative methods address scenarios needing clearer risk decisions. Recommendations must feed specifications, drawings, control narratives, safety requirements, inspection plans, procedures, training, and commissioning tests. The pre-startup review then confirms the built plant and operating organization match the safety basis ([1] [4] [6] [8]).

Projects should treat safety-critical barriers as deliverables. Each needs a function, performance standard, design basis, verification method, maintenance strategy, owner, and impairment response. For an instrumented trip, that includes the initiating condition, set point, process safety time, sensor and final-element design, integrity target, proof-test interval, bypass controls, and validation. For passive containment, it includes capacity, compatible materials, drainage, inspection, and assumptions about simultaneous events. This makes later asset management possible ([6] [8] [16]).

### For operations, maintenance, and asset managers

Operating organizations should make the safety basis usable at the point of decision. Shift teams need clear limits, alarm priorities, abnormal-response guidance, and current barrier status. Maintenance planners need to know which tasks preserve safety-critical functions and what operational restrictions apply when work is overdue. Asset managers need a visible register of degraded barriers, temporary repairs, overdue tests, open hazard-study actions, and changes awaiting permanent resolution ([5] [10] [16]).

Mechanical-integrity programs should begin with credible damage mechanisms and consequences, not generic intervals. Process data, inspection findings, leak history, material verification, and operating excursions should update risk models. When evidence contradicts assumptions, the response is not merely to add another inspection point: teams should reconsider materials, operating conditions, inventory, isolation, detection, and replacement. Corrosion and degradation expertise must participate in PHA and change decisions where loss of containment is credible ([1] [14] [15]).

Turnarounds and startups are tests of system integration. Large contractor populations, opened equipment, temporary systems, simultaneous work, modified lineups, and schedule pressure create conditions unlike normal operation. A controlled process links scope changes to hazard review, verifies equipment and instruments, resolves findings, restores documentation, removes temporary connections, trains affected workers, and conducts field walkdowns before introducing hazardous material ([1] [2] [5]).

### For leadership and boards

Senior leaders cannot govern major-accident risk using personal injury rates and audit completion percentages alone. They need a concise picture of top scenarios, critical barriers, current impairments, overdue risk-reduction actions, significant changes, loss-of-containment events, and recurring challenges to protection systems. Indicators should lead to decisions: additional resources, reduced throughput, repair, design change, independent review, or shutdown when required ([9] [10] [13]).

Governance should protect technical independence. Hazard-study teams, inspectors, operators, and engineers need escalation paths when production, cost, or schedule pressure conflicts with barrier requirements. Decisions to reject recommendations or continue with degraded protection should identify accountable authority, technical basis, residual risk, duration, compensating measures, and review date. This does not remove managerial judgment; it makes the judgment explicit and auditable ([5] [11] [13]).

Leadership also sets reporting quality. Near-miss and concern reporting declines when workers expect blame or inaction. A learning system distinguishes accountability for deliberate violations from analysis of error-producing conditions, closes feedback to reporters, and checks whether corrective actions changed the system. OECD guidance and major investigations support attention to underlying technical, human, and organizational causes rather than stopping at the last person who touched the equipment ([11] [12] [16]).

### For regulators, emergency planners, and communities

Regulation establishes a floor and common language, but a covered-process boundary is not a physical risk boundary. Owners of hazardous systems should apply the engineering principles according to credible consequences even where a listed chemical, quantity, industry, or jurisdiction does not trigger a particular rule. Regulators can test effectiveness by tracing a sample scenario from process information through hazard analysis, recommendation closure, barrier testing, change records, field condition, indicators, and emergency planning ([1] [3] [5]).

Emergency preparedness cannot compensate for preventable design weakness, yet it remains an essential mitigating layer. Facility and public plans should use credible release scenarios, identify notification and command arrangements, account for responder hazards and equipment compatibility, and exercise communication with affected communities. OECD guidance calls for coordinated onsite and offsite planning and timely, factual public information during and after an accident ([11]).

Communities need information proportionate to their role without creating false precision. Worst-case and alternative scenarios describe planning envelopes, not predictions of exactly what will happen. Transparent communication should explain hazards, protective actions, warning systems, and uncertainties. It should also incorporate environmental and infrastructure interdependencies: a release can disable roads, power, water, communications, or emergency access that the response plan assumes will remain available ([3] [11]).

### For analysts and assurance functions

Auditors should test vertical and horizontal coherence. Vertical testing starts with a major scenario and follows each credited barrier into design records, test procedures, field condition, defects, bypasses, and performance indicators. Horizontal testing examines a management element across units, such as whether every change updates process information, procedures, training, and hazard analysis. This is more informative than confirming that forms contain required signatures ([1] [5] [10]).

Quantitative risk results should be presented with assumptions and sensitivity. Initiating frequencies and barrier failure probabilities are estimates derived from data, expert judgment, and management-system conditions. Correlation, common-cause failure, human dependence, and uncertainty can dominate the result. LOPA's order-of-magnitude structure is useful precisely because it disciplines scenario decisions without pretending to provide more resolution than the inputs support ([6]).

Independent review is especially valuable where consequence is extreme, technology is novel, evidence is disputed, or the organization has strong schedule pressure. Reviewers should examine whether the scenario set is complete, methods fit the problem, safeguards qualify for credit, recommendation closure is technically defensible, and residual risk is understood by the decision maker. Independence does not substitute for line ownership; it supplies challenge where familiarity and incentives can narrow attention ([4] [5] [13]).

### A practical operating model

The author's synthesis is a seven-step operating model. First, maintain an accurate model of chemicals, process, equipment, people, and environment. Second, identify credible scenarios across the lifecycle and operating modes. Third, eliminate or moderate hazards where feasible. Fourth, specify independent preventive and mitigating barriers for residual risk. Fifth, convert barrier assumptions into inspection, testing, procedures, competence, and impairment rules. Sixth, control every change and verify readiness before startup. Seventh, learn through indicators, near misses, incidents, audits, and management review ([1] [5] [7] [10] [11]).

The single worst outcome is a catastrophic scenario that the organization believed was controlled but whose credited barriers were unavailable, dependent, degraded, or never capable of the claimed function. Preventing that outcome requires evidence at the barrier, not confidence at the program level. A process-safety system is therefore healthy when it can state what must not happen, show which independent provisions prevent it, demonstrate that those provisions work now, and act before degraded protection becomes an accident path ([6] [14] [15] [16]).

## Sources

1. Occupational Safety and Health Administration. "29 CFR 1910.119 -
   Process Safety Management of Highly Hazardous Chemicals."
   https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.119 [high]

2. Occupational Safety and Health Administration. "Process Safety
   Management," OSHA 3132.
   https://www.osha.gov/sites/default/files/publications/OSHA3132.pdf [high]

3. Electronic Code of Federal Regulations. "40 CFR Part 68 - Chemical
   Accident Prevention Provisions."
   https://www.ecfr.gov/current/title-40/chapter-I/subchapter-C/part-68 [high]

4. U.S. Department of Energy. "Chemical Process Hazards Analysis,"
   DOE-HDBK-1100-2004, reaffirmed 2022.
   https://www.energy.gov/sites/default/files/2026-05/DOE-HDBK-1100-2004.pdf [high]

5. Center for Chemical Process Safety. "Risk Based Process Safety."
   https://www.aiche.org/sites/default/files/docs/summaries/rbps.pdf [high]

6. Center for Chemical Process Safety. "LOPA Data."
   https://www.aiche.org/ccps/resources/tools/lopa [high]

7. Hendershot, D. C. (2012). "Inherently Safer Design: The Fundamentals."
   Chemical Engineering Progress.
   https://www.aiche.org/sites/default/files/cep/20120140-1.pdf [high]

8. International Electrotechnical Commission. "IEC 61511-1:2016,
   Functional Safety - Safety Instrumented Systems for the Process
   Industry Sector."
   https://webstore.iec.ch/en/publication/24237 [high]

9. American Petroleum Institute. "Recommended Practice 754: Process
   Safety Performance Indicators for the Refining and Petrochemical
   Industries," third edition, 2021.
   https://www.api.org/oil-and-natural-gas/health-and-safety/refinery-and-plant-safety/process-safety/process-safety-standards/rp-754 [high]

10. UK Health and Safety Executive. "Developing Process Safety Indicators:
    A Step-by-Step Guide for Chemical and Major Hazard Industries,"
    HSG254.
    https://www.hse.gov.uk/pubns/books/hsg254.htm [high]

11. Organisation for Economic Co-operation and Development. "OECD Guiding
    Principles for Chemical Accident Prevention, Preparedness and
    Response - Third Edition" (2023).
    https://doi.org/10.1787/162756bf-en [high]

12. U.S. Chemical Safety and Hazard Investigation Board. "BP America
    Refinery Explosion: Final Investigation Report" (2007).
    https://www.csb.gov/file.aspx?DocumentId=5596 [high]

13. BP U.S. Refineries Independent Safety Review Panel. "The Report of the
    BP U.S. Refineries Independent Safety Review Panel" (2007).
    https://www.csb.gov/assets/1/20/baker_panel_report1.pdf?13842 [high]

14. U.S. Chemical Safety and Hazard Investigation Board. "Tesoro Anacortes
    Refinery Fatal Explosion and Fire: Final Investigation Report" (2014).
    https://www.csb.gov/file.aspx?DocumentId=5851 [high]

15. U.S. Chemical Safety and Hazard Investigation Board. "Chevron Richmond
    Refinery Pipe Rupture and Fire: Final Investigation Report" (2015).
    https://www.csb.gov/file.aspx?documentid=5917 [high]

16. U.S. Chemical Safety and Hazard Investigation Board. "Macondo
    Investigation Report, Volume 1" (2014).
    https://www.csb.gov/file.aspx?DocumentId=5930 [high]

17. Behie, S. W., Halim, S. Z., Efaw, B., and O'Connor, T. M. (2020).
    "Guidance to Improve the Effectiveness of Process Safety Management
    Systems in Operating Facilities." Journal of Loss Prevention in the
    Process Industries, 68, 104257.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC7409999/ [high]

18. International Labour Organization. "Prevention of Major Industrial
    Accidents: An ILO Code of Practice" (1991).
    https://www.ilo.org/resource/prevention-major-industrial-accidents [high]

## See Also

- `library/engineering-infrastructure/reliability-engineering-failure-analysis.md` -- methods for modeling, diagnosing, and reducing equipment and system failure.
- `library/engineering-infrastructure/corrosion-and-materials-degradation.md` -- damage mechanisms and material-loss processes that mechanical-integrity programs must control.
- `library/engineering-infrastructure/manufacturing-systems-industrial-engineering.md` -- production-system design, operational control, and continuous improvement around industrial work.
- `library/engineering-infrastructure/systems-engineering-complex-systems-under-constraints.md` -- lifecycle requirements, interfaces, verification, and trade-offs in complex engineered systems.
