---
name: agent-memory-and-persistence
id: 20260727T114838Z
tier: library-topic
domain: coding-agentic-ai
author: Researcher-1
tags: [agent-memory, memory-hierarchy, episodic-memory, semantic-memory, procedural-memory, memory-consolidation, rag, vector-stores, context-persistence]
links: [library/coding-agentic-ai/context-window-management.md, library/coding-agentic-ai/agent-skill-systems.md, library/coding-agentic-ai/multi-agent-orchestration.md]
reviewed: 2026-09-21
---

# Agent Memory and Persistence -- Persistent Agents Need Lifecycle Design, Not Just Longer Context

Agent memory is the engineered state that lets an agent recover and revise useful information across turns, sessions, and process restarts. A longer model context can hold more working material for one inference, but persistence requires an explicit lifecycle for retention, representation, retrieval, evidence use, updating, deletion, scope, and evaluation ([1] [5] [6] [9]).

## Background

A language model call is not by itself a persistent agent. The model receives an input context and produces an output; information from an earlier call is available later only if the surrounding application supplies it again or the information has been incorporated into model parameters. CoALA therefore distinguishes the language model from the language agent around it: the agent can maintain a working-memory data structure across calls, read from long-term stores, write new information, and act in an environment. This boundary matters because context capacity, application state, and durable memory solve different problems ([1]).

The earliest conversational pattern was to replay prior messages. A bounded replay window preserves recent wording and requires little additional machinery, but older turns eventually fall outside the prompt. Recursive summaries reduce prompt length, yet compression can omit details that a later question needs. The underlying trade-off is recoverability: a short summary is inexpensive to inject, while a raw transcript preserves evidence but becomes expensive and difficult to search as it grows. MemGPT formalized this trade-off with an operating-system analogy. Its main context contains system instructions, editable working context, and a rolling message queue; external context contains recall and archival storage that the agent accesses through functions ([4]).

Retrieval-augmented generation predates the recent agent-memory systems. Lewis et al. introduced RAG in 2020 as a combination of parametric memory and a retrievable, non-parametric Wikipedia index. Their model retrieved passages and conditioned generation on them, making the external text inspectable and replaceable. That work established retrieval as a practical way to decouple stored knowledge from model parameters, but its corpus was an externally prepared knowledge source rather than an evolving record written by an agent during interaction ([2]).

Agent memory added a write path and a time dimension to retrieval. Generative Agents stored a natural-language stream of experiences, ranked memories by relevance, recency, and importance, generated higher-level reflections, and used both memories and reflections in planning. MemGPT let the model call functions to edit working context and search external storage. CoALA then supplied a broader conceptual vocabulary: working memory plus episodic, semantic, and procedural long-term memory, connected by retrieval, reasoning, learning, and external action. These systems did not establish one mandatory implementation, but they clarified that memory includes decisions about what to write and how to use it, not merely a vector search over transcripts ([1] [3] [4]).

Long-context research also weakened the premise that capacity alone solves persistence. In controlled multi-document question answering and key-value retrieval, Liu et al. found that several models used information less reliably when it appeared in the middle of a long prompt than when it appeared near the beginning or end. Their open-domain question-answering case study also found that reader accuracy saturated before retriever recall: adding more documents increased input size faster than answer quality. These experiments concerned particular 2023-era models and should not be universalized to every later model, but they demonstrate why advertised context length is not equivalent to dependable recall ([5]).

Evaluation subsequently moved from isolated retrieval toward sustained interaction. LongMemEval contains 500 questions testing information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention. Its standard histories include an approximately 115,000-token setting and a 500-session setting of roughly 1.5 million tokens. This design makes timestamp handling, contradictions, missing information, and cross-session synthesis visible as separate failure modes instead of collapsing memory into a single nearest-neighbor score ([6]).

By 2025-2026, research systems increasingly treated memory as a managed lifecycle. Zep represented raw episodes, entities, relationships, communities, and validity intervals in a temporal knowledge graph. Mem0 extracted candidate facts and compared them with similar stored memories before choosing ADD, UPDATE, DELETE, or NOOP. Oracle Agent Memory separated an active layer for extraction, summarization, and search orchestration from a passive store for scoped persistence and retrieval. These are alternative designs rather than evidence of a settled production consensus. Their common contribution is to make selection, revision, temporal state, provenance, and scope explicit engineering concerns ([7] [8] [9]).

