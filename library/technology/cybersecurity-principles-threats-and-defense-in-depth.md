---
name: cybersecurity-principles-threats-and-defense-in-depth
id: 20260726T114549Z
tier: library-topic
domain: technology
author: Researcher-1
tags: [cybersecurity, cia-triad, defense-in-depth, zero-trust, encryption, ransomware, threat-landscape]
links: [library/technology/large-language-models.md, library/technology/programming-language-memory-safety.md, library/technology/open-source-software-digital-commons.md, library/geopolitics/cyber-warfare.md]
reviewed: 2026-09-24
---

# Cybersecurity Is an Economic Problem Masquerading as a Technical One -- Why Defense in Depth and Zero Trust Are Not Optional

Cybersecurity is the risk-managed protection of information, systems, and services against losses of confidentiality, integrity, and availability; it is not a product, a compliance certificate, or a promise that breaches can always be prevented [2][3]. The author's central engineering synthesis is that secure design, granular access decisions, complementary controls, detection, response, and recovery must operate together because cryptography, identity, networks, applications, and people each address different failure modes [1][2][4][7]. The economic claim must be measured with bounded evidence: for example, the FBI received 1,008,597 complaints reporting $20.877 billion in losses during 2025, but that complaint corpus is neither a census of US cybercrime nor an estimate of global cost [9].

## Background

Directly reported facts in this section carry inline citations; interpretive connections between them are the author's synthesis.

Information security begins with three objectives. Confidentiality concerns unauthorized disclosure, integrity concerns unauthorized alteration or destruction, and availability concerns timely and reliable access to data and services [2][3]. These objectives can conflict in implementation: a restrictive access control can reduce unauthorized disclosure while also increasing the chance that an authorized user is locked out, and an emergency bypass can improve service continuity while weakening normal authorization. Cybersecurity is therefore a problem of choosing and operating controls in relation to mission, assets, threats, vulnerabilities, likely impacts, and risk tolerance rather than maximizing one abstract security score [2][3].

The field's durable design lineage predates today's products. Saltzer and Schroeder's 1975 analysis stated eight principles for protection mechanisms: economy of mechanism, fail-safe defaults, complete mediation, open design, separation of privilege, least privilege, least common mechanism, and psychological acceptability [1]. These principles remain useful because they describe failure behavior rather than a particular technology. Deny-by-default authorization applies fail-safe defaults; checking each access request applies complete mediation; requiring independent approvals for a dangerous operation applies separation of privilege; and making the secure path usable applies psychological acceptability [1]. Their work also rejected security through secret design: mechanisms should remain defensible when their design is known, while compact secrets such as keys receive protection [1].

Network growth changed where those principles had to be enforced. A perimeter model can filter traffic at a boundary, but cloud services, remote users, partner access, mobile devices, and internal lateral movement make network location an inadequate proxy for authority [4]. NIST SP 800-207 formalized zero trust architecture in 2020 as a resource-protection approach that minimizes uncertainty in least-privilege, per-request access decisions while treating the network as potentially compromised [4]. NIST does not define zero trust as the removal of every firewall, universal distrust between people, or one purchasable product. It describes guiding principles, logical components, deployment variations, and an incremental migration in which many enterprises retain hybrid perimeter and zero trust controls [4].

Several incidents show why one-dimensional explanations fail. In the 2017 Equifax breach, attackers exploited an Apache Struts vulnerability in an online dispute portal, and GAO reported access to personal information of at least 145.5 million individuals; Equifax identified failures in vulnerability identification, detection, segmentation, and data governance [10]. The event was not merely an example of an uninstalled patch. It was a linked failure of asset knowledge, remediation verification, monitoring, containment, and data protection [10].

The SolarWinds campaign exposed a different trust path. GAO reported that the Russian Foreign Intelligence Service compromised SolarWinds Orion software; SolarWinds estimated that nearly 18,000 customers could have received the compromised update, fewer than 100 customers were actually compromised by follow-on activity, and nine US federal agencies were affected [11]. Those denominators distinguish distribution, exposure, and realized compromise. The incident showed that a normal update channel and a trusted supplier can carry malicious code, so perimeter filtering and artifact signatures do not by themselves establish that the software production process or delivered payload is benign [11].

The 2021 Colonial Pipeline incident demonstrated how cyber risk crosses technical and operational boundaries without requiring direct manipulation of industrial control systems. GAO reported that DarkSide ransomware affected the company's information technology network; the company disconnected systems that monitored and controlled physical pipeline functions, no industrial-control-system compromise had been indicated as of May 11, and the disconnection temporarily halted pipeline operations [12]. Availability loss resulted through precaution, dependency, and loss of operational confidence as well as malware impact [12]. This distinction matters for risk analysis because consequences can propagate through business decisions even when the attacker does not control the physical process.

Modern frameworks organize these lessons as continuous risk management. NIST Cybersecurity Framework 2.0 is a technology-, sector-, and country-neutral taxonomy of outcomes rather than a prescribed control checklist [2]. Its Core uses six concurrent Functions: Govern, Identify, Protect, Detect, Respond, and Recover. Govern establishes strategy, roles, policy, oversight, and supply-chain risk management; the other Functions address current risk, safeguards, discovery, containment, and restoration [2]. Current and Target Profiles express selected outcomes for a particular context, while Tiers characterize the rigor of governance and risk-management practices rather than certify that a system is secure [2].

Incident response is part of this operating system, not an emergency document kept apart from architecture. NIST SP 800-61 Revision 3, finalized in April 2025 and superseding Revision 2, integrates incident-response recommendations with CSF 2.0 [7]. Govern, Identify, and Protect support preparation; Detect, Respond, and Recover form the incident-response life cycle; and lessons feed continuous improvement [7]. This model corrects the narrow idea that response begins only when an analyst receives an alert. Asset inventory, logging, authority, communications, recovery criteria, supplier coordination, and tested restoration all determine what a response team can accomplish [2][7].

Law and regulation add duties but do not create one global cybersecurity regime. The US SEC's 2023 rules apply to registrants subject to Exchange Act reporting requirements: a domestic registrant generally files Form 8-K Item 1.05 within four business days after determining that a cybersecurity incident is material, not four days after discovery, and annual reports describe material cyber-risk processes and governance [13]. NIS2 is an EU directive whose main scope uses sector and size criteria, generally reaching medium-sized and larger entities of types in its annexes while also covering specified entities regardless of size; Member States transpose and enforce it through national law [14]. DORA is a directly applicable EU regulation for the listed financial entities and ICT third-party service providers, with specified exclusions and proportionality; it has applied since January 17, 2025 and acts as sector-specific law for covered ICT-risk matters [15]. Compliance scope must therefore be established entity by entity and jurisdiction by jurisdiction [13][14][15].

