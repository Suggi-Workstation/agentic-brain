---
name: hindsight-system
id: 20260911T134852Z
tier: insight
status: active
source:
  - 20260911T135041Z
  - 20260810T112711Z
author: Morpheus
tags: [memory, shared-memory, architecture, fleet, embeddings, verification]
links:
  - reflections/2026-09-11_morpheus_memory-needs-evidence-not-another-owner.md
  - reflections/2026-08-10_link_shared-memory-is-an-operations-problem.md
  - research/insights/mnemosyne-system.md
  - research/insights/two-tier-fleet-memory-single-vector-space.md
  - governance/system-blueprint.md
  - governance/system-primedirectives.md
---

# Hindsight System: Native Memory, Deliberate Sharing, Traceable Evidence

## The Insight

**A fleet memory system becomes simpler and more trustworthy when one native engine owns evidence and its derivatives, personal capture stays automatic, and sharing remains a deliberate act rather than an invisible replication pipeline.**

This is an implementation blueprint and a lesson about ownership. It describes the deployed Hindsight memory system for VPS-hosted Hermes profiles, with observation-only recall and the configuration-only cross-session scope workaround verified on 2026-09-12. It is organized by agent role, not by a roster or a hand-maintained bank count. Profile membership can change without changing the design. An agent on another machine, an unconfigured profile, and a temporary delegated worker are not implicitly enrolled merely because they belong to the wider fleet.

Hindsight is the external durable-memory engine. Hermes is its client and the agent runtime. PostgreSQL holds the memory data. Dedicated embedding and reranking models support retrieval; separately configured generative models extract facts, consolidate observations, and reason over evidence. The repositories remain the authoritative home for governance and authored research. These are complementary responsibilities, not interchangeable databases.

The ownership split is explicit. Each enrolled profile automatically retains conversation turns into its own personal bank and retrieves relevant evidence from that bank for the current question. Core profiles additionally receive a native, bank-bound MCP connection to `core-shared`. They choose when to search it and what to contribute. Persistent task-runner profiles receive personal memory without that shared connection by default. No custom classifier copies private conversations into shared memory. No local shared SQLite replica or memory-relay ticker is part of this deployment.

The important qualification is that native does not mean infallible. A stored document can yield no extracted facts. Consolidated observations are fallible derived beliefs, not evidence that the underlying sources may safely be discarded. A generated knowledge page can retain prose after its evidence is deleted. A server tool can exist without appearing in a particular conversation. This blueprint therefore explains the boundaries at which evidence must be checked, as well as the components themselves.

It replaces the former VPS Mnemosyne operating model, not the need for provenance, explicit authorization, or independent verification. It does not claim that every off-host agent has migrated. Historical references remain useful for understanding why the system changed; they are not installation instructions for the present VPS stack.

## Evidence

### Evidence basis and scope

The originating consolidated reflection is `20260911T135041Z`, linked above. It covers the sessions titled **Mnemosyne upgrade + Hindsight comparison**, **Hindsight build**, and the subsequent shared-MCP lifecycle session. Their original distinct user/assistant records, including compacted-out messages, were reviewed. Duplicate notifications and derived compaction summaries were distinguished from new decisions. Historical statements were then compared with the live deployment rather than simply repeated.

The initial local checks included Compose image references and mounts; the running API and database; nonsecret runtime model settings; each enrolled profile's provider settings and shared-tool selection; installed Hermes source at commit `8defaaad4830620ba55e1779e1fe424e80888004`; bank configuration fields; migration and native-transition receipts; and saved native acceptance results. Public documentation was checked against release-pinned Hindsight v0.9.2 sources and current Hermes documentation. Where prose and implementation differed, the narrower implemented behavior governs this account.

The observation-only revision was checked against installed Hermes commit `0b8daf30aae1d0b129ede9b857cac2158eb50324`. Fresh native providers for every enrolled VPS profile requested only observations and returned context through `MemoryManager.prefetch_all` within its eight-second deadline in the sampled checks. Other profile fields were verified unchanged. This establishes the configured retrieval path, not hot activation in an already-open Desktop session or universal semantic accuracy.

The subsequent scope audit on the same installed commit corrected an earlier claim in this blueprint. Although every enrolled personal profile requested `observation_scopes: shared`, the Hermes normalizer returned `None`, omitted the field from actual retain payloads, and produced session-tagged observations. The server was consolidating successfully with no reported backlog; the defect was request shaping, not scheduling. The authorized configuration-only workaround below passed fresh initialization and request-shape checks for every enrolled profile. In a disposable bank, two separate native provider sessions retained the same synthetic project policy and produced one observation with two supporting source facts, one from each session. Native observation-only recall returned that policy. The fixture bank was deleted and its absence verified; production sources and old observations were not rewritten.

This extends the earlier reflection `20260810T112711Z`, **Shared Memory Is an Operations Problem**: configuring a feature is not proof that the consumer receives it. The earlier Mnemosyne insights correctly emphasized end-to-end verification, but their relay, local-replica, publishing-job, and vector-distribution anatomy is historical for migrated VPS profiles.

### System map

