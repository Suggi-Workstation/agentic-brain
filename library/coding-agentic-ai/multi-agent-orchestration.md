---
name: multi-agent-orchestration
id: 20260724T182200Z
tier: library-topic
domain: coding-agentic-ai
author: Ava
tags: [multi-agent, orchestration, agent-architecture, coordination, langgraph, crewai, agent-patterns, orchestrator-workers, multi-agent-debate, failure-modes]
links: [library/coding-agentic-ai/anchor-coding-agentic-ai.md, library/coding-agentic-ai/context-window-management.md, library/coding-agentic-ai/agent-planning-and-task-decomposition.md, library/coding-agentic-ai/agent-cost-latency-and-resource-governance.md, library/coding-agentic-ai/agent-uncertainty-verification-and-abstention.md, research/insights/council-of-five.md]
reviewed: 2026-10-08
---

# Multi-Agent Orchestration -- More Agents Help Only When the Task Splits Cleanly and the Work Is Verified

Multi-agent orchestration is the engineering discipline of deciding how
several language-model agents divide a task, pass work and context between
them, and check each other's results. Current evidence shows that adding
agents is not a general upgrade: coordination helps on tasks that
decompose into separable parts and hurts on tightly sequential ones [16],
and many failures come from system design and missing verification rather
than from weak individual agents [15]. The practical rule that follows is
to start with a single agent and add orchestration only where a specific
failure of that agent justifies it [10][11][14].

## Background

The problem of coordinating several problem solvers is older than large
language models. The Hearsay-II speech-understanding system, described by
Erman and colleagues in 1980, integrated diverse knowledge sources to
resolve uncertainty in spoken input [1]. It is a classic early example of
the blackboard architecture, in which specialist knowledge sources
iteratively update a shared knowledge base, the blackboard, and each
contributes a partial solution when its conditions match the current state
[2]. In 1980 Reid G. Smith published the Contract Net Protocol, a
task-sharing protocol for distributed problem solving [3]. In it a manager
announces a task with a call for proposals, contractors answer with a bid
or a refusal, and the manager awards the task to the best proposal and
rejects the rest [4]. In the author's reading, these two designs
anticipate the coordination ideas that recur in modern systems: shared
state that every participant reads and writes, and explicit delegation
from a manager to contractors. By the mid-1990s Wooldridge and Jennings
could organize the field of intelligent agents into agent theory, agent
architectures and agent languages, treating architecture as the software
engineering problem of building systems that satisfy properties theorists
specify [5].

The language-model generation of multi-agent systems arrived in 2023.
AutoGen offered a framework in which several agents converse to complete a
task, combining models, human input and tools, with interaction patterns
programmed in natural language and code [6]. MetaGPT encoded standardized
operating procedures into prompt sequences and assigned agents the roles
of a software company -- product manager, architect, project manager,
engineer and QA engineer -- arguing that naively chaining models produces
cascading hallucinations [7]. ChatDev organized specialized agents across
design, coding and testing phases through a "chat chain" that controls
what they discuss and a "communicative dehallucination" step that controls
how [8]. In the same year Du and colleagues proposed multiagent debate, in
which several model instances propose answers and debate them over several
rounds before settling on a common answer, and reported gains in
mathematical and strategic reasoning and in factual accuracy [9]. In the
author's summary, these works put three candidate mechanisms on the table:
role specialization, structured hand-off artifacts, and critique between
agents.

Practitioner guidance from 2024 and 2025 was more cautious than the early
enthusiasm. Anthropic distinguished workflows, in which models and tools
run through predefined code paths, from agents, which direct their own
process and tool use; it catalogued designs including
orchestrator-workers, parallelization and evaluator-optimizer and advised
finding the simplest solution possible and adding complexity only when
needed [10]. OpenAI's guide to building agents recommended maximizing a
single agent's capabilities first and splitting into several agents only
when instructions become too complex or tools overlap too much to choose
between [11]. In June 2025 Anthropic described a production multi-agent
research system together with its costs [12], and in the same month
Cognition argued against multi-agent designs for most tasks, because
subagents that do not share context make conflicting implicit decisions
[13]. Microsoft's Azure Architecture Center now catalogues five
orchestration patterns and places multi-agent orchestration at the top of
a complexity ladder, after a direct model call and a single agent with
tools [14].

