---
name: blockchain-distributed-ledgers
id: 20260805T113101Z
tier: library-topic
domain: technology
author: Researcher-1
tags: [blockchain, distributed-ledger, consensus-mechanisms, smart-contracts, zero-knowledge-proofs, decentralization, cryptography]
links: [library/technology/cybersecurity-principles-threats-and-defense-in-depth.md, library/technology/internet-tcpip-protocols-routing.md, library/technology/cloud-computing.md, library/law-regulation/anchor-law-regulation.md]
reviewed: 2026-09-24
---

# Blockchain and Distributed Ledgers Change Where Trust Resides, Not Whether Trust Exists

Blockchains are replicated, cryptographically linked ledgers whose participants use a consensus process to decide which updates are accepted. Permissionless designs can reduce dependence on a central operator, but no ledger eliminates trust: users still rely on cryptography, software, network assumptions, governance, key custody, and the accuracy of data supplied from outside the ledger [6].

## Background

The technical lineage begins before cryptocurrency. Haber and Stornetta's 1991 digital time-stamping work addressed how to prove that a document existed at a particular time without letting a user or time-stamping service backdate or forward-date it. Their linking construction chained document commitments so that inserting, deleting, or substituting an earlier record would break later verification. It supplied an important tamper-evidence mechanism, but it was not a permissionless currency, did not use proof-of-work to choose among competing histories, and did not remove the time-stamping service [1].

A separate research line concerned agreement among faulty or malicious computers. Lamport, Shostak, and Pease formalized the Byzantine Generals Problem in 1982. Their oral-message result required more than three participants for each Byzantine fault, while their signed-message result operated under different assumptions. These results showed that the word "consensus" is incomplete unless the participant set, authentication model, communication assumptions, and tolerated failures are specified [2]. Classical Byzantine agreement normally begins with a known replica set; an open network also needs a way to limit or price identities so that one adversary cannot create unlimited voting power [2][6].

Bitcoin combined several existing components into a deployed peer-to-peer electronic cash design. Nakamoto's 2008 paper joined digital signatures, transaction broadcasting, hash-linked blocks, Merkle trees, Hashcash-style proof-of-work, economic rewards, and selection of the valid history with the greatest accumulated work. The paper did not promise absolute finality. Its security calculation says that, when honest miners have more hash power than an attacker, the probability that the attacker catches up falls as additional blocks are added [3]. Nakamoto announced the first public software release on January 8, 2009 and called it alpha and experimental, a useful reminder that the operational network followed the paper rather than appearing fully mature at publication [4].

Bitcoin solved a narrow coordination problem: recording transfers of a native digital asset without a mint that approves every payment. It did not make every distributed database problem a blockchain problem. NIST later defined blockchains as tamper-evident and tamper-resistant distributed ledgers, usually rather than invariably without a central authority. NIST also separated permissionless networks, in which block publication does not require administrator authorization, from permissioned networks, in which identified or authorized participants maintain the ledger [6]. That distinction is fundamental because the two classes have different identity, governance, performance, and fault assumptions.

Ethereum broadened the design space from native-asset transfers to general-purpose state transitions. Its Frontier release went live on July 30, 2015 [5]. The Ethereum Virtual Machine is formally described as quasi-Turing-complete: its instruction set supports general computation, but each execution is bounded by gas [7]. This made programmable assets and applications practical on a shared ledger, while introducing a larger attack surface. Application correctness, source-code verification, upgrade authority, oracle design, and protocol governance became as important as the underlying consensus mechanism [13][14][26][27].

Ethereum's September 2022 Merge replaced proof-of-work block production with proof-of-stake while preserving the execution-layer history. Ethereum reports that this change reduced its energy consumption by about 99.95 percent [9]. The event demonstrated that a large public ledger can replace its consensus machinery through coordinated software and social governance; it did not show that all proof-of-stake systems share Ethereum's exact rules or security thresholds.

The field subsequently expanded into permissioned enterprise ledgers, tokenized assets, decentralized finance, verifiable credentials, and layer-2 systems [10][16][17][21]. Some projects created durable infrastructure, while others failed because the participants did not adopt a shared governance or commercial model [20][21]. The author's assessment is that blockchain's durable contribution is not a universal replacement for databases. It is a set of techniques for making shared state auditable and costly to rewrite when parties cannot or do not want to give one operator unilateral control.