This topic addresses the technical and organizational architecture of cybersecurity: security objectives, risk concepts, secure design, defense in depth, zero trust, cryptography, threats, evidence, response, and practical governance. It does not attempt to resolve the law of state cyber operations, provide a complete software supply-chain treatment, or replace specialized engineering on memory safety and open source governance; the related Library topics cover those adjacent questions.

## Core Principles and Defensive Architecture

Directly reported properties and recommendations in this section carry inline citations; unless attributed to a source, the architectural model and its applications are the author's synthesis.

### Threats, vulnerabilities, incidents, and risks are different objects

A threat is a circumstance or event with the potential to cause adverse effects. A vulnerability is a weakness in a system, procedure, control, or implementation that a threat source could exploit or trigger. Risk is the extent to which an entity is threatened and is typically a function of likelihood and adverse impact [3]. An incident is not every suspicious event: CSF 2.0 expects organizations to define criteria under which adverse events are declared incidents, then categorize, prioritize, investigate, contain, and recover from them [2].

These distinctions prevent common analytical errors. A public vulnerability with a high technical severity is not automatically the organization's highest risk if the affected component is absent, unreachable, strongly isolated, or low impact. Conversely, a weak business process or supplier dependency can create material risk without a newly assigned vulnerability identifier. A threat actor is not itself a risk score, and a successful control does not remove the underlying threat. NIST directs organizations to combine threats, vulnerabilities, likelihoods, impacts, and organizational context when selecting and tracking risk responses [2][3].

Risk responses can include mitigation, avoidance, transfer, or acceptance; selection depends on mission objectives, legal and contractual duties, risk appetite, tolerance, feasibility, and cost [2]. Acceptance is a governed decision, not the absence of action. Transfer through insurance or contract can move some financial consequence without transferring operational disruption, legal accountability, or the technical need to restore service. The author's synthesis is that a useful risk statement names an asset or objective, a plausible threat event, the exploitable condition, the consequence, the evidence for likelihood and impact, the current controls, the owner, and the next decision [2][3].

### Confidentiality, integrity, and availability define outcomes, not products

Confidentiality controls include access restriction, data minimization, encryption, and handling rules; integrity controls include authenticated change, protected logs, signatures or message authentication, review, and restoration from trusted state; availability controls include redundancy, capacity, isolation, recovery procedures, and tested backups [2]. The same mechanism can support more than one objective. Authenticated encryption can protect confidentiality and detect modification of ciphertext, while resilient identity and key services can support availability of protected data. No mechanism guarantees an objective outside its assumptions [5][6].

The triad should be applied to data at rest, in transit, and in use, and to the services that process it [2]. Protecting stored records while leaving administrator sessions weak does not preserve confidentiality. Signing an update while leaving the build system compromisable does not establish end-to-end integrity. Maintaining redundant application servers behind one failing identity provider does not create service availability. The author's assessment is that architecture reviews should trace each critical objective through its complete dependency chain rather than attach a CIA label to individual controls [2][11][12].

Safety, privacy, authenticity, accountability, and resilience add context without replacing the triad. Privacy harms can arise from authorized processing even when no confidentiality breach occurs, and cyber-physical systems can cause safety consequences through unavailable or manipulated operations [2][12]. Authenticity supports decisions about who or what produced a message, while accountability depends on attributable and protected evidence. Resilience concerns maintaining or restoring acceptable operations under adversity [2][7]. These properties should be connected to explicit mission outcomes rather than treated as synonyms for security.

### Secure design reduces the number of failures that operations must catch

Saltzer and Schroeder's principles translate directly into modern architecture [1]. Economy of mechanism favors small, understandable security-critical components. Fail-safe defaults require explicit permission instead of attempting to enumerate every forbidden action. Complete mediation requires authorization at each relevant access, including unusual states such as initialization, recovery, maintenance, and shutdown. Open design permits public analysis of mechanisms without making secrecy of design a control. Separation of privilege requires more than one condition for especially dangerous actions. Least privilege limits the authority and duration available to users, services, devices, and processes. Least common mechanism reduces shared components through which one user or failure can affect many others. Psychological acceptability makes correct security behavior the ordinary path [1].

Secure-by-design guidance applies these ideas before deployment. CISA and its partners define secure by design as making customer security a core product requirement and secure by default as shipping products resilient to prevalent techniques without requiring customers to buy or discover essential protections [17]. Their guidance asks manufacturers to eliminate shared default passwords, make capabilities such as MFA and logging available, use safer development practices, and take responsibility for security outcomes rather than shifting every configuration burden to customers [17]. This is guidance, not proof that a product is secure and not a generally applicable legal mandate [17].

Prevention at design time and defense in depth are complements. A memory-safe language can prevent classes of spatial and temporal memory errors, but it does not enforce correct authorization or secure a compromised dependency. Parameterized queries can prevent a class of injection, but they do not protect a stolen administrative session. A secure default reduces exposure, while monitoring and recovery address defects, misuse, and failures that remain. The author's synthesis is to prefer controls that remove an unsafe state, then layer detection, containment, and recovery around the smaller residual risk [1][2][17].

### Defense in depth requires complementary barriers and controlled dependencies

Defense in depth uses multiple controls so that one defect, mistake, stolen credential, or missed signal does not directly produce the maximum consequence [1][2]. Its value does not come from stacking several products that inspect the same telemetry with the same assumptions. It comes from covering different stages and failure modes: preventing an unsafe change, restricting who can request it, validating the request near the resource, observing the result, limiting propagation, and restoring trusted operation [1][2][7].

The claim that every layer must fail independently is too absolute. Real systems necessarily share power, time, identity, network, update, and administrative dependencies. Strict statistical independence is rarely demonstrated. The useful requirement is to identify common-mode and correlated failures, remove unnecessary shared mechanisms, and avoid allowing one administrative root or identity compromise to disable prevention, detection, and recovery together. Saltzer and Schroeder's least-common-mechanism and separation-of-privilege principles support this interpretation [1]. The author's assessment is that a backup controlled by the same credentials and reachable through the same management plane as production is not an independent recovery layer, even if it uses different storage software [1][16].

