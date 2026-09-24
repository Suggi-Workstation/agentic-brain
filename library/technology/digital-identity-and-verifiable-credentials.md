---
name: digital-identity-and-verifiable-credentials
id: 20260924T093941Z
tier: library-topic
domain: technology
author: Librarian
tags: [digital-identity, verifiable-credentials, digital-wallets, decentralized-identifiers, selective-disclosure, interoperability, credential-status, trust-frameworks]
links: [library/technology/cybersecurity-principles-threats-and-defense-in-depth.md, library/technology/blockchain-distributed-ledgers.md, library/technology/post-quantum-cryptography-migration.md, library/technology/internet-tcpip-protocols-routing.md]
---

# Digital Identity and Verifiable Credentials -- Portability Requires Aligned Cryptography, Trust, and Lifecycle Controls

Verifiable credentials let an issuer give a holder tamper-evident claims that a verifier can check without contacting the issuer during every transaction, but a valid signature proves neither that a claim is true nor that its issuer is authoritative. Portable digital identity therefore depends on an entire system: interoperable formats and exchange protocols, trustworthy issuers and verifiers, secure wallets, selective disclosure, status and recovery mechanisms, and governance that gives cryptographic evidence operational meaning. [1][6][7][10]

## Background

Digital identity is not one identifier or one account. It is the technical representation of claims used to recognize a person, organization, device, or other subject in a particular context. Conventional federation commonly places an identity provider in the live transaction: a relying party redirects a user to that provider, which authenticates the user and returns a signed assertion. NIST SP 800-63C-4 describes this federation model and separately specifies subscriber-controlled wallets, in which a credential service provider issues signed attribute bundles that a wallet can later present to relying parties. The architectural change is from a provider-mediated assertion for each transaction toward reusable, holder-mediated evidence, not from centralized truth to trust-free identity. [10]

Physical credentials supplied the basic analogy. A university signs a diploma, a government issues a driving licence, and an employer issues an identity card; the document travels with its holder and a recipient evaluates both the document and its issuer. The first W3C Verifiable Credentials Data Model became a Recommendation in November 2019 and formalized a Web data model for issuers, holders, subjects, verifiers, credentials, and presentations. Its privacy design included presentations containing selected information from one or more credentials rather than requiring the holder to reveal every stored attribute. Version 2.0, published as a W3C Recommendation in May 2025, defines a verifiable credential as tamper-evident claims plus metadata that cryptographically prove who issued it. [1][17]

This model separated the meaning of a credential from any single cryptographic envelope or transport. W3C Data Integrity specifies one family of proof mechanisms for making documents tamper-evident, while JOSE- and COSE-based envelopes and other credential formats use different serialization and signing machinery. That separation permits the same broad credential concepts to be represented with linked-data proofs, compact JSON tokens, or mobile-document structures, but it also creates a profiling problem: two products can claim standards support while choosing incompatible formats, algorithms, identifiers, status methods, and exchange options. [1][3][7]

Decentralized Identifiers, or DIDs, developed as one identifier layer associated with this ecosystem. DID Core became a W3C Recommendation in July 2022 and defines a URI scheme, a data model for DID documents, verification relationships, and a resolution concept. A DID document can expose verification methods and service information under rules defined by a DID method and its underlying registry. DID Core describes DIDs as components of larger systems such as verifiable credentials; it does not turn a DID into a credential, prove that its controller is a particular legal person, or require every credential system to use a blockchain. [2]

Issuance and presentation protocols matured on a parallel track. OpenID for Verifiable Credential Issuance 1.0, finalized in September 2025, defines an OAuth-protected API through which a wallet obtains credentials. It supports multiple credential formats, including W3C Verifiable Credentials, ISO mobile documents, and SD-JWT-based credentials. OpenID for Verifiable Presentations 1.0, finalized in July 2025, defines an OAuth-based mechanism through which a verifier requests and receives one or more presentations. It explicitly states that the framework requires profiling to achieve interoperability because deployments must agree on formats, query rules, client identification, security options, and other choices. [6][7]

Selective disclosure became a central privacy objective because most transactions require fewer attributes than a conventional identity document contains. An age check might require proof that a threshold is met, not a name, address, document number, and full date of birth. W3C presentations, SD-JWT, ISO mobile documents, and BBS-based proofs provide different technical routes for disclosing a subset of credential data. RFC 9901 standardizes selective disclosure for JSON Web Tokens by letting an issuer sign digests while a holder releases selected disclosures; BBS proofs can create derived presentations designed to be unlinkable at the proof layer. These mechanisms differ in privacy properties, implementation complexity, data representation, and maturity. [5][8][13][14]

Governments have moved the architecture from standards work into deployment programs. Regulation (EU) 2024/1183 established the European Digital Identity Framework and requires Member States to provide at least one European Digital Identity Wallet under specified conditions. It calls for common issuance and interaction protocols, relying-party registration, selective disclosure, user control, security by design, and validation mechanisms. The European Commission's EUDI Toolbox combines an Architecture and Reference Framework, reference implementation, and technical specifications, while pilots test cross-border use cases. This is a regulated ecosystem built from credentials, wallets, registries, certification, and common profiles rather than a single universal identity database. [11][12]

