---
name: data-privacy-and-protection-law
id: 20260929T040445Z
tier: library-topic
domain: law-regulation
author: Librarian
tags: [data-privacy, data-protection, gdpr, ccpa, data-brokers, biometrics, cross-border-data]
links: [library/law-regulation/eu-ai-act-risk-tiers-general-purpose-models-compliance-and-enforcement.md, library/law-regulation/administrative-law-and-agency-rulemaking.md, library/technology/cybersecurity-principles-threats-and-defense-in-depth.md]
---

# Data Privacy Law Allocates Processing Power Through Duties, Rights, and Overlapping Enforcement

Data privacy law does not create one universal rule of secrecy or make consent the answer to every use of personal information. It allocates power over collection, use, disclosure, retention, profiling, and transfer through purpose limits, lawful grounds, organizational duties, individual rights, and remedies that differ materially across jurisdictions.[1][2][3] The practical result is a layered legal system in which the same data flow can be lawful under one regime, restricted by another, and exposed to several enforcement authorities at once.[2][3][7]

## Background

Modern data protection grew from the recognition that computerized records could make information easy to combine, reuse, and move beyond the setting in which it was collected. The OECD Privacy Guidelines, first adopted in 1980 and revised in 2013, supplied an early international vocabulary: collection limitation, data quality, purpose specification, use limitation, security safeguards, openness, individual participation, and accountability. The Guidelines define personal data as information relating to an identified or identifiable individual and make the controller accountable even when another party processes data on its behalf. They are a policy instrument rather than a directly enforceable global code, but their principles recur in later national and regional laws.[1]

The European Union turned those principles into a comprehensive, rights-based regulation. Regulation (EU) 2016/679, the General Data Protection Regulation, applies to processing in the context of an EU establishment and can also reach certain organizations outside the Union when they offer goods or services to people in the Union or monitor their behavior there. It regulates personal data across sectors, identifies controllers and processors, requires a legal basis for processing, creates enforceable data-subject rights, and assigns supervision to independent authorities. Its territorial and material rules contain exclusions and qualifications, so neither an EU customer nor an EU-facing website automatically resolves every scope question.[2]

The United States developed through a different sequence. Congress enacted laws aimed at particular relationships or data uses rather than one general private-sector code. HIPAA and its Privacy Rule govern protected health information held or transmitted by covered entities and business associates; Regulation P implements financial-privacy requirements for covered financial institutions; COPPA regulates online collection from children under 13 by covered services; and the Federal Trade Commission uses Section 5 of the FTC Act against unfair or deceptive privacy practices within its jurisdiction. Credit reports, education records, communications, government records, and other categories sit within additional statutes. Coverage therefore follows the entity, relationship, data, and use, not the sensitivity of a fact in the abstract.[3][4][5][6]

States have filled part of the remaining space. A Congressional Research Service report dated August 29, 2025 identified California as the first comprehensive state mover in 2018 and counted at least eighteen additional state comprehensive privacy laws enacted afterward. CRS found recurring rights to obtain, correct, and delete data and recurring rights to opt out of sale or targeted advertising, while also documenting differences in thresholds, sensitive-data consent, rulemaking, enforcement, cure periods, and private actions. The report also noted that all fifty states had breach-notification laws, illustrating that a business can face a broad notification duty even where no comprehensive state processing law applies.[3]

California is the most developed state example. The California Consumer Privacy Act, as amended, gives covered consumers rights involving access, deletion, correction, sale or sharing, and sensitive personal information, while placing duties on covered businesses, service providers, and contractors. The California Privacy Protection Agency shares enforcement responsibility with the attorney general and has rulemaking authority. California separately regulates data brokers and launched the Delete Request and Opt-out Platform, or DROP; beginning August 1, 2026, covered brokers must retrieve and process matching deletion requests on a rolling schedule, subject to legal exceptions.[7][16]

This architecture separates privacy from cybersecurity. Cybersecurity addresses confidentiality, integrity, availability, access control, incident response, and recovery. Privacy law also asks whether an authorized collection is necessary, whether a later use is compatible with the stated purpose, whether a person can exercise a right, and whether a transfer or profile is legally permitted. A perfectly encrypted database can still violate a minimization or purpose-limitation rule, while a lawful collection can still be exposed through inadequate security. NIST therefore treats privacy risk and cybersecurity-related privacy events as overlapping but not identical problems.[2][15]

The growth of data brokerage made that distinction concrete. A broker can lawfully obtain data from suppliers yet create privacy harm by combining location, health, purchasing, demographic, or political indicators into a product the individual never expected. The FTC's 2024 final InMarket order prohibited specified sale or sharing of precise location data and required deletion, consent withdrawal, supplier assessment, retention controls, and a privacy program after allegations concerning notice and consent. California's 2026 enforcement against data brokers and operation of DROP address a related market through registration, deletion, and state enforcement rather than through a general federal ownership right in personal data.[13][16]

