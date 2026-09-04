---
name: agent-protocol-design
id: 20260904T051832Z
tier: library-topic
domain: coding-agentic-ai
author: Library Runner
tags: [agent-protocols, interoperability, mcp, a2a, capability-negotiation, agent-communication]
links: [library/coding-agentic-ai/anchor-coding-agentic-ai.md, library/coding-agentic-ai/multi-agent-orchestration.md, library/coding-agentic-ai/tool-use-and-function-calling.md, library/coding-agentic-ai/agent-sandboxing-and-security.md]
---

# Agent Protocol Design -- Interoperability Requires Explicit Contracts, Not Shared Assumptions

Agent protocol design turns an otherwise private agent implementation into a system that another agent, client, tool server, or human-facing application can discover and use without sharing its internals. The central engineering claim is that interoperability comes from explicit contracts for identity, capabilities, message shape, lifecycle, authorization, and failure handling; a common model, framework, or natural-language convention is not a substitute for those contracts. [1][2][5][6]

## Background

A protocol is an agreement about observable behavior. In software terms, it defines what a participant may send, what another participant may return, how each side identifies a request or task, and what both sides must do when a capability is absent or an operation fails. JSON-RPC 2.0 illustrates the minimum transport-neutral layer: a request specifies a version, method, optional structured parameters, and an identifier; a response correlates to that identifier; and a notification intentionally has no identifier and therefore no response. [9] The protocol does not decide whether a caller is an editor, an agent, or a tool server. It makes the message exchange interpretable once those roles have been assigned.

Agent systems add requirements that ordinary RPC alone does not settle. A language-model application may need to discover a tool schema, a remote agent may need to describe a long-running task, and an editor may need a coding agent to report incremental progress and request file or terminal access. Those interactions require a contract for more than an endpoint name. They require a vocabulary for capabilities, input and output formats, state changes, permissions, and compatibility. The current protocol documents for MCP, A2A, and the two protocols called ACP make those boundaries explicit in different ways. [2][3][5][6][7][8]

The Model Context Protocol (MCP) addresses the connection between an LLM application and specialized context or tool providers. Its architecture defines a host that coordinates clients, client instances that each maintain an isolated connection to a server, and servers that expose focused resources, prompts, and tools. The host retains responsibility for orchestration, permission decisions, and separation between server connections. [2] MCP therefore standardizes a provider interface inside an agent application; it is not a general claim that every remotely accessible agent should be treated as a tool. This distinction matters because a complete agent may have its own task lifecycle, skills, authentication requirements, and artifacts. [2][4]

MCP's capability negotiation is a concrete example of contract-first design. During initialization, clients and servers declare which optional facilities they support. A server that exposes tools advertises the tools capability, while tool listings provide names, descriptions, and input schemas that allow a client to determine how an invocation must be shaped. [2][4] The resulting interface is composable only when a client uses the declared contract rather than assuming that a particular server implements every optional facility.

The Agent2Agent protocol (A2A) addresses a different boundary: communication and collaboration between independent, potentially opaque AI agent systems. The A2A specification names discovery, modality negotiation, collaborative task management, and secure information exchange without requiring an agent to reveal internal memory, tools, or reasoning. [5] Its model separates a canonical data layer, abstract operations, and concrete protocol bindings. That separation lets the meaning of a task, message, artifact, or agent card remain stable while implementations choose a compatible binding such as JSON-RPC, gRPC, or HTTP/REST. [5]

A2A's Agent Card is an answer to the question that point-to-point integrations often leave implicit: how does a caller know what a remote agent is, where to reach it, which inputs it accepts, and which authentication and interaction features it supports? The A2A discovery documentation specifies an Agent Card containing identity, service endpoint, capabilities, authentication information, and skill descriptions. It describes well-known URIs, curated registries, and direct configuration as distinct discovery approaches rather than pretending that one discovery method fits public, enterprise, and tightly coupled deployments equally well. [6]

