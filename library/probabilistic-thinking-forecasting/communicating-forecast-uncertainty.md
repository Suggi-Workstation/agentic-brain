---
name: communicating-forecast-uncertainty
id: 20260929T060518Z
tier: library-topic
domain: probabilistic-thinking-forecasting
author: Librarian
tags: [forecast-uncertainty, probability-communication, prediction-intervals, fan-charts, ensemble-forecasts, decision-thresholds, numeracy, calibrated-language]
links: [library/probabilistic-thinking-forecasting/forecast-question-design.md, library/probabilistic-thinking-forecasting/calibration-and-overconfidence.md, library/probabilistic-thinking-forecasting/expected-value-decision-trees.md, library/probabilistic-thinking-forecasting/scenario-planning-and-analysis.md, library/probabilistic-thinking-forecasting/fermi-estimation-and-decomposition.md, library/probabilistic-thinking-forecasting/base-rate-neglect.md]
reviewed: 2026-10-01
---

# Forecast Uncertainty Is Useful Only When Its Meaning and Decision Consequences Are Explicit

Communicating forecast uncertainty means specifying what outcome is uncertain, over what horizon, under which assumptions, and how the stated probability or range should affect a decision. A numerical probability, verbal likelihood, prediction interval, fan chart, ensemble, or scenario can clarify the future only when the audience can connect the format to the event and its consequences; otherwise apparent precision can hide model limits, dependence, revisions, and unresolved unknowns.[1][2][3]

## Background

A forecast is an information-conditioned statement about a future outcome, not a promise that one value will occur. The information may be summarized as a point, an event probability, a set of quantiles, a predictive distribution, or a collection of conditional scenarios. Each summary suppresses part of the underlying uncertainty. A point forecast suppresses dispersion and tails. A range suppresses the shape of the distribution unless its coverage and construction are given. A verbal phrase suppresses numerical detail unless its intended scale is defined. A scenario can preserve causal structure while leaving relative likelihood unspecified. The communication problem is therefore not simply whether to disclose uncertainty, but which parts of it a user must see to make the intended decision.[1][8][12]

Operational weather forecasting made this problem concrete. The National Research Council documented that numerical probability-of-precipitation forecasts entered U.S. operations in 1965, while ensemble methods became practical tools for estimating forecast uncertainty by the early 1990s.[1] The World Meteorological Organization describes uncertainty as arising throughout an information chain: observations and models may be incomplete, a forecaster must interpret their output, a service must express that interpretation, and a user must interpret the message.[3] Leutbecher and Palmer explain the technical motivation for ensembles: imperfect initial-state estimates and imperfect models produce forecast errors whose growth depends on the evolving atmospheric flow, so uncertainty can change from case to case rather than being represented by one historical average.[9]

Economic and climate institutions developed other conventions. The Bank of England began using fan charts to show a central inflation projection together with widening probability bands; its 1998 explanation states that the earlier shaded range was based on the previous ten years of forecast errors and would ordinarily contain the outcome just over half of the time.[10] The Intergovernmental Panel on Climate Change developed calibrated terms such as "likely" and "very likely," while separating qualitative confidence in a finding from quantified likelihood.[2] These conventions were responses to real communication needs, but none is self-interpreting. A shaded band can be mistaken for a hard boundary, a scenario bundle for a probability distribution, and a familiar word for a shared numerical judgment.[2][6][8][10]

Several kinds of uncertainty can coexist in one forecast. Outcome variability concerns which value will occur even if the model is correctly specified. Parameter uncertainty concerns imperfectly known quantities inside the model. Model uncertainty concerns alternative structures, omitted mechanisms, and imperfect approximations. Measurement and baseline uncertainty concern the data used to initialize or estimate the system. Judgmental uncertainty concerns expert choices that cannot be derived mechanically. Communication uncertainty arises when the sender and receiver attach different meanings to the same term, number, range, color, or graphic. IPCC guidance specifically warns that experts tend to understate structural uncertainty and asks authors to state assumptions and provide a traceable account of evidence and agreement.[2] The WMO likewise distinguishes uncertainty in the science from uncertainty introduced by interpretation and language.[3]

The decision context determines which uncertainty matters. A farmer deciding whether to protect a crop, an emergency manager deciding whether to evacuate, and a central bank deciding whether to change policy can rationally take different actions after receiving the same probability because their costs, losses, timing constraints, and available alternatives differ.[1] The simple cost-loss model makes this consequence dependence explicit: if protective action costs C and avoids loss L, a user minimizes expected expense by acting when the event probability exceeds the user's C/L ratio.[15] A user with a lower cost relative to the avoidable loss should therefore act at a lower probability. The probability belongs to the forecast; the action threshold belongs to the user and the consequence structure. Combining them without disclosure turns a forecast into hidden advice.