The historical progression exposes a recurring category error. Cryptography can show that protected data has not changed and that a particular key produced a proof. It cannot by itself establish that a university is accredited, that an identity-proofing process was adequate, that a verifier has a legitimate purpose, or that a current claim remains valid. The W3C model leaves issuer trust to the verifier, NIST specifies trust agreements and assurance information, and the EU framework adds registration, certification, and supervision. The author's synthesis is that digital identity becomes portable only when technical portability and institutional trust portability are designed together. [1][10][12]

## Core Concepts

### A credential system has distinct actors and artifacts

The W3C model distinguishes issuer, holder, credential subject, and verifier. The issuer makes claims and secures the credential. The holder possesses or controls it and can create a presentation. The subject is the entity described by the claims; the holder and subject can be the same entity, but they need not be. The verifier receives a credential or presentation and applies verification and business rules. A digital wallet is software, and sometimes associated hardware or a hosted service, that stores credentials or references, protects keys, mediates user approval, and participates in issuance and presentation protocols. [1][10]

A claim is a statement, such as an assertion that a subject holds a degree or is over a threshold age. A credential groups claims with issuer and lifecycle metadata. A verifiable credential adds a securing mechanism that makes alteration detectable and binds the protected content to an issuer-controlled verification method. A verifiable presentation is the artifact delivered for a particular interaction; it can contain one or more credentials, derived disclosures, proof of holder participation, an audience, a challenge, and freshness data. Keeping these artifacts separate prevents a stored credential from being treated as a reusable bearer token that can be copied into any context. [1][7]

Verification is a pipeline, not a single signature check. A verifier may have to parse the representation, validate the securing mechanism, resolve or obtain the issuer's verification key, verify the expected proof purpose, bind the response to the intended audience and challenge, check time conditions and credential status, validate the data model, and apply an acceptance policy for credential type, issuer, assurance, and requested attributes. OpenID4VP includes replay-prevention and audience-binding requirements, while the W3C model expects verifiers to evaluate status according to the credential's status type and their own criteria. [1][7]

Even a successful pipeline produces a bounded result. It can establish that protected claims came from the key associated with an asserted issuer under the selected method and have not been modified. It does not independently validate every underlying fact, infer the issuer's authority, or decide whether the claims satisfy a service's policy. The author's assessment is that systems should report these results separately: cryptographic validity, lifecycle validity, issuer trust, schema or semantic validity, holder binding, and policy acceptance. A single green "verified" label hides materially different failure modes. [1][4][10]

### Format, proof, protocol, and policy are separate layers

A data model defines the conceptual fields and relationships in a credential. A credential format defines a concrete encoding and protection method. An issuance protocol moves a credential from issuer to wallet. A presentation protocol lets a verifier request evidence and a wallet respond. A trust framework defines who may issue or verify which claims, with what assurance, liability, audit, and status obligations. Products interoperate only when enough choices align across all five layers. [1][6][7][10]

The W3C Verifiable Credentials Data Model uses JSON-LD semantics and supports different securing mechanisms. Data Integrity cryptosuites place proofs over transformed data, while JOSE or COSE envelopes secure serialized payloads through established token and binary-signing technologies. SD-JWT is a selective-disclosure construction for JSON claims, and the developing SD-JWT VC profile adds credential-specific metadata and processing rules. ISO/IEC 18013-5 specifies the mobile driving licence application and its mobile-document structure. OpenID4VCI and OpenID4VP can carry several of these formats, which shows why protocol support is not identical to format support. [1][3][6][7][8][9][13]

An implementation statement such as "supports OpenID4VP" is therefore incomplete. The final OpenID4VP specification says that the framework requires profiles to define interoperable choices. A profile might select SD-JWT VC and mdoc, approved signing algorithms, verifier-identification schemes, response encryption, status mechanisms, key-attestation rules, and a fixed subset of optional protocol features. The OpenID Foundation's High Assurance Interoperability Profile and conformance program are examples of constraining this option space. The author's synthesis is that optionality is useful for standards evolution but must be converted into explicit deployment profiles before procurement or integration. [7][18][19]

### Identifiers locate keys or subjects; they do not supply authority

Identifiers answer different questions. A local account identifier may identify a person only within one service. A URI may identify an issuer or credential type on the Web. A DID is a URI whose method defines creation, resolution, update, and deactivation rules. Resolving a DID can produce a DID document containing verification methods and their authorized relationships, but DID Core leaves the underlying registry and many governance properties to individual DID methods. [2]

This means decentralization is not a binary system property. A DID method can depend on a distributed ledger, a Web domain, a consortium registry, or another verifiable data registry. Governance can remain concentrated even when key control is technically distributed, and a globally resolvable identifier can still create correlation risk if reused across transactions. Conversely, a credential ecosystem can use conventional Web identifiers and certificate chains while giving users substantial presentation control. The author's assessment is that identifier choice should follow requirements for key rotation, resolution availability, governance, privacy, cost, and recovery rather than an assumption that every verifiable credential needs a blockchain. [2][15]