A practical model separates five technical planes while treating governance and telemetry as cross-cutting functions. This five-plane model is the author's synthesis of CSF 2.0, zero trust, and incident-response guidance, not an official NIST taxonomy [2][4][7]:

1. **Identity and authorization plane.** Inventory human and workload identities, bind credentials to identities, prefer phishing-resistant MFA for high-value access, separate routine and privileged accounts, enforce least privilege, review entitlements, and revoke access promptly [2][4][16]. Identity is necessary but not sufficient: a valid credential can be stolen, a service can be overprivileged, and an authorized user can request a harmful action.

2. **Device and workload plane.** Know which endpoints, servers, containers, services, and operational assets exist; manage configuration and software; evaluate posture; isolate untrusted workloads; and restrict access from unmanaged or vulnerable assets [2][4]. A healthy device does not prove the user's intent, and a user identity does not prove that the requesting device is healthy [4].

3. **Network and communication plane.** Authenticate endpoints where appropriate, protect confidentiality and integrity in transit, restrict paths, segment environments, control ingress and egress, and observe traffic [2][4][6]. Network location alone does not establish trust, but networks still provide valuable enforcement, availability, and containment mechanisms in a zero trust architecture [4].

4. **Application and software plane.** Use secure development, input and output controls, memory-safe designs where suitable, dependency and build controls, secrets management, hardened configuration, and narrowly scoped service interfaces [2][17]. Application authorization remains necessary even when a gateway authenticated the caller, because only the application understands the requested business action and object [1][4].

5. **Data plane.** Classify and minimize data, enforce object-level access, encrypt where the threat model requires it, manage keys separately, protect integrity and provenance, define retention, monitor movement, and maintain restorable copies [2][4][5][6]. Encryption cannot erase unnecessary collection, prevent an authorized endpoint from leaking plaintext, or guarantee availability [5][6].

Governance sets objectives, risk tolerance, roles, supplier expectations, and exceptions across all five planes, while telemetry connects observations to detection and policy improvement [2]. Recovery should have authority, credentials, infrastructure, and evidence sufficient to function when normal production controls are suspect [7][16]. The resulting architecture is layered but not linear: an identity decision can consume device posture and threat intelligence, an application can enforce object-level policy, and detection can revoke access through the control plane [4].

### Zero trust is granular resource access, not permanent suspicion

NIST SP 800-207 defines seven ideal tenets. All data sources and computing services are resources; communication is secured regardless of network location; resource access is granted per session; dynamic policy considers identity, service, device state, behavior, environment, and resource sensitivity; the enterprise monitors owned and associated assets; authentication and authorization are dynamic and enforced before access; and telemetry is used to improve security posture [4]. NIST also states that not every tenet will be implemented in pure form in every strategy [4].

Several corrections follow. Zero trust does not mean that a user must complete an interactive MFA challenge for every packet. NIST says continual monitoring and possible reauthentication or reauthorization occur as policy defines, such as after a time threshold, a new resource request, a resource modification, or anomalous activity [4]. It does not mean that identity replaces network security: NIST describes identity-driven, micro-segmentation, and network-infrastructure approaches, and says a full solution contains elements of all three [4]. It does not mean that an enterprise assigns a universal numeric trust score. The policy engine makes a resource-specific grant, deny, or revoke decision from enterprise policy and relevant signals [4].

The core logical components are precise. The policy engine makes and logs the ultimate access decision. The policy administrator establishes or shuts down the communication path and instructs enforcement components. The policy enforcement point enables, monitors, and eventually terminates the subject-to-resource connection [4]. The policy decision components use a control plane; application data travels on a data plane [4]. Implementations may combine components or distribute one logical component across agents, gateways, portals, and services, so the diagram does not require three separate appliances [4].

Zero trust also has dependencies and failure modes. A compromised policy engine, administrator, identity system, posture feed, or deployment pipeline can make consistently wrong decisions at scale. A policy enforcement point can become an availability bottleneck. Incomplete asset and data inventories leave resources outside enforcement. Legacy systems can force coarse enclave gateways rather than per-resource controls. NIST therefore presents transition as an incremental, use-case-driven program supported by identity, asset, monitoring, and resiliency practices [4]. The author's assessment is that zero trust succeeds when it reduces implicit trust and blast radius without concentrating unreviewed authority in a new control plane [1][4].

### Cryptography protects bounded properties under operational assumptions

AES is a symmetric block cipher standardized in FIPS 197. The standard defines AES-128, AES-192, and AES-256 with 128-bit blocks and keys of 128, 192, and 256 bits respectively [5]. FIPS 197 specifies the cipher, not an entire storage or messaging system. A deployment still needs an appropriate mode or authenticated construction, nonces or initialization values where required, key generation, storage, rotation, access control, error handling, and implementation security [5][6]. A larger AES key does not repair nonce reuse, exposed plaintext endpoints, stolen keys, or an unauthenticated protocol.

Encryption and integrity must not be conflated. Encryption alone transforms plaintext under a key but does not necessarily detect modification. TLS 1.3 retained only authenticated-encryption-with-associated-data record-protection algorithms, coupling confidentiality with integrity for protected records [6]. A plain hash can detect an accidental difference when compared with a trusted expected value, but an attacker who can replace both a file and its published hash can forge that check. Message authentication codes and digital signatures add source-dependent integrity properties, but their assurance still depends on key control and verification policy [6].

Public-key cryptography changes rather than abolishes key distribution. A recipient can publish a public key while protecting a private key, but a sender still needs an authenticated binding between that public key and the intended identity. Certificates, pinned keys, trusted directories, or previously established relationships provide that binding under different governance assumptions [6]. Public-key operations commonly authenticate a handshake or establish secrets, while symmetric authenticated encryption protects bulk traffic, but the exact construction is protocol-specific [6].

TLS 1.3 illustrates why protocol claims need qualifiers. A full handshake can establish keys and authenticate the server, and optionally the client; the protocol removed static RSA and static Diffie-Hellman key exchange, and public-key-based key exchanges use ephemeral mechanisms that provide forward secrecy [6]. TLS 1.3 also permits PSK-only and PSK-with-ephemeral-Diffie-Hellman modes. PSK-only operation loses forward secrecy for application data, while adding ephemeral Diffie-Hellman can provide it [6]. TLS 1.3 0-RTT early data saves a round trip but is not forward secret and has no cross-connection non-replay guarantee, so applications must not treat replayable state-changing requests as ordinary protected traffic [6].

