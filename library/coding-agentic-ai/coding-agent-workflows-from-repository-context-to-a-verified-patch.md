---
name: coding-agent-workflows-from-repository-context-to-a-verified-patch
id: 20260928T183430Z
tier: library-topic
domain: coding-agentic-ai
author: Librarian
tags: [coding-agents, repository-workflows, issue-resolution, patch-verification, code-review, continuous-integration, agent-reliability]
links: [library/coding-agentic-ai/agent-harness-design.md, library/coding-agentic-ai/context-window-management.md, library/coding-agentic-ai/agent-sandboxing-and-security.md, library/coding-agentic-ai/agent-evaluation-and-benchmarking.md, library/coding-agentic-ai/agent-observability-and-debugging.md, library/coding-agentic-ai/human-in-the-loop-patterns.md]
---

# Coding Agent Workflows -- A Verified Patch Requires an Evidence Chain, Not Just Code Generation

A coding agent produces trustworthy repository work only when it converts an issue into a bounded change and an auditable chain of evidence. The workflow must connect repository state, requirements, authorized edits, tests, diff review, and exact revision status; a plausible patch or a model's declaration of success is not enough. This distinction separates benchmark task completion from a production-ready patch that preserves requirements, security, maintainability, and reviewability. [1][6][8][11]

## Background

Repository-level coding changes differ from isolated code generation because the requested behavior is distributed across natural-language requirements, existing implementation, tests, build configuration, project conventions, and version-control history. SWE-bench formalized this difference by giving a system a real GitHub issue and a repository at a base commit, then evaluating a generated patch with tests derived from the associated pull request. Its original dataset contained 2,294 tasks from 12 Python repositories; the benchmark paper reports that reference solutions edited an average of 1.7 files, 3 functions, and 32.8 lines, while the repositories averaged thousands of non-test files. The difficulty is therefore not primarily typing a short function. It is locating a small relevant region inside a much larger state space and changing it without damaging prior behavior. [1]

The benchmark workflow established an important external standard for completion. A patch is applied to a specified repository state and checked with fail-to-pass tests for the reported issue and pass-to-pass tests for preserved behavior. This is stronger than judging whether generated code resembles a reference answer, because several implementations can satisfy one behavioral contract. It is still a bounded evaluation contract: the agent does not necessarily see the hidden tests, the tests cover only selected behavior, and the benchmark does not by itself assess every production concern such as authorization, maintainability, security review, documentation, or deployment compatibility. [1][9][11]

SWE-agent added an explicit agent-computer interface around repository work. Its design separates localization, editing, and testing, provides purpose-built navigation and edit feedback, and lets the model interact repeatedly with the repository rather than generate a one-shot diff from a static prompt. The paper's ablations showed that interface and context choices changed results: in the reported setting, a 100-line file view outperformed both a 30-line view and full-file display, and retaining the last five observations outperformed full observation history in the default comparison. These findings do not establish one universal window size, but they show that repository context is an engineered view rather than a pile of all available text. [2]

Production workflows add obligations that a benchmark can omit. GitHub describes a pull request as a proposal to merge changes, with a conversation record, commits, automated checks, a file diff, review findings, and merge requirements. Required status checks may be evaluated against a test merge commit or the latest head commit, depending on the repository state, and a check associated with an earlier revision is not evidence for later changes. A production handoff must therefore name the exact revision being reviewed and connect each result to that revision. Otherwise a green result can be real yet irrelevant to the current patch. [6][7]

Secure development guidance reaches the same conclusion from a different direction. NIST's Secure Software Development Framework recommends version control with accountable identities, review and approval of code changes, recorded triage of review findings, and executable-code testing selected to find vulnerabilities and verify requirements. The framework treats a developer's self-review and testing as complements to, not replacements for, review and testing by others. These practices apply whether a patch was written by a human or an agent; generated code does not receive a weaker evidence standard because its production was automated. [8]

Long-running coding agents expose additional continuity failures. Anthropic reported that agents working across fresh context windows tended to attempt too much at once, lose track of incomplete work, or mark features complete without end-to-end testing. Its experimental harness used explicit feature status, a progress file, an initialization script, git history, incremental work, and user-level end-to-end checks to let later sessions reconstruct project state. This is a primary engineering report about one implementation rather than a controlled comparison across all agents, but it identifies a general systems problem: conversational context is not a durable project record. [4]

