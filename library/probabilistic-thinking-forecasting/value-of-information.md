---
name: value-of-information
id: 20261001T000534Z
tier: library-topic
domain: probabilistic-thinking-forecasting
author: Librarian
tags: [value-of-information, decision-analysis, evpi, evsi, bayesian-updating, experimental-design, optimal-stopping]
links: [library/probabilistic-thinking-forecasting/expected-value-decision-trees.md, library/probabilistic-thinking-forecasting/bayesian-reasoning.md, library/probabilistic-thinking-forecasting/forecast-question-design.md, library/probabilistic-thinking-forecasting/fermi-estimation-and-decomposition.md, library/probabilistic-thinking-forecasting/communicating-forecast-uncertainty.md]
---

# Value of Information -- More Evidence Is Worth Buying Only When It Can Improve a Decision

Value-of-information analysis asks how much better a decision could become if specified uncertainty were reduced before action. It values evidence by the expected improvement in consequences, not by data volume, statistical significance, or uncertainty reduction alone, and then compares that improvement with the monetary, temporal, operational, and opportunity costs of learning.[3][5][6][12]

## Background

Claude Shannon's 1948 theory made information measurable without requiring a judgment about what a message means or what follows from it. Entropy measures uncertainty in a probability distribution, conditional entropy measures uncertainty remaining after another variable is known, and related quantities describe transmission and coding limits.[1] This abstraction was essential for communication engineering, but it deliberately separated probability structure from consequences. A bit about a harmless event and a bit about a catastrophic event can have the same Shannon quantity even though they matter very differently to a decision-maker.

Dennis Lindley connected Bayesian learning to information measurement in 1956. His measure compared prior uncertainty about a parameter with posterior uncertainty expected after an experiment, and he applied it to experimental design where the objective was gaining knowledge about the world rather than choosing an action.[2] Ronald Howard's 1966 information-value theory drew the decision boundary more sharply: probabilities alone cannot establish an uncertainty's importance because value also depends on available actions and their consequences. Howard therefore joined probability and economic consequence in one model and showed that the value of resolving several uncertainties need not equal the sum of resolving each one separately.[3]

Modern value-of-information analysis inherits that decision-theoretic structure. A model specifies actions, uncertain states or parameters, information that may be observed, and utility or loss for each action-state combination. The decision-maker first chooses the action with the largest expected utility under current knowledge. Perfect or sample information has value only to the extent that a later observation changes which action is chosen, changes when it is chosen, or changes the exposure attached to it.[3][5][6] Information that substantially changes beliefs can have zero decision value when every posterior still recommends the same action; a small belief change can have high value when it crosses a consequential decision boundary.

Bayesian experimental design places experiment selection inside this framework. A design determines the distribution of possible observations; the prior and likelihood determine how each observation would update belief; and a utility function states what the experiment is trying to accomplish. Chaloner and Verdinelli's review presents Bayesian design as a decision problem and shows that optimal designs change when the prior or utility changes.[4] The implication is structural: there is no universally most informative experiment independent of the target, prior, downstream action, and objective.

Health technology assessment developed a particularly explicit applied vocabulary. The ISPOR task force distinguishes the expected value of perfect information, the expected value of partial perfect information, the expected value of sample information, and the expected net benefit of sampling. Its workflow begins by constructing and parameterizing a decision model, propagating parameter uncertainty, and identifying the currently preferred action; only then does it ask whether more evidence is potentially worthwhile and which study design has the largest expected net benefit.[5][6] This sequence prevents a familiar inversion in which researchers select a study first and search afterward for a decision it might inform.

The framework is broader than health research. The U.S. Geological Survey describes prediction as estimating the consequences of alternative actions relative to objectives and states that the value of filling a knowledge gap depends on how much the reduced uncertainty improves the decision outcome.[12] In investment timing, Bernanke modeled an irreversible commitment under arriving information and showed that committing early must be weighed against the expected value of learning while waiting.[10] In artificial intelligence, rational metareasoning treats a computation as an information-producing action whose expected improvement in the external decision is offset by the delay and resources it consumes.[9] These applications differ in units, horizons, and mechanisms, but they share the same comparison: act with current information versus pay or wait for information and then act conditionally.

Value of information is not the same as statistical power. A conventional power calculation chooses a sample size to control Type I and Type II error for a specified hypothesis, effect size, and variance. It does not automatically value the consequences of a wrong action, the number of people affected by the decision, alternative study endpoints, research cost, implementation, or delay.[15][16] EVSI instead asks how a proposed study's complete distribution of possible data would change the selected action and reduce expected decision loss. Power and precision remain relevant design properties, but they answer statistical questions inside a larger decision problem.