Communication also has an audience constraint. Numerical probabilities can preserve distinctions that words blur, but low numeracy, denominator neglect, graph literacy, and framing can change how those numbers are used.[5][8][13] Verbal probability expressions are accessible and can convey the speaker's attitude or the direction of concern, but those pragmatic meanings may move interpretation away from the intended probability.[6][12] Graphics can make distributions visible, but a cone, band, or color gradient can be read as geography, confidence, density, severity, or a hard limit depending on design and prior expectations.[8] The correct response is not to retreat to a single deterministic number. It is to match the representation to the task, test interpretation, and retain the assumptions needed to audit the message.

Honest uncertainty is different from vagueness. Honest uncertainty defines the target, identifies known sources of error, quantifies what the evidence supports, labels what remains unquantified, and states the conditions under which the forecast should be revised.[1][2] Vagueness uses flexible words without a resolution rule or decision link. False precision uses extra digits, narrow ranges, or exact-looking probabilities unsupported by the evidence. The author's synthesis is that both failures remove accountability: vagueness prevents the claim from being tested, while false precision makes an under-specified model look more informative than it is.

## Core Concepts

### The forecast object must be specified before its uncertainty

A probability is incomplete unless it refers to a defined event. The event needs an outcome rule, population or system, geographic scope where relevant, time horizon, and evidence cutoff. "There is a 30 percent chance of disruption" is not operational until disruption, the affected system, the qualifying period, and the observation used to resolve the claim are specified. The existing forecast-question-design framework in this library treats these elements as a measurement contract because a later score depends on the same definitions that guide the original judgment. The National Research Council and IPCC guidance add a second requirement: state the assumptions and sources of uncertainty that condition the forecast.[1][2]

The conditioning set matters because forecast probabilities change with information. A probability issued before a new data release is not directly comparable with one issued afterward unless the vintages are identified. A projection conditional on current policy is different from an unconditional forecast of what policymakers will actually do. A weather forecast conditional on an ensemble system, initialization time, and model version is different from the probability implied by a later system. The author's synthesis is to place five items beside every headline forecast: target, horizon, information cutoff, conditioning assumptions, and version. This preserves the meaning of revisions instead of making each new number silently replace the previous claim.

The same discipline applies to dependencies. Probabilities for related events cannot always be added or multiplied as though the events were independent. Several scenario paths may share the same model, data, supplier, political assumption, or physical driver. An ensemble may sample only the sources of uncertainty that its construction represents.[9] IPCC guidance asks authors to consider structural uncertainty and conditional findings separately, especially when causes and effects carry different degrees of certainty.[2] The author's synthesis is that a communication should name material common drivers and say whether dependence is modeled, assumed, stress-tested, or unresolved.

### A point, probability, range, and interval answer different questions

A point forecast identifies one representative value, often a mean, median, mode, or selected central path. Those summaries can differ in a skewed distribution, so "best estimate" is ambiguous unless the statistic is named.[8][10] A binary event probability answers how likely a defined threshold event is. A quantile answers which value a specified fraction of the predictive distribution falls below. A prediction interval combines lower and upper quantiles to cover a stated share of future outcomes under the forecast model. A complete predictive distribution represents relative probability across the outcome space. These objects can be derived from one model, but they are not interchangeable.

An interval needs both a coverage level and an interpretation. An 80 percent prediction interval for a future outcome means that the model assigns 80 percent of predictive probability between its endpoints; it does not mean that every value inside is equally likely or that the outcome cannot fall outside.[8][12] It is also not the same as a confidence interval for an estimated parameter. A range without a coverage statement may instead be a sensitivity range, an expert-defined plausible range, a minimum-to-maximum envelope, or the spread of selected scenarios. Calling each of these an "uncertainty interval" conceals differences in construction and evidential status.[1][8][12]

Interval width is not a standalone measure of quality. A narrow interval can be useful if it is well calibrated and disastrous if it systematically misses. A very wide interval can achieve high coverage while providing little discrimination. Forecast evaluation therefore considers calibration or reliability together with sharpness or resolution: among forecasts that achieve the stated coverage, narrower informative distributions are preferred.[1][9] The author's synthesis is to report the central statistic, coverage level, interval type, method, and relevant backtest together, rather than letting a shaded band imply that all five are known.

### Numerical probabilities are precise in syntax, not automatically in evidence

A numerical probability makes differences explicit. The receiver can distinguish 20 percent from 40 percent, compare the forecast with a decision threshold, update an expected-value calculation, and later score repeated forecasts. Joslyn and LeClerc found that explicit numerical uncertainty improved weather-related decisions relative to deterministic formats in experimental tasks.[4] Grounds and Joslyn found that most participant groups benefited from probabilities, although extremely low numeracy constrained the benefit.[5] Numbers therefore support disciplined action, but they do not prove that the underlying estimate is accurate.