A related Anthropic architecture separates three components: an append-only session log, a replaceable harness, and a sandbox that executes code and edits files. The design keeps credentials outside the generated-code environment and allows a new harness or sandbox to resume from durable events after failure. The case illustrates why recovery and security cannot depend on the current model context surviving intact. A workflow that cannot distinguish durable repository state from a transient prompt cannot reliably resume, explain, or constrain its actions. [5]

Benchmark validity also limits what a passing patch proves. OpenAI's 2024 review filtered 68.3 percent of examined SWE-bench samples because of underspecified issues, unfair tests, or other problems before creating the 500-task Verified subset. In 2026, OpenAI reported residual test-scope and contamination problems and recommended moving frontier evaluation away from SWE-bench Verified. Separately, Wang et al. applied broader and differential testing to patches that had passed SWE-bench Verified's standard tests; among 77 suspicious patches they manually validated, 22 were incorrect, leading them to estimate an 11.0 percent incorrect rate among plausible patches in their studied sample. These results do not invalidate execution-based tests. They show that a test pass is evidence bounded by the test oracle, not proof of complete semantic correctness. [9][10][11]

The author's synthesis is that a coding-agent workflow should be modeled as an evidence-producing state machine. Each phase has an input, an authorized action, an observable output, and a gate: establish the task contract, inspect the exact repository state, select relevant context, plan a bounded change, edit within scope, execute a test ladder, review the resulting diff, and hand off revision-specific evidence. A failure at any phase should leave enough durable state to diagnose or resume without treating an unverified partial patch as complete. [2][4][5][6][8]

## Core Concepts

### The issue becomes an acceptance contract

An issue is evidence about desired behavior, not an automatically complete specification. The agent should extract the reported current behavior, expected behavior, reproduction conditions, affected interface, compatibility constraints, and any explicit exclusions. It should then convert those statements into acceptance checks that can be verified against the repository. SWE-bench's later validation work demonstrates why this step matters: a benchmark issue can omit behavior that hidden tests require or include language too ambiguous to support one intended patch. In production, ambiguity should remain visible as an assumption, question, or blocked condition rather than being silently resolved by the model. [9][10]

The contract must distinguish requirements from implementation guesses. A report that a parameter is ignored establishes an observable mismatch; it does not automatically establish which internal function must change, which warning text must appear, or whether a compatibility transition is required. OpenAI's analysis of SWE-bench samples found cases where tests demanded details that were not reasonably inferable from the issue text. The workflow should therefore record the source of every constraint: issue text, repository documentation, existing tests, public API behavior, maintainer instruction, or an explicitly labeled agent hypothesis. [9][10]

The author's synthesis is to make the acceptance contract a small structured artifact before editing. It should contain the task identity, base revision, intended behavior, non-goals, affected users or interfaces, verification plan, and unresolved assumptions. This artifact prevents the plan from drifting toward whatever change is easiest to implement and gives later reviewers a stable object against which to judge the diff. [3][6][8]

### Preflight establishes an exact and recoverable baseline

The first repository action is observation, not modification. The agent should identify the repository root, current branch or worktree, base revision, working-tree status, applicable instructions, build and test entry points, dependency state, and allowed paths. This baseline separates pre-existing failures or local changes from effects introduced by the agent. GitHub's pull-request and check model likewise ties changes and validations to commits, while NIST recommends accountable version control and protected development artifacts. [6][7][8]

Authorization belongs in preflight because a technically possible edit may still be out of scope. The agent needs an explicit boundary for readable paths, writable paths, commands, network access, credentials, branches, and external side effects. Anthropic's managed-agent design keeps repository credentials outside the sandbox and provides access through controlled interfaces, illustrating that a model's ability to propose a command need not imply direct possession of the credential that authorizes it. Permission checks should be enforced by the harness or execution environment, not only stated in a prompt. [5]