The distinction between an identifier and an identity claim is equally important. Control of a DID key can demonstrate control of that identifier under its method, but connecting the controller to a legal name, professional licence, age, or organizational role requires an issuer and an evidence process. A credential can make that connection, and the verifier then decides whether it trusts the issuer and process. This is why cryptographic self-assertion and independently issued evidence should not be displayed as equivalent. [1][2][10]

### Issuance binds claims, issuer intent, and often a holder key

Issuance begins before a credential is signed. The issuer determines what evidence is required, identifies or authenticates the applicant, constructs claims and metadata, selects a format and cryptographic suite, and decides how the credential is bound to its holder or device. OpenID4VCI supplies protocol rails for authorization, credential offers, access tokens, proof material, credential requests, and responses. It does not standardize the substantive evidence needed for a university degree, a government identity, or an employment role. [6]

Holder binding reduces simple credential sharing. A credential can contain or refer to a confirmation key, and a later presentation can prove possession of the corresponding private key. Wallet and key attestation can provide additional evidence about the software or hardware protecting that key. OpenID4VCI defines common attestation structures to improve interoperability, while NIST requires trust agreements to address wallet activation, key management, and software-integrity information in subscriber-controlled wallet deployments. Strong binding raises security but also creates recovery, migration, delegation, and accessibility challenges if the binding is too rigid. [6][10]

Issuers also need lifecycle semantics at issuance. Expiration limits how long a verifier may rely on old evidence. Status references let the verifier determine whether an unexpired credential is suspended or revoked. Credential schemas or type metadata help recipients interpret claims. Terms or policies can constrain use, although machine-readable terms do not enforce themselves. The author's synthesis is that a credential should be treated as a versioned evidence package with explicit validity and update rules, not as a permanent database row exported to a phone. [1][4][9]

### Presentation minimizes and binds disclosure to a transaction

Presentation starts with a verifier request describing acceptable credentials and needed claims. OpenID4VP uses the Digital Credentials Query Language to express such requirements and returns presentations in a `vp_token` structure. The wallet evaluates the request, finds candidate credentials, lets the user choose where applicable, derives or assembles the response, and binds it to the verifier and transaction. HTTPS, signed requests, response encryption, client-identifier schemes, audience values, nonces, and short validity windows address different interception, substitution, and replay risks. [7]

Data minimization has several levels. A wallet can choose among credentials and reveal only requested credentials. A format can support claim-level selective disclosure, allowing the holder to reveal an age or qualification without unrelated fields. A predicate or zero-knowledge proof can establish a statement such as "age is at least 18" without revealing the underlying birth date. These levels should not be conflated: omitting a credential is not the same as selectively disclosing fields, and disclosing a signed Boolean attribute is not the same as proving a predicate over a hidden value. [5][8][12][14]

SD-JWT uses salted disclosures whose digests are covered by an issuer-signed JWT. During presentation, the holder releases selected disclosure values, and the verifier recomputes their digests and checks the issuer signature. Key binding can attach the presentation to a holder-controlled key. This construction uses familiar JSON and JOSE tools and is standardized for selective disclosure in RFC 9901; SD-JWT VC remains a separate credential-profile work item, so deployments must record the exact draft or final version they implement. [8][9]

BBS-based Data Integrity credentials use a different model. An issuer creates a BBS signature, and the holder derives a proof containing selected statements. The W3C BBS cryptosuite describes derived proofs that can be unlinkable at the proof level, including different proofs over the same disclosed information. This is stronger than merely hiding undisclosed fields, but system-level unlinkability still depends on avoiding stable subject identifiers, unique attribute combinations, status handles, network identifiers, cookies, and verifier collusion. The BBS specification itself warns that IP and link-layer artifacts can reintroduce linkage. [5][14][15]

### Status, revocation, and expiry solve different problems

Expiration is determined from time metadata and ends normal acceptance after a defined interval. Revocation marks a credential as no longer valid before its scheduled end, while suspension can represent a reversible status. Key revocation or rotation concerns the issuer's verification method and may affect many credentials, whereas credential status concerns a specific credential or status-list entry. A verifier needs rules for all of these conditions and for failure to obtain status information. [1][2][4]

A naive status endpoint that receives a unique credential identifier on every presentation lets the issuer observe where and when the credential is used. Bitstring Status List v1.0 reduces this direct communication by publishing compressed status lists in verifiable credentials; a verifier retrieves a list and checks the indexed bit. The specification sets a minimum bitstring size to provide group privacy when issuance volume is sufficient. This design reduces but does not eliminate correlation: unusual list allocation, cache behavior, small anonymity sets, or verifier logging can still expose patterns. [4]