The scope boundary is equally important. Pure information theory asks about uncertainty, dependence, coding, and transmission; formal probability and statistical inference establish how evidence changes distributions; value-of-information analysis asks whether that change is worth acquiring for a particular choice. Portfolio construction, clinical treatment, engineering design, and computational control require their own domain models. The contribution here is the forecasting and decision framework that links uncertain evidence to an action before the action becomes irreversible.

## Core Concepts

### The Current Decision Is the Baseline

Let `d` denote an available decision, `theta` an uncertain state or vector of parameters, and `U(d, theta)` the utility produced by taking decision `d` when `theta` obtains. Under current information, the decision rule is:

`current value = max_d E_theta[U(d, theta)]`

The maximization occurs after expected utility is calculated for each action. This ordering matters. The decision-maker must select one action under current uncertainty rather than select a different action for every unknown state. The selected action is the baseline against which information is valued.[5][6]

The model can use money, net health benefit, lives, reliability, service level, forecast-user utility, or another coherent value measure. A risk-neutral monetary analysis can use expected money directly. A risk-sensitive decision requires a utility function or loss function that represents the relevant preferences and constraints. Howard's information-value argument and later decision-analysis research both make consequences indispensable: the same probability signal can have different values under different payoffs.[3][14]

The author's synthesis is that a valid baseline record needs five items: the action set, the uncertain state or parameter set, the current joint distribution, the utility or loss function, and the current maximizing action. Omitting any item makes later claims about information value ambiguous. A probability distribution without actions cannot say what should change; an action without utilities cannot say whether the change is better; a utility table without a joint distribution cannot say how often each consequence is expected.[3][5][6]

### Expected Value of Perfect Information

Perfect information reveals the relevant state before the decision is chosen. Its expected value is:

`EVPI = E_theta[max_d U(d, theta)] - max_d E_theta[U(d, theta)]`

The first term permits a state-contingent action because `theta` is known before choice. The second term is the best action under current uncertainty. EVPI is also the expected opportunity loss from making the current decision when another action would have been better in some states.[5][6] Under the model and a common utility scale, free perfect information cannot reduce expected utility because the decision-maker can always ignore it and take the current action.

EVPI is an upper bound, not a forecast that perfect knowledge can actually be purchased. If EVPI is smaller than the full cost of any feasible research program, that research cannot be justified solely by its informational benefit under the modeled decision.[5][6] A large EVPI says that current uncertainty has material decision consequences; it does not identify which parameter matters, which study should be conducted, or whether the model includes the relevant uncertainty.

A constructed example shows the mechanics. Suppose launching a product yields 100 units if demand is high and loses 40 units if demand is low; not launching yields zero. With prior probability 0.40 for high demand, launching has current expected value `0.40 x 100 + 0.60 x (-40) = 16`, so launch is preferred. Perfect information would lead to launch only when demand is high, producing expected value `0.40 x 100 + 0.60 x 0 = 40`; EVPI is therefore 24. These are the author's illustrative calculations, not empirical estimates. They show that perfect information is worth avoiding the low-demand launch, not merely knowing demand more accurately.

### Partial Perfect Information Locates Decision-Critical Uncertainty

Expected value of partial perfect information, or EVPPI, reveals one parameter or parameter group while leaving the rest uncertain. The decision is then optimized conditional on the revealed component and averaged over its current distribution. EVPPI identifies which uncertainty can change the decision enough to matter and sets an upper bound on the value of any feasible study that informs only that component.[5][6]

Partial information is not generally additive. Two parameters can be substitutes, complements, or jointly decisive. Learning either one alone may leave the same action optimal, while learning both could cross the decision boundary; alternatively, either one may resolve nearly the same decision uncertainty, so summing their separate values double counts the benefit. Howard explicitly noted that jointly resolving independent uncertainties can have a value different from the sum of resolving them separately because the action rule links them through consequences.[3]

The author's synthesis is to organize EVPPI around researchable groups rather than spreadsheet cells. A demand study may jointly inform market size, conversion, and retention; an engineering test may jointly inform failure rate and degradation; an investment research task may jointly inform margins and reinvestment needs. Grouping should follow the data-generating process and prospective study, because a parameter ranking detached from feasible evidence can misdirect research.[5][6]

### Expected Value of Sample Information

Perfect information is a benchmark; real studies produce noisy data. Let `X` denote a prospective study result with predictive distribution under the current model. After observing `X`, Bayes' theorem gives a posterior distribution for `theta`, and the decision-maker chooses the action with the highest posterior expected utility. Before collecting the data, every possible result must be averaged over its predictive probability:

`EVSI = E_X[max_d E[U(d, theta) | X]] - max_d E[U(d, theta)]`

