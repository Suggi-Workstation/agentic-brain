---
name: clinical-trials-and-evidence-based-medicine
id: 20260930T070808Z
tier: library-topic
domain: health-medicine
author: Librarian
tags: [clinical-trials, evidence-based-medicine, randomization, estimands, trial-reporting, risk-of-bias, systematic-reviews]
links: [library/health-medicine/drug-development-from-molecule-to-medicine.md, library/health-medicine/public-health-epidemiology.md, library/mathematics-statistics/experimental-design.md, library/mathematics-statistics/causal-inference.md, library/mathematics-statistics/hypothesis-testing-and-the-p-value-debate.md]
---

# Clinical Trials and Evidence-Based Medicine -- Trust Depends on Alignment From Question to Cumulative Review

Clinical trials do not become trustworthy through randomization, large enrollment, or statistical significance alone. A credible estimate aligns a defined treatment question with eligible participants, a control, protected allocation, outcomes, follow-up, analysis, harms surveillance, and transparent reporting, then asks whether the estimate applies beyond the study [1][2][3][6]. Evidence-based medicine combines that evidence with clinical expertise and patient preferences rather than treating any single trial as a command [8].

## Background

Clinical experimentation developed because plausible mechanisms and professional experience could not reliably separate treatment effects from the natural course of illness, selection, expectation, co-intervention, and measurement error. A patient may improve after treatment because the treatment helped, because symptoms would have improved anyway, because care changed in other ways, or because the outcome was observed differently. A concurrent comparison narrows those explanations, and random assignment can make treatment allocation independent of prognosis in expectation when the sequence is generated and concealed correctly. Randomization does not guarantee identical groups, prevent post-allocation bias, or make an ill-defined outcome meaningful; its value comes from the assignment process and the analysis that respects it [1][6][15].

The Medical Research Council's 1948 investigation of streptomycin for pulmonary tuberculosis became an influential example of this logic. The report compared streptomycin plus bed rest with bed rest alone, used a centrally controlled random allocation schedule, and masked radiographic and bacteriological assessors even though injections made treatment delivery apparent. The study enrolled 55 patients in the streptomycin group and 52 controls; its six-month table reported four and 14 deaths, respectively. The case is important not because it was the first controlled experiment, but because allocation protection, a concurrent control, defined outcomes, and masked assessment were joined in one documented design [16].

The ethical and scientific obligations later became institutionalized. Good Clinical Practice now treats participant rights, safety, and well-being together with reliable results, informed consent, qualified oversight, protocol adherence, proportionate quality management, and traceable records. The consolidated ICH E6(R3) guideline, adopted in 2026, also addresses pragmatic elements, decentralized activities, and real-world data while retaining the requirement that data be fit for purpose in reliability and relevance [2]. WHO's 2024 guidance similarly argues for trials that are ethical, informative, adequately sized, efficient, and integrated into sustainable research systems; it emphasizes that negative findings deserve reporting as much as positive findings [1].

Evidence-based medicine supplied the decision framework around those trials. Sackett and colleagues defined it in 1996 as the conscientious, explicit, and judicious use of current best evidence in individual care, integrated with clinical expertise. They rejected both unexamined authority and cookbook medicine: external evidence can inform whether an intervention is likely to help, but the clinician must judge whether the study population, alternatives, burdens, and outcomes match the patient, while the patient's rights and preferences shape the decision [8]. A trial therefore creates evidence for a defined contrast; it does not make the clinical decision by itself.

The modern protocol-to-report chain developed partly because readers could not appraise methods that were missing from publications. SPIRIT 2025 specifies 34 minimum protocol items and a schedule of enrollment, interventions, and assessments; its open-science content includes registration and access to the protocol and statistical analysis plan [4]. CONSORT 2025 specifies 30 minimum reporting items and a participant-flow diagram for completed randomized trials [5]. Both are reporting standards rather than certificates of valid design. Their value is to expose what was planned, what occurred, which participants entered each analysis, and where deviations or missing information limit interpretation [4][5].