The acronym ACP requires particular care because it names two different protocol efforts. Agent Communication Protocol describes an agent-to-agent interoperability protocol with REST-based communication, varied modalities, discovery, and support for synchronous and asynchronous operation; its official documentation states that it is now part of A2A under the Linux Foundation. [7] Agent Client Protocol instead defines communication between coding agents and clients such as editors. It uses JSON-RPC 2.0 methods and notifications, initialization and capability exchange, sessions, prompt turns, progress updates, permissions, file operations, and terminal operations. [8] Treating either ACP as a generic synonym for every kind of agent interoperability is a scope error. The names are similar, but the roles and lifecycle contracts are different.

The distinction among layers gives protocol selection a simple starting point. MCP is appropriate when an agent host needs standardized access to tools, resources, prompts, or contextual services. A2A is appropriate when an independently deployed agent needs to advertise itself, accept a collaboration task, and exchange results with another agent. Agent Client Protocol is appropriate when an interactive coding client needs to manage a coding-agent session and its user-facing work loop. These are complementary interfaces, not interchangeable brands. [2][4][5][6][8]

The author's synthesis is that protocol design should begin by naming the boundary that must be stabilized. A team that starts with a favored transport or framework can accidentally expose the wrong abstraction: it can reduce a remote autonomous agent to a tool call, or turn a local tool server into a faux peer agent. Starting with roles, trust boundaries, and lifecycle requirements makes the protocol smaller and its failure modes easier to test. This synthesis follows the role separation and capability declarations in the cited specifications. [2][5][8]

## Core Concepts

### Protocol Layer and Boundary Selection

The first design decision is the protocol layer. A transport contract states how messages travel. A data-model contract defines the objects whose meaning must survive transport changes. A capability contract specifies optional functions. A lifecycle contract defines state transitions and completion. An authorization contract defines who can use which operation under what conditions. Collapsing all five into a single API description makes compatibility brittle because a change in one layer can silently alter another. A2A explicitly separates canonical data, abstract operations, and protocol bindings, while MCP distinguishes architecture, primitives, capability negotiation, and transport authorization. [3][5]

The boundary determines the minimum useful contract. For example, a client that needs a weather lookup service normally needs a tool name, input schema, result content, and an authorization path. It does not need to know the provider's model state or internal plan. MCP tools expose exactly this type of focused interface: a server declares tool support, a client lists tools, and calls identify a selected tool with structured arguments. [4] Conversely, a caller that delegates a research task to a remote agent needs a durable task identity, progress and completion semantics, artifacts, and a way to learn whether the remote participant can accept the request. A2A makes these agent-level concerns first-class. [5][6]

The author's synthesis is a boundary test: ask whether the remote side is being used for a bounded function, a continuing autonomous task, or an interactive work session. The first case points toward a tool-provider contract, the second toward an agent-to-agent contract, and the third toward an agent-client session contract. A system can implement more than one layer, but it should not describe one layer as if it supplied guarantees that belong to another. [4][5][8]

### Roles, Ownership, and Trust Boundaries

A useful protocol names its participants and assigns responsibility for each decision. MCP assigns the host the coordinating role: it creates clients, controls connection permissions and lifecycle, handles user authorization decisions, and isolates server connections. Servers expose specialized capabilities but should not receive the whole conversation or inspect other servers' contexts. [2] This avoids an ambiguous model in which every component assumes another component has performed consent, routing, or data minimization.

A2A instead assumes peer interaction among independent agent systems. It describes collaboration without requiring one agent to expose its internal state, memory, or tools to another. [5] Its Agent Card informs a potential client about the remote agent's public identity, skills, endpoint, capabilities, and authentication requirements. [6] The remote agent is consequently a separately governed system, not merely a function with an undocumented implementation.

Agent Client Protocol uses a different ownership model. The client provides the user-facing environment, and the agent reports work through methods and notifications. The documented flow includes initialization, optional authentication, creation or loading of a session, a prompt turn, progress updates, user permission requests, and cancellation. [8] An editor can therefore mediate user interaction and environment access without assuming that the coding agent has unrestricted control.

