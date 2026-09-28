---
name: forecast-question-design
id: 20260928T213514Z
tier: library-topic
domain: probabilistic-thinking-forecasting
author: Librarian
tags: [forecast-question-design, resolution-criteria, forecasting-tournaments, proper-scoring-rules, prediction-markets, ai-benchmarks, question-decomposition]
links: [library/probabilistic-thinking-forecasting/superforecasting.md, library/probabilistic-thinking-forecasting/prediction-markets.md, library/probabilistic-thinking-forecasting/fermi-estimation-and-decomposition.md, library/probabilistic-thinking-forecasting/calibration-and-overconfidence.md, library/probabilistic-thinking-forecasting/base-rate-neglect.md]
---

# Forecast Question Design Makes Uncertainty Measurable Only When Resolution Is Specified in Advance

A forecast question converts a concern about the future into a defined event, outcome space, time horizon, and resolution procedure that can support probabilistic judgment and later scoring [1][4][6]. The wording is not administrative packaging: it determines what forecasters research, when they may update, which evidence counts, and whether two forecasts can be compared fairly [2][3][8][9]. A useful question must therefore be decision-relevant, discriminating, and difficult enough to reward judgment while remaining unambiguous enough to resolve from evidence that will actually be available [10][11][12].

## Background

Human beings have always made predictions, but ordinary predictive language often protects a claim from decisive evaluation. Statements such as "instability may increase," "the policy could work," or "the technology is likely to arrive soon" do not identify an outcome, probability, population, or deadline. Tetlock and colleagues argued that forecasting tournaments create transparency by replacing such vague-verbiage predictions with explicit probabilities that can be compared with observed outcomes [6]. This conversion is an operationalization problem: a broad uncertainty must be reduced to a proposition whose truth conditions are known before the future unfolds.

The modern tournament tradition joined this operationalization with repeated measurement. The U.S. Intelligence Advanced Research Projects Activity created the Aggregative Contingent Estimation program to improve the accuracy, precision, and timeliness of intelligence forecasts by eliciting and combining probabilistic judgments and testing them against real events [5]. In the resulting tournaments, forecasters worked on hundreds of questions, updated while questions remained open, and received accuracy feedback through Brier scores [6][7]. Those arrangements made question design part of the measurement instrument. If an outcome cannot be classified consistently, a score is not a clean measure of forecasting skill; it partly measures how administrators interpreted the question after the fact.

Operational platforms developed detailed rules because the failure modes recur. Metaculus tells question writers to use tight resolution criteria, authoritative sources, explicit dates, fallback criteria, and advance treatment of edge cases [1]. Its approval checklist asks whether the headline matches the resolution criteria, whether the question tracks a named source or the underlying truth, and whether fallback sources exist [2]. Its resolution policy distinguishes ambiguity, where reality itself is unclear, from annulment, where reality may be clear but the question failed to specify how to map that reality to an outcome [3]. Good Judgment Open similarly specifies evidentiary standards, source handling, deadline conventions, data revisions, rounding, and retroactive closing rules [4]. These are accumulated controls against predictable specification errors, not stylistic preferences.

Prediction markets expose the same issue with direct financial consequences. A market contract pays according to a resolved outcome, so the title, source, end date, contingencies, and dispute process together define the asset being traded. Polymarket's documentation states that its pre-defined rules identify the resolution source, end date, and edge cases, and that disputed outcomes can move through challenge and voting procedures [13]. A market that asks about the public meaning of an event while settling on a narrower textual trigger creates basis risk: traders may be correct about the event they thought they were forecasting and still lose under the contract they actually bought. The author's synthesis is that a forecast question and an event contract share the same core architecture even when only the latter transfers money.

Question design also determines whether a set of forecasts can evaluate people or machines. ForecastBench was built as a dynamic benchmark containing unresolved future questions, with new questions and resolution values updated over time so that model training data cannot already contain the answers [10]. Bosse and colleagues later used web-research agents to generate and resolve 1,499 questions, explicitly treating unambiguous resolution, appropriate difficulty, non-extreme base rates, diversity, and discrimination of forecasting skill as benchmark properties [11]. The benchmark problem is stricter than merely collecting interesting questions: the items must remain unknown at submission, later acquire a defensible ground truth, and vary enough to reveal differences in research and judgment.

A second design problem is usefulness. A perfectly resolvable question can still be trivial, irrelevant, or disconnected from any decision. McCaslin and colleagues used conditional trees to derive intermediate questions that would change beliefs about a distant target outcome, then measured each question's expected value of information [12]. Their approach separates two questions that are often conflated: "Can this be resolved?" and "Would knowing the answer matter?" The first is a validity gate. The second concerns the value of the information produced.