Clinical evidence also extends beyond individually randomized, two-group efficacy trials. Cluster trials assign practices or communities; crossover trials compare periods within participants; factorial trials study more than one intervention; adaptive trials make prospectively planned changes using accumulating information; pragmatic trials test effects under conditions closer to routine care; and nonrandomized studies use observed treatment decisions. Each design changes the estimand, dependence structure, sources of bias, and population to which results may apply [1][10][12]. No label supplies validity automatically: an adaptive rule can inflate error if improvised, a pragmatic label can hide weak measurement, and an observational analysis remains vulnerable to confounding even when it uses large real-world datasets [2][9][10][12].

This topic is narrower than drug-development operations and broader than one statistical technique. Manufacturing, phase transitions, application strategy, and regulatory approval belong to the development pathway; general randomization theory, causal identification, and hypothesis testing belong to adjacent mathematics-statistics topics. The focus here is the clinical evidence chain: how a treatment question becomes a study, how conduct and analysis preserve or weaken the comparison, and how clinicians and reviewers decide whether one or more studies support a credible benefit-harm judgment.

## Core Concepts

### Define the Decision, Population, and Estimand Before the Method

A trial should begin with the decision it is meant to inform. The protocol needs a target population, intervention, comparator, outcome, and time horizon, together with an effect measure that states what contrast will be estimated. Eligibility criteria operationalize the population; the intervention and comparator define treatment strategies rather than product names alone; and the outcome identifies what will count as benefit or harm. A question such as whether a drug works is incomplete until dose, background care, follow-up, outcome timing, and treatment discontinuation are addressed [1][3][4].

ICH E9(R1) uses the estimand to connect the clinical question with design and analysis. An estimand specifies the population, treatment conditions, variable or endpoint, how intercurrent events are handled, and the population-level summary of the outcome. Intercurrent events are events after treatment initiation that affect interpretation or observation, such as stopping assigned treatment, using rescue medication, switching therapy, or dying before a nonfatal endpoint. Different strategies answer different questions: a treatment-policy strategy may estimate the effect of assignment regardless of later discontinuation, while a hypothetical strategy asks what would have happened under a defined counterfactual condition. The choice must be clinical, explicit, and made before results determine which question looks most favorable [3].

The estimator and analysis set must match that estimand. An intention-to-treat analysis usually preserves the randomized comparison for an effect of assignment by analyzing participants in the groups to which they were assigned. A naive per-protocol or as-treated comparison can reintroduce confounding because adherence, switching, and discontinuation may be related to prognosis. Per-protocol effects can be legitimate targets, but estimating them requires methods and assumptions that address post-randomization selection rather than simply deleting nonadherent participants [1][3][6][9].

### Controls, Randomization, Concealment, and Blinding Solve Different Problems

The control should represent the relevant alternative. Depending on the question and ethics, it may be placebo, usual care, no additional treatment, another dose, or an active treatment. Placebo control can separate the investigational treatment from expectations and ancillary care when withholding active therapy is acceptable. Active control can answer comparative effectiveness or non-inferiority questions, but a poorly chosen margin or an ineffective implementation can make two treatments look similar without showing that either worked. Historical or external controls can be useful when concurrent randomization is infeasible, but changes in prognosis, measurement, and care can confound the comparison [1][2].

Random sequence generation prevents allocation from following prognosis or investigator preference. Allocation concealment protects that sequence until a participant is irrevocably enrolled; it is distinct from blinding after allocation. Central randomization or otherwise secure assignment can prevent an enrolling investigator from delaying, excluding, or advancing a participant after anticipating the next treatment. Randomization balances measured and unmeasured prognostic factors only in expectation, so chance imbalance can remain, especially in small trials [6][15].

Blinding protects behavior and assessment after assignment. Participants, clinicians, outcome assessors, adjudicators, statisticians, and decision committees are different roles and may have different access. Blinding is most consequential when knowledge of treatment can change co-interventions, symptom reports, follow-up, or subjective judgments. When blinding is impossible, credible alternatives include blinded outcome assessment, objective endpoints where appropriate, standardized care, prespecified decisions, and transparent disclosure. Calling a trial open-label does not make it invalid, but it identifies pathways that must be controlled or considered in the risk-of-bias judgment [1][5][6][15].