This is preposterior analysis: it evaluates a posterior-guided decision before the posterior data exist.[6] EVSI depends on the full study design, including sample size, measurement process, endpoints, follow-up, missingness, bias, and the relation between observations and decision parameters. A study can be statistically precise about an outcome that does not change the action and therefore have little decision value.

Return to the constructed launch example. Suppose a market test is positive with probability 0.80 when demand is high and 0.30 when demand is low. The predictive probability of a positive test is `0.40 x 0.80 + 0.60 x 0.30 = 0.50`. Bayes' theorem gives posterior high-demand probability 0.64 after a positive test and 0.16 after a negative test. Launching after a positive result has expected value 49.6; launching after a negative result has expected value -17.6, so the conditional policy is launch after positive and do not launch after negative. The expected value with the test is 24.8 and EVSI is 8.8. These are the author's illustrative calculations. The test is worth at most 8.8 units before considering delay, implementation, or financing, even though its perfect-information upper bound is 24.

Under a common model, a study that informs only a parameter group normally satisfies `EVSI <= EVPPI <= EVPI` because sample data leave residual uncertainty, partial perfect information resolves only a subset, and perfect information resolves all modeled uncertainty.[6] The inequality is a model check, not a statement that more data are always socially better. Research can have harms, privacy costs, participant burden, delays, and implementation failures that enter only after gross information value is converted to net value.

### Expected Net Benefit of Sampling

Expected net benefit of sampling subtracts the expected cost of the study from the population value of sample information:

`ENBS = population EVSI - expected research cost`

Population EVSI scales per-person or per-decision gains by the number of future decisions affected over the relevant horizon, with discounting where appropriate.[5][6][7] Research cost should include fixed setup, per-observation expense, analysis, governance, participant burden when represented in the objective, and any decision consequences of waiting. If a result will be implemented slowly or incompletely, the affected population and realized improvement should be adjusted rather than assuming immediate universal adoption.[5]

The optimal design maximizes ENBS, not EVSI alone. Larger studies generally reduce more uncertainty, but their marginal decision benefit can diminish while costs continue to rise. A smaller study can have greater net value if it resolves the action boundary sufficiently; a larger study can be justified when small errors affect many people or when the relevant decision is highly consequential.[6][15] This is why a fixed power convention and a value-based sample-size calculation can recommend different designs.

The author's synthesis is that gross value, acquisition cost, and delay cost should remain separate fields. Combining them prematurely makes it difficult to see whether a study fails because it is uninformative, expensive, slow, or attached to a decision that will be implemented poorly. Separate fields also support redesign: a cheaper measurement, earlier endpoint, staged rollout, or narrower target population may turn negative ENBS positive without changing the underlying scientific question.[5][6][11]

### Decision Relevance Differs From Information Quantity

Shannon entropy and mutual information quantify probability structure without requiring an action or payoff.[1] Lindley's experimental-information measure uses expected prior-to-posterior uncertainty reduction and is suitable when learning itself is the stated objective.[2] Decision value asks a different question: how much does the signal improve the best available action under a utility model?[3] Neither quantity invalidates the other. They optimize different objectives.

A highly informative observation can be decision-irrelevant. If every possible posterior leaves the same treatment, forecast response, or investment action optimal, the gross decision value is zero even though posterior entropy falls. Conversely, a binary test with modest information can be valuable when it separates cases just above and below a treatment or commitment threshold. The National Academies' diagnostic-testing chapter makes this logic explicit: a test is useful when it can move posttest disease probability across the threshold that changes treatment, while the threshold itself depends on test performance, treatment benefits and harms, and test cost.[8]

Forecast skill and forecast value are likewise distinct. Laugesen and colleagues model forecast value through expected utility for specific water-management decisions and show that the result depends on decision type, utility, risk attitude, and the baseline forecast, not only on conventional forecast verification.[13] A more accurate forecast may add little value away from action thresholds; a modest improvement in a costly tail can matter greatly. The author's synthesis is to preserve both layers: score probability quality with proper forecast metrics, then evaluate decision value with explicit actions and consequences.

### Priors, Utilities, and Models Govern the Result

EVSI requires a predictive distribution for data and a posterior update after each possible result. The prior therefore affects which results are expected and how strongly they change belief; the likelihood affects how diagnostic the study is; and the utility function affects which belief changes cross the action boundary.[4][6] Prior sensitivity is especially important with small samples, weak identification, correlated parameters, or disputed reference classes. Utility sensitivity matters when consequences are asymmetric, risk tolerance is uncertain, or multiple stakeholders bear different costs.