Forecast question design is therefore the construction of a measurement contract between the question writer, forecasters, resolver, and forecast user. The contract must define the target without pretending away uncertainty, preserve incentives while evidence arrives, and specify how later facts become a score. When it succeeds, vague concern becomes a revisable probability and eventually a comparable observation. When it fails, precision in the submitted percentages cannot repair ambiguity in the object being measured [1][3][8].

## Core Concepts

### Begin with the decision and the uncertain quantity

A question should begin with the use of its answer. The author's synthesis is to write one sentence in the form: "Decision maker D will reconsider action A if the probability or resolved value of outcome O crosses threshold T before date H." This sentence distinguishes a forecast from curiosity. It also exposes whether the proposed question measures an outcome that can change an action, an intermediate indicator that informs another forecast, or a proxy chosen only because it is easy to observe. Conditional-tree research formalizes this concern by selecting questions according to how much their answers would update a target belief [12].

The target then needs a unit of uncertainty. For a binary question, the object is the probability that a proposition will be true. For a multiple-choice question, the options must cover the relevant outcome space without overlap. For an ordered or continuous question, bins, thresholds, units, and treatment of boundary values must be defined. Good Judgment Open uses categorical questions for date ranges and quantity ranges, while Metaculus supports question types with different resolution structures [1][4]. The author's synthesis is that the format should follow the decision variable: do not force a continuous policy threshold into Yes or No merely because binary scoring is convenient, and do not use a continuous distribution when only one operational threshold affects action.

### Make outcomes mutually exclusive, collectively adequate, and observable

Outcome categories should be mutually exclusive so that no future state satisfies two options, and collectively adequate so that plausible states do not fall outside every option. A binary proposition requires symmetry: both Yes and No need feasible evidentiary paths. Metaculus documents questions that could resolve Yes after one prominent report but could not resolve No without proving a universal negative; such asymmetry can require annulment because the two sides do not face consistent resolution standards [3]. The author's synthesis is to write a proof obligation for every outcome: what finite evidence would be sufficient to assign it?

Observability is separate from conceptual importance. "Will the reform improve social welfare?" may be decision-relevant but lacks a unique observable unless welfare, population, counterfactual, interval, and measurement rule are supplied. A narrower question such as whether a specified official series exceeds a threshold on a defined release can resolve cleanly, but it measures the series rather than welfare itself. The question writer must state that trade-off. Metaculus explicitly asks whether a question is forecasting a named source or the underlying true answer and recommends fallback sources when the latter is intended [2].

Definitions should be behavioral or documentary where possible. Concrete actions, legal states, published quantities, certified results, and dated records are easier to adjudicate than labels such as "significant," "successful," "recognized," or "invaded." If a contested term cannot be removed, the resolution criteria should list necessary and sufficient indicators, exclusions, and the authority applying the definition. Metaculus warns that questions depending on a person saying particular words often produce polarizing disputes unless the relevant term is formal and well defined [2]. The author's synthesis is to treat every adjective and operative verb as a potential hidden branch in the outcome tree.

### Separate the event horizon, close time, and resolution time

A forecast question contains at least three temporal boundaries. The event horizon is the last instant at which a qualifying event may occur. The close time is when forecasters can no longer submit or update predictions. The resolution time is when sufficient evidence is expected to exist for adjudication. Metaculus defines close and resolution dates separately and requires the predicted interval to be stated in the question text [1]. Good Judgment Open distinguishes when an event occurred from when open-source reporting confirmed it and may close a question retroactively to exclude forecasts made after the event but before confirmation [4].

These boundaries prevent information leakage and post-event trading. For scheduled data, closing immediately before release and resolving after publication is usually coherent. For an event that can occur at an unknown time, a fixed close date may either end useful updating too early or let some forecasters trade on an event that has occurred but is not yet widely reported. Retroactive closure can address that case only when the event time is itself independent of the forecasts being scored; Metaculus warns that inappropriate retroactive closure can violate proper-scoring incentives [3]. The question should also name the timezone, whether "before" excludes the first instant of the stated date, and how leap days or delayed releases are handled [3][4].

A close date should not be confused with an annulment deadline. If the source is late, the event may still have a well-defined outcome. The criteria should state whether resolution waits, uses a fallback, freezes at the latest available observation, or annuls after a specified long-stop date. Good Judgment Open may extend an expected end date when the underlying process remains unresolved, whereas fixed event deadlines remain binding [4]. The author's synthesis is that every question needs both a forecast horizon and a source-failure horizon.

### Write the resolution rule as an executable procedure

The author's synthesis is to write resolution criteria as a resolver's algorithm rather than an essay. A minimal binary procedure contains: the proposition; the observation window; the primary source; the exact field, document, or announcement to inspect; the publication or certification state that counts; the mapping to Yes and No; the treatment of corrections; fallback sources; and the action if no admissible evidence appears. A second reader should be able to apply the procedure without inferring the author's intent.