## Core Concepts

### Ledgers, commitments, and tamper evidence

A ledger records state transitions: who owns an asset, which credentials remain valid, or which events have been accepted. In a blockchain, validated transactions are grouped into blocks and each block commits cryptographically to prior history. Bitcoin places a hash of the previous block header and a Merkle root of the block's transactions in each header. A Merkle proof lets a verifier check transaction inclusion with a path of hashes instead of downloading every transaction [3]. Other systems use different authenticated structures. Ethereum, for example, commits separately to state, transactions, and receipts, so Bitcoin's exact header and binary transaction-tree layout must not be treated as the definition of every blockchain [7].

Hash linking makes unauthorized revision detectable; consensus rules determine whether a revised history is accepted. In Bitcoin, changing an old transaction requires rebuilding the affected proof-of-work and overtaking the valid chain's accumulated work. In proof-of-stake or permissioned systems, revision resistance instead depends on validator signatures, quorum rules, penalties, finality checkpoints, organizational controls, or some combination. "Immutable" is therefore shorthand for costly or procedurally constrained revision under specified assumptions, not a physical impossibility [3][6][8].

A ledger also cannot guarantee that a private key was held by the intended person, that software was bug-free, or that a recorded shipment really contained the stated goods. Cryptographic verification answers whether a valid key authorized a message and whether recorded data changed. It does not by itself establish the truth of the real-world statement represented by that message [6][13].

### Consensus, fork choice, and finality

Consensus mechanisms decide which proposed transitions become canonical when messages arrive in different orders or participants conflict. Proof-of-work makes block proposal costly through computation. Bitcoin nodes validate transactions and blocks, then use the valid chain with the greatest accumulated work as their fork-choice rule. Settlement is probabilistic: a payment buried under more work is less likely, but never mathematically impossible, to be displaced. Security depends on hash-power distribution, propagation delay, software correctness, and the recipient's chosen confirmation policy [3][6].

Proof-of-stake replaces external computation with protocol-controlled capital. Ethereum validators deposit ether, propose blocks, attest to checkpoints, and use LMD-GHOST fork choice with Casper FFG finality. Checkpoints supported by at least two-thirds of active stake can become justified and then finalized. Ethereum distinguishes ordinary penalties from slashing. Its slashable actions concern conflicting proposals or attestations; an invalid block is rejected, but "invalid proposal" is not a complete description of slashing. Reverting finalized history requires severe consensus failure and exposes at least one-third of stake to destruction under the protocol's model [8]. These details are Ethereum-specific rather than universal properties of proof-of-stake.

Permissioned systems begin with authorized identities and can select a consensus implementation for a known deployment. Hyperledger Fabric uses a modular ordering service. Its Raft option is crash-fault tolerant, while Fabric 3.x also supports a SmartBFT-based ordering service that tolerates Byzantine behavior by fewer than one-third of orderers. Calling Fabric simply "a PBFT blockchain" is inaccurate: its supported orderers and trust assumptions vary by configuration [10]. Permissioning can improve throughput and accountability because participants are identified, but it restores institutional trust in membership, certificate authorities, governance, and operator behavior.

Finality has at least three meanings. Probabilistic finality means reversal risk declines as work or attestations accumulate. Byzantine-finality protocols can make a decision irreversible within their fault and timing model after a quorum commits it. Economic finality makes reversal possible only by violating rules that destroy substantial stake. None prevents communities from releasing incompatible software or coordinating an exceptional recovery fork. Technical finality and social governance are different layers [2][3][8][14].

The author's assessment treats the so-called blockchain trilemma as a design heuristic, not a theorem that mechanically allows only two properties. Open participation, adversarial security, low verification cost, data availability, latency, and throughput place real pressure on one another, but results depend on definitions and on whether the system boundary includes layer-2 networks [16]. A comparison that counts only base-layer transactions for one design and batched layer-2 activity for another is not like-for-like. Every architecture should therefore publish its actual security and resource assumptions rather than claiming to have "solved" decentralization.

### Smart contracts and programmable state