## Core Concepts

### Context, working state, and durable memory are different layers

A context window is the set of tokens available to one model inference. It may contain instructions, recent messages, retrieved records, tool results, and temporary reasoning artifacts. Working memory is the agent-side state used to assemble that context and carry active goals or variables between calls. CoALA explicitly defines working memory more broadly than the model prompt: it is a data structure that can persist across calls, while each prompt is synthesized from a subset of it. Durable memory is state intended to remain available beyond the active thread or process lifetime ([1]).

Conflating these layers creates two common design errors. First, replaying a transcript is called persistence even though nothing has been selected, revised, or made searchable. Second, a database is called memory even though no policy determines which records should influence the next action. A useful architecture specifies movement between layers: events enter as raw records, selected records become durable artifacts, retrieval moves a bounded subset into working state, and prompt construction exposes only the subset needed for the current inference. This paragraph is an architectural synthesis of the lifecycle described by CoALA, MemGPT, LongMemEval, and Oracle Agent Memory ([1] [4] [6] [9]).

### The cognitive taxonomy is a design lens, not a storage mandate

CoALA organizes long-term memory into episodic, semantic, and procedural forms. Episodic memory records experiences from earlier decision cycles, such as conversations, tool outcomes, or task trajectories. Semantic memory stores knowledge about the world or the agent. Procedural memory includes implicit knowledge in model parameters and explicit procedures in agent code. Working memory holds current observations, active goals, retrieved knowledge, and intermediate state. The categories describe the role information plays; they do not require four databases or prescribe a particular vendor ([1]).

An individual record may move between categories. A failed deployment attempt begins as an episode containing commands, outputs, and timestamps. A consolidation process may derive a semantic fact such as a service dependency, and repeated outcomes may justify a procedural rule such as running a schema check before deployment. Preserving links back to the episode makes the derived fact or rule auditable. The transformation is lossy by design, so the raw record should not be discarded merely because a compact abstraction exists. Zep's episode-to-entity structure and Oracle's distinction among raw messages, summaries, facts, and procedural memory illustrate this need for both evidence and derived artifacts ([7] [9]).

### Memory is a lifecycle with separate failure points

A complete memory path contains at least six functions. Retention captures messages, documents, tool traces, and outcomes. Extraction converts selected input into candidate facts, events, preferences, or procedures. Consolidation compares candidates with existing state and may merge, update, invalidate, or reject them. Retrieval selects evidence for a query under a token and latency budget. Reading or reasoning uses the evidence to answer or act. Revision and removal correct stale state, honor deletion requirements, or retire records that should no longer influence behavior. LongMemEval describes indexing, retrieval, and reading as distinct stages; Oracle extends the operational view across ingestion, extraction, consolidation, summarization, revision, and removal ([6] [9]).

Separating the stages makes failures diagnosable. If a correct fact was never extracted, tuning the retriever cannot recover it. If retrieval returned the right evidence but the model ignored a timestamp, the defect is in reading or reasoning. If an old preference remains retrievable after a correction, the defect may be consolidation, temporal representation, ranking, or update policy. End-to-end answer accuracy alone cannot identify which component failed. Oracle therefore recommends measuring evidence retrieval, evidence use, final outcome, and operational efficiency separately ([9]).

Write policy is the first consequential gate. Persisting every utterance as a fact creates noise, duplicates, and privacy exposure; extracting too little produces repeated clarification and cold starts. Mem0 addresses this with an LLM extraction stage followed by comparison against semantically similar memories and a choice among ADD, UPDATE, DELETE, and NOOP. This makes the policy concrete but does not eliminate model error: extraction and update decisions can still be wrong. Systems should therefore retain provenance and make destructive operations reviewable or reversible where the risk warrants it ([8]).

### Retrieval requires more than semantic similarity

Vector similarity is useful when the query and memory express related meaning in different words, but it does not by itself encode chronology, exact identifiers, negation, validity, or graph relationships. Generative Agents combined relevance, recency, and importance. Zep combined cosine similarity, BM25 full-text search, and graph traversal before reranking. LongMemEval found that expanding an index key with extracted user facts improved average recall@k by 9.4 percent and downstream accuracy by 5.4 percent in its reported configurations; time-aware indexing and query expansion improved temporal-reasoning recall by 6.8 to 11.3 percent when the stronger tested model generated the time range ([3] [6] [7]).