Source selection should match the claim. An official statistical agency is suitable for the value it publishes but may not be suitable for the underlying phenomenon if methodology changes. A government announcement is authoritative evidence that the government announced something, not necessarily that the announced fact is true. News wires can corroborate public events, while a specialized registry may be necessary for technical outcomes. Good Judgment Open uses credible open-source evidence by default and can name particular sources; it also reserves review for clear source error [4]. Metaculus can replace a defunct or inadequate source with a functional equivalent unless the question explicitly tracks that source [3]. These policies show why source identity and truth conditions must not be left implicit.

The hierarchy should be specified before resolution. A robust rule may say: use the primary agency's initial release; if no release exists by the long-stop date, use the first available value from a named fallback; if the methodology changed, reconstruct the prior series if the source provides it; otherwise annul. The exact hierarchy will vary, but the priority order should not be chosen after administrators see which source favors which outcome. Metaculus recommends fallback criteria and asks writers to consider source disappearance and unknown unknowns [1]. Prediction-market rules similarly define sources, end dates, edge cases, and a dispute path [13].

Corrections and revisions require an explicit freeze rule. Economic and scientific data can be revised after initial publication. Good Judgment Open normally resolves on the initial release unless the question says otherwise [4]. A question designed to predict the best later estimate may instead use a stated revision vintage. The choice changes the target: predicting a flash estimate rewards knowledge of the release process, while predicting a final revised value rewards knowledge of the underlying system. Neither is intrinsically correct, but mixing them after forecasts are submitted invalidates comparison.

### Design edge cases before they become live disputes

Edge cases are low-probability states with high specification leverage. They include cancellation, postponement, partial completion, replacement of a named institution, ties, recounts, retroactive legal reversals, missing records, conflicting sources, threshold equality, currency redenomination, revised methodologies, and an event occurring exactly at the deadline. Metaculus instructs writers to consider plausible edge cases and fallback criteria; its FAQ explains that an underspecified question may be annulled when reality does not correspond to any rule supplied [1][3]. Polymarket requires market rules to specify edge cases and provides an Unknown or 50-50 path in rare cases where neither outcome applies [13].

The objective is not to enumerate every imaginable future. That is impossible and can bury the central rule under speculative detail. The objective is to identify edge cases generated by the question's own nouns, verbs, dates, sources, and boundaries. The author's synthesis is to run four tests: remove the named source, delay the event past the expected resolution date, place the observation exactly on every threshold, and change the institutional label while preserving the underlying function. If one of these tests produces no deterministic outcome, add a rule or reject the question.

Annulment is a protection, not a neutral outcome. It removes or alters scoring after forecasters have invested effort and may selectively erase questions whose outcomes were difficult to classify. Metaculus treats annulled and ambiguous questions as unscored and separates unclear reality from unclear specification [3]. The author's synthesis is to publish an annulment policy in advance, record the reason, and audit the rate by question writer and question type. A rising annulment rate is evidence of a design process that is transferring specification risk to the resolver.

### Balance resolvability, relevance, and discrimination

A question can be clear yet useless. "Will the Sun rise tomorrow?" resolves easily but is unlikely to separate skilled from unskilled forecasters. A question tied closely to an efficient market price may similarly leave little room for research or judgment to add value. Bosse and colleagues classify good benchmark questions as unambiguously resolvable, timely, representative, diverse, appropriately difficult, nontrivial in base rate, and capable of discriminating forecasting skill [11]. Conditional-tree research adds a user-centered criterion: the answer should be expected to change an important downstream belief [12].

Difficulty has at least two components. Research difficulty concerns whether better search can uncover more diagnostic information. Judgment difficulty concerns whether better reasoning can convert the same information into a better probability [11]. A question that turns entirely on an inaccessible secret may be hard but not usefully discriminating. A question whose answer is already on a public dashboard is resolvable but no longer a forecast. The useful middle permits informed disagreement, updates as evidence arrives, and eventual adjudication.

Base rates affect information value and scoring. A set dominated by near-certain negatives lets a cautious forecaster score well without much discrimination. A set selected only for events thought likely to occur can bias the apparent success rate and distort calibration. The question portfolio should include a range of ex ante probabilities and topics, but balance must not be achieved by writing artificial or low-value events. The author's synthesis is to monitor the distribution of crowd probabilities after launch and revise future question selection, never a live question's target, when the portfolio clusters near zero or one [8][11].

### Decompose without changing the target