The number of displayed digits should match the information content. Reporting 63.27 percent can imply a degree of knowledge that expert judgment, sparse data, or model instability cannot support. IPCC guidance recommends a full distribution or probability range when sufficient information exists and warns against using a probability phrase merely to express lack of knowledge.[2] Teigen's review notes that numerical estimates can themselves be approximate, including probability ranges such as 60 to 80 percent.[12] The author's synthesis is to round to the smallest distinction that could change the decision and to use a probability range when disagreement, sampling error, or structural uncertainty makes a point probability misleading.

A number also needs a reference class. "A 10 percent chance" can be misunderstood when users do not know what set of comparable cases, time windows, or possible outcomes supports it. Gigerenzer and Edwards show that natural frequencies can make conditional risk information easier to understand by keeping a common denominator, such as seven affected people among 1,000 rather than several nested percentages.[13] Natural frequencies are especially useful when base rates and conditional evidence interact. They are less natural for a unique future event with no stable repeated reference class, where a subjective probability should be labeled as judgment rather than disguised as an observed frequency.

### Verbal likelihood scales need numerical anchors and contextual care

Words such as "possible," "unlikely," "likely," and "almost certain" are compact and work in speech, but listeners assign broad and differing numerical meanings to them.[6][12] Direction also matters. "A 30 percent chance of failure" and "a 70 percent chance of success" describe complements but can focus attention on different outcomes. Teigen's review finds that verbal expressions carry pragmatic information about source, valence, severity, and speaker attitude beyond their nominal probability.[12] This additional meaning can be useful in conversation, but it prevents a word from serving as a universal numerical code.

Calibrated lexicons reduce variation only if the audience sees and uses the mapping. The IPCC defines likelihood terms with probability ranges and treats confidence as a separate judgment based on evidence and agreement.[2] Budescu, Broomell, and Por tested sentences from an IPCC report and found that readers' spontaneous numerical interpretations did not consistently match the institutional scale; adding numerical boundaries to the verbal terms improved communication.[6] The practical rule is therefore not "numbers instead of words" in every medium. The author's synthesis is to pair the verbal label with its numerical range at the point of use, keep the wording and number directionally consistent, and reserve confidence language for evidential support rather than event probability.

Verbal uncertainty is especially weak when it becomes a substitute for omitted analysis. "There is some chance" can mean a small modeled probability, unresolved model disagreement, lack of data, or unwillingness to commit. Those states require different responses. A small modeled probability may trigger action when losses are severe. Model disagreement may call for robust strategies. Missing data may justify research. The author's synthesis is to follow every qualitative uncertainty statement with its source: variability, measurement, parameter, model, judgment, dependence, or ignorance.

### Fan charts and prediction bands display distributions but can hide construction

A fan chart places nested shaded bands around a central trajectory, usually widening with horizon. Darker or inner bands commonly represent more central portions of the predictive distribution, while outer bands add probability mass.[8][10] The format efficiently displays location, dispersion, horizon, and sometimes skewness. It can also move attention away from whether one point forecast was exactly right and toward the range of outcomes considered before the event.[10]

The visual does not reveal its own probability model. Bands may be based on historical forecast errors, model simulations, expert judgment, or a combination. They may be marginal intervals for each future date rather than a simultaneous statement that the entire future path will remain inside the fan. They may omit structural breaks and low-probability tails. The Bank of England's explanation is valuable because it states how the range was tied to historical errors and what frequency of containment it was intended to represent.[10] A fan chart without equivalent metadata risks becoming decoration.

Color and geometry also shape interpretation. Spiegelhalter, Pearson, and Short review how icon arrays, cones, densities, and fan charts interact with numeracy and perceptual heuristics.[8] A hurricane cone, for example, can be misread as the physical size or impact area of a storm rather than uncertainty about the track. A fan may be read as a hard feasible region even when outcomes outside it retain probability. The author's synthesis is to label the central statistic, each band's coverage, the horizon, the method, and the possibility of outcomes beyond the outer band directly on or beside the graphic.

### Ensembles represent sampled futures, not every possible future

An ensemble runs multiple forecast trajectories from perturbed initial conditions, different model formulations, or both. The collection can represent flow-dependent variation in forecast uncertainty that one deterministic run cannot show.[9] Event probabilities, quantiles, clusters, and scenario paths can be estimated from the members after appropriate calibration. The ensemble mean may be useful as a central summary, but it should not erase the member spread, multimodality, or tail-relevant clusters that motivated the ensemble.

An ensemble is finite and conditional on its design. Members may share biases, model structure, observations, or parameterizations. Raw member counts are not automatically calibrated probabilities, and a narrow spread can understate uncertainty if important error sources are absent.[9] The author's synthesis is to communicate what was varied, what remained common, the ensemble size, any post-processing, historical reliability, and known omitted sources. Showing selected members without that explanation can make a small computational sample look like an exhaustive set of futures.