The design implication is straightforward but important: authority must have an owner. A specification may define a method that requests a file write, but a client or policy layer must decide whether the requested write is allowed. The MCP tools specification recommends clear disclosure of exposed tools and a human ability to deny tool invocations. [4] The MCP authorization specification further separates an MCP client, protected resource server, and authorization server for HTTP-based transports. [3] A protocol that omits this allocation of responsibility leaves security-critical behavior to undocumented convention.

### Identity, Discovery, and Description

Interoperability begins before the first task or tool call. A caller must identify a participant, obtain an authentic endpoint, and understand the participant's advertised contract. A2A's Agent Card provides a structured description with identity, endpoint, capabilities, authentication schemes, and AgentSkill descriptions including identifiers, names, descriptions, input modes, output modes, and examples. [6] This enables a client to reject an incompatible agent before sending sensitive context or creating work it cannot monitor.

Discovery is deployment-dependent. The A2A documentation describes a well-known URI for public or domain-controlled discovery, curated registries for catalog-based enterprise discovery, and direct configuration for known private relationships. [6] These approaches create different operational risks. A public endpoint benefits from predictable discovery but needs protective access controls where its card reveals sensitive information. A curated registry centralizes governance but becomes infrastructure that must be operated and trusted. Direct configuration reduces discovery complexity but can make changes require synchronized client updates. [6]

A description is not a proof of trust. An Agent Card can state an authentication scheme or skill, but the caller still needs a policy for which issuers, endpoints, and claimed capabilities it accepts. The author's synthesis is that discovery should produce a candidate, while authenticated transport and local policy decide whether that candidate may receive a request. This separation is consistent with A2A's treatment of Agent Card protection and MCP's transport-level authorization roles. [3][6]

For tool providers, discovery has a more local shape. MCP clients use declared server capabilities and operations such as tools/list to learn the available interface. [2][4] The protocol-level description should include enough information to form a valid structured call, but a host should still decide which discovered tools enter an agent's available context. This keeps tool discovery from becoming automatic trust or automatic authority. [2][4]

### Capability Negotiation and Version Compatibility

A protocol stays usable as implementations evolve only when it states what is mandatory, what is optional, and how a peer learns the difference. MCP uses initialization-time capability declarations. Its architecture documentation explains that clients and servers declare supported features and that each party must respect those declared capabilities for the session. [2] The tools specification gives a concrete case: a server supporting tools must advertise the tools capability, and a client uses a paginated listing to obtain the available tool definitions. [4]

A2A uses a related but broader compatibility model. Its specification identifies a released version and explains that protocol version compatibility is based on major and minor elements, while its canonical data model and abstract operations remain separate from concrete bindings. [5] A2A Agent Cards expose capabilities such as streaming and push notifications so a client can avoid assuming that every agent supports each delivery mode. [6] The important design principle is that an optional feature becomes usable only after both sides have made its availability explicit.

Agent Client Protocol also starts with initialization and capability exchange. Its overview distinguishes baseline methods from optional methods such as session loading, file reading, file writing, terminal management, and structured user elicitation. [8] This prevents a client from expecting a particular editor integration to support every interaction a more capable agent can offer.

The author's synthesis is that compatibility has three dimensions: wire compatibility, semantic compatibility, and policy compatibility. Two components can parse the same JSON yet disagree about a task state. They can agree about a task state yet disagree about whether a given user approval permits a side effect. Therefore a robust compatibility test must include version negotiation, named capabilities, schema validation, and authorization checks. The cited specifications establish the first three; the final check is an engineering control required when protocol messages can cause side effects. [2][3][5][8]

### Correlation, State, and Completion

Every nontrivial interaction needs a way to correlate later information with the work that caused it. JSON-RPC uses the request identifier: a response must include the same identifier, while a notification omits one and receives no response. [9] This distinction prevents a caller from confusing a one-way progress signal with proof that an operation succeeded.