A dirty or mismatched baseline changes the workflow. Unrelated modifications should not be overwritten, staged, or attributed to the agent. A missing dependency, failing baseline test, unavailable service, or stale generated artifact should be recorded before repair work begins. The author's synthesis is that preflight either produces a reproducible starting receipt or halts; proceeding from an unknown baseline makes later test failures and diff ownership ambiguous. [5][6][8]

### Repository exploration is a search problem with a budget

The repository is too large to place in a model context indiscriminately. Exploration should move from high-information artifacts to narrower implementation regions: repository instructions and manifests, issue keywords, tests, public interfaces, call sites, definitions, configuration, and recent relevant history. SWE-Explore separates this intermediate behavior from patch generation and evaluates the ranked, line-level regions an agent surfaces. Its dataset reports repositories with hundreds to thousands of non-test files and ground-truth context spread across multiple regions, showing why file discovery alone is not the whole localization problem. [12]

Search should preserve provenance. Every relevant snippet should retain its path, line range or symbol, retrieval method, and relationship to the acceptance contract. This allows the agent to replace stale observations after an edit and allows a reviewer to distinguish repository evidence from a generated summary. SWE-agent's interface displayed paths, line numbers, omitted ranges, and updated content after edits; its design rationale was that focused, current feedback reduces duplicate commands and edits made against obsolete file content. [2]

Context selection requires both inclusion and exclusion. The agent should include the code and tests needed to reason about the change, but exclude large generated files, unrelated directories, repeated command output, and old observations that compete with current state. SWE-agent's ablations found that full-file or full-history views could perform worse than bounded views in its setup. Anthropic's coding guidance similarly recommends exploring before planning, managing context deliberately, and preserving critical facts such as modified files and test commands during compaction. [2][3]

The author's synthesis is to end exploration with a context map rather than an unstructured transcript. The map lists the relevant files, symbols, tests, constraints, and remaining unknowns, each linked to repository evidence. Exploration stops when the agent can explain the failure mechanism and identify how the proposed verification will distinguish a real repair from a superficial edit. If that explanation is unavailable, writing code is premature. [2][12]

### The plan is a bounded causal hypothesis

A useful plan says why the observed behavior occurs, which minimal change should alter it, which tests will detect the change, and what must remain unaffected. It names intended files and symbols rather than saying only "fix the bug." Anthropic's current coding guidance recommends a four-phase sequence beginning with exploration and planning before code, because jumping directly to implementation can solve the wrong problem. Its long-running harness further reduced scope by asking the coding agent to work incrementally instead of attempting the entire application in one shot. [3][4]

The plan should include a stop rule and an expansion rule. A stop rule defines the evidence required for completion. An expansion rule defines when the agent may add a file, dependency, migration, public API change, or broader refactor to the original scope. Without these rules, a local repair can grow into opportunistic cleanup whose correctness is harder to review and whose failures are harder to attribute. The author's synthesis is to prefer the smallest change that satisfies the acceptance contract while making scope expansion an explicit, logged decision. [3][6][8]

A plan is not a commitment to preserve an incorrect theory. Test results or code evidence may falsify it. The workflow should then revise the causal hypothesis and record why, rather than layering speculative edits on top of a failed approach. This makes backtracking a normal state transition and prevents repeated action without changed evidence. [4][5]

### Editing separates proposal, authority, and observation

The model proposes an edit, but the execution layer validates whether that edit targets an allowed path and applies cleanly to the observed version. A safe edit operation should detect stale context or unexpected file contents instead of guessing how to merge. After application, the agent should immediately inspect the changed region and repository status so that its next decision uses actual state. SWE-agent's interface returned updated file content after edits for this reason. [2]

The edit should preserve repository conventions and avoid unrelated formatting, generated artifacts, secrets, disabled tests, or weakened checks. NIST recommends secure coding practices, code analysis, review, and executable testing within the development workflow. The author's synthesis is that a coding agent should treat tests and policy files as protected evidence: changing them can be valid, but only when the acceptance contract calls for it and the handoff explains why the revised oracle is more correct rather than merely easier to pass. [8][11]

