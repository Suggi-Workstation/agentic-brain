---
name: clinical-trials-and-evidence-based-medicine
id: 20260930T070808Z
tier: library-topic
domain: health-medicine
author: Librarian
tags: [clinical-trials, evidence-based-medicine, randomization, estimands, trial-reporting, risk-of-bias, systematic-reviews]
links: [library/health-medicine/drug-development-from-molecule-to-medicine.md, library/health-medicine/public-health-epidemiology.md, library/mathematics-statistics/experimental-design.md, library/mathematics-statistics/causal-inference.md, library/mathematics-statistics/hypothesis-testing-and-the-p-value-debate.md]
reviewed: 2026-09-30
---

# Clinical Trials and Evidence-Based Medicine -- Trust Depends on Alignment From Question to Cumulative Review

Clinical trials do not become trustworthy through randomization, large enrollment, or statistical significance alone. A credible estimate aligns a defined treatment question with eligible participants, a control, protected allocation, outcomes, follow-up, analysis, harms surveillance, and transparent reporting, then asks whether the estimate applies beyond the study [1][2][3][6]. Evidence-based medicine combines that evidence with clinical expertise and patient preferences rather than treating any single trial as a command [8].

## Background

Clinical experimentation developed because plausible mechanisms and professional experience could not reliably separate treatment effects from the natural course of illness, selection, expectation, co-intervention, and measurement error. A patient may improve after treatment because the treatment helped, because symptoms would have improved anyway, because care changed in other ways, or because the outcome was observed differently. A concurrent comparison narrows those explanations, and random assignment can make treatment allocation independent of prognosis in expectation when the sequence is generated and concealed correctly. Randomization does not guarantee identical groups, prevent post-allocation bias, or make an ill-defined outcome meaningful; its value comes from the assignment process and the analysis that respects it [1][6][15].

The Medical Research Council's 1948 investigation of streptomycin for pulmonary tuberculosis became an influential example of this logic. The report accepted 109 patients, excluded two who died during a preliminary observation week, and allocated the remaining 107: 55 to streptomycin plus bed rest and 52 to bed rest alone. A centrally controlled random schedule protected allocation, and radiographs were assessed without knowledge of treatment even though injections made delivery apparent. Most streptomycin courses lasted four months, follow-up continued to six months, and later collapse therapy occurred in both groups. The six-month table reported four and 14 deaths, respectively. The case is important not because it was the first controlled experiment, but because allocation protection, a concurrent control, defined outcomes, and masked radiographic assessment were joined in one documented design [16].

The ethical and scientific obligations later became institutionalized. Good Clinical Practice now treats participant rights, safety, and well-being together with reliable results, informed consent, independent ethical review, qualified oversight, protocol adherence, proportionate quality management, and traceable records. The consolidated ICH E6(R3) guideline, adopted in 2026, formally applies to interventional trials of investigational products intended for regulatory submission, although its principles may apply more broadly under local requirements. It also addresses pragmatic elements, decentralized activities, and secondary use of real-world data while retaining the requirement that data be fit for purpose in reliability and relevance [2]. WHO's 2024 guidance has a broader trial-system scope and similarly argues for trials that are ethical, informative, adequately sized, efficient, and integrated into sustainable research systems; it emphasizes that negative findings deserve reporting as much as positive findings [1].

Evidence-based medicine supplied the decision framework around those trials. Sackett and colleagues defined it in 1996 as the conscientious, explicit, and judicious use of current best evidence in individual care, integrated with clinical expertise. They rejected both unexamined authority and cookbook medicine: external evidence informs but cannot replace the clinician's assessment of the patient's clinical state and predicament, while the patient's rights and preferences shape the decision [8]. They also stated that evidence-based medicine is not restricted to randomized trials and meta-analyses; the best design depends on whether the question concerns therapy, diagnosis, prognosis, harm, or another decision [8]. A trial therefore creates evidence for a defined contrast; it does not make the clinical decision by itself.

The modern protocol-to-report chain developed partly because readers could not appraise methods that were missing from publications. SPIRIT 2025 specifies 34 minimum protocol items and a schedule of enrollment, interventions, and assessments; its open-science content includes registration and access to the protocol and statistical analysis plan [4]. CONSORT 2025 specifies 30 minimum reporting items and a participant-flow diagram for completed randomized trials [5]. Both focus on the common individually randomized, two-group parallel design, while extensions cover designs such as cluster, crossover, adaptive, pragmatic, and multi-arm trials [4][5]. They are reporting standards rather than certificates of valid design. Their value is to expose what was planned, what occurred, which participants entered each analysis, and where deviations or missing information limit interpretation [4][5].

Clinical evidence also extends beyond individually randomized, two-group efficacy trials. Cluster trials assign practices or communities; crossover trials compare periods within participants; factorial trials study more than one intervention; adaptive trials make prospectively planned changes using accumulating information; pragmatic trials test effects under conditions closer to routine care; and nonrandomized studies use observed treatment decisions. Each design changes the estimand, dependence structure, sources of bias, and population to which results may apply [1][10][12]. No label supplies validity automatically: an adaptive rule can inflate error if improvised, a pragmatic label can hide weak measurement, and an observational analysis remains vulnerable to confounding even when it uses large real-world datasets [2][9][10][12].

This topic is narrower than drug-development operations and broader than one statistical technique. Manufacturing, phase transitions, application strategy, and regulatory approval belong to the development pathway; general randomization theory, causal identification, and hypothesis testing belong to adjacent mathematics-statistics topics. The focus here is the clinical evidence chain: how a treatment question becomes a study, how conduct and analysis preserve or weaken the comparison, and how clinicians and reviewers decide whether one or more studies support a credible benefit-harm judgment.

## Core Concepts

### Define the Decision, Population, and Estimand Before the Method