Expected utility increase is not the only monetary expression of information value. Abbas and Hazen distinguish expected utility increase from the buying price, the maximum amount a decision-maker would pay for information while preserving indifference. They show that rankings can diverge across decision problems when risk attitude matters, so a utility-scale gain should not automatically be reported as a transferable cash price.[14] The safe practice is to state the utility model, initial wealth or resource context when relevant, valuation measure, and sensitivity range.

Model uncertainty is a separate boundary. Standard parameter VOI can be numerically precise while omitting a live action, state, mechanism, or structural model. The ISPOR analytical report notes that methods for structural uncertainty are less developed than methods for parameter uncertainty.[6] The author's synthesis is to treat an omitted plausible model as an unresolved candidate, not assign it implicit probability zero. Scenario analysis, alternative model structures, and explicit model-improvement value can complement parameter VOI when the uncertainty is about the map rather than a number on the map.

### Delay, Irreversibility, and Stopping Turn Information Into a Dynamic Choice

Information has timing. Waiting can produce a better decision, but it can also forgo current benefits, allow a competitor to act, increase costs, expose people to an inferior status quo, or make the eventual action infeasible. Bernanke's irreversible-investment model states the rule in dynamic terms: commit when the cost of deferring exceeds the expected value of information gained by waiting.[10] The option to learn is especially valuable when commitment is difficult to reverse and later evidence can still change the action.

Sequential studies add repeated choices: stop and act, continue the current experiment, or select a different experiment. Flight and colleagues apply EVSI and ENBS to fixed and group-sequential clinical-trial designs, including alternative interim-analysis schedules and stopping rules.[11] Rational metareasoning applies the same structure inside an agent. A computation can improve the external action, but it consumes time and resources; the controller should continue reasoning only while expected improvement exceeds computational and delay cost.[9]

The author's synthesis is a one-step stopping rule for practical use: continue gathering evidence only when the expected net value of the next feasible information action is positive after acquisition cost, delay, and the possibility of later continuation are represented. This is myopic unless future options are included; high-stakes sequential problems require backward induction or dynamic programming. Still, it is superior to stopping at an arbitrary confidence level because it asks whether another observation can improve the decision enough to pay for itself.[9][10][11]

## Evidence

### Foundational Results Establish Two Different Meanings of Information

Shannon's paper derives entropy from the probabilities of possible source events and uses it to characterize communication and coding problems.[1] Its method deliberately abstracts from consequences. Lindley's 1956 paper starts from a prior distribution over parameters, measures information expected from an experiment through Bayesian uncertainty reduction, and applies the measure to designs whose purpose is knowledge rather than a downstream action.[2] Howard's 1966 paper then constructs information value from both probabilities and consequences and argues that probabilistic information content alone cannot represent importance to a decision-maker.[3]

These are mathematical and conceptual results rather than field experiments. Their joint evidential contribution is a boundary test. Entropy reduction can rank experiments for learning under an information objective, while expected utility improvement can rank observations for action under a decision objective. The rankings need not agree because the latter includes actions and consequences that the former intentionally omits.[1][2][3] This difference supports the candidate's central claim: information quantity and decision relevance are distinct objects.

### Bayesian Experimental Design Makes the Objective Explicit

Chaloner and Verdinelli reviewed Bayesian experimental design through a decision-theoretic framework spanning linear, nonlinear, logistic, and hierarchical problems. Their abstract and synthesis state that design criteria can be treated coherently through utility functions and that design solutions change when priors or utilities are changed to represent the experiment's specific structure.[4] The method evaluates a design before data collection by averaging utility over possible parameters and observations.

The evidence is methodological rather than a universal performance estimate. It establishes that an "optimal experiment" is conditional on a prior, sampling model, and utility. It does not show that a selected prior is correct or that a utility fully represents stakeholder values. The practical implication is sensitivity analysis: if reasonable priors or utility functions select different experiments, that disagreement is part of the decision rather than a nuisance to hide.[4][6]

### Health Technology Assessment Supplies an Operational Pipeline

The two 2020 ISPOR task-force reports synthesize value-of-information methods for research decisions. Report 1 defines EVPI as the expected cost of current uncertainty, uses EVPPI to identify parameter groups where research may matter, and uses EVSI and ENBS to compare feasible studies with their costs.[5] Report 2 provides formulas and algorithms for EVPI, EVPPI, EVSI, and ENBS, including sampling-based computation when analytic solutions are unavailable.[6] Both reports require the decision problem and probabilistic model to be established before research value is calculated.

The task-force evidence is a professional good-practice synthesis, not a randomized test that VOI always improves policy. Its strength is procedural specificity: current action, parameter uncertainty, perfect-information bound, study-specific update, population scaling, and research cost are separate quantities.[5][6] Its limits are also explicit. Results depend on the model, risk-neutral formulations are common, structural uncertainty is harder, and implementation and time horizon can materially change population value.[5][6][15]