Cross-border transfers add another layer because data can remain accessible across several legal systems at once. GDPR Chapter V allows transfers through an adequacy decision, specified safeguards such as standard contractual clauses or binding corporate rules, or narrowly construed derogations. The Court of Justice's 2020 Schrems II judgment invalidated the EU-US Privacy Shield while preserving the standard-clauses mechanism subject to an essentially equivalent level of protection, case-specific assessment, supplementary measures where needed, and suspension when protection cannot be ensured. The European Commission adopted a new EU-US Data Privacy Framework adequacy decision in 2023, but transfer analysis still depends on the recipient, certification or safeguard used, onward access, and current legal conditions.[2][9][11]

By September 2026, privacy law was therefore neither converging on one statute nor remaining purely national. Common principles coexist with different definitions, thresholds, exceptions, enforcement institutions, and remedies. The central legal problem is not merely whether an organization possesses personal information. It is whether each processing operation has a valid purpose and authority, whether the responsible actors can prove compliance, whether individuals can exercise applicable rights, and whether data remain protected when responsibility or jurisdiction changes.[1][2][3]

## Core Concepts

### Personal data, processing, and functional roles

Privacy analysis begins with the regulated object. The GDPR defines personal data broadly as information relating to an identified or identifiable natural person and defines processing to include operations such as collection, recording, organization, storage, alteration, retrieval, consultation, use, disclosure, combination, restriction, erasure, and destruction. This means that a record need not contain a name to be personal data if the person is identifiable through an identifier, location, online identity, or other factors. Pseudonymization can reduce risk without necessarily taking data outside the regulation because the additional information needed to reidentify a person may still exist.[2]

Roles follow decision-making power rather than a company's preferred label. A controller determines the purposes and means of processing; a processor handles personal data on the controller's behalf; joint controllers determine purposes and means together. One enterprise can be a processor for a customer-hosted service, an independent controller for employee records, and a joint controller for a shared campaign. GDPR Article 28 requires a processor contract and documented instructions, confidentiality, security assistance, subprocessor controls, support for rights and impact assessments, return or deletion after service, and audit information. A contract can allocate work, but it cannot convert an actor that actually determines purpose into a processor by declaration.[2]

US laws use different role vocabularies. HIPAA distinguishes covered entities and business associates. California distinguishes businesses, service providers, contractors, third parties, and data brokers. California defines a data broker around knowing collection and sale to third parties of personal information about a consumer with whom the broker lacks a direct relationship. Regulation P applies to covered financial institutions and regulates disclosure of nonpublic personal information to nonaffiliated third parties. A cross-jurisdictional inventory therefore needs to record legal roles separately for each processing purpose rather than translate every actor into one universal controller-processor pair.[3][4][5][7][16]

### Principles and legal grounds constrain the whole lifecycle

The GDPR's principles require lawfulness, fairness, transparency, purpose limitation, data minimization, accuracy, storage limitation, integrity and confidentiality, and controller accountability. These are continuing duties, not statements satisfied by publishing a privacy notice. A lawful collection can become unlawful when data are reused for an incompatible purpose, retained without a continuing justification, or exposed to recipients not covered by the original analysis. Accountability requires the controller to demonstrate compliance, making records, decisions, contracts, and control evidence part of the legal position.[2]

Lawfulness is not synonymous with consent. GDPR Article 6 provides six grounds: consent, contract necessity, legal obligation, vital interests, public interest or official authority, and legitimate interests subject to balancing, with qualifications for public authorities and special categories. Consent must be freely given, specific, informed, and unambiguous, and withdrawal must be as easy as giving it. Contract necessity does not cover processing that is merely useful to a business model, and legitimate interests requires necessity plus a balance against the person's rights and freedoms. Special-category data, including specified health, biometric, genetic, political, religious, and sexual information, face an additional prohibition-and-exception structure under Article 9.[2]

US comprehensive state laws more often combine notice, opt-out, and targeted consent duties. CRS found that most surveyed state comprehensive laws required opt-out from sale and affirmative consent before processing sensitive data, but definitions and operational details differed. California gives a right to opt out of sale or sharing and a right to limit specified uses or disclosures of sensitive personal information; its law also creates exceptions for uses such as security, legal obligations, and providing requested services. The correct question is therefore which law, right, and processing purpose apply, not whether the organization has one broad acceptance recorded at account creation.[3][7]

Purpose and minimization should be evaluated before collection. A purpose should state the outcome, affected population, data categories, recipients, retention period, and legal basis with enough specificity to test later changes. Collecting every available field because it may become useful defeats that test. The author's synthesis is that minimization has four separate dimensions: collect only what the stated purpose needs, expose it only to actors that need it, retain it only for the justified period, and use it only within the authorized purpose or a separately analyzed compatible or lawful purpose.[1][2][15]

### Rights make processing contestable