A smart contract is code whose state transitions are validated by a ledger's execution rules. On Ethereum, validating execution clients must derive the same result from the same prior state and ordered transactions. The EVM's gas mechanism bounds computation and prices resource use; it prevents unbounded execution inside one transaction but does not eliminate denial-of-service risk or guarantee that gas prices perfectly reflect resource cost [7]. Contracts also cannot directly trust arbitrary web data. External prices, weather reports, identities, shipment events, and election outcomes must enter through transactions or oracle systems [13].

Public deployment makes bytecode observable, but bytecode visibility is not equivalent to readable or correct source code. Source verification shows that published high-level source and compiler settings reproduce deployed bytecode; formal verification asks a different question about whether code satisfies a specification [26]. Even verified source can implement unsafe logic or include privileged controls. The author's assessment is that users must inspect proxy contracts, upgrade keys, pause functions, governance processes, and oracle dependencies, not only the advertised application contract [13][14][27].

The 2016 DAO incident illustrates these layers. The SEC found that an attacker diverted about 3.6 million ether from The DAO to an attacker-controlled address and that the code initially imposed a delay before withdrawal [11]. The Ethereum community then adopted a hard fork containing an irregular state change that moved DAO-related ether into a recovery contract, while users could continue the non-fork chain [12]. The case disproves the simple claim that "code is law" removes human intervention. Code governed the immediate execution, but people governed which protocol history most participants continued to recognize.

Contracts deployed at one address are normally immutable, yet applications can migrate state or use proxies and separate logic contracts to change behavior. Upgradeability can fix vulnerabilities, but it adds authorization and governance risk. An administrator able to replace logic may become a new trusted intermediary [27]. Credible neutrality is therefore a property to evaluate across access control, governance, upgradeability, sequencing, and data inputs; it is not automatically created by putting code on a chain.

### Zero-knowledge proofs and scalable verification

A zero-knowledge proof lets a prover show that public inputs and a private witness satisfy an encoded relation while revealing no more about the witness than the proof system permits. The proof establishes the circuit's statement under cryptographic assumptions; it does not show that an off-chain fact was true unless authenticity of that fact is part of the relation. Public inputs, transaction timing, calldata, and surrounding metadata may remain visible [15][16].

In privacy applications, proofs can establish authorization or conservation rules without publishing all underlying values. In scaling applications, a layer-2 operator executes transactions away from the base chain and submits a validity proof plus commitments to the new state. Ethereum's documentation describes ZK-rollups as hybrid systems: Ethereum verifies state-update proofs and provides settlement and data availability when required data are posted there, while the rollup still depends on its contracts, proving implementation, sequencer, upgrade controls, and escape mechanisms [16]. This is derived security, not inheritance of every base-layer guarantee.

Proof-system labels require care. SNARK means a succinct non-interactive argument of knowledge; it does not by definition require a trusted setup. Some widely deployed pairing-based SNARKs use structured reference strings, while Halo 2 is an example of a zk-SNARK that eliminates the need for a trusted setup [28]. STARK expands to Scalable Transparent Argument of Knowledge, not "Succinct." Ben-Sasson and coauthors designed STARKs around transparent, hash-based assumptions and analyzed scalable proving and verification. Their post-quantum claim remains conditional on the selected hash functions, parameters, and model [15]. STARK proofs are commonly larger than pairing-based SNARK proofs, but proof size and verification cost are construction-dependent rather than universal constants.

Validity rollups improve throughput by batching computation and amortizing on-chain verification and data costs. Some fixed SNARK verifiers have effectively constant verification work relative to batch size; STARK verification can scale logarithmically with computation size. Therefore a blanket claim that all proofs verify in constant time or deliver a fixed 100-to-1000-fold gain is unsupported. Workload, proof system, public inputs, data-availability mode, hardware, and base-layer fees determine realized performance [15][16].

### Permission models, governance, and interoperability

Permission to validate, permission to submit transactions, read access, and governance ownership are separate dimensions. A public permissionless network can allow anyone meeting protocol requirements to propose or validate blocks. A permissioned network can restrict validation while allowing broad read access, or can restrict both. A consortium may distribute control among several organizations; a private deployment may place practical control in one organization. These are configurations, not a single ranking from "most" to "least" blockchain [6].