Agent-level workflows need more than request-response correlation. A2A defines first-class Task, Message, AgentCard, Part, Artifact, and Extension data-model concepts, plus operations for sending messages, obtaining tasks, listing tasks, canceling tasks, and retrieving an Agent Card. [5] This represents work that may be long-running, stream updates, request more input, produce artifacts, fail, or be canceled. An agent protocol must specify which transitions are allowed, which participant owns the transition, and how a reconnecting client learns the current state.

Agent Client Protocol similarly distinguishes a session from a prompt turn. A client creates or resumes a session, sends a session/prompt request, receives session/update notifications during work, can issue session/cancel, and receives a terminal response carrying a stop reason. [8] This lifecycle is a better representation of interactive coding work than a single opaque RPC because it can show progress and support a user's control over ongoing work.

The author's synthesis is that a state machine should be written before an endpoint list. The state machine should include success, failure, cancellation, expiration, retry, duplicate delivery, and user-input-required paths. A message schema alone cannot tell an implementer whether a retry creates a second task or resumes the first one. A task identifier alone cannot tell an operator whether a late progress update is valid after cancellation. The A2A and Agent Client documents demonstrate the value of named task and session lifecycles; the remaining edge states are a local contract decision that should be made explicit. [5][8]

### Message Schema, Modality, and Extensibility

A shared transport does not make arbitrary payloads interoperable. A message contract must state whether content is text, structured data, a file reference, or a binary object; it must name required fields and the rules for extending them. A2A is explicitly modality agnostic and identifies text, files, structured data, and other forms as interaction modes that agents can negotiate. [5] Its Agent Card lets an AgentSkill declare input and output modes, allowing a caller to determine whether an interaction is suitable before it creates a task. [6]

MCP tool definitions use an input schema. A tool listing contains a tool name, description, and inputSchema; a tool call supplies a selected name and structured arguments. [4] This reduces ambiguity at the function boundary, but it does not validate an application-specific semantic promise by itself. For example, a field named target may be syntactically a string but still require a policy-defined interpretation such as an allowlisted repository or account.

Agent Client Protocol reserves extensibility mechanisms while retaining a base convention. Its documentation permits custom data in _meta fields and custom methods with an underscore prefix, and it describes capability advertisement for optional behavior. [8] JSON-RPC likewise reserves method names beginning with rpc. for system extensions. [9] These mechanisms are useful only when extensions are namespaced, versioned, documented, and rejected safely by implementations that do not recognize them.

The author's synthesis is that extensibility should preserve a strict core. Put commonly required identity, correlation, capability, and error fields in the core schema. Put vendor-specific metadata in a namespaced extension field. Do not overload a free-form description with security-relevant semantics. This makes an old implementation able to decline a new feature without silently misinterpreting a side effect. [4][8][9]

### Security, Authorization, and Human Control

Protocol interoperability can increase exposure as well as reuse. A remote endpoint, a tool descriptor, or an Agent Card supplies information that a model or application may use to choose an action. The MCP architecture constrains server visibility by leaving full conversation history with the host and isolating server connections. [2] The MCP tools specification recommends an interface that shows users which tools are exposed, signals invocation, and supports confirmation for operations. [4]

For HTTP-based MCP transports, the authorization specification defines roles for an MCP client, protected resource server, and authorization server. It requires protected-resource metadata support by servers and specifies discovery mechanisms for authorization servers. [3] The document also distinguishes HTTP transport authorization from STDIO use, where credentials are ordinarily obtained from the environment. [3] The protocol therefore supplies an authorization framework but does not remove the engineering need to minimize credentials, restrict side effects, and record policy decisions.

A2A's discovery documentation cautions that Agent Cards can contain sensitive details, such as internal URLs and skill descriptions, and recommends authenticated extended cards for sensitive information. [6] A2A's main specification also identifies authentication, authorization, security, privacy, tracing, and monitoring as enterprise requirements. [5] These statements are requirements to design and verify controls, not evidence that a remote agent is trustworthy because it publishes a standards-shaped card.