The most recent work measures rather than advocates. A failure taxonomy
applied to more than 1,600 annotated traces of seven open-source
multi-agent frameworks found failure rates between 41% and 86.7% and
attributed many failures to system design and coordination [15]. A
controlled study of 260 configurations across six agentic benchmarks found
that multi-agent coordination raised performance by 80.8% on one task and
lowered it by up to 70% on another [16]. A 2025 study of debate found that
majority voting over independent answers accounts for most of the gains
attributed to it [20]. The question the field now asks is therefore no
longer whether several agents beat one, but which coordination structure
fits which task structure and where verification must sit. This is the
author's synthesis of the sources above.

## Core Concepts

Every orchestration design answers three questions: who decides what work
exists, how work and context move between agents, and who checks a result
before it is accepted. The patterns below give different answers. The
three-question framing is the author's synthesis; the patterns themselves
are documented in the cited sources.

### The Sequential Pipeline

A sequential pipeline chains agents in a predefined linear order; each
agent processes the output of the one before it. Microsoft lists the
pattern under the names pipeline, prompt chaining and linear delegation
[14]. MetaGPT is an assembly line of this kind: each role produces a
structured document such as requirements or a system design for the next
role, and the authors report that these intermediate structured outputs
significantly increase the success rate of code generation because they
keep communication consistent [7]. The Knowrite novel-writing engine is a
creative example: a writer agent drafts a chapter from an outline, an
editor agent applies a structured review and returns the draft for
revision for up to three rounds, and further agents remove machine-like
phrasing, proofread and simulate a reader [26]. The strengths are a
deterministic order and stages that can each be inspected. The weakness is
that nothing runs in parallel and an error made early travels down the
line; MetaGPT's authors name cascading hallucinations as the failure that
structured hand-offs are meant to stop [7].

### The Supervisor-Worker (Orchestrator-Workers) Pattern

In the orchestrator-workers design a central model breaks a task down,
delegates the parts to worker models and synthesizes their results [10].
Anthropic recommends it for complex tasks whose subtasks cannot be
predicted in advance, such as a coding change whose files depend on the
request; unlike plain parallelization, the subtasks are chosen by the
orchestrator for each input [10]. OpenAI calls the same idea the manager
pattern, in which a central manager agent calls specialized agents as
tools [11], and LangChain's documentation calls it subagents, with all
routing passing through the main agent [23]. Kim and colleagues describe
their centralized architecture, a single orchestrator coordinating rounds
of sub-agents, as stabilizing reasoning at the cost of a bottleneck at the
orchestrator [16]. Anthropic's Research system uses this pattern: a lead
agent plans the research, saves the plan to memory and spawns subagents
that search in parallel [12]. The strength is one place where work is
assigned and results are checked; the weakness is that the orchestrator's
judgment and context window limit the whole system.

### Hierarchical Decomposition

A hierarchy nests the supervisor pattern: managers delegate to agents that
may in turn manage others. CrewAI's hierarchical process organizes tasks
in a chain of command and requires either a manager model or a custom
manager agent that creates and manages the tasks [24]. Microsoft's
Magentic-One puts a lead Orchestrator over specialized agents that operate
a web browser, navigate files or write and run code; the Orchestrator
plans, tracks progress and re-plans to recover from errors [21]. Azure's
matching "magentic" pattern targets open-ended problems with no
predetermined plan: a manager agent builds a task ledger of goals and
subgoals and tracks it to completion [14]. Kim and colleagues' hybrid
architecture combines an orchestrated hierarchy with limited peer
communication [16]. In the author's assessment, each added level adds one
more hand-off at which context is summarized and can be lost, so depth
should follow the real structure of the task rather than an organizational
chart.