### Endpoints Must Represent Patient Benefit, Harm, and Time

An endpoint is not valid merely because it is easy to measure. Mortality, symptoms, function, quality of life, hospitalization, biomarkers, imaging findings, and composite outcomes differ in clinical meaning and susceptibility to bias. A surrogate endpoint may shorten follow-up when it reliably predicts how patients feel, function, or survive, but a biomarker response can fail to translate into patient benefit. Composite endpoints can increase event counts while obscuring that treatment mainly affected a less important component. The protocol should define the endpoint, assessment method, time point, adjudication, and handling of competing events before outcomes are known [1][3][4][5].

Treatment effects should be reported in units that support decisions. Relative risks and hazard ratios can show proportional change, while risk differences and numbers needed to treat show how baseline risk changes absolute benefit. The same relative effect can produce a large or small absolute benefit in populations with different baseline risk. Confidence intervals express sampling uncertainty under the analysis assumptions; they do not include bias from failed allocation, missing outcomes, outcome switching, or poor transportability. Statistical significance does not determine clinical importance, and failure to cross a threshold does not prove equivalence or absence of a meaningful effect [3][5][7].

Harms require the same design discipline as benefits. The protocol should define adverse events of special interest, collection periods, severity, attribution procedures, and stopping or escalation rules. Rare or delayed harms may remain undetected in a trial sized for a common efficacy outcome, and selective collection can make benefit evidence much more precise than harm evidence. A credible interpretation states what harms were actively sought, how much exposure and follow-up occurred, and which risks remain too uncommon or delayed for the trial to estimate [1][2][4][5].

### Sample Size, Multiplicity, and Monitoring Control Random Error and Opportunity

Sample-size planning connects the smallest important effect, expected event rate or variability, allocation ratio, desired precision or power, Type I error, attrition, clustering, and analysis method. A small trial can be appropriate for an early safety or pharmacology question, a rare disease, or a very large effect, but it should not claim to exclude moderate benefit or harm that it could not estimate. A large trial can estimate a trivial effect precisely while remaining biased if assignment, measurement, or follow-up are defective [1][4].

Multiplicity arises when a trial examines many primary outcomes, doses, treatment arms, subgroups, interim looks, or analytical variants. If every opportunity is treated as an independent confirmatory test without control, the chance of at least one favorable finding increases. Valid approaches include a prespecified hierarchy, alpha allocation, gatekeeping, or another multiplicity procedure suited to the objectives. Subgroup effects require interaction tests and biological or clinical justification; a significant result in one subgroup and a nonsignificant result in another does not itself demonstrate that treatment effects differ [3][5][10].

Adaptive designs permit prospectively planned modifications based on accumulating data. Examples include early stopping for efficacy or futility, sample-size re-estimation, dropping treatment arms, enriching enrollment, or changing allocation probabilities. Adaptation can improve efficiency and learning, but the rule, information flow, operating characteristics, and inferential correction must be specified and evaluated in advance. FDA warns that unadjusted changes based on comparative interim results can inflate Type I error and bias treatment-effect estimates; concealed interim access and simulation may be needed for complex designs [10]. Adaptation is therefore planned flexibility, not permission to redesign a trial after seeing a desired pattern.

Independent data-monitoring committees can review unblinded interim safety and efficacy information while investigators remain protected from comparative trends. Their charter should define membership, analyses, meeting procedures, decision guidance, confidentiality, and communication. Stopping early can be ethically necessary for clear harm, overwhelming benefit, or futility, but an early estimate may be unstable and follow-up may be insufficient for durability or uncommon harms. A recommendation should therefore weigh statistical evidence, totality of data, external evidence, safety, and the consequences of continuing or stopping [1][2].

### Protocol Deviations and Missing Data Change the Meaning of the Result