Status freshness also creates an availability-policy trade-off. A verifier that fails closed when a list cannot be retrieved can deny service during an outage. A verifier that uses an old cached list or fails open can accept a recently revoked credential. NIST recommends limited validity windows and an independent status-verification means for wallet attribute bundles. The author's assessment is that deployments need explicit maximum status age, caching, outage, audit, and emergency-revocation policies rather than leaving network errors to library defaults. [4][10]

### Trust registries turn cryptographic identities into accepted authorities

A verifier needs to know which issuers it accepts for each credential type and assurance level. That decision can be configured locally, delegated to a federation authority, derived from a regulated trusted list, or evaluated from public issuer information. NIST allows federation authorities to define trust agreements and requires credential service providers to publish information that relying parties can evaluate. The EU framework uses notified schemes, trusted lists, relying-party registration, certification, and supervision to establish institutional context around wallet transactions. [10][12]

A trust registry should not be treated as a universal list of "good" organizations. Its entries require scope: issuer identity, accepted credential types, verification keys or discovery locations, assurance and evidence processes, jurisdiction, validity period, status obligations, and governance. A university might be trusted to issue its own degree credential but not a driving licence; a government issuer accepted for one jurisdiction might not satisfy another service's policy. The author's synthesis is that authorization to issue is a typed, time-bounded relationship, not a Boolean property of an issuer key. [1][10][12]

Verifier trust matters too. A wallet that releases valid personal data to any requester with a network endpoint invites overcollection and phishing. OpenID4VP defines verifier-identification and metadata mechanisms, and the EU regulation requires wallet-relying parties to register and state intended data requests. A secure user interface must show who is asking, which claims will be released, why they are requested when that information is available, and whether the request exceeds policy. Cryptographic authentication of the verifier is necessary but does not make the requested purpose legitimate. [7][12][15]

### The wallet is a security boundary and a usability system

A wallet protects private keys, credentials, transaction state, consent decisions, and often sensitive metadata about the user's relationships. Compromise can enable impersonation or disclosure even if every credential signature remains mathematically sound. NIST therefore treats wallet activation, key management, software integrity, assertion freshness, audience restriction, and replay prevention as parts of the trust agreement and transaction. The EU framework adds security-by-design, active user confirmation, breach notification, certification, and high-assurance requirements for EUDI wallets. [10][12][16]

Device loss and migration make pure key custody insufficient as a product design. Recovery can reissue credentials after renewed identity proofing, restore protected wallet state, transfer keys through a controlled protocol, or use managed backup. Each option changes the threat model: effortless cloud recovery can recreate centralized account-takeover risk, while no recovery can exclude a user after device failure. Delegation and guardianship introduce further questions about whose authority is being exercised. The author's assessment is that wallet architecture must document recovery assurance, revocation of old devices, backup confidentiality, migration, and support for users who cannot operate a smartphone or biometric authenticator. [10][12][15]

User control also requires more than placing a consent button before disclosure. The EDPS notes that seamless wallet interactions can make unintentional disclosure less perceptible than handing over paper documents. Repeated prompts can normalize approval, technical claim names can conceal meaning, and bundled requests can undermine minimization. A trustworthy wallet should convert protocol detail into specific human choices, preserve a comprehensible transaction history, and make refusal possible without silently releasing fallback data. [15]

## Evidence

### W3C standards show convergence at the data-model layer, not one complete stack

The W3C standards record provides a longitudinal case. The 2019 Verifiable Credentials Data Model 1.0 established the actor and artifact model; DID Core reached Recommendation status in 2022; and the Verifiable Credentials 2.0 family in 2025 added a revised data model plus companion work on Data Integrity and status. The method is standards-based consensus supported by normative requirements, public issue handling, implementation reports, and test suites rather than a controlled experiment. The resulting specifications demonstrate that multiple organizations agreed on common vocabulary and validation behavior, but their modularity deliberately leaves transport, trust policy, identifier methods, cryptosuites, and profiles open. [1][2][3][4][17]

The W3C VC 2.0 interoperability report tests issuer and verifier implementations against conformance statements. Its published table records both passes and failures, including cases in which an implementation did not reject a malformed presentation. This evidence is valuable because it tests observable behavior rather than vendor claims, but it is bounded by the implementations, versions, and assertions included in the suite. The finding is not that the ecosystem is universally interoperable; it is that a shared testable data model exists and that implementation errors remain visible even after the standard is published. [18]

This case supports a layered conclusion. A Recommendation can stabilize syntax and algorithms, while independent suites show whether products implement them consistently. It cannot make two deployments accept the same issuers, assurance processes, credential formats, or privacy profile. The author's interpretation is that data-model conformance is necessary evidence for portability but is weaker than transaction-level interoperability across real issuers, wallets, verifiers, status services, and trust registries. [1][7][18]

### OpenID final specifications and conformance tests reduce protocol ambiguity

OpenID4VP 1.0 and OpenID4VCI 1.0 reached final status in July and September 2025. The specifications define protocol messages, endpoint behavior, security considerations, metadata, and mappings for multiple credential formats. This is a concrete engineering advance over ecosystem-specific wallet APIs because an issuer or verifier can target public protocol requirements. OpenID4VP nevertheless states that it is a framework requiring profiling, so a conforming base implementation can still differ from another on formats and options. [6][7]