GDPR rights include transparent information, access, rectification, erasure, restriction, portability in specified circumstances, objection, and protections concerning decisions based solely on automated processing that produce legal or similarly significant effects. These rights are not absolute. Erasure, for example, is subject to grounds and exceptions; portability applies to specified automated processing based on consent or contract; and Article 22 contains exceptions paired with safeguards. A controller must identify the request, search relevant systems, apply exceptions, explain the result, and preserve evidence that the response covered the correct data and recipients.[2]

California provides a related but nonidentical bundle. Covered consumers can request knowledge or access, deletion of specified data collected from them, correction of inaccurate data, opt-out from sale or sharing, and limitation of specified sensitive-data uses. The law distinguishes verifiable requests from opt-out or limit requests. The California agency's 2025 Honda stipulated order found that Honda required excessive fields and applied verification burdens to requests that did not require that level of verification, used an interface that did not present symmetrical choices, created barriers for authorized agents, and lacked required contractual terms with advertising-technology recipients. The order demonstrates that a formal right can be violated through request design even when a web form exists.[7][14]

Rights require an identity strategy that does not create a second privacy problem. Too little verification can disclose or delete another person's records; excessive verification can collect more data than the request requires and deter exercise. The organization should match assurance to the right, likely harm, account context, and legal rule, then minimize retained verification evidence. The Honda order is a concrete warning against treating every request as if it carried the same impersonation risk.[14]

### Sensitive data changes the threshold, not every rule

Sensitivity can arise from subject matter, use, inference, and context. Health information in a hospital record, precise location around a clinic, a face template used for identification, and a purchase history used to infer a condition may be regulated through different statutes even when they reveal related facts. HIPAA protects specified health information held by covered entities and business associates, not every health-related datum held by every app or retailer. The FTC can pursue deceptive or unfair commercial uses outside HIPAA, and state consumer-health laws may add duties. Coverage must therefore be mapped before saying that data are either "HIPAA protected" or "unregulated."[3][4][13]

Biometric law illustrates narrower but stronger rules. Illinois BIPA requires covered private entities to publish retention and destruction policies, provide written notice, state purpose and duration, obtain a written release before collection, restrict sale and disclosure, and apply protective safeguards. It also grants an aggrieved person a private action, with statutory or actual damages and other relief under stated conditions. BIPA is not a general facial-recognition ban and contains exclusions, but its private remedy makes role, consent, retention, and transmission records directly consequential.[8]

Children's information has age- and service-specific protections. COPPA applies to covered websites and online services collecting personal information from children under 13 and requires verifiable parental consent subject to stated exceptions. The FTC's 2025 amendments require separate parental opt-in for specified third-party advertising disclosures, limit retention to what is reasonably necessary for a specific purpose, and add biometric and government-issued identifiers to covered definitions. These federal rules coexist with state protections for minors and with general laws, so age estimation, parental authority, audience design, and advertising integrations can create overlapping duties.[6]

### Profiling and AI do not displace ordinary privacy analysis

Profiling uses personal data to evaluate or predict characteristics such as performance, economic situation, health, preferences, interests, reliability, behavior, location, or movements under the GDPR definition. Article 22 addresses a narrower category: decisions based solely on automated processing that produce legal or similarly significant effects. Many recommendation, ranking, fraud, advertising, or triage systems can involve profiling without automatically falling within Article 22, yet they still require a legal basis, transparency, purpose compatibility, minimization, security, and applicable objection rights.[2]

AI regulation and privacy law examine different legal objects. An AI system can comply with an AI-specific transparency or conformity rule while its training, evaluation, deployment, or monitoring data violate privacy law. Conversely, a processing operation can have a GDPR legal basis without making an AI system accurate, nondiscriminatory, or compliant with the EU AI Act. The author's synthesis is to maintain two connected analyses: one traces personal-data operations, roles, purposes, grounds, rights, retention, and transfers; the other traces the AI system's use classification, provider and deployer duties, performance, oversight, and prohibited practices.[2]

### Duties turn principles into evidence

A defensible privacy program needs records of processing that connect data categories, people, purposes, legal grounds, systems, recipients, retention, transfers, rights, and controls. GDPR duties can include privacy by design and default, processor governance, security appropriate to risk, breach notification, data protection impact assessment for likely high-risk processing, a data protection officer in specified circumstances, and cooperation with authorities. The exact obligation depends on scope and risk; a checklist copied from a different role is not proof of compliance.[2]

Privacy by design means building the legal constraints into collection, defaults, interfaces, data models, access paths, and deletion rather than adding a notice after deployment. Privacy by default narrows the initial processing to what each purpose requires. A system that can accept an opt-out but continues sending events to advertising recipients until a monthly batch runs has an implementation gap. A deletion workflow that removes a production row but leaves identified exports, caches, models, or downstream copies without a legal retention basis has a scope gap. The author's synthesis is that each right and duty needs a technical state transition plus evidence that the transition propagated.[2][7][14][15]