Nonadherence, treatment switching, rescue therapy, loss to follow-up, and competing events are not clerical imperfections. They can alter which treatment contrast is being estimated and can make outcomes missing for reasons related to prognosis. The protocol should reduce avoidable missingness, continue outcome collection after treatment discontinuation when appropriate, record reasons and timing, and distinguish an intercurrent event from an unobserved outcome. Deleting incomplete participants is not a neutral repair when missingness depends on treatment, health, or outcome [3][4][6].

A primary analysis must state the assumptions used for missing data and intercurrent events. Sensitivity analyses should test the robustness of inference to credible departures from those assumptions while targeting the same estimand. A supplementary analysis that answers a different question can be informative, but it is not a sensitivity analysis merely because its result differs. ICH E9(R1) emphasizes alignment among objective, estimand, estimator, and sensitivity analysis so that disagreement can be interpreted rather than hidden inside competing methods [3].

Protocol deviations also need provenance. Investigators should distinguish eligibility errors, missed visits, treatment errors, nonadherence, prohibited co-interventions, and analysis departures, then assess whether each threatens participant safety, data reliability, or interpretation. A modified analysis that excludes participants after randomization can destroy the original comparison. The safer default for an assignment effect is to retain randomized participants, disclose deviations, and use estimand-aligned methods rather than construct a cleaner but selected cohort [2][3][6].

### Internal Validity and Applicability Are Separate Questions

Internal validity asks whether the estimated contrast is credible for the enrolled participants under the study conditions. External validity asks whether it applies to another population, setting, clinician, treatment implementation, or time. Narrow eligibility, specialist centers, intensive follow-up, free treatment, and high adherence can improve control while making routine implementation less representative. Broad eligibility and ordinary-care delivery can improve relevance while creating variation that must be measured and handled [1][12].

PRECIS-2 treats explanatory and pragmatic design as a continuum across nine domains: eligibility, recruitment, setting, organization, flexibility of delivery, flexibility of adherence, follow-up, primary outcome, and primary analysis. It is a design aid, not a quality score. A trial can be highly pragmatic and biased, or tightly explanatory and internally valid but poorly applicable. The design should be as pragmatic as the decision requires and as controlled as credible inference requires [12].

Decentralized elements move activities such as visits, measurement, consent, or delivery away from conventional trial sites. They may reduce travel burden and widen access, but home measurement, local providers, digital tools, connectivity, and participant choice can introduce variable implementation or missingness. FDA's final 2024 guidance recommends specifying which activities occur remotely, standardizing procedures, training participants and local personnel, protecting data integrity, and managing safety and investigational products. Decentralization changes logistics and representation; it does not weaken the need for a defined estimand and reliable measurement [11].

Real-world data from records, claims, registries, devices, or routine care can support randomized pragmatic trials, external controls, safety studies, or nonrandomized comparisons. ICH E6(R3) describes fitness for purpose through reliability -- including accuracy, completeness, provenance, and traceability -- and relevance to the question. Nonrandomized studies additionally require a design that addresses confounding, selection, treatment timing, measurement, and overlap. Emulating a target trial can make eligibility, strategies, assignment, follow-up, outcomes, and analysis explicit, but it does not create randomization or remove unmeasured confounding [2][9].

### Registration, Reporting, Replication, and Synthesis Complete the Evidence Chain

Prospective registration and a public protocol create a time-stamped record of planned outcomes, analyses, and enrollment. SPIRIT 2025 aligns the protocol with registration, the statistical analysis plan, data sharing, funding, harms, and participant involvement [4]. CONSORT 2025 asks the completed report to disclose allocation, blinding, participant flow, deviations, outcomes, harms, analysis, registration, protocol access, and data-sharing information [5]. Registration and checklists do not guarantee honest or competent research, but they allow readers to compare what was planned, done, and reported.

