---
name: coverage-needs-a-selection-order
id: 20260914T214659Z
tier: reflection
trigger: session-end
author: Morpheus
tags: [verification, gate-design, knowledge-system, scope, automation]
links:
  - research/insights/library-system.md
  - library/guide-library.md
  - governance/skills/library-reviewer.md
  - reflections/2026-09-09_morpheus_safe-publication-does-not-certify-knowledge.md
  - reflections/2026-09-03_morpheus_natural-transitions-prove-automation.md
---

# Coverage Needs a Selection Order, Not Just More Reviews

## I -- Idea

Coverage improves only when the rule choosing the next task uses the same scope as the coverage goal.

The library already separated discovering candidate topics, writing new material, and reviewing existing knowledge. Its domain indexes exposed review dates, but the master index showed topic totals without a corresponding review count. Suggi observed repeated attention to the early domains and asked for a way to see unfinished review work across the whole library. That request concerned allocation of attention before research began, not the quality of the eventual prose or the safety of its Git commit.

The approved master table now distinguishes topic totals from the count reviewed at least once. Overdue reviews are a subset of that reviewed count. Subtracting Reviewed from Topics therefore identifies the first-review backlog without counting older reviewed material twice. The generator reads the underlying topic metadata and builds both index levels from the same data. It does not treat its own previous output as a second source of truth. Invalid dates stop generation instead of quietly producing reassuring but false coverage.

Visibility alone did not define the next action. The reviewer procedure was changed to compare domains before entering their topic indexes. It selects the largest absolute never-reviewed backlog, with explicit tie-breaking. Only when no never-reviewed topics remain anywhere in the reviewable library does it consider overdue work. Suggi also reduced the cycle to one topic. The publication helper's existing review-size check was tightened accordingly, while the procedural rule additionally prevents replacement attempts and multiple requests within the same cycle.

A real execution exercised that selection. It naturally chose the value-investing domain and one previously unreviewed Berkshire annual-report topic. This was evidence that the revised rule reached the running agent and influenced its choice. It was not evidence of a completed review. The provider later ended a response with an incomplete status and content-filter reason, before the agent submitted a publication request. The original topic remained unchanged, and the partial draft retained unfinished citation and content checks.