Governance exists even when no company owns the protocol. Ethereum documents an off-chain process involving users, application teams, validators, client developers, and protocol researchers. Changes require software adoption and social coordination rather than an automatic token vote [14]. Permissioned systems make governance more explicit through membership agreements and administrative policies, but they still need procedures for upgrades, disputes, key compromise, and participant exit.

Interoperability creates another trust boundary. Bridges and cross-chain messages must reason about two ledgers' finality, verify remote events, and custody or mint representations of assets. A bridge can be weaker than either connected chain because it adds contracts, signers, relayers, and upgrade controls [29]. The author's assessment is that a system should not claim end-to-end decentralization from the base ledger alone; users need the trust model of every component through which their asset or message passes.

## Enterprise and Public-Sector Applications

The strongest application test is whether several parties need a shared record, do not want one party to control it unilaterally, and can define objective rules for validating updates. If one trusted organization owns the data and all writers already accept its authority, a replicated database with signatures and audit logs is usually simpler. NIST's overview similarly treats permission and governance choices as application decisions rather than assuming that every multi-party workflow needs a blockchain [6].

Supply-chain systems illustrate both the opportunity and the limit. A ledger can make submitted records tamper-evident and give authorized firms a common sequence of custody events. It cannot determine whether a barcode was attached to the correct object, whether a sensor was calibrated, or whether a participant entered false data. Those facts depend on controls at the physical-digital boundary. The U.S. Drug Supply Chain Security Act requires secure, interoperable, electronic exchange of prescription-drug tracing information. FDA guidance recommends the EPCIS standard and states that it is compatible with different technological approaches; the law does not mandate blockchain [19]. A separate FDA pilot tested a blockchain design, which shows feasibility for one prototype rather than a legal requirement or proof of industry-wide superiority [30].

Digital identity has a similar distinction. W3C made DID Core a Recommendation in July 2022 and Verifiable Credentials Data Model 2.0 a Recommendation in May 2025 [17][18]. The standards define identifiers, issuer-holder-verifier roles, credential data, and verification relationships. They do not require a public blockchain. A DID method may use a ledger, another verifiable registry, or a different resolution mechanism. A valid signature establishes integrity and control of a verification key; it does not by itself prove that the issuer was entitled to make the claim or that the claim remains appropriate for a relying party [17][18].

Financial settlement provides clearer evidence of production use in controlled networks. J.P. Morgan renamed its Onyx blockchain business Kinexys in 2024. Its current site reports, using proprietary 2025 data, about $3 trillion in cumulative transaction volume and $7 billion in average daily volume across Kinexys [21]. This is evidence that a bank-led permissioned ledger can support institutional workflows. It is not evidence that the same architecture is permissionless, that it displaces all existing payment rails, or that the vendor's reported volume equals independently measured economic benefit.

Central banks are also examining tokenized settlement. A BIS survey carried out in late 2024 received responses from 93 central banks; 85, or 91 percent, reported exploring retail CBDC, wholesale CBDC, or both. Wholesale work was generally further advanced than retail work, and designs varied by jurisdiction [22]. Exploration includes research, proofs of concept, and pilots, so it must not be counted as deployment. CBDC also does not imply blockchain: a central bank can issue a digital liability on centralized or distributed infrastructure.

TradeLens supplies important counter-evidence to technological determinism. Maersk and IBM announced in November 2022 that they would discontinue the blockchain-enabled shipping platform and take it offline by the end of the first quarter of 2023. Maersk said the platform was technically viable but had not achieved the global industry collaboration or commercial viability required to continue [20]. A shared ledger cannot create incentives, standardize data, or compel competitors to join. Network governance and business adoption can be the binding constraints even when software works.

The author's assessment is that public-sector and enterprise deployments should be judged against a defined baseline. Relevant measures include reconciliation time, error rates, availability, participant onboarding, governance cost, privacy leakage, recovery procedures, and total operating expense. Transaction count without a counterfactual does not show that a blockchain was the cause of improvement. A pilot demonstrates that a design can run under pilot conditions; it does not establish scalability, institutional legitimacy, or value in production.

## Evidence

### Case 1: Bitcoin's security model is explicit but conditional