A trial should begin with the decision it is meant to inform. The protocol needs a target population, intervention, comparator, outcome, and time horizon, together with an effect measure that states what contrast will be estimated. Eligibility criteria operationalize the population; the intervention and comparator define treatment strategies rather than product names alone; and the outcome identifies what will count as benefit or harm. A question such as whether a drug works is incomplete until dose, background care, follow-up, outcome timing, and treatment discontinuation are addressed [1][3][4].

ICH E9(R1) uses the estimand to connect the clinical question with design and analysis. An estimand specifies the population, treatment conditions, variable or endpoint, how intercurrent events are handled, and the population-level summary of the outcome. Intercurrent events occur after treatment initiation and affect either the interpretation or the existence of measurements associated with the clinical question; an uncollected measurement is missing data, not itself an intercurrent event. E9(R1) describes five strategies. A treatment-policy strategy estimates the effect of assignment regardless of a later event when the variable still exists. A hypothetical strategy asks what would have happened under a defined condition in which the event did not occur. A composite-variable strategy incorporates the event into the outcome definition; a while-on-treatment strategy considers the response before the event; and a principal-stratum strategy targets the subgroup defined by potential occurrence of the event under specified treatments. Principal stratification is not the same as selecting participants according to an event observed after randomization, which can create prognostic selection [3]. The choice must be clinical, explicit, and made before results determine which question looks most favorable.

The estimator and analysis set must match that estimand. An intention-to-treat analysis usually preserves the randomized comparison for an effect of assignment by analyzing participants in the groups to which they were assigned. Conventional as-treated analyses can be confounded because treatment received is related to prognosis; conventional per-protocol restriction can create selection bias because adherence, switching, and discontinuation occur after assignment. Per-protocol effects can be legitimate targets, but sustained-strategy estimation generally needs methods that adjust appropriately for time-varying confounding and selection rather than simply deleting nonadherent participants [1][3][6][9].

### Controls, Randomization, Concealment, and Blinding Solve Different Problems

The control should represent the relevant alternative. Depending on the question and ethics, it may be placebo, usual care, no additional treatment, another dose, or an active treatment. Placebo control can separate the investigational treatment from expectations and ancillary care when withholding active therapy is acceptable. Active-control non-inferiority trials depend on a justified margin and evidence that the design could distinguish effective from ineffective treatment; otherwise similarity can be uninterpretable. Historical or other external controls are vulnerable to changes in prognosis, measurement, and care and require unusually predictable disease and comparability [1][2][17].

Random sequence generation prevents allocation from following prognosis or investigator preference. Allocation concealment protects that sequence until a participant is irrevocably enrolled; it is distinct from blinding after allocation. Central randomization or otherwise secure assignment can prevent an enrolling investigator from delaying, excluding, or advancing a participant after anticipating the next treatment. Randomization balances measured and unmeasured prognostic factors only in expectation, so chance imbalance can remain, especially in small trials [6][15].

Blinding protects behavior and assessment after assignment. Participants, clinicians, outcome assessors, adjudicators, statisticians, and decision committees are different roles and may have different access. Blinding is most consequential when knowledge of treatment can change co-interventions, symptom reports, follow-up, or subjective judgments. When blinding is impossible, credible alternatives include blinded outcome assessment, objective endpoints where appropriate, standardized care, prespecified decisions, and transparent disclosure. Calling a trial open-label does not make it invalid, but it identifies pathways that must be controlled or considered in the risk-of-bias judgment [1][5][6][15].

### Endpoints Must Represent Patient Benefit, Harm, and Time

An endpoint is not valid merely because it is easy to measure. Mortality, symptoms, function, quality of life, hospitalization, biomarkers, imaging findings, and composite outcomes differ in clinical meaning and susceptibility to bias. A surrogate endpoint may shorten follow-up when it reliably predicts how patients feel, function, or survive, but a biomarker response can fail to translate into patient benefit. A composite endpoint can increase event counts but should be clinically coherent, prespecified, and reported by component because a common but less important component may dominate the aggregate [1][4][5][22]. The protocol should define the endpoint, assessment method, time point, adjudication, and handling of competing events before outcomes are known [1][3][4][5].

Treatment effects should be reported in units that support decisions. Relative risks and hazard ratios can show proportional change, while risk differences and numbers needed to treat show how baseline risk changes absolute benefit. The same relative effect can produce a large or small absolute benefit in populations with different baseline risk. Confidence intervals express sampling uncertainty under the analysis assumptions; they do not include bias from failed allocation, missing outcomes, outcome switching, or poor transportability. Statistical significance does not determine clinical importance, and failure to cross a threshold does not prove equivalence or absence of a meaningful effect [3][5][7].

Harms require the same design discipline as benefits. The protocol should define adverse events of special interest, collection periods, severity, coding, attribution procedures, and stopping or escalation rules. Reports should provide denominators and deaths, withdrawals due to harms, participants with at least one harm, and event counts by group; they should distinguish systematic from spontaneous collection and should not suppress harms through arbitrary frequency thresholds [4][5]. Rare or delayed harms may remain undetected in a trial sized for a common efficacy outcome. A credible interpretation states what harms were actively sought, how much exposure and follow-up occurred, and which risks remain too uncommon or delayed for the trial to estimate [1][2][4][5].

### Sample Size, Multiplicity, and Monitoring Control Random Error and Opportunity

Sample-size planning connects the smallest important effect, expected event rate or variability, allocation ratio, desired precision or power, Type I error, attrition, clustering, and analysis method. A small trial can be appropriate for an early safety or pharmacology question, a rare disease, or a very large effect, but it should not claim to exclude moderate benefit or harm that it could not estimate. A large trial can estimate a trivial effect precisely while remaining biased if assignment, measurement, or follow-up are defective [1][4].