The author's synthesis is a least-authority rule for protocol design: discover broadly only where appropriate, disclose the minimum necessary contract, authenticate before restricted operations, authorize each consequential action at the enforcing boundary, and preserve auditable correlation among user, task, tool, target, and outcome. This rule translates the cited protocol security structures into a deployable control plane. [2][3][4][5][6]

## Evidence

The evidence base for agent protocols is primarily normative specification evidence and documented interface cases rather than controlled experiments that measure a universal productivity effect. A standard can show what its maintainers require an implementation to do; it cannot by itself prove that every implementation is secure, interoperable, or operationally effective. The cases below therefore report the design method and stated result from primary protocol documentation, while keeping that limitation explicit.

### Case 1: MCP Separates Host Coordination from Focused Server Capabilities

Method: the MCP architecture specification defines the responsibilities of its three named roles and its capability-negotiation mechanism. The host creates and manages client instances, controls permissions and lifecycle, handles user authorization decisions, and coordinates model integration. Each client maintains an isolated connection to a particular server. Servers expose focused resources, prompts, and tools rather than receiving unrestricted access to the host's whole conversation. [2]

Finding: the documented architecture makes composability depend on host-governed isolation and declared capabilities. The specification states that clients and servers explicitly declare supported features during initialization and must respect those declarations; it gives resource subscriptions, tool support, prompt templates, sampling, and notification handling as examples. [2] This is direct evidence that MCP treats interoperability as a negotiated contract rather than an assumption that all providers have an identical feature set.

A second MCP document provides a concrete testable interface case. Method: the tools specification requires a server supporting tools to advertise tools capability, defines tools/list for discovery and tools/call for invocation, and represents tool inputs with JSON Schema-like inputSchema data. [4] Finding: a conforming client can discover a tool name and its expected structured arguments before calling it. The same document recommends a human ability to deny tool invocations and visible confirmation for operations, showing that schema discovery does not transfer authorization ownership to the model. [4]

The authorization specification supplies a third dimension of the MCP case. Method: it defines an HTTP transport authorization model based on selected OAuth-related specifications and names client, protected resource server, and authorization server roles. [3] Finding: protected resources and authorization-server discovery are explicit elements of the contract for HTTP-based MCP, while STDIO implementations are directed to retrieve credentials from the environment instead. [3] The evidence supports a layered reading: tool schema, capability negotiation, and authorization are related but separate interfaces.

### Case 2: A2A Makes Independent-Agent Collaboration a First-Class Contract

Method: the A2A specification defines a canonical data model consisting of Task, Message, AgentCard, Part, Artifact, and Extension; it then separates abstract operations from concrete bindings. Its stated goal is communication and interoperability between independent, potentially opaque agent systems, including discovery, modality negotiation, task collaboration, and information exchange without access to the other agent's internal state, memory, or tools. [5]

Finding: A2A treats remote-agent collaboration as more than a function invocation. The documented operations include sending messages, sending streaming messages, getting and listing tasks, canceling tasks, and obtaining an Agent Card. [5] The protocol also documents synchronous responses, streaming updates, asynchronous push notifications, long-running work, and human-in-the-loop scenarios as design goals. [5] These requirements make task state, artifacts, and delivery style part of the interoperable surface.

The Agent Card documentation is a focused discovery case within A2A. Method: it specifies an Agent Card as a JSON description containing identity, endpoint, capabilities, authentication, and skills, then describes well-known URI, curated registry, and direct-configuration discovery. [6] Finding: discovery can be selected according to deployment context rather than embedded as an undocumented assumption. The document also says that the current A2A specification does not prescribe a standard API for curated registries, an important negative finding because it prevents an implementer from claiming registry interoperability that the protocol does not define. [6]

The security limits are also observable in this case. The discovery document identifies internal URLs and sensitive skill descriptions as potentially sensitive Agent Card information and recommends authenticated extended cards for sensitive data. [6] This supports the narrower conclusion that publishing a descriptor is a security decision; it does not support a stronger claim that a descriptor proves a peer's safety or reliability.