Alternative scenarios solve a different problem. A scenario specifies a coherent set of assumptions and traces their consequences; it need not carry a probability.[2] Scenarios are useful when structural choices or deep uncertainty make a single predictive distribution contestable. They should not be plotted beside probabilistic intervals in a way that suggests equal likelihood, quantile status, or exhaustive coverage. The author's synthesis is to label each scenario with its assumptions and purpose, and to state explicitly whether it is probable, plausible, adverse, exploratory, or a sensitivity case.

### Decision thresholds connect uncertainty to asymmetric consequences

Forecast communication becomes actionable when it identifies the event probability or outcome quantile relevant to the decision. In a simple cost-loss setting, protective action is justified when the forecast probability exceeds the user's ratio of protection cost to avoidable loss.[15] Different users can therefore use one probability forecast differently without either user misunderstanding it. A deterministic warning collapses these varied thresholds into one institutional rule and can serve some users poorly.

Losses are often asymmetric. Underprediction of a flood, demand spike, liquidity need, or safety hazard may be far more costly than overprediction; in another setting, false alarms may erode scarce resources or compliance. The relevant central forecast may then be a decision-weighted quantile rather than the mean or median. The author must distinguish this action-oriented statistic from an unbiased descriptive center. The author's synthesis is to publish both when they differ: the predictive distribution describes belief, while the recommended threshold or action states the consequence rule.

Thresholds also expose why framing matters. A message focused on the chance of crossing the harmful threshold usually maps more directly to protective action than a complementary message about remaining below it. Joslyn and colleagues found that mismatch between wording and the decision goal increased errors in threshold tasks.[14] The author's synthesis is to express the event in the same direction as the action trigger, while also showing the complement when balanced interpretation matters.

### Revision is evidence, not an admission that the prior forecast was meaningless

Forecasts should change when new observations, model corrections, or assumption changes arrive. A revision record needs the prior distribution, new evidence, changed assumption or model, revised distribution, and resulting decision change. Without this record, users cannot distinguish evidence-based updating from arbitrary movement. IPCC guidance calls for traceable accounts of evidence and agreement, and WMO guidance treats interpretation and communication as explicit stages where uncertainty can enter.[2][3]

A changing central estimate and a changing uncertainty width carry different information. New evidence can move the center without reducing uncertainty, narrow uncertainty without moving the center, or reveal omitted structure that widens the range. A model-version change may make before-and-after numbers non-comparable. The author's synthesis is to preserve forecast vintages and decompose revisions into data, parameter, model, assumption, and judgment components where feasible.

Unknowns cannot always be assigned defensible probabilities. An unmodeled mechanism, an unprecedented institutional response, or an undefined outcome space may resist quantification. Honest communication states what the model does not cover and uses stress tests or scenarios where probabilities would be invented rather than estimated.[1][2][8] "Unknown" is not the same as zero probability, and an outer prediction band is not proof that all important outcomes have been considered.

### A decision-linked communication workflow

The author's synthesis of the evidence is a nine-step workflow. First, name the user and decision before choosing a graphic. Second, define the event, variable, unit, population, horizon, resolution rule, and information cutoff. Third, list uncertainty sources and dependencies, separating represented uncertainty from omitted or deep uncertainty. Fourth, identify the user's actions, costs, losses, constraints, and reversibility. Fifth, select the smallest sufficient format: event probability for a threshold, prediction interval or distribution for a continuous outcome, fan chart for horizon-dependent distributions, ensemble display for multiple sampled paths, and scenarios for assumption-contingent futures. Sixth, attach coverage, construction, calibration, and assumptions. Seventh, test comprehension with users of varied numeracy, including boundary cases and action questions. Eighth, version the forecast and preserve revisions. Ninth, verify outcomes over repeated cases and update the communication method as well as the model.[1][2][4][5][8][9]

No format passes merely because it is technically valid. The final test is whether the receiver can answer four questions: What exactly may happen? How likely or how widely distributed is it under the stated assumptions? What important uncertainty is not represented? What action changes at which threshold? If the message cannot support those answers, it has not yet converted forecast uncertainty into decision information.

## Evidence

### Numerical uncertainty improved decisions in controlled weather tasks

Joslyn and LeClerc tested forecast formats in road-salting decisions based on overnight temperature forecasts. Participants saw deterministic low-temperature forecasts in a control condition and, in other conditions, explicit probabilities of freezing or decision advice. The task created a cost-loss tradeoff: salting cost resources, while failing to salt before a freeze caused a larger penalty. The economically rational action threshold was 17 percent probability of freezing: salting below 17 percent and not salting at or above 17 percent were classified as decision errors.[4]

The experiments found an overall advantage for uncertainty formats, and explicit uncertainty reduced the damaging effects of forecast error on decision quality and trust. Advice alone did not provide the same overall improvement; the combination of advice and uncertainty performed best in the reported comparison.[4] The method matters because it evaluated actions rather than asking only whether participants could restate a percentage. Its limit is equally important: the task was a controlled weather decision with a known payoff structure, not proof that every probability display improves every real-world choice.

