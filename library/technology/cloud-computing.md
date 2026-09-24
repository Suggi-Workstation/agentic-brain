---
name: cloud-computing
id: 20260726T133103Z
tier: library-topic
domain: technology
author: Researcher-1
tags: [cloud-computing, iaas, paas, saas, serverless, microservices, infrastructure]
links: [library/technology/large-language-models.md, library/technology/cybersecurity-principles-threats-and-defense-in-depth.md]
reviewed: 2026-09-24
---

# Cloud Computing -- Renting Shared Infrastructure Changes Costs, Control, and Software Operations

Cloud computing provides on-demand network access to pooled computing resources that can be provisioned and released rapidly, usually with metered usage. It can replace, supplement, or interoperate with owned infrastructure; its central trade-off is faster access to scalable services in exchange for shared responsibility, variable costs, and dependence on provider interfaces and operating choices [1][2].

## Background

Cloud computing joined several older ideas rather than appearing as a single invention. In 1961, John McCarthy described a future in which computation might be organized as a public utility and subscribers would pay for the capacity they used. Time-sharing systems were already turning scarce mainframes into shared services: IBM's CP-40 project began in 1964, CP-67 was supplied to selected time-sharing customers in 1967, and VM/370 was announced in 1972. These systems established that one physical computer could present multiple isolated computing environments to users, decades before the modern public-cloud market [3][4].

Virtualization therefore did not originate in the late 1990s. The later breakthrough was practical virtualization on commodity x86 machines. VMware Workstation brought that capability to x86 in 1999 even though the architecture had not been designed for traditional virtualization. Virtual machines became a major mechanism for isolation, consolidation, and automated provisioning in early infrastructure clouds, but they are not a defining requirement of cloud computing. NIST defines cloud through on-demand self-service, broad network access, resource pooling, rapid elasticity, and measured service; providers can implement those properties with virtual machines, containers, bare-metal allocation, or other mechanisms [1][5].

Networking, distributed systems, automation, and large datacenters were equally important. The public Internet supplied broad access, while provider APIs converted capacity planning and provisioning from a manual procurement process into software operations. Resource pooling allowed a provider to serve multiple consumers from a common capacity base, and measured service supplied the accounting layer needed to meter use. Together, these features separated access to computing capacity from ownership of the underlying machines [1][2].

The modern infrastructure-cloud market took recognizable form in 2006. Amazon announced Simple Storage Service on March 13 and Elastic Compute Cloud in beta on August 24. S3 offered web-accessible object storage, while EC2 offered resizable compute capacity that could be obtained and configured with comparatively little friction. Benjamin Black, a coauthor of the initial Amazon proposal that led to AWS, has explicitly rejected the often-repeated story that AWS began by selling unused retail-server capacity [6][28].

Other major providers broadened the model. Windows Azure became generally available on February 1, 2010. Google announced Compute Engine as a general-purpose virtual-machine service on June 28, 2012 and made it generally available on December 2, 2013. Those lifecycle distinctions matter: an announcement, a beta, and general availability are different events. Competition subsequently expanded cloud from basic compute and storage into managed databases, analytics, identity, messaging, machine learning, and application platforms [7][8].

The 2009 Berkeley report "Above the Clouds" explained the economic mechanism more carefully than the slogan "CapEx becomes OpEx." A cloud user can avoid a large initial hardware commitment, rent resources for short periods, release them when no longer needed, and transfer some overprovisioning and underprovisioning risk to the provider. The report also warned that a rented server-hour may cost more than an owned server-hour. Cloud economics therefore depend on elasticity, utilization, labor, resilience, migration, data transfer, and contract terms rather than on an automatic cost advantage [9].

Cloud also changed the operating interface. Capacity that once required purchasing, delivery, installation, and configuration could be requested through an API. This reduced provisioning delay and made repeatable automation practical at a larger scale. It did not make automation, microservices, continuous delivery, or infrastructure as code logically dependent on public cloud: all can run on premises. Cloud APIs and managed services instead lowered the friction of applying those practices and made temporary environments and rapid capacity changes easier to obtain [11][12].