A production retrieval plan should therefore match the questions the agent must answer. Exact names, error codes, and file paths benefit from lexical retrieval. Paraphrased preferences benefit from dense retrieval. Questions such as "what changed after the migration?" require event time and ordering. Questions connecting a user, project, and prior decision may benefit from entity links or graph traversal. Reciprocal rank fusion or a learned reranker can combine channels, but every additional channel adds latency and new failure modes. The appropriate design is empirical: measure recall, precision, downstream use, and cost on representative tasks ([6] [7] [9]).

Retrieval granularity is equally important. Whole sessions preserve context but can bury the relevant turn. Isolated facts are easy to rank but may remove qualifications needed for correct reasoning. In LongMemEval, decomposing sessions into rounds improved question-answering performance in the reported setup, while compressing values into facts could harm overall performance through information loss even though fact representations helped some multi-session questions. The safer pattern is layered retrieval: use compact keys or summaries to locate candidates, then make source passages available when detail or provenance matters ([6]).

### Time, contradiction, and provenance must be represented explicitly

A memory that says "the user works in Berlin" is incomplete if the statement was true only during an earlier period. Creation time records when the system stored a record; event time records when the underlying event occurred; valid time records the interval during which a fact held. These timestamps are not interchangeable. Zep uses a bi-temporal model and attaches valid and invalid times to relationship edges while also retaining transaction history. When new information conflicts with an existing relationship, it can invalidate the earlier edge without erasing the historical record ([7]).

Contradiction is not always error. "The user lives in Paris" after "the user lives in Berlin" may be a legitimate change, while two different birth dates may indicate extraction error or unresolved evidence. A consolidation policy needs rules for temporal succession, mutually exclusive facts, confidence, and source priority. It should preserve enough provenance to answer both "where does the user live now?" and "where did the user live before?" Deleting the old statement would answer the first question but destroy the second. LongMemEval's separate knowledge-update and temporal-reasoning categories expose this distinction ([6] [7]).

Provenance also constrains trust. Derived summaries and semantic facts should link to raw messages, documents, or tool results. Without that link, an agent cannot quote the source, explain why it believes a fact, or distinguish an extraction error from a user correction. Zep connects semantic artifacts to source episodes; Oracle emphasizes attributable, scoped records and raw evidence alongside compact summaries. The design implication is that compression should add an index or abstraction, not silently replace the only recoverable evidence ([7] [9]).

### Control, scope, and deletion are part of memory semantics

Memory can be managed by the agent, by a deterministic pipeline, or by a hybrid. MemGPT gives the model functions to edit working context and search external storage, which makes memory management responsive to the current reasoning process but consumes model calls and depends on correct tool use. Mem0 places extraction and update logic in a surrounding pipeline, reducing the need for explicit agent-initiated housekeeping but making pipeline policy decisive. Neither control model is inherently superior; the risk depends on whether missed writes, mistaken edits, or additional latency are more costly for the application ([4] [8]).

Scope determines who can retrieve a memory and under which task. A record may belong to one thread, one user across threads, one agent, one team, or an organization. Oracle's architecture exposes thread, user, and agent scope in its storage and search model, while warning that retrieval filters are not substitutes for database authorization. The same principle applies to shared coding agents: filesystem visibility or a common vector index does not itself establish permission to read every record ([9]).

Deletion is not merely a ranking choice. A record that must be removed for user control, policy, or legal compliance should not remain recoverable through a raw transcript, vector index, graph edge, summary, backup, or cache. Conversely, low ranking is often preferable to irreversible deletion when the issue is relevance rather than authorization. The author's synthesis is that memory APIs need separate operations for suppression, invalidation, archival, and erasure because those actions have different evidentiary and governance consequences ([7] [9]).

## Evidence

The 2020 RAG study provides a baseline for understanding external memory. It paired a BART generator with a dense Wikipedia index and a DPR retriever, then evaluated open-domain question answering, abstractive question answering, Jeopardy question generation, and fact verification. The authors reported state-of-the-art results on three open-domain question-answering tasks in their comparison and showed that swapping a 2016 Wikipedia index for a 2018 index changed answers to questions about officeholders without retraining the generator. This demonstrated that non-parametric memory can be inspectable and replaceable, but the experiment did not test online consolidation of an agent's own experiences ([2]).