Kunst and colleagues reviewed four model-based EVSI computation methods and describe EVSI as the expected reduction in expected loss from a proposed study. They show how several approximation methods can evaluate alternative sample sizes without the full cost of nested simulation, while noting method-specific computational limits and the common assumption of risk-neutral expected-value choice.[15] This evidence supports feasibility of study-design comparison, not automatic validity of any input model.

### Clinical Testing Demonstrates the Action-Threshold Mechanism

The National Academies' diagnostic-technology assessment derives clinical testing from pretest probability, test sensitivity and false-positive rate, treatment consequences, and test burden. Bayes' theorem maps results to posttest probabilities, while expected utility determines whether to do nothing, test, or treat. The chapter states that testing is useful when a possible result can move probability across the treatment threshold and describes lower test and upper test-treatment thresholds.[8]

This framework provides a concrete case in which more diagnostic accuracy is not automatically valuable. A test can strongly change probability yet leave the same action optimal, or it can have high decision value in an intermediate probability region where its result determines treatment.[8] The model's limits are consequential: test characteristics may vary across populations, utilities can be difficult to elicit, and unmodeled harms can shift thresholds. Those limits reinforce rather than weaken the VOI requirement to state the population, likelihood, action set, and consequence model.

### Sequential Trial Design Shows That Stopping Rules Have Economic Consequences

Flight, Julious, Brennan, and Todd compared five proposed full-scale trial designs in a hypothetical case study based on pilot data: one fixed design and group-sequential designs using Pocock or O'Brien-Fleming rules with two or five analyses. They simulated the designs, estimated EVSI and sampling cost, and compared ENBS. In their case study, the O'Brien-Fleming design with two analyses had the highest EVSI and ENBS.[11]

The result is not a universal ranking of stopping rules. It depends on the disease model, endpoints, prior evidence, costs, interim schedule, and relationship between clinical and economic outcomes. Its evidential value is the demonstrated comparison method: a stopping rule changes expected sample size, analysis cost, bias adjustment, and residual decision uncertainty, so it should be evaluated as a decision design rather than selected from statistical convention alone.[11]

### Forecasting Evidence Separates Accuracy From User Value

Laugesen, Thyer, McInerney, and Kavetski developed relative utility value for probabilistic subseasonal streamflow forecasts. Their method evaluates forecast-informed decisions against a reference baseline and perfect information using expected utility, and their case studies vary decision type and risk attitude.[13] They report that fixed probability-threshold use can fail to extract maximum value and that optimization using the full forecast distribution can perform better for the modeled users.

This is applied evidence from one forecast domain, not proof that every probabilistic forecast should be used. The study states that value depends on the economic model, utility function, baseline, and real decision context.[13] It supports a bounded conclusion: forecast verification and decision value complement each other, and a forecast's value cannot be inferred from accuracy alone without specifying how a user acts.

### Investment and Computation Expose the Cost of Waiting

Bernanke's model studies irreversible investment when information about returns arrives over time. The derived decision rule compares the cost of delay with the probability and magnitude of a commitment mistake that later information could reveal.[10] The result formalizes an option to wait: positive expected project value is not sufficient for immediate commitment when delay preserves a valuable chance to learn. Its assumptions include irreversible investment, a specified information process, and a dynamic model; different competitive or timing conditions can reduce the value of waiting.

Russell's metareasoning synthesis treats computation as an internal information action. Given a model of how a computation may change beliefs about external actions, the controller estimates improvement in object-level utility and subtracts delay or computational cost; it can then choose which computation to perform and when to act.[9] The evidence is theoretical and architectural. It supports human-AI workflow design in which searches, model calls, simulations, and human reviews are selected for expected decision improvement rather than accumulated without a stopping rule.

### Statistical Power Does Not Supply Decision Value by Itself

Bacchetti analyzes conventional sample-size rules based on significance and power and argues that a blanket 80 percent threshold does not create a meaningful boundary between valuable and valueless studies. He presents value-of-information methods as an alternative that compares projected value and cost across sample sizes.[16] Kunst and colleagues make the complementary point operationally: conventional power calculations manage test errors for a selected endpoint, while EVSI values how data reduce expected loss in the downstream decision and can optimize study size across the decision model.[15]

These sources do not imply that power, Type I error, or precision can be ignored. A biased or uninformative study remains defective, and regulatory settings may require specified error control. The supported conclusion is that statistical operating characteristics and decision value answer different questions. A defensible design can report both, with VOI supplying the bridge from evidence quality to consequences.[15][16]

## Implications