Grounds and Joslyn extended this line of work by testing whether cognitive and demographic differences changed the value of probabilities. In two studies, participants again chose whether to spend resources preventing icy roads or risk a larger freeze-related loss. Conditions included a deterministic nighttime low, the probability of freezing, and expected-value advice.[5] All groups except those with extremely low numeracy scores made better decisions when probabilistic information was available, and no tested group performed worse because probabilities were included. Numeracy was the strongest predictor of decision quality across formats.[5]

These findings reject two simple positions. The public is not categorically unable to use numerical uncertainty, but a raw percentage is not equally usable by every audience. The author's assessment is that the evidence supports layered communication: retain the probability for users and systems that can apply it, add plain-language meaning and decision-relevant context, and test alternatives for audiences with very low numeracy rather than removing uncertainty from everyone.[4][5][13]

### Verbal probability labels were interpreted inconsistently

Budescu, Broomell, and Por conducted an experiment in which participants read probabilistic sentences drawn from the IPCC's 2007 report and assigned numerical values to the verbal terms.[6] The study compared readers' interpretations with the IPCC's intended probability scale. The authors found substantial mismatch and recommended presenting verbal categories together with numerical ranges. Their follow-up reporting states that supplementing terms with numerical boundaries improved communication considerably.[6]

The evidence identifies a specific failure mechanism. A standardized lexicon can be consistent among authors yet remain inconsistent in readers' minds. General instructions or a table elsewhere in a report do not guarantee that a reader will retrieve the intended range at the point of use. The author's assessment is that verbal labels remain useful for fluency and memory, but the number or range should accompany the label wherever the distinction could affect action.[2][6][12]

Teigen's review broadens the interpretation. It synthesizes research on verbal probabilities and numeric ranges and concludes that phrases such as "likely" carry information about direction, severity, source, and speaker attitude in addition to approximate probability.[12] This explains why exact word-number mappings never remove every framing effect. The same phrase can communicate a different practical message when it refers to a benefit, a loss, a speaker's confidence, or an externally varying event.

### Numerical ranges did not generally destroy public trust

Van der Bles and colleagues conducted four survey experiments and one field experiment on the BBC News website to test how uncertainty around facts and numbers affected trust.[7] Their designs compared a central estimate alone with numerical ranges and verbal uncertainty statements across topics including unemployment, wildlife, climate, and migration statistics. One condition, for example, gave an unemployment estimate as a central count plus explicit minimum and maximum values; another said only that the estimate could be somewhat higher or lower.[7]

Across the five experiments, numerical uncertainty did not substantially reduce trust in the numbers or their source. Verbal uncertainty reduced perceived reliability or trust in some comparisons more than numerical ranges did.[7] This evidence is about uncertainty in reported quantities, including epistemic uncertainty about facts, rather than only probability forecasts of future events. It nonetheless addresses a common institutional fear: showing a bounded numerical range is not inherently a confession of incompetence. The study does not show that every range is trusted, especially if it is unexplained, manipulated, or repeatedly misses.

### Visual sampling improved some distribution judgments

Hullman, Resnick, and Adar compared hypothetical outcome plots with error bars and violin plots.[11] A hypothetical outcome plot displays draws from a distribution one at a time as animated frames, translating an abstract density into a finite sequence of possible outcomes. Participants recruited through Amazon Mechanical Turk answered probability questions about one, two, or three uncertain quantities.[11]

The reported experiment found much more accurate judgments with hypothetical outcome plots for comparisons involving two and three quantities, while accuracy was similar across formats for most questions involving a single quantity.[11] In an illustrative task with 96 viewers, more than half misestimated the probability that one uncertain quantity exceeded another when using a conventional static display. The evidence supports a bounded conclusion: sampled-outcome displays can help untrained viewers integrate multivariate uncertainty that error bars or violin plots encode abstractly. Animation also introduces finite-sample and attention constraints, so it is not automatically superior for central-value reading or every delivery medium.[11]

Spiegelhalter, Pearson, and Short's review reaches a compatible but cautious conclusion. It catalogues words, numbers, icon arrays, cones, fan charts, densities, and interactive graphics, while emphasizing that reproducible evidence for universal best practice was limited and that context, numeracy, and task shape performance.[8] The author's assessment is that uncertainty visualization should be treated as an interface to a specific inference, not as a generic badge of statistical sophistication.

### Institutional cases show why construction metadata matters

The Bank of England fan chart is an institutional case rather than a controlled communication experiment. Britton, Fisher, and Whitley documented how the Bank moved from a central projection with one historical-error band toward a richer fan representation of forecast uncertainty.[10] Their explanation tied the shaded region to an empirical reference set and stated its intended containment frequency. That metadata made the bands interpretable and exposed the fact that the chart depended on past forecast errors and committee judgment.[10]