By the mid-2020s, cloud had become a large and concentrated infrastructure sector rather than a single destination for every workload. Synergy Research Group estimated worldwide cloud-infrastructure-service revenue, covering IaaS, PaaS, and hosted private cloud, at $143.4 billion in the second quarter of 2026 and $500 billion over the trailing twelve months. It estimated Amazon, Microsoft, and Google shares of that broader market at 28%, 20%, and 15%, respectively; in the narrower public IaaS and PaaS market, the top three collectively represented 67%. These are provider-revenue estimates for a defined infrastructure-services market, not a measure of all products described as cloud [15].

## Core Service Models

### Defining characteristics and deployment models

NIST's definition is a useful boundary because it separates cloud properties from marketing language. On-demand self-service means a consumer can provision capabilities without a human interaction for each request. Broad network access means capabilities are available through standard network mechanisms; it does not require every service to traverse the public Internet. Resource pooling means provider resources serve multiple consumers with allocation changing according to demand. Rapid elasticity means capabilities can expand and contract quickly. Measured service means usage is monitored, controlled, and reported. Pay-per-use is typical, but a particular billing formula is not itself the definition [1].

NIST also distinguishes public, private, community, and hybrid deployment models. A public cloud is offered for open use and operates on the provider's premises. A private cloud is provisioned for one organization and may be on or off premises. A community cloud is provisioned for organizations with shared concerns. A hybrid cloud combines distinct infrastructures with technology that supports data or application portability. These models describe governance and deployment, while IaaS, PaaS, and SaaS describe which capabilities the consumer receives and which layers each party controls [1].

### Infrastructure as a Service

Infrastructure as a Service gives the consumer processing, storage, networks, and other fundamental resources on which arbitrary software can run. The consumer controls operating systems, storage, deployed applications, and sometimes selected network controls; the provider controls the underlying cloud infrastructure. Virtual machines are common, but bare-metal instances and other implementations can satisfy the model. The decisive boundary is control over the guest environment versus control over the underlying service [1][2].

IaaS resembles traditional infrastructure enough to support many existing operating systems and applications. It is useful when a team requires operating-system control, custom network topology, specialized software, or a migration path that does not immediately replace the application platform. That flexibility preserves customer duties: guest-system patching, application configuration, identity, data protection, backup design, and workload monitoring normally remain with the consumer unless a managed service or contract explicitly transfers them [2][23].

Consumption pricing changes the timing and visibility of cost. Compute may be charged by time and configuration, storage by capacity and operations, and networking by transfer direction and volume. Discounts can exchange flexibility for a term or spending commitment. An economic comparison must place like-for-like resilience, utilization, labor, licensing, financing, and exit costs on both sides. A steady workload on already-owned efficient equipment can favor ownership, while volatile or uncertain demand can make rapid release of rented capacity valuable even if its unit price is higher [9][17].

### Platform as a Service

Platform as a Service lets a consumer deploy applications created with languages, libraries, services, and tools supported by the provider. The consumer controls the deployed applications and may control application-hosting settings, while the provider controls the network, servers, operating systems, and storage beneath the platform. PaaS does not make all infrastructure concerns disappear: application architecture, data, identities, permissions, dependency choices, observability, and configuration remain consequential [1][2].

The value of PaaS is operational leverage. A managed runtime, database, queue, or deployment service can remove undifferentiated installation and maintenance work from an application team. The corresponding cost is a narrower control surface and deeper dependence on provider behavior. Portability is highest when the application depends on open protocols and replaceable components; it is lower when it relies on proprietary APIs, data models, event systems, identity integrations, or operational assumptions. The correct comparison is not simply "control versus convenience" but which operating responsibilities create value for the customer and which a specialized provider can perform more reliably [17][18].

PaaS is therefore a continuum rather than one uniform bundle. A managed relational database transfers hardware provisioning, much operating-system work, and portions of backup and patching to the provider, but the customer still owns schema design, access policy, query behavior, retention requirements, and recovery objectives. A managed application runtime transfers a different set of duties. Service documentation and contracts, not the PaaS label alone, determine the exact responsibility boundary [2][23].

### Software as a Service

Software as a Service gives consumers access to provider applications running on cloud infrastructure. The provider controls the application and underlying infrastructure, while the consumer may receive limited user-specific configuration. SaaS can eliminate local installation and product maintenance, but it does not eliminate customer responsibility. Customers still make choices about user accounts, authorization, data classification, retention, integrations, acceptable use, and the configuration options that the service exposes [1][2].

