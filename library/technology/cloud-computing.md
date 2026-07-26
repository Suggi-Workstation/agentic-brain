---
name: cloud-computing
id: 20260726T133103Z
tier: library-topic
domain: technology
author: Researcher-1
tags: [cloud-computing, iaas, paas, saas, serverless, microservices, infrastructure]
links: [library/technology/large-language-models.md, library/technology/cybersecurity-principles-threats-and-defense-in-depth.md]
---

# Cloud Computing -- How Renting Compute Transformed the Software Industry and Lowered the Barrier to Global Scale

Cloud computing is the delivery of computing resources -- servers,
storage, databases, networking, and software -- over the internet on
a pay-as-you-go basis, replacing the capital-intensive model of owning
and operating physical data centers. By turning computing into a
utility, cloud computing reduced the upfront cost of launching a
software company from millions of dollars to a credit card and an
idea, fundamentally restructuring the economics of the entire software
industry. The shift from owning servers to renting compute did not
merely change how companies buy IT -- it enabled new architectural
patterns, compressed time-to-market, and created the conditions for
the platform economy, while also introducing new risks around vendor
dependency and data control.

## Background

The intellectual foundation of cloud computing traces back to the
1960s, when computer scientist John McCarthy proposed that computing
could one day be organized as a public utility, much like electricity
or water. This vision remained largely theoretical for decades because
the hardware, networking, and virtualization technologies did not
exist to make it practical.

The first major step toward making computing a utility came with the
development of virtualization technology in the late 1990s and early
2000s. VMware, founded in 1998, commercialized x86 virtualization,
allowing multiple virtual machines to run on a single physical server.
This was the critical enabling technology: without virtualization,
cloud providers could not pool physical hardware into elastically
allocatable resources.

Amazon Web Services (AWS) launched in 2006 with two foundational
services: Elastic Compute Cloud (EC2) for virtual servers and Simple
Storage Service (S3) for object storage. Amazon's motivation was
internal: the company had built massive computing infrastructure to
run its e-commerce operations and realized it could sell excess
capacity. This internal-to-external pattern -- building for your own
needs and then productizing the infrastructure -- became the template
for cloud innovation.

Microsoft Azure followed in 2010, and Google Cloud Platform (GCP)
launched its compute services in 2012. By the mid-2010s, the "Big
Three" hyperscalers were locked in a fierce competition that drove
prices down and capabilities up, creating a flywheel of adoption.
Organizations that once spent months procuring servers could now
provision equivalent capacity in minutes.

The COVID-19 pandemic accelerated cloud adoption dramatically.
Companies with cloud-native infrastructure scaled remote work and
digital services rapidly; those still running on-premises struggled.
By 2025, approximately 94% of organizations used cloud infrastructure
in some form, and 85% had completed or were completing a cloud-first
transition. The cloud had become the default assumption for new
software, not an alternative to consider.

## Core Service Models

Cloud computing is not a single technology but a stack of service
models, each abstracting away a different layer of the computing
stack. Understanding these models is essential because they define
the division of responsibility between provider and customer, the
pricing model, and the degree of operational control.

### Infrastructure as a Service (IaaS)

IaaS provides virtualized computing resources over the internet:
virtual machines, storage, and networking. The provider manages the
physical hardware, data center, and virtualization layer; the
customer manages the operating system, middleware, runtime,
applications, and data. This is the most flexible model -- essentially
renting a data center in software -- and the one that most closely
resembles traditional on-premises infrastructure.

Key IaaS offerings include AWS EC2, Azure Virtual Machines, and Google
Compute Engine. IaaS pricing is typically consumption-based: you pay
for the compute seconds, storage gigabytes, and network transfer you
consume. This shifts IT spending from capital expenditure (CapEx) to
operating expenditure (OpEx), which is the foundational economic
transformation of cloud computing.

IaaS is best suited for workloads requiring maximum control: legacy
application migrations where rewriting for a platform is impractical,
highly customized environments with specific kernel or security
requirements, and workloads with predictable, steady-state utilization
where the cloud's elasticity premium is less valuable.

### Platform as a Service (PaaS)

PaaS builds on IaaS by providing a managed platform for developing,
deploying, and running applications. The provider manages everything
below the application layer -- operating system, runtime, middleware,
scaling, and patching -- and the customer focuses on application code
and data. PaaS abstracts away infrastructure management entirely.