Leutbecher and Palmer's review of the ECMWF ensemble system provides the corresponding model-side case. It explains how perturbed initial conditions and model-error representations generate multiple trajectories intended to quantify flow-dependent uncertainty, and it evaluates the system's ability to represent variations in forecast error.[9] The evidence supports ensembles as a method for representing forecast uncertainty, not the stronger claim that raw ensemble spread exhausts it. Calibration, initial-condition representation, model-error representation, and shared structural limitations remain material.[9]

Together, the studies and cases support four conclusions. First, explicit numerical uncertainty can improve decisions when it maps to a defined threshold.[4][5] Second, verbal labels alone are interpreted too variably for high-stakes precision.[6][12] Third, numerical ranges and well-designed displays can communicate uncertainty without necessarily destroying trust.[7][11] Fourth, a distributional graphic or ensemble must disclose its construction and omissions.[9][10] No study supports a single universal format; the consistent finding is that meaning, task, audience, and validation must be designed together.

## Implications

### For forecasters and model builders

The forecast product should be designed from the decision backward. A model may generate a full distribution, but the user's action may depend on one threshold, one lower-tail quantile, or the probability of a sequence of events. The author's synthesis is to retain the full distribution for audit and evaluation while presenting the decision-relevant slice prominently. This prevents the interface from overwhelming the user without reducing the stored forecast to a point.[1][4][9]

Model outputs should distinguish represented uncertainty from total uncertainty. An ensemble that varies initial conditions but shares one model family does not measure uncertainty from omitted mechanisms. A prediction interval estimated from historical errors may fail after a regime change. A scenario selected for severity is not a percentile unless a probability model makes it one.[2][9][10] The author's synthesis is to add an uncertainty inventory to every release: data, parameters, initial state, model, judgment, dependence, scenario assumptions, and excluded unknowns. Each item should say whether it is quantified, stress-tested, described qualitatively, or absent.

Calibration must be monitored at the level communicated. Binary probabilities require reliability and discrimination checks over comparable events. Prediction intervals require empirical coverage by horizon and subgroup, together with sharpness. Fan-chart bands require verification of the stated marginal or joint interpretation. Ensemble probabilities require post-processing and verification against observations.[1][9] A message that says "80 percent interval" should eventually be tested on many forecasts for whether approximately 80 percent of relevant outcomes were covered under comparable conditions.

Revisions should be published as changes in evidence and assumptions, not merely overwritten numbers. The author should preserve forecast time, model version, data vintage, prior value or distribution, new value or distribution, and a short decomposition of the change. This supports calibration research, organizational learning, and accountability. It also prevents later users from treating the newest forecast as though it had been known from the start.[2][3]

### For decision-makers and organizations

Decision-makers should separate belief from preference. The forecast probability describes the analyst's state of information about an event. The action threshold describes the organization's costs, losses, risk tolerance, legal duties, and reversibility. Asking an analyst to lower a probability because the action is expensive corrupts the belief estimate; asking the decision-maker to act at 10 percent because the possible loss is catastrophic may be rational.[1][15] The two should meet in an explicit decision rule.

The author's synthesis is a three-column decision table. The first column lists observable states or threshold events. The second gives probabilities, intervals, and conditioning assumptions. The third gives actions and their consequences. Where losses are asymmetric, the table should show why the selected action threshold is below or above 50 percent. Where several actions exist, it should show staged responses rather than forcing one warning level to serve every user.

Organizations should preserve alternative views before aggregation. A group probability can hide whether analysts share evidence or merely converge socially. IPCC guidance recommends a traceable account of evidence and agreement and warns that group discussion can suppress important views or narrow ranges.[2] The author's synthesis is to elicit initial judgments independently, record the reasons and dependence among information sources, aggregate only after comparison, and publish material dissent when it changes tails or actions.

Forecast consumers should ask whether a range is a predictive interval, scenario envelope, sensitivity test, or negotiation artifact. They should ask whether bands are pointwise at each horizon or simultaneous for a whole path, whether the distribution includes parameter and model uncertainty, and what evidence supports the tails. These questions convert a polished visualization back into an auditable claim.[8][10]

### For public communication and varied numeracy

Layered communication serves more users than either a bare number or a vague phrase. A first layer can state the defined event, time, numerical probability or range, and recommended action if one exists. A second can show natural frequencies, an icon array, or a simple interval graphic. A third can provide the full distribution, assumptions, method, calibration record, and revision history. Evidence on numeracy and visual formats supports giving users multiple compatible representations rather than deleting numerical uncertainty.[5][8][13]

Denominators and complements should remain stable. Switching from "1 in 10" to "9 in 100" or from losses to gains across comparisons increases cognitive work and can amplify framing. Gigerenzer and Edwards show why a common reference class and natural frequencies can clarify conditional risks.[13] The author's synthesis is to present both event and complement when balance matters, but to keep the action-relevant event first and the denominator constant.