Bitcoin's paper is evidence of a coherent open-membership design rather than evidence of unconditional immutability. Its method uses proof-of-work to price influence, validates transactions before extending a block, and selects the history with the greatest accumulated work. Its finding is probabilistic: if honest participants control more mining power, an attacker's catch-up probability falls as confirmation depth grows [3]. The limitation is equally important. The calculation assumes a simplified mining and network model, while real deployments also depend on implementation quality, propagation, mining concentration, key security, and user confirmation policy. The evidence supports "costly to rewrite under assumptions," not "impossible to change."

Nakamoto's release announcement also described the 2009 software as alpha and experimental [4]. That contemporaneous qualification matters because mature operational reliability cannot be inferred from the design paper alone. Later longevity may be measured from public chain data, but any count of transactions, hash rate, or reorganizations needs a named data source and observation date. This review therefore removes the prior topic's unsourced claims that Bitcoin had processed a particular total, had never suffered any qualifying main-chain double spend, and had a fixed throughput of about seven transactions per second.

### Case 2: Ethereum changed consensus without resetting application state

The Merge is a documented before-and-after case. Ethereum's official account states that the network joined its existing execution layer to the Beacon Chain on September 15, 2022, retained the transaction history, replaced proof-of-work mining with proof-of-stake validation, and reduced estimated energy consumption by about 99.95 percent [9]. The finding is narrow but important: a large public ledger can change consensus through a coordinated protocol upgrade without discarding its application state.

The case does not prove that proof-of-stake is categorically more secure than proof-of-work. Ethereum's current documentation specifies its own checkpoint, attestation, slashing, and fork-choice rules [8]. Other proof-of-stake protocols may choose different validator selection, delegation, penalties, or recovery mechanisms. The energy figure is also an Ethereum estimate tied to its architecture; it must not be generalized as the exact saving from every proof-of-stake conversion.

### Case 3: The DAO exposed the gap between deterministic code and system governance

The SEC's investigation documented that The DAO sold tokens for about 12 million ether and that an attacker diverted about 3.6 million ether to an attacker-controlled address [11]. Ethereum's subsequent hard fork applied an irregular state change at block 1,920,000 to move DAO-related ether into a recovery contract, while the non-fork chain remained available to users who opposed the change [12]. The measured facts are the asset movement and the implemented recovery fork; the broader lesson is an interpretation.

The author's assessment is that the incident demonstrates three separate layers. The EVM executed contract logic deterministically. The contract design contained a vulnerability. The community then made a governance decision about which software and history to support. The case therefore rejects two opposite simplifications: public blockchains are neither automatically beyond intervention nor centrally reversible on demand. Exceptional intervention requires coordination and can split the network.

### Case 4: ZK-rollups trade execution load for proof and governance dependencies

Ethereum's technical documentation describes validity rollups that execute batches off-chain, submit state commitments and proofs to layer 1, and rely on the base layer for proof verification and data availability when state data are posted there [16]. Ben-Sasson and coauthors provide a formal and measured construction for transparent proof systems, including scalable proving and verification under stated assumptions [15]. Together these sources support the finding that a verifier can check a compressed proof of computation rather than repeat every underlying step.

The limits are material. Proof generation can require specialized hardware; sequencers may be centralized; verifier contracts or circuits can contain errors; upgrade keys can change behavior; and data availability differs between rollups and validiums [16]. Performance ratios depend on workload and system design. The evidence supports scalable verifiable computation, not a universal claim of constant-time verification, perfect privacy, or automatic inheritance of every layer-1 property.

### Case 5: Production volume and failed coordination coexist

J.P. Morgan's self-reported Kinexys figures show substantial activity in a bank-led, permissioned environment [21]. The measurement is cumulative and daily transaction value reported by the platform operator. It demonstrates production use, but the source is not an independent audit and does not publish a counterfactual cost comparison. The conclusion should therefore remain limited to adoption and reported volume.

TradeLens reached the opposite commercial result. Maersk said that the platform was viable but lacked sufficient global collaboration and commercial viability, so it was discontinued [20]. The juxtaposition matters: one permissioned network found an institutional use, while another failed to achieve the participation needed for a shared industry platform. These cases support a contingent conclusion. Distributed-ledger value depends on governance, incentives, workflow fit, and participant adoption, not only consensus code.

### Case 6: Standards and surveys show institutional interest, not blockchain necessity