Multiplicity arises when a trial examines many primary outcomes, doses, treatment arms, subgroups, interim looks, or analytical variants. If every opportunity is treated as an independent confirmatory test without control, the chance of at least one favorable finding increases. Valid approaches include a prespecified hierarchy, alpha allocation, gatekeeping, or another multiplicity procedure suited to the objectives. Subgroup effects require interaction tests and biological or clinical justification; a significant result in one subgroup and a nonsignificant result in another does not itself demonstrate that treatment effects differ [3][5][10][22].

Adaptive designs permit prospectively planned modifications based on accumulating data. Examples include early stopping for efficacy or futility, sample-size re-estimation, dropping treatment arms, enriching enrollment, or changing allocation probabilities. Adaptation can improve efficiency and learning, but the rule, information flow, operating characteristics, and any required inferential adjustment must be specified and evaluated before comparative interim results can influence the design. Adequately prespecified adaptations based only on noncomparative data may have little or no effect on Type I error; adaptations based on comparative data often inflate error or bias estimates and require stronger controls. Access to comparative interim results should be restricted to independent people with relevant expertise and a need to know, and simulation may be needed for complex designs [10]. Planned flexibility is not permission to redesign a trial after seeing a desired pattern.

Independent data-monitoring committees can review unblinded interim safety and efficacy information while investigators remain protected from comparative trends. Their charter should prespecify membership, reporting structure, meeting procedures, interim analyses, decision guidance, and communication routes [1][2][4]. Stopping early can be ethically necessary for clear harm, overwhelming benefit, or futility, but an early estimate may be unstable and follow-up may be insufficient for durability or uncommon harms [4][5]. A recommendation should therefore weigh statistical evidence, totality of data, external evidence, safety, and the consequences of continuing or stopping.

### Protocol Deviations and Missing Data Change the Meaning of the Result

Nonadherence, treatment switching, rescue therapy, loss to follow-up, and competing events are not clerical imperfections. They can alter which treatment contrast is being estimated and can make outcomes missing for reasons related to prognosis. The protocol should reduce avoidable missingness, continue outcome collection after treatment discontinuation when appropriate, record reasons and timing, and distinguish an intercurrent event from an unobserved outcome. Deleting incomplete participants is not a neutral repair when missingness depends on treatment, health, or outcome [3][4][6].

A primary analysis must state the assumptions used for missing data and intercurrent events. Sensitivity analyses should test the robustness of inference to credible departures from those assumptions while targeting the same estimand. A supplementary analysis that answers a different question can be informative, but it is not a sensitivity analysis merely because its result differs. ICH E9(R1) emphasizes alignment among objective, estimand, estimator, and sensitivity analysis so that disagreement can be interpreted rather than hidden inside competing methods [3].

Protocol deviations also need provenance. Investigators should distinguish eligibility errors, missed visits, treatment errors, nonadherence, prohibited co-interventions, and analysis departures, then assess whether each threatens participant safety, data reliability, or interpretation. A modified analysis that excludes participants after randomization can destroy the original comparison. The safer default for an assignment effect is to retain randomized participants, disclose deviations, and use estimand-aligned methods rather than construct a cleaner but selected cohort [2][3][6].

### Internal Validity and Applicability Are Separate Questions

Internal validity asks whether the estimated contrast is credible for the enrolled participants under the study conditions. External validity asks whether it applies to another population, setting, clinician, treatment implementation, or time. Narrow eligibility, specialist centers, intensive follow-up, free treatment, and high adherence can improve control while making routine implementation less representative. Broad eligibility and ordinary-care delivery can improve relevance while creating variation that must be measured and handled [1][12].

PRECIS-2 treats explanatory and pragmatic design as a continuum across nine domains scored from 1, very explanatory, to 5, very pragmatic: eligibility, recruitment, setting, organization, flexibility of delivery, flexibility of adherence, follow-up, primary outcome, and primary analysis. It is an applicability design aid, not an assessment of internal validity or overall trial quality. Its default framing assumes two arms, one unchanged usual-care comparator; materially different arms should be scored separately. A trial can be highly pragmatic and biased, or tightly explanatory and internally valid but poorly applicable [12]. The design should be as pragmatic as the decision requires and as controlled as credible inference requires.

Decentralized elements move activities such as visits, measurement, consent, or delivery away from conventional trial sites. They may reduce travel burden and widen access, but home measurement, local providers, digital tools, connectivity, and participant choice can introduce variable implementation, missingness, or selection bias. FDA's final 2024 guidance recommends specifying which activities occur remotely, standardizing procedures, training participants and local personnel, protecting data integrity, providing needed devices or telecommunications to avoid access-based exclusion, and managing safety and investigational products. Allowing a participant to choose remote or site assessment can itself bias comparison if health status affects that choice [11]. Decentralization changes logistics and representation; it does not weaken the need for an estimand defined under [3] or for reliable measurement [2][3][11].

Real-world data are patient-health data originally collected outside clinical trials, such as electronic health records, claims, and registries; a device used prospectively to collect trial data does not become a real-world source merely because it is digital [2]. Such data can support randomized pragmatic trials, external controls, safety studies, or nonrandomized comparisons. ICH E6(R3) describes fitness for purpose through reliability -- including accuracy, completeness, provenance, and traceability -- and relevance to the question [2]. Nonrandomized studies additionally require a design that addresses confounding, selection, treatment timing, measurement, and overlap. Emulating a target trial makes eligibility, treatment strategies, assignment, start and end of follow-up, outcomes, causal contrast, and analysis explicit. It does not create randomization or remove assumptions of consistency, positivity, exchangeability, and aligned time zero [9].

### Ethics, Representation, and Partnership Are Design Requirements