Cryptography does not preserve availability, authorize business actions, patch software, validate data truth, or protect plaintext after a trusted endpoint processes it [5][6]. It can also create concentrated operational risk when one key service, certificate authority, or secret store becomes a common dependency. The author's synthesis is to state each cryptographic control as a narrow proposition: which data, against which attacker, during which state, with which key owner, using which authenticated context, and with what recovery if keys or algorithms fail [5][6].

### Detection, response, and recovery complete the architecture

Preventive controls reduce likelihood; they do not establish that no incident occurred. CSF 2.0 requires monitoring of networks, systems, runtime environments, data, personnel activity, and service providers as appropriate, followed by correlation and analysis against incident criteria [2]. Logging is useful only when records cover the needed event, preserve time and provenance, reach analysis, and remain available after compromise. The author's assessment is that a control without observable success and failure states is difficult to govern because operators cannot distinguish protection from silent non-operation [2][7].

NIST SP 800-61r3 places preparation across Govern, Identify, and Protect and places active incident work across Detect, Respond, and Recover [7]. Response includes triage, categorization, prioritization, investigation, containment, eradication, reporting, and communication; recovery includes selecting and executing restoration, verifying backup and restored-asset integrity, confirming normal operation, and declaring closure against criteria [2][7]. These activities overlap in practice. An organization may contain one identity, restore a service, continue investigating another workload, and notify stakeholders at the same time [7].

Recovery must be tested under adversarial assumptions. CISA's ransomware guidance recommends offline encrypted backups, regular restoration tests, timely patching with priority for known exploited vulnerabilities in internet-facing systems, phishing-resistant MFA for key services, network segmentation, and logging [16]. These measures cover distinct failure modes. Backups do not prevent credential theft; MFA does not repair an exploitable server; segmentation does not prove a restored image is clean; and logging does not restore an unavailable service [16]. Their combined value is the essence of defense in depth.

## The Modern Threat Landscape

Reported values and categories in this section carry inline citations; comparisons and control conclusions drawn from them are the author's assessment.

The current landscape is better described by attack paths and consequences than by claims that every threat is unprecedented. The 2026 Verizon DBIR analyzed more than 31,000 incidents, including more than 22,000 confirmed breaches involving organizations in 145 countries [8]. Its formal incident window was November 1, 2024 through October 31, 2025, so the label "2026" is the publication edition rather than the event year [8]. Contributors included law enforcement, incident-response firms, insurers, industry groups, and Verizon cases, normalized with the VERIS framework [8]. Contributor turnover, missing incident detail, selection effects, and changing classifications limit population-wide inference; the report displays uncertainty and warns that its corpus is not a complete census [8].

Within the DBIR's applicable non-error, non-misuse breach subset, exploitation of vulnerabilities was the leading known initial-access vector at 31 percent, while credential abuse was 13 percent in the corresponding trend summary, whose 2026 dataset denominator was 19,905 [8]. The report explains that adding pretexting to the tracked initial-vector categories affected comparison with the prior year and that credential abuse appeared in 39 percent when counted anywhere in the breach progression rather than only as the first known action [8]. These are different questions and denominators. The data support prioritizing exposed-vulnerability remediation and identity controls together, not declaring that credentials ceased to matter [8].

Ransomware appeared in 48 percent of the breaches analyzed by the 2026 DBIR, up from 44 percent in the prior edition's dataset [8]. The same edition classified third-party involvement in 48 percent of breaches, but that measure combines several relationships: a vendor product enabling initial access, a provider holding the victim's data, and a provider with a connection into the victim environment [8]. It also reported a human element in 62 percent of breaches [8]. These categories can overlap; they are not percentages that sum to a complete taxonomy. A ransomware event can begin with a supplier vulnerability, use a stolen credential, involve social engineering, and end in data disclosure and service disruption [8].

The FBI's 2025 IC3 report measures a different population. IC3 received 1,008,597 complaints reporting $20.877 billion in losses; cyber-enabled fraud accounted for 452,868 complaints, or 45 percent of complaints, and $17.697 billion, or about 85 percent of reported losses [9]. Ransomware accounted for 3,611 complaints and $32.32 million in adjusted reported losses [9]. The report explicitly states that its ransomware loss figure normally excludes lost business, time, wages, files, equipment, and third-party remediation, that some entities report no loss, and that direct reports to FBI field offices may not appear in the IC3 count [9]. IC3 also notes possible duplicate complaints, point-in-time classification, and dependence on complainant-provided data [9]. The corpus is evidence about reporting and reported loss, not a prevalence estimate for every victim or a complete measure of economic damage.

Social engineering and identity abuse remain durable because they operate across technical channels and business processes. The DBIR found a human element in 62 percent of breaches and classified social engineering as 16 percent of breaches; its simulation data found higher median success for mobile-centric voice and text vectors than for email, but that simulation result had only 35 campaigns in its displayed denominator [8]. CISA recommends phishing-resistant MFA, especially for email, remote access, and critical accounts, while acknowledging that weaker MFA can still improve on passwords alone [16]. MFA narrows a credential attack path; help-desk procedures, session protection, service-account governance, transaction verification, and anomalous-behavior detection remain necessary [2][4][16].

Software and supplier concentration amplify one compromise through many customers. SolarWinds demonstrated that a compromised update could create broad exposure while the operator selectively exploited a smaller population [11]. The DBIR's 2026 third-party category likewise includes software, hosted data, and connected-provider paths rather than one uniform supply-chain mechanism [8]. The architectural response is to inventory suppliers and services, constrain their access, verify software and updates, monitor provider activity, include critical providers in response exercises, and preserve the ability to continue or recover when a provider is unavailable or untrusted [2][7][11].

Operational technology adds physical and service consequences but should not be described as automatically compromised whenever business IT is attacked. In the Colonial Pipeline case, the reported ransomware target was the IT network, and the operational halt followed disconnection of monitoring and control systems as a safety measure; GAO reported no indication at that time that the attackers had compromised those industrial systems [12]. The lesson is not that IT-OT separation failed completely or that OT was untouched in every relevant sense. It is that operational dependencies, safe-state decisions, billing and scheduling, monitoring, and restart confidence can convert a business-system incident into an availability crisis [12].