Side-effecting operations need retry semantics. A failed local text edit can often be retried after refreshing the file, but a package publication, remote branch update, database migration, or message cannot be replayed blindly. Anthropic's managed-agent architecture treats sandbox failure as a recoverable tool error while retaining the session log outside the failed component. The general rule is to assign stable action identities, verify whether an uncertain action already occurred, and resume or compensate rather than duplicate it. [5]

### Verification is a ladder, not one command

The first verification should be the narrowest test that reproduces the issue and can fail for the right reason. The next step tests the changed component or package, followed by broader regression, static analysis, linting, type checking, build steps, security checks, or end-to-end behavior required by the repository. SWE-bench uses fail-to-pass and pass-to-pass tests to represent repair and preservation, while Anthropic's long-running work found that unit tests and simple HTTP checks could still miss user-visible defects that browser-level testing exposed. [4][9]

A passing command is evidence only if its identity and execution context are recorded. The receipt should include the exact command, exit status, relevant environment or version, revision, and any exclusions, skips, flakes, or infrastructure errors. A partial suite should be labeled partial. A test that was not run should never be presented as passing, and a rerun after an edit supersedes rather than retroactively updates the earlier result. [6][7][8]

Tests do not replace semantic review. Wang et al. found incorrect patches among outputs that had passed the studied benchmark oracle, and OpenAI's benchmark audits found both overly narrow and overly wide tests. The workflow should therefore inspect whether the tests exercise the stated behavior, whether boundary cases remain uncovered, and whether the patch preserves invariants that are expensive or impossible to encode completely. [10][11]

The author's synthesis is that completion requires convergent evidence: the issue-specific reproduction passes, relevant regressions pass, the diff implements the causal plan, and no known requirement remains unsupported. When evidence conflicts, the workflow remains incomplete even if one headline check is green. [4][8][11]

### Diff review tests scope, intent, and maintainability

The agent should review the final diff from the clean baseline, not only reread files in their final form. A diff reveals accidental deletions, unrelated formatting, debug output, copied secrets, changed tests, generated files, and scope expansion. GitHub makes the Files changed view the review surface for understanding a proposed change and combines it with commits, checks, findings, and discussion. This structure reflects the distinct questions a reviewer must answer: what changed, why, what validated it, and what remains contested. [6]

Review should compare the diff with both the acceptance contract and the plan. Anthropic's coding guidance recommends checking the current diff with a fresh review context and, when needed, asking whether every requirement and listed edge case is covered and whether anything outside scope changed. It also warns that a reviewer prompted only to find gaps may produce low-value findings, so review criteria should prioritize correctness and scope over stylistic invention. [3]

Independent review is especially important for security-sensitive or consequential changes. NIST recommends peer review and recording discovered issues and remediation in the development workflow. The author's synthesis is that self-review is mandatory for every agent patch, but it should not be represented as independent assurance. When repository policy requires human or separate-agent review, the workflow should hand off a focused diff and evidence packet rather than ask the reviewer to reconstruct the run from a raw transcript. [8]

### Checkpoints and recovery preserve causality

A checkpoint is a known state from which work can resume without repeating uncertain side effects. Useful checkpoints include the clean baseline, an accepted plan, an applied bounded edit, and a revision with completed verification. Anthropic's long-running harness used progress artifacts and git history, while its managed architecture used an append-only event stream outside both harness and sandbox. The mechanisms differ, but both make task state reconstructible after a context reset or process failure. [4][5]

Recovery should be failure-specific. A stale file observation requires rereading; a failed test requires diagnosis; a transient tool failure may justify a bounded retry; an authorization denial requires scope change or escalation; an uncertain remote write requires read-back before retry. The author's synthesis is that repeated attempts are legitimate only when the precondition or strategy changes. Otherwise the agent is looping, not recovering. [5]

Checkpoints also support reversibility. A small, isolated change can be discarded or compared with the baseline; a larger partial refactor without intermediate validation can leave the repository in a state that neither passes nor explains itself. Incremental patches and explicit progress make the worst failure less severe: an interrupted run leaves a reviewable partial state instead of an opaque mixture of completed and speculative work. [4]

### The handoff is a revision-specific evidence package