Scientific validity does not excuse ethical failure. Before enrollment, independent research ethics review must assess the protocol, risks, benefits, consent process, privacy, compensation, and provisions for care after trial-related injury. Consent is an ongoing process rather than a signature, and protocol amendments generally require ethical review before implementation except when urgent action is needed to remove an immediate hazard [2][4][18]. Placebo use, treatment withholding, and early stopping must remain consistent with genuine uncertainty and participant welfare [1][17][18]. Post-trial plans should address access to beneficial interventions, ancillary care, compensation for trial-related harm, and the risk that communities supplying evidence cannot obtain the resulting intervention [1][4][18].

Selection should represent the population intended to benefit, not merely the people easiest to recruit. ICH E6(R3) makes representativeness a principle, and final FDA guidance identifies dimensions including sex, race, ethnicity, age, residence, organ dysfunction, comorbidities, disabilities, and weight extremes [2][20]. Unnecessary exclusions and participation burdens can narrow applicability and distribute risk or benefit unfairly. A representative sample does not guarantee reliable subgroup estimates, so important heterogeneity still requires prespecified questions, sufficient information, interaction analysis, and honest uncertainty [2][5][20].

Participant and community involvement can improve the relevance of questions, outcomes, burden, recruitment, communication, and dissemination. Current WHO, ICH, SPIRIT, CONSORT, and the Declaration of Helsinki treat this involvement as part of ethical and informative research rather than an optional courtesy [1][2][4][5][18]. Reports should say who was involved, at which stages, what changed, and where involvement was absent. Engagement cannot transfer scientific or ethical responsibility to participants; it exposes design assumptions to the people who bear the intervention and its burdens.

### Registration, Reporting, Replication, and Synthesis Complete the Evidence Chain

Prospective registration and a public protocol create a time-stamped record of planned outcomes, analyses, and enrollment. SPIRIT 2025 aligns the protocol with registration, the statistical analysis plan, data sharing, funding, harms, and participant involvement [4]. CONSORT 2025 asks the completed report to disclose allocation, blinding, participant flow, deviations, outcomes, harms, analysis, registration, protocol access, and data-sharing information [5]. The 2024 Declaration of Helsinki requires public registration before recruitment and public availability of negative, inconclusive, and positive results [18]. Jurisdictional law can use a different scope and clock: for applicable US clinical trials, FDAAA generally requires registration within 21 days after first enrollment and summary results within one year after primary completion [21]. Registration, registry maintenance, summary-results posting, protocol and analysis-plan disclosure, and journal publication are distinct acts; compliance with one does not establish the others [4][5][18][21].

A trial should begin and end in cumulative evidence. SPIRIT asks protocols to justify the new study against current systematic evidence, and CONSORT asks reports to interpret results in relation to the existing evidence [4][5]. Cochrane similarly states that a systematic review should ordinarily precede new primary research to avoid unnecessary duplication and reveal unresolved questions [23]. This obligation makes a trial part of a revisable evidence base rather than an isolated contest for statistical significance.

Replication asks whether a result survives new participants, investigators, settings, and time. The author's synthesis is that exact procedural replication can test whether a result recurs under closely matched conditions, while pragmatic or comparative-effectiveness trials test whether it travels into ordinary care. Differences do not have one automatic explanation: the original estimate may have been exaggerated, the replication may be imprecise, implementation may differ, or effects may vary. Cumulative interpretation should compare effect estimates, uncertainty, protocols, populations, adherence, and bias rather than count how many studies crossed a p-value threshold [5][7][23].

Systematic reviews make the search and synthesis process explicit, but a pooled estimate inherits the limitations of included evidence. Cochrane's RoB 2 framework assesses bias arising from randomization, deviations from intended interventions, missing outcome data, outcome measurement, and selection of the reported result for a specific result; its judgments are low risk, some concerns, or high risk [6]. Selection of a reported result is narrower than complete nonreporting of an outcome or study, which is assessed at evidence-synthesis level. GRADE rates certainty as high, moderate, low, or very low after considering risk of bias, inconsistency, indirectness, imprecision, and publication bias, with specified rules for starting levels and possible upgrading [7]. Meta-analysis can improve precision when studies address sufficiently coherent questions; it cannot turn incompatible estimands, biased trials, or unpublished outcomes into a trustworthy average.

## Evidence

### The Streptomycin Trial Demonstrated a Protected Comparison

The 1948 Medical Research Council study tested streptomycin plus bed rest against bed rest alone in patients with acute progressive bilateral pulmonary tuberculosis. Investigators accepted 109 patients; two died during the preliminary observation week and were excluded, leaving 55 allocated to streptomycin and 52 to control. Assignment schedules were prepared centrally from random sampling numbers, treatment was not known before enrollment, and radiographs were assessed without knowledge of assignment. Most streptomycin treatment lasted four months, while outcomes were followed to six months; later collapse therapy occurred in 11 participants in each group. At six months the primary report recorded four deaths in the streptomycin group and 14 in the control group, alongside radiographic and bacteriological outcomes [16].

This case shows why a clinical trial is more than a treated series. The concurrent control represented what occurred under bed rest during the same period; protected allocation limited prognostic selection; masked radiographic assessment reduced judgment influenced by treatment knowledge; and a defined follow-up made the comparison auditable. The report does not establish that bacteriological assessment was blinded. The intervention had toxicities, treatment delivery was visible, co-intervention occurred, and the sample was too small to settle every benefit and harm. The evidentiary achievement was a bounded causal comparison, not complete knowledge about streptomycin [16].

### Meta-Epidemiology Associated Reported Design Protections With Effect Estimates

Wood and colleagues combined data from three meta-epidemiological studies, covering 146 meta-analyses and 1,346 controlled trials, to examine whether reported allocation concealment and reported blinding were associated with treatment-effect estimates. In 102 meta-analyses containing 804 trials, estimates from trials with inadequate or unclear reported allocation concealment were, on average, 17% more favorable on the odds-ratio scale than estimates from adequately concealed trials. The association varied among meta-analyses and was stronger for subjectively assessed outcomes than for mortality [15].