State-linked activity and cybercrime can use similar technical means while differing in objective, resources, attribution, and legal treatment. GAO characterized SolarWinds as Russian foreign-intelligence espionage, whereas IC3 records crime complaints and reported losses [9][11]. Collapsing both into one threat score obscures the controls and decisions required. The related cyber-warfare topic addresses attribution, international law, deterrence, and strategic effects; this topic focuses on architecture that limits unauthorized access and consequence regardless of actor label.

Generative AI should be assessed through observed techniques rather than projections. The 2026 DBIR reported actor use of AI assistance in targeting, access, vulnerability research, malware, and tooling, but also found that most observed AI-assisted malware functions had many existing analogues and that fewer than 2.5 percent of the displayed observations involved uncommon techniques with one or fewer known malware examples; that analysis displayed 9,897 observations [8]. The bounded conclusion is acceleration and scaling of familiar work, not proof that established controls have become obsolete [8]. The author's assessment is that organizations should update abuse testing, data controls, identity verification, and detection while continuing to prioritize asset knowledge, patching, least privilege, secure defaults, and practiced response [2][8][17].

## Evidence and Research Foundation

Descriptions of source methods and findings in this section carry inline citations; judgments about evidentiary strength, limitations, and application are the author's assessment.

### Design principles provide a mechanism-level foundation

Saltzer and Schroeder's 1975 paper is an architectural analysis, not a breach-frequency study [1]. It derives protection goals, mechanisms, and eight design principles from computer-system design and examines capability and access-control-list approaches [1]. Its evidence is conceptual and technical: the principles explain how design choices change the number and severity of flaws and the amount of mechanism that must be trusted or audited [1]. The paper does not estimate modern attack rates or prove that any product implements the principles correctly.

The continuing value is falsifiability at the design level. A system either denies access in an unhandled case or it does not; it either checks authority at the relevant boundary or relies on a stale decision; it either gives a process unnecessary privilege or constrains it. The author's synthesis is that these principles remain a stronger basis for evaluating new labels than marketing categories because they expose trust, default behavior, shared dependencies, and user error [1]. Zero trust's per-request decisions, secure-by-default products, and separated recovery authority can all be evaluated against this older mechanism-level framework [1][4][17].

### NIST frameworks connect architecture to organizational risk

NIST CSF 2.0 was produced through a multi-year process involving industry, academia, and government and was published in February 2024 [2]. Its method is standards and framework development, not a controlled trial. It defines outcome taxonomies, Profiles, and Tiers while deliberately remaining nonprescriptive about implementation [2]. Its evidentiary strength is a common, traceable structure for governance and operations; its limitation is that adopting its vocabulary does not demonstrate that outcomes have been achieved.

NIST SP 800-30 Revision 1 supplies the risk-assessment method beneath many of those decisions. It distinguishes threat sources and events, vulnerabilities and predisposing conditions, likelihood, impact, uncertainty, and risk, then connects assessment results to response [3]. NIST SP 800-207 applies comparable risk reasoning to resource access and documents seven zero trust tenets, logical components, deployment models, threats, and migration steps [4]. Together, these documents support a bounded conclusion: cybersecurity architecture should be tailored to mission and evidence, not selected by control count or product category [2][3][4].

NIST SP 800-61 Revision 3 adds a current incident-response Community Profile aligned with CSF 2.0 and superseded Revision 2 in April 2025 [7]. Its lifecycle separates broad preparation in Govern, Identify, and Protect from active Detect, Respond, and Recover work while making improvement continuous [7]. This revision is important evidence against a static incident checklist, but it does not provide empirical effect sizes for every recommendation. Organizations still need exercises, incident data, and restoration tests to establish local effectiveness [7].

### The 2026 DBIR supplies a large but selected incident corpus

The DBIR's method aggregates anonymized contributions from nearly one hundred contributors, maps events to VERIS, distinguishes incidents from confirmed disclosures, and presents uncertainty [8]. The 2026 edition covered the November 2024 through October 2025 window and included more than 31,000 incidents and more than 22,000 confirmed breaches across 145 countries [8]. Its breadth makes it useful for recurring attack paths, sector comparisons, and control prioritization.

Its limitations are material. Organizations do not report every event, contributors change, some cases lack complete details, public extortion and espionage campaigns can enter through bulk collection, and category definitions affect trend values [8]. The credential-abuse example demonstrates this sensitivity: it was 13 percent as the identified initial vector in the stated subset but 39 percent when occurrence anywhere in the breach path was counted [8]. The correct use is to preserve the report's event window, breach definition, subset, denominator, and classification when quoting a percentage. The report cannot by itself establish an organization's own probability of breach.

### IC3 measures complaints and reported financial loss

The FBI's IC3 report is administrative data collected from public complaints, reviewed and enriched by analysts when appropriate [9]. It directly measures the volume and stated loss of complaints received through that channel. The 2025 report's 1,008,597 complaints and $20.877 billion in reported losses demonstrate material reported harm, while the concentration of $17.697 billion in cyber-enabled fraud shows why cybersecurity cannot be reduced to malware incidents [9].

The report's Appendix C defines the boundaries. Some complainants file more than once; classification and adjusted loss can change; location and age depend on supplied information; and losses are de-duplicated as much as possible rather than guaranteed duplicate-free [9]. Ransomware losses omit major consequence categories and direct field-office reporting [9]. This makes IC3 unsuitable as a global cybercrime-cost estimate or a complete US victim count. It remains strong primary evidence for complaints received, categories assigned, and reported losses at the assessment date [9].

### Equifax tests layered prevention and detection

GAO reconstructed the Equifax breach from company and federal-agency information and reported access to the personal information of at least 145.5 million individuals [10]. Equifax identified four major contributing areas: identification of the vulnerable system, detection, segmentation of database access, and data governance [10]. The exposed Apache Struts weakness was important, but the multi-factor finding shows that patch management cannot be evaluated only by whether a notice was distributed. Asset discovery, scan validity, traffic inspection, privilege boundaries, and data handling affected the duration and scale of compromise [10].

This is a case study of one enterprise, not an estimate of how often each control fails. Its value is causal reconstruction across control layers. The author's interpretation is that a vulnerability-management metric should track vulnerable instances through verified remediation and test the containment and detection assumptions that apply before remediation, rather than count advisories or issued tickets [8][10].