SaaS also changes procurement and governance. Subscription access can let business units adopt software rapidly, while centralized IT and security teams may have less advance visibility into stored data and third-party integrations. Effective governance requires an inventory of services, identity lifecycle controls, contractual review, data-export procedures, and exit planning. These controls address the organizational consequences of abstraction: the provider operates more of the stack, but the customer still owns the decision to use the service and remains accountable for its data and users [2][23].

### Serverless services

Serverless computing shifts provisioning and much runtime administration to the provider. Function as a Service is its general-purpose compute core: a developer supplies code that runs in response to events, while the platform allocates execution capacity. The broader serverless model also includes managed backend services, so serverless is not synonymous with FaaS. Servers still exist; the consumer's unit of operation changes from a long-lived host toward functions, events, and managed capabilities [10].

Serverless can fit intermittent, event-driven, or highly variable work because capacity can be allocated on demand and billing is tied to product-specific measures of use. It also introduces design constraints. Cold starts can add latency when a new execution environment is created, while state management, storage, communication, observability, execution duration, and provider-specific event interfaces can constrain an application. These limits vary by service and version, so no single execution-time rule or billing unit describes all serverless products [10].

### Responsibility is allocated, not removed

Across every service model, abstraction reallocates control. NIST's reference architecture states that security is shared and that controls should be assigned to the party best positioned to implement them. The allocation changes as a customer moves from IaaS to PaaS to SaaS, and it can differ between managed and unmanaged products within one provider. A concise rule such as "the provider secures the cloud and the customer secures data in the cloud" is useful only as a reminder; actual duties follow service design, configuration, and contract [2][23].

This allocation applies beyond security. Providers can assume hardware repair, facility operation, capacity management, and portions of software maintenance. Consumers still define availability needs, select regions and services, configure access, test recovery, monitor business outcomes, and decide how much provider failure they can tolerate. Cloud replaces some operational tasks with architecture, governance, and supplier-management tasks rather than removing operations altogether [2][18].

The service model and deployment model must therefore be evaluated together. A private-cloud IaaS environment can give one organization exclusive infrastructure while retaining an API-driven, pooled operating model; a public SaaS product can transfer nearly the entire technical stack to an external provider while leaving the customer responsible for access and information governance. Hybrid systems add interfaces between environments, and those interfaces become part of the reliability, security, and cost design. The useful question is not whether a system is simply "in the cloud," but which party controls each layer, how capacity is obtained, where state resides, what evidence is available for assurance, and how the workload can be recovered or moved. Those questions remain valid as product labels and implementation technologies change [1][2][17].

## Architectural Patterns and Operating Model

### Containers and orchestration

Containers package an application with many of its user-space dependencies while sharing the host operating-system kernel. They are generally lighter than full virtual machines, but portability is conditional: a container image still depends on compatible processor architecture, operating-system family, runtime, kernel facilities, and external services. NIST also notes that shared-kernel isolation differs from a virtual-machine hypervisor boundary and requires container-specific security controls [13][23].

The Open Container Initiative, launched in 2015 by Docker, CoreOS, and other industry participants, established vendor-neutral specifications for container images, runtimes, and distribution. Kubernetes, open sourced by Google in 2014, provides a portable platform for declarative management of containerized workloads and services. It can automate deployment, scaling, service discovery, rollouts, and recovery across public-cloud and on-premises environments. These tools complement cloud, but neither containers nor Kubernetes requires public cloud [11][13][27].

### Microservices

Microservices divide an application into independently deployable services organized around business capabilities. They can permit teams to release and scale components independently, but they exchange in-process simplicity for distributed-systems problems such as network failure, data consistency, interface versioning, tracing, and coordinated operations. Cloud APIs, managed services, containers, and orchestration can reduce provisioning and operational friction, but cloud did not invent microservices and is not a prerequisite for them [11][14].

Architecture should follow system and organizational needs rather than a cloud fashion. A modular monolith can be easier to test and operate when independent scaling or release boundaries are unnecessary. Microservices become more defensible when domains are separable, deployment independence has value, and the organization can support service ownership and distributed observability. The author's assessment is that cloud increases the feasible range of architectures; it does not make the most distributed architecture the best one [11][14].

### Infrastructure as code and delivery automation