A broad concern often contains several causal and evidentiary branches. Decomposition can turn "Will the country face a debt crisis?" into questions about refinancing, reserves, official support, missed payments, and legal default. The existing Fermi-estimation framework in this library shows that decomposition is useful when components are more tractable than the whole and warns that multiplying weak, correlated judgments can amplify error. In question design, the same boundary applies: subquestions should reveal independent or conditionally informative evidence, not merely create more prompts.

Conditional trees provide one disciplined approach. Experts identify intermediate events that would change a target forecast, and forecasters estimate the target conditional on each intermediate outcome [12]. This preserves the connection between a resolvable near-term indicator and a long-term decision. It also exposes conditional incoherence: the probability of the target and indicator jointly cannot exceed the probability of the target. McCaslin and colleagues observed conjunction inconsistencies in some conditional forecasts, showing that a tree creates additional coherence checks rather than eliminating judgment error [12].

The author's synthesis is to separate question decomposition from forecast decomposition. Question decomposition creates multiple independently resolvable measurement objects. Forecast decomposition is a forecaster's internal method for estimating one object. A platform should not force one causal decomposition into the official question unless the decision requires those components, because doing so can narrow the hypothesis space and reward conformity to the writer's model.

### Align scoring, updating, and participation incentives

A scoring rule maps a forecast and resolved outcome to a numerical result. Gneiting and Raftery define a proper scoring rule as one under which a forecaster maximizes expected score by reporting the distribution that matches the forecaster's actual belief; strict propriety makes that optimum unique [8]. The Brier score is a strictly proper quadratic score for categorical or binary forecasts and became the official metric in the ACE tournaments [6][7][8][14]. Proper scoring does not guarantee honest behavior under every social or financial incentive, but it removes a direct mathematical reward for deliberately misstating belief under the modeled payoff.

Question design interacts with scoring. Time-averaged scores reward early correct judgment and continuing updates, while a final-only score ignores the path. Closing after an outcome becomes privately knowable rewards access rather than forecasting. Allowing participants to choose questions creates missingness and difficulty differences: Mellers and colleagues standardized scores within question to reduce difficulty effects, while Merkle and colleagues found that question selection itself contains information about forecaster ability [7][9]. A fair tournament must therefore state coverage requirements, question weights, update treatment, and how unmatched question sets affect rankings.

Scoring cannot repair a malformed outcome. If two reasonable resolvers disagree, the numerical score includes adjudication noise. If rules change after forecasts, the target distribution changes while old forecasts remain fixed. If an answer option is impossible but remains in the outcome space, forecasters allocate probability to a state the organizer should have removed or explained. The author's synthesis is that outcome integrity precedes score sophistication: first make the event resolvable, then select a proper rule matched to the outcome type.

### Freeze the contract while permitting non-substantive clarification

Once forecasts or trades exist, substantive edits can advantage participants who anticipated the new interpretation or invalidate earlier probabilities. A versioned question record should preserve the title, context, resolution criteria, source hierarchy, open time, close rule, weights, and every clarification. Polymarket states that later clarification cannot change the fundamental intent of a market and publishes such updates for resolvers [13]. Metaculus asks writers to double-check consistency before approval and reserves resolution authority to administrators rather than authors or commenters [1].

The author's synthesis is to classify edits in advance. Typographical corrections that cannot change outcome classification are non-substantive. Clarifications that select among plausible existing readings require a public timestamp and may require score exclusion for the earlier interval. Changes to the outcome set, threshold, source hierarchy, or deadline are substantive; the safer remedy is normally to annul and relaunch rather than pretend that one question persisted. This rule favors reversibility and prevents a live measurement instrument from being redesigned around emerging facts.

## Evidence

### Forecasting tournaments show why item definition and scoring must be joined

The ACE program was designed to test probabilistic forecasts against real events and to improve elicitation, aggregation, and communication across a broad range of event types [5]. Tetlock and colleagues report that the tournament's official metric was cumulative Brier score across time and more than 200 questions selected by the intelligence community [6]. Mellers and colleagues describe approximately nine-month annual tournaments in which forecasters selected questions, updated until closure, and were evaluated with question-standardized Brier scores to reduce differences in item difficulty [7]. These methods demonstrate that a forecast question is both a substantive inquiry and a scored item in a repeated measurement system.

The same studies identify design limits. Mellers and colleagues note that self-selection could let strong participants choose easier questions, so performance comparisons required within-question standardization [7]. Merkle and colleagues later modeled forecasts together with question selection and found that better forecasters tended to answer more questions and were more likely to select some less popular or more difficult items [9]. The evidence does not imply that every participant must answer every item. It shows that question portfolios, coverage, and difficulty are part of the inference from scores to skill.