The study compared trial characteristics across collections of trials rather than randomly assigning methodological defects, so residual confounding and imperfect reporting remained possible. A well-conducted trial can be poorly reported, and trial features cluster together. The result does not provide a correction factor that should be subtracted from every unblinded study. It supports an outcome-specific risk-of-bias judgment: allocation concealment matters before assignment, blinding matters most where knowledge can influence care or assessment, and uncertainty about conduct should reduce confidence rather than be converted into a mechanical penalty [15].

### RECOVERY Showed the Power and Boundaries of a Large Pragmatic Platform

The RECOVERY platform trial evaluated dexamethasone in hospitalized patients with Covid-19 across 176 National Health Service organizations in the United Kingdom. It randomly assigned 2,104 patients to dexamethasone 6 mg once daily for up to 10 days or discharge and 4,321 to usual care, used 28-day mortality as the primary outcome, and analyzed assignment by intention to treat. Death occurred in 22.9% of the dexamethasone group and 25.7% of usual care, an age-adjusted Cox rate ratio of 0.83 with a 95% confidence interval from 0.75 to 0.93 [14].

The prespecified respiratory-support subgroups changed the clinical meaning. Dexamethasone reduced mortality among patients receiving invasive ventilation or oxygen, with the oxygen category including noninvasive ventilation. Patients receiving no oxygen at randomization had 17.8% versus 14.0% mortality, with an age-adjusted rate ratio of 1.19 and a 95% confidence interval from 0.92 to 1.55. The latter interval did not establish benefit and allowed possible harm. The study therefore supported the defined regimen for specified severity groups, not a general claim that every patient with Covid-19 should receive dexamethasone [14].

RECOVERY also illustrates pragmatic efficiency without evidentiary looseness. Broad hospital participation, a simple intervention, routine clinical outcomes, and a platform structure enabled rapid enrollment. Its open-label design was less threatening for the objective mortality endpoint than it would have been for a subjective symptom score, although co-intervention remained possible. Outcome ascertainment was 99.9% complete, with follow-up forms available for 99.6% and 99.7% of the two groups. Age adjustment was added after a 1.1-year baseline imbalance became apparent rather than specified in the first analysis plan, and subgroup p-values were not adjusted for multiplicity; unadjusted sensitivity analyses were similar [14]. Large size narrowed random error, while randomization, protocol provenance, near-complete follow-up, and interaction analysis determined what the numbers meant.

A platform trial is an ongoing master-protocol design in which treatment arms may enter or leave. FDA's June 2026 revised guidance remains a draft, not for implementation, but identifies two important design issues: primary comparisons should generally use controls who were concurrently enrolled, eligible, and able to be randomized to the relevant arm, and multiplicity should be controlled within a drug-disease objective even though strong family-wise control across distinct drugs or diseases is not generally required [25]. Platform efficiency does not make nonconcurrent controls exchangeable or every shared-control comparison one confirmatory family.

### FDA Records Exposed How Selective Publication Alters the Evidence Base

Turner and colleagues obtained FDA reviews for 74 efficacy studies of 12 antidepressants and matched them to qualifying stand-alone journal reports. Their analyzed denominator of 12,564 participants excluded active-comparator arms and unapproved doses, so it was smaller than total participation in the submitted studies. The FDA judged 38 of 74 studies positive, or 51%, while 48 of 51 published studies appeared positive, or 94%. Data from 3,449 participants had no qualifying publication, and another 1,843 participants appeared in reports whose highlighted finding conflicted with the FDA-defined primary outcome [13].

Selection changed apparent magnitude as well as the count of positive trials. For every drug, the effect size derived from journal reports exceeded the effect size derived from FDA reviews; increases ranged from 11% to 69%, and the weighted mean effect size increased 32%, from 0.31 to 0.41. The study was limited to antidepressant efficacy trials submitted to FDA, and its rules could classify a study covered only in a multi-study article as unpublished. It could not determine whether nonpublication decisions originated with investigators, sponsors, journals, or several actors. It nevertheless demonstrated directly that a literature composed only of qualifying visible reports can misrepresent the regulatory evidence set [13].

This result explains why registration, result posting, protocol access, and systematic searches for unpublished evidence are part of validity at evidence-base level. An internally credible trial that disappears still biases the accessible record, while outcome switching can make a completed trial communicate a different claim. WHO explicitly requires reporting regardless of whether findings are positive or negative [1]; ICH E6(R3), SPIRIT, CONSORT, and the Declaration of Helsinki impose related but differently scoped registration, disclosure, or reporting expectations [2][4][5][18].

### Evidence Appraisal Requires Both Study-Level and Body-Level Judgments

The Cochrane Handbook separates a risk-of-bias judgment for a specific trial result from certainty in a body of evidence. RoB 2 asks whether randomization, deviations, missing outcomes, measurement, and selection of the reported result could bias the result being used [6]. GRADE then asks whether the body is limited by those biases, inconsistent effects, indirect populations or interventions, imprecision, or publication bias [7]. This layered approach prevents a common error: calling all randomized evidence high certainty regardless of conduct, or calling a pooled estimate certain because it is numerically precise.

The combined evidence supports a dependency model. The 1948 trial shows how allocation and assessment create a defensible comparison; the meta-epidemiological analysis shows that failures in those protections are associated with distorted estimates; RECOVERY shows how a large pragmatic platform can produce decision-changing evidence while preserving subgroup boundaries; and the antidepressant cohort shows that even completed trials can mislead collectively when results are selected. Trust is therefore not one property attached to the acronym RCT. It is the result of consistent protections from question formulation through public synthesis [13][14][15][16].

## Implications

### For Trialists: Design Backward From the Clinical Decision