Infrastructure as code represents infrastructure through versioned descriptive models and automated deployment. This can make environments reproducible, reviewable, and testable while reducing manual configuration drift. Cloud APIs are well suited to IaC because resources expose programmable lifecycle operations, but the practice also applies to virtualized and physical infrastructure outside public cloud [12].

Continuous integration and delivery likewise predate and extend beyond public cloud. Elastic test environments, API-driven infrastructure, and managed deployment platforms can shorten provisioning, but build quality, automated tests, release design, and organizational coordination remain necessary. Cloud removes some physical bottlenecks; it does not guarantee that a team can release safely or quickly [12].

### Reliability, observability, and failure domains

Cloud resources are not inherently continuously available. Regions, availability zones, services, control planes, networks, credentials, and customer configurations create distinct failure modes. A resilient design identifies business recovery objectives, maps them to failure domains, tests restoration, and avoids treating a provider service-level agreement as a complete continuity plan. Multi-region or multi-provider designs can reduce selected dependencies, but they also add synchronization, testing, operational, and cost complexity [2][23].

Measured service generates detailed operational and billing data. That visibility supports observability and cost allocation only when teams preserve useful labels, ownership metadata, logs, traces, budgets, and alerts. Without those controls, elastic provisioning can create resources faster than an organization can understand or govern them. The operating model must connect technical consumption to accountable owners and business outcomes [2][16].

## Evidence

### Early economic model

The Berkeley 2009 report used engineering-economic examples rather than a population-wide cost survey. It identified three buyer-side mechanisms: elimination of a large initial resource commitment, short-term use with release on demand, and elastic scaling that reduces the penalties of overprovisioning or underprovisioning. It explicitly observed that pay-as-you-go capacity could cost more than purchasing and depreciating comparable servers. The evidence supports lower commitment and transferred demand risk, not a universal percentage saving or a claim that every migration has positive return [9].

That distinction invalidates broad claims that cloud migration normally cuts IT cost by 20-30%, that 89% of migrations produce positive return, or that cloud is automatically two or three times more expensive than on-premises systems. None of those cross-organization figures is supported by a defined, authoritative comparison in the sources reviewed. Total cost depends on the workload, utilization, staffing, service level, migration effort, licensing, discounts, data movement, and accounting boundary [9][16][17].

### Industry entry and concentration

Lu, Phillips, and Yang studied Chinese firm registrations and cancellations from 2007 through 2018 across 89 two-digit industries. Their difference-in-differences design used industries' pre-shock exposure to cloud-related computing services and a 2013 cost shock. They reported that a one-standard-deviation increase in cloud influence was associated with a 13-25% increase in expected firm entry and a reduction in industry concentration, depending on specification and concentration measure. The study is an NBER working paper, uses a specific Chinese policy and industry context, and identifies exposure through business-scope keywords; it does not prove that cloud reduces concentration in every economy or sector [19].

The result nevertheless supplies evidence for a mechanism often asserted without support. Lower fixed computing commitments can matter more to potential entrants and small firms than to incumbents that already possess infrastructure and operating capabilities. The defensible conclusion is contextual: cloud can reduce one barrier to entry, while access to data, distribution, capital, regulation, and complementary skills can remain important or become more important [9][19].

### Learning after adoption

Brand and coauthors examined high-frequency CPU-utilization records from more than one billion virtual machines used by nearly 100,000 customer firms at an anonymous global provider. Their revised NBER working paper reports that adopters improved measured compute productivity by about 33% in the first year and reached a plateau after roughly four years. The data are intermittent from 2017 through 2023, omit 2020-2021, and observe one provider without knowing all prior experience elsewhere [20].

The outcome is compute productivity, not total factor productivity, profit, revenue, or customer value. The study cannot establish that every workload should move to cloud. It instead shows that efficient use is learned over time and that adoption alone does not exhaust the available productivity gain. Governance, architecture, rightsizing, and operating routines are complementary capabilities [20].

### Current market structure

Synergy's Q2 2026 estimate put quarterly cloud-infrastructure-service revenue at $143.4 billion and trailing-twelve-month revenue at $500 billion. The covered market includes IaaS, PaaS, and hosted private cloud, not all SaaS or every cloud-labelled product. Amazon, Microsoft, and Google held estimated shares of 28%, 20%, and 15% in this broader market, while the three together accounted for 67% of public IaaS and PaaS. The narrower and broader denominators must not be mixed [15].

