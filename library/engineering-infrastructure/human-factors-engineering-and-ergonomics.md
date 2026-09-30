---
name: human-factors-engineering-and-ergonomics
id: 20260930T040452Z
tier: library-topic
domain: engineering-infrastructure
author: Librarian
tags: [human-factors-engineering, ergonomics, human-systems-integration, anthropometry, cognitive-workload, error-tolerant-design, usability, safety-engineering]
links: [library/engineering-infrastructure/systems-engineering-complex-systems-under-constraints.md, library/engineering-infrastructure/process-safety-management-and-hazard-analysis.md, library/engineering-infrastructure/reliability-engineering-failure-analysis.md, library/engineering-infrastructure/manufacturing-systems-industrial-engineering.md, library/communication/information-architecture-and-content-design.md]
---

# Human Factors Engineering -- Physical Systems Work Reliably Only When Designed for Human Capabilities and Limits

Human factors engineering and ergonomics apply evidence about people to the design of equipment, workplaces, controls, procedures, and organizations so that the whole system can perform safely and effectively. The central claim is that human performance is not a fixed input: geometry, information, workload, fatigue, maintenance access, organizational conditions, and feedback can either support reliable action or systematically create error and injury [1][2][3]. Designing the work around the real user population, then testing representative people in realistic tasks, is therefore an engineering obligation rather than a cosmetic improvement [3][4][10].

## Background

### From fitting workers to machines toward designing whole systems

The International Ergonomics Association defines human factors and ergonomics as both a scientific discipline concerned with interactions among humans and other system elements and a profession that applies theory, data, principles, and methods to design for human well-being and overall system performance [1]. The two names are commonly used interchangeably, although particular traditions may emphasize physical work, engineering psychology, or system design. The shared object is the human-system fit: whether a person can perceive the relevant state, understand it, reach and operate what is needed, sustain the required workload, recover from error, and complete the task under the conditions in which the system will actually be used [1][2].

That object is broader than comfort. Physical ergonomics concerns anatomy, anthropometry, physiology, and biomechanics; cognitive ergonomics concerns perception, memory, reasoning, attention, decision making, workload, and motor response; organizational ergonomics concerns roles, communication, schedules, teamwork, and work design [1][15]. These dimensions interact. A valve may be physically reachable but difficult to identify; an alarm may be visible but one of hundreds competing for attention; a procedure may be accurate but impossible to use while wearing protective equipment; a maintainable component may become inaccessible after adjacent equipment is installed. Human factors engineering treats those interactions as properties of the designed system rather than as separate defects to be assigned to the worker [2][18].

Human systems integration extends that reasoning across the engineering lifecycle. NASA defines a system for this purpose as an integration of hardware, software, humans, data, and processes, and includes owners, operators, maintainers, assemblers, logistics personnel, trainers, testers, and other people who affect or use it [2]. The inclusion of maintainers and support personnel is consequential. A machine that performs well for its nominal operator but requires unsafe lifting, hidden fasteners, ambiguous isolation, or impossible inspection access is not well integrated. Human considerations must enter the concept of operations, requirements, architecture, procurement, detailed design, verification, validation, operation, modification, and retirement rather than being checked after the physical arrangement has become expensive to change [2][3][18].

Human factors engineering belongs in engineering-infrastructure when it governs physical systems and their lifecycle performance. It uses findings from psychology, physiology, biomechanics, occupational health, and design research, but its output is an engineered requirement, configuration, control, procedure, test, or operating constraint [1][3]. Pure research into cognition belongs elsewhere unless it is translated into system design. Software-only interaction design is also outside this topic's center, although software displays are in scope when they control or communicate the state of physical equipment. The defining boundary is the designed relationship among people, equipment, facilities, work, and operating conditions [1][2].

### Accidents made the hidden design problem visible

High-consequence accidents exposed the weakness of treating the operator as an adaptable component. The U.S. Nuclear Regulatory Commission's investigation of the 1979 Three Mile Island Unit 2 accident examined control-room design, operator activity, training, emergency procedures, and the application of human factors criteria. It found required information that was missing, poorly located, ambiguous, or hard to read, and concluded that the human errors in the event arose from inadequacies in equipment design, information presentation, emergency procedures, and training rather than from operator deficiencies alone [12]. The subsequent regulatory response institutionalized detailed control-room reviews and human-system interface guidance; the current NUREG-0700 covers displays, interactions, alarms, automation, procedures, workstations, workplaces, communication, and degraded conditions [5][12].