Security remains mandatory but risk-based. GDPR Article 32 requires appropriate technical and organizational measures in light of state of the art, cost, nature, scope, context, purpose, likelihood, and severity. HIPAA separately applies privacy and security requirements to its regulated population. NIST's voluntary Privacy Framework organizes privacy risk through Identify-P, Govern-P, Control-P, Communicate-P, and Protect-P and explicitly states that it has no force of law. Framework use can support governance, but only the applicable legal text, facts, and authority determine compliance.[2][4][15]

### Cross-border transfer is a second legal test

Under GDPR Article 44, a transfer to a third country must satisfy both the general regulation and Chapter V. An adequacy decision can permit covered transfers without additional authorization. Without adequacy, Article 46 mechanisms include standard contractual clauses, binding corporate rules, approved codes or certifications with commitments, and specified public-authority arrangements. Article 49 derogations apply to particular situations and are not a routine substitute for a durable transfer mechanism. The destination's law and actual access conditions matter because a contract between exporter and importer cannot bind every public authority.[2][9]

Schrems II made that structure operational. The Court upheld the standard-clause decision but required protection essentially equivalent to that guaranteed in the Union, considered the law and practice of the destination, recognized supplementary measures, and required a supervisory authority to suspend or prohibit a transfer when adequate protection cannot be ensured and no valid adequacy decision controls. It invalidated the Privacy Shield because the Court found the relevant surveillance limitations and redress guarantees insufficient under the Charter. The holding did not ban every EU-US transfer; it rejected one adequacy decision and imposed a protection test on other mechanisms.[9]

The Commission's 2023 EU-US Data Privacy Framework adequacy decision created a new route for transfers to participating US organizations after new US safeguards and a Data Protection Review Court were established. It applies to certified participants, not every US recipient. Standard clauses and other tools remain relevant outside its scope. A 2024 first review by the Commission found the framework's elements in place while the EDPB called for continued monitoring and further guidance, showing that adequacy is an ongoing institutional assessment rather than permanent immunity from legal change.[11][17]

Foreign-government demands create a separate conflict. The EDPB's 2025 Article 48 guidelines state that responding to a third-country authority request is itself a transfer requiring a two-step test: a lawful processing basis under the GDPR and a Chapter V transfer ground. A foreign judgment or administrative order is not automatically recognized or enforceable in the Union merely because it binds a parent or recipient elsewhere. In the United States, the 2025 Data Security Program instead restricts or prohibits specified transactions giving countries of concern or covered persons access to bulk sensitive personal data or government-related data, adding a national-security control to commercial transfer analysis.[10][12]

### Enforcement determines whether rights are practical

Enforcement is distributed. EU supervisory authorities investigate, order access or restriction, suspend transfers, and impose administrative fines, with judicial remedies and compensation available under the regulation. California divides public enforcement between its privacy agency and attorney general and reserves a limited private action for specified security incidents. BIPA creates a broader statute-specific private action. COPPA is enforced by the FTC and state attorneys general rather than through a federal private right. The same factual practice can therefore generate administrative, judicial, contractual, and consumer-protection exposure through different legal routes.[2][3][6][7][8]

Remedies are not limited to fines. Authorities can require deletion, cease-and-desist measures, contract changes, simplified rights interfaces, audits, monitoring, restrictions on sale, or suspension of transfers. These measures can change a data-dependent product more directly than a monetary penalty. The author's synthesis is that boards and analysts should classify exposure by affected processing operation and possible remedy, not multiply a headline maximum fine by an assumed probability.[2][13][14][16]

## Evidence

### Legal texts reveal two distinct architectures

The GDPR and the US sectoral-state system are primary evidence about institutional design. The GDPR's method is comprehensive: it begins with broadly defined personal data and processing, applies principles and legal bases, assigns controller and processor duties, grants rights, and regulates transfers and remedies across covered sectors. The US method is layered: HIPAA, Regulation P, COPPA, the FTC Act, state comprehensive laws, state biometric rules, breach statutes, and data-broker laws each begin from a different covered entity, relationship, practice, or data category.[2][3][4][5][6][7][8]

The comparison supports a bounded finding. EU law supplies a common baseline but still contains sectoral rules, Member State choices, exceptions, and separate authorities. US law lacks one general federal private-sector baseline, but that does not mean the absence of privacy law. CRS documented recurring rights and duties across nineteen state comprehensive laws by August 2025 while emphasizing variation in coverage and enforcement. The evidence therefore supports the description "fragmented," not the stronger claim "unregulated."[2][3]

### Schrems II shows that contractual form cannot replace destination protection

Schrems II was a preliminary ruling by the Court of Justice sitting as Grand Chamber. The Court examined the GDPR, Charter rights, the standard contractual clauses decision, the Privacy Shield adequacy decision, US public-authority access, and available redress. It held the standard-clauses decision valid because the mechanism includes exporter, importer, and supervisory-authority duties, but it required a level of protection essentially equivalent to EU guarantees and contemplated supplementary measures when clauses alone are insufficient.[9]