The OpenID Foundation completed conformance suites for OpenID4VP, OpenID4VCI, and the High Assurance Interoperability Profile and opened self-certification in August 2026. The published testing guides cover issuer, wallet, and verifier roles and make successful and failure-path tests available. They also state an important limit: running the tests with mdoc or SD-JWT VC does not exhaustively test those credential formats; certification establishes that the relevant OpenID4VP, OpenID4VCI, and profile provisions were implemented. The method therefore tests protocol behavior against a fixed profile, not the entire security or semantics of every credential. [19][20]

This is stronger interoperability evidence than a list of organizations saying they use a specification, because a common suite can expose mismatched parameters and security behavior. It remains self-certification through a standards organization, not proof that a deployed wallet resists device compromise, uses a sound identity-proofing process, or complies with every local policy. The author's interpretation is that conformance results should be one procurement artifact alongside threat models, format-specific tests, key-protection evidence, privacy review, and end-to-end ecosystem trials. [18][19][20]

### The EU program tests an ecosystem, not only a credential format

The European Digital Identity Framework is an institutional deployment case. Regulation (EU) 2024/1183 defines obligations for Member States, wallet providers, relying parties, validation, certification, user control, and common protocols. The Commission's Toolbox translates the regulation into an Architecture and Reference Framework, reference implementation, and technical specifications. Large-scale pilots and cross-border work examine use cases such as identification, qualifications, payments, and mobile documents under a shared policy environment. [11][12]

This case demonstrates why interoperable credentials require coordinated non-cryptographic infrastructure. Relying parties register and declare intended data requests; wallets and schemes are certified; Member States provide validation mechanisms; issuers and attestations operate under legal and supervisory rules; and common profiles constrain protocol choices. ENISA's certification work adds harmonized cybersecurity requirements for wallet products and schemes. The system is therefore testing governance, software, registries, certification, and operational roles together. [12][16]

The evidence has limits. Regulation and reference architecture specify intended behavior, while deployment outcomes depend on national implementations, certification quality, user interfaces, accessibility, incident response, and actual cross-border tests. The Commission describes the Toolbox as continuously updated, which is appropriate for an evolving stack but means version pinning is essential when comparing implementations. The author's interpretation is that the EUDI program is evidence of serious institutional adoption and ecosystem engineering, not proof that every technical and privacy problem has been solved. [11][12][15]

### NIST exposes trust and lifecycle requirements behind the wallet abstraction

NIST SP 800-63C-4 is a requirements-and-guidance case for federated identity. Its subscriber-controlled wallet model specifies signed attribute bundles, direct trust between credential service providers and wallets, relying-party evaluation of issuer information, optional federation authorities, assertion audiences, timestamps, validity windows, nonces, signatures, wallet activation, and status verification. The method is risk-based normative guidance for identity systems rather than a market survey or cryptographic proof. [10]

The model makes two often-hidden dependencies explicit. First, an issuer and relying party do not need direct transaction-by-transaction communication, which can reduce tracking, but the relying party still needs a trust basis for the issuer and its assurance process. Second, a reusable bundle needs limited validity and status handling because facts, accounts, and keys change. The wallet changes the communication topology; it does not remove federation agreements or lifecycle management. [10]

NIST's scope is also a limitation. Its terms and assurance requirements serve the Digital Identity Guidelines and do not mandate one global credential format or one legal trust framework. Deployments outside that context must map their own risks and policy. The author's interpretation is that the guidance is strongest as a checklist of technical obligations that remain necessary when a product description merely says "user-controlled wallet." [6][10]

### Selective-disclosure research shows that privacy properties depend on mechanism and system context

Flamini and coauthors compare widely used cryptographic mechanisms for selective disclosure, including hiding-commitment designs such as ISO mobile documents and non-interactive zero-knowledge proof approaches such as BBS signatures. Their method is a technical analysis of mechanisms, supported features, standard maturity, security considerations, computational properties, and cryptographic agility. The study rejects the idea that "selective disclosure" names one uniform primitive. [14]

The comparison identifies presentation unlinkability as a separate property from hiding attributes. A format can prevent disclosure of an address while still exposing a stable signature, identifier, status reference, or attribute combination that lets verifiers correlate presentations. BBS-derived proofs address signature-level linkage, whereas other mechanisms make different trade-offs in complexity and deployment compatibility. The W3C BBS specification reinforces the system boundary by warning that network artifacts can link otherwise unlinkable cryptographic presentations. [5][14]

The academic paper evaluates designs rather than measuring large population deployments, and some specifications it reviews have continued to evolve. Its value is diagnostic: it supplies dimensions that protocol labels alone omit. The author's synthesis is that a privacy claim should name the protected fields, adversary, linkability scope, verifier behavior, status design, and surrounding metadata. "Supports selective disclosure" without those qualifiers is not a complete privacy result. [5][14][15]