### Debate, Group Chat and Maker-Checker Loops

In group chat orchestration, agents share one conversation thread and a
chat manager decides who speaks next; Microsoft lists the pattern under
the names roundtable, collaborative, multiagent debate and council, and
advises limiting it to three or fewer agents to keep control [14]. A
maker-checker loop is a special case in which one agent proposes and
another checks the result against defined criteria and sends it back with
feedback until it passes [14]; Anthropic describes the same loop as
evaluator-optimizer [10]. Du and colleagues' debate has several instances
answer, read each other's answers and revise over several rounds [9].
Liang and colleagues motivated their debate framework by a failure of
self-reflection they call degeneration of thought: once a model is
confident in a solution it stops generating new ideas even when it is
wrong. Their framework sets agents arguing "tit for tat" under a judge,
and they found that an adaptive stopping rule and only a modest level of
disagreement were needed for good results, and that a model may not judge
fairly when the debaters are different models [17]. In the author's
assessment, every debater and round adds model calls, so debate multiplies
cost, and it decorrelates errors only when agents disagree for independent
reasons; the Evidence section shows how much of its measured gain comes
from voting.

### Parallel Fan-Out (the Swarm Pattern)

Concurrent orchestration runs several agents on the same task at once,
each giving an independent analysis; Microsoft lists it under the names
parallel, fan-out/fan-in, scatter-gather and map-reduce [14]. Anthropic
distinguishes two variants: sectioning, which splits a task into
independent subtasks run in parallel, and voting, which runs the same task
several times to obtain diverse outputs [10]. Mixture-of-Agents stacks
this pattern in layers, each agent reading all outputs of the previous
layer; a version built only from open-source models scored 65.1% on
AlpacaEval 2.0 against 57.5% for GPT-4 Omni [25]. Fan-out shortens wall
time: Anthropic's lead agent starts three to five subagents in parallel,
and with parallel tool calls this cut research time by up to 90% for
complex queries [12]. It does not remove errors. In Kim and colleagues'
study, independent agents whose outputs were merged without cross-checking
amplified trace-level errors 17.2 times, against 4.4 times under
centralized coordination [16].

### Handoffs and Routing

In a decentralized design, peer agents pass work to each other according
to their specialization. OpenAI defines a handoff as a one-way transfer,
implemented as a tool: when an agent calls it, the receiving agent starts
and receives the latest conversation state [11]. Microsoft's handoff
orchestration lets each agent decide whether to handle a task or transfer
it, and lists routing, triage, transfer, dispatch and delegation as other
names [14]. LangChain separates handoffs, where state changes switch the
active agent, from a router, which classifies the input once, sends it to
one or more specialized agents and combines their responses; it also
offers custom workflows built with LangGraph that mix deterministic logic
with agent steps [23].

### Context: Isolation Versus Sharing

Each subagent in Anthropic's system works in its own context window and
returns a condensed result, so the lead agent's context holds summaries
rather than raw search output [12]. Cognition draws the opposite lesson
from the same mechanism. Its two principles are to share context and to
remember that actions carry implicit decisions; in its example, two
subagents build parts of a Flappy Bird clone: one misreads its subtask and
builds a Super Mario-style background, the other builds a bird that
matches neither the game's look nor its movement, and the final agent is
left to combine two miscommunications. It recommends a single-threaded
linear agent, with a model that compresses history for very long tasks
[13]. In the author's assessment the two positions agree on the mechanism
and differ on the task: isolation buys context capacity and parallelism at
the price of shared understanding, which suits read-heavy, separable
research and fails on tightly coupled work. Anthropic itself notes that
most coding tasks are a poor fit [12].

### Communication Mechanisms