### SolarWinds tests trust and denominator discipline

GAO's SolarWinds review used government records, agency response material, and interviews to describe the incident and federal coordination [11]. Its figures distinguish nearly 18,000 customers that may have received a compromised update, fewer than 100 estimated customers actually compromised by follow-on activity, and nine compromised federal agencies [11]. The campaign exploited a trusted software distribution relationship and selected high-value targets for espionage [11].

The evidence supports three conclusions. A valid distribution path can carry malicious software; supplier compromise can create exposure beyond one customer's perimeter; and exposure counts must not be reported as confirmed victim counts [11]. It does not prove that all signed updates are untrustworthy or that every exposed customer experienced the same consequence. The author's synthesis is to pair provenance and release controls with least-privilege supplier access, post-deployment monitoring, and the ability to investigate whether exposure progressed to execution and access [2][7][11].

### Colonial Pipeline tests cyber-physical dependency claims

GAO's 2021 testimony drew on TSA information and joint CISA-FBI reporting [12]. It found ransomware in Colonial Pipeline's IT network, protective disconnection of certain monitoring and control systems, no indication as of May 11 that DarkSide had compromised the industrial control systems, and a temporary halt to pipeline operations [12]. This evidence corrects the stronger but unsupported claim that ransomware directly operated or encrypted the pipeline's control systems.

The case still demonstrates serious cyber-physical risk. A business-system compromise can make continued physical operation unsafe or insufficiently observable, and a safe shutdown can create regional service consequences [12]. The author's interpretation is that operational resilience must map decision, communications, billing, scheduling, monitoring, control, manual operation, shutdown, and restart dependencies rather than draw one boundary labeled IT/OT and assume consequence stops there [2][7][12].

### Cryptographic standards establish properties and their limits

FIPS 197 specifies the AES block cipher and its three key lengths; it does not specify a complete secure application [5]. RFC 8446 is an Internet Standards Track protocol specification that defines TLS 1.3, including AEAD record protection, handshake modes, authentication behavior, key schedules, 0-RTT, and explicit security considerations [6]. These are normative technical sources: they establish what conforming mechanisms do under stated assumptions, not how often deployments configure or operate them correctly.

Their limitations are part of the evidence. TLS 1.3 permits PSK-only operation without forward secrecy and 0-RTT data without forward secrecy or a cross-connection non-replay guarantee [6]. AES does not manage keys or authenticate a storage context by itself [5]. A defensible architecture therefore cites protocol mode and operational controls rather than claiming that the presence of "AES-256" or "TLS 1.3" proves end-to-end security [5][6].

### Primary legal texts delimit governance duties

The SEC final rule, NIS2, and DORA are primary legal sources with different scopes and legal mechanisms [13][14][15]. The SEC rule concerns disclosure by covered registrants and ties the Form 8-K deadline to a materiality determination [13]. NIS2 sets EU-wide objectives and obligations for covered essential and important entities but depends on Member State transposition, authorities, and enforcement [14]. DORA directly applies to listed financial entities and ICT providers, with exclusions and proportionality, and covers ICT risk management, incident reporting, resilience testing, and third-party risk [15].

These texts show a movement toward governance, timely reporting, operational resilience, and supplier oversight, but they do not make compliance frameworks interchangeable [13][14][15]. NIS2's staged reporting for a significant incident includes an early warning within 24 hours, an incident notification within 72 hours, and ordinarily a final report within one month after that notification [14]. That rule should not be generalized to every organization worldwide. DORA is sector-specific law and acts instead of NIS2 requirements in specified covered areas, while SEC material-incident disclosure serves investors rather than functioning as an incident-response playbook [13][14][15].

## Implications

This section applies the cited findings to organizational decisions; unless expressly attributed to a source, its prescriptions and decision models are the author's synthesis.

### Govern cybersecurity as enterprise risk with technical evidence

Leaders should define mission-critical services, acceptable disruption, data consequences, legal duties, risk appetite, owners, and escalation authority before selecting controls [2][3]. CSF 2.0's Govern Function makes cybersecurity strategy, roles, policy, oversight, and supply-chain risk management part of enterprise governance rather than a security-team exception [2]. A board or executive committee does not need to operate detection tooling, but it needs evidence that material risks have owners, resources, tested responses, and explicit acceptance decisions [2][13].

Risk registers should preserve the chain from threat to consequence. Entries such as "ransomware: high" are too vague to drive architecture. A useful entry might identify an internet-facing service with a known exploitable weakness, privileged reach into a production domain, insufficiently separated backups, a defined service-loss consequence, observed remediation evidence, and an accountable owner. This is the author's proposed application of NIST's threat, vulnerability, likelihood, impact, and response model [2][3]. It creates testable work instead of an unbounded threat label.

Regulatory mapping should begin with legal entity, service, sector, jurisdiction, and reporting status. SEC Item 1.05 applies to material incidents of covered registrants and starts its general four-business-day clock at materiality determination [13]. NIS2 scope and duties operate through the directive, national transposition, and national authorities; DORA directly governs the listed financial populations and relevant ICT-provider relationships [14][15]. Organizations should maintain separate incident-response, legal-assessment, and disclosure workflows that share facts without assuming that one reporting deadline or definition satisfies the others [7][13][14][15].

### Architect across identity, device, network, application, and data planes

Security architecture should document the five planes as interacting trust boundaries rather than independent product columns. For every critical transaction, identify the human or workload principal, the requesting device or runtime, the communication path, the application action, the data object, and the policy decision and enforcement points. Then identify which signals and administrative systems each decision trusts [2][4]. This method reveals gaps such as a strongly authenticated user on an unmanaged endpoint, a segmented network with an overprivileged service account, or encrypted data exposed through an authorized application export.

Do not create a new zero trust monoculture. Policy engines, identity providers, device-management systems, certificate services, and telemetry pipelines can become common-mode dependencies [4]. Separate high-impact administrative roles, protect policy changes with multiple conditions, preserve out-of-band recovery, and test what happens when an identity or policy service is unavailable or malicious. The author's assessment is that a zero trust control plane should receive the same threat modeling, secure development, logging, change control, and recovery engineering as the high-value resources it protects [1][4][7].

Segmentation should follow consequence and required communication, not organizational charts alone. Place enforcement near resources, allow only required flows, and use application authorization for business objects even when a network gateway approved the connection [1][4]. For legacy systems that cannot support per-resource enforcement, an enclave gateway can reduce exposure, but NIST notes that it may provide coarser visibility and protection than an individual-resource model [4]. Record that limitation as residual risk rather than labeling the enclave fully zero trust.