The first practical task is to write the claim the trial should support, then design backward. Specify the patient population, treatment strategies, comparator, primary benefit and harm outcomes, time horizon, intercurrent events, effect measure, and smallest important difference. Translate that question into an estimand, choose an assignment and control capable of identifying it, and choose an estimator that preserves the design. If those elements cannot be stated coherently, adding sites, variables, or statistical complexity will not rescue the study [1][3][4].

Eligibility should balance safety, signal detection, recruitment feasibility, representativeness, and applicability. Excluding people with common comorbidities, older age, concomitant treatment, language barriers, disability, place of residence, or limited digital access may simplify conduct while making the result less useful for routine care. Inclusion should not be indiscriminate: a population must have a defensible benefit-harm rationale and appropriate safeguards. The protocol should explain each important restriction, reduce avoidable participation burdens, and describe the population to which the effect is intended to apply [1][2][20].

The control and outcome should match the decision rather than convenience. A placebo comparison may establish efficacy but leave clinicians without direct evidence against current best treatment [17]. A surrogate may accelerate learning but leave uncertainty about patient benefit. A composite may improve power while allowing a common minor component to drive the result unless components are coherent and reported separately [22]. The author's synthesis is a simple test: if the primary result were favorable, could a clinician explain exactly what changed for patients, compared with what alternative, over what time, and at what cost in harms? If not, the endpoint or comparator is not yet decision-ready.

The analysis plan should make favorable improvisation difficult. Prespecify primary and secondary outcomes, analysis populations, covariates, missing-data assumptions, multiplicity control, subgroup hypotheses, interim rules, and sensitivity analyses. Preserve exploratory work, but label it and seek new data for confirmation. For an adaptive design, prospective means specifying the change before comparative analyses of accumulating trial data, not merely before outcomes become public. Amendments based only on external information may be legitimate while comparative results remain concealed; an outcome redefinition influenced by emerging comparative results is a different evidentiary act and must not be presented as the original test [3][4][5][10].

Quality management should focus on errors that could harm participants or change the answer. Perfect transcription of low-value data does not compensate for failed consent, predictable allocation, missing primary outcomes, treatment contamination, or inaccessible source records. ICH E6(R3) and WHO support risk-proportionate systems: identify critical-to-quality factors, prevent their failure, monitor them, and preserve traceability. This approach is stricter about consequential errors while avoiding bureaucracy that consumes resources without improving safety or reliability [1][2].

### For Clinicians and Patients: Read the Estimate as a Conditional Answer

A trial report should be translated into a sentence with explicit boundaries: in this enrolled population, assignment to this treatment strategy rather than this comparator changed this outcome over this period by this estimated amount, with this uncertainty and these observed harms. That sentence prevents a drug name, trial phase, p-value, or press-release conclusion from standing in for the actual treatment contrast [3][5].

Absolute effects should be reconstructed for the patient's baseline risk whenever possible. A relative reduction can look stable across risk groups while the number of events prevented differs materially. Confidence intervals should be inspected for both benefit and harm of clinically important magnitude. A small p-value does not resolve bias or applicability, and a large p-value does not prove equality. The relevant question is which effect sizes remain compatible with the data and whether those effects would change the decision [3][7].

Harms and burden deserve symmetric attention. Ask whether adverse events were actively collected, whether follow-up was long enough, whether withdrawals differed, and whether the trial was large enough to observe uncommon risks. Also ask about treatment inconvenience, monitoring, cost, and feasibility, because an efficacious regimen can fail in practice if delivery differs from the study. Evidence-based medicine combines external evidence and clinical expertise with the patient's circumstances, rights, and preferences; neither external evidence nor expertise alone is sufficient [1][2][8].

Subgroups should be treated cautiously. A treatment effect can genuinely vary with disease severity, biology, timing, or background care, as RECOVERY's respiratory-support results demonstrate [14]. But searching many subgroups creates false patterns, and comparing one significant subgroup with one nonsignificant subgroup is not a valid interaction test. Credible heterogeneity is stronger when prespecified, supported by an interaction, clinically plausible, replicated, and measured with adequate information [3][5].

### For Reviewers, Guidelines, and Health Systems: Audit the Whole Evidence Path

Critical appraisal should begin with the trial's protocol and registry entry, not only the abstract. Reviewers should compare primary outcomes, time points, sample-size assumptions, analysis populations, amendments, participant flow, and harms across the protocol, statistical analysis plan, registry, report, and supplements. Missing information is not proof of misconduct. Depending on which RoB 2 signaling question it affects, absence may simply leave no evidence of a problem or may preclude assessment and raise concern when the information should have been available [4][5][6].

The risk-of-bias judgment should be result-specific. Lack of participant blinding may matter greatly for pain ratings and less for all-cause mortality; missingness may threaten one outcome more than another; an analysis that is valid for assignment may not estimate adherence. A quality score that adds unrelated checklist items can hide a fatal flaw behind many minor passes. Domain-level judgments make the causal pathway explicit and connect directly to sensitivity analysis or exclusion in synthesis [6][15].

Systematic reviews should use a comprehensive, documented search that includes appropriate registries and nonjournal sources, define eligible populations, interventions, comparators, outcomes, designs, and estimands before selection, assess result-specific bias, investigate heterogeneity, and show how conclusions change under plausible assumptions [3][6][24]. Turner and colleagues show why regulatory records can recover evidence absent or distorted in journal publication [13]. Pooling should be refused when treatment versions, follow-up, outcome definitions, or estimands answer materially different questions. When synthesis is appropriate, both relative and absolute effects, uncertainty, study limitations, and certainty should be reported [7].

Guidelines add a decision layer beyond evidence synthesis. GRADE Evidence-to-Decision frameworks consider benefit-harm balance, certainty, patient values, resources, equity, acceptability, and feasibility; applicability to the decision context must also be explicit [19]. A strong recommendation based on a precise but indirect surrogate can be less justified than a conditional recommendation based on direct but imprecise patient outcomes. The author's assessment is that transparent separation of evidence, values, and implementation assumptions is safer than allowing a recommendation grade to conceal why action was chosen.