The Court separately invalidated the Privacy Shield decision. It concluded that the relevant limitations on US surveillance and the ombudsperson mechanism did not provide protections essentially equivalent to Articles 7, 8, and 47 of the Charter. It also stated that, absent a valid adequacy decision, a competent supervisory authority must suspend or prohibit a standard-clause transfer when the clauses are not or cannot be complied with and protection cannot be ensured by other means. This is doctrinal evidence about transfer validity, not empirical proof that every transfer under clauses is unsafe.[9]

The later record shows institutional adaptation rather than final settlement. The Commission adopted the EU-US Data Privacy Framework adequacy decision in July 2023 based on new safeguards and redress. Its first periodic review in October 2024 concluded that the framework's elements had been implemented and were functioning, while the EDPB recommended continued monitoring, guidance on onward transfers and human-resources data, and another review within three years or sooner. The evidence supports a current legal route for certified organizations and an explicit review mechanism; it does not guarantee that law, certification, or judicial assessment will never change.[11][17]

### InMarket shows how general consumer-protection authority reaches data brokerage

The FTC's InMarket matter ended in a final consent order in May 2024. The Commission alleged that the company collected location information from its own and third-party applications, combined it for advertising, failed to provide full notice about uses and combinations, and did not ensure informed consent through supplier applications. The order prohibited sale, sharing, or licensing of precise location data and products targeting consumers based on sensitive location data and required deletion or deidentification subject to consent, a withdrawal mechanism, supplier assessment, retention controls, and a privacy program.[13]

The method and limitation matter. A consent order is enforceable against the respondent but is not a trial judgment establishing every allegation after contested proof. It nevertheless provides primary evidence of the FTC's enforcement theory and chosen controls. The order also demonstrates that Section 5 remedies can govern a broker outside a comprehensive federal privacy statute by focusing on unfair or deceptive collection, disclosure, consent, and retention practices.[13]

### Honda shows that interface friction can defeat a statutory right

The California agency's Honda matter ended in a stipulated final order in March 2025. The agency alleged that Honda required at least eight fields for rights requests even where fewer data points were ordinarily needed, applied verification to opt-out and limit requests that did not require it, used asymmetrical choice design, burdened authorized agents, and shared data without required contractual terms. Honda agreed to change practices, certify compliance, train personnel, obtain user-experience review, change contracting, and pay an administrative fine.[14]

This case supplies implementation evidence. The legal defect was not limited to a missing privacy policy or a completed sale. Request design, verification, recipient contracts, and user-interface symmetry were treated as enforceable parts of the law. Because the order was stipulated, it should be reported as a settlement of alleged violations rather than a judicial finding after trial. Its value lies in showing which operational details the state authority inspected and remedied.[14]

### BIPA and DROP test two different routes to individual control

Illinois BIPA uses a focused private-law model. The statute regulates specified biometric identifiers and information, requires public retention and destruction policies, notice, purpose and term disclosure, written release, sale restrictions, disclosure conditions, and reasonable protection. An aggrieved person can bring an action and seek statutory or actual damages, fees, and other relief, subject to the current statutory treatment of repeated collection or disclosure. The mechanism gives individuals direct enforcement power over a narrow data class rather than a general right across all personal data.[8]

California's DROP uses centralized administration for data brokers. The state platform lets a consumer submit one deletion request to active brokers, stores and communicates identifiers through a hashing process, and requires brokers beginning August 1, 2026 to retrieve lists, match records, delete nonexempt information on a rolling timetable, and report status. California's January 2026 data-broker settlements, including an order stopping one broker from selling Californians' personal information after unregistered sale of lists concerning health and other traits, show public enforcement alongside the centralized request mechanism.[16]

Neither model proves perfect control. A BIPA claimant must establish statutory coverage and an actionable violation. DROP depends on registration, matching, broker compliance, exceptions, and enforcement, and hashing identifiers does not guarantee a match where source records differ. The evidence shows two institutional choices -- private litigation for a sensitive category and a one-to-many administrative request for an opaque market -- rather than a universal solution to data brokerage.[8][16]

### Evidence boundaries

Legal sources establish obligations, powers, and decided outcomes; they do not by themselves measure prevalence, compliance cost, consumer understanding, or deterrence. Consent orders show what an authority alleged and required, not the frequency of the practice across an industry. Counts of enacted laws show fragmentation but do not establish that every law offers equal protection or enforcement capacity. Framework documents such as NIST and OECD organize practice and principles but do not become binding merely because an organization adopts their vocabulary.[1][3][13][14][15]

The evidence is strongest when claims stay at the correct level. It verifies that the GDPR uses a comprehensive role-and-purpose architecture, that the United States combines sectoral federal and state regimes, that courts and authorities can restrict transfers and data sales, and that request design can be an enforcement issue. Claims that privacy notices create informed choice, that maximum fines deter every actor, or that deletion systems remove every downstream copy would require separate empirical studies with defined populations and measurements.[2][3][9][14][16]

## Implications

### For individuals: identify the holder and law before choosing a right