Aviation, spaceflight, defense, transport, and process industries developed comparable standards because operators and maintainers must act in dynamic systems with incomplete time, limited attention, and serious consequences. FAA requirements call for human factors engineering during analysis, design, development, testing, and in-service management, including task analysis, function allocation, mockups, prototypes, verification, and validation [3][4]. NASA's guidance similarly treats usability, workload, and design-induced error as measurable properties to be evaluated through representative human-in-the-loop testing [10][18]. These practices do not imply that every project requires a nuclear-control-room program. They establish a scalable principle: the rigor of analysis and testing should rise with novelty, complexity, irreversibility, and the consequence of a poor human-system fit [3][4][18].

### The design population is not an average person

Anthropometry illustrates why informal intuition fails. NIOSH defines anthropometry as measurement of human size, form, and functional capacity and uses it to study fit among workers, tasks, tools, vehicles, machines, and protective equipment [7]. Workforces differ by occupation, sex, age, body composition, disability, clothing, protective equipment, and population. NIOSH warns that much available workplace design data historically came from military samples that do not represent the variability of general industrial populations [7]. The U.S. Access Board reached the related conclusion that anthropometric data must be appropriate to the design and descriptive of the target user population, especially where disability changes reach, clearance, posture, or mobility-aid use [17].

The historical movement of the field is therefore from correction after injury or accident toward prospective integration. The earlier a team defines users, tasks, environments, abnormal states, and human performance constraints, the more design alternatives remain reversible. HSE guidance states that early attention to ergonomics generally produces better results and calls for both human factors expertise and participation by people who understand the work [14]. The author's synthesis is that the field's durable contribution is not a catalog of ideal dimensions. It is a lifecycle method for converting variability in human capability and operating context into explicit engineering decisions and evidence [2][3][14].

## Core Concepts

### Design for a population, a task, and an operating condition

A human factors requirement must identify who is expected to perform what task under which conditions. Designing for an undefined "user" hides the variables that govern fit. The target population may include small and large bodies, limited mobility, reduced strength, color-vision differences, hearing protection, gloves, respirators, cold-weather clothing, pregnancy, aging, temporary injury, or unfamiliar emergency responders. The relevant body dimension also depends on the task: a large body may govern clearance, while a small body may govern reach; eye height may govern sight lines, hand breadth may govern tool clearance, and strength rather than stature may govern manual force [7][17].

Percentiles should not be applied as a universal recipe. A design that accommodates a range for one body dimension does not necessarily accommodate the same people for another dimension because body measures are not perfectly correlated. Static dimensions also do not capture joint motion, balance, force, clothing, tool use, or the space needed to perform a sequence. The appropriate process is to define the exclusion consequence, select data from a representative population, model the task, provide adjustability where feasible, and test actual or representative users. Digital human models can screen reach, line of sight, posture, and clearance, but physical trials remain necessary where contact forces, movement strategies, visibility, protective equipment, or emergency speed matter [7][17][19].

Accessibility is not a separate concession after ordinary ergonomics. It is evidence that the design population was initially specified too narrowly. The Access Board's research found that data drawn from specialized or military populations could not simply stand in for people with diverse disabilities, and its design standards convert some accessibility needs into enforceable dimensions and routes [17]. The author's synthesis is that inclusive design strengthens ordinary engineering: it forces explicit treatment of variability, alternative modes, clearances, forces, feedback, and failure recovery that average-person design leaves implicit [17].

### Physical workload joins biomechanics to exposure

Physical ergonomics examines how force, posture, repetition, duration, vibration, contact stress, environmental conditions, and recovery affect performance and injury risk. NIOSH identifies lifting, pushing, pulling, carrying, awkward posture, vibration, cold, intensity, frequency, duration, and psychosocial stressors as contributors to work-related musculoskeletal disorders [6]. None of these factors should be reduced to a single maximum load. A light object lifted frequently at long horizontal reach can create substantial cumulative demand; a heavy object close to the body may be manageable with mechanical assistance; a nominally acceptable force may become unsafe when grip, footing, visibility, or recovery time is poor [6][8].

The Revised NIOSH Lifting Equation demonstrates how human factors turns this complexity into a bounded decision aid. It combines object weight with horizontal and vertical hand locations, travel distance, asymmetry, frequency, duration, and coupling quality to calculate a recommended weight limit and lifting index for defined two-handed lifting tasks [8]. NIOSH recommends a lifting index or composite lifting index at or below 1.0, while also directing users to an ergonomics program rather than treating the equation as a complete workplace assessment [8]. Its scope limits matter: an equation for specified lifting tasks cannot validate one-handed handling, unstable loads, patient transfers, unusual populations, poor floors, heat stress, or every sequence of variable work without additional analysis [8][9].

Engineering controls generally dominate instructions because they alter the demand. Hoists, lift tables, counterbalances, conveyors, adjustable work heights, better grips, reduced reach, smaller containers, access platforms, and redesigned service points can remove force or posture at the source. Administrative controls such as rotation, work-rest scheduling, or training can supplement the design, but they depend on continuing compliance and may redistribute exposure rather than eliminate it [6][14]. The author's assessment is that the worst physical-design error is to define a foreseeable task that exceeds human capability and then call safe execution a matter of technique.