Plain language should explain, not replace, the quantitative object. "Likely (66 to 100 percent under this scale)" is more testable than "likely" alone. "An 80 percent prediction interval from 12 to 18 units, conditional on current policy" is more informative than "between 12 and 18." "Four model scenarios, not assigned probabilities" prevents a scenario bundle from being read as a forecast distribution.[2][6][12] The author should avoid adjectives such as "small," "safe," or "extreme" unless a threshold or comparison defines them.

Graphics require comprehension testing with the intended users. Ask users to locate the median, estimate the chance of crossing the decision threshold, explain the meaning of an outer band, and identify whether outcomes outside the display remain possible. Testing only aesthetic preference is insufficient. Hullman and colleagues show that a display can materially change multivariate probability judgments, while Spiegelhalter and colleagues show that perceptual interpretation depends on design and context.[8][11]

### For warnings and high-consequence decisions

High-consequence communication should expose low-probability outcomes without allowing them to dominate by vividness alone. IPCC guidance notes that tails matter when consequences are large, persistent, widespread, or irreversible.[2] The decision-maker needs probability, consequence, lead time, and feasible protective actions. A worst-case scenario without probability or plausibility can induce panic; a central forecast without tails can encourage dangerous inaction.

Warnings should distinguish forecast uncertainty from action advice. One layer can state the chance of the hazard and its timing. Another can state the warning level, trigger, and protective action. Joslyn and LeClerc's experiments found that probability plus advice outperformed advice alone in their controlled setting.[4] The author's synthesis is to preserve both layers so users can understand why the warning exists and organizations with different cost-loss ratios can adapt their response.

Repeated false alarms should be evaluated against the forecast probability and loss structure rather than counted as simple failures. If action is rational at a 10 percent hazard probability, most protective actions will occur on occasions when the hazard does not materialize. That does not make the forecast or decision wrong. Calibration over many comparable forecasts and transparent threshold logic are necessary to judge the system.[1][4][15]

### For investing and capital allocation

Investment theses contain forecasts about demand, margins, competition, financing, regulation, and duration. The author's synthesis is to translate each decision-critical claim into a horizon, event or range, probability, conditioning assumptions, and an action threshold. A statement such as "margins should recover" becomes auditable only when the measure, period, base case, interval, and evidence that would change the position are recorded.

Asymmetric loss is central. Overestimating upside may cause permanent capital loss, while underestimating upside may create only an opportunity cost. The decision-relevant valuation may therefore emphasize downside quantiles, financing constraints, and paths to ruin rather than the mean outcome. This does not justify arbitrarily pessimistic probabilities. It justifies applying a conservative consequence function to an honestly estimated distribution.[1]

Scenario analysis and probabilistic forecasting should remain separate in an investment memo. Bull, base, and bear cases are usually conditional narratives, not automatically 20th, 50th, and 80th percentiles. Probabilities can be assigned only when the scenarios are sufficiently defined, collectively adequate, and supported by evidence. The author's synthesis is to state scenario assumptions first, estimate probabilities separately, test dependence among drivers, and compare the probability-weighted result with liquidity, leverage, and margin-of-safety constraints.

### For governance, trust, and institutional learning

Institutions often fear that acknowledging uncertainty will weaken authority. Van der Bles and colleagues found little evidence that explicit numerical ranges generally reduced trust, while vague verbal uncertainty produced larger trust penalties in some conditions.[7] Trust should not be optimized by hiding uncertainty. It should be earned through definitions, traceable evidence, calibrated performance, visible corrections, and consistent treatment of favorable and unfavorable outcomes.

A forecast archive is therefore governance infrastructure. It should retain original forecasts, revisions, data cutoffs, model versions, explanations, decisions, and outcomes. This record permits calibration analysis and prevents hindsight from rewriting what was believed. It also separates model error from communication error: the distribution may have been reasonable while the user misread it, or the graphic may have been clear while the model omitted a decisive mechanism.[1][3]

The worst institutional failure is a precise-looking forecast that no one can audit and everyone interprets differently. Prevention is structural: define the target; disclose assumptions; distinguish probability, confidence, interval, ensemble, and scenario; connect the message to explicit thresholds; test comprehension; preserve revisions; and score outcomes. The author's assessment is that this procedure does not eliminate uncertainty. It makes uncertainty usable without pretending that the future has become certain.

## Sources

1. National Research Council (2006). "Completing the Forecast:
   Characterizing and Communicating Uncertainty for Better Decisions
   Using Weather and Climate Forecasts." National Academies Press.
   https://doi.org/10.17226/11699 [high]

2. Mastrandrea, M. D., Field, C. B., Stocker, T. F., et al. (2010).
   "Guidance Note for Lead Authors of the IPCC Fifth Assessment Report
   on Consistent Treatment of Uncertainties." Intergovernmental Panel
   on Climate Change.
   https://www.ipcc.ch/site/assets/uploads/2018/05/uncertainty-guidance-note.pdf
   [high]