Replication asks whether a result survives new participants, investigators, settings, and time. Exact procedural replication can test whether the original result recurs under closely matched conditions; pragmatic or comparative-effectiveness trials can test whether it travels into ordinary care. Differences do not have one automatic explanation: the original estimate may have been exaggerated, the replication may be imprecise, implementation may differ, or treatment effects may vary. Cumulative interpretation should compare effect estimates, uncertainty, protocols, populations, adherence, and bias rather than count how many studies crossed a p-value threshold [1][5][7].

Systematic reviews make the search and synthesis process explicit, but a pooled estimate inherits the limitations of included evidence. Cochrane's RoB 2 framework assesses bias arising from randomization, deviations from intended interventions, missing outcome data, outcome measurement, and selective reporting for a specific result [6]. GRADE then considers risk of bias, inconsistency, indirectness, imprecision, and publication bias when rating certainty for an outcome [7]. Meta-analysis can improve precision when studies address sufficiently coherent questions; it cannot turn incompatible estimands, biased trials, or unpublished outcomes into a trustworthy average.

## Evidence

### The Streptomycin Trial Demonstrated a Protected Comparison

The 1948 Medical Research Council study tested streptomycin plus bed rest against bed rest alone in patients with acute progressive bilateral pulmonary tuberculosis. Assignment schedules were prepared centrally from random sampling numbers, treatment was not known before enrollment, and radiographs were assessed without knowledge of assignment. Fifty-five participants entered the streptomycin group and 52 entered the control group; at six months the primary report recorded four deaths in the streptomycin group and 14 in the control group, alongside radiographic and bacteriological outcomes [16].

This case shows why a clinical trial is more than a treated series. The concurrent control represented what occurred under bed rest during the same period; protected allocation limited prognostic selection; masked assessment reduced judgment influenced by treatment knowledge; and a defined follow-up made the comparison auditable. The intervention still had toxicities, treatment delivery was visible, and the sample was too small to settle every benefit and harm. The evidentiary achievement was a bounded causal comparison, not complete knowledge about streptomycin [16].

### Meta-Epidemiology Shows That Design Defects Can Distort Effects

Wood and colleagues combined data from three meta-epidemiological studies, covering 146 meta-analyses and 1,346 controlled trials, to examine whether reported allocation concealment and blinding were associated with treatment-effect estimates. In 102 meta-analyses containing 804 trials, estimates from trials with inadequate or unclear allocation concealment were, on average, 17% more favorable than estimates from adequately concealed trials. The degree of bias varied among meta-analyses, and effects were more pronounced or more evident for subjectively assessed outcomes than for mortality [15].

The study compared trial characteristics across collections of trials rather than randomly assigning methodological defects, so residual confounding and imperfect reporting remained possible. A well-conducted trial can be poorly reported, and trial features cluster together. The result does not provide a correction factor that should be subtracted from every unblinded study. It supports an outcome-specific risk-of-bias judgment: allocation concealment matters before assignment, blinding matters most where knowledge can influence care or assessment, and uncertainty about conduct should reduce confidence rather than be converted into a mechanical penalty [15].

### RECOVERY Showed the Power and Boundaries of a Large Pragmatic Platform

The RECOVERY platform trial evaluated dexamethasone in hospitalized patients with Covid-19 across 176 National Health Service organizations in the United Kingdom. It randomly assigned 2,104 patients to dexamethasone and 4,321 to usual care, used 28-day mortality as the primary outcome, and analyzed treatment assignment by intention to treat. Death occurred in 22.9% of the dexamethasone group and 25.7% of usual care, an age-adjusted rate ratio of 0.83 with a 95% confidence interval from 0.75 to 0.93 [14].

The prespecified respiratory-support subgroups changed the clinical meaning. Dexamethasone reduced mortality among patients receiving invasive ventilation or oxygen, whereas patients receiving no respiratory support had 17.8% versus 14.0% mortality, with a rate ratio of 1.19 and a 95% confidence interval from 0.92 to 1.55. The latter interval did not establish benefit and allowed possible harm. The study therefore supported treatment for defined severity groups, not a general claim that every patient with Covid-19 should receive dexamethasone [14].