### Task analysis converts work into design requirements

Task analysis identifies the actions, information, decisions, tools, timing, environment, interfaces, dependencies, and possible errors required to achieve a goal. It begins with the concept of operations and covers normal operation, startup, shutdown, inspection, maintenance, abnormal conditions, emergencies, restoration, and retirement as applicable [2][3]. The output is not merely a procedure draft. It supplies requirements for displays, controls, access, staffing, automation, training, communications, protective equipment, lighting, documentation, and verification [3][18].

A useful task analysis records the goal, trigger, prerequisites, sequence, concurrent work, information required, decisions, feedback, completion criteria, hazards, time limits, physical demand, cognitive demand, communication, likely errors, and recovery paths. Critical tasks deserve deeper analysis because failure has high consequence, because time or workload is tight, or because the action is infrequent and therefore poorly practiced. FAA requirements explicitly call for evaluating task timing, sequencing, simultaneity, criticality, accuracy, decision making under uncertainty, and learning or performance difficulty [3]. The result should be traceable: if a task requires diagnosis within two minutes while wearing gloves and hearing protection, the design and test plan must preserve those conditions.

Function allocation decides what people, automation, or a team should do. Allocation is not a contest in which automation receives everything technically possible and people receive the remainder. Automation excels at rapid calculation, stable repetition, monitoring specified thresholds, and applying consistent logic; people can reframe goals, recognize novel context, integrate weak signals, improvise, and make value-laden judgments. Both can fail. Allocation must address authority, information, mode awareness, handover, fallback, workload during normal and abnormal states, maintenance, and the skills that atrophy when a function is rarely practiced [2][3][13].

### Perception, attention, workload, and situation awareness constrain control

A control system can contain the correct data while failing to present usable information. Human attention is selective, working memory is limited, and perception depends on contrast, timing, expectation, sensory conditions, and competing signals. Situation awareness research describes a progression from perceiving relevant elements, through comprehending their meaning, to projecting how the situation may develop. Endsley's model connects those stages to attention, working memory, goals, mental models, workload, stress, complexity, automation, and interface design [16]. The model is influential but not a substitute for measurement; reviews note continuing debate about how situation awareness should be measured [16].

Workload must be treated as a relation between task demands, available time, user capability, support, and system state. Excessive workload can create omission, fixation, rushed diagnosis, and loss of overview. Workload that is too low can reduce vigilance and engagement, especially when automation performs routine control but demands rapid intervention after a rare failure. A design review should therefore examine demand across time rather than quote one average. Peak concurrent tasks, alarm bursts, mode changes, communications, manual fallback, and recovery from interruption often govern performance [3][5][10].

Fatigue changes the available capability. NIOSH reports that nonstandard schedules, extended hours, stress, demanding tasks, and heat can contribute to fatigue, and that fatigue can slow reaction, reduce attention and concentration, limit short-term memory, and impair judgment [11]. These effects cannot be engineered away by a clearer display alone. Staffing, shift design, break opportunities, environmental conditions, commute risk, call-outs, and workload are system variables. Training a worker to "manage fatigue" without examining schedules and operating demands transfers a design responsibility to the individual [11][15].

### Displays, controls, and alarms must support the task

A human-system interface should reveal the system state, the significance of change, available actions, action consequences, and whether the action succeeded. NUREG-0700 requires consistency with user conventions, clear titles and identifiers, task-related grouping, manageable navigation, appropriate ranges, and designs that reduce memory demands across pages [5]. These are not aesthetic preferences. They reduce the translation required between a user's task model and the physical or digital representation of the plant [5].

Controls should be identifiable, reachable, operable in the expected posture and protective equipment, resistant to inadvertent activation, and compatible with the direction and magnitude of system response. Displays and controls that belong to one task should be spatially or logically integrated. Feedback should be timely and distinguish command acceptance from achieved physical state; a lit command button does not prove that a valve moved. Critical status should not depend on color alone, and labels should use the terms found in procedures and training [4][5].

Alarms are requests for attention and action, not a list of every parameter excursion. An effective alarm identifies a condition that matters, is prioritized by consequence and urgency, distinguishes itself without masking communication, supports diagnosis, and provides or links to the expected response. Alarm flooding destroys those properties by presenting more signals than the operator can interpret during the event that most requires discrimination. NRC guidance addresses alarm selection, setpoints, processing, filtering, suppression, organization, coding, content, and controls because each affects whether an alarm supports rather than competes with situation awareness [5].

### Error tolerance is designed before error occurs