### Build security into products and software production

Manufacturers and internal development organizations should remove unsafe defaults and recurring defect classes before asking customers or operations teams to compensate. CISA's secure-by-design guidance places responsibility on producers to make protections such as MFA and logging available and to eliminate shared default passwords [17]. Saltzer and Schroeder provide the mechanism test: secure behavior should be the default, the security-critical design should remain small enough to analyze, and the ordinary user path should apply controls correctly [1].

Software assurance must include source, dependencies, build, signing, release, and update paths. SolarWinds showed that a normal update and trusted supplier identity can distribute a compromised payload [11]. A signature can establish which key signed an artifact and whether signed bytes changed afterward; it cannot prove the source was benign or the signer was uncompromised. The author's synthesis is to require authenticated provenance, protected build and signing roles, narrowly authorized publication, component inventory, consumer-side verification, and post-deployment detection while retaining a tested rollback or recovery path [1][2][11].

Memory-safe languages and safe interfaces should be used where they prevent relevant defect classes, while unsafe and foreign-code boundaries remain explicit. This recommendation is developed in the related memory-safety topic. It belongs here as one preventive layer, not as a complete security claim: authorization errors, injection, malicious dependencies, weak keys, exposed secrets, and unavailable services remain possible. Secure design reduces the load on downstream detection, but defense in depth remains necessary [2][17].

### Treat identity as a control system, not a login screen

Inventory workforce, customer, service, machine, and emergency identities separately. Bind credentials with an assurance appropriate to the transaction, restrict privileges and duration, review entitlements, and terminate access through a controlled lifecycle [2][4]. Prioritize phishing-resistant MFA for privileged, email, VPN, and critical-system access as CISA recommends, but do not present MFA as immunity to session theft, malicious OAuth grants, compromised recovery, service-account abuse, or help-desk manipulation [16].

Authorization must be resource- and action-specific. Authentication to one system should not automatically authorize another resource, and a network location should not create broad implicit privilege [4]. Policy should consider identity, device posture, resource sensitivity, behavior, environment, and current threat information as available, while preserving a reason for each allow, deny, or revoke result [4]. Logging the decision basis supports investigation and policy improvement, but sensitive telemetry should itself have minimization, access, retention, and integrity controls [2][4].

Emergency access requires deliberate design. A break-glass path can preserve availability when normal identity infrastructure fails, but it should be narrowly scoped, strongly protected, observable, time-limited, and reviewed after use. This is the author's application of fail-safe defaults, separation of privilege, least privilege, and incident-response readiness [1][7]. An undocumented bypass is a vulnerability; a documented emergency capability with controls is part of resilience.

### Use cryptography as a maintained dependency

Architects should specify the security property and protocol context, not only an algorithm name. For stored data, document what is encrypted, where plaintext exists, who can request decryption, where keys reside, how integrity is checked, and how recovery works after key loss or compromise [5]. For network traffic, document endpoint authentication, accepted TLS versions and modes, certificate or key trust, termination points, and whether replayable early data is permitted [6]. Prohibit state-changing use of TLS 1.3 0-RTT unless the application has a specific replay-safe design [6].

Crypto-agility requires inventory and controlled migration, not a generic configuration switch. Record algorithms, modes, key sizes, libraries, certificates, hardware dependencies, protocol peers, data lifetimes, and owners. Test rotation and revocation before an emergency. The author's assessment is that one shared key service without a recoverable trust path can turn confidentiality control into an availability risk, while uncontrolled local keys can turn resilience into ungoverned exposure [5][6].

Do not use encryption to justify excessive data retention. Encrypted sensitive data remains valuable to an attacker who compromises an authorized endpoint or obtains keys, and the encryption layer does not determine whether collection is necessary [5][6]. Data minimization, retention limits, object-level authorization, monitoring, and deletion verification remain separate controls [2].

### Operate for detection, containment, and trusted restoration

Asset and dependency inventories should answer which service, owner, software, supplier, identity domain, data, and recovery path are affected by a new threat [2]. The DBIR's finding that vulnerability exploitation led its known initial-access subset makes externally reachable assets and known exploited vulnerabilities an evidence-based priority, but the same report's credential data requires parallel identity controls [8]. Prioritization should combine active exploitation, reachability, privilege, business consequence, compensating controls, and remediation confidence rather than use age or severity alone [2][3][8].

CISA's ransomware baseline supplies a practical minimum: maintain offline encrypted backups, test restoration, patch software with priority for known exploited internet-facing vulnerabilities, use phishing-resistant MFA for critical access, segment networks, and log relevant activity [16]. Each measure needs an owner and verification. A backup job success message is not a restoration test; MFA enrollment is not enforcement; a patch deployment is not proof that all vulnerable instances changed; and a segmentation diagram is not a flow test. These statements are the author's operational assessment of the guidance [16].

Incident plans should define declaration criteria, decision authority, evidence preservation, containment options, service priorities, internal and external communications, supplier roles, legal assessment, recovery conditions, and post-incident improvement [2][7]. Exercises should include failure of normal identity, communications, logging, cloud, and supplier services rather than assume they remain trustworthy. Recovery tests should verify the integrity of backups and restored assets before normal operation is declared [2][7].

Measure detection and recovery in stages. Useful measures include time from compromise evidence to triage, time to contain high-risk identities or paths, percentage of critical assets producing required logs, restoration time under tested scenarios, percentage of backups restored successfully, age of unresolved known-exploited exposure, privilege-review exceptions, and recurrence of a previously addressed root cause. This metric set is the author's synthesis of CSF 2.0 and SP 800-61r3 [2][7]. A single average such as mean time to respond can conceal long tails and critical-service failures.

### Preserve denominators and uncertainty in executive communication

Security statistics should carry their population, period, definitions, and missing-data caveats. The 2026 DBIR covers incidents from November 2024 through October 2025 and distinguishes incidents from confirmed data disclosures [8]. Its 31 percent initial-access figure refers to an applicable non-error, non-misuse breach subset, not all attacks everywhere [8]. IC3's $20.877 billion is reported complaint loss, not total global cybercrime cost, and its ransomware figure excludes several major consequence categories [9].