3. World Meteorological Organization (2008). "Communicating Forecast
   Uncertainty for Service Providers." WMO Bulletin, 57(4).
   https://wmo.int/resources/bulletin/vol-57-4-2008/communicating-forecast-uncertainty-service-providers
   [high]

4. Joslyn, S. L., and LeClerc, J. E. (2012). "Uncertainty Forecasts
   Improve Weather-Related Decisions and Attenuate the Effects of
   Forecast Error." Journal of Experimental Psychology: Applied, 18(1),
   126-140. https://doi.org/10.1037/a0025185 [high]

5. Grounds, M. A., and Joslyn, S. L. (2018). "Communicating Weather
   Forecast Uncertainty: Do Individual Differences Matter?" Journal of
   Experimental Psychology: Applied, 24(1), 18-33.
   https://doi.org/10.1037/xap0000165 [high]

6. Budescu, D. V., Broomell, S., and Por, H.-H. (2009). "Improving
   Communication of Uncertainty in the Reports of the Intergovernmental
   Panel on Climate Change." Psychological Science, 20(3), 299-308.
   https://doi.org/10.1111/j.1467-9280.2009.02284.x [high]

7. van der Bles, A. M., van der Linden, S., Freeman, A. L. J., and
   Spiegelhalter, D. J. (2020). "The Effects of Communicating
   Uncertainty on Public Trust in Facts and Numbers." Proceedings of the
   National Academy of Sciences, 117(14), 7672-7683.
   https://doi.org/10.1073/pnas.1913678117 [high]

8. Spiegelhalter, D., Pearson, M., and Short, I. (2011). "Visualizing
   Uncertainty About the Future." Science, 333(6048), 1393-1400.
   https://doi.org/10.1126/science.1191181 [high]

9. Leutbecher, M., and Palmer, T. N. (2008). "Ensemble Forecasting."
   Journal of Computational Physics, 227(7), 3515-3539.
   https://doi.org/10.1016/j.jcp.2007.02.014 [high]

10. Britton, E., Fisher, P., and Whitley, J. (1998). "The Inflation
    Report Projections: Understanding the Fan Chart." Bank of England
    Quarterly Bulletin, 38(1).
    https://www.bankofengland.co.uk/quarterly-bulletin/1998/q1/the-inflation-report-projections-understanding-the-fan-chart
    [high]

11. Hullman, J., Resnick, P., and Adar, E. (2015). "Hypothetical Outcome
    Plots Outperform Error Bars and Violin Plots for Inferences About
    Reliability of Variable Ordering." PLOS ONE, 10(11), e0142444.
    https://doi.org/10.1371/journal.pone.0142444 [high]

12. Teigen, K. H. (2022). "Dimensions of Uncertainty Communication:
    What Is Conveyed by Verbal Terms and Numeric Ranges." Current
    Psychology. https://doi.org/10.1007/s12144-022-03985-0 [high]

13. Gigerenzer, G., and Edwards, A. (2003). "Simple Tools for
    Understanding Risks: From Innumeracy to Insight." BMJ, 327(7417),
    741-744. https://doi.org/10.1136/bmj.327.7417.741 [high]

14. Joslyn, S. L., Nadav-Greenberg, L., Taing, M. U., and Nichols,
    R. M. (2009). "The Effects of Wording on the Understanding and Use
    of Uncertainty Information in a Threshold Forecasting Decision."
    Applied Cognitive Psychology, 23(1), 55-72.
    https://doi.org/10.1002/acp.1449 [high]

15. Richardson, D. S. (2003). "Predictability and Economic Value."
    Seminar on Predictability of Weather and Climate. European Centre
    for Medium-Range Weather Forecasts.
    https://www.ecmwf.int/en/elibrary/76166-predictability-and-economic-value
    [high]

## See Also

- `library/probabilistic-thinking-forecasting/forecast-question-design.md`
  -- defines the event, horizon, resolution rule, and versioned contract
  that uncertainty statements must attach to.
- `library/probabilistic-thinking-forecasting/calibration-and-overconfidence.md`
  -- evaluates whether stated probabilities and intervals match outcomes
  across repeated forecasts.
- `library/probabilistic-thinking-forecasting/expected-value-decision-trees.md`
  -- connects probability distributions with payoffs, information value,
  and decision thresholds.
- `library/probabilistic-thinking-forecasting/scenario-planning-and-analysis.md`
  -- develops assumption-contingent futures that should not be mistaken
  for probability intervals.
- `library/probabilistic-thinking-forecasting/fermi-estimation-and-decomposition.md`
  -- exposes assumptions, ranges, and decision-sensitive unknowns when
  precise data are unavailable.
- `library/probabilistic-thinking-forecasting/base-rate-neglect.md`
  -- explains why event probabilities need reference classes and why
  natural-frequency formats can improve interpretation.