Proper scoring supplies the incentive foundation but not the question specification. Gneiting and Raftery show that strictly proper rules encourage a forecaster to report the distribution that represents the forecaster's best judgment, and they warn that improper rules can produce misleading scientific inferences [8]. Brier's original work provided a squared-error verification method for probability forecasts [14]. These results justify scoring explicit probabilities after resolution. They do not determine which event should be asked, which source should resolve it, or whether the event is important; those remain design choices.

### Platform records reveal recurrent ambiguity and source failures

Metaculus's operating guidance is evidence from a large forecasting platform rather than a controlled experiment. Its question-writing guide requires tight criteria, authoritative sources, edge-case treatment, fallbacks, and explicit dates [1]. Its FAQ records distinct unsuccessful-resolution categories: ambiguity when the facts remain unclear, annulment when the question is underspecified, and failures caused by asymmetric evidence or unavailable sources [3]. The approval checklist additionally tests headline-resolution alignment and whether a named source is the object or only evidence about the object [2]. The recurrence of these controls across the guide, checklist, and FAQ indicates that wording, source continuity, and negative-outcome evidence are persistent operational risks.

Good Judgment Open independently addresses similar problems. Its FAQ specifies credible open-source evidence, treatment of source error, handling of data revisions and rounding, event-time rather than report-time closing, timezone rules, and the possibility of voiding a question amid substantial controversy [4]. The two platforms differ in administrative discretion and terminology, but they converge on the need for a known evidence standard, temporal cutoff, and failure policy. This convergence is primary operational evidence that a short headline alone does not define a forecastable event.

Prediction markets add a stronger settlement incentive. Polymarket's current documentation requires each market's rules to specify a source, end date, and edge cases, then uses bonded proposals, challenges, and an escalation process for disputed outcomes [13]. The mechanism cannot make an ambiguous predicate objective; it supplies a governance path after the predicate is applied. The evidence supports a two-layer distinction: ex ante specification reduces avoidable disputes, while ex post dispute resolution manages residual disagreement.

### Dynamic AI benchmarks make question supply and resolution measurable

ForecastBench introduced a dynamic benchmark built from 1,000 standardized questions sampled from a continuously updated bank drawing on prediction markets, forecasting platforms, and real-world data sources [10]. Questions are unresolved when forecasts are submitted, which limits answer leakage from model training data, and resolved questions are scored against later outcomes [10]. In the reported 200-question human comparison, the median superforecaster Brier score was 0.091 and the median public-participant score was 0.111, while model performance varied by configuration [10]. The exact ranking will change as systems improve, but the benchmark design establishes that time, source updates, and delayed ground truth are part of AI evaluation.

Bosse and colleagues tested a more automated pipeline. They generated 1,499 real-world questions, resolved them several months later, and manually verified a sample [11]. The paper reports an estimated annulment rate of 3.9 percent with a 95 percent confidence interval from 1.1 to 8.4 percent and an automated-resolution error rate of 4.9 percent with a 95 percent confidence interval from 1.6 to 9.8 percent in the checked sample [11]. It also reports that subquestion decomposition reduced the Brier score of one model configuration from 0.141 to 0.132 on sampled questions [11]. These are primary experimental results, but the uncertainty intervals and manual sample matter: automated generation and resolution remained imperfect, and the authors identified failures involving interactive sites, dynamically loaded content, and long PDF extraction [11].

The automated study also makes a useful distinction between research difficulty and judgment difficulty [11]. A benchmark should reward systems that find better public evidence and systems that reason better from the same evidence, but it should not be dominated by inaccessible pages or arbitrary interface friction. The author's assessment is that source accessibility is therefore part of item validity for AI benchmarks. A question can be objectively resolvable by a human with privileged browsing access yet measure tool integration more than forecasting when evaluated on constrained agents.

### Conditional trees test whether resolvable questions are informative

McCaslin and colleagues interviewed 21 AI domain experts and three highly skilled generalist forecasters to generate 75 questions intended to inform a distant AI-risk target, then collected conditional forecasts from eight superforecasters to estimate value of information [12]. For questions resolving by 2030, the conditional-tree questions were on average nine times more informative than the comparison set of high-engagement platform questions, with reported p = 0.025 [12]. Most of the tested conditional-tree questions exceeded all ten comparison questions on the study's value-of-information metric, although four ranked much lower [12].

The study is a working-paper case study with important limits. Its target concerned AI extinction, its elicitation sample for conditional forecasts was eight, and its longer-horizon comparison was not statistically significant [12]. Some conditional forecasts also violated conjunction constraints [12]. The evidence therefore does not establish a universal nine-fold gain from conditional trees. It supports the narrower proposition that structured decomposition around downstream belief change can produce questions with higher measured information value than engagement-based selection, while adding labor and coherence challenges.