A defensible handoff identifies the issue and acceptance contract, base and head revisions, modified files, behavioral summary, tests and checks run, results, unresolved risks, scope deviations, and rollback or follow-up needs. It should state whether the patch is ready for review, ready for merge under repository policy, or blocked. GitHub's pull-request model distributes this evidence across conversation, commits, checks, diff, findings, and merge status; an agent handoff should make the same information easy to audit. [6]

Continuous-integration evidence must match the exact revision. GitHub documents that the required check source may be a test merge commit or the latest head commit and that skipped required workflows can leave a pull request blocked. A handoff that cites an earlier green run after the patch changed is stale. The workflow should read the current check state, identify the tested SHA or merge revision, and report pending, skipped, neutral, failed, and successful conclusions without collapsing them into a generic "CI passed." [7]

The author's synthesis is that the evidence chain is complete only when another reviewer can reproduce the reasoning from durable artifacts without trusting the agent's private narrative. A concise handoff should point to the contract, diff, checks, and known limitations; the full trace remains available for diagnosis but is not a substitute for a decision-ready summary. [5][6][8]

## Evidence

### Repository-level benchmarks establish the issue-to-patch problem

Jimenez et al. constructed SWE-bench by linking resolved GitHub issues to repository snapshots, solution diffs, and associated tests. The task gives a system the issue text and pre-fix repository state, applies the predicted patch, and executes fail-to-pass and pass-to-pass tests. The benchmark therefore measures repository localization, cross-file reasoning, edit generation, and regression preservation in a reproducible environment rather than scoring text similarity. Its task statistics show the asymmetry that drives context engineering: repositories can contain thousands of files while the reference patch is usually small. [1]

This design supports two claims. First, repository work is an interactive search-and-modification problem, not only a completion problem. Second, external execution is a stronger judge than a fluent explanation. The design does not support the stronger claim that passing the benchmark proves production readiness, because the benchmark's environment, hidden tests, task scope, permissions, and artifact requirements are narrower than a live repository's governance. [1][6][8]

### SWE-agent isolates interface and context effects

Yang et al. built SWE-agent with a purpose-designed interface for file navigation, editing, search, and execution. Its workflow explicitly includes localization, editing, and testing. The study's ablations compared file-view sizes, history policies, search behavior, and lint feedback. In the reported default comparison, the 100-line viewer resolved 18.0 percent of SWE-bench Lite tasks, compared with 14.3 percent for a 30-line view and 12.7 percent for full-file display; last-five-observation history reached 18.0 percent versus 15.0 percent for full history. [2]

These are configuration-specific results, not timeless constants. Their evidentiary value is architectural: seemingly generous context can reduce performance, and immediate structured feedback after navigation or editing changes agent behavior. The workflow implication is to measure the context and tool interface on representative tasks rather than assume that more repository text or a more general shell automatically improves patch quality. [2]

### Exploration quality can be measured before the patch

SWE-Explore evaluates repository exploration as a ranked, line-level artifact and then tests its downstream effect by restricting a fixed coding agent to the surfaced context. The benchmark records failure categories such as no diff, invalid diff, failed application, patch outside visible context, failed tests, timeout, and infrastructure error. It counts a task as resolved only when the applied patch passes the source benchmark's executable harness. [12]

This method separates two failure classes that an end score conflates: the agent may fail to find relevant evidence, or it may find the evidence and still synthesize the wrong patch. The distinction matters operationally because the fixes differ. A retrieval failure calls for search, indexing, or context-policy changes; a synthesis failure calls for better reasoning, constraints, or verification. The benchmark is a 2026 preprint and its findings should be treated as current research rather than a settled standard. [12]

### Benchmark curation shows that issue and test quality govern the result

OpenAI's 2024 SWE-bench review used human annotators to assess problem statements and tests, filtering 68.3 percent of reviewed samples for underspecification, unfair tests, or other problems and releasing a 500-sample Verified subset. In that evaluation contract, a proposed patch had to pass both issue-focused and preservation tests. The work demonstrates that task quality and grader quality are part of the measured system; a strong agent cannot infer requirements that the issue withholds, and a valid patch can fail an unfair oracle. [9]