Health systems should support learning infrastructure before emergencies. Standing protocols, interoperable data, trained sites, ethics and governance capacity, and simple randomization systems can make large trials feasible when uncertainty is urgent. RECOVERY enrolled through ordinary hospitals because a platform and network could convert routine care into a protected comparison [14]. WHO's guidance favors sustainable trial ecosystems that can study endemic conditions and pivot during crises rather than rebuilding capacity after every emergency [1].

### For Adaptive, Decentralized, and Real-World Approaches: Innovation Must Preserve Identifiability

Adaptive design is valuable when uncertainty at launch can be converted into a prespecified decision. The design should state what can change, which data trigger change, who sees comparative interim results, how error and estimation are controlled where necessary, and how operating characteristics were verified. Prespecified adaptations based only on noncomparative data may require little or no inferential correction, while comparative-data adaptations usually require stronger control and restricted access. A change based only on external information can be acceptable while comparative trial results remain concealed. If a modification is improvised after comparative results are known, the trial may still yield exploratory information, but its original confirmatory error guarantees no longer apply [10].

Decentralization should be judged component by component. Remote consent may improve reach but requires the ordinary consent, privacy, and documentation protections. Home measurements may reduce travel while adding device, training, and environmental variation. Local clinicians can make participation feasible while increasing delivery heterogeneity, and mixed remote or site choice may select participants by health status [11]. The protocol should standardize what must be standardized, measure what is allowed to vary, supply needed technology to reduce socioeconomic exclusion, and prespecify how access-related participation or missingness will be evaluated; the final clause is the author's synthesis from the access and bias risks [2][11].

Real-world data do not become evidence merely by scale. A million incomplete records with ambiguous treatment timing can answer less than a small trial with protected allocation and complete outcomes. Before analysis, investigators should verify provenance, coding, coverage, timing, linkage, missingness, and whether the data contain the confounders and outcomes required for the target question. Randomization embedded in routine data can retain causal protection while improving efficiency; nonrandomized comparisons require explicit identification assumptions and sensitivity analysis for residual bias [2][9].

The author's synthesis is that innovation should be evaluated through invariants rather than labels. The clinical question must remain defined; treatment assignment or selection must be understood; measurements must be fit for purpose; analysis must follow the estimand; participant protection must remain proportionate; and reporting must expose deviations and uncertainty. Pragmatic, adaptive, decentralized, and real-world approaches are trustworthy when they preserve those invariants, not when novelty substitutes for them [1][2][3][10][11][12].

### A Practical Evidence Audit

A reader can audit a treatment claim with twelve connected questions. What exact decision and estimand were specified? Who was eligible and who enrolled? Was selection representative of the intended population, and were patients or communities involved in choosing consequential questions and outcomes? What alternatives were compared? How was assignment generated and concealed? Which roles were blinded, and what protections replaced impossible blinding? Were consent, independent ethical review, privacy, safety monitoring, and post-trial responsibilities adequate? Were outcomes patient-important, prespecified, completely observed, and measured comparably? Were sample size, interim looks, multiplicity, and subgroups planned? How were adherence, switching, missing data, and harms handled? Does the result apply to the intended patient and setting? Are registration, protocol and analysis-plan disclosure, result posting, publication, replication, and placement in the complete evidence base all traceable [1][2][3][4][5][6][7][18].

The questions function as a dependency chain rather than a score. A large sample cannot repair a confounded comparison. Randomization cannot repair outcome switching. Complete reporting cannot repair a meaningless endpoint, although it lets readers see the failure. Meta-analysis cannot repair missing negative trials. The worst preventable outcome is a precise, influential answer to a question the design did not identify; prevention requires alignment at every link [3][6][13][15].

The positive conclusion is equally bounded. Clinical trials can distinguish moderate treatment effects from noise, detect harm, overturn plausible but ineffective practice, and support rapid learning when their questions, protections, and analyses align [1][14][16]. Evidence-based medicine completes rather than replaces that work by integrating trustworthy estimates with expertise, patient circumstances, and preferences [8]. Trust is therefore earned cumulatively: by a protocol that states the question, conduct that preserves the comparison, analysis that targets it, reporting that exposes it, and synthesis that keeps uncertainty visible.

## Sources

1. World Health Organization. (2024). "Guidance for Best Practices for
   Clinical Trials." ISBN 978-92-4-009771-1.
   https://www.who.int/publications/i/item/9789240097711 [high]

2. International Council for Harmonisation. (2026). "Guideline for Good
   Clinical Practice E6(R3)," consolidated Principles, Annex 1, and Annex 2,
   adopted June 16, 2026.
   https://database.ich.org/sites/default/files/ICH%20E6%28R3%29_Step4_FinalConsolidatedGuideline_2026_0616_.pdf [high]

3. International Council for Harmonisation. (2019). "Addendum on Estimands
   and Sensitivity Analysis in Clinical Trials to the Guideline on
   Statistical Principles for Clinical Trials E9(R1)."
   https://database.ich.org/sites/default/files/E9-R1_Step4_Guideline_2019_1203.pdf [high]

4. Chan, A.-W., Boutron, I., Hopewell, S., et al. (2025). "SPIRIT 2025
   Statement: Updated Guideline for Protocols of Randomised Trials." BMJ,
   389, e081477. https://doi.org/10.1136/bmj-2024-081477 [high]

5. Hopewell, S., Chan, A.-W., Collins, G. S., et al. (2025). "CONSORT 2025
   Statement: Updated Guideline for Reporting Randomised Trials." BMJ, 389,
   e081123. https://doi.org/10.1136/bmj-2024-081123 [high]