Taken together, the evidence supports a layered standard. Proper scores can elicit and compare probabilities when outcomes are defined [8][14]. Tournament evidence shows that difficulty and participation affect skill estimates [7][9]. Platform experience shows that sources, deadlines, negative evidence, and edge cases repeatedly break questions [1][3][4]. AI studies show that question supply and resolution can be partly automated but still require verification [10][11]. Conditional-tree research shows that resolvability alone does not guarantee decision value [12].

## Implications

### For human forecasting tournaments

Tournament organizers should treat the question portfolio as a test instrument. Before launch, each item should pass separate gates for decision relevance, outcome completeness, source availability, temporal integrity, difficulty, and ethical acceptability. After launch, organizers should monitor coverage, crowd-probability distribution, update activity, disputes, and annulments without changing the target. At evaluation, scores should be adjusted or modeled for differing question difficulty and participation patterns when entrants did not answer the same items [7][9].

The worst tournament design failure is to rank forecasters precisely on outcomes that were not specified consistently. Proper scoring encourages truthful probabilities only relative to the event as understood by the participant [8]. If the organizer later selects a different interpretation, the ranking confounds forecasting with interpretive luck. The prevention is structural: publish the resolution rule, freeze substantive terms, timestamp clarifications, and keep an adjudication record that explains how each rule was applied [1][3][4].

Question portfolios should also be designed for discrimination rather than spectacle. Highly salient questions can attract participation while contributing little information if almost everyone makes the same near-certain forecast. Obscure questions can be difficult because data are inaccessible rather than because judgment matters. The author's synthesis is to pilot candidate items with independent reviewers who estimate likely base rate, research tractability, ambiguity risk, and connection to the tournament's intended construct. Items that test trivia, privileged access, or source-navigation accidents should be removed even if they are resolvable [10][11].

### For prediction markets

A prediction market should expose the contract, not merely the headline. Traders need the exact source hierarchy, observation time, initial-versus-revised-data rule, threshold treatment, cancellation policy, and dispute process because each can change settlement [13]. A short title can aid discovery, but it must not imply a broader real-world proposition than the contract actually pays on. The author's synthesis is that market interfaces should display a compact machine-readable rule summary beside the order entry, with the full versioned contract one click away.

Settlement governance cannot substitute for clear semantics. A bonded challenge process can deter careless resolution proposals and provide an appeal path, but voters still need a predicate to apply [13]. If the rule asks whether an undefined event "counts," token voting converts ambiguity into a governance contest. Platforms should therefore measure dispute and 50-50 rates by question template, retire templates with repeated semantic failures, and separate source disputes from definition disputes. The former ask what evidence says; the latter reveal that the asset was under-specified at listing.

Market incentives also create manipulation and self-reference risks. A question about an action that traders can cheaply cause is not merely a forecast; it is an incentive contract. Metaculus's public guidance avoids questions likely to incentivize harmful acts or create self-fulfilling and self-negating effects [1]. The same principle is stronger when money is at stake. The author's synthesis is to screen each market for whether the payout could exceed the cost of causing, suppressing, or delaying the resolution event, and to reject the market or redesign the target when that incentive is material.

### For AI forecasting benchmarks

AI benchmarks require temporal provenance. Every question should record creation time, model forecast cutoff, source snapshots available at that cutoff, close time, resolution evidence, and resolver version. ForecastBench's dynamic design addresses answer leakage by using unresolved future events and updating the bank over time [10]. A static collection eventually becomes contaminated as answers enter training corpora. A valid benchmark therefore needs a continuing question-production and resolution pipeline, not only a fixed test file.

Automated generation should be evaluated on more than grammatical quality. Bosse and colleagues demonstrate useful metrics: expert acceptability, annulment rate, resolution accuracy, diversity, and whether stronger forecasting systems score better [11]. The author's synthesis adds source-access parity, rule complexity, base-rate balance, and robustness to independent human resolution. A question that only one browser stack can resolve or that requires hidden interactive state may test infrastructure rather than forecasting.

Automated resolution should retain a human-verifiable evidence packet. The packet should contain the query plan, retrieved passages, source timestamps, the applied rule branch, the proposed outcome, and any dissent among resolver agents. A consensus of models is not independent verification when models share retrieval failures or training biases. The reported 4.9 percent error rate in a manually checked sample and the system's difficulty with interactive content and long PDFs show why disagreement triggers and random audits remain necessary [11].

Benchmark designers should avoid treating one aggregate score as a complete account of capability. Question difficulty, topic, horizon, research burden, and source type can all affect performance. ForecastBench separates question sources and resolution states, while tournament research models item difficulty and participation [9][10]. The author's synthesis is to publish stratified scores and confidence intervals, preserve item-level forecasts, and disclose which unresolved questions use crowd forecasts as temporary proxies rather than ground truth.

### For organizations using forecasts in decisions