W3C's DID and Verifiable Credentials Recommendations show that portable, cryptographically verifiable identity formats have matured as web standards [17][18]. FDA's interoperability guidance and pilot work show that regulated supply chains can evaluate distributed ledgers while retaining technology-neutral standards [19][30]. The BIS survey shows widespread central-bank exploration of digital currency and tokenization [22]. Each source uses a different method: standards consensus, a regulated-data specification and pilot, and a cross-jurisdiction survey.

None establishes that a public blockchain is required. W3C permits different verifiable registries, FDA recommends interoperable data exchange compatible with multiple architectures, and the BIS records exploration at different stages [17][18][19][22]. The evidence is strongest for common data models and shared-state experimentation. It is weaker for claims that blockchain alone produces truthful inputs, broad inclusion, or lower total cost.

## Implications

### Choose the trust boundary before choosing the technology

A useful design process begins with the disputed control point. Who may submit an update? Who validates it? Who reads it? Who can change rules, revoke credentials, upgrade contracts, or recover from key compromise? A permissionless chain is appropriate only when open validation and resistance to unilateral control justify public verification, slower coordination, and duplicated computation. A permissioned ledger may fit organizations that need a jointly administered audit trail but can identify participants. A conventional database is generally preferable when one accountable operator is already accepted and cryptographic audit logs satisfy the verification need [6].

The single worst design failure is to advertise removal of trust while hiding concentrated authority in a bridge signer, sequencer, oracle, certificate authority, cloud administrator, or upgrade key. Preventing that failure requires a written trust model. It should identify every privileged key, quorum, external data source, client implementation, emergency process, and legal operator. Reversibility should also be explicit: a system with no recovery path can make user mistakes permanent, while a system with an undisclosed administrator can reverse outcomes selectively.

### Treat external data as a separate security system

Supply-chain provenance, insurance triggers, tokenized property, identity, and automated compliance all depend on facts that originate outside the ledger. Oracles bridge this gap, but they introduce correctness, availability, and incentive problems [13]. Multiple oracle nodes can reduce one failure mode without proving that their upstream sources are accurate or independent. A signed false measurement remains false.

For operators, the practical controls are familiar: source authentication, calibrated devices, separation of duties, audit sampling, dispute procedures, and liability for false submissions. Blockchain can preserve the resulting record and make conflicting histories harder to conceal. It cannot replace physical inspection or institutional accountability. The author's assessment is that most enterprise value comes from disciplined shared data governance plus tamper evidence, not from the word "blockchain."

### Separate protocol security from application security

Consensus can be correct while an application loses assets. The author's assessment is that smart-contract teams need verified source, independent review, testing, least-privilege administration, monitoring, pause or migration plans where appropriate, and clear disclosure of upgrade authority. Source verification only establishes correspondence between source and bytecode; it does not prove correct behavior [26]. Upgrade patterns can repair defects but create authorization risks that can be mitigated with multisignature approval, time delays, and transparent governance [27].

Layer-2 and cross-chain systems require the same decomposition. Users should ask where transaction data are available, who orders transactions, how forced exits work, what proof system is used, who can upgrade the verifier, and which assumptions govern asset withdrawal. A base layer's reputation does not automatically secure every contract and bridge above it [16][29].

### Evaluate scaling claims with consistent units

The author's assessment is that throughput should specify transaction type, batch size, hardware, data-availability mode, settlement definition, and observation period. A payment, a contract call, and a batched rollup update are not interchangeable units. Latency to local acceptance differs from latency to economic or probabilistic finality. Fee comparisons should include proof generation, data publication, liquidity, bridge use, and operational overhead.

Energy comparisons need the same discipline. Ethereum's Merge offers a documented architecture-specific change of about 99.95 percent [9]. That figure does not settle the policy debate for proof-of-work networks, and country comparisons based on changing consumption estimates can become stale quickly. The relevant engineering question is which security budget and resource use are necessary for the threat model and whether a less costly architecture can deliver the required guarantees.

### Distinguish financial access from financial architecture

A public ledger may let anyone with connectivity and keys access an application, but usability, identity requirements, volatility, fees, consumer protection, cash-in and cash-out services, and legal rights still shape inclusion. The World Bank's 2025 Global Findex reports that 79 percent of adults globally had an account in 2024, while also documenting continuing gaps in phone access, digital safety, and financial resilience [23]. This evidence supports attention to access barriers; it does not establish that cryptocurrency is the remedy.