Major PaaS offerings include Google App Engine, AWS Elastic Beanstalk,
Azure App Service, and Heroku. The trade-off is reduced control in
exchange for dramatically faster development velocity. A developer
can go from code to production in minutes without configuring a single
server.

PaaS is ideal for application development teams that want to focus on
business logic rather than infrastructure operations. It accelerates
development cycles, simplifies collaboration for distributed teams,
and reduces the operational burden of patching, scaling, and
monitoring. The author's assessment is that PaaS represents the
direction the industry is heading: managed services that make
infrastructure invisible to developers.

### Software as a Service (SaaS)

SaaS delivers fully managed software applications over the internet.
The provider manages everything -- infrastructure, platform, and
application -- and the customer simply uses the software, typically
via a web browser. SaaS is the end-user-facing layer of the cloud
stack.

Examples include Google Workspace, Microsoft 365, Salesforce, Zoom,
and Slack. SaaS pricing is typically per-user, per-month subscription
based. For the end user, SaaS eliminates installation, maintenance,
and upgrade concerns entirely.

SaaS is the most abstracted model and the one that reaches furthest
beyond IT departments to touch every business function. Its dominance
has reshaped enterprise software procurement: line-of-business leaders
can now purchase and deploy software without IT involvement, a shift
that has both empowered business units and created governance
challenges around shadow IT.

### Serverless and Functions as a Service (FaaS)

Serverless computing, typically delivered as Functions as a Service
(FaaS), is a specialization of PaaS where developers deploy individual
functions that execute in response to events. Despite the name,
servers still exist -- but the developer never sees them. The provider
handles all infrastructure provisioning, scaling, and capacity
planning. Pricing is per-invocation and per-millisecond of execution
time, making it potentially very cost-effective for intermittent or
spiky workloads.

AWS Lambda, Google Cloud Functions, and Azure Functions are the
dominant FaaS offerings. Serverless is widely adopted for event-driven
workloads such as API backends, data processing pipelines, scheduled
jobs, and IoT applications. Its main limitation is cold-start latency
-- the delay when a function is invoked after being idle -- which
makes it less suitable for latency-sensitive or long-running processes.

## Architectural Patterns Enabled by the Cloud

The shift to cloud computing did not just change where software runs;
it changed how software is designed, built, and operated. Several
architectural patterns emerged that would be impractical or impossible
with on-premises infrastructure.

### Microservices

Cloud computing made microservices architecture economically viable.
In a monolithic architecture, the entire application runs as a single
process; scaling requires replicating the whole monolith. Microservices
decompose the application into independently deployable services, each
responsible for a single business capability. Each service can be
scaled independently based on its specific load, and teams can deploy
updates to their services without coordinating with other teams.

The cloud provides the infrastructure that makes this practical:
container orchestration platforms like Kubernetes automate deployment,
scaling, and management of containerized microservices across clusters
of virtual machines. Without cloud infrastructure, managing dozens or
hundreds of independent services at scale would be operationally
overwhelming.

### Containers and Orchestration

Containers package an application and its dependencies into a portable
unit that runs consistently across any environment. Docker,
popularized after 2013, became the standard container format.
Containers are lighter-weight than virtual machines because they share
the host operating system kernel, making them faster to start and more
resource-efficient.

Kubernetes, originally designed by Google and released as open source
in 2014, became the dominant container orchestration platform.
It automates deployment, scaling, load balancing, self-healing, and
service discovery for containerized applications. By 2025,
approximately 66% of organizations ran their containerized
applications on private or hybrid cloud infrastructure, reflecting
the central role containers and orchestration play in modern cloud
architecture.

### DevOps and Infrastructure as Code

Cloud computing enabled the DevOps movement -- the integration of
software development (Dev) and IT operations (Ops) into a single,
continuous workflow. Because infrastructure could be provisioned
programmatically through APIs, teams could treat infrastructure
configuration as code, stored in version control, tested, and deployed
through the same pipelines as application code.

Tools like Terraform and AWS CloudFormation made infrastructure as
code (IaC) standard practice. Continuous integration and continuous
delivery (CI/CD) pipelines automated the build, test, and deploy
cycle, reducing the time from code commit to production deployment
from weeks to hours or minutes. The cloud made this possible by
eliminating the physical provisioning bottleneck that had always
separated development from deployment.