6. Higgins, J. P. T., Savovic, J., Page, M. J., Elbers, R. G., and Sterne,
   J. A. C. (2024). "Chapter 8: Assessing Risk of Bias in a Randomized
   Trial." Cochrane Handbook for Systematic Reviews of Interventions,
   version 6.5. https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-08 [high]

7. Schunemann, H. J., Higgins, J. P. T., Vist, G. E., et al. (2024).
   "Chapter 14: Completing Summary of Findings Tables and Grading the
   Certainty of the Evidence." Cochrane Handbook for Systematic Reviews of
   Interventions, version 6.5.
   https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-14 [high]

8. Sackett, D. L., Rosenberg, W. M. C., Gray, J. A. M., Haynes, R. B., and
   Richardson, W. S. (1996). "Evidence Based Medicine: What It Is and What
   It Isn't." BMJ, 312, 71-72.
   https://doi.org/10.1136/bmj.312.7023.71 [high]

9. Hernan, M. A., and Robins, J. M. (2020; online version updated August
   19, 2026). "Causal Inference: What If." Chapman & Hall/CRC.
   https://miguelhernan.org/whatifbook [high]

10. U.S. Food and Drug Administration. (2019). "Adaptive Designs for
    Clinical Trials of Drugs and Biologics: Guidance for Industry."
    https://www.fda.gov/media/78495/download [high]

11. U.S. Food and Drug Administration. (2024). "Conducting Clinical Trials
    With Decentralized Elements: Guidance for Industry, Investigators, and
    Other Interested Parties."
    https://www.fda.gov/regulatory-information/search-fda-guidance-documents/conducting-clinical-trials-decentralized-elements [high]

12. Loudon, K., Treweek, S., Sullivan, F., Donnan, P., Thorpe, K. E., and
    Zwarenstein, M. (2015). "The PRECIS-2 Tool: Designing Trials That Are
    Fit for Purpose." BMJ, 350, h2147.
    https://doi.org/10.1136/bmj.h2147 [high]

13. Turner, E. H., Matthews, A. M., Linardatos, E., Tell, R. A., and
    Rosenthal, R. (2008). "Selective Publication of Antidepressant Trials
    and Its Influence on Apparent Efficacy." New England Journal of
    Medicine, 358, 252-260. https://doi.org/10.1056/NEJMsa065779 [high]

14. RECOVERY Collaborative Group. (2021). "Dexamethasone in Hospitalized
    Patients with Covid-19." New England Journal of Medicine, 384,
    693-704. https://doi.org/10.1056/NEJMoa2021436 [high]

15. Wood, L., Egger, M., Gluud, L. L., et al. (2008). "Empirical Evidence
    of Bias in Treatment Effect Estimates in Controlled Trials With
    Different Interventions and Outcomes: Meta-Epidemiological Study."
    BMJ, 336, 601-605. https://doi.org/10.1136/bmj.39465.451748.AD [high]

16. Medical Research Council. (1948). "Streptomycin Treatment of Pulmonary
    Tuberculosis: A Medical Research Council Investigation." British
    Medical Journal, 2(4582), 769-782.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC2091872/ [high]

17. International Council for Harmonisation. (2000). "Choice of Control
    Group and Related Issues in Clinical Trials E10."
    https://database.ich.org/sites/default/files/E10_Guideline.pdf [high]

18. World Medical Association. (2024). "Declaration of Helsinki: Ethical
    Principles for Medical Research Involving Human Participants."
    https://www.wma.net/policies-post/wma-declaration-of-helsinki/ [high]

19. Alonso-Coello, P., Schunemann, H. J., Moberg, J., et al. (2016). "GRADE
    Evidence to Decision Frameworks: A Systematic and Transparent Approach
    to Making Well Informed Healthcare Choices. 1: Introduction." BMJ, 353,
    i2016. https://doi.org/10.1136/bmj.i2016 [high]

20. U.S. Food and Drug Administration. (2025). "Enhancing Participation in
    Clinical Trials -- Eligibility Criteria, Enrollment Practices, and Trial
    Designs: Guidance for Industry."
    https://www.fda.gov/regulatory-information/search-fda-guidance-documents/enhancing-participation-clinical-trials-eligibility-criteria-enrollment-practices-and-trial-designs [high]

21. U.S. National Library of Medicine. "FDAAA 801 and the Final Rule."
    ClinicalTrials.gov policy information.
    https://clinicaltrials.gov/policy/fdaaa-801-final-rule [high]

22. U.S. Food and Drug Administration. (2022). "Multiple Endpoints in
    Clinical Trials: Guidance for Industry."
    https://www.fda.gov/media/162416/download [high]

23. Cochrane. "Chapter 1: Starting a Review." Cochrane Handbook for
    Systematic Reviews of Interventions, current version.
    https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-01 [high]

24. Lefebvre, C., Glanville, J., Briscoe, S., et al. (2025). "Chapter 4:
    Searching for and Selecting Studies." Cochrane Handbook for Systematic
    Reviews of Interventions, version 6.5.1.
    https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04 [high]

25. U.S. Food and Drug Administration. (2026). "Master Protocols for Drug
    and Biological Product Development: Revised Draft Guidance for
    Industry." Draft -- Not for Implementation.
    https://www.fda.gov/media/174976/download [high]

## See Also

- `library/health-medicine/drug-development-from-molecule-to-medicine.md` -- places clinical trials within the wider pathway from candidate selection through postmarket evidence.
- `library/health-medicine/public-health-epidemiology.md` -- extends treatment evidence to populations, surveillance, and prevention.
- `library/mathematics-statistics/experimental-design.md` -- develops randomization, blocking, blinding, replication, and validity across experimental settings.
- `library/mathematics-statistics/causal-inference.md` -- explains estimands and identification assumptions for randomized and nonrandomized comparisons.
- `library/mathematics-statistics/hypothesis-testing-and-the-p-value-debate.md` -- distinguishes statistical thresholds from effect magnitude, uncertainty, and replication.