```text
Hermes profile
  |
  +-- SOUL / AGENTS / identity ----------> identity and operating anchors
  |
  +-- native Hindsight provider
  |     current question -> personal recall -> relevant prompt context
  |     completed turn -> personal retain -> asynchronous server work
  |     explicit personal retain / recall / reflect tools
  |                          |
  |                          v
  |                    private-<profile>
  |
  +-- core role only: native hindsight_shared MCP
        intentional read / write / synthesis
                           |
                           v
                       core-shared

Both bank classes live inside the same Hindsight service:
  source documents -> extracted facts + entities + retrieval indexes
                                |
                                v
                    consolidated observations
                                |
                                v
              optional mental models / knowledge pages

Hindsight API + native workers <----> PostgreSQL + pgvector
          |
          +-- resident local embedding / reranking models
          +-- configured remote generative-model route

Repository search and authored Git artifacts remain separate.
```

The shared service is justified by shared runtime and shared fleet knowledge. Personal data remains logically separated by bank. This is a trusted-fleet ownership and default-routing model, not a claim of cryptographic isolation between agents holding equivalent service credentials. Adding an untrusted tenant would require a separate access-control design.

### Role boundaries

| Role | Automatic memory | Explicit personal tools | Shared memory | Enrollment boundary |
|:--|:--|:--|:--|:--|
| Core agent profile | Own `private-<profile>` bank | Native retain, recall, reflect | Native `hindsight_shared` MCP bound to `core-shared` | Shared access is an explicit profile configuration |
| Persistent subagent or task-runner profile | Own `private-<profile>` bank | Same native personal tools | Not configured by default | Its own profile, bank, and task scope; not the parent's private bank |
| Temporary delegated worker | Determined by actual host delegation behavior | Only the tools/context actually supplied | No entitlement inferred from parent role | A temporary worker is not automatically a new persistent bank |
| Other or off-host agent | Not established by this blueprint | Inspect that runtime | Requires separately approved connection | Fleet membership alone is not evidence of installation |

A core agent does not automatically receive every shared fact on each turn. It deliberately recalls or reflects through MCP when shared context is relevant. A personal observation scope is likewise local to its bank: the deployed `scope:private` tag is not a destination, an access grant, or publication to `core-shared`.

### Filesystem and persistence map

The service root is `/srv/hindsight/`. Profile connection settings remain in Hermes profiles; putting the server under one directory does not move Hermes's session database or Docker's internal storage there.

| Path | Responsibility | Persistence and handling |
|:--|:--|:--|
| `/srv/hindsight/compose.yaml` | Defines the database and Hindsight API services, pinned images, mounts, nonsecret model settings, and resource controls | Deployment configuration; inspect before changing the service |
| `/srv/hindsight/data/postgres/` | PostgreSQL data, including documents, facts, entities, vectors, observations, model/page records, and native operation state | Authoritative mutable memory store; not a Git folder or disposable cache |
| `/srv/hindsight/cache/` | Hindsight model-download/cache files | Reusable disk cache; distinct from models already loaded in RAM |
| `/srv/hindsight/auth/codex/` | Dedicated Hindsight Codex authentication state | Private, writable credential state; never publish its contents |
| `/srv/hindsight/secrets/service.env` | Hindsight service secrets | Local-only; not blueprint content or a shared artifact |
| `/srv/hindsight/secrets/postgres.env` | PostgreSQL initialization/access secrets | Local-only; never print or commit values |
| `/srv/hindsight/secrets/` | Other approved client/service credential material | Use through the authorized credential path, not by copying secrets into instructions |
| `/srv/hindsight/tools/codex/` | Local Codex CLI installation used for the service's sign-in workflow | Authentication utility, not the memory database or a custom memory worker |
| `/srv/hindsight/README.md` | Lean deployment entry point | Orientation; effective Compose/profile/bank settings still need inspection |
| `/srv/hindsight/migration-result.json` | Receipt for the historical native import | Historical outcome, not a live inventory counter |
| `/srv/hindsight/deployment-result.json` | Cutover and retirement receipts | Historical deployment evidence; earlier intermediate failure fields require chronology |
| `/srv/hindsight/native-transition.json` | Receipt for replacing custom integration with native provider ownership | Historical evidence of plugin/outbox removal and native activation |
| `/srv/hindsight/retirement-jobs.json` | Retired-job record | Not an active scheduler or authorization to restore old jobs |
| `/srv/hindsight/.gitignore` | Exclusion intent for sensitive/generated material | Does not by itself establish that this service directory is versioned |

The Compose bind mappings are significant: host `data/postgres/` is mounted at `/var/lib/postgresql/18/docker`; host `cache/` at `/home/hindsight/.cache`; host `auth/codex/` at `/home/hindsight/.codex`. These are the actual deployed mappings, not the earlier proposed mount paths. Docker image layers, container runtime metadata, and container logs remain under Docker's own management. No separate knowledge-page filesystem mirror is installed by this blueprint.

For a named profile, define `P=/home/hermes/.hermes/profiles/<profile>`:

| Profile path | Responsibility |
|:--|:--|
| `P/config.yaml` | Selects `memory.provider: hindsight`; core profiles also define `mcp_servers.hindsight_shared` |
| `P/hindsight/config.json` | Native provider endpoint, bank, mode, capture policy, recall policy, tags, and budgets |
| `P/.env` | Profile-local credentials resolved by Hermes; values are not documentation |
| `P/state.db` | Hermes's canonical conversation/session store and FTS history; not the Hindsight database |
| `P/sessions/` | Hermes transcript/routing artifacts as provided by the runtime |
| `P/logs/agent.log` | Provider registration and operational diagnostics; inspect narrowly because logs can contain private context |
| `P/SOUL.md` and the configured workspace's `AGENTS.md`, `IDENTITY.md`, `BOX.md` | Identity, operating rules, and lean machine reference |
| Configured workspace `memory/` and `identity/` | Authored session learning and identity history under Git |
| `P/skills/` | Profile-specific operational procedures and learned verification workflows |