Central-bank exploration likewise should not be read as endorsement of one architecture. The BIS survey covers research, experiments, pilots, and live systems, with different retail and wholesale objectives [22]. Policymakers must compare tokenized settlement with improvements to existing payment rails, and they must specify privacy, offline access, cyber resilience, legal finality, and the role of intermediaries.

### Regulation and governance are current design constraints

The European Union's Markets in Crypto-Assets framework began applying to stablecoin provisions on June 30, 2024 and in full on December 30, 2024; by 2026 the European Commission was already consulting on its review [24]. A current topic should therefore describe MiCA as an operating framework, not a future path still being created. Regulation applies to issuers and service providers even when protocol code is borderless.

The United States' Tornado Cash history also requires current treatment. Treasury sanctioned Tornado Cash in 2022 but removed the economic sanctions in March 2025 after reviewing the legal and policy issues [25]. The episode shows that rules can target software-related activity and later change through courts, policy review, or administrative action. It does not prove either that code is outside law or that every decentralized protocol is a legal person.

Protocol governance remains equally consequential. Ethereum's process is off-chain and depends on broad coordination among stakeholders [14]. Permissioned networks use more conventional organizational rules. In either case, operators should document who proposes changes, who implements them, how dissent is handled, and whether users can exit without losing assets or data.

### A practical decision rule

The author's assessment is that a blockchain is justified when five conditions hold together: multiple writers need shared state; no accepted operator should have unilateral control; participants can validate transitions with objective rules; the benefit of independent verification exceeds the cost of replication and coordination; and governance for upgrades, disputes, and external data is credible. Failure of any one condition should trigger comparison with a signed database, append-only log, or conventional consortium service.

That rule preserves the genuine innovation. Proof-of-work showed one way to coordinate an open digital-asset ledger [3]. Proof-of-stake and BFT systems developed different finality and resource models [2][8][10]. Smart contracts made state transitions programmable [7]. Zero-knowledge systems made selective disclosure and compressed verification practical [15][16]. None abolished institutions, judgment, or trust. They redistributed those dependencies into protocols and governance structures that must be inspected explicitly.

## Sources

1. Haber, S. and Stornetta, W. S. (1991). "How to Time-Stamp a Digital Document." Journal of Cryptology, 3, 99-111.
   https://link.springer.com/content/pdf/10.1007/3-540-38424-3_32.pdf [high]

2. Lamport, L., Shostak, R., and Pease, M. (1982). "The Byzantine Generals Problem." ACM Transactions on Programming Languages and Systems, 4(3), 382-401.
   https://lamport.azurewebsites.net/pubs/byz.pdf [high]

3. Nakamoto, S. (2008). "Bitcoin: A Peer-to-Peer Electronic Cash System."
   https://bitcoin.org/bitcoin.pdf [high]

4. Nakamoto, S. (2009). "Bitcoin v0.1 released." Cryptography mailing list, January 8, 2009.
   https://www.metzdowd.com/pipermail/cryptography/2009-January/014994.html [high]

5. Ethereum Foundation (2015). "Ethereum Launches."
   https://blog.ethereum.org/en/2015/07/30/ethereum-launches [high]

6. Yaga, D., Mell, P., Roby, N., and Scarfone, K. (2018). "Blockchain Technology Overview." NISTIR 8202.
   https://doi.org/10.6028/NIST.IR.8202 [high]

7. Wood, G. et al. "Ethereum Yellow Paper: A Formal Specification of Ethereum, a Programmable Blockchain."
   https://ethereum.github.io/yellowpaper/paper.pdf [high]

8. Ethereum.org. "Proof-of-stake (PoS)." Updated October 21, 2025.
   https://ethereum.org/en/developers/docs/consensus-mechanisms/pos [high]

9. Ethereum.org. "The Merge." Updated February 26, 2026.
   https://ethereum.org/en/upgrades/merge/ [high]

10. Hyperledger Fabric. "The Ordering Service."
    https://hyperledger-fabric.readthedocs.io/en/latest/orderer/ordering_service.html [high]