A useful privacy request begins with four facts: who holds the data, what relationship created it, where the person and organization are located, and what action is wanted. A patient seeking a medical record may use HIPAA access rights; a California consumer may use CCPA access, correction, deletion, opt-out, or limit rights; an Illinois worker challenging a face template may rely on BIPA; and an EU data subject may invoke GDPR rights. Sending a generic "delete everything" demand can obscure the governing rule, exceptions, identity requirements, and appeal or complaint route.[2][4][7][8]

Individuals should preserve the submitted request, date, delivery method, identity evidence, response, and any appeal or complaint. They should distinguish access from deletion, correction from objection, and opt-out from withdrawal of consent because each produces a different duty. A response that retains data for a stated legal obligation is not automatically a refusal to recognize the right; the organization should identify the applicable exception and limit further use. The author's synthesis is that the strongest request states the right, relevant account or interaction, categories or processing at issue, desired result, and preferred secure response channel.[2][7]

Data-broker rights require a market-specific approach because the individual may not know which brokers hold a profile. California's DROP reduces this search problem by sending one request across active brokers, while FTC orders can impose deletion and withdrawal mechanisms on named firms. These routes remain jurisdiction- and respondent-specific. Individuals should not assume that one state request reaches a broker outside coverage or that deleting a broker copy erases records held independently by a direct-service provider.[13][16]

### For organizations: map processing, not documents

The foundational compliance artifact should be a processing map rather than one privacy policy. For each operation, record the person category, data, source, purpose, legal basis or statutory permission, role, system, recipient, location, retention, rights, security controls, transfer mechanism, and owner. Connect that record to contracts, product requirements, interface behavior, logs, deletion jobs, and evidence. This model follows the GDPR's accountability structure, the OECD controller principle, and NIST's inventory and governance approach.[1][2][15]

The worst failure is an unknown flow that crosses a legal boundary after launch. Advertising tags can disclose health or purchase events; software-development kits can transmit location; support tools can expose account contents to another country; model-training pipelines can copy data into long-lived datasets; and acquisitions can add systems whose notices, contracts, and retention were never reconciled. Preventing that outcome requires release gates for new data, recipients, purposes, profiling, locations, and retention, with periodic discovery to detect flows that bypass review.[2][13][15]

Lawful-basis analysis should be tied to necessity. If consent is used, the product must work with refusal where consent is meant to be freely given, record the specific choice, propagate withdrawal, and avoid bundling unrelated purposes. If contract necessity is used, document why processing is objectively needed to perform the requested contract. If legitimate interests are used, identify the interest, test necessity, assess impact and reasonable expectations, apply safeguards, and honor applicable objection. The author's synthesis is that a basis selected after the data flow exists is often evidence of design drift rather than genuine legal architecture.[2]

Retention should be executable. A schedule needs a triggering event, system owner, deletion or deidentification method, legal hold path, downstream instructions, backup treatment, verification, and exception review. "Retain while necessary" does not tell an engineer when the state changes. COPPA's amended rule, BIPA's destruction requirements, GDPR storage limitation, FTC location orders, and California deletion rights all show that retention is both a legal and operational control.[2][6][8][13]

### For product and interface teams: make rights ordinary operations

Rights interfaces should minimize friction without sacrificing proportionate identity assurance. Separate requests that require verification from those that do not, ask only for fields needed to locate records and authenticate the request, present acceptance and refusal symmetrically, support authorized agents where required, and provide clear status. The Honda order shows that dark patterns and excessive fields can be substantive compliance failures rather than merely poor user experience.[14]

Engineering should represent privacy choices as durable policy states. An opt-out state should be available to advertising, analytics, personalization, and export services before they act. A consent withdrawal should stop future covered processing and trigger any required downstream notice. A correction should identify derived fields that may need recomputation. A deletion should distinguish active data, legally retained data, backups, derived models, recipient copies, and audit evidence. The author's synthesis is that privacy operations fail when a user interface records a choice but the data plane cannot enforce it.[2][7][14][15]

### For AI and biometric systems: separate inference from permission

AI systems can infer sensitive characteristics from apparently ordinary signals, but inferential power does not supply legal authority. Teams should inventory training, prompt, output, evaluation, telemetry, and human-review data separately; identify controller and processor roles; determine whether special-category, minor, biometric, or employee rules apply; and assess whether automated decisions create significant effects. Model accuracy and privacy law answer different questions: a highly accurate inference can be an unlawful use, and a lawfully processed input can still produce an inaccurate or discriminatory result.[2][6][8]

Biometric templates require particular restraint because compromise cannot be remedied like a password change and because state definitions differ. A system should document the identifier, identification or verification purpose, notice, release, retention trigger, disclosure recipients, protection, and deletion evidence. If an AI system uses face geometry for identification, AI-specific classification does not replace BIPA or GDPR analysis. The related EU AI Act topic supplies the system-and-operator framework; this topic supplies the personal-data operation framework.[2][8]

### For cross-border operations: treat access as a transfer decision