Agents exchange information in three basic ways. Shared stores descend
from the blackboard [2]: MetaGPT's agents publish structured messages to a
shared message pool, subscribe to the messages their role needs and act
only when all their prerequisites have arrived [7]. Conversation passes
messages between agents directly, as in AutoGen [6]. Append-only logs let
agents record what they did and let others catch up asynchronously; the
logbook that coordinates the agents of the Suggi-Workstation system works
this way, with entries appended and never edited and no agent waiting for
a reply [28]. The choice determines how tightly agents are coupled and how
easily a failure can be traced afterwards; this is the author's synthesis.

## Evidence

### Anthropic's Research system: orchestrator-workers at production scale

Anthropic built its Research feature as an orchestrator-worker system. A
lead agent analyzes the query, plans and saves its plan to memory, then
spawns subagents that search in parallel with their own context windows
and return findings; the lead synthesizes them, and a separate citation
agent finally attributes each claim to its source [12]. On Anthropic's
internal research evaluation, a system with Claude Opus 4 as lead and
Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by
90.2%. In an analysis of the BrowseComp browsing benchmark, three factors
explained 95% of the performance variance, and token usage alone explained
80% [12]. The cost is steep: agents used about four times the tokens of a
chat, and multi-agent systems about fifteen times. Early versions spawned
50 subagents for simple queries and distracted each other with excessive
updates, and the lead agent still waits synchronously for its subagents,
which creates a bottleneck [12]. In the author's assessment, the study is
an engineering report on Anthropic's own evaluation rather than an
independent benchmark, but it shows where the pattern pays: breadth-first,
parallelizable search whose value justifies the tokens.

The same report records what made the orchestration work. Each subagent
needed an objective, an output format, guidance on tools and sources, and
clear task boundaries; without them subagents duplicated each other's work
or left gaps. Because agents misjudged how much effort a query deserved,
Anthropic wrote scaling rules into the prompts: one agent with three to
ten tool calls for simple fact-finding, two to four subagents for direct
comparisons, and more than ten with divided responsibilities for complex
research [12]. Small changes to the lead agent changed subagent behavior
unpredictably, so the team evaluated end states rather than the exact path
taken, started with about twenty test queries, graded outputs with a
rubric-based model judge, and kept manual testing [12].

### MAST: why multi-agent systems fail

Cemri and colleagues collected more than 1,600 execution traces from seven
open-source frameworks: MetaGPT, ChatDev, HyperAgent, AppWorld, AG2,
Magentic-One and OpenManus [15]. Expert annotators built a taxonomy from
150 traces, refining definitions until they reached an inter-annotator
agreement of kappa 0.88; an LLM judge validated against them (94%
accuracy, kappa 0.77) then labeled the rest. The taxonomy has 14 failure
modes in three categories: system design issues, inter-agent misalignment
and task verification [15]. Failure rates ranged from 41% to 86.7% across
the systems. Among the labeled failures, common modes included step
repetition (15.7%), reasoning-action mismatch (13.2%), not recognizing
task completion (12.4%) and disobeying the task specification (11.8%);
verification failures -- premature termination, missing verification and
incorrect verification -- accounted for 6.2%, 8.2% and 9.1% [15]. Systems
with explicit verifiers such as MetaGPT and ChatDev showed fewer failures,
but a verifier was not sufficient by itself. In one example a
ChatDev-generated chess program passed superficial checks such as
compilation but contained runtime bugs, because the verifier never tested
it against the actual rules of the game; the authors found that many
verifiers in existing systems perform only such surface checks [15]. Two
interventions with the same model and prompt raised ChatDev's task success
by 9.4% (clearer role specifications) and 15.6% (a high-level objective
verification step). The authors conclude that many failures come from
organizational design and coordination rather than from the limitations of
individual agents [15].

### Controlled scaling across architectures