### Case 3: ACP Names Must Be Disambiguated by Role and Lifecycle

Method: the Agent Communication Protocol documentation describes an open interoperability protocol for agents, applications, and humans. It lists REST-based communication, multiple MIME-typed content forms, offline discovery, and asynchronous-first operation with synchronous support. The same official page states that this ACP is now part of A2A under the Linux Foundation. [7]

Finding: this ACP case supplies historical and conceptual evidence for consolidation around an agent-to-agent contract, but it also creates a naming hazard. An implementation or architecture document that uses ACP without expansion can refer to a protocol whose documentation declares it part of A2A, not necessarily to an active independent wire contract. [7] Protocol documents should therefore specify the full name, version, role relationship, and source of truth instead of relying on acronyms.

Method: Agent Client Protocol documentation describes a different ACP. It defines bidirectional JSON-RPC communication between coding agents and clients, with method calls and notifications. Its typical flow is initialization, optional authentication, session creation or loading, a prompt turn, session updates, potential permission requests, cancellation, and a terminal response. [8]

Finding: this ACP's interface is centered on the editor-to-coding-agent session, not on generic remote-agent delegation. Its optional client capabilities include file read and write, terminal management, and user elicitation, while its extensibility mechanism allows _meta fields and underscore-prefixed custom methods. [8] The contrast between the two ACP documents is direct evidence that protocol selection cannot be inferred from a name alone. The role relationship and lifecycle are the discriminating variables.

### Case 4: JSON-RPC Provides Correlation Semantics, Not Agent Semantics

Method: the JSON-RPC 2.0 specification defines a stateless, lightweight RPC format that is transport agnostic. Its request object contains jsonrpc, method, optional params, and optionally id; responses return the matching identifier. A notification is a request without id, and the server must not reply to it. [9]

Finding: JSON-RPC supplies a precise correlation rule and a distinction between requests and one-way notifications. MCP tools and Agent Client Protocol both use JSON-RPC 2.0 message semantics in their documented interfaces. [4][8][9] The evidence supports the limited conclusion that these protocols can share an RPC envelope while still defining different roles, capabilities, and lifecycles above it. It does not support the claim that JSON-RPC alone provides task discovery, agent identity, authorization, or long-running work management.

Across all four cases, the repeated design pattern is explicitness: declared roles, typed objects, named capabilities, documented optionality, stable identifiers, and defined security boundaries. This is an author synthesis from the cases, not a measured causal result. The primary specifications establish the interfaces; deployment testing is still required to show that two selected implementations actually interoperate under expected failures and policy constraints. [2][3][4][5][6][7][8][9]

## Implications

### For Agent-System Architects

The first practical implication is to select the protocol by the boundary being standardized, not by ecosystem momentum. An architect integrating a database, repository, or document service into an agent host should evaluate an MCP-style provider contract: resource and tool exposure, schema discovery, host-controlled authorization, and user-visible invocation controls. [2][3][4] An architect delegating a durable job to an independently run agent should evaluate an A2A-style peer contract: Agent Card discovery, task identity, modality negotiation, artifacts, progress, cancellation, and authentication. [5][6] An architect integrating a coding agent with an editor should evaluate an Agent Client Protocol session contract: initialization, prompts, session state, user permissions, and progress updates. [8]

The author's synthesis is a selection matrix with three questions. First, who owns the user interaction and final authorization decision? Second, does the remote participant expose a bounded capability or execute an autonomous, long-running task? Third, must the caller manage an interactive session and environmental permissions? Answering those questions before choosing a protocol prevents category errors such as treating an external agent as an ungoverned tool or wrapping every local tool as a remote agent. The questions derive from the role differences documented by MCP, A2A, and Agent Client Protocol. [2][5][8]

Protocol layering should be intentional. A system may use Agent Client Protocol between an IDE and its coding agent, MCP inside that coding agent to reach tools and context providers, and A2A between that agent and a separately deployed specialist. This is an author synthesis, not a requirement of any one specification. It follows from the different scopes: client-agent interaction in ACP, host-provider interaction in MCP, and independent-agent collaboration in A2A. [2][4][5][8] The interfaces should expose only the contract required at each boundary and keep internal implementation details behind that boundary.