A transfer inventory should identify exporter, importer, onward recipients, remote administrators, hosting, support, government-access exposure, and the legal tool relied upon. For GDPR data, the organization should determine whether an adequacy decision covers the recipient; otherwise assess an Article 46 safeguard or a narrow Article 49 derogation, evaluate destination conditions, and document supplementary measures where needed. Certification under the EU-US Data Privacy Framework must be verified for the relevant recipient and scope rather than inferred from a corporate group's name.[2][9][11][17]

Foreign legal demands need an escalation path. The EDPB's Article 48 guidance requires both a processing basis and a Chapter V transfer basis, while the US Data Security Program can restrict covered transactions with countries of concern. Contracts should require notice where lawful, control onward transfer, identify challenge and preservation responsibilities, and assign decision authority. Encryption can reduce access only if the relevant recipient or authority does not control the keys; it is not a legal basis and cannot resolve every compelled-access conflict.[10][12]

Transfer programs must be versioned because adequacy decisions, certifications, surveillance law, guidance, and recipient facts can change. Schrems II invalidated a framework that organizations had relied upon, and the replacement framework contains periodic review. The reversible design is to know where data and keys are, preserve alternative suppliers or regions where proportionate, and maintain a route to suspend a transfer without destroying the service. This operational option supports legal compliance when the governing assessment changes.[9][11][17]

### For regulators and lawmakers: enforce interoperability without erasing differences

Fragmented enforcement can leave gaps, duplicate demands, or create incompatible interfaces. Regulators can reduce those costs through common request signals, compatible data inventories, joint investigations, reasoned referrals, and published interpretations while preserving each statute's scope. California's centralized DROP demonstrates one interoperability model for brokers; GDPR cooperation mechanisms address cross-border supervision inside the Union. Coordination should not turn the weakest rule into the ceiling for every jurisdiction.[2][3][16]

Enforcement should target the control failure, not only the headline data category. InMarket's order addressed supplier consent, notice, retention, withdrawal, deletion, and sensitive-location products. Honda's order addressed verification, interface symmetry, agents, and contracts. These remedies are more diagnostic than a fine alone because they identify which processing step enabled the violation. Public orders should continue to distinguish allegations, stipulated facts, adjudicated findings, and prospective requirements so later users do not mistake settlement language for universal doctrine.[13][14]

Legislatures should make private rights, agency powers, preemption, and remedies explicit. BIPA's private action, COPPA's public enforcement, CCPA's limited security-breach action, and GDPR's administrative and judicial routes distribute enforcement differently. A nominal right without an accessible complaint or action can depend entirely on agency resources; an expansive private remedy can increase litigation and interpretation costs. The policy choice should be evaluated against detection, proof, remedy, and institutional capacity rather than against the abstract appeal of either public or private enforcement.[2][3][6][7][8]

### For boards, investors, and auditors: assess dependency and remedy exposure

Privacy exposure should be mapped by processing dependency. A business that earns revenue from targeted advertising, location, identity resolution, health inferences, or brokered profiles can face greater operational impact from an opt-out mandate, deletion order, transfer suspension, or sale prohibition than from a one-time fine. A processor may depend on customer instructions and subprocessor access; a controller may depend on a legal basis that changes when the purpose expands. The relevant questions are which revenue and workflows require which data, which rights reduce availability, and whether the service can operate under a narrower purpose or retention period.[2][13][16]

Audits should test evidence, not policy presence. Sample processing records against observed network and database flows; test consent refusal and withdrawal; submit rights requests; trace deletion across systems and recipients; verify broker and subprocessor contracts; review retention exceptions; confirm transfer certifications and clauses; and inspect incident and complaint escalation. NIST's Privacy Framework can organize these tests but does not determine their legal sufficiency. The audit conclusion should identify the law, role, processing operation, evidence, exception, and unresolved gap.[2][15]

The author's synthesis is a seven-question privacy audit. What personal data operation occurs? Which actor determines its purpose and means? What law and legal ground authorize it? Which principles, sensitive-data rules, and individual rights constrain it? Which recipients, processors, brokers, and countries receive access? What retention, security, and request evidence proves the controls work? Which authority or person can challenge the operation, and what remedy could stop it? If the organization cannot answer all seven from current records, its privacy position is not yet auditable.[1][2][3][15]

Privacy law ultimately regulates institutional power over information. Its most durable ideas are simple: specify purpose before collection, minimize the data and duration, keep responsibility visible through outsourcing, let affected people contest material uses, and preserve protection when information crosses systems or borders. The difficult work lies in translating those ideas across overlapping statutes and into product states that can be verified. A notice without control is disclosure, not governance; security without purpose limits protects a database while leaving the use of its contents unchecked.[1][2][15]

## Sources

1. OECD. "Recommendation of the Council concerning Guidelines Governing
   the Protection of Privacy and Transborder Flows of Personal Data,"
   OECD/LEGAL/0188, adopted 1980 and revised 2013; current text published
   2025.
   https://legalinstruments.oecd.org/public/doc/114/114.en.pdf [high]