Generative Agents tested whether observation, retrieval, reflection, and planning affected behavior in a 25-agent sandbox. The memory stream stored natural-language observations and retrieved them using relevance, recency, and importance. In a controlled interview study with 100 evaluators, the full architecture received a TrueSkill mean of 29.89, compared with 26.88 after removing reflection, 25.64 after removing both reflection and planning, and 21.21 after removing observation, reflection, and planning. The study therefore supplies ablation evidence that memory structure and reflection contributed to judged believability in that simulation. It does not establish general task accuracy, and the authors reported retrieval failures, embellished memories, high token cost, and only a two-day simulation as limitations ([3]).

MemGPT evaluated agent-controlled paging on multi-session conversation and document-analysis tasks. In its Deep Memory Retrieval task, the fixed-context GPT-4 baseline achieved 32.1 percent accuracy and GPT-4 with MemGPT achieved 92.5 percent; GPT-4 Turbo rose from 35.3 to 93.4 percent. The baseline received a lossy summary of five prior sessions, whereas MemGPT could search the full history, so the result supports hierarchical retrieval over that summary baseline rather than a universal claim that agent-controlled memory beats every pipeline. Its nested key-value experiment further showed that MemGPT with GPT-4 continued multi-hop lookups at depths where the tested fixed-context models fell to zero, while weaker tool-calling models also degraded ([4]).

The Lost in the Middle study isolated a different constraint: evidence use after information is already in the prompt. It used 2,655 NaturalQuestions-Open queries for multi-document question answering and controlled both document count and the answer passage's position. Performance commonly followed a U-shaped curve, with higher accuracy near the beginning or end and lower accuracy in the middle. In one setting GPT-3.5-Turbo fell more than 20 percentage points, and adding documents beyond 20 improved open-domain reader accuracy by only about 1 to 1.5 percentage points for the tested GPT-3.5-Turbo and Claude-1.3 models. The finding justifies testing evidence position and distractor load; it does not prove that every contemporary long-context model has the same curve ([5]).

LongMemEval evaluates the full indexing-retrieval-reading chain with 500 manually curated questions. The benchmark's five abilities are information extraction, multi-session reasoning, knowledge updates, temporal reasoning, and abstention. In the approximately 115,000-token setting, the tested long-context models lost roughly 30 to 60 percent relative performance against an oracle-evidence condition. The paper's optimization experiments found that fact-expanded keys improved average recall@k by 9.4 percent and answer accuracy by 5.4 percent, time-aware query expansion improved temporal recall by 6.8 to 11.3 percent, and a structured Chain-of-Note reading strategy improved oracle-retrieval answer accuracy by as much as 10 absolute points. These results show that indexing, retrieval, and reading can each limit performance even when storage capacity is adequate ([6]).

Zep tested a temporal graph design on Deep Memory Retrieval and LongMemEval. On LongMemEval's 115,000-token setting, its reported GPT-4o configuration scored 71.2 percent versus 60.2 percent for full-context GPT-4o while using an average 1,600 context tokens instead of 115,000; reported latency was 2.58 seconds versus 28.9 seconds. The category results are more informative than the aggregate: Zep improved multi-session, temporal, knowledge-update, preference, and user-fact questions, but fell from 94.6 to 80.4 percent on single-session assistant facts. The study was produced by Zep and did not hold every component constant across all external systems, so its results are evidence for the evaluated configuration, not a vendor-independent ranking ([7]).

Mem0 evaluated extracted natural-language memories and a graph-enhanced variant on LoCoMo. Its update pipeline explicitly compared each new candidate with related memories before ADD, UPDATE, DELETE, or NOOP. The paper reported an overall LLM-judge score of 67.13 for Mem0 and 68.44 for the graph variant; full context scored about 73 but had a p95 response latency of 17.117 seconds, compared with 1.440 seconds for Mem0 and 2.590 seconds for the graph variant. The graph variant helped temporal questions but did not improve every category. Because the authors built the system and used an LLM judge, the result should be read as a measured quality-latency trade-off under their setup, not as proof that graph memory is categorically better ([8]).