## Evidence

The economic impact of cloud computing is measurable at multiple
scales. The global cloud computing market was estimated at
approximately $500 billion in 2023, with projections reaching $1
trillion by 2028 and $2 trillion by 2030, representing a compound
annual growth rate exceeding 20% (Goldman Sachs; Precedence Research).
Global public cloud infrastructure spending grew from $525 billion in
2023 to $592 billion in 2024, with $679 billion projected for 2025.

At the organizational level, cloud migration drives an average 20-30%
reduction in IT costs compared to traditional on-premises
infrastructure. Approximately 89% of cloud migration projects report
positive ROI. The author's synthesis of multiple surveys is that the
savings come from three sources: eliminated hardware procurement and
maintenance, reduced staffing requirements for infrastructure
operations, and the ability to scale resources precisely to demand
rather than provisioning for peak load.

The CEPR (Centre for Economic Policy Research) has analyzed cloud
computing as a general-purpose technology that reduces barriers to
entry across the economy. By converting fixed capital expenditure
into variable operating costs, cloud computing enables small and
medium-sized enterprises to access computing resources that previously
required the capital reserves of large corporations. The entry of new
firms, reduction of markups, and expansion of total production are
all predicted consequences in sectors with the largest IT cost savings.

Cloud repatriation -- the movement of workloads from public cloud back
to on-premises or private infrastructure -- has emerged as a
significant counter-trend. An OpenText survey found that organizations
target an average of 36% of workloads for repatriation in the US, 35%
in Europe, and 47% in Asia-Pacific. The top drivers are data security
and privacy concerns (51%), cost control (39%), and the need for more
customization (35%). Among organizations that have repatriated, 92%
report improved security posture, 61% report better security and
compliance, and 52% report improved data governance.

Adoption statistics paint a picture of near-universal cloud usage with
growing sophistication. As of 2025, approximately 94% of organizations
use cloud infrastructure in some form. Multi-cloud adoption has grown
from 76% in 2024 to 89%, with 94% of large enterprises using multiple
cloud providers. Hybrid cloud adoption reached 80% in 2025, and 87%
of enterprises were expected to operate in hybrid environments by the
end of the year. These numbers suggest that the future is not purely
cloud or purely on-premises, but hybrid -- where organizations
strategically place workloads based on cost, compliance, performance,
and sovereignty requirements.

## Implications

The most profound implication of cloud computing is the reduction of
barriers to entry in the software industry. Before the cloud, launching
a software company required significant upfront capital for servers,
networking equipment, data center space, and the personnel to manage
them. A startup needed to raise venture capital before it could deploy
its first line of code. After the cloud, a founder with a credit card
can provision a world-class infrastructure in minutes and scale it to
serve millions of users.

This lowering of the capital barrier transformed the geography and
demographics of entrepreneurship. Software startups could emerge from
anywhere with an internet connection, not just from venture capital
hubs with access to expensive infrastructure. The global distribution
of software innovation widened, and the cycle time from idea to
product compressed from years to months.

For established enterprises, the cloud enabled a different kind of
transformation: the ability to experiment at low cost. Before the
cloud, experimenting with a new application meant procuring and
provisioning hardware -- a process that could take months and cost
hundreds of thousands of dollars before a single user tested the
product. In the cloud, an experiment can be launched in hours and
shut down if it fails, with costs proportional to actual usage. This
shift toward low-cost experimentation increased the rate of innovation
across industries.

However, the concentration of cloud infrastructure in a small number
of hyperscalers -- AWS, Azure, and GCP collectively dominate the
public cloud market -- has created new risks. Vendor lock-in occurs
when an organization becomes so dependent on a specific provider's
proprietary services, APIs, or data formats that migration becomes
prohibitively expensive or technically infeasible. Managed services
that accelerate development -- proprietary databases, AI/ML platforms,
analytics tools -- simultaneously deepen dependency. Once integrated
into a provider's ecosystem, the organization faces high switching
costs that reduce its negotiating leverage.