The UK Competition and Markets Authority reached a related but geographically narrower conclusion after a statutory investigation of UK cloud infrastructure services. Its 2025 final decision found technical and commercial switching barriers. This does not prove that every customer is locked in, but it shows that switching difficulty is a market characteristic, not merely an anecdote [18].

The CMA evidence is materially different from a vendor poll. It was produced through a statutory market investigation that combined submissions, provider and customer evidence, documents, and quantitative analysis before a final decision. Its scope is also narrower than the global market: UK infrastructure services, especially IaaS and PaaS. The finding therefore strengthens the case that provider-specific interfaces, commercial terms, and software licensing can impede switching in that market, while leaving open how strongly the same mechanisms operate for a particular SaaS product, jurisdiction, or customer architecture [18].

### Adoption, cost management, and repatriation

Flexera's 2025 State of the Cloud report surveyed 759 cloud decision-makers and users through an independent vetted panel in winter 2024. Respondents estimated that 27% of public-cloud spending was wasted, and managing cloud spending remained a leading challenge. These are self-reported estimates from a vendor-sponsored industry survey, not audited waste measurements or a census of all organizations. They support the need for cost ownership and optimization, not a universal cloud-versus-on-premises multiplier [16].

The same report found that 21% of cloud workloads had been repatriated in its respondent organizations, while incoming migrations and new cloud workloads exceeded exits. This is evidence of selective workload rebalancing within continued cloud growth, not a wholesale reversal of cloud adoption. A workload may move because of cost, performance, governance, technical fit, contract terms, or organizational capability; the destination can be private cloud, hosted infrastructure, on-premises systems, or another arrangement [16].

OpenText and Foundry's 2025 study illustrates why denominators matter. It surveyed 201 qualified IT or security managers at organizations with at least $500 million in revenue, and every organization had already repatriated or planned to repatriate public-cloud workloads. Among those planning repatriation, the average share targeted was 36% in the United States, 35% in Europe, and 47% in Asia-Pacific. Those figures describe a deliberately selected repatriation-oriented sample and cannot estimate how prevalent repatriation is among organizations generally. Reported security and cost outcomes are respondents' perceptions, not controlled before-and-after measurements [24].

## Implications

### For new products and growing firms

Cloud can lower the minimum initial commitment required to test a software service. A team can obtain small resource allocations, increase them if demand appears, and release them if an experiment fails. This changes financing and timing: hardware need not be purchased for forecast peak demand before the product has users. The supported claim is reduced commitment and provisioning friction, not that every startup previously needed millions of dollars or that a credit card alone creates a globally scalable business [9].

The implication for founders is to preserve option value. Early architectures should make the next experiment inexpensive without assuming that the first provider and service will remain optimal forever. Managed services can accelerate learning, but each proprietary interface creates a future migration decision. The author's assessment is that early speed can rationally outweigh portability when uncertainty is high, provided the team records dependencies, exports critical data, and understands what an exit would require [17][18].

### For established organizations

For an established organization, cloud is a portfolio decision rather than a binary migration destination. Variable demand, temporary environments, rapid regional deployment, and access to specialized managed capabilities can favor cloud. Predictable high utilization, unusual hardware, strict latency constraints, sunk efficient capacity, or particular legal and operational requirements can favor owned or dedicated infrastructure. Hybrid design is useful when it reflects measured workload requirements; it is wasteful when it merely duplicates platforms without a clear responsibility and recovery model [9][16].

Migration strategy should distinguish rehosting, replatforming, and redesign. Rehosting may reduce datacenter obligations or meet a deadline while preserving application architecture. It should not be promised to capture every elasticity or managed-service benefit. Redesign can extract more provider capability but raises delivery risk and switching cost. A rational sequence defines the business outcome, measures the current baseline, chooses the smallest sufficient change, and verifies the result after migration [9][17].

### For engineering and operations

Engineering teams gain programmable infrastructure, but they also inherit distributed failure, configuration, and cost surfaces. Service selection should include recovery objectives, data flows, identity boundaries, observability, quotas, and exit paths. Infrastructure as code and automated policy can reduce drift, yet automation can also reproduce an error rapidly. Review, staged deployment, least privilege, and tested rollback remain necessary [12][23].