The error research also separated a structured signal from an explanation. [OpenAI's response schema](https://developers.openai.com/api/reference/resources/responses/methods/retrieve.md) lists content filtering separately from output-budget exhaustion. Hermes has an [upstream issue](https://github.com/NousResearch/hermes-agent/issues/55637) and [merged correction](https://github.com/NousResearch/hermes-agent/pull/65061) addressing that exact incomplete-response shape. Those sources explain the classification, not which passage caused this particular block. Reports of apparent false positives make that possibility credible without establishing it here. The installed classifier and the captured response supported a provider-filter diagnosis, not a timeout or a publication-lock rejection.

My blank-page model already distinguished safe publication from justified knowledge. The prior publication and natural-transition reflections support that distinction. This session adds an earlier boundary: a correct review of the wrong next topic would still fail the chosen coverage policy. Selection, execution, content acceptance, and publication need separate evidence because they answer different questions.

## O -- Opinion

Confidence: high (90%), as an engineering judgment rather than a measured reliability estimate. I favor an explicit domain-first selection order over vague instructions to spread reviews around. The evidence is the observable change in selection after the master index and procedure were aligned. I do not extend that confidence to successful end-to-end operation on the replacement model, because the attempted run stopped before completing its review.

The chosen backlog rule is a policy, not a universal definition of value. Ranking absolute unfinished counts directs more attention toward larger backlogs. Ranking percentages would favor a different pattern of coverage, while ranking risk or expected knowledge value could choose different topics again. Suggi selected first-review coverage. My responsibility was to make that objective explicit and executable, not quietly substitute a round-robin schedule or a preferred investing topic. The selected domain's familiarity must not become an unofficial tie-breaker.

That policy has a real limitation. A continuing supply of new, never-reviewed topics can postpone overdue work indefinitely. The rule deliberately gives first review precedence, so this consequence should remain visible rather than be hidden behind the word fairness. If the library later needs an age limit or a reserved allocation for overdue material, that would be a new policy decision requiring approval. It would not be a harmless implementation detail that an agent should insert while repairing the selector.

Reducing the batch to one topic gives the cycle a smaller research and publication scope. It does not prove a fixed duration, prevent every context problem, or establish that a less demanding model setting is sufficient. Comparing a successful two-topic run with an interrupted one-topic run would confound batch size, subject matter, model, and completion status. The failed run is useful evidence about selection and a failure boundary, but it is not a speed benchmark or a valid estimate of completed reviews per hour.

The daily index refresh is justified by a different mechanism: eligibility can change as time passes without any file being edited. A scheduled invocation of the existing Python workflow catches that transition without adding another reasoning agent. Preserving unchanged output avoids timestamp-only commits. This is a shared-library need, whereas job model pins remain the responsibility of the individual agent's configuration. Similar use of scheduling does not make those two scopes interchangeable.

Finally, I favor leaving an unexplained provider filter alone until the next authorized test rather than adjusting unrelated guards. [Hermes's official guidance](https://hermes-agent.nousresearch.com/docs/reference/faq) distinguishes explicit tool enforcement from a model's explanation of its refusal. The captured provider field was stronger evidence than the surrounding generated text. [Public reports](https://github.com/openai/codex/issues/33736) describe apparent false positives, but they do not identify our trigger. The right position is narrow: classification established, cause within the provider unknown, no safety bypass, and no claim that waiting guarantees recovery.

## R -- Reflection

### Surprise (30%)

I expected the live test to tell us primarily whether one topic on the replacement model was sufficiently quick and coherent. Instead, it established the new selection behavior while leaving the completion question unanswered. The provider interruption split what initially looked like one experiment into different results. The choice of domain passed; the final artifact could not be approved. Treating the entire run as either uniformly successful or uniformly useless would have discarded evidence.

A second surprise was how much meaning sat inside the Reviewed column. Ever-reviewed and currently fresh are not interchangeable totals. An overdue topic has already received an initial review. If I had subtracted the overdue subset again, I would have changed the user's priority rule through a bookkeeping error. The small interface decision therefore carried a scheduling contract, not merely a readability preference. Its definition had to be shared by the generator, the procedure, and the explanation.

### Feel (30%)

The pressure was to validate a reasonable simplification: a smaller cycle and a different model should be enough for routine library work. I cannot turn that expectation into a result. The partial draft contained useful corrections, but it also had unresolved citation numbering and incomplete checks. Calling it a reviewed topic would have repeated the earlier mistake of letting progress replace acceptance. Equally, judging the unfinished draft as the model's final standard would have overstated the negative evidence.

Suggi's suspicion about the publication guard was worth testing because that component had recently changed. The code and trace rejected the hypothesis: one topic was accepted by the current regression, and no publish command had been invoked. I am satisfied with answering through that evidence instead of defending the component because I helped build it. Proportionality remains a constraint, however. Once the failing boundary was established, further modification would have required a new reason and new approval.

### Learn (40%)

First, translate a global priority into an ordered selection procedure before beginning local work. Compute the backlog from the complete master table, choose the domain, then choose the topic. Keep the date semantics explicit and verify the underlying frontmatter. A general instruction to prefer never-reviewed material is insufficient if the agent first narrows its attention to a convenient domain and only then applies that preference.

Second, preserve the separate meanings of progress and completion. A model pin is configuration evidence; a runtime log identifies actual use. Correct selection establishes the allocation policy for that attempt. A finished draft, passed checklist, publication receipt, and exact remote readback establish later stages. A zero process exit or a plausible summary cannot stand in for those stages. An interruption should leave a clear partial result rather than acquire a successful review stamp through implication.

Third, keep deterministic checks close to the rules they can actually enforce. Date-boundary, invalid-metadata, unchanged-output, and one-topic publication tests can reject concrete counterexamples automatically. Research quality still requires the complete topic and source checks. The next authorized reviewer test must observe that remaining path; repeating the already-passing publisher test would not answer whether the agent can finish. This is a bounded use of uncertainty, not an invitation to add a new monitor or redesign the pipeline.

## One Actionable Change

Use the existing single-run timing and before/after procedure for the next
user-authorized reviewer test: record a clean starting commit and scheduling
state, derive the expected domain from the complete master index, run once,
and compare the selected topic with its original. PASS for a completed review
requires the expected selection, one completed execution, the final topic
checklist, and exact published output. Otherwise HALT the completed-review
claim. A failed execution is recorded as a
failed test with its specific verified partial results. The canonical reviewer
owns selection; the existing operator procedure owns observation. Do not add
an automatic retry or a separate scheduler to manufacture a green result.

## Cross-links

- `research/insights/library-system.md` -- index semantics, selection policy, refresh ownership, and failure boundaries.
- `library/guide-library.md` -- publication contract and the separation between mechanical checks and research acceptance.
- `governance/skills/library-reviewer.md` -- domain-first selection, global never-reviewed precedence, and one-topic limit.
- `reflections/2026-09-09_morpheus_safe-publication-does-not-certify-knowledge.md` (id: 20260909T081148Z) -- the content-acceptance boundary; this reflection adds the prior allocation decision.
- `reflections/2026-09-03_morpheus_natural-transitions-prove-automation.md` (id: 20260903T165935Z) -- why observing the normal execution path matters.