## Implications

### For system architects

Architecture should begin with the decision and evidence required, not with a preferred wallet or identifier. A service asking whether a user is licensed needs to define the authoritative issuer set, acceptable assurance and evidence process, exact attributes or predicates, freshness, status, holder binding, dispute path, and retention policy. Only then should it select credential formats, protocols, identifier methods, and cryptosuites. This sequence prevents a technically valid token from becoming the definition of business trust by accident. [1][7][10]

The worst technical failure is a system that accepts authentic but unauthorized evidence at scale. A signature-valid self-issued credential, an issuer trusted for the wrong credential type, or a status response from an untrusted operator can all pass narrow cryptographic checks. The preventative design is typed trust: bind each accepted issuer to credential types, assurance rules, key-discovery methods, jurisdictions, and validity periods, then log which rule authorized each decision. This paragraph is the author's synthesis from the verifier and trust requirements in the standards. [1][4][10][12]

Data minimization should be enforced in request policy as well as enabled by the credential. A verifier should ask only for claims needed for the decision, prefer derived or threshold claims when available, avoid stable identifiers unless account continuity requires them, and set retention independently of presentation validity. A wallet cannot protect privacy if the verifier's policy demands the whole credential, and selective-disclosure cryptography cannot prevent correlation through unique disclosed values or network metadata. [5][7][12][15]

Profiles should be versioned as deployable contracts. They should state exact versions of OpenID4VCI, OpenID4VP, credential formats, cryptosuites, status mechanisms, query language, verifier-authentication scheme, response security, algorithms, and optional features. Test vectors and conformance suites should accompany the profile. The author's assessment is that a profile change is an API and trust migration, not a documentation update, because wallets, issuers, verifiers, and registries may all need coordinated changes. [6][7][18][19][20]

### For issuers and credential authorities

Issuers carry the semantic burden that cryptography cannot supply. They need documented identity-proofing or evidence processes, clear credential schemas, accurate issuer identifiers, protected signing keys, status operations, incident response, and rules for correction and reissuance. A highly secure signature over weakly established or stale claims produces highly secure misinformation. NIST's assurance model and the EU framework both connect technical assertions to issuance processes and supervision. [10][12]

Key management should separate routine issuance, root trust, recovery, and emergency response. Verification material needs controlled rotation and sufficient overlap for existing credentials, while compromise procedures must explain how verifiers distinguish affected credentials and times. Data Integrity explicitly treats cryptographic agility and layering as security concerns, and DID Core includes update and deactivation concepts for verification methods. The author's synthesis is that long-lived credential programs should inventory algorithms and dependencies so that a cryptographic migration does not require an unplanned identity-system replacement. [2][3]

Status design should be proportionate to the claim. Short-lived credentials can reduce reliance on online revocation but increase issuance frequency and availability dependence. Long-lived credentials reduce routine issuance but require stronger status and key-compromise handling. Shared bitstring lists can improve group privacy over per-credential callbacks, while allocation and caching still require analysis. Issuers should publish status availability objectives and preserve evidence needed to resolve disputes about what status was visible at a transaction time. [4][10]

### For verifiers and relying parties

Verifiers should separate parsing failures, proof failures, expired or revoked status, untrusted issuers, insufficient assurance, missing holder binding, and policy mismatch. This improves security monitoring and avoids teaching operators that every rejection means "bad signature." It also supports appeals: a user whose credential is structurally valid but outside an issuer list faces a governance problem, not a corrupt file. The distinction follows the layered validation behavior in the W3C, OpenID, and NIST specifications. [1][7][10]

Requests should be bound to an authenticated verifier, intended audience, nonce, and short transaction window. Responses should be checked against the original request rather than accepted as generic credentials. OpenID4VP devotes security requirements to replay prevention, client identification, and returned credential checks. A verifier should also constrain redirects, metadata retrieval, algorithm choices, and presentation size because flexible protocol inputs can become attack surfaces even when signatures are correct. [7]

A relying party must decide what happens when infrastructure is unavailable. Status endpoints, issuer metadata, DID resolution, trust registries, and certificate paths can fail independently. Each dependency needs caching, maximum age, fail-open or fail-closed policy, monitoring, and recovery. The author's assessment is that the decision should depend on harm: access to a low-risk personalized service and authorization of a high-value regulated transaction should not inherit the same outage default. [2][4][10]

Relying-party registration and purpose declarations can improve transparency, but they do not automatically prevent overcollection. Technical enforcement can compare requested fields with registered purposes, constrain approved credential types, and make deviations visible to users and auditors. The EU framework provides a concrete model by requiring registration and intended-use information for wallet-relying parties. [12]

### For wallet and platform providers

The wallet is both a cryptographic agent and a safety-critical user interface. Private keys should be protected against extraction, presentations should require clear user action where appropriate, and the interface should authenticate the requester before asking for consent. The screen should translate claim identifiers into understandable data and distinguish required from optional disclosure. NIST, the EU regulation, and the EDPS each treat activation, explicit confirmation, information security, or perceptible disclosure as material controls. [10][12][15]