Serverless, containers, Kubernetes, and microservices should be selected for concrete operating properties. Serverless can match bursty event work; containers can standardize packaging; Kubernetes can coordinate containerized services; microservices can create independent release boundaries. Each introduces a new control plane and skill requirement. The author's assessment is that the simplest architecture meeting scale, reliability, and organizational needs usually preserves the most room for later change [10][11][13][14].

### For finance and management

Cloud makes cost more variable and granular, but not automatically more controlled. Resource tags, budget ownership, unit metrics, forecasts, anomaly detection, commitment management, and deletion of unused resources turn provider billing data into management information. FinOps is best understood as a cross-functional operating discipline connecting engineering choices to financial accountability, rather than as a one-time cost-cutting project [16].

A sound comparison avoids false precision. It includes equivalent availability and recovery, staff time, licenses, support, facilities, networking, security controls, migration, and exit. It also values speed and flexibility when they affect revenue or risk. A cheaper unit of compute can still be a poor decision if it delays a critical product; an expensive managed service can still be rational if it replaces scarce operational work. Conversely, convenience does not justify unmeasured consumption or an architecture whose switching cost exceeds its benefit [9][17].

### For competition and portability

Provider concentration creates both economies of scale and dependency. Large providers can invest in global facilities, specialized hardware, security, and broad service portfolios. Customers can also face technical differences, retraining, data movement, proprietary services, licensing terms, credits, and committed-spend agreements when switching or combining providers. The magnitude depends on the architecture and contract; migration is not universally impossible, but it can be expensive and difficult [17][18].

Portability should be designed selectively. Open data formats, standard protocols, container specifications, automated builds, and tested export procedures can reduce switching friction. Duplicating every workload across providers can cost more and create a lowest-common-denominator architecture. The author's assessment is to protect portability where dependency would be consequential, while accepting deliberate provider specialization where the benefit is larger and the exit cost is understood [11][13][17].

European law now changes part of this calculation. Chapter VI of the EU Data Act has applied since September 12, 2025 and requires providers of data-processing services to remove specified obstacles to switching and multi-provider use. Reduced switching charges during the transition may not exceed directly incurred switching costs; from January 12, 2027, providers may not impose switching charges, including switching-related data-egress charges. The rule does not abolish every transfer charge: cost-based egress charges can remain for ongoing in-parallel use in circumstances covered by the Act [21].

### For security and sovereignty

Cloud security is a division of control, not a transfer of accountability. Providers can patch and monitor shared infrastructure at scale, while customers retain duties tied to identities, data, application code, service configuration, and resources they manage. The NSA identifies misconfiguration as the most prevalent cloud vulnerability, but the sources reviewed do not support attributing 70% of cloud incidents or breaches to misconfiguration. Security claims should remain qualitative unless a study defines incidents, sample, and denominator [2][23].

Data location alone does not settle legal control. The US CLOUD Act clarified that providers subject to US jurisdiction can be compelled through valid US legal process to disclose data in their possession, custody, or control regardless of storage location; it did not remove jurisdictional or procedural requirements. For EU personal data, the EDPB states that a response to a third-country authority request is a transfer that must independently satisfy an Article 6 legal basis and GDPR Chapter V. A foreign request is not itself sufficient authority under the GDPR [22][25].

The practical implication is a layered sovereignty assessment. Organizations should examine provider jurisdiction and ownership, contractual commitments, administrator access, encryption and key control, software supply chains, support paths, recovery capability, and applicable law. Local infrastructure can reduce selected dependencies but does not by itself eliminate remote administration, vendor control, or legal-process risk. Under oath before the French Senate on June 10, 2025, Microsoft France legal and public-affairs director Anton Carniaux said he could not guarantee that French citizens' data entrusted through UGAP would never be transmitted following a US-government injunction without explicit French-authority consent; the statement concerned that specific procurement context, not every category of EU data [26].

## Common Pitfalls and Emerging Concerns

A first pitfall is treating cloud as a location rather than an operating model. Moving an unchanged application to virtual machines can be a valid rehosting choice, but it does not automatically add elasticity, resilience, or lower cost. If the application still requires fixed capacity, manual change, and tightly coupled recovery, the organization may reproduce its old constraints on a different balance sheet. Expectations should match the migration method [9][17].