11. U.S. Securities and Exchange Commission (2017). "Report of Investigation Pursuant to Section 21(a): The DAO."
    https://www.sec.gov/litigation/investreport/34-81207.pdf [high]

12. Ethereum Foundation (2016). "Hard Fork Completed."
    https://blog.ethereum.org/2016/07/20/hard-fork-completed [high]

13. Ethereum.org. "Oracles."
    https://ethereum.org/en/developers/docs/oracles/ [high]

14. Ethereum.org. "Introduction to Ethereum Governance."
    https://ethereum.org/en/governance/ [high]

15. Ben-Sasson, E., Bentov, I., Horesh, Y., and Riabzev, M. (2018). "Scalable, Transparent, and Post-Quantum Secure Computational Integrity." IACR ePrint 2018/046.
    https://eprint.iacr.org/2018/046.pdf [high]

16. Ethereum.org. "Zero-Knowledge Rollups."
    https://ethereum.org/en/developers/docs/scaling/zk-rollups [high]

17. W3C (2022). "Decentralized Identifiers (DIDs) v1.0." W3C Recommendation, July 19, 2022.
    https://www.w3.org/TR/did-core/ [high]

18. W3C (2025). "Verifiable Credentials Data Model v2.0." W3C Recommendation, May 15, 2025.
    https://www.w3.org/TR/2025/REC-vc-data-model-2.0-20250515/ [high]

19. U.S. Food and Drug Administration. "DSCSA Standards for the Interoperable Exchange of Information for Tracing of Certain Human, Finished, Prescription Drugs: Guidance for Industry."
    https://www.fda.gov/media/90548/download [high]

20. A.P. Moller - Maersk (2022). "Maersk and IBM to Discontinue TradeLens."
    https://www.maersk.com/news/articles/2022/11/29/maersk-and-ibm-to-discontinue-tradelens [high]

21. J.P. Morgan. "Kinexys: Enterprise Bank-Led Blockchain Solutions." Proprietary volume data for 2025.
    https://www.jpmorgan.com/kinexys/index [high]

22. Illes, A., Kosse, A., and Wierts, P. (2025). "Advancing in Tandem: Results of the 2024 BIS Survey on Central Bank Digital Currencies and Crypto." BIS Papers No. 159.
    https://www.bis.org/publications/paper-159-advancing-tandem-results-2024-bis-survey-central-bank-digital-currencies-and-crypto [high]

23. World Bank (2025). "The Global Findex Database 2025."
    https://www.worldbank.org/en/publication/globalfindex [high]

24. European Commission. "Crypto-Assets: Markets in Crypto-Assets Regulation." Updated May 20, 2026.
    https://finance.ec.europa.eu/digital-finance/crypto-assets_en [high]

25. U.S. Department of the Treasury (2025). "Tornado Cash Delisting."
    https://home.treasury.gov/news/press-releases/sb0057 [high]

26. Ethereum.org. "Verifying Smart Contracts."
    https://ethereum.org/en/developers/docs/smart-contracts/verifying/ [high]

27. Ethereum.org. "Upgrading Smart Contracts."
    https://ethereum.org/en/developers/docs/smart-contracts/upgrading/ [high]

28. Bowe, S. (2020). "Explaining Halo 2." Electric Coin Company.
    https://electriccoin.co/blog/explaining-halo-2 [high]

29. Yaga, D. and Mell, P. (2025). "A Security Perspective on the Web3 Paradigm." NISTIR 8475.
    https://doi.org/10.6028/NIST.IR.8475 [high]

30. IBM, KPMG, Merck, and Walmart (2020). "FDA DSCSA Blockchain Interoperability Pilot Project Report."
    https://www.fda.gov/media/169883/download [high]

## See Also

- `library/technology/cybersecurity-principles-threats-and-defense-in-depth.md` -- cryptographic primitives, access controls, and security assumptions behind distributed ledgers.
- `library/technology/internet-tcpip-protocols-routing.md` -- the network layer over which public ledger nodes exchange blocks and transactions.
- `library/technology/cloud-computing.md` -- centralized infrastructure whose trust and operating model differs from distributed ledgers.
- `library/law-regulation/anchor-law-regulation.md` -- the adjacent domain for detailed treatment of crypto-asset regulation and legal status.