Wallets should avoid becoming a new universal observer. If every issuer, verifier, credential, and presentation routes through one hosted account, the provider can reconstruct relationships even when the credential format supports unlinkability. Local processing, pairwise identifiers, minimized telemetry, separation of backup from transaction logs, and unobservable transaction design reduce that risk. The EU regulation explicitly calls for provider unobservability, while the EDPS emphasizes data protection by design. [12][15]

Recovery and portability require tested procedures. Users need a way to replace a lost or compromised device, revoke old wallet instances, obtain replacement credentials, and move between approved wallet products without indefinite lock-in. Recovery should not allow a support agent or email compromise to bypass the assurance that protected the original wallet. The author's assessment is that providers should publish recovery threat models and measure successful recovery, fraudulent recovery, and permanent-loss rates separately. [10][12]

Accessibility and exception handling are architectural requirements. A mobile-only flow can exclude people without compatible devices, stable connectivity, vision, dexterity, or the ability to manage authentication factors. Assisted use can create coercion or disclosure risks if helpers gain access to unrelated credentials. The EU framework's user-control and cross-border service goals make alternate channels and scoped delegation relevant even though the exact implementation is deployment-specific. This paragraph is a bounded design implication, not a claim that one standard already solves accessibility. [12]

### For security and privacy reviewers

Threat models should include malicious and compromised issuers, wallets, verifiers, registries, and software-supply dependencies, not only forged signatures. Relevant attacks include issuer-key theft, credential replay, verifier impersonation, request tampering, overbroad disclosure, cloned wallets, compromised recovery, status manipulation, correlation, metadata leakage, downgrade to weak algorithms, and denial of status or resolution services. The cited specifications distribute these risks across security and privacy sections because no single layer controls all of them. [1][2][3][4][5][6][7][15]

Privacy testing should observe complete transactions. Reviewers should record DNS and network connections, wallet and verifier logs, stable identifiers, status-list access, analytics, push notifications, backup traffic, and error reports. Two cryptographically unlinkable presentations can remain operationally linkable through any of these channels. The BBS and EDPS analyses support treating unlinkability as an end-to-end property rather than a feature flag on the signature suite. [5][15]

Conformance, penetration testing, code review, and governance review answer different questions. A conformance suite tests specified protocol behavior. Penetration testing looks for exploitable implementation defects. Code and build review examine software integrity. Governance review examines issuer authorization, certification, incident authority, liability, and appeals. The author's synthesis is that high-assurance deployment needs evidence from all four; passing one cannot substitute for the others. [16][18][19][20]

### For organizations selecting or operating an ecosystem

Procurement should request an interoperability matrix rather than a generic standards list. The matrix should name roles tested, exact versions, profiles, formats, algorithms, status methods, trust-registry integration, offline modes, device platforms, and negative-test results. A vendor certified for an OpenID profile with one format should not be assumed to have exhaustive conformance for the underlying credential format; the OpenID testing guides state this limitation directly. [19][20]

Operational metrics should measure more than successful presentations. Useful measures include issuance completion, failed holder binding, time to revoke, status freshness, recovery success, rejected replay, false rejection by policy, cross-wallet success, accessibility completion, and disclosure size by use case. The author's assessment is that these metrics reveal whether the system delivers portable proof rather than merely generating valid credentials. [4][7][10]

Exit and migration plans should exist before adoption. Credentials may outlive a wallet vendor, cryptosuite, DID method, or profile version. Organizations need rules for reissuance, algorithm deprecation, registry continuity, export, audit evidence, and user communication. A system that is cryptographically decentralized but depends on one proprietary wallet, metadata service, or trust-list operator can still have a concentrated operational failure point. [2][3][11]

### A practical evaluation framework

The author's synthesis is a seven-part evaluation. First, semantics: what exact claim and decision are represented? Second, authority: who may issue and who governs that authorization? Third, assurance: what evidence and holder-binding process support the claim? Fourth, protocol: how are issuance and presentation secured and profiled? Fifth, lifecycle: how do expiration, status, key rotation, recovery, and reissuance work? Sixth, privacy: what is disclosed and what can be linked by each participant? Seventh, operations: how are conformance, incidents, outages, disputes, accessibility, and migration handled? [1][4][6][7][10][12][15]

A design fails if any layer is treated as somebody else's unspecified responsibility. Perfect selective disclosure cannot repair an untrusted issuer. A strong issuer cannot protect a wallet that releases data to an impersonated verifier. A secure wallet cannot make incompatible profiles interoperate. A comprehensive trust registry cannot preserve privacy if status checks reveal each transaction. The durable engineering conclusion is that verifiable credentials are composable evidence, not self-executing trust: portability emerges only when cryptography, semantics, policy, lifecycle, and operations agree. [1][4][5][7][10]

## Sources

1. World Wide Web Consortium. "Verifiable Credentials Data Model v2.0."
   W3C Recommendation, 15 May 2025.
   https://www.w3.org/TR/vc-data-model-2.0/ [high]