A second pitfall is confusing ease of provisioning with efficiency. Self-service can produce abandoned storage, idle compute, oversized instances, duplicated data, and unexpected network charges. Flexera's respondent-estimated waste shows that this is a material management problem, but it does not prove that public cloud is always more expensive. Continuous ownership, allocation, and optimization are required because consumption and prices change [16].

A third pitfall is interpreting abstraction as absence of responsibility. PaaS and SaaS remove many provider-operated layers from customer view, yet identities, data, permissions, integrations, and business continuity remain customer concerns. Teams should map responsibility for each control and test it rather than infer it from the service-model label [1][2][23].

A fourth pitfall is assuming portability from packaging alone. A container can standardize an application artifact while the system still depends on a provider database, identity service, event schema, network design, and operational toolchain. Kubernetes can run in many environments, but a portable control plane does not make state, data gravity, skills, and contracts portable. Exit tests should exercise data restoration and service replacement, not merely rebuild a container image [11][13][17][18].

A fifth pitfall is using survey percentages without their population. Cloud adoption, multi-cloud, hybrid use, waste, and repatriation figures vary with definitions and samples. OpenText's regional repatriation percentages apply only to large organizations prequalified for past or planned repatriation. Synergy's market shares apply to cloud infrastructure services, not all SaaS. Every percentage should carry its year, denominator, geography, and measurement method [15][16][24].

The final concern is concentration. Concentration can create operational, negotiating, and systemic dependencies even when a provider performs well. Multi-cloud is not an automatic remedy: duplicated platforms can dilute expertise and increase failure paths. The defensible response is explicit dependency management -- identify critical services, quantify exit effort, preserve data access, test recovery, negotiate contracts, and diversify only where the reduction in risk exceeds the added complexity [18][21].

## Sources

1. Mell, P. and Grance, T. "The NIST Definition of Cloud Computing."
   NIST Special Publication 800-145, September 2011.
   https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf [high]

2. NIST. "NIST Cloud Computing Reference Architecture."
   Special Publication 500-292, September 2011.
   https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication500-292.pdf [high]

3. Stoica, I. and Shenker, S. "From Cloud Computing to Sky Computing."
   ACM HotOS '21, June 2021.
   https://dl.acm.org/doi/pdf/10.1145/3458336.3465301 [high]

4. IBM. "z/VM History: Timeline."
   https://www.ibm.com/support/pages/zvm/history/timeline.html [high]

5. Bugnion, E., Devine, S., Rosenblum, M., Sugerman, J., and Wang, E.
   "Bringing Virtualization to the x86 Architecture with the Original
   VMware Workstation." ACM Transactions on Computer Systems, 2012.
   https://dl.acm.org/doi/10.1145/2382553.2382554 [high]

6. Amazon Web Services. "Announcing Amazon S3" and "Announcing Amazon
   Elastic Compute Cloud (Amazon EC2) - beta," March and August 2006.
   https://aws.amazon.com/about-aws/whats-new/2006/03/13/announcing-amazon-s3---simple-storage-service/
   https://aws.amazon.com/about-aws/whats-new/2006/08/24/announcing-amazon-elastic-compute-cloud-amazon-ec2---beta/ [high]

7. Microsoft. "Windows Azure General Availability," February 1, 2010.
   https://blogs.microsoft.com/blog/2010/02/01/windows-azure-general-availability/ [high]

8. Google. "Google Compute Engine launches" and "Google Compute Engine
   is now Generally Available," June 28, 2012 and December 2, 2013.
   https://cloudplatform.googleblog.com/2012/06/google-compute-engine-launches.html
   https://developers.googleblog.com/google-compute-engine-is-now-generally-available-with-expanded-os-support-transparent-maintenance-and-lower-prices/ [high]

9. Armbrust, M. et al. "Above the Clouds: A Berkeley View of Cloud
   Computing." UC Berkeley Technical Report EECS-2009-28, 2009.
   https://www2.eecs.berkeley.edu/Pubs/TechRpts/2009/EECS-2009-28.pdf [high]

10. Jonas, E. et al. "Cloud Programming Simplified: A Berkeley View on
    Serverless Computing." UC Berkeley Technical Report EECS-2019-3, 2019.
    https://www2.eecs.berkeley.edu/Pubs/TechRpts/2019/Archive/EECS-2019-3.pdf [high]

11. Kubernetes. "Overview."
    https://kubernetes.io/docs/concepts/overview/ [high]