Human error is an outcome description, not a root cause. A slip, lapse, mistaken diagnosis, rule misapplication, or deliberate deviation can arise through different mechanisms and therefore requires different controls. Good design prevents foreseeable errors where possible, makes the safe action easy, makes incompatible states difficult, detects errors quickly, contains their effects, preserves evidence, and provides a clear recovery path. NASA treats design-induced error as a measurable verification concern and sets a goal of zero observed catastrophic design-induced errors in the cited spaceflight guidance [10].

Error-tolerant design includes forcing functions, interlocks, guarded or differentiated controls, confirmation for consequential actions, reversible intermediate states, independent indications, limits that preserve a safe envelope, and graceful degradation. It also includes procedures matched to actual equipment, diagnostic information that distinguishes competing hypotheses, and layouts that allow a maintainer to verify isolation before contact. Redundancy can help only if the channels are sufficiently independent and if added complexity does not create new confusion or common-cause failure [5][10].

Blaming an operator prevents this learning. The relevant question is not merely why the person acted, but why the action made sense from the information, goals, time pressure, training, interface, and organizational conditions then present. This does not remove individual accountability for deliberate misconduct. It prevents a convenient label from closing the investigation before the controllable design and management conditions are identified [12][14].

### Human factors is an iterative evidence process

Standards provide accumulated design knowledge, but compliance with a dimensional table or interface checklist does not validate the integrated task. The lifecycle begins with users, work, environments, hazards, and operating experience; converts these into requirements and design concepts; evaluates alternatives through analysis, prototypes, and mockups; and verifies and validates the integrated system with representative users, tasks, procedures, equipment, and conditions [2][3][10]. Each cycle should produce traceable findings, design decisions, unresolved risks, and retest criteria.

Prototype fidelity should match the question. A paper layout can test grouping and sequence; a digital prototype can test navigation and information; a full-scale mockup can test reach, clearance, sight lines, ingress, and teamwork; a simulator can test timing, workload, alarms, mode transitions, and abnormal scenarios. NASA's human-in-the-loop program uses representative hardware, software, procedures, and operational conditions, then measures errors, time, workload, usability, comments, reach, motion, and other task-relevant outcomes [10][19]. Expensive fidelity is wasteful if the question can be answered cheaply, but cheap fidelity is misleading when force, motion, protective equipment, vibration, stress, or integrated behavior governs the result.

Operational feedback completes the loop. Near misses, workarounds, repeated alarms, procedure deviations, maintenance deferrals, injury reports, support requests, and user modifications are evidence about the design. A handwritten label or improvised tool may reveal adaptation to a mismatch rather than carelessness. Field evidence should trigger bounded investigation and controlled change, with re-analysis when a modification alters tasks, staffing, interfaces, automation, or recovery [14][15]. Human factors engineering is therefore continuous configuration management of human-system assumptions, not a one-time usability approval.

## Evidence

### Epidemiology links physical exposure to musculoskeletal harm

NIOSH's 1997 critical review synthesized epidemiologic evidence on work-related disorders of the neck, upper extremity, and low back. It examined a literature that had grown to more than 6,000 scientific articles and concluded that a large body of credible research showed a consistent relationship between musculoskeletal disorders and certain physical workplace factors, particularly at higher exposure levels [6]. The strength of this source is its systematic comparison of occupational exposure and health evidence across body regions rather than reliance on laboratory plausibility alone. Its limitation is age: equipment, populations, and measurement methods have changed, and the review does not make every individual injury attributable to work. It supports the engineering proposition that repeated force, posture, vibration, and similar exposures are controllable risk factors, not that one threshold predicts every outcome [6].

The Revised NIOSH Lifting Equation provides a more focused test of exposure assessment. A 2016 review in Human Factors identified 13 studies linking lifting-index measures to adverse low-back outcomes and found a positive relationship between the lifting index or composite lifting index and the severity of low-back-pain outcomes [9]. A separate one-year prospective study evaluated the equation against incident low-back pain in workers performing manual lifting and used quantified job exposure rather than job title alone [20]. These studies do not establish a perfectly safe boundary or eliminate confounding by individual, psychosocial, and organizational variables. They provide convergent evidence that a structured biomechanical and task-based measure can discriminate risk better than an unsupported instruction to "lift safely" [8][9][20].

The design implication follows from the method. The equation requires measured hand locations, travel distance, asymmetry, frequency, duration, and coupling, so it directs attention toward variables an engineer can change. Moving a load closer, raising its origin, improving the grip, reducing frequency, or adding mechanical assistance changes the exposure model and can be verified after redesign [8]. The author's synthesis is that the strongest physical-ergonomics evidence connects a measured exposure to a health outcome and then to a controllable design variable; injury counts alone cannot identify which change will work.

### Three Mile Island showed that context creates operator performance