RECOVERY also illustrates pragmatic efficiency without evidentiary looseness. Broad hospital participation, a simple intervention, routine clinical outcomes, and a platform structure enabled rapid enrollment. Its open-label design was less threatening for the objective mortality endpoint than it would have been for a subjective symptom score, although co-intervention remained possible. Large size narrowed random error, while randomization, a prespecified protocol, complete vital-status follow-up, and subgroup interactions determined what the numbers meant [14].

### FDA Records Exposed How Selective Publication Alters the Evidence Base

Turner and colleagues obtained FDA reviews for 74 studies of 12 antidepressants involving 12,564 participants and matched them to journal publications. The FDA judged 38 of 74 studies positive, or 51%, while 48 of 51 published studies appeared positive, or 94%. Data from 3,449 participants were not published, and another 1,843 participants appeared in reports whose highlighted finding conflicted with the FDA-defined primary outcome [13].

Selection changed apparent magnitude as well as the count of positive trials. For every drug, the effect size derived from journal reports exceeded the effect size derived from FDA reviews; increases ranged from 11% to 69%, and the weighted mean effect size increased 32%, from 0.31 to 0.41. The study was limited to efficacy trials of antidepressants submitted to FDA and could not determine whether nonpublication decisions originated with investigators, sponsors, journals, or several actors. It nevertheless demonstrated directly that a literature composed only of visible reports can misrepresent the complete registered evidence [13].

This result explains why registration, result posting, protocol access, and systematic searches for unpublished evidence are part of trial validity at the evidence-base level. An internally credible trial that disappears still biases the accessible record, while outcome switching can make a completed trial communicate a different claim. WHO, SPIRIT, CONSORT, and ICH E6(R3) accordingly treat registration and public reporting as obligations, including when findings are negative [1][2][4][5].

### Evidence Appraisal Requires Both Study-Level and Body-Level Judgments

The Cochrane Handbook separates a risk-of-bias judgment for a specific trial result from certainty in a body of evidence. RoB 2 asks whether randomization, deviations, missing outcomes, measurement, and selective reporting could bias the result being used [6]. GRADE then asks whether the body is limited by those biases, inconsistent effects, indirect populations or interventions, imprecision, or publication bias [7]. This layered approach prevents a common error: calling all randomized evidence high quality regardless of conduct, or calling a pooled estimate certain because it is numerically precise.

The combined evidence supports a dependency model. The 1948 trial shows how allocation and assessment create a defensible comparison; the meta-epidemiological analysis shows that failures in those protections are associated with distorted estimates; RECOVERY shows how a large pragmatic platform can produce decision-changing evidence while preserving subgroup boundaries; and the antidepressant cohort shows that even completed trials can mislead collectively when results are selected. Trust is therefore not one property attached to the acronym RCT. It is the result of consistent protections from question formulation through public synthesis [13][14][15][16].

## Implications

### For Trialists: Design Backward From the Clinical Decision

The first practical task is to write the claim the trial should support, then design backward. Specify the patient population, treatment strategies, comparator, primary benefit and harm outcomes, time horizon, intercurrent events, effect measure, and smallest important difference. Translate that question into an estimand, choose an assignment and control capable of identifying it, and choose an estimator that preserves the design. If those elements cannot be stated coherently, adding sites, variables, or statistical complexity will not rescue the study [1][3][4].

Eligibility should balance safety, signal detection, recruitment feasibility, and applicability. Excluding people with common comorbidities, older age, concomitant treatment, language barriers, or limited digital access may simplify conduct while making the result less useful for routine care. Inclusion should not be indiscriminate: a population must have a defensible benefit-harm rationale and appropriate safeguards. The protocol should explain each important restriction and describe the population to which the effect is intended to apply [1][2].

The control and outcome should match the decision rather than convenience. A placebo comparison may establish efficacy but leave clinicians without direct evidence against current best treatment. A surrogate may accelerate learning but leave uncertainty about patient benefit. A composite may improve power while allowing a minor component to drive the result. The author's synthesis is a simple test: if the primary result were favorable, could a clinician explain exactly what changed for patients, compared with what alternative, over what time, and at what cost in harms? If not, the endpoint or comparator is not yet decision-ready [1][3].