### For Platform and Security Teams

Protocol metadata is security-relevant configuration. An Agent Card can reveal endpoints, skills, and authentication requirements; an MCP server can advertise tools and schemas; an ACP client can expose file and terminal capabilities. [4][6][8] Platform teams should therefore treat registration, discovery, and capability publication as controlled change processes. A descriptor may be syntactically valid but point to an unapproved endpoint, claim an unreviewed capability, or use an authentication scheme that policy forbids.

For MCP over HTTP, authorization is an explicit transport-layer concern with defined client, resource-server, and authorization-server roles. [3] The practical implication is to bind an access token and requested operation to a resource, scope, audience, and policy decision outside the model's text output. The MCP specification provides the protocol roles and metadata requirements; the following deployment recommendation is the author's synthesis: log the authenticated principal, task or session identifier, selected capability, target resource, user approval where required, and result. This makes an incident traceable even if the model's reasoning is unavailable or unreliable. [3][4]

Human control must sit at a boundary that can refuse execution. MCP's tools documentation recommends clear visibility into exposed tools, invocation indicators, confirmation prompts, and a human ability to deny calls. [4] In a broader platform design, the same principle applies to A2A task submission and ACP file or terminal requests: show the relevant requested effect, apply policy before execution, and return a structured denial or error that the caller can handle. This extension is an author synthesis grounded in the protocols' distinct authorization, user-permission, and security structures. [3][4][5][8]

Security review should also test negative cases. The test suite should verify that a client rejects unsupported capabilities, refuses an untrusted or misconfigured endpoint, treats an expired or absent authorization as a denial, handles a duplicate task or late update safely, and distinguishes a notification from proof of success. The notification rule is specified by JSON-RPC, while capabilities and lifecycle behavior are surfaced by MCP, A2A, and Agent Client Protocol. [2][4][5][8][9] A protocol that only passes the happy path has not demonstrated interoperability under operational conditions.

### For Agent Builders and Integration Authors

A builder should publish the smallest complete public contract. For an MCP server, this means accurate capability declarations and tool schemas that describe the arguments a caller must provide. [2][4] For an A2A agent, it means an Agent Card whose identity, skills, endpoint, input and output modes, capabilities, and authentication descriptions match the implementation. [6] For an Agent Client Protocol agent, it means negotiated capabilities that truthfully represent available session, filesystem, terminal, permission, and update behavior. [8]

Overclaiming is a protocol defect. Advertising streaming, push notifications, file writes, or a particular skill while silently failing at runtime creates the same integration failure as omitting a required field. A safe implementation either honors a declared capability or rejects its negotiation. The author's synthesis is that capability declarations need contract tests: a test should fetch the descriptor, exercise every advertised baseline operation, verify the advertised failure behavior, and confirm that unadvertised optional operations are not accepted accidentally. This test strategy follows the documents' capability-based interfaces. [2][4][6][8]

Naming must be fully qualified in source code, configuration, and runbooks. Write "Model Context Protocol" or "MCP" only after the first expansion; write "Agent2Agent Protocol (A2A)" when referring to the peer-agent standard; and distinguish "Agent Communication Protocol" from "Agent Client Protocol" when using ACP. The documentation directly supports the distinction: the former says it is now part of A2A, while the latter specifies editor-client and coding-agent interactions. [7][8] This small documentation discipline prevents an integration team from implementing a technically correct protocol at the wrong architectural boundary.

Version and extension management require the same discipline. Pin the protocol version that an integration was tested against, record negotiated capability sets, namespace custom fields, and document the fallback when a peer lacks a feature. A2A's versioning and layered bindings, MCP's initialization capabilities, Agent Client Protocol's optional methods and extension conventions, and JSON-RPC's reserved system-extension names all support this approach. [2][5][8][9] The author's synthesis is that a compatibility matrix should be an artifact of release engineering, not tribal knowledge in a prompt or wiki page.