### Use a Decision-First Research Workflow

The author's synthesis from the decision-analysis and experimental-design evidence is a nine-step workflow.[4][5][6][12]

1. Define the decision, not merely the topic. List feasible actions, the decision-maker, horizon, and what can still be changed.
2. Define uncertainty. State the uncertain states or parameters, their joint distribution, provenance, and material structural alternatives.
3. Define consequences. Build a utility or loss model that includes asymmetric harms, opportunity costs, constraints, and who bears them.
4. Compute the current action. Record expected utility for every action and the margin between the best and alternatives.
5. Calculate EVPI. Use it as the maximum gross value of resolving all modeled uncertainty and as a screen against obviously uneconomic research.
6. Calculate EVPPI for researchable groups. Identify uncertainty that can both change the decision and be addressed by a plausible evidence process.
7. Specify candidate information actions. For each test, study, search, simulation, expert review, or computation, model the distribution of results and Bayesian update.
8. Calculate EVSI and net value. Subtract acquisition, delay, implementation, and opportunity costs; scale only to the population and time horizon actually affected.
9. Choose, stage, stop, or act. Select the information action with the highest positive net value, preserve the option to revise, and stop when continuation value no longer exceeds its full cost.

This workflow prevents three category errors. It does not confuse uncertainty with decision uncertainty, because EVPI depends on action regret rather than posterior width alone. It does not confuse a parameter with a feasible study, because EVPPI is only an upper bound while EVSI models actual data. It does not confuse gross information value with net research value, because ENBS includes cost and timing.[5][6]

### For Medicine and Public Decisions

A diagnostic test should be ordered because its possible results can change patient management enough to justify its harms and costs, not because it is accurate in isolation. The threshold model combines pretest probability, likelihood ratios, treatment consequences, and test burden to identify regions where doing nothing, testing, or treating is optimal.[8] The author's synthesis is to attach every proposed test to a conditional action table: what action follows each result, how that action changes outcomes, and whether any plausible result crosses the current threshold.

Research funders can apply the same logic at population scale. EVPI screens whether all current decision uncertainty is worth resolving; EVPPI identifies outcomes or mechanisms worth targeting; EVSI compares sample size, follow-up, endpoints, and adaptive rules; ENBS ranks designs after cost.[5][6][11] The model should include the number of future patients affected and the period during which the result remains relevant. A technically excellent study can have low population value if practice will change before completion, only a small population remains, or implementation will be weak.[5]

Ethical and regulatory constraints remain gates rather than terms to trade away casually. Positive ENBS does not authorize a harmful study, and negative ENBS does not erase a legal evidence requirement. The decision model should represent participant harms where appropriate, but rights, consent, and mandatory standards can constrain the feasible design set before optimization. VOI improves choices within that set; it does not convert every obligation into a price.

### For Forecasting and Operations

Forecast producers should evaluate which uncertainty affects an operational choice. A warehouse manager may care about the probability demand exceeds capacity; an emergency manager may care about a low tail because the loss is asymmetric; a reservoir operator may need a full distribution because release amount is continuous. The same forecast can have different values for these users because actions, baselines, and utility functions differ.[12][13]

The author's synthesis is to pair each forecast product with a user decision model. Record the baseline action without the forecast, the action rule with the forecast, the cost of a false alarm, the loss from a miss, and any constraints on response. Evaluate proper forecast scores separately from realized utility. If a model improvement lowers average score but never changes an action, it has no measured value for that user under the current rule. If it improves a critical tail and prevents rare large losses, its decision value may exceed its average-score change.[13]

Operations teams can use EVPPI as a research-priority map. If uncertainty in demand dominates decision regret, improve demand sensing; if equipment failure dominates, fund condition monitoring; if supplier lead time does not change the current contingency policy, more precise lead-time data may have little immediate value. Dependence matters: several dashboards sourced from one system are not independent information, and jointly resolving interacting bottlenecks can be worth more or less than the sum of separate estimates.[3]

Sequential operations require explicit stopping. Continue inspection, simulation, or sampling while the expected gain from the next stage exceeds its cost and delay. Use backward induction when later stages depend on earlier findings. A fixed confidence threshold can be wasteful when the action is already robust, and insufficient when an irreversible downside remains near a decision boundary.[9][11]

### For Investing and Capital Allocation

The author's synthesis is to treat research as part of the investment decision rather than as a ritual preceding valuation. Begin with the actions available now: buy, sell, hold, size differently, hedge, wait, or decline. Define uncertain business states, not only point estimates, and map each state to cash flows, financing needs, and permanent-loss consequences. Then ask which evidence could change the action or position size.[3][10]