The analysis plan should make favorable improvisation difficult. Prespecify primary and secondary outcomes, analysis populations, covariates, missing-data assumptions, multiplicity control, subgroup hypotheses, interim rules, and sensitivity analyses. Preserve exploratory work, but label it and seek new data for confirmation. An amendment made before comparative outcomes are known can be legitimate; an outcome redefinition chosen after a result appears is a different evidentiary act and must not be presented as the original test [3][4][5][10].

Quality management should focus on errors that could harm participants or change the answer. Perfect transcription of low-value data does not compensate for failed consent, predictable allocation, missing primary outcomes, treatment contamination, or inaccessible source records. ICH E6(R3) and WHO support risk-proportionate systems: identify critical-to-quality factors, prevent their failure, monitor them, and preserve traceability. This approach is stricter about consequential errors while avoiding bureaucracy that consumes resources without improving safety or reliability [1][2].

### For Clinicians and Patients: Read the Estimate as a Conditional Answer

A trial report should be translated into a sentence with explicit boundaries: in this enrolled population, assignment to this treatment strategy rather than this comparator changed this outcome over this period by this estimated amount, with this uncertainty and these observed harms. That sentence prevents a drug name, trial phase, p-value, or press-release conclusion from standing in for the actual treatment contrast [3][5].

Absolute effects should be reconstructed for the patient's baseline risk whenever possible. A relative reduction can look stable across risk groups while the number of events prevented differs materially. Confidence intervals should be inspected for both benefit and harm of clinically important magnitude. A small p-value does not resolve bias or applicability, and a large p-value does not prove equality. The relevant question is which effect sizes remain compatible with the data and whether those effects would change the decision [3][7].

Harms and burden deserve symmetric attention. Ask whether adverse events were actively collected, whether follow-up was long enough, whether withdrawals differed, and whether the trial was large enough to observe uncommon risks. Also ask about treatment inconvenience, monitoring, cost, and feasibility, because an efficacious regimen can fail in practice if delivery differs from the study. Evidence-based medicine then combines the external estimate with clinical circumstances and the patient's values; neither the trial nor clinician preference should erase the other [1][2][8].

Subgroups should be treated cautiously. A treatment effect can genuinely vary with disease severity, biology, timing, or background care, as RECOVERY's respiratory-support results demonstrate [14]. But searching many subgroups creates false patterns, and comparing one significant subgroup with one nonsignificant subgroup is not a valid interaction test. Credible heterogeneity is stronger when prespecified, supported by an interaction, clinically plausible, replicated, and measured with adequate information [3][5].

### For Reviewers, Guidelines, and Health Systems: Audit the Whole Evidence Path

Critical appraisal should begin with the trial's protocol and registry entry, not only the abstract. Reviewers should compare primary outcomes, time points, sample-size assumptions, analysis populations, amendments, participant flow, and harms across the protocol, statistical analysis plan, registry, report, and supplements. Missing information is not proof of misconduct, but it limits verification and should reduce confidence until resolved [4][5][6].

The risk-of-bias judgment should be result-specific. Lack of participant blinding may matter greatly for pain ratings and less for all-cause mortality; missingness may threaten one outcome more than another; an analysis that is valid for assignment may not estimate adherence. A quality score that adds unrelated checklist items can hide a fatal flaw behind many minor passes. Domain-level judgments make the causal pathway explicit and connect directly to sensitivity analysis or exclusion in synthesis [6][15].

Systematic reviews should search registries, regulatory records, and nonjournal sources; define eligible estimands and outcomes before screening; assess risk of bias; investigate heterogeneity; and show how conclusions change under plausible assumptions. Pooling should be refused when treatment versions, follow-up, outcome definitions, or effect measures answer materially different questions. When synthesis is appropriate, both relative and absolute effects, uncertainty, study limitations, and certainty should be reported [7][13].