The NUREG/CR-1270 investigation of Three Mile Island used four complementary methods: reconstruction of the control-room design process, analysis of operator activities during the accident, evaluation of staffing and training, and application of human factors test-and-evaluation methods to lighting, labeling, workspace, controls, displays, information processing, and procedures [12]. The investigators also used a full-scale mockup to evaluate control-display and workspace relationships [12]. This method matters because it did not infer cause from the last operator action. It examined the information and physical environment in which diagnosis and control occurred.

The report found that required information was often absent, poorly located, ambiguous, or difficult to read; that the plant lacked a coherent human-machine integration concept; and that panel design created excessive movement, workload, error probability, and response time [12]. It also identified deficiencies in emergency procedures and training. Its primary conclusion was that the human errors observed during the event were not explained by operator deficiencies alone but by inadequacies in equipment design, information presentation, procedures, and training [12]. As a post-accident investigation, it cannot experimentally isolate each factor, and later analyses may refine individual causal claims. Its value is the traceable convergence of design review, task reconstruction, documentary evidence, mockup evaluation, and training analysis.

The regulatory response supplies evidence of institutional durability. NRC now uses a family of human factors review documents, including NUREG-0711 for program review and NUREG-0700 for human-system interface design, and conducts simulator research to support licensing decisions [5][21]. Revision 4 of NUREG-0700 includes detailed guidance for information displays, user interaction, alarms, automation, procedures, communication, workstations, workplaces, and degraded interface conditions [5]. This does not prove that following every guideline prevents every accident. It demonstrates that a major accident finding was converted into repeatable design and review controls rather than left as a recommendation to improve operator vigilance.

### Human-in-the-loop testing finds defects that drawings conceal

NASA's human-in-the-loop process provides prospective evidence. Its technical guidance begins with functions, tasks, error analysis, and concepts, then uses increasingly representative hardware, software, procedures, trained participants, and operational conditions to measure usability, workload, design-induced error, and operability [10]. This is a staged test method rather than a single demonstration. Early prototypes answer design questions while changes remain cheap; integrated validation tests whether the final combination of people, equipment, procedures, training, and environment supports the mission [10][18].

NASA reports concrete design changes from this process. Human-in-the-loop evaluations identified suited hand-controller interference and led to changes in controller mounts; detected display glare and led to revised light locations; informed display colors, refresh rates, backlighting, and indicator levels; and changed hatch, tunnel, restraint, stowage, and egress arrangements [19]. These are observational program cases rather than controlled trials, so they do not provide a universal effect size. They demonstrate the mechanism: interaction among body dimensions, protective equipment, vibration, lighting, geometry, and task sequence can remain invisible in drawings or isolated component tests and become observable when representative users perform the integrated task [19].

NASA's usability technical brief also reports a validation study of a modified usability scale using 35 crew-like participants who performed procedures with a better-designed and a worse-designed spacecraft power-system prototype. The modified scale discriminated between the prototypes and produced results practically equivalent to the established System Usability Scale [10]. The study concerns a measurement instrument, not mission safety directly. It shows that subjective usability can be evaluated against controlled design differences and should be combined with objective measures such as errors, timing, completion, reach, and workload [10].

### Automation accidents test function allocation and engagement assumptions

The NTSB's investigation of a 2016 collision involving partial driving automation examined vehicle performance data, driver engagement, the operational design domain, event recording, and safety metrics [13]. The investigation treated the driver and automation as one control system. Its safety questions included whether the automation could be used outside the conditions for which it was designed and whether steering-wheel interaction was an adequate surrogate for visual engagement [13]. The resulting recommendations called for safeguards that limit use to appropriate conditions and for stronger means of monitoring engagement.

This case does not imply that automation is inherently unsafe or that one vehicle architecture generalizes to industrial plants. It demonstrates a recurring human factors problem: assigning continuous supervision to a person while automation performs the routine control can create low engagement, weak feedback about system limits, and a demand for rapid recovery after a rare boundary failure [13][16]. The design must make the active mode, capability, uncertainty, operating envelope, and fallback responsibility evident; training and warnings cannot compensate for a system that predictably permits misuse while depending on immediate human rescue.

### What the evidence does and does not establish

The evidence base combines epidemiology, controlled and prospective studies, simulator work, accident investigation, standards research, and program experience. These methods answer different questions. Epidemiology links exposure patterns to population outcomes; task experiments compare designs under controlled conditions; human-in-the-loop tests reveal integrated defects; accident investigations reconstruct causal pathways; and standards consolidate evidence into reusable constraints [5][6][9][10][12]. Agreement across methods strengthens a claim, while disagreement should remain visible rather than be averaged away.

No source establishes a universal return on investment, one ideal interface, or a fixed percentage of accidents caused by human factors. Context, users, technology, task frequency, consequence, and organizational conditions differ. The defensible conclusion is narrower: measurable properties of physical and cognitive demand affect performance and health; design can change those properties; and representative evaluation can reveal mismatches before or after operation [6][9][10][12]. Human factors engineering is strongest when it states the target population and task, measures the relevant demand and outcome, records uncertainty, and verifies the effect of the intervention.