EVPI places an upper bound on what perfect resolution of modeled uncertainty could be worth. EVPPI can separate decision-critical groups such as unit economics, balance-sheet resilience, regulatory outcome, competitive response, or reinvestment runway. EVSI can compare a channel check, technical expert, additional filing review, customer survey, small position that creates learning access, or simply waiting for the next disclosure. The research budget should be below net decision value, not a fixed percentage of capital.[5][6]

Irreversibility changes the analysis. Buying a liquid security is often reversible at a price, but concentrated positions, illiquid assets, control investments, reputation, taxes, financing, and lost alternatives can make reversal costly. Waiting preserves information value but sacrifices dividends, price opportunity, strategic access, or time for compounding. Bernanke's rule provides the mental model: commit when the full cost of waiting exceeds the expected value of mistakes that waiting could prevent.[10]

Utility sensitivity matters for investors. A fund facing redemptions, leverage, or a survival constraint should not translate expected utility gains into cash values as though it were risk neutral. Abbas and Hazen show that expected utility increase and buying price can rank information differently across decision problems under risk-sensitive utility.[14] The author's synthesis is to report a risk-neutral information value, a survival-constrained case, and sensitivity to priors and downside utility when the result can change position size.

The worst investment use is to pay for information that cannot change the action because identity, sunk cost, or mandate has already fixed the conclusion. A disconfirming-evidence test should be specified before purchase: which result would reduce, reverse, or postpone commitment? If no credible result can do so, the activity is thesis decoration rather than information acquisition.

### For Human-AI Workflows

A human-AI system faces a portfolio of information actions: web search, database query, code execution, simulation, another model call, specialist review, or human escalation. Each action has expected benefit, monetary cost, latency, error risk, and dependence on evidence already collected. Rational metareasoning supplies the governing analogy: choose computations for expected improvement in the external action and stop when improvement no longer exceeds cost and delay.[9]

The author's synthesis is to attach a value-of-computation record to consequential workflows. The record should state the external decision, current best action, uncertainty that could reverse it, candidate computation, possible outputs, expected update, cost, latency, and stopping rule. Cheap verification should be prioritized when it can expose a catastrophic error; expensive broad search should be rejected when every plausible result leaves the action unchanged.

Agreement among models should not be valued by vote count alone. Models may share training data, prompts, retrieval sources, or failure modes. The relevant question is whether an additional model supplies evidence with a different likelihood under the live hypotheses and whether that evidence changes the action. Howard's nonadditivity result applies directly: resolving several uncertainties or consulting several sources can be complementary or redundant even when their outputs look independent.[3]

Human review is likewise not automatically valuable. It is most valuable where human context, authority, accountability, or error detection can change a consequential action. It is wasteful when used as an unconditional final step on low-stakes, reversible outputs whose automated decision is already robust. The reversible design is tiered: automate bounded low-loss cases, sample them for calibration, escalate near decision boundaries or under model disagreement, and audit rare high-consequence outcomes.

### Boundaries, Failure Modes, and Stopping Conditions

VOI is only as sound as its decision model. A precise calculation can fail through a missing action, wrong prior, misspecified likelihood, correlated evidence counted twice, omitted implementation friction, false population scaling, or a utility function that hides who bears the harm.[4][5][6] Sensitivity analysis should vary priors, utilities, time horizon, uptake, research cost, and structural alternatives. If the preferred information action changes, report the switch point rather than one authoritative number.

Perfect information is a conceptual bound, not an attainable promise. Sample information rarely eliminates uncertainty, and its realized result can leave the decision unchanged. EVSI is an expectation over possible data, so a study that produces no decision change ex post was not necessarily irrational ex ante. Conversely, one dramatic useful result does not prove the study design had positive expected net value. Evaluation must preserve the pre-study model and compare repeated decisions where possible.[5][6]

VOI should not reward delay indefinitely. Information can become stale, an opportunity can expire, and research can impose harm while the current inferior action continues. Dynamic problems require the value of acting now, learning, and preserving future options to be represented together.[9][10][11] The author's synthesis is that the terminal question is not "Do we know enough?" It is "Does the next feasible unit of evidence have positive expected net value for the action that remains available?"

The durable rule is simple. Quantify uncertainty when that improves understanding, but buy information only after identifying the decision it can change. Stop when the expected improvement in the action is no greater than the full cost of learning.

## Sources

1. Shannon, C. E. (1948). "A Mathematical Theory of Communication."
   Bell System Technical Journal, 27(3), 379-423 and 27(4), 623-656.
   https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
   [high]

2. Lindley, D. V. (1956). "On a Measure of the Information Provided by
   an Experiment." Annals of Mathematical Statistics, 27(4), 986-1005.
   https://doi.org/10.1214/aoms/1177728069 [high]