Data sovereignty has emerged as a critical concern. Regulations like
the EU's GDPR and the US CLOUD Act create conflicting requirements
about where data may be stored and who may access it. In June 2025,
Microsoft testified before the French Senate that it could not
guarantee EU data would be beyond the reach of the US CLOUD Act --
sworn testimony from a hyperscaler acknowledging the limits of
contractual data sovereignty. The structural answer to sovereignty
is not a better contract with a cloud provider but owning the
infrastructure in the relevant jurisdiction.

The cloud repatriation trend reflects a maturing understanding of
cloud economics. Organizations that migrated to the cloud for cost
savings are discovering that the public cloud is not always cheaper,
particularly for predictable, steady-state workloads. The FinOps
discipline -- cloud financial management -- has emerged to help
organizations track, optimize, and govern cloud spending. The emerging
consensus is that optimal infrastructure strategy combines public
cloud for elastic, experimental, and variable workloads with private
or on-premises infrastructure for predictable, data-heavy, and
sovereignty-sensitive workloads.

## Common Pitfalls and Emerging Concerns

Lift-and-shift migrations without re-architecture are a persistent
pitfall. Moving a monolithic application designed for dedicated
servers to cloud virtual machines without redesigning for cloud-native
patterns (auto-scaling, statelessness, managed services) often results
in higher costs and no operational improvement. The cloud is not just
a hosting location; it is a different operational model, and treating
it as a remote data center misses the point.

Uncontrolled cloud costs are the most common post-migration surprise.
The pay-as-you-go model that makes cloud adoption easy also makes it
easy to accumulate charges from forgotten resources, over-provisioned
instances, and unexpected data egress fees. Without FinOps discipline,
cloud bills can exceed on-premises costs by 2-3x. The author's
assessment is that cloud cost management is an organizational
capability that must be built intentionally, not an automatic benefit
of cloud adoption.

Security misconfiguration remains the leading cause of cloud data
breaches. In the shared responsibility model, the provider secures
the infrastructure but the customer secures what they put in it.
Misconfigured storage buckets, overly permissive identity and access
management (IAM) policies, and exposed APIs account for approximately
70% of cloud security incidents. The shift to the cloud does not
eliminate security responsibility; it redistributes it.

## Sources

1. AWS. "Types of Cloud Computing -- SaaS vs PaaS vs IaaS."
   https://aws.amazon.com/types-of-cloud-computing/ [high]

2. Microsoft Azure. "What are IaaS, PaaS, and SaaS?"
   https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-are-iaas-paas-and-saas [high]

3. Google Cloud. "PaaS vs IaaS vs SaaS vs CaaS: How are they different?"
   https://cloud.google.com/learn/paas-vs-iaas-vs-saas [high]

4. Etro, F. "The Economics of Cloud Computing." CEPR/VoxEU, 2011.
   https://cepr.org/voxeu/columns/economics-cloud-computing [high]

5. Bourreau, M. et al. "The Economics of the Cloud." Toulouse School
   of Economics Working Paper, 2024.
   https://www.tse-fr.eu/sites/default/files/TSE/documents/doc/wp/2024/wp_tse_1520.pdf [high]

6. DuploCloud. "Cloud Migration Statistics: Key Trends, Challenges, and
   Opportunities in 2025."
   https://duplocloud.com/blog/cloud-migration-statistics/ [medium]

7. OpenText. "The Cloud Repatriation Shift: What the Data Tells Us."
   https://www.opentext.com/en/media/guide/the-cloud-repatriation-shift-what-the-data-tells-us-guide-en.pdf [medium]

8. InfoWorld. "Cloud repatriation is back on the agenda." June 2026.
   https://www.infoworld.com/article/4190757/cloud-repatriation-is-back-on-the-agenda.html [medium]

9. Shopify. "Cloud Reset: A Guide to Cloud Repatriation Strategy in
   2026."
   https://www.shopify.com/enterprise/blog/cloud-repatriation [medium]

## See Also

- `library/technology/large-language-models.md` -- LLMs are among the
  most significant cloud workloads; their training and inference depend
  on the elastic compute that only hyperscalers provide at scale.
- `library/technology/cybersecurity-principles-threats-and-defense-in-depth.md` --
  cloud security is a major dimension of modern cybersecurity, and the
  shared responsibility model creates distinct attack surfaces.
- `library/coding-agentic-ai/anchor-coding-agentic-ai.md` -- AI agents
  and coding assistants run on cloud infrastructure; the economics of
  cloud compute directly shape what is feasible in agentic AI.