## Implications

### For requirements and systems engineering

Human factors requirements should enter the same controlled baseline as structural, electrical, hydraulic, software, reliability, and safety requirements. A requirement should state the user population, task, environment, operating mode, performance criterion, and verification method. "Easy to use" is not verifiable; "a trained maintainer wearing specified protective equipment can isolate, access, remove, replace, inspect, and restore the component within the allowed outage while maintaining required clearances and forces" can be decomposed and tested [2][3]. The exact criterion must come from the system's risk and operating need, not from a generic example.

Systems engineers should connect each human requirement to the concept of operations, task analysis, architecture, interface, hazard analysis, procedure, training, and validation scenario. Function allocation should be revisited when automation, staffing, or operating modes change. A new automatic feature can reduce routine workload while increasing monitoring demand, creating mode confusion, or eroding manual skill. A maintenance redesign can shorten replacement time while obstructing inspection. Traceability makes these cross-effects visible before local optimization becomes whole-system failure [2][3][13].

The worst design outcome is a safety- or mission-critical action that appears feasible in documentation but fails in the real configuration, under the real time pressure, with the real information and protective equipment. Prevention requires progressive evidence: analysis against representative data, task walkthroughs, prototype evaluation, full-scale fit checks, abnormal-scenario simulation, and integrated validation proportional to consequence [3][10][19]. Review gates should ask what has actually been tested, with whom, under which conditions, and which assumptions remain unverified.

### For equipment, facilities, and infrastructure design

Design teams should specify adjustability, reach, clearance, force, visibility, access, ingress, egress, labeling, environmental limits, communication, and maintenance space from representative population data. They should distinguish design limits from nominal settings and allow for clothing, tools, personal protective equipment, carried loads, and temporary configurations [7][17]. Where a single fixed geometry cannot accommodate the population, the design should provide adjustment, alternative methods, or a justified operating restriction.

Physical layout should follow task relationships. Frequently or urgently used controls and information belong within reliable reach and view; components requiring coordinated action should be grouped; unrelated or dangerous controls should be separated or differentiated; and service access should allow inspection and removal without creating new hazards. The integrated layout must include cable routes, insulation, guards, temporary lifting equipment, scaffolding, doors, stored items, and neighboring equipment rather than evaluating an isolated model [4][5][19].

Accessibility and emergency use should be design cases, not exceptions. An accessible route that exists only in nominal conditions can disappear during maintenance, crowding, smoke, power loss, or debris. Emergency controls must remain identifiable and operable under stress, low light, noise, gloves, and abnormal posture where those conditions are credible. The author's synthesis is that universal or inclusive design is best treated as resilience to human variability: it enlarges the set of people and conditions under which the asset can deliver its intended service [17].

### For controls, automation, and alarm systems

Control interfaces should minimize memory-dependent translation and expose the causal state that matters to the task. Designers should show whether a command was accepted, whether the physical equipment achieved the commanded state, what automatic mode is active, which limits are binding, and what action is expected if automation cannot continue [5]. Overview displays should preserve the relationships needed for diagnosis, while detail should remain accessible without requiring users to reconstruct the system from unrelated pages [5][16].

Alarm design should begin with operator response, not sensor availability. Every alarm should have a defined cause, consequence, priority, expected action, time available, suppression logic, and test method. Teams should analyze alarm rates during representative abnormal scenarios, not only during stable operation. The design should prevent one initiating event from producing an uninterpretable cascade and should preserve communication and overview during the disturbance [5]. Alarm performance should be monitored after commissioning because process changes and maintenance can create nuisance, stale, or hidden alarms.

Automation should be bounded by an explicit operating envelope and a credible fallback. If the human is responsible for supervision, the design must support engagement, understanding of capability and limits, detection of automation failure, and recovery within the available time. A warning that demands an impossible intervention is not a safeguard. The NTSB automation case shows why permission to activate, engagement monitoring, and operational-domain limits are design variables rather than matters of user discipline alone [13].

### For operations, maintenance, and organizational design

Operating organizations should treat fatigue, staffing, communication, competence, and procedure quality as engineered conditions. NIOSH's account of fatigue effects means that schedules and workload can directly alter reaction time, attention, short-term memory, and judgment [11]. A staffing plan should therefore be tested against peak and degraded scenarios, including simultaneous tasks, interruptions, handovers, and recovery work. Minimum headcount without task demand is not an adequate human factors justification.

Procedures should be developed from the task and tested at the point of use. They should use equipment labels, state prerequisites and completion conditions, present warnings before the hazardous action, support branching and recovery, and remain usable with the available lighting, space, displays, gloves, and communications. If experienced workers routinely skip or rewrite a step, the organization should investigate whether the procedure, interface, or task has diverged rather than assuming noncompliance is the complete cause [3][12][14].