Guidelines add a decision layer beyond evidence synthesis. They must consider benefit-harm balance, certainty, patient values, resources, equity, feasibility, and applicability. A strong recommendation based on a precise but indirect surrogate can be less justified than a conditional recommendation based on direct but imprecise patient outcomes. The author's assessment is that transparent separation of evidence, values, and implementation assumptions is safer than allowing a recommendation grade to conceal why action was chosen [7][8].

Health systems should support learning infrastructure before emergencies. Standing protocols, interoperable data, trained sites, ethics and governance capacity, and simple randomization systems can make large trials feasible when uncertainty is urgent. RECOVERY enrolled through ordinary hospitals because a platform and network could convert routine care into a protected comparison [14]. WHO's guidance favors sustainable trial ecosystems that can study endemic conditions and pivot during crises rather than rebuilding capacity after every emergency [1].

### For Adaptive, Decentralized, and Real-World Approaches: Innovation Must Preserve Identifiability

Adaptive design is valuable when uncertainty at launch can be converted into a prespecified decision. The design should state what can change, which data trigger change, who sees interim results, how error and estimation are controlled, and how operating characteristics were verified. If a modification is improvised after comparative results are known, the trial may still yield exploratory information, but its original confirmatory error guarantees no longer apply [10].

Decentralization should be judged component by component. Remote consent may improve reach but require identity, comprehension, privacy, and documentation safeguards. Home measurements may reduce travel while adding device, training, and environmental variation. Local clinicians can make participation feasible while increasing delivery heterogeneity. The protocol should standardize what must be standardized, measure what is allowed to vary, and analyze whether missingness or participation differs across access groups [2][11].

Real-world data do not become evidence merely by scale. A million incomplete records with ambiguous treatment timing can answer less than a small trial with protected allocation and complete outcomes. Before analysis, investigators should verify provenance, coding, coverage, timing, linkage, missingness, and whether the data contain the confounders and outcomes required for the target question. Randomization embedded in routine data can retain causal protection while improving efficiency; nonrandomized comparisons require explicit identification assumptions and sensitivity analysis for residual bias [2][9].

The author's synthesis is that innovation should be evaluated through invariants rather than labels. The clinical question must remain defined; treatment assignment or selection must be understood; measurements must be fit for purpose; analysis must follow the estimand; participant protection must remain proportionate; and reporting must expose deviations and uncertainty. Pragmatic, adaptive, decentralized, and real-world approaches are trustworthy when they preserve those invariants, not when novelty substitutes for them [1][2][3][10][11][12].

### A Practical Evidence Audit

A reader can audit a treatment claim with ten connected questions. What exact decision and estimand were specified? Who was eligible and who enrolled? What alternatives were compared? How was assignment generated and concealed? Which roles were blinded, and what protections replaced impossible blinding? Were outcomes patient-important, prespecified, completely observed, and measured comparably? Were sample size, interim looks, multiplicity, and subgroups planned? How were adherence, switching, missing data, and harms handled? Does the result apply to the intended patient and setting? Is the trial registered, fully reported, replicated, and consistent with the complete evidence base [1][3][4][5][6][7].

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

9. Hernan, M. A., and Robins, J. M. (2020; updated 2025). "Causal
   Inference: What If." Chapman & Hall/CRC.
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

## See Also

- `library/health-medicine/drug-development-from-molecule-to-medicine.md` -- places clinical trials within the wider pathway from candidate selection through postmarket evidence.
- `library/health-medicine/public-health-epidemiology.md` -- extends treatment evidence to populations, surveillance, and prevention.
- `library/mathematics-statistics/experimental-design.md` -- develops randomization, blocking, blinding, replication, and validity across experimental settings.
- `library/mathematics-statistics/causal-inference.md` -- explains estimands and identification assumptions for randomized and nonrandomized comparisons.
- `library/mathematics-statistics/hypothesis-testing-and-the-p-value-debate.md` -- distinguishes statistical thresholds from effect magnitude, uncertainty, and replication.