Organizations should start from a decision map rather than a list of interesting topics. For each decision, identify the uncertain variables that could change timing, scale, or direction; then write the smallest set of resolvable questions that covers those variables. Conditional trees are useful when a distant target cannot resolve soon but intermediate events would materially update belief [12]. The tree should remain a model of relevance, not a claim that every causal path is known.

A practical question specification can use the following twelve fields. This framework is the author's synthesis of the platform, tournament, scoring, and benchmark evidence [1][2][3][4][8][10][11][13]:

1. **Decision use:** who will use the forecast and what action it could change.
2. **Headline proposition:** one neutral sentence matching the resolution rule.
3. **Outcome space:** exhaustive, non-overlapping outcomes with boundary rules.
4. **Definitions:** operational meanings for every contested noun, verb, and threshold.
5. **Event window:** first and last qualifying instants, including timezone.
6. **Open and close rules:** when forecasting starts, stops, and may close retroactively.
7. **Primary evidence:** the exact source, field, document, and publication state.
8. **Fallback hierarchy:** ordered substitutes and a long-stop date for source failure.
9. **Revision policy:** initial, latest, or named-vintage data and treatment of corrections.
10. **Edge cases:** cancellation, postponement, ties, institutional change, and equality.
11. **Scoring and weight:** proper rule, update treatment, coverage, and question weight.
12. **Governance:** resolver, clarification authority, dispute path, annulment rule, and version log.

The draft should then undergo an adversarial resolution rehearsal. Give the criteria and several hypothetical futures to reviewers who did not write the question. Ask each reviewer to resolve every future independently and explain the applied rule. Disagreement identifies hidden discretion. The author's synthesis is to reject or rewrite the question if disagreements concern the core predicate; use a documented fallback only when disagreement concerns a genuinely unforeseeable source failure. This rehearsal is the question-design analogue of testing code against boundary cases.

The base rate and decomposition belong in the forecasting brief, not necessarily in the resolution rule. Background material can identify reference classes, causal branches, and known data sources so forecasters begin from an informed baseline. It should not assert the desired answer or make the outcome depend on an argument in the background. Metaculus separates context from resolution criteria and emphasizes neutral tone and internal consistency [1]. The author's synthesis is that the brief explains why the uncertainty matters, while the rule states only how the future will be classified.

### For investors and capital allocators

Investment theses often contain forecasts that are too vague to audit: management will execute, margins will normalize, a cycle will turn, or a moat will endure. Converting these claims into resolvable questions creates a decision record. A thesis could specify a revenue-retention threshold by a filing date, a regulatory milestone evidenced by a named docket, or a leverage range based on defined accounting fields. This does not reduce intrinsic value to quarterly targets. It separates intermediate claims that can be tested from a long-term valuation that remains uncertain.

Question design can also prevent thesis drift. The investor records the source, horizon, threshold, and implications before price movement or new narrative changes the interpretation. Proper scoring over a portfolio of such questions can reveal calibration, but comparisons require similar difficulty and complete records [8][9]. The author's synthesis is to keep probability, payoff, and action separate: a resolved operational question updates the business-state distribution; valuation translates that state into cash flows; margin of safety and portfolio constraints determine the trade.

The most dangerous investment question is one whose negative outcome cannot be observed. "Will the moat weaken?" can remain perpetually unresolved because every adverse signal is reclassified as temporary. A better design identifies observable mechanisms such as customer loss, price compression, distribution displacement, or returns on incremental capital, while acknowledging that no single metric exhausts the concept. The same symmetry rule used by forecasting platforms applies: write evidence that could support both persistence and impairment, or label the thesis untestable [2][3].

### Limits and stopping rule

Not every important uncertainty can be made objectively resolvable. Counterfactual policy effects, unique historical causes, moral values, and very long-run outcomes may lack an observable ground truth within a useful horizon. Reciprocal or intersubjective methods can sometimes elicit disciplined judgments about such questions, but they are not equivalent to scoring against a realized event. The honest response is to distinguish a judgment exercise from a resolved forecasting tournament rather than manufacture a proxy and call it truth.

Question design should stop when further precision costs more value than it adds. A rule can become so elaborate that forecasters spend more effort interpreting the contract than researching the world. The author's synthesis is to retain a clause only if it changes outcome classification in a plausible state, protects scoring incentives, or identifies admissible evidence. Remove detail that merely restates the same predicate. Simplicity is achieved after the essential boundaries are explicit, not by omitting them.

The final test is reproducibility. Before launch, two independent reviewers should be able to apply the rule to the same hypothetical evidence and obtain the same outcome. After resolution, a later auditor should be able to reconstruct what forecasters knew, when the item closed, which evidence was used, and why the assigned outcome followed. If either test fails, the percentages may look precise, but the forecast question is not yet a valid measurement instrument [1][3][8].