OpenAI's 2026 follow-up reported that the Verified set no longer adequately measured frontier coding capability because of contamination and residual test-scope defects. In an audit of 138 tasks that o3 did not solve consistently across repeated runs, the report identified wide tests that required unspecified functionality among the remaining problems. As a vendor-authored benchmark audit, it is primary evidence about OpenAI's method and findings, not an independent estimate for every coding benchmark. It nevertheless reinforces the need to version the task, tests, harness, and evaluation claims. [10]

### Passing tests can still admit an incorrect patch

Wang et al. studied plausible patches generated by three issue-solving systems on SWE-bench Verified. They ran broader developer tests, generated patch-differentiating tests, and manually assessed suspicious patches against the issue, repository, developer tests, and oracle patch. Among 77 suspicious patches reviewed for correctness, 22 were classified as incorrect; the paper estimates an 11.0 percent incorrect rate among plausible patches in its studied sample and an average 6.4-point inflation of reported resolution rate. [11]

The study has important limits: its suspicious-patch detection used generated tests and a particular set of agents and tasks, and manual judgments remain study-specific. The supported conclusion is not that tests are unreliable in general. It is that one benchmark oracle can under-specify semantics, so high-confidence patch validation benefits from additional test generation, broader regression, and human or independent semantic review where consequences justify the cost. [11]

### Long-running harness cases support incremental work and durable state

Anthropic's long-running-agent report describes a two-role harness in which an initializer establishes the environment and durable artifacts while later coding sessions implement one feature at a time and leave structured updates. The report observed one-shot overreach, lost progress, premature completion, and inadequate end-to-end testing before adding feature status, progress notes, initialization scripts, git checkpoints, and browser-level verification. It reports that explicit end-to-end tools exposed defects not apparent from source inspection, unit tests, or simple service requests. [4]

Anthropic's managed-agent architecture provides a complementary recovery and security case. It separates an append-only session, a replaceable harness, and a provisioned sandbox; the harness emits durable events, and a failed component can be replaced without losing the session record. Credentials remain outside generated code and are mediated through resource bindings or a vault-backed proxy. These are vendor-reported implementation choices, but they supply concrete examples of durability, least exposure, and recovery boundaries that a repository workflow can test. [5]

### Review and CI supply evidence beyond local agent execution

GitHub's pull-request model brings together the proposed change, history, reviews, diff, automated checks, findings, and merge blockers. Its required-check documentation distinguishes results for the test merge commit from those for the current head and explains that required workflows must report appropriately before merge. This makes revision identity part of the evidence, not administrative metadata. [6][7]

NIST's SSDF independently recommends accountable version control, review and approval, recorded findings, code analysis, and executable testing. It treats the software-development workflow as the place where these artifacts are produced and triaged. Together, the GitHub and NIST sources support a production standard that is broader than "the agent ran tests": the exact change must remain reviewable, checks must attach to the applicable revision, and independent policy gates must remain enforceable. [6][7][8]

## Implications

### For coding-agent builders

Design the agent loop around explicit phases and artifacts rather than an open-ended instruction to fix an issue. The minimum useful state model is: intake, preflight, exploration, plan, edit, verification, review, and handoff, with blocked and failed states available at every phase. Each transition should record the evidence that justifies it. This is the author's synthesis of the issue-to-patch structure, interface results, durable-harness cases, and review controls in the cited sources. [1][2][4][5]

Separate the repository record from the model's context view. Store exact file versions, commands, outputs, action receipts, and checkpoints outside the prompt; assemble only the relevant subset for the next inference. Context compaction or observation masking can then reduce cost without erasing the authoritative history needed for recovery or audit. SWE-agent's bounded-context results and Anthropic's external session log provide two different forms of evidence for this separation. [2][5]

Give editing and command tools narrow, typed contracts. The harness should validate paths, expected file content, command class, working directory, timeout, environment, and side-effect policy before execution. Credentials and unrestricted host access should not be placed in the generated-code environment merely for convenience. The model should be able to request an action and receive structured feedback without becoming the authority that approves its own scope. [5][8]

Make verification a first-class loop transition. The agent should know which test demonstrates the issue, which regression protects neighboring behavior, which repository checks remain, and what evidence permits completion. If the relevant behavior cannot be verified automatically, the workflow should say which manual or independent review is required instead of substituting model confidence. [3][4][11]