3. Howard, R. A. (1966). "Information Value Theory." IEEE Transactions
   on Systems Science and Cybernetics, 2(1), 22-26.
   https://doi.org/10.1109/TSSC.1966.300074 [high]

4. Chaloner, K., and Verdinelli, I. (1995). "Bayesian Experimental
   Design: A Review." Statistical Science, 10(3), 273-304.
   https://doi.org/10.1214/ss/1177009939 [high]

5. Fenwick, E., Steuten, L., Knies, S., et al. (2020). "Value of
   Information Analysis for Research Decisions - An Introduction:
   Report 1 of the ISPOR Value of Information Analysis Emerging Good
   Practices Task Force." Value in Health, 23(2), 139-150.
   https://doi.org/10.1016/j.jval.2020.01.001 [high]

6. Rothery, C., Strong, M., Koffijberg, H. E., et al. (2020). "Value of
   Information Analytical Methods: Report 2 of the ISPOR Value of
   Information Analysis Emerging Good Practices Task Force." Value in
   Health, 23(3), 277-286.
   https://pmc.ncbi.nlm.nih.gov/articles/PMC7373630/ [high]

7. Wilson, E. C. F. (2015). "A Practical Guide to Value of Information
   Analysis." PharmacoEconomics, 33(2), 105-121.
   https://doi.org/10.1007/s40273-014-0219-x [high]

8. Institute of Medicine. (1989). "The Use of Diagnostic Tests: A
   Probabilistic Approach." In Assessment of Diagnostic Technology in
   Health Care. National Academies Press.
   https://www.ncbi.nlm.nih.gov/books/NBK235178/ [high]

9. Russell, S. J. (1999). "Metareasoning." In The MIT Encyclopedia of
   the Cognitive Sciences, 539-541. MIT Press.
   https://aima.eecs.berkeley.edu/~russell/papers/mitecs-metareasoning.pdf
   [high]

10. Bernanke, B. S. (1983). "Irreversibility, Uncertainty, and Cyclical
    Investment." Quarterly Journal of Economics, 98(1), 85-106.
    https://doi.org/10.2307/1885568 [high]

11. Flight, L., Julious, S., Brennan, A., and Todd, S. (2022). "Expected
    Value of Sample Information to Guide the Design of Group Sequential
    Clinical Trials." Medical Decision Making, 42(4), 461-473.
    https://doi.org/10.1177/0272989X211045036 [high]

12. Smith, D. R. (2020). "Introduction to Prediction and the Value of
    Information." In Structured Decision Making: Case Studies in Natural
    Resource Management, 189-195. Johns Hopkins University Press.
    https://pubs.usgs.gov/publication/70211059 [high]

13. Laugesen, R., Thyer, M., McInerney, D., and Kavetski, D. (2023).
    "Flexible Forecast Value Metric Suitable for a Wide Range of
    Decisions: Application Using Probabilistic Subseasonal Streamflow
    Forecasts." Hydrology and Earth System Sciences, 27, 873-893.
    https://doi.org/10.5194/hess-27-873-2023 [high]

14. Abbas, A. E., and Hazen, G. B. (2025). "On the Value of Information
    Across Decision Problems." Decision Analysis, 22(1), 1-13.
    https://doi.org/10.1287/deca.2024.0187 [high]

15. Kunst, N. R., Wilson, E. C. F., Glynn, D., et al. (2020). "Computing
    the Expected Value of Sample Information Efficiently: Practical
    Guidance and Recommendations for Four Model-Based Methods." Value in
    Health, 23(6), 734-742.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC8183576/ [high]

16. Bacchetti, P. (2010). "Current Sample Size Conventions: Flaws,
    Harms, and Alternatives." BMC Medicine, 8, 17.
    https://doi.org/10.1186/1741-7015-8-17 [high]

## See Also

- `library/probabilistic-thinking-forecasting/expected-value-decision-trees.md`
  -- the action, probability, payoff, and rollback structure on which
  information value is calculated.
- `library/probabilistic-thinking-forecasting/bayesian-reasoning.md` --
  the prior, likelihood, posterior, and predictive distributions used to
  model sample information.
- `library/probabilistic-thinking-forecasting/forecast-question-design.md`
  -- the resolution contract and decision relevance required before a
  forecast or study can produce interpretable evidence.
- `library/probabilistic-thinking-forecasting/fermi-estimation-and-decomposition.md`
  -- a lower-cost way to expose decision-sensitive unknowns before formal
  VOI modeling.
- `library/probabilistic-thinking-forecasting/communicating-forecast-uncertainty.md`
  -- how uncertainty reaches users whose actions and consequences determine
  realized forecast value.