## Sources

1. Metaculus. "Question Writing and Submission Guidelines."
   https://www.metaculus.com/question-writing [high]

2. Metaculus. "Question Approval Checklist."
   https://www.metaculus.com/help/question-checklist [high]

3. Metaculus. "Metaculus FAQ," sections on question resolution,
   ambiguous outcomes, annulment, sources, and retroactive closure.
   https://www.metaculus.com/faq [high]

4. Good Judgment Open. "Frequently Asked Questions," Question
   Clarifications and Resolutions.
   https://www.gjopen.com/faq [high]

5. Intelligence Advanced Research Projects Activity. "Aggregative
   Contingent Estimation (ACE)."
   https://www.iarpa.gov/research-programs/ace [high]

6. Tetlock, P. E., Mellers, B. A., Rohrbaugh, N., & Chen, E. (2014).
   "Forecasting Tournaments: Tools for Increasing Transparency and
   Improving the Quality of Debate." Current Directions in Psychological
   Science, 23(4), 290-295.
   https://faculty.wharton.upenn.edu/wp-content/uploads/2015/07/2014---forecasting-tournaments-tools-for-increasing-transparency-and-improving-debate.pdf [high]

7. Mellers, B., Stone, E., Murray, T., Minster, A., Rohrbaugh, N.,
   Bishop, M., Chen, E., Baker, J., Hou, Y., Horowitz, M., Ungar, L., &
   Tetlock, P. (2015). "Identifying and Cultivating Superforecasters as
   a Method of Improving Probabilistic Predictions." Perspectives on
   Psychological Science, 10(3), 267-281.
   https://doi.org/10.1177/1745691615577794 [high]

8. Gneiting, T., & Raftery, A. E. (2007). "Strictly Proper Scoring
   Rules, Prediction, and Estimation." Journal of the American
   Statistical Association, 102(477), 359-378.
   https://sites.stat.washington.edu/raftery/Research/PDF/Gneiting2007jasa.pdf [high]

9. Merkle, E. C., Steyvers, M., Mellers, B. A., & Tetlock, P. E.
   (2017). "A Neglected Dimension of Good Forecasting Judgment: The
   Questions We Choose Also Matter." International Journal of
   Forecasting, 33(4), 817-832.
   https://doi.org/10.1016/j.ijforecast.2017.04.002 [high]

10. Karger, E., Bastani, H., Chen, Y.-H., Jacobs, Z., Halawi, D.,
    Zhang, F., & Tetlock, P. E. (2025). "ForecastBench: A Dynamic
    Benchmark of AI Forecasting Capabilities." International Conference
    on Learning Representations.
    https://arxiv.org/abs/2409.19839 [high]

11. Bosse, N. I., Muehlbacher, P., Wildman, J., Phillips, L., &
    Schwarz, D. (2026). "Automating Forecasting Question Generation and
    Resolution for AI Evaluation." ICLR 2026 Workshop on AI for
    Mechanism Design and Strategic Decision Making.
    https://arxiv.org/abs/2601.22444 [medium]

12. McCaslin, T., Rosenberg, J., Karger, E., Morris, A., Hickman, M.,
    Kuusela, O., Glover, S., Jacobs, Z., & Tetlock, P. E. (2024).
    "Conditional Trees: A Method for Generating Informative Questions
    About Complex Topics." Forecasting Research Institute Working Paper 3.
    https://forecastingresearch.org/pdf/ai-conditional-trees.pdf [medium]

13. Polymarket. "Resolution." Official platform documentation.
    https://docs.polymarket.com/concepts/resolution [high]

14. Brier, G. W. (1950). "Verification of Forecasts Expressed in Terms
    of Probability." Monthly Weather Review, 78(1), 1-3.
    https://journals.ametsoc.org/view/journals/mwre/78/1/1520-0493_1950_078_0001_vofeit_2_0_co_2.xml [high]

## See Also

- `library/probabilistic-thinking-forecasting/superforecasting.md` --
  tournament evidence on calibration, updating, and forecast skill that
  depends on well-specified questions.
- `library/probabilistic-thinking-forecasting/prediction-markets.md` --
  market mechanisms whose prices and payouts depend on event-contract
  definitions and settlement rules.
- `library/probabilistic-thinking-forecasting/fermi-estimation-and-decomposition.md`
  -- methods for breaking a difficult forecast into tractable components
  without hiding assumptions.
- `library/probabilistic-thinking-forecasting/calibration-and-overconfidence.md`
  -- why resolved question sets and proper feedback are necessary to test
  whether stated probabilities match outcomes.
- `library/probabilistic-thinking-forecasting/base-rate-neglect.md` --
  reference-class selection and prior probabilities used before
  case-specific evidence is incorporated.