Kim and colleagues held tools, prompts and compute constant and compared a
single agent with four multi-agent architectures -- independent,
centralized, decentralized and hybrid -- across 260 configurations, six
benchmarks and three model families [16]. Their predictive model explains
part of the variance (cross-validated R-squared 0.373) and picked the best
architecture for 87% of held-out configurations. Results depended on task
structure. On Finance-Agent, a decomposable financial-reasoning task,
centralized coordination improved performance by 80.8% over a single
agent. On PlanCraft, a sequential planning task, every multi-agent
architecture did worse, from -39.1% for hybrid to -70.0% for independent
agents [16]. Gains also shrank as the single agent improved: where a
single agent already exceeded about 45% accuracy, adding agents gave
negative returns, and tool-heavy tasks appeared to carry extra
coordination overhead. Architectures without central verification
propagated errors more: trace-level error amplification was 17.2 for
independent agents, 7.8 for decentralized, 5.1 for hybrid and 4.4 for
centralized [16].

### Debate under controlled comparison

Du and colleagues' debate improved reasoning and factual accuracy over a
single model in their experiments [9]. Later controlled studies narrowed
the claim. Smit and colleagues benchmarked several debate protocols
against other prompting strategies and found that debate in its current
form does not reliably beat self-consistency or ensembling over multiple
reasoning paths, although tuned protocols and adjusting how readily agents
agree could surpass them [18]. Wang and colleagues found that a single
model with strong prompts nearly matches the best multi-agent discussion
across a range of reasoning tasks, and that discussion helped only when
the prompt contained no worked demonstrations [19]. Choi, Zhu and Li
separated debate into its two components across seven benchmarks: majority
voting alone accounted for most of the gains attributed to debate, and
they proved that debate alone induces a martingale over agents' beliefs,
so debate by itself does not raise expected correctness; interventions
that bias belief updates toward correction made it more effective [20].

### Self-correction, structured roles and generalist teams

Huang and colleagues showed that language models struggle to correct their
own reasoning without external feedback and sometimes get worse after
trying [22]; this is the case for a second agent or an external check
rather than self-review. Structured roles can also pay off: MetaGPT
reported 85.9% and 87.7% Pass@1 on the HumanEval and MBPP code benchmarks
[7], and Magentic-One's orchestrator-led team reached performance
statistically competitive with the state of the art on GAIA,
AssistantBench and WebArena without changing its agents between benchmarks
[21].

## Implications

For **agent system architects**, the first design decision is whether to
orchestrate at all. Anthropic, OpenAI and Microsoft all recommend the
lowest level of complexity that reliably meets the requirement: a direct
model call, then a single agent with tools, then several agents
[10][11][14]. OpenAI names two signals that justify splitting a single
agent: instructions so full of conditional branches that the prompt no
longer scales, and tool sets whose overlap leads the agent to pick the
wrong tool, noting that some agents handle more than fifteen distinct
tools while others struggle with fewer than ten overlapping ones [11].
Microsoft adds a third: tasks that need distinct security boundaries for
different agents [14]. Once orchestration is justified, the pattern should
follow the task's structure. In the author's synthesis of the evidence:
work that decomposes into independent, read-heavy parts fits
orchestrator-workers or fan-out with a central check [12][16]; tightly
sequential planning is usually better left to a single agent [16];
judgment calls benefit first from independent answers and a vote, with
debate added only when its protocol is designed to correct errors [20];
and open-ended tasks with no plan suit a manager that keeps an explicit
task ledger [14][21].

Architects also own the delegation contract. Anthropic's experience is
that an orchestrator delegates well only when each subtask states its
objective, output format, tools and sources, and boundary, and when effort
rules tell the orchestrator how many subagents a query deserves [12]. The
written role specifications that raised ChatDev's success rate [15] are
the same lesson in another system: the interface between agents is a
design artifact to be specified, reviewed and versioned, not a sentence
left to the orchestrator's improvisation. This is the author's synthesis.
Cognition's warning sets the limit of the pattern: when subtasks share
hidden decisions, such as the visual style of a game, splitting them
across agents that cannot see each other's choices produces parts that do
not fit, however carefully each part is specified [13].

For **reliability and verification engineers**, the evidence points to
verification as the main lever. In MAST's ChatDev case study, adding an
objective-level verification step raised task success by 15.6%, more than
clearer role specifications did [15]; centralized coordination cut error
amplification to roughly a quarter of the independent level [16]; and
self-review without outside feedback is unreliable [22]. In the author's
assessment, a checker that runs tests, re-reads sources or compares the
output with the original requirement does more than a second agent asked
for its opinion. MAST also shows that many failures are about termination
and specification -- agents that repeat steps, do not know when they are
done or drift from the task -- which argues for explicit stopping
conditions and written role contracts rather than more agents [15]. The
chess example in MAST is a warning about verifier design: a check that
confirms compilation but not behavior lets a wrong result pass with an
appearance of review [15]. In the author's assessment, every verifier
should be able to fail the output on the property the user actually cares
about, and its own pass rate should be watched; a checker that never
rejects anything is a sign that it tests the wrong thing.

For **teams that own cost and operations**, multi-agent designs multiply
spending. Anthropic's systems used about fifteen times the tokens of a
chat, and token use alone explained 80% of the performance variance in its
browsing analysis, so the design only pays where a task's value covers the
tokens [12]. The capability ceiling in Kim and colleagues' study suggests
that as base models improve, the margin for coordination shrinks on tasks
a single agent already handles [16]. Operations also change: early agents
spawned far too many subagents, long-running agents need deployment
methods that do not break work in progress -- Anthropic shifts traffic
gradually between versions -- and synchronous waiting on subagents limits
throughput [12]. Budgets for the number of agents, rounds and tokens
belong in the design rather than in after-the-fact monitoring; this is the
author's assessment.

For **coding-agent builders**, the evidence argues for restraint.
Anthropic judges most coding tasks a poor fit for its research
architecture because they have fewer truly parallel subtasks and need
shared context [12]. Cognition notes that Claude Code, as of June 2025,
used subagents mainly to answer well-defined questions rather than to
write code, and never ran them in parallel with the main agent, so that
their investigation stayed out of the main agent's history [13]. Where
coding systems do use several agents, the measured gains come from
structured artifacts and executable checks: MetaGPT's engineer runs the
code and fixes errors from the feedback, and its structured documents
raised success rates [7]. Kim and colleagues include SWE-bench Verified
and Terminal-Bench among their benchmarks [16]; in the author's reading,
their finding that tool-heavy tasks carry coordination overhead applies
most directly to such work.

For **researchers and evaluators**, the comparison that matters is against
a strong single-agent baseline with the same tools and compute. Without
it, gains attributed to coordination may come from extra tokens, extra
samples or better prompts [12][19][20]. Kim and colleagues' controlled
design and the MAST taxonomy offer reusable methods: hold inputs constant
across architectures, and annotate traces with a shared failure vocabulary
so that fixes target the actual failure mode [15][16].

For **the Suggi-Workstation system**, the Library pipeline has discoverer,
writer and reviewer roles that share one candidate queue and activity log,
and a publishing helper applies each change under a lock [27]; in the
author's assessment this is a sequential pipeline with a verification
stage. The logbook that links the agents is an append-only log: agents
append entries, never edit them, and catch up by reading what others wrote
since they last looked [28]. In the author's assessment, the logbook is
closer to a blackboard than to a pipeline, and both choices match the
evidence above: they keep agents loosely coupled, leave every hand-off
inspectable, and put verification in a named role rather than in agreement
between agents.

## Common Pitfalls

**Over-orchestration.** Not every complex task needs several agents; a
single agent with the right tools and prompt often achieves similar
results [23]. Add an agent only when a specific failure of the single
agent -- prompt complexity, tool overload or a security boundary --
justifies it [11][14].

**Under-specified hand-offs.** Inter-agent misalignment, such as
withholding information or ignoring another agent's input, is one of
MAST's three failure categories [15], and subagents that lack shared
context make conflicting implicit decisions [13]. Define what each
hand-off carries -- the original requirement, the decisions already taken
and the expected output format -- and prefer structured documents to free
conversation [7].