2. World Wide Web Consortium. "Decentralized Identifiers (DIDs) v1.0."
   W3C Recommendation, 19 July 2022.
   https://www.w3.org/TR/did-core/ [high]

3. World Wide Web Consortium. "Verifiable Credential Data Integrity 1.0."
   W3C Recommendation, 15 May 2025.
   https://www.w3.org/TR/vc-data-integrity/ [high]

4. World Wide Web Consortium. "Bitstring Status List v1.0."
   W3C Recommendation, 15 May 2025.
   https://www.w3.org/TR/vc-bitstring-status-list/ [high]

5. World Wide Web Consortium. "Data Integrity BBS Cryptosuites v1.0."
   https://www.w3.org/TR/vc-di-bbs/ [high]

6. OpenID Foundation. "OpenID for Verifiable Credential Issuance 1.0."
   Final, 16 September 2025.
   https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html [high]

7. OpenID Foundation. "OpenID for Verifiable Presentations 1.0."
   Final, 9 July 2025.
   https://openid.net/specs/openid-4-verifiable-presentations-1_0-final.html [high]

8. Fett, D., Yasuda, K., and Campbell, B. "Selective Disclosure for
   JSON Web Tokens." RFC 9901, November 2025.
   https://www.rfc-editor.org/rfc/rfc9901.html [high]

9. IETF OAuth Working Group. "SD-JWT-based Verifiable Digital
   Credentials (SD-JWT VC)." Internet-Draft, draft-ietf-oauth-sd-jwt-vc-18.
   https://datatracker.ietf.org/doc/html/draft-ietf-oauth-sd-jwt-vc [high]

10. National Institute of Standards and Technology. "Digital Identity
    Guidelines: Federation and Assertions." NIST SP 800-63C-4, July 2025.
    https://pages.nist.gov/800-63-4/sp800-63c/Wallets [high]

11. European Commission. "EU Digital Identity Wallet Toolbox process."
    https://digital-strategy.ec.europa.eu/en/policies/eudi-wallet-toolbox [high]

12. European Parliament and Council of the European Union. "Regulation
    (EU) 2024/1183 establishing the European Digital Identity Framework."
    11 April 2024.
    https://eur-lex.europa.eu/eli/reg/2024/1183/oj [high]

13. International Organization for Standardization. "ISO/IEC
    18013-5:2021 - Personal identification - ISO-compliant driving
    licence - Part 5: Mobile driving licence (mDL) application."
    https://www.iso.org/standard/69084.html [high]

14. Flamini, A., Sciarretta, G., Scuro, M., Sharif, A., Tomasi, A., and
    Ranise, S. (2024). "On Cryptographic Mechanisms for the Selective
    Disclosure of Verifiable Credentials."
    https://arxiv.org/abs/2401.08196 [high]

15. European Data Protection Supervisor. "TechDispatch #3/2025 -
    Digital Identity Wallets." 15 December 2025.
    https://www.edps.europa.eu/data-protection/our-work/publications/techdispatch/2025-12-15-techdispatch-32025-digital-identity-wallets [high]

16. European Union Agency for Cybersecurity. "EU Digital Identity
    Wallet: A leap towards secure and trusted electronic identification
    through certification." 24 September 2024.
    https://www.enisa.europa.eu/news/eu-digital-identity-wallet-a-leap-towards-secure-and-trusted-electronic-identification-through-certification [high]

17. World Wide Web Consortium. "Verifiable Credentials Data Model 1.0."
    W3C Recommendation, 19 November 2019.
    https://www.w3.org/TR/2019/REC-vc-data-model-20191119 [high]

18. World Wide Web Consortium. "VC v2.0 Interoperability Report."
    https://w3c.github.io/vc-data-model-2.0-test-suite [high]

19. OpenID Foundation. "OpenID Foundation completes conformance
    programme for widely adopted digital identity standards."
    7 August 2026.
    https://openid.net/oidf-completes-conformance-programme-for-widely-adopted-digital-identity-standards [high]

20. OpenID Foundation. "Conformance Testing for OpenID for Verifiable
    Presentations" and "Conformance Testing for OpenID for Verifiable
    Credential Issuance."
    https://openid.net/certification/conformance-testing-for-openid-for-verifiable-presentations
    https://openid.net/certification/conformance-testing-for-openid-for-verifiable-credential-issuance/ [high]

## See Also

- `library/technology/cybersecurity-principles-threats-and-defense-in-depth.md` -- places wallet, verifier, issuer, registry, and recovery controls within a layered threat model.
- `library/technology/blockchain-distributed-ledgers.md` -- explains one possible registry substrate while clarifying why digital credentials do not inherently require a blockchain.
- `library/technology/post-quantum-cryptography-migration.md` -- develops the cryptographic-agility and migration problem for long-lived identity infrastructure.
- `library/technology/internet-tcpip-protocols-routing.md` -- provides the network foundation whose identifiers and metadata can undermine presentation unlinkability.