Maintenance deserves equal status with operation. Designers should provide isolation points, test access, lifting and handling provisions, diagnostic feedback, component identification, tool space, replacement paths, safe postures, and independent confirmation before energy is restored. Maintainers often work in configurations that designers did not model: guards removed, adjacent systems live, temporary lighting, heat, contamination controls, or constrained outages. Maintenance human factors should therefore be included in mockups, task analysis, procurement reviews, and modification control [2][3].

Worker participation is evidence, not a veto or a substitute for expertise. Operators and maintainers know work as performed, including variability, informal coordination, weak signals, and adaptations that documents may omit. ILO and IEA guidance calls for full worker participation in designing systems, detecting problems, and creating solutions, within a trans-disciplinary process [15]. The engineering team remains responsible for reconciling local experience with hazards, standards, population data, and lifecycle constraints.

### For safety, reliability, and incident learning

Safety analyses should describe human actions with the same rigor applied to hardware barriers. If an operator must detect, diagnose, decide, travel, manipulate, verify, and communicate within a stated time, each dependency should be supported and tested. Crediting "operator action" without examining alarms, workload, access, procedure, staffing, environment, and recovery overstates protection [5][12]. Human reliability estimates should preserve their assumptions and should not replace direct design improvement where error can be prevented or contained.

Incident investigations should move from the immediate action to the conditions that shaped it. Questions should include what information was available, what the interface implied, which goals competed, how workload evolved, whether procedures matched the system, what training prepared the team to expect, which safeguards detected the error, and why recovery succeeded or failed [12]. The goal is not to deny agency. It is to identify changes that can prevent a different person in the same system from reaching the same state.

Operational indicators should include workarounds, alarms, overrides, repeated retraining, rejected recommendations, access problems, ergonomic symptoms, aborted maintenance, procedure edits, near misses, and user-generated labels or tools. These signals are useful only if they trigger investigation and closure. Counting completed training or design reviews does not establish fit; measured task performance and resolved field problems provide stronger evidence [10][14].

### A practical lifecycle framework

A project can apply human factors engineering through seven linked steps. First, define users, stakeholders, tasks, environments, operating modes, hazards, and lifecycle phases. Second, gather representative anthropometric, biomechanical, cognitive, organizational, and operating-experience evidence. Third, convert that evidence into traceable requirements and function-allocation decisions. Fourth, create alternatives that remove demand or error opportunity before relying on warnings, procedures, or training. Fifth, evaluate concepts iteratively with analysis, prototypes, mockups, and representative users. Sixth, verify requirements and validate the integrated system under realistic normal, abnormal, maintenance, and emergency scenarios. Seventh, monitor operation and feed field evidence through controlled change [2][3][10][15].

The framework should be tailored, not skipped. A low-consequence hand tool may need a brief task study, fit trial, and field check. A rail control center, chemical plant, medical facility, power system, aircraft, or spacecraft may need formal program management, task and error analysis, workload studies, alarm evaluation, staffing validation, high-fidelity simulation, and independent review. The criterion is evidence proportional to consequence and uncertainty [3][5][18].

The author's assessment is that human factors engineering creates lifecycle value when it prevents late redesign, injury, unusable automation, maintenance delay, operator overload, and recurrent error. That value should be demonstrated through the project's own evidence: fewer unresolved interface findings, lower measured task demand, successful representative validation, reduced exposure, faster and more reliable maintenance, and closure of operating feedback. The discipline's claim is not that humans are the center of every engineering decision. It is that any physical system dependent on human action is incomplete until the human-system relationship has been specified, designed, tested, and maintained.

## Sources

1. International Ergonomics Association. "What Is Ergonomics (HFE)?"
   https://iea.cc/about/what-is-ergonomics/ [high]

2. NASA. "NASA Human Systems Integration Handbook," NASA/SP-20210010952,
   2021. https://ntrs.nasa.gov/citations/20210010952 [high]

3. Federal Aviation Administration. "Human Factors Engineering Requirements,"
   HF-STD-004A, 2016.
   https://hf.tc.faa.gov/publications/2016-09-human-factors-engineering-requirements/HF-STD-004A.pdf [high]

4. Federal Aviation Administration. "Human Factors Design Standard,"
   HF-STD-001B, 2016.
   https://hf.tc.faa.gov/publications/2016-12-human-factors-design-standard [high]

5. U.S. Nuclear Regulatory Commission. "Human-System Interface Design Review
   Guidelines," NUREG-0700, Revision 4, 2026.
   https://www.nrc.gov/docs/ML2602/ML26022A094.pdf [high]