12. Microsoft Learn. "What is infrastructure as code?"
    https://learn.microsoft.com/en-us/devops/deliver/what-is-infrastructure-as-code [high]

13. NIST. "Application Container Security Guide."
    Special Publication 800-190, September 2017.
    https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-190.pdf [high]

14. Lewis, J. and Fowler, M. "Microservices," March 25, 2014.
    https://martinfowler.com/articles/microservices.html [medium]

15. Synergy Research Group. "Q2 Cloud Market Passes $143 Billion;
    Highest Growth Rate in Eight Years," July 30, 2026.
    https://www.srgresearch.com/articles/q2-cloud-market-passes-143-billion-highest-growth-rate-in-eight-years [medium]

16. Flexera. "2025 State of the Cloud Report," March 2025; survey
    fielded in winter 2024.
    https://resources.flexera.com/web/pdf/Flexera-State-of-the-Cloud-Report-2025.pdf [medium]

17. Biglaiser, G., Cremer, J., and Mantovani, A. "The Economics of the
    Cloud." Toulouse School of Economics Working Paper 24-1520, March
    29, 2024. The report discloses support from a Microsoft research grant.
    https://www.tse-fr.eu/sites/default/files/TSE/documents/doc/wp/2024/wp_tse_1520.pdf [high]

18. UK Competition and Markets Authority. "Cloud Services Market
    Investigation: Summary of Final Decision," July 31, 2025.
    https://assets.publishing.service.gov.uk/media/688b20e6ff8c05468cb7b120/summary_of_final_decision.pdf [high]

19. Lu, Y., Phillips, G., and Yang, M. "The Impact of Cloud Computing
    and AI on Industry Dynamics and Concentration." NBER Working Paper
    32811, August 2024.
    https://www.nber.org/system/files/working_papers/w32811/w32811.pdf [high]

20. Brand, J. et al. "Firm Productivity and Learning with Digital
    Technologies: Evidence from Cloud Computing." NBER Working Paper
    32938, September 2024, revised December 2025.
    https://www.nber.org/system/files/working_papers/w32938/w32938.pdf [high]

21. European Union. "Regulation (EU) 2023/2854 (Data Act)," December
    13, 2023; applicable from September 12, 2025.
    https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng [high]

22. US Department of Justice. "The Purpose and Impact of the CLOUD Act,"
    April 2019.
    https://www.justice.gov/criminal/media/999601/dl?inline [high]

23. US National Security Agency. "Mitigating Cloud Vulnerabilities,"
    January 22, 2020.
    https://media.defense.gov/2020/Jan/22/2002237484/-1/-1/0/CSI-MITIGATING-CLOUD-VULNERABILITIES_20200121.PDF [high]

24. OpenText and Foundry. "The Cloud Repatriation Shift: What the Data
    Tells Us," 2025; fieldwork March 2025.
    https://www.opentext.com/en/media/guide/the-cloud-repatriation-shift-what-the-data-tells-us-guide-en.pdf [medium]

25. European Data Protection Board. "Guidelines 02/2024 on Article 48
    GDPR," final Version 2.1, June 5, 2025.
    https://www.edpb.europa.eu/system/files/documents/2025-06/edpb_guidelines_202402_article48_v2_en.pdf [high]

26. French Senate. "CE Commande publique: compte rendu de la semaine du
    9 juin 2025 -- Audition de Microsoft," June 10, 2025.
    https://www.senat.fr/compte-rendu-commissions/20250609/ce_commande_publique.html [high]

27. Open Container Initiative. "About the Open Container Initiative."
    https://opencontainers.org/about/overview/ [high]

28. Network World. "The myth about how Amazon's Web service started
    just won't die," March 2, 2015.
    https://www.networkworld.com/article/936248/the-myth-about-how-amazon-s-web-service-started-just-won-t-die.html [medium]

## See Also

- `library/technology/large-language-models.md` -- large-language-model
  training and inference are major consumers of cloud compute and specialized
  accelerators.
- `library/technology/cybersecurity-principles-threats-and-defense-in-depth.md` --
  cloud responsibility boundaries and configuration risks are applications of
  defense-in-depth.
- `library/coding-agentic-ai/anchor-coding-agentic-ai.md` -- agentic systems
  commonly depend on cloud-hosted models, tools, storage, and execution.