Oracle Agent Memory adds an enterprise-oriented evaluation and useful cautions about comparability. Its reported high-accuracy LongMemEval configuration answered 469 of 500 questions correctly, with multi-session reasoning the lowest category at 88.0 percent. On the stricter order-sensitive BEAM scoring convention, it scored 0.630 at one million tokens and 0.510 at ten million; event ordering, multi-session reasoning, summarization, and temporal reasoning remained difficult at the larger scale. The report explicitly warns that model, embedding, top-k, prompt, judge, dataset, and scoring choices must be held constant before scores from different systems are treated as directly comparable ([9]).

Taken together, the evidence supports a bounded conclusion. External storage, structured extraction, hybrid retrieval, temporal metadata, and explicit reading strategies can outperform replay or summary baselines on particular long-horizon tasks. The studies do not establish that one taxonomy, database, graph, or control model is universally optimal. They also show that retrieval success can coexist with reasoning failure, that compression can improve cost while losing rare evidence, and that better aggregate accuracy may conceal weaker performance on a specific memory ability ([3] [5] [6] [7] [8] [9]).

## Implications

For agent builders, the first implication is to specify memory requirements before choosing a framework. List the decisions that must survive a turn, a thread, a restart, and a user session. Classify the required artifacts as raw episodes, durable facts, relationships, preferences, procedures, or active task state. Then define retention duration, ownership, update semantics, provenance, and deletion behavior for each class. This prevents a vector database from becoming an undifferentiated sink and aligns storage with the episodic, semantic, procedural, and working roles described by CoALA ([1]).

The second implication is to design backward from failure. The worst memory failure in a low-risk assistant may be an annoying repeated question; in deployment tooling it may be replaying an obsolete command; in a multi-user system it may be retrieving one user's private record for another. The controls should follow the severity: scoped identifiers and authorization, source links, confidence or validity state, reversible invalidation, confirmation before destructive procedural changes, and complete erasure paths for data that must be deleted. Oracle's warning that scope filters are not authorization boundaries is especially important: memory relevance and access control are separate checks ([9]).

For retrieval design, semantic search should be a baseline rather than the whole system. Build a representative test set containing paraphrases, exact identifiers, recent corrections, temporal questions, cross-session joins, and unanswerable queries. Compare lexical, dense, temporal, graph, and fused retrieval under a fixed token budget. Measure whether the evidence was retrieved and whether the downstream model used it correctly. LongMemEval and Zep show why this decomposition matters: time-aware and graph-aware methods can improve difficult categories while hurting another category, and correct retrieval does not guarantee correct reading ([6] [7]).

For consolidation, retain the evidence chain. A compact fact such as "the project uses PostgreSQL" should carry its source, observation time, applicable scope, and current validity. When a later statement changes the database choice, the system should distinguish an update from an extraction conflict and should preserve history when historical questions matter. Summaries can accelerate routine prompt assembly, but raw episodes should remain available under the applicable retention policy. The author's synthesis is to treat summaries, facts, graphs, and procedures as indexes over evidence rather than unquestionable replacements for it ([6] [7] [9]).

For coding agents, memory classes map to concrete artifacts. A checkpoint or thread state records the current task. Tool transcripts and test results are episodic evidence. Repository facts, user preferences, and architectural decisions are semantic memory. Versioned instructions, skills, and runbooks are procedural memory. This mapping does not mean every artifact should enter every prompt. Retrieval should be task-scoped, and procedural artifacts should be versioned and reviewed because an incorrect instruction can alter future actions rather than merely misstate a fact. CoALA explicitly notes that writes to procedural memory are riskier than writes to episodic or semantic memory because they can introduce bugs or subvert intended behavior ([1]).

For multi-agent systems, sharing storage is not the same as sharing memory safely. Records need an owner, audience, provenance, and conflict policy. One agent's inference should not silently become another agent's fact without an evidence link and an authorized promotion step. Shared procedural memory deserves stronger controls because it can change the behavior of every consuming agent. A reversible publication workflow, immutable history, and scoped retrieval reduce the risk that one mistaken consolidation contaminates the fleet. This is an architectural synthesis based on CoALA's distinction among memory types and Oracle's explicit scope model ([1] [9]).

Evaluation should cover four layers. First, test retention and extraction: was the needed evidence stored in a recoverable form? Second, test retrieval: was the correct record returned within the budget, with appropriate precision and temporal ordering? Third, test evidence use: did the model obey corrections, combine records, and abstain when evidence was absent? Fourth, test operations: latency, token use, ingestion delay, storage growth, deletion completeness, and authorization behavior. Aggregate answer accuracy remains necessary, but Oracle's analysis and LongMemEval's staged model show why it is insufficient for diagnosis ([6] [9]).