The source implementation is in the Hermes installation's `plugins/memory/hindsight/`; the inspected entry point is `/home/hermes/.hermes/hermes-agent/plugins/memory/hindsight/__init__.py`. `agent/memory_manager.py` owns the host's provider lifecycle. Native MCP discovery and dispatch live in `tools/mcp_tool_discovery.py` and `tools/mcp_tool_handlers.py`. These are reference locations, not invitations to patch installed core code.

### Configuration ownership and precedence

There are distinct configuration layers. Mixing them creates convincing but false explanations:

| Layer | Owns | Does not own |
|:--|:--|:--|
| Hermes profile `config.yaml` | Provider selection and MCP exposure | Server fact extraction model or PostgreSQL storage layout |
| Profile `hindsight/config.json` | Personal bank selection and automatic turn behavior | Automatic publication to another bank |
| Hindsight Compose/environment | Server model routes, retrieval implementation, workers, storage connection, defaults | Which tools a particular Hermes conversation has attached |
| Hindsight bank configuration in PostgreSQL | Bank-specific extraction/consolidation/reflect policy and supported overrides | Hermes's main conversation model or session summarizer |
| MCP tool allowlist | Which discovered operations are exposed to the agent | Server authorization, disabling storage capabilities, or granting permission to mutate |
| SOUL/AGENTS and canonical governance | Agent authorization and operating standards | A second executable memory pipeline |

An operator must resolve bank overrides before declaring a global default effective. The installed Hindsight configuration API explicitly rejects reading bank-configurable fields as if they were unconditional global settings. In the inspected banks, observations and concise extraction are explicitly enabled; automatic consolidation, near-duplicate reconciliation, and history behavior use the inspected server defaults unless overridden.

The native personal configuration currently uses `local_external`, not `local_embedded`. That means Hermes connects to the already-running server; it does not start a private Hindsight/PostgreSQL daemon for each profile. `memory_mode: hybrid` supplies both automatic context and explicit tools. `bank_id` selects the profile's personal bank; `bank_id_template` is empty, preventing a dynamic template from silently superseding that explicit destination.

Capture is enabled with `auto_retain: true`, `retain_async: true`, and `retain_every_n_turns: 1`. Current-question recall is enabled with `auto_recall: true`, `recall_sync: true`, `recall_prefetch_method: recall`, and `recall_types: observation`. The type filter follows Hermes's prescribed consolidated-knowledge default; synchronous current-question recall remains an explicit choice instead of previous-turn prefetch. Automatic context and the native personal `hindsight_recall` tool both use this filter. Raw world/experience facts remain stored as evidence but are no longer independently injected by those paths; newly extracted evidence must reach an observation first. Deliberate Reflect and exact source/API inspection remain available for deeper evidence review.

The provider reads `hindsight/config.json` at session initialization. An already-open client needs a fresh agent initialization, such as starting a new chat, to load a changed filter or retain scope; editing the file does not retroactively change cached provider settings or previously injected context. This is a client lifecycle boundary, not a reason to restart the Hindsight API or database. The provider's JSON settings are not inherited from the machine-wide Hermes YAML policy.