**The telephone game.** Each stage that summarizes or rewrites can
introduce distortions that compound, and errors spread furthest when no
stage checks them [7][16]. Keep the original requirement available to the
final verifier, keep verification central, and keep group conversations
small; Microsoft advises three or fewer agents in a group chat [14].

**Mistaking agreement for evidence.** In the author's assessment, when
agents share a model, prompts and sources, their agreement may count one
judgment several times. Collect independent answers before any discussion,
because voting over them carries most of the measured benefit of debate
[20].

**Unbounded spawning.** Without explicit effort rules, orchestrators
over-delegate; Anthropic's early agents spawned 50 subagents for simple
queries [12]. Tie the number of subagents and tool calls to the complexity
of the query.

## Sources

1. Erman, L. D., Hayes-Roth, F., Lesser, V. R. & Reddy, D. R. (1980).
   "The Hearsay-II Speech-Understanding System: Integrating Knowledge to
   Resolve Uncertainty." ACM Computing Surveys, 12(2), 213-253.
   https://doi.org/10.1145/356810.356816 [high]

2. Wikipedia. "Blackboard system."
   https://en.wikipedia.org/wiki/Blackboard_system [medium]

3. Smith, R. G. (1980). "The Contract Net Protocol: High-Level
   Communication and Control in a Distributed Problem Solver." IEEE
   Transactions on Computers, C-29(12), 1104-1113.
   https://doi.org/10.1109/TC.1980.1675516 [high]

4. Wikipedia. "Contract Net Protocol."
   https://en.wikipedia.org/wiki/Contract_Net_Protocol [medium]

5. Wooldridge, M. & Jennings, N. R. (1995). "Intelligent agents: theory
   and practice." The Knowledge Engineering Review, 10(2), 115-152.
   https://doi.org/10.1017/S0269888900008122 [high]

6. Wu, Q., Bansal, G., Zhang, J., et al. (2023). "AutoGen: Enabling
   Next-Gen LLM Applications via Multi-Agent Conversation."
   arXiv:2308.08155. https://arxiv.org/abs/2308.08155 [high]

7. Hong, S., Zhuge, M., Chen, J., et al. (2023). "MetaGPT: Meta
   Programming for A Multi-Agent Collaborative Framework."
   arXiv:2308.00352. https://arxiv.org/abs/2308.00352 [high]

8. Qian, C., Liu, W., Liu, H., et al. (2024). "ChatDev: Communicative
   Agents for Software Development." ACL 2024. arXiv:2307.07924.
   https://arxiv.org/abs/2307.07924 [high]

9. Du, Y., Li, S., Torralba, A., Tenenbaum, J. B. & Mordatch, I. (2024).
   "Improving Factuality and Reasoning in Language Models through
   Multiagent Debate." Proceedings of the 41st International Conference
   on Machine Learning, PMLR 235. arXiv:2305.14325.
   https://arxiv.org/abs/2305.14325 [high]

10. Anthropic -- Erik S. & Zhang, B. (2024). "Building Effective AI
    Agents." Anthropic Engineering, 19 December 2024.
    https://www.anthropic.com/engineering/building-effective-agents [high]

11. OpenAI (2025). "A practical guide to building agents."
    https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
    [high]

12. Anthropic -- Hadfield, J., Zhang, B., Lien, K., Scholz, F., Fox, J. &
    Ford, D. (2025). "How we built our multi-agent research system."
    Anthropic Engineering, 13 June 2025.
    https://www.anthropic.com/engineering/multi-agent-research-system [high]

13. Yan, W. (2025). "Don't Build Multi-Agents." Cognition, 12 June 2025.
    https://cognition.ai/blog/dont-build-multi-agents [medium]

14. Microsoft Azure Architecture Center (2026). "AI Agent Orchestration
    Patterns."
    https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns [high]