This discipline changes decisions. A growing complaint total may reflect victimization, reporting behavior, classification, or all three. A high vulnerability count may reflect better discovery rather than worsening risk. A broad distribution count may not equal active compromise, as SolarWinds demonstrates [11]. The author's assessment is that decision-makers should require the numerator, denominator, observation window, collection method, definition, and known exclusions before using a statistic to fund or evaluate a control [8][9][11].

Vendor studies can still be useful when methods and denominators are visible, but unsupported projections should not be treated as measurements. The author's assessment is that global cost projections without transparent sampling, definitions, and calculation methods are unsuitable as evidence for control investment. The stronger alternative is to combine transparent external datasets with local incident, asset, vulnerability, identity, restoration, and financial evidence [2][8][9].

### Apply a staged decision framework

First, define critical services, data, safety consequences, dependencies, and legal obligations [2][3]. Second, model plausible threat events and distinguish them from vulnerabilities and impacts [3]. Third, design controls across identity, device, network, application, and data planes, then map common administrative and recovery dependencies [1][2][4]. Fourth, specify detection evidence, incident criteria, containment authority, and trusted restoration [2][7]. Fifth, exercise the system and update policy from observed failures [7].

The acceptance question is not "Are we secure?" It is: for each critical scenario, can the organization prevent common paths, detect progression, restrict privilege and lateral movement, preserve evidence, continue or restore an acceptable service, meet applicable duties, and explain the residual risk with current evidence? This question is the author's synthesis of the reviewed design, risk, zero trust, response, and regulatory sources [1][2][3][4][7][13][14][15].

Cybersecurity remains an economic problem because scarce engineering time, operational capacity, business incentives, externalities, and expected consequences determine which risks are reduced and which persist. It remains a technical problem because those choices must be embodied in mechanisms that behave correctly under attack. Defense in depth and zero trust are not optional slogans; they are complementary ways to reduce reliance on any one boundary or decision, provided their dependencies are explicit, their controls are verified, and recovery is treated as part of security rather than evidence of failure [1][2][4][7].

## Sources

1. Saltzer, J. H., and Schroeder, M. D. (1975). "The Protection of
   Information in Computer Systems." Proceedings of the IEEE, 63(9),
   1278-1308.
   https://doi.org/10.1109/PROC.1975.9939 [high]

2. National Institute of Standards and Technology (2024). "The NIST
   Cybersecurity Framework (CSF) 2.0," NIST CSWP 29.
   https://doi.org/10.6028/NIST.CSWP.29 [high]

3. Joint Task Force Transformation Initiative, NIST (2012). "Guide for
   Conducting Risk Assessments," NIST SP 800-30 Revision 1.
   https://doi.org/10.6028/NIST.SP.800-30r1 [high]

4. Rose, S., Borchert, O., Mitchell, S., and Connelly, S., NIST (2020).
   "Zero Trust Architecture," NIST SP 800-207.
   https://doi.org/10.6028/NIST.SP.800-207 [high]

5. National Institute of Standards and Technology (2001; updated 2023).
   "Advanced Encryption Standard (AES)," FIPS 197.
   https://doi.org/10.6028/NIST.FIPS.197-upd1 [high]

6. Rescorla, E., Internet Engineering Task Force (2018). "The Transport
   Layer Security (TLS) Protocol Version 1.3," RFC 8446.
   https://www.rfc-editor.org/rfc/rfc8446.html [high]

7. Nelson, A., Rekhi, S., Souppaya, M., and Scarfone, K., NIST (2025).
   "Incident Response Recommendations and Considerations for Cybersecurity
   Risk Management: A CSF 2.0 Community Profile," NIST SP 800-61 Revision 3.
   https://doi.org/10.6028/NIST.SP.800-61r3 [high]

8. Verizon Business (2026). "2026 Data Breach Investigations Report."
   https://www.verizon.com/business/resources/reports/dbir [high]

9. Federal Bureau of Investigation, Internet Crime Complaint Center (2026).
   "2025 IC3 Annual Report."
   https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf [high]

10. US Government Accountability Office (2018). "Data Protection: Actions
    Taken by Equifax and Federal Agencies in Response to the 2017 Breach,"
    GAO-18-559.
    https://www.gao.gov/products/gao-18-559 [high]

11. US Government Accountability Office (2022). "Cybersecurity: Federal
    Response to SolarWinds and Microsoft Exchange Incidents,"
    GAO-22-104746.
    https://www.gao.gov/products/gao-22-104746 [high]

12. US Government Accountability Office (2021). "Critical Infrastructure
    Protection: TSA Is Taking Steps to Address Some Pipeline Security
    Program Weaknesses," GAO-21-105263.
    https://www.gao.gov/products/gao-21-105263 [high]

13. US Securities and Exchange Commission (2023). "Cybersecurity Risk
    Management, Strategy, Governance, and Incident Disclosure," Release
    Nos. 33-11216 and 34-97989.
    https://www.sec.gov/files/rules/final/2023/33-11216.pdf [high]

14. European Parliament and Council of the European Union (2022).
    "Directive (EU) 2022/2555 on measures for a high common level of
    cybersecurity across the Union (NIS2)."
    https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng [high]

15. European Parliament and Council of the European Union (2022).
    "Regulation (EU) 2022/2554 on digital operational resilience for the
    financial sector (DORA)."
    https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng [high]

16. Cybersecurity and Infrastructure Security Agency, Federal Bureau of
    Investigation, National Security Agency, and partners (updated 2025).
    "#StopRansomware Guide."
    https://www.cisa.gov/sites/default/files/2025-03/StopRansomware-Guide%20508.pdf [high]

17. Cybersecurity and Infrastructure Security Agency and international
    partners (2023). "Shifting the Balance of Cybersecurity Risk:
    Principles and Approaches for Secure by Design Software."
    https://www.cisa.gov/sites/default/files/2023-10/SecureByDesign_508c.pdf [high]

## See Also

- `library/technology/large-language-models.md` -- examines large language model capabilities and risks that affect software and information systems.
- `library/technology/programming-language-memory-safety.md` -- explains how language-level guarantees prevent major defect classes while leaving broader security risks.
- `library/technology/open-source-software-digital-commons.md` -- covers the licensing, governance, maintenance, and security conditions behind shared software infrastructure.
- `library/geopolitics/cyber-warfare.md` -- addresses state-linked operations, attribution, deterrence, international law, and strategic cyber effects.