2. European Parliament and Council. Regulation (EU) 2016/679, General
   Data Protection Regulation, including Articles 3-6, 9, 12-35, 44-49,
   77-83.
   https://eur-lex.europa.eu/legal-content/EN/TXT/HTML?uri=CELEX:02016R0679-20160504 [high]

3. Congressional Research Service. "Preemption and Privacy Law,"
   R48667, August 29, 2025.
   https://www.congress.gov/crs_external_products/R/HTML/R48667.web.html [high]

4. US Department of Health and Human Services, Office for Civil Rights.
   "Summary of the HIPAA Privacy Rule," current agency summary accessed
   September 2026.
   https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html [high]

5. Consumer Financial Protection Bureau. Regulation P, 12 CFR Part
   1016, especially Section 1016.10 on limits on disclosure of nonpublic
   personal information.
   https://www.consumerfinance.gov/rules-policy/regulations/1016/10 [high]

6. Federal Trade Commission. "FTC Finalizes Changes to Children's
   Privacy Rule Limiting Companies' Ability to Monetize Kids' Data,"
   January 16, 2025; final amendments published April 22, 2025.
   https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-changes-childrens-privacy-rule-limiting-companies-ability-monetize-kids-data [high]

7. California Privacy Protection Agency. "California Consumer Privacy
   Act of 2018," statute effective January 1, 2026.
   https://cppa.ca.gov/pdf/20260101_ccpa_statute.pdf [high]

8. Illinois General Assembly. Biometric Information Privacy Act,
   740 ILCS 14, current compiled text.
   https://www.ilga.gov/Legislation/ILCS/Articles?ActID=3004&ChapterID=57&Print=True [high]

9. Court of Justice of the European Union. Data Protection Commissioner
   v. Facebook Ireland Limited and Maximillian Schrems, Case C-311/18,
   ECLI:EU:C:2020:559, July 16, 2020.
   https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62018CJ0311 [high]

10. European Data Protection Board. "Guidelines 02/2024 on Article 48
    GDPR," Version 2.1, adopted June 5, 2025.
    https://www.edpb.europa.eu/system/files/2025-06/edpb_guidelines_202402_article48_v2_en.pdf [high]

11. European Commission. "Adequacy Decision for Safe EU-US Data Flows,"
    July 10, 2023.
    https://ec.europa.eu/commission/presscorner/detail/en/ip_23_3721 [high]

12. US Department of Justice, National Security Division. "Data Security
    Program: Compliance Guide," April 11, 2025, explaining 28 CFR Part
    202.
    https://www.justice.gov/opa/media/1396356/dl [high]

13. Federal Trade Commission. "FTC Finalizes Order with InMarket
    Prohibiting It from Selling or Sharing Precise Location Data," May 1,
    2024.
    https://www.ftc.gov/news-events/news/press-releases/2024/05/ftc-finalizes-order-inmarket-prohibiting-it-selling-or-sharing-precise-location-data [high]

14. California Privacy Protection Agency. "In the Matter of American
    Honda Motor Co., Inc., Stipulated Final Order," Case
    ENF23-V-HO-2, March 7, 2025.
    https://cppa.ca.gov/regulations/pdf/20250307_hmc_order.pdf [high]

15. National Institute of Standards and Technology. "NIST Privacy
    Framework: A Tool for Improving Privacy Through Enterprise Risk
    Management," Version 1.0, January 16, 2020.
    https://www.nist.gov/system/files/documents/2020/01/16/NIST%20Privacy%20Framework_V1.0.pdf [high]

16. California Privacy Protection Agency. "DROP for Data Brokers" and
    "CalPrivacy Brings New Round of Enforcement Actions Against Data
    Brokers," current through September 2026.
    https://privacy.ca.gov/data-brokers
    https://cppa.ca.gov/announcements/2026/20260108.html [high]

17. European Commission. "Report on the First Periodic Review of the
    Functioning of the Adequacy Decision on the EU-US Data Privacy
    Framework," COM(2024) 451 final, October 9, 2024; European Data
    Protection Board review report, November 4, 2024.
    https://commission.europa.eu/document/download/25695177-8073-4ce3-bf81-eb816dc6b468_en
    https://www.edpb.europa.eu/system/files/2024-11/edpb_report_20241104_reportonfirstreviewofeu-u.s.dpf_en.pdf [high]

## See Also

- `library/law-regulation/eu-ai-act-risk-tiers-general-purpose-models-compliance-and-enforcement.md` -- distinguishes AI-system and model duties from personal-data processing duties.
- `library/law-regulation/administrative-law-and-agency-rulemaking.md` -- explains delegated authority, guidance, adjudication, and judicial review behind privacy enforcement.
- `library/technology/cybersecurity-principles-threats-and-defense-in-depth.md` -- covers confidentiality, integrity, availability, and technical risk controls that overlap with but do not replace privacy law.