15. Cemri, M., Pan, M. Z., Yang, S., et al. (2025). "Why Do Multi-Agent
    LLM Systems Fail?" arXiv:2503.13657.
    https://arxiv.org/abs/2503.13657 [high]

16. Kim, Y., Gu, K., Park, C., et al. (2025). "Towards a Science of
    Scaling Agent Systems." arXiv:2512.08296 (v3, April 2026).
    https://arxiv.org/abs/2512.08296 [high]

17. Liang, T., He, Z., Jiao, W., et al. (2024). "Encouraging Divergent
    Thinking in Large Language Models through Multi-Agent Debate."
    EMNLP 2024. arXiv:2305.19118.
    https://arxiv.org/abs/2305.19118 [high]

18. Smit, A., Duckworth, P., Grinsztajn, N., Barrett, T. D. &
    Pretorius, A. (2023). "Should we be going MAD? A Look at Multi-Agent
    Debate Strategies for LLMs." arXiv:2311.17371.
    https://arxiv.org/abs/2311.17371 [high]

19. Wang, Q., Wang, Z., Su, Y., Tong, H. & Song, Y. (2024). "Rethinking
    the Bounds of LLM Reasoning: Are Multi-Agent Discussions the Key?"
    arXiv:2402.18272. https://arxiv.org/abs/2402.18272 [high]

20. Choi, H. K., Zhu, X. & Li, S. (2025). "Debate or Vote: Which Yields
    Better Decisions in Multi-Agent Large Language Models?" NeurIPS 2025.
    arXiv:2508.17536. https://arxiv.org/abs/2508.17536 [high]

21. Fourney, A., Bansal, G., Mozannar, H., et al. (2024). "Magentic-One:
    A Generalist Multi-Agent System for Solving Complex Tasks."
    arXiv:2411.04468. https://arxiv.org/abs/2411.04468 [high]

22. Huang, J., Chen, X., Mishra, S., et al. (2024). "Large Language
    Models Cannot Self-Correct Reasoning Yet." ICLR 2024.
    arXiv:2310.01798. https://arxiv.org/abs/2310.01798 [high]

23. LangChain. "Multi-agent." LangChain documentation.
    https://docs.langchain.com/oss/python/langchain/multi-agent [medium]

24. CrewAI. "Processes." CrewAI documentation.
    https://docs.crewai.com/en/concepts/processes [medium]

25. Wang, J., Wang, J., Athiwaratkun, B., Zhang, C. & Zou, J. (2024).
    "Mixture-of-Agents Enhances Large Language Model Capabilities."
    arXiv:2406.04692. https://arxiv.org/abs/2406.04692 [high]

26. knoai. "Knowrite: AI-Powered Multi-Agent Novel Writing Engine."
    GitHub repository README. https://github.com/knoai/knowrite [medium]

27. agentic-brain. "Library Guide." `library/guide-library.md`.
    [medium]

28. agentic-brain. "Logbook Protocol -- Inter-Agent Communication Spec."
    `logbook/protocol.md`. [medium]

## See Also

- `library/coding-agentic-ai/anchor-coding-agentic-ai.md` -- domain anchor.
- `library/coding-agentic-ai/context-window-management.md` -- how context
  limits drive the need for agent decomposition.
- `library/coding-agentic-ai/agent-planning-and-task-decomposition.md` --
  how work is split into units before it is distributed to agents.
- `library/coding-agentic-ai/agent-cost-latency-and-resource-governance.md`
  -- budgets for the token cost that orchestration multiplies.
- `library/coding-agentic-ai/agent-uncertainty-verification-and-abstention.md`
  -- why external verification beats self-confidence.
- `library/probabilistic-thinking-forecasting/forecast-aggregation-and-ensembles.md`
  -- when combining independent judgments improves accuracy.
- `research/insights/council-of-five.md` -- a fleet design that applies
  independent first assessments before discussion.