### For Operators, Evaluators, and Procurement Teams

An interoperability claim should be evaluated as a set of observable tests. The minimum test should include discovery, identity validation, capability negotiation, one valid request, one invalid request, authorization success and denial, a state transition, cancellation where supported, a reconnect or retry case, and log correlation. The exact surface differs by protocol: A2A supplies Agent Cards and task operations; MCP supplies server capabilities and tool operations; Agent Client Protocol supplies session and update methods; JSON-RPC supplies request and notification correlation. [2][4][5][6][8][9]

Documentation should be read as a contract, not marketing. The A2A discovery guide explicitly says that curated registries have no standard API prescribed by the current specification. [6] This means a vendor can support A2A Agent Cards yet still require a proprietary registry integration. Similarly, MCP's authorization rules apply to HTTP-based transports and explicitly distinguish STDIO credential behavior. [3] A capability statement without a deployment context is incomplete evidence for interoperability.

The author's synthesis is that procurement questions should ask: Which version and binding are implemented? Which capabilities are mandatory, optional, or absent? How are identity and authorization established? What are the state and cancellation semantics? Which artifacts or logs allow an operator to reconstruct a failure? What is the fallback when a peer does not implement an extension? These questions convert a broad standards claim into verifiable acceptance criteria. [2][3][5][6][8]

Finally, protocol choice should preserve reversibility. Start with the smallest interface that covers the required boundary, retain an adapter at the edge, and avoid allowing protocol metadata to become direct authority for side effects. This is an author synthesis based on the separation of host, server, agent, client, authorization, capability, and lifecycle roles in the cited specifications. [2][3][4][5][8] When a protocol evolves or an ecosystem consolidates, an explicit adapter and recorded contract make replacement possible without rewriting the agent's core logic.

## Sources

1. Model Context Protocol. "Specification." Official protocol specification, version 2025-11-25.
   https://modelcontextprotocol.io/specification/2025-11-25 [high]

2. Model Context Protocol. "Architecture." Official protocol architecture and capability-negotiation documentation, version 2025-11-25.
   https://modelcontextprotocol.io/specification/2025-11-25/architecture [high]

3. Model Context Protocol. "Authorization." Official authorization requirements for MCP HTTP transports, version 2025-11-25.
   https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization [high]

4. Model Context Protocol. "Tools." Official server-tools capability, discovery, and invocation documentation, version 2025-11-25.
   https://modelcontextprotocol.io/specification/2025-11-25/server/tools [high]

5. A2A Protocol. "Agent2Agent (A2A) Protocol Specification." Official A2A specification, latest release 1.0.0.
   https://a2a-protocol.org/latest/specification/ [high]

6. A2A Protocol. "Agent Discovery in A2A." Official Agent Card and discovery documentation.
   https://a2a-protocol.org/latest/topics/agent-discovery/ [high]

7. Agent Communication Protocol. "Welcome." Official documentation stating ACP's agent-interoperability scope and its incorporation into A2A.
   https://agentcommunicationprotocol.dev/introduction/welcome [high]

8. Agent Client Protocol. "Overview." Official protocol documentation for client-to-coding-agent communication.
   https://agentclientprotocol.com/protocol/v1/overview [high]

9. JSON-RPC Working Group. "JSON-RPC 2.0 Specification." Primary specification for request, response, identifier, and notification semantics.
   https://www.jsonrpc.org/specification [high]

## See Also

- `library/coding-agentic-ai/anchor-coding-agentic-ai.md` -- domain scope for agent protocol design.
- `library/coding-agentic-ai/multi-agent-orchestration.md` -- orchestration topologies that need explicit handoff and communication contracts.
- `library/coding-agentic-ai/tool-use-and-function-calling.md` -- the tool boundary that MCP standardizes for agent hosts and servers.
- `library/coding-agentic-ai/agent-sandboxing-and-security.md` -- enforcement boundaries for agent capabilities and tool side effects.