Benchmark claims also need disciplined comparison. A score depends on the dataset version, memory ingestion method, model, embeddings, candidate count, reranker, prompt, judge, and scoring convention. Self-reported vendor experiments are useful primary evidence about a configuration, but cross-paper leaderboards can mislead when those variables differ. Report both the configuration and category-level results, disclose whether external baselines were reproduced, and separate estimated tokens from billed cost. Zep, Mem0, and Oracle each publish informative measurements while also illustrating how architectures and evaluation setups differ ([7] [8] [9]).

Cost is a systems outcome, not simply a prompt-token count. Retrieval and consolidation add embedding, model-call, index, and storage costs; full-history prompting adds repeated input and latency; summaries can reduce tokens but disrupt provider cache locality or omit rare evidence. Oracle notes that regenerated memory near the front of a prompt may reduce exact-prefix cache hits even while shortening the prompt. The correct operating point therefore minimizes effective cost and latency subject to accuracy, recoverability, and policy constraints, rather than maximizing either context length or compression ([9]).

Finally, persistent memory changes the trust relationship with users. A system that remembers preferences can reduce repetition and improve continuity, but the same persistence can retain sensitive data, propagate extraction errors, and produce unwarranted confidence from stale records. Users need visibility into what is stored, correction mechanisms, and meaningful deletion controls. Developers need audit trails that distinguish raw statements from derived conclusions. The central engineering principle is therefore not "remember more." It is to preserve the right evidence, derive cautiously, retrieve selectively, update explicitly, and forget completely when required ([7] [8] [9]).

## Sources

1. Sumers, T. R., Yao, S., Narasimhan, K., & Griffiths, T. L. (2024).
   "Cognitive Architectures for Language Agents." Transactions on
   Machine Learning Research. https://arxiv.org/abs/2309.02427 [high]

2. Lewis, P., Perez, E., Piktus, A., et al. (2020).
   "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks."
   Advances in Neural Information Processing Systems 33.
   https://arxiv.org/abs/2005.11401 [high]

3. Park, J. S., O'Brien, J. C., Cai, C. J., et al. (2023).
   "Generative Agents: Interactive Simulacra of Human Behavior." UIST 2023.
   https://doi.org/10.1145/3586183.3606763 [high]

4. Packer, C., Fang, V., Patil, S. G., Lin, K., Wooders, S.,
   Stoica, I., & Gonzalez, J. E. (2024). "MemGPT: Towards LLMs as
   Operating Systems." https://arxiv.org/abs/2310.08560 [high]

5. Liu, N. F., Lin, K., Hewitt, J., et al. (2024). "Lost in the Middle:
   How Language Models Use Long Contexts." Transactions of the Association
   for Computational Linguistics, 12, 157-173.
   https://doi.org/10.1162/tacl_a_00638 [high]

6. Wu, D., Wang, H., Yu, W., Zhang, Y., Chang, K.-W., & Yu, D. (2025).
   "LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive
   Memory." ICLR 2025. https://arxiv.org/abs/2410.10813 [high]

7. Rasmussen, P., Paliychuk, P., Beauvais, T., Ryan, J., & Chalef, D.
   (2025). "Zep: A Temporal Knowledge Graph Architecture for Agent
   Memory." https://arxiv.org/abs/2501.13956 [high]

8. Chhikara, P., Khant, D., Aryan, S., Singh, T., & Yadav, D. (2025).
   "Mem0: Building Production-Ready AI Agents with Scalable Long-Term
   Memory." https://arxiv.org/abs/2504.19413 [high]

9. Alake, R., Bernardis, C., Cayet, P., et al. (2026). "Oracle Agent
   Memory as an Enterprise Memory Substrate for Long-Horizon AI Agents."
   https://arxiv.org/abs/2607.13157 [high]

## See Also

- `library/coding-agentic-ai/context-window-management.md` -- management
  of the working context into which retrieved memories are placed.
- `library/coding-agentic-ai/agent-skill-systems.md` -- versioned skills
  as a practical form of procedural memory for coding agents.
- `library/coding-agentic-ai/multi-agent-orchestration.md` -- scope,
  provenance, and coordination when several agents consume shared state.