6. National Institute for Occupational Safety and Health. "About Ergonomics and
   Work-Related Musculoskeletal Disorders," 2024.
   https://www.cdc.gov/niosh/ergonomics/index.html [high]

7. National Institute for Occupational Safety and Health. "Anthropometry and
   Work: An Overview."
   https://www.cdc.gov/niosh/anthropometry/about/index.html [high]

8. National Institute for Occupational Safety and Health. "Revised NIOSH
   Lifting Equation."
   https://www.cdc.gov/niosh/ergonomics/about/RNLE.html [high]

9. Lu, M.-L., Putz-Anderson, V., Garg, A., and Davis, K. G. (2016).
   "Evaluation of the Impact of the Revised National Institute for Occupational
   Safety and Health Lifting Equation." Human Factors, 58(5), 667-682.
   https://pmc.ncbi.nlm.nih.gov/articles/PMC4991821 [high]

10. NASA Office of the Chief Health and Medical Officer. "Usability, Workload,
    and Error," OCHMO-TB-005, Revision C, 2023.
    https://www.nasa.gov/wp-content/uploads/2023/12/ochmo-tb-005-usability.pdf [high]

11. National Institute for Occupational Safety and Health. "Fatigue and Work,"
    2026. https://www.cdc.gov/niosh/fatigue/about/index.html [high]

12. Malone, T. B., Kirkpatrick, M., Mallory, K., Eike, D., Johnson, J. H., and
    Walker, R. W. (1980). "Human Factors Evaluation of Control Room Design and
    Operator Performance at Three Mile Island-2," NUREG/CR-1270, Volume 1.
    https://www.nrc.gov/docs/ML1930/ML19308C512.pdf [high]

13. National Transportation Safety Board. "Collision Between a Car Operating
    With Automated Vehicle Control Systems and a Tractor-Semitrailer Truck Near
    Williston, Florida, May 7, 2016," NTSB/HAR-17/02, 2017.
    https://www-d.ntsb.gov/investigations/AccidentReports/Reports/HAR1702.pdf [high]

14. UK Health and Safety Executive. "Design - Human Factors."
    https://www.hse.gov.uk/humanfactors/topics/design.htm [high]

15. International Labour Organization and International Ergonomics Association.
    "Principles and Guidelines for Human Factors/Ergonomics Design and
    Management of Work Systems," 2021.
    https://iea.cc/wp-content/uploads/2021/06/Principles-and-Guidelines_June2021.pdf [high]

16. Wickens, C. D. (2008). "Situation Awareness: Review of Mica Endsley's 1995
    Articles on Situation Awareness Theory and Measurement." Human Factors,
    50(3), 397-403. https://pubmed.ncbi.nlm.nih.gov/18689045 [high]

17. Bradtmiller, B., and Annis, J. (1997). "Anthropometry for Persons with
    Disabilities: Needs for the 21st Century." U.S. Access Board.
    https://www.access-board.gov/research/human/anthropometry-1997 [high]

18. Adelstein, B., Hobbs, A., O'Hara, J., and Null, C. (2006). "Design,
    Development, Testing, and Evaluation: Human Factors Engineering,"
    NASA/TM-2006-214535.
    https://human-factors.arc.nasa.gov/publications/NASA_TM_2006-214535.pdf [high]

19. NASA Johnson Space Center. "Human-In-The-Loop Evaluations: Evaluation to
    Optimize Design, Improve Safety and Increase Mission Success," 2023.
    https://www.nasa.gov/wp-content/uploads/2023/07/jsc-hhp-human-in-the-loop-evaluations-2023-1.pdf [high]

20. Lu, M.-L., Waters, T. R., Krieg, E., and Werren, D. (2014). "Efficacy of
    the Revised NIOSH Lifting Equation to Predict Risk of Low-Back Pain
    Associated With Manual Lifting: A One-Year Prospective Study." Human
    Factors, 56(1), 73-85.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC4634706/ [high]

21. U.S. Nuclear Regulatory Commission. "Human Factors."
    https://www.nrc.gov/reactors/operating/ops-experience/human-factors [high]

## See Also

- `library/engineering-infrastructure/systems-engineering-complex-systems-under-constraints.md` -- lifecycle requirements, interfaces, verification, and validation into which human factors work must integrate.
- `library/engineering-infrastructure/process-safety-management-and-hazard-analysis.md` -- human performance and interface conditions within major-accident prevention and barrier assurance.
- `library/engineering-infrastructure/reliability-engineering-failure-analysis.md` -- failure mechanisms, error tolerance, and systemic investigation beyond an "operator error" label.
- `library/engineering-infrastructure/manufacturing-systems-industrial-engineering.md` -- work-system design, physical flow, standardized work, and continuous operational improvement.
- `library/communication/information-architecture-and-content-design.md` -- task-oriented information structure for labels, navigation, and content presented through human-system interfaces.