Use the native key `recall_prefetch_method`, not the stale `prefetch_method` spelling in the external integration guide. Automatic injection remains Recall; Reflect stays a deliberate personal or shared tool call. The native [provider reference](https://github.com/NousResearch/hermes-agent/blob/0b8daf30aae1d0b129ede9b857cac2158eb50324/plugins/memory/hindsight/README.md) governs these client settings.

The inspected recall budget is `mid`; `recall_max_tokens` is 4096 and `recall_max_input_chars` is 800. The latter limits the *query sent to automatic recall*, not stored source text. A decisive topic late in a long user message may therefore need an explicit, focused recall. A fact-text budget is also not a guarantee that an MCP JSON envelope, provenance, or legacy metadata fits the same size.

**Cross-session consolidation.** Hindsight officially supports the retain-item parameter `observation_scopes: "shared"`, equivalent to `[[]]`: one untagged observation scope inside a bank, with provenance tags preserved on source facts. It is not a server environment variable or a bank-configurable default. Retain strategies cannot supply it because they only override supported hierarchical configuration fields. The installed Hermes normalizer accepts neither `"shared"` nor `[[]]`; both become `None`, silently reverting to the server's session-fragmenting `combined` default. Hermes issue #74933 documents this exact defect, and keyword-fix PR #72565 remained unmerged when checked on 2026-09-12. The earlier assertion that the configured keyword was effective was incorrect.

All enrolled VPS personal profiles instead use the issue's configuration-only workaround in `P/hindsight/config.json`: `retain_tags: ["scope:private"]` and `observation_scopes: [["scope:private"]]`. The native adapter preserves this explicit nonempty scope. Source facts carry both the stable tag and their original session/parent lineage tags; observations carry only `scope:private`, allowing related evidence from different sessions to consolidate together. Reusing that label in separate personal banks does not merge the banks. This is one common fleet provisioning policy applied to each enrolled profile, not a hidden root-profile inheritance rule or a universal policy for arbitrary API/MCP writers.

This workaround creates a named scope, not Hindsight's untagged `shared` scope. Existing personal recall has no tag restriction, so it can retrieve the named observations. Any future tag-filtered reader or generated page must be checked against that distinction. Existing observations in session or migration scopes remain in place: changing future retain requests does not migrate old source scope assignments or clean their derivatives. Such reconciliation is a separately authorized data operation. No Hermes source patch, service restart, or bank-wide observation reset was part of this correction.

### A conversation's end-to-end path

**Recall before the reply.** Hermes calls the active provider with the current question. In synchronous mode, the provider queries the selected personal bank now, rather than returning the previous turn's background result. Hindsight searches relevant evidence; the provider formats returned text into a memory-context block for the current model request. This context is evidence to evaluate, not a new user instruction. The system-prompt header naming the bank is only an identity/status declaration; it does not prove a successful retrieval.

**Answering.** The main conversation model uses the question, bootstrap instructions, recent conversation, and retrieved evidence. It can request further personal recall or synthesis. A core agent can separately discover and invoke shared MCP tools. These optional shared calls are visible actions; there is no automatic multi-bank merge hidden behind native personal prefetch.

**Capture after the turn.** After a completed response, the host calls the installed provider's `sync_turn`, which builds labeled user/assistant messages, timestamps and metadata, then hands work to a FIFO background writer. The configured interval is every completed conversational turn, not every internal tool call; interrupted turns are skipped by the host. For an append-capable server, the normal path uses a stable session document ID and sends new turn deltas with append semantics. Session identifiers also provide provenance tags. This is not a second hand-written SQLite outbox.

There is a documentation qualification here. General Hermes prose advertises full turns, including tools. The inspected provider interface accepts user and assistant content strings and serializes those. This inspection does not prove that every internal tool event is retained as its own Hindsight source. Exact execution history still belongs to Hermes's session records; a retrieved fact is not a verbatim transcript ledger.

**Server processing.** Asynchronous retain acceptance returns before extraction and indexing necessarily finish. The server stores source text, applies the bank's extraction policy, associates entities and time information, creates facts, embeds them, and updates retrieval structures. Concise extraction selects useful information rather than manufacturing a fact for every sentence. Strict schema and `HINDSIGHT_API_FAIL_ON_EXTRACTION_ERRORS=true` improve structural/error handling, but a schema-valid empty fact list is still possible and is not an extraction error.

**Consolidation.** Native background work turns related source facts into observations. It may create a new observation, refine an existing one, or reconcile near-duplicates. Evidence and history are retained. The deployed PostgreSQL setup uses the default deduplication threshold of 0.97, with no configured observation-count cap (`-1`). A similar embedding proposes candidates; the consolidation LLM decides whether their meaning supports merging. Similarity alone is not proof that numbers, negations, or dates agree.

Consolidation is event-driven after retention and relevant source changes, not a nightly sweep of all knowledge. Both `enable_observations` and `enable_auto_consolidation` are enabled in the inspected effective personal-bank configuration. The internal worker polls queued operations every 500 milliseconds; that polling interval is not an LLM execution schedule or completion deadline. Pending consolidation requests are coalesced per bank, and later jobs process new or reset source facts. Asynchronous extraction and consolidation can still finish after the next user turn starts. A completed operation proves that processing finished, not that every derived belief is semantically correct.

**Later use.** The Hindsight API supports facts and observations, but ordinary personal Hermes recall now requests observations only. Reflect performs a more expensive evidence-seeking synthesis, potentially consulting saved mental models, observations, and underlying facts. A fact being indexed does not mean it will rank into every query; an observation being fresh does not certify that its interpretation is correct. For consequential claims, inspect the cited source and relevant date.

**Failure boundary.** The client writer queue is in memory, with bounded shutdown handling. It is not a durable exactly-once transport. The provider's readiness waits are liveness mechanisms, not an application-level proof that all evidence was preserved. In synchronous recall mode, the configured background-prefetch retain barrier is not a guarantee that the preceding turn has finished indexing. For an immediate dependent action, inspect the operation and exact target rather than relying on a saving indicator.

### Retrieval models and generative models

| Component | Deployed setting | Work performed |
|:--|:--|:--|
| Hindsight server | `ghcr.io/vectorize-io/hindsight:0.9.2`, digest pinned in Compose | Native API, MCP, memory processing and worker lifecycle |
| Database | `pgvector/pgvector:pg18`, digest pinned in Compose | Durable relational, full-text and vector-backed memory state |
| Embedder | `BAAI/bge-small-en-v1.5`, local CPU provider | Converts queries and evidence to the same English-oriented vector space |
| Reranker | `cross-encoder/ms-marco-MiniLM-L-6-v2`, local CPU provider | Scores query/candidate pairs after candidate retrieval |
| Normal recall candidate cap | `HINDSIGHT_API_RERANKER_MAX_CANDIDATES_MID=30` | Bounds reranking work for `mid` recall, not stored memory or context-token capacity |
| Retain extraction | `openai-codex`, `gpt-5.6-luna`, `high` | Extracts structured facts and their framing from retained text |
| Observation consolidation | `gpt-5.6-terra`, `high` | Refines observations and adjudicates near-duplicate reconciliation |
| Reflect and generated-page/model synthesis | `gpt-5.6-terra`, `high` | Reasons across retrieved evidence and writes the requested answer/document |

The embedder and reranker load in the long-lived Hindsight process and reuse disk caches and resident models. They are not reloaded for each ordinary Hermes turn. A separate embedding daemon was therefore unnecessary. The existing `brain-embed.service` continues to serve repository search; it is neither Hindsight's memory server nor a protocol-compatible substitute merely because it also produces embeddings.

A chat-model change does not change these memory routes. Hermes conversation compression is another auxiliary operation, separately configured in Hermes; it is not Hindsight consolidation. Fixing a compaction timeout does not repair memory retrieval, and changing a memory model does not repair conversation compression. Dedicated Codex sign-in supplies Hindsight's remote inference route. Self-hosted storage and local embeddings do not make extraction or reflection local, free of usage, or independent of provider availability.

The measured recommendation was to keep the deployed retrieval pair. Larger English embeddings and EmbeddingGemma were evaluated, but stronger model-stage scores did not establish a better complete retrieval path. MiniLM-L12 was a plausible quality-first alternative, not an automatic upgrade: the small native fixture showed a modest ranking gain and greater latency. Removing neural reranking was faster but materially worse on that fixture.

For LLM work, Luna-low extraction and Luna-high consolidation were promising alternatives; Terra-high reflection remained the recommendation. Those extraction/consolidation changes were **not deployed**, and their newly combined configuration was not tested as one complete production pipeline. The retained live settings above are the blueprint. Small, non-blinded fixtures do not establish a universal ranking, and more reasoning did not monotonically improve fidelity: schema-valid outputs could still lose a condition or reverse polarity.

### Native shared MCP

Core profiles define `mcp_servers.hindsight_shared` in `config.yaml`. Its Streamable HTTP endpoint is bank-bound at the service's `/mcp/core-shared/` route. Endpoint origin and authentication are supplied by approved local configuration; this public blueprint intentionally does not publish connection secrets or external access topology.

Hermes connects, discovers the server's tools, filters them through `tools.include`, and registers the allowed operations for the agent. The source of truth is that live discovery result plus the profile allowlist, not a copied tool count. Server-local names such as `recall` and `get_document` are stable conceptual names; the host-visible prefix should be discovered in the current runtime. In the verified conversation it was `mcp__hindsight_shared__`.

The enabled everyday families are ordinary retention/retrieval/reflection; exact source and operation inspection; deliberate raw-fact correction or invalidation; and creation, reading, updating and refresh of mental models and knowledge pages. Existing document deletion remains an explicitly authorized destructive operation. Bulk bank administration, model clearing/deletion, and recursive knowledge-tree deletion were not added to everyday use. Tool availability never supersedes approval rules.

MCP sampling is separately configurable; it is not how this Hindsight deployment obtains its normal memory LLMs. Generic resource/prompt helper tools are likewise not additional memory engines. The server's resource listing was empty during verification. Do not invent a useful resource URI from the existence of `read_resource`.

There are three distinct acceptance questions: does the server advertise an operation; does the profile allow it; and can this conversation invoke it? The previous resumed chat failed the last boundary despite a working standalone native client. The following fresh conversation successfully invoked shared retain, operation lookup, exact readback, recall, reflection and source inspection. Newly added page/model tools then passed fresh profile-specific Hermes discovery/dispatch. That does not retroactively certify a refreshed tool snapshot in every already-open Desktop conversation.

Current Hermes documents `/reload-mcp` for refreshing changed MCP configuration. The old bundled reference claiming no hot reload is stale. After an authorized refresh or new session, verify attachment with a harmless native read; a reload success message alone was insufficient in the earlier failed session. Do not build another adapter or restart unrelated services to hide an attachment problem.

### Mental models and knowledge pages

A Hindsight mental model is a saved answer to a standing question. It is not a newly installed LLM, a persona, or automatically a Buffett/Munger reasoning framework. Its record includes the question, synthesis settings, evidence scope, generated content and freshness/provenance information. Reading stored content needs no new synthesis; creating or refreshing it uses Reflect.

A knowledge page uses the same underlying mental-model engine, organized in a folder tree. It has document-oriented defaults: observations as evidence, incremental delta refresh after relevant consolidation, and exclusion of sibling pages/models from its evidence. Page search retrieves documents; ordinary recall retrieves memory units. The folder tree is stored in Hindsight, not as hand-maintained files beneath each Hermes workspace.

| Behavior | Ordinary mental model default | Knowledge page default |
|:--|:--|:--|
| Refresh after consolidation | Off for native MCP creation | On |
| Refresh style | Full regeneration | Delta update |
| Evidence emphasis | Configurable model/reflection scope | Observations |
| Sibling generated models as evidence | Depends on model configuration | Excluded |
| Organization | Saved model listing | Folders and pages |

These are defaults, not immutable guarantees for every existing object. Inspect the actual object's settings. The server's default minimum refresh interval is zero; enabling many auto-refreshing pages can create repeated LLM work. No fleet-wide schedule or filesystem projection was added during the pilot. Creating a model also does not insert its whole body into every personal prefetch.

The disposable lifecycle test covered creation, generation completion, exact content retrieval, strict scope filtering, page search, duplicate rejection, rename/move, amendment, automatic delta refresh, manual refresh, clearing/rebuilding and owned-object deletion. New evidence changed the fictional channel and budget while preserving an unchanged opening paragraph. The manual model remained unchanged until explicitly refreshed. Native Reflect returned the amended structured answer.

The most important negative result was deletion. Removing the test source removed its facts and observations from scoped recall, but generated page prose survived. It was marked stale in that run. Release documentation also warns that pure deletions may evade the freshness watermark. Affected pages therefore require inspection and deliberate correction/rebuild/retirement; neither successful source deletion nor `is_stale=false` proves the prose is clean. Delta refresh should not be assumed to remove unsupported text automatically.

All owned test documents, facts, observations, models, pages and folders were removed, and the pre-existing source document was verified unchanged. This is functional lifecycle evidence, not proof of long-term accuracy, multi-agent edit safety, or reliable concurrent updates. No permanent production page collection was created merely because the tools became available.

### Migration and retirement

The migration retained approved current, non-expiring authoritative legacy records as native Hindsight source documents, preserving original record information in metadata and verifying document readback. Existing extracted material used the native chunks strategy rather than pretending legacy vectors or graph internals could be imported unchanged. Embeddings were generated in the target space. Live conversation capture now uses concise extraction, not the migration strategy.

Imported sources are not surviving Mnemosyne databases. They are evidence now stored by Hindsight and supporting its observations. Consolidating them does not make deletion harmless: deleting a source can remove the support for derived beliefs. The import was not a lossless restoration of old graph history, persona behavior, canonical-slot semantics, expiry enforcement, or every old derived cache. Those differences were explicit scope decisions, not silently missing features.

The old Mnemosyne runtime, local stores, relay and maintenance/publishing jobs were retired with user authorization. The intermediate custom `hindsight_fleet` integration and its empty outboxes were subsequently removed in favor of the bundled provider. `/srv/hindsight/integration`, `/srv/hindsight/data/outbox`, the migration tooling, and the former backup tree are not current runtime dependencies. Existing receipts describe that history; they are not functioning rollback media. This blueprint does not assert an installed recurring backup/restore service.

The chronology matters: initial successful server canaries preceded integration repairs and cutover; a later native-only decision superseded the custom automation design; model benchmarks did not silently alter production. Restoring the early plugin because an old transcript called it finished would reintroduce precisely the ownership and maintenance complexity the final design removed.

## Implications

### How an agent should use the system

Start with the question's ownership. Use personal Hindsight for the agent's own accumulated context. Use shared MCP deliberately for approved common knowledge. Use `session_search` for what was actually said in a conversation, and repository search for authored research, procedures and governance. Do not make the presence of a memory tool a reason to bypass the authoritative source.

For a new shared contribution, retain a concise, attributable fact or decision with a useful event time and source reference. Distinguish an approved decision from a proposal, a tool observation from a model inference, and a real event from an example. Shared retention is intentional publication to the core bank, not an automatic copy of the private chat. A stable document identifier is useful when later source-level maintenance is required; inspect the current tool schema rather than inventing argument names.

After a material write, use the returned operation handle where applicable, inspect the exact source, and ask a focused retrieval question. For a genuine change in the world, add dated evidence rather than overwriting valid history. Use raw-memory correction for a bad extraction, and reversible invalidation when retirement rather than erasure is appropriate. For deletion, include affected observations and generated documents in the verification scope. A successful API response is the beginning of that check, not the conclusion.

Choose a mental model when a recurring standing question deserves a compact briefing. Choose a knowledge page when an evolving document benefits from native organization and refresh. Define the evidence scope and desired language, inspect the initial result, and understand its refresh cost before relying on automatic updates. Do not generate a second authoritative copy of the constitution or copy the entire repository into pages merely to populate an empty tree.

### Provisioning and maintenance responsibilities

A new persistent profile needs an explicitly owned bank, native provider selection, and reviewed personal capture/recall settings. For cross-session personal consolidation on the inspected adapter, provision the stable retain tag and explicit named scope above; do not copy the ineffective `"shared"` keyword from an older configuration. Re-evaluate this workaround against released Hermes support before replacing it. Core-role membership additionally justifies a bank-bound shared MCP connection and a reviewed allowlist; task-runner membership does not. Verify the effective profile home rather than using the default profile by accident. Temporary delegation needs a separate scope check, not automatic inheritance of this provisioning recipe.

Installation or reconstruction starts from official Hermes and Hindsight releases, the Compose storage mappings, the local authentication workflow, and native bank configuration. Establish durable storage and service access before attaching profiles. Then verify a personal write-to-consumer round trip and, for a core role, a deliberate shared round trip. Do not reinstate the retired custom plugin, replica stores, publisher cron, or migration directory. These are reconstruction responsibilities, not authorization to deploy from reading this document.

Operationally, service health, client activation, data migration, and model-consumer delivery remain separate claims. Inspect `compose.yaml`, profile files, exact bank overrides and runtime attachment in that order when their relationship is unclear. Use Hermes's supported configuration CLI for approved `config.yaml` changes; keep credentials local. Configuration readback should project only necessary nonsecret fields instead of dumping credential-bearing files into shared logs.

Memory quality and storage growth require separate policies. For a genuine change, retain dated new evidence and let consolidation reconcile it; correct a misextraction or invalidate a confirmed obsolete/duplicate raw fact when curation is needed. Invalidation removes a fact from active recall and consolidation but keeps a recoverable archive. Reprocessing its original document resets fact curation. Routine observation clearing is not stale-fact garbage collection: it removes derived history and re-synthesizes surviving sources, rather than deleting historical evidence.

The inspected native revision caps retain at most 50 history entries per observation and per mental model; LLM traces expire after one day. Terminal-operation retention remains `HINDSIGHT_API_OPERATION_RETENTION_DAYS=0` (indefinite); a positive retention window is available but was not changed by the recall-policy revision. These controls do not bound total source storage. Continued ingestion can grow the database even with clean recall, so retention decisions should distinguish useful evidence, audit history, operational records, and inactive migration stores rather than deleting knowledge merely because it is old.

Do not change the embedder merely by changing its model name. A different vector space requires supported re-embedding/migration and validation even if dimensionality happens to match. Reranker and LLM changes also need a task-relevant, bounded comparison, not a permanent benchmarking loop. Preserve the distinction between proposed recommendations and deployed settings in every handoff.

### Operational verification contract

Apply the following before claiming the corresponding capability ready. PASS requires the evidence named in the row; failure or missing evidence HALTs that claim, not unrelated working features. The acceptance scope is the target profile/bank/object, and any write test requires prior authorization and an owned, removable fixture.

| Claim | Verification and PASS condition | HALT condition |
|:--|:--|:--|
| Correct personal destination | Effective profile and bank agree with ownership policy; native request targets that bank | Inferred bank, wrong profile, or an unresolved template override |
| Automatic capture works | A completed real host turn reaches exact source readback and intended facts | Only a saving indicator, queue acceptance, or document storage without useful evidence |
| Recall reaches the model | Focused query retrieves the evidence and the actual model request contains it | Only a standalone helper succeeds or the question already supplies the answer |
| Observation-only recall configured | Each enrolled profile's native filter is `observation`; fresh native requests and returned types agree, other settings stay unchanged | Any broad raw-fact filter remains, or fresh-process verification is claimed as an existing chat's reload |
| Cross-session observation scope works | Configured scope survives native normalization and the retain request; source lineage is preserved, stored observations use the intended stable scope, and a cross-session fixture has evidence from both sessions | Config readback alone, omitted request scope, session-fragmented observations, or a new scope claimed to have migrated historical data |
| Shared MCP works here | Current conversation invokes a bank-bound native read successfully | Server health or another process's success substituted for attachment |
| Mutation is complete | Exact target and relevant derivatives match the intended result; unrelated source preserved | Success response without readback, incomplete cleanup, or unsupported surviving prose |
| Artifact publication is complete | Required workspace commit verified; shared artifact committed, naturally mirrored and indexed | Correct local text mistaken for the user's published result |

This contract is embodied operationally in the active memory-provider skill and the existing workspace File Operations and session-end gates. It does not add another runtime daemon. The current task strengthened the documentation-completion check after a repeated omission: verified workspace edits had been left uncommitted despite the workspace requirement. Commit authority and path scope must be resolved explicitly, not silently replaced by a generic coding default.

### What remains outside the demonstrated result

Long-term semantic drift, recovery from a host/storage loss, concurrent page editing, and a fleet-wide Desktop acceptance sweep were not established by the lifecycle pilot. Neither was a scheduled refresh or filesystem-mount workflow. The underlying Hermes notification-profile bug was contained in the affected prior session, not patched upstream by this work. Its repeated notices and the separate conversation-compaction failures were host-lifecycle problems, not reasons to reinstall Hindsight.

The next useful improvement should respond to a demonstrated failure or a concrete new use case. Fresh recall can still be slow; imported metadata can make responses large; English-only intent did not prevent some Spanish extraction in the pilot. These are recorded limitations, not permission for automatic model changes, source deletion, or quota-monitoring jobs.

## Counter-evidence

The architectural claim would weaken if deliberate shared lookup consistently failed to surface knowledge that core agents needed, and a supported, simpler multi-bank native path measurably improved grounded outcomes without privacy or latency regressions. In that case, automatic shared retrieval could be reconsidered. The current finding is narrower: the bundled personal provider selects one bank, while native MCP provides an explicit shared surface. It does not prove that manual choice is optimal for every future workload.

A second falsifier would be persistent loss of important turns attributable to the in-memory client writer under ordinary operation. Native ownership removes custom maintenance, but does not erase its durability limits. A bounded test of restart/failure behavior with approved synthetic evidence could establish whether the actual workload needs a durable capture mechanism. Until such a requirement is demonstrated and approved, a hypothetical stronger queue is not a reason to resurrect the retired plugin.

A third challenge concerns semantic quality. The measured baseline may lose to another supported configuration on representative new material, especially numeric constraints, negation, long questions, or changing decisions. A held-out comparison must keep source evidence and scoring criteria fixed, distinguish model-stage measurements from complete Hindsight behavior, and score unsupported assertions as well as retrieved keywords. Reusing tuned fixture questions does not create an untouched holdout. The existing small comparison supports restraint, not a universal best-model claim.

The observation-only check supplied a concrete limit: a shared-publication question ranked the current private-only automatic policy first, while a summarization-policy question still ranked a superseded observation above its correction. Consolidated does not mean currently valid. The later scope audit found a concrete mechanical contributor: the native adapter had discarded the intended cross-session scope. The named-scope workaround repairs future request shaping and passed a cross-session evidence check, but that does not attribute every semantic error to this defect or clean existing session/migration-scoped observations. Those still require evidence-led source review and separately approved reconciliation; neither change demonstrates that all outdated context disappeared.

Knowledge pages already supply concrete counter-evidence to an overbroad claim that derived documents always maintain themselves correctly: prose survived deletion of supporting evidence. If an upgraded implementation demonstrably handles source removal and concurrent edits better, its verified contract can replace this limitation. Conversely, a page that repeatedly loses qualifications or manufactures certainty would justify manual review or retiring that page, not promoting it to canonical governance because it is automatically refreshed.

Finally, centralized storage changes the failure and confidentiality boundary. Service unavailability, credential compromise, or database loss can affect multiple logical banks. Bank names and client allowlists are not independent security barriers. The system would need a different isolation design for untrusted tenants or stricter confidentiality requirements. Backups and recovery must be designed and exercised separately; removal of obsolete migration backups is not evidence of disaster recovery.

The cheapest ongoing falsification is a focused, authorized check at the boundary being claimed: write one meaningful fact, verify the correct destination, ask a question that does not contain its answer, inspect delivered context, amend the fact, and inspect affected derivatives. Stop once that acceptance question is answered. The result should either support the existing design, identify one concrete repair, or explicitly leave a gap unresolved. More test volume alone is not stronger evidence.

## Sources and Cross-Links

- `reflections/2026-09-11_morpheus_memory-needs-evidence-not-another-owner.md` -- originating consolidated reflection, `20260911T135041Z`; chronology, learning and verification limits.
- `reflections/2026-08-10_link_shared-memory-is-an-operations-problem.md` -- prior operational insight, `20260810T112711Z`.
- `research/insights/mnemosyne-system.md` -- historical fleet anatomy; superseded for migrated VPS profiles, not evidence of other machines' current state.
- `research/insights/two-tier-fleet-memory-single-vector-space.md` -- historical private/shared and vector-space rationale; the relay mechanics are not current VPS practice.
- `governance/system-blueprint.md` -- repository and fleet authority; memory storage does not replace it.
- `governance/system-primedirectives.md` -- truth, scope, simplicity, and verification obligations.
- [Installed-version Hermes provider source](https://github.com/NousResearch/hermes-agent/blob/0b8daf30aae1d0b129ede9b857cac2158eb50324/plugins/memory/hindsight/__init__.py) -- bank resolution, capture, prefetch, tools and lifecycle.
- [Installed-version Hermes Hindsight reference](https://github.com/NousResearch/hermes-agent/blob/0b8daf30aae1d0b129ede9b857cac2158eb50324/plugins/memory/hindsight/README.md) -- observation-only default for both automatic and explicit personal recall.
- [Hermes memory-provider documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers) -- provider selection and host integration; interpret broad prose against the inspected implementation.
- [Hermes native MCP documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) -- discovery, filtering, reload and sampling.
- [Hindsight v0.9.2 configuration](https://github.com/vectorize-io/hindsight/blob/v0.9.2/hindsight-api-slim/hindsight_api/config.py) -- operation-specific settings and defaults; live bank overrides remain authoritative.
- [Hindsight v0.9.2 observations](https://raw.githubusercontent.com/vectorize-io/hindsight/v0.9.2/hindsight-docs/docs/developer/observations.mdx) -- consolidation, scopes, source lifecycle and reconciliation.
- [Hindsight v0.9.2 retain scopes](https://raw.githubusercontent.com/vectorize-io/hindsight/v0.9.2/hindsight-docs/docs/developer/api/retain.mdx) -- named custom scopes, `shared`, and the distinction between `[[]]` and `[]`.
- [Merged Hindsight scope implementation #2202](https://github.com/vectorize-io/hindsight/pull/2202) -- supported request-level solution; explicitly no new global environment flag.
- [Hermes scope defect #74933](https://github.com/NousResearch/hermes-agent/issues/74933) -- exact failure and documented stable-tag/custom-scope configuration workaround.
- [Hermes proposed keyword fix #72565](https://github.com/NousResearch/hermes-agent/pull/72565) -- unmerged as checked on 2026-09-12; not applied locally. This is proposed upstream code, not a released recommendation.
- [Hindsight v0.9.2 memory curation](https://raw.githubusercontent.com/vectorize-io/hindsight/v0.9.2/hindsight-docs/docs/developer/api/memories.mdx) -- correction, reversible invalidation and document-reprocessing caveat.
- [Hindsight v0.9.2 operations](https://raw.githubusercontent.com/vectorize-io/hindsight/v0.9.2/hindsight-docs/docs/developer/api/operations.mdx) -- optional terminal-operation retention, separate from source-memory retention.
- [Hindsight v0.9.2 mental-model API](https://raw.githubusercontent.com/vectorize-io/hindsight/v0.9.2/hindsight-docs/docs/developer/api/mental-models.mdx) -- saved synthesis, freshness and refresh semantics.
- [Hindsight v0.9.2 knowledge pages](https://raw.githubusercontent.com/vectorize-io/hindsight/v0.9.2/hindsight-docs/docs/developer/knowledge-pages.mdx) -- organization and document-oriented defaults.
- [Hindsight v0.9.2 knowledge-page API](https://raw.githubusercontent.com/vectorize-io/hindsight/v0.9.2/hindsight-docs/docs/developer/api/knowledge-pages.mdx) -- API-level defaults and object operations.
- [Hindsight v0.9.2 MCP implementation](https://github.com/vectorize-io/hindsight/blob/v0.9.2/hindsight-api-slim/hindsight_api/mcp_tools.py) -- actual tool contracts, distinct from a client's allowlist.

Local verification receipts are named in the persistence map so an authorized operator can locate the deployment history. Temporary pilot files are not runtime dependencies. This blueprint deliberately contains no private memory contents, credential values, public connection endpoints, or agent inventory totals.