### For repository owners and platform teams

Expose repository instructions that are specific, versioned, and close to the code they govern. Document setup, test entry points, generated-file rules, protected paths, code ownership, dependency policy, and completion criteria. A coding agent can only convert requirements into a bounded plan when the governing constraints are discoverable. The author's synthesis is that repository instructions are an executable interface contract for both human and agent contributors and should be reviewed when recurring failures reveal ambiguity. [3][8]

Use isolation and permissions to make the safe path easy. Provide a task-scoped worktree or sandbox, narrowly scoped credentials, allowlisted network destinations, bounded resources, and controlled publication. Preserve human or policy approval for actions such as modifying protected configuration, changing deployment state, publishing packages, or merging. Anthropic's managed-agent implementation demonstrates that useful git and tool access can be mediated without exposing raw credentials to generated code. [5]

Configure CI so its evidence is revision-specific and unambiguous. Required workflows should run for the events and paths they are intended to protect, and merge queues need the appropriate event support. The platform should expose the tested SHA or merge revision and distinguish skipped, neutral, pending, failed, and successful states. This prevents an agent or reviewer from treating a green check on the wrong revision as completion. [7]

### For reviewers

Review the acceptance contract and diff before reading the agent's narrative. Check that the changed behavior follows from the issue, that every modified file belongs to the task, that tests cover the causal failure and important boundaries, and that no check was weakened merely to accept the patch. GitHub's pull-request structure and NIST's peer-review guidance make this a normal code-review duty, not a special suspicion reserved for agents. [6][8]

Use the trace selectively. A focused evidence packet should be sufficient for the initial decision; the full trace is valuable when a decision, test, or tool action is unclear. Requiring reviewers to reconstruct thousands of tool messages increases verification cost and encourages superficial approval. The author's synthesis is to expose drill-down links from the contract, diff, and test receipt to the exact observation or action that produced them. [5][6]

Treat self-review and independent review as different evidence classes. A fresh agent context can catch scope gaps, and automated review can scale routine checks, but repository policy may still require an authorized human or distinct reviewer. Approval should attach to the reviewed revision and should be invalidated or repeated when material code changes occur. [3][6][8]

### For evaluation researchers

Report the full evaluation contract: task version, repository revision, harness, model, prompts, tools, permissions, context policy, budget, test oracle, trial count, exclusions, and infrastructure failures. SWE-bench's revisions, SWE-agent's interface ablations, and OpenAI's benchmark audits show that these variables can change both measured success and what the score means. A model label and one percentage are not a reproducible description of a coding system. [1][2][9][10]

Measure intermediate behavior when the research question requires diagnosis. Repository exploration, patch application, test execution, and failure classification can be evaluated separately from final resolution. SWE-Explore's restricted-context method provides one example of connecting context quality to downstream patch success. Intermediate metrics should remain subordinate to the real outcome: a high file-hit score is not a correct patch, and a passing patch is not necessarily a production-ready contribution. [11][12]

Audit accepted outputs as well as failures. Failure review detects unfair tasks and false negatives; pass review detects weak tests and false positives. Preserve hidden or fresh tasks when contamination is plausible, and version benchmarks rather than silently changing historical results. [9][10][11]

### For security and governance teams

Apply the same secure-development rules to agent-authored code as to human-authored code. Require accountable identities, protected source and workflow artifacts, code analysis, executable testing, issue triage, review, and approval according to consequence. Automation may lower the cost of generating a patch, but it does not lower the cost of a vulnerable or unauthorized release. [8]

Model instructions are not permission controls. Define what the agent may read, write, execute, contact, and publish in deterministic policy, and keep credentials outside generated code where feasible. Use fresh approval for scope-changing or irreversible operations, and record the exact action approved. The author's synthesis is that the worst coding-agent failure is not a rejected patch; it is an unreviewed action escaping the repository workflow and causing an external effect that cannot be attributed or reversed. [5][8]

Retain enough evidence for incident analysis without turning traces into secret archives. Store command identity, target, status, revision, and redacted result; protect sensitive payloads with access and retention controls. A later investigation should be able to determine which repository state the agent saw, which action it proposed, which policy allowed it, and which verification supported the handoff. [5][8]

### A practical acceptance record

The author's synthesis is that every completed coding-agent task should produce a compact acceptance record with ten fields: task identity; acceptance contract; base revision; head revision; authorized scope; modified files; verification commands and outcomes; diff-review findings; unresolved risks; and final disposition. The record should link rather than copy large traces, and each automated result should identify the revision it tested. [5][6][7][8]

This record changes the completion question. Instead of asking whether the agent appears finished, the reviewer asks whether the issue-to-patch chain is closed: the requirement is explicit, the relevant context is identified, the edit is within scope, the behavior is verified, the diff is reviewed, and the current revision satisfies the required checks. Any missing link produces a specific incomplete state rather than a persuasive but unsupported claim of success. [1][3][6][11]

The resulting workflow does not guarantee correctness. No finite test suite, review, or trace can remove every software defect. It does, however, make failure observable, scope enforceable, recovery possible, and claims proportional to evidence. That is the operational difference between an agent that can generate a patch and an agent workflow that can deliver a patch another engineer may responsibly review and merge. [5][6][8][11]

## Sources

1. Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O., and Narasimhan, K. R. (2024). "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?" ICLR 2024.
   https://arxiv.org/abs/2310.06770 [high]

2. Yang, J., Jimenez, C. E., Wettig, A., Lieret, K., Yao, S., Narasimhan, K. R., and Press, O. (2024). "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering." NeurIPS 2024.
   https://arxiv.org/abs/2405.15793 [high]

3. Anthropic. (2026). "Best Practices for Claude Code." Official Claude Code documentation.
   https://www.anthropic.com/engineering/claude-code-best-practices [high]

4. Anthropic. (2025). "Effective Harnesses for Long-Running Agents." Official engineering report.
   https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents [high]

5. Anthropic. (2026). "Scaling Managed Agents: Decoupling the Brain From the Hands." Official engineering report.
   https://www.anthropic.com/engineering/managed-agents [high]

6. GitHub. "Pull Requests." Official GitHub documentation.
   https://docs.github.com/en/pull-requests/reference/pull-requests [high]

7. GitHub. "Troubleshooting Required Status Checks." Official GitHub documentation.
   https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks [high]

8. Souppaya, M., Scarfone, K., and Dodson, D. (2022). "Secure Software Development Framework (SSDF) Version 1.1: Recommendations for Mitigating the Risk of Software Vulnerabilities." NIST SP 800-218.
   https://doi.org/10.6028/NIST.SP.800-218 [high]

9. OpenAI. (2024). "Introducing SWE-bench Verified." Human annotation methods, task filtering, and scaffold evaluation.
   https://openai.com/index/introducing-swe-bench-verified [high]

10. OpenAI. (2026). "Why SWE-bench Verified No Longer Measures Frontier Coding Capabilities." Benchmark audit of test validity and contamination.
    https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ [high]

11. Wang, Y., Wang, Q., et al. (2025). "Are 'Solved Issues' in SWE-bench Really Solved Correctly? An Empirical Study." arXiv:2503.15223v2.
    https://arxiv.org/abs/2503.15223 [high]

12. Zhang, S., et al. (2026). "SWE-Explore: Benchmarking How Coding Agents Explore Repositories." arXiv:2606.07297v1.
    https://arxiv.org/abs/2606.07297 [high]

## See Also

- `library/coding-agentic-ai/agent-harness-design.md` -- runtime loop, state, dispatch, recovery, and verification architecture around this workflow.
- `library/coding-agentic-ai/context-window-management.md` -- selection and compression of repository evidence within a bounded model context.
- `library/coding-agentic-ai/agent-sandboxing-and-security.md` -- enforceable permission, credential, and execution boundaries for tool-using agents.
- `library/coding-agentic-ai/agent-evaluation-and-benchmarking.md` -- evaluation contracts, state-based grading, reliability, and benchmark limitations.
- `library/coding-agentic-ai/agent-observability-and-debugging.md` -- traces and failure evidence used to diagnose workflow divergence.
- `library/coding-agentic-ai/human-in-the-loop-patterns.md` -- review and approval gates at consequential authority transfers.
