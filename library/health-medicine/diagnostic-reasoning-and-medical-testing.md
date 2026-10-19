---
name: diagnostic-reasoning-and-medical-testing
id: 20260930T144113Z
tier: library-topic
domain: health-medicine
author: Librarian
tags: [diagnostic-reasoning, medical-testing, pretest-probability, likelihood-ratios, diagnostic-error, clinical-decision-making, safety-netting]
links: [library/health-medicine/preventive-screening-and-overdiagnosis.md, library/health-medicine/clinical-trials-and-evidence-based-medicine.md, library/probabilistic-thinking-forecasting/bayesian-reasoning.md, library/probabilistic-thinking-forecasting/base-rate-neglect.md]
reviewed: 2026-10-19
---

# Diagnostic Reasoning Works When Tests Update Decisions Rather Than Replace Judgment

Diagnostic reasoning is the iterative process of turning a patient's history, examination, prior risk, and test results into a working explanation and a safe next action. A test adds value only when its possible results can change a consequential decision [13]; indiscriminate testing can instead create false reassurance, false alarms, incidental findings, harmful cascades, and neglected follow-up [2][8][9][16].

## Background

Diagnosis is not a single label attached at the end of a visit. The National Academies described it as a collaborative process of information gathering, clinical reasoning, communication, and explanation that must reach the patient and the care team in time to guide action [1]. The process begins when symptoms, signs, exposures, prior conditions, and the care setting make some explanations more plausible than others. It continues through testing, treatment response, consultation, and observation over time. The author's assessment is that a diagnosis can be provisional without being careless, and a workup can be incomplete without being unsafe, provided that the remaining uncertainty, follow-up plan, and triggers for escalation are explicit [1][10][11].

The intellectual roots of modern diagnostic reasoning join bedside medicine with probability and decision analysis. History and physical examination findings are themselves diagnostic information: each finding can increase, decrease, or barely change the probability of a proposed disease. Laboratory tests and imaging extend that process rather than creating a separate realm of certainty. The Institute of Medicine's 1989 probabilistic account of testing and later evidence-based diagnosis methods formalized the same relationship: pretest probability is revised by the observed result, and the size of the revision depends on how often that result occurs in people with and without the disease [3][13].

Pauker and Kassirer's threshold model added the decision that probability alone cannot supply. As presented in the Institute of Medicine's 1989 monograph, the model starts from a treatment threshold probability, the probability of disease at which treating and not treating are equally attractive, and derives two further boundaries from it: a lower no-treat/test threshold, below which neither testing nor treatment is worthwhile, and an upper test-treatment threshold, above which treatment should begin without waiting for another test. Testing is useful between those boundaries, where a result could move the probability across the treatment threshold and change the preferred action [13]. The boundaries depend on the test's true-positive and false-positive rates, the treatment threshold, and the burden of the test itself, and the treatment threshold in turn reflects the benefit of treating diseased patients relative to the cost of treating non-diseased patients [13]. A threshold is therefore not a universal number attached to a disease; it varies with the disease, the treatment, and clinician and patient risk tolerance [2][13]. It is a decision boundary for a particular patient, action, and clinical context. The model is normative rather than a description of practice: a primary-care researcher notes that explicit testing of specific hypotheses may occur in fewer than 40 percent of diagnostic episodes and that the model casts the patient as a passive party [18].

This framework helps explain why more testing is not automatically safer. Testing a patient whose probability is already far below the action threshold can generate an abnormality without making the target disease probable [10][13]. Testing a patient whose probability is already high can delay urgent treatment or produce a false negative that distracts from a coherent clinical picture. Testing can also find an unrelated abnormality that begins a cascade of repeat imaging, biopsy, consultation, or treatment [9]. A systematic review found wide variation in low-value testing across settings and definitions, while a national survey of US internists documented physician-reported harms after incidental findings [8][9]. The problem is not the existence of tests; it is ordering information without specifying how each result will alter care.

Diagnostic safety developed as a field because error was not adequately captured by traditional patient-safety programs. The National Academies defined diagnostic error around failure to establish an accurate and timely explanation or failure to communicate that explanation to the patient [1]. This definition makes the diagnostic process broader than a clinician's private thought. History taking, examination, test ordering, test performance, interpretation, referral, communication, result tracking, and follow-up can each fail. In a study of confirmed primary-care diagnostic errors, breakdowns often involved several of these processes at once [6].

The history and examination retain a central role because they establish the hypotheses, urgency, and pretest probabilities that make subsequent tests interpretable [2]. In a review of 190 confirmed primary-care diagnostic errors, problems with the history were identified in 56.3 percent of cases, problems with examination in 47.4 percent, and problems with ordering tests for further work-up in 57.4 percent [6]. In 100 cases of internist diagnostic error, flawed synthesis of the available information accounted for 264 contributing factors, compared with 45 for faulty data gathering and 11 for inadequate knowledge or skill [14]. These are selected error cases, so they show where reasoning fails rather than how often. This does not mean that bedside judgment should replace laboratory, imaging, pathology, or consultation. It means that a test answer has no clinical meaning until someone has defined the question, relevant population, result threshold, and action.

The boundaries of this topic are important. Preventive screening tests asymptomatic populations and is treated separately in `library/health-medicine/preventive-screening-and-overdiagnosis.md`. Clinical trials ask whether interventions cause outcomes and are treated in `library/health-medicine/clinical-trials-and-evidence-based-medicine.md`. Artificial-intelligence engineering, model architecture, and software regulation are outside the present scope, although an AI output used in diagnosis must meet the same requirements for intended population, calibration, threshold, workflow, and follow-up as any other test. The focus here is the clinical pathway from a patient's presenting problem to a probability-informed, patient-centered, and revisable decision.

## Core Concepts

### Start with the decision and the danger of delay

A diagnostic encounter should begin with two questions: what dangerous or consequential conditions must be considered, and what decision must be made now? The first prevents a common diagnosis from excluding a time-critical alternative. The second prevents a broad differential diagnosis from becoming an unranked list. An emergency decision about possible meningitis, a same-day decision about suspected venous thromboembolism, and a longitudinal evaluation of fatigue have different acceptable delays, false-negative costs, and testing thresholds [1][7][13].

Urgency changes how much uncertainty can be tolerated. When delay carries large irreversible harm and treatment is comparatively safe, the treatment threshold can be low. When treatment is toxic, invasive, or difficult to reverse, stronger evidence may be required. When both testing and treatment carry material risk, observation, consultation, or a staged test sequence may dominate. The author's synthesis is that the worst diagnostic error is not always a wrong label; it can be choosing an information-gathering plan whose delay or cascade is more harmful than the uncertainty it was meant to reduce [13].

The intended action should be written before the order where feasible. Examples include starting or withholding treatment, admitting or discharging, obtaining a definitive procedure, referring urgently, repeating an examination, or observing a defined trajectory. If neither a positive nor a negative result would alter any action, the test has no immediate decision value. It may still have research, prognostic, public-health, or documentation value, but that different purpose should be named rather than disguised as necessary diagnosis [13].

### Build and rank a differential diagnosis

A differential diagnosis is a set of competing explanations, not a ritual list of every imaginable disease. Each candidate should connect the patient's findings to a plausible mechanism, expected course, and discriminating evidence. Ranking combines prevalence in a defensible reference population, patient-specific risk factors, the fit of the history and examination, and the consequences of missing the condition. A rare but catastrophic disease may deserve active exclusion even when it is not the most likely explanation, while a common benign explanation may remain the working diagnosis if a safe follow-up plan can detect an unexpected course [1][2].

Good differentials remain open to revision. Premature closure, the failure to continue considering reasonable alternatives once an initial diagnosis has been reached, was the single most common cognitive factor in a study of 100 internist diagnostic errors, and 14 of the 23 failed-heuristic factors reflected the assumption that all findings share a single cause [14]. Yet simply listing more diagnoses is not a complete remedy. The AHRQ probability brief warns that education can reward suggestion of rare diseases with extremely small likelihood, which can undermine attention to prevalence and probability [2]. The corrective discipline is to ask what observed or future evidence would differ among the leading hypotheses and which difference would change management.

A diagnosis can coexist with another diagnosis. Comorbidity, treatment adverse effects, and independent incidental disease mean that a single explanatory story is not always sufficient [14]. At the same time, adding hypotheses without independent evidence can encourage panels of low-yield tests. The author's synthesis is to maintain a small ranked working set, a separate list of high-consequence exclusions, and explicit criteria for reopening the set. This preserves breadth without treating every logically possible disease as equally probable.

### Treat history and examination findings as probability updates

Symptoms and signs have sensitivity, specificity, and likelihood ratios just as laboratory tests do. Their value depends on elicitation, measurement, observer skill, disease spectrum, and timing. A finding with a likelihood ratio near one barely changes probability even if it sounds clinically impressive. A well-measured absence can be useful when it is uncommon in the target disease, while a classic sign can be weak if it also appears frequently in competing conditions [2][3].

History taking should establish onset, sequence, severity, associated features, exposures, medications, prior probability modifiers, and what the patient means by the symptom. A label such as dizziness, weakness, or chest discomfort can contain several distinct experiences with different differentials. The examination should be selected to discriminate among plausible explanations and to assess severity, not performed as an undifferentiated checklist. In confirmed primary-care diagnostic errors, history, examination, and ordering decisions frequently contributed to breakdowns [6]. That evidence comes from selected error cases rather than all encounters, so it identifies recurring failure points rather than a universal percentage of causation.

Repeated examination is a distinct diagnostic tool. Some diseases reveal themselves through evolution, response, or a new focal sign rather than through one test at one time. The test of time is useful only when paired with a safety net: the expected course, warning signs, time boundary, route back to care, and responsibility for review must be explicit [10]. Passive advice to return if worse can fail when the patient does not know what worse means, how quickly change matters, or whether reconsultation is welcome [10].

### Estimate pretest probability before interpreting the result

Pretest probability is the estimated chance of the target condition before the current test result is known. It can come from a validated clinical prediction rule, prevalence in a comparable population, prior tests, the history and examination, or a bounded clinical estimate. The estimate should match the actual setting: prevalence in a tertiary referral clinic is not automatically applicable to primary care, and a screening population is not interchangeable with symptomatic patients [2][3][4].

The estimate need not always be expressed as a precise percentage. Low, intermediate, and high categories can be useful if their boundaries correspond to decisions and the uncertainty is acknowledged. False precision is harmful when the underlying reference class is weak. However, an unspoken probability is still influencing the decision. Making it explicit enough to compare with testing and treatment thresholds exposes disagreements and prevents the test from silently determining its own prior [2][13].

Base rates are starting information, not an oracle. Age, symptoms, exposures, comorbidity, referral history, and earlier tests can move a patient away from a population average. The related library topic `library/probabilistic-thinking-forecasting/base-rate-neglect.md` shows why vivid case information can receive too much weight, but it also explains that the reference class must be defensible. The author's synthesis is to state the source population and show a probability range when more than one reference class is plausible.

### Use likelihood ratios to update, not to certify

A likelihood ratio compares how likely a result is in people with the disease with how likely it is in people without the disease. For a binary test, the positive likelihood ratio is sensitivity divided by one minus specificity; the negative likelihood ratio is one minus sensitivity divided by specificity. The odds form of Bayes' theorem is `posttest odds = pretest odds x likelihood ratio` [3][13]. A ratio above one raises the odds, a ratio below one lowers them, and a ratio near one contributes little information.

The same result produces different posttest probabilities at different starting risks. A positive result can be mostly false positives in a low-prevalence population despite high sensitivity and specificity, while the same result can be compelling in a selected high-risk group. A negative result can substantially reduce moderate risk without reducing high risk below a safe discharge threshold. The AHRQ pathway therefore requires interpretation in the context of pretest probability and rejects the notion that a test result is definitive by itself [2].

Likelihood ratios also apply to graded results. A very high biomarker value, a mildly abnormal value, and an indeterminate value should not be collapsed into one positive category if their evidential weights differ. Dichotomizing continuous information can hide this gradient and make a threshold look like a biological boundary. The test threshold remains important for action, but the underlying result can support a more refined update when the evidence provides result-specific likelihoods [3][4].

Dependence limits sequential multiplication. The posttest probability after one test serves as the pretest probability for the next only if the second test's sensitivity and specificity are the same whatever the first result was, a conditional independence assumption that is seldom tested in practice [13]. Two tests can share the same biological marker, specimen error, acquisition process, or selection mechanism, so multiplying their likelihood ratios as though they were independent counts shared evidence more than once. The author's synthesis is to use a validated multivariable pathway where available, or to treat correlated findings as one evidence cluster and show a sensitivity range rather than inventing independent precision.

### Distinguish sensitivity, specificity, predictive value, and calibration

Sensitivity is the proportion of people with the target condition who have the specified result. Specificity is the proportion without the condition who have the alternative result. Positive predictive value is the proportion of positive results that are true positives; negative predictive value is the proportion of negative results that are true negatives. Predictive values change with prevalence even when sensitivity and specificity remain similar [2][3][13]. Confusing sensitivity with the chance of disease after a positive result reverses the conditional probability.

Accuracy estimates are not immutable product specifications. Sensitivity and specificity are not fixed test properties: the relative numbers of false-positive and false-negative results vary across settings, depending on how patients present and which tests they have already undergone [4]. STARD 2015 therefore asks authors to report participant selection, intended use and clinical role of the test, setting, index-test procedures, reference standards, positivity cutoffs, indeterminate and missing results, timing, and precision, because each can change the apparent performance or its applicability [4]. If not all tested patients are included in the final analysis, or if only healthy controls are included, accuracy estimates may not reflect performance in clinical use, and estimates can also differ because of variable definitions of the reference standard [4].

Calibration asks whether stated risks correspond to observed frequencies. Risk estimates can be unreliable even when an algorithm discriminates well, for example when they are systematically too high for all patients, and a poorly calibrated model can be less clinically useful than a well-calibrated competitor with a lower area under the curve [19]. Since decisions depend on thresholds, the author's synthesis is that evidence for a test should include both how it separates patients and what its outputs mean at the local prevalence, threshold, and workflow.

### Use test and treatment thresholds

The threshold model separates three regions. Below the no-treat/test threshold, neither testing nor treatment is justified. Between that threshold and the test-treatment threshold, information can change the preferred action. Above the test-treatment threshold, the expected benefit of treatment exceeds the value of waiting for another test [13]. The monograph's guiding rule is to do a test only if the probability of disease could change enough to cross the treatment threshold [13]. The model is a simplification, but it makes the hidden logic of testing auditable.

Thresholds move with consequences. A highly harmful missed diagnosis lowers the willingness to stop testing. A dangerous definitive procedure raises the evidentiary burden before proceeding. A safe, effective, reversible treatment can justify action at lower probability than a toxic or irreversible treatment [13]. Test burden includes radiation, contrast, bleeding, infection, discomfort, delay, financial cost, incidental findings, and the possibility that an ambiguous result starts a cascade [2][8][9]. Patient preferences can change how these burdens are valued, especially when expected benefits and harms are close [1][2].

The value of information is therefore action-specific. A test with excellent analytic performance can have little value if every result leads to the same choice. A modest test can have high value if it reliably moves patients across a consequential boundary. The author's synthesis is to write a result-action table before testing: for each plausible result, what will be done, what uncertainty will remain, and what new harm can the branch create? An empty or identical table is evidence that the order should be reconsidered.

### Recognize false positives, false negatives, and incidental findings

A false positive indicates the target condition when it is absent; a false negative fails to indicate it when present. Neither is identical to misdiagnosis, because subsequent interpretation and confirmation can correct the result. Harm arises when a false positive becomes an unsupported disease label or a false negative closes the workup despite persistent risk. Low pretest probability magnifies the proportion of positive results that are false, while very high pretest probability can make a negative result insufficient to exclude disease [2][12][13].

Reference intervals create another source of abnormal findings. Many laboratory ranges contain the central 95 percent of values in a reference population, so approximately 5 percent of results from comparable healthy people fall outside the range by definition [12]. A Canadian analysis of family-physician ordering (Naugler and Ma) used this principle to estimate that a substantial share of abnormal results in the observed setting could be false positives; the authors also described limitations of the estimate [12]. Ordering large nonselective panels increases the chance that at least one value will be flagged even when no relevant disease is present [12].

Incidental findings are real observations unrelated to the original question. Some reveal important treatable disease, while others have uncertain or no clinical importance. In a national survey of US outpatient internists, 99.4 percent of respondents reported experiencing cascades after incidental findings, including cascades with clinically important and intervenable outcomes (90.9 percent) and cascades with no such outcome (94.4 percent), and most reported harms to patients and wasted effort, frustration, or anxiety for themselves [9]. The survey measured physician reports rather than independently adjudicated outcomes, so its percentages should not be treated as causal population rates. It nevertheless demonstrates that an incidental finding creates a new decision problem rather than an automatic obligation to pursue every possible abnormality.

### Make consultation, follow-up, and feedback part of diagnosis

Consultation adds expertise, another examination, or an alternative framing, but it does not transfer responsibility automatically. The referring clinician should state the unresolved question, urgency, relevant prior evidence, and what decision the consultation must inform. The consultant should communicate an assessment, confidence, alternatives, and follow-up needs. A referral placed without confirmation of receipt or completion leaves the diagnostic loop open [1][6][11].

Test-result management requires named ownership. Closed-loop communication means that a result is sent, received, acknowledged, interpreted, communicated to the patient, and acted on when action is needed [11][16]. A rapid review of systematic and narrative reviews on test-result communication in hospital settings grouped interventions into information technology, following up on results, and point-of-care testing; it found support for education, checklists or templates, and email notification for results pending at discharge, but described the empirical evidence of clinical impact for technology as weak [11]. Practitioners interviewed in the same study identified clear lines of responsibility as central to improvement [11]. An alert without a responsible recipient, escalation rule, and completion measure is notification rather than closure.

Feedback is the final learning mechanism. A clinician who never learns the later diagnosis cannot calibrate pretest estimates, pattern recognition, or safety-netting decisions. The National Academies and the AHRQ probability brief both identify feedback on diagnostic accuracy as important for improved diagnostic performance [1][2]. Feedback should include correct provisional diagnoses, errors, near misses, and cases that evolved despite reasonable initial care. Without that comparison set, learning can be distorted toward memorable failures and miss systematic overtesting.

## Evidence

### Observational estimates show that diagnostic error is common but hard to measure

Singh and colleagues combined three observational studies of US adults to estimate outpatient diagnostic error. Two studies used electronic triggers, one for unusual return-visit patterns after primary care visits and one for lack of follow-up of abnormal findings related to colorectal cancer; the third examined consecutive lung cancer cases. In all three, errors were confirmed by chart review and defined as missed opportunities to make a timely or correct diagnosis. Their extrapolation yielded an estimated diagnostic-error rate of 5.08 percent, approximately 12 million US adults annually, and the authors estimated from prior work that about one-half of the errors could potentially lead to severe harm [5]. The estimate depends on extrapolation from selected health systems and trigger definitions, and the authors state that it probably underestimates the true frequency because their triggers missed uncommon diseases and chart review misses errors tied to documentation problems [5]. It should be read as a population estimate with methodological boundaries rather than a direct census.

A separate study examined 190 confirmed primary-care diagnostic errors and found 68 unique missed diagnoses. Pneumonia, decompensated heart failure, acute renal failure, primary cancer, and urinary infection or pyelonephritis were among the most frequent. Breakdowns involved the patient-practitioner encounter in 78.9 percent of cases, referrals in 19.5 percent, patient factors in 16.3 percent, follow-up and tracking in 14.7 percent, and test performance or interpretation in 13.7 percent; 43.7 percent involved more than one process [6]. Because investigators selected confirmed error cases, most detected through unplanned returns or hospitalizations, these percentages describe the anatomy of those errors, not the rate of failure among all visits. They support a systems model in which reasoning, ordering, referral, and follow-up interact.

The 2022 AHRQ evidence review of emergency-department diagnosis included 279 studies and estimated that 5.7 percent of ED visits (95% confidence interval 4.4 to 7.1) involve at least one diagnostic error, which it extrapolated to 7.4 million errors among 130 million US ED visits annually. Fifteen diseases, led by stroke, myocardial infarction, aortic aneurysm and dissection, spinal cord compression and injury, and venous thromboembolism, accounted for an estimated 68 percent of serious misdiagnosis-related harms in the ED, and disease-specific error rates ranged from 1.5 percent for myocardial infarction to 56 percent for spinal abscess [7]. A separate disease-based analysis across ambulatory, emergency, and inpatient care estimated about 795,000 Americans permanently disabled or killed by misdiagnosis each year, with 15 diseases accounting for 50.7 percent of serious harms and five (stroke, sepsis, pneumonia, venous thromboembolism, and lung cancer) for 38.7 percent [17]. Both national figures are extrapolations: the ED review's authors recommend confirming its overall rates in US-based prospective studies [7], and the disease-based analysis relies on literature-derived estimates that its authors state cannot be directly verified [17]. The stronger findings are the concentration of serious harm in a bounded set of conditions and large variation in error rates by disease.

### History, examination, and synthesis failures remain consequential

Singh and colleagues' primary-care series found that, among 190 confirmed errors, problems with the history were present in 56.3 percent, problems with examination in 47.4 percent, and problems with ordering tests in 57.4 percent; no differential diagnosis was documented at the index visit in 81.1 percent. The authors concluded that preventive interventions should target common contributory factors, especially data gathering and synthesis in the patient-practitioner encounter, because disease-specific efforts are unlikely to be sufficient [6]. Graber and colleagues analyzed 100 internist diagnostic errors and identified system-related factors in 65 percent and cognitive factors in 74 percent, averaging 5.9 factors per case; faulty synthesis dominated the cognitive factors, premature closure was the single most common, and inadequate knowledge or skill appeared in only 11 factor instances [14]. Clusters of factors that tended to co-occur included an incomplete history and examination, failure to consider the correct candidate diagnosis, and premature closure [14]. Both studies are retrospective reviews of selected error cases, and their authors acknowledge hindsight bias [6][14], so they identify recurring failure points rather than rates of failure across all encounters.

These data do not prove that bedside findings are always superior to testing. They show that testing cannot compensate reliably for a malformed initial question. A high-technology result may be accurately reported and still mislead when the target disease, pretest probability, or competing explanation was chosen incorrectly.

### Probability research explains both missed disease and false alarms

AHRQ's probability-based diagnostic pathway requires clinicians to use history and examination to estimate pretest probability, select tests, and interpret each result through Bayes' theorem to obtain a posttest probability. The brief notes that clinicians often overestimate disease probability before and after testing and argues for clinically integrated probability training rather than isolated memorization of two-by-two tables [2]. The document is an evidence-informed issue brief, not a randomized trial of one educational program. Its value is the explicit diagnostic model and its synthesis of known reasoning failures.

A systematic review of 24 studies found that health professionals' estimates of post-test probability were generally poor, with a tendency to overestimate. Likelihood ratios were the least well understood accuracy measure (in one study, 17 percent of professionals could define a positive likelihood ratio, compared with 76 percent for sensitivity), and studies disagreed on whether likelihood-ratio presentations improved estimates [15]. Presenting accuracy data as natural frequencies improved estimation in five studies; in one randomized trial, 73 percent of participants estimated post-test probability correctly with natural frequencies plus graphics, compared with 23 percent with probabilities alone [15]. The review did not formally assess risk of bias and included mostly single-group studies of calculation tasks, so it shows a difficulty with probability presentation rather than a measured effect on patient outcomes [15].

The Institute of Medicine monograph presents the threshold model developed by Pauker and Kassirer, shows why testing adds little when pretest probability is very high or very low, and shows how a likelihood ratio determines the size of an update [13]. Deeks and Altman's likelihood-ratio account supplies the operational odds relationship [3]. Together these sources support a coherent framework; they do not supply one universal threshold for every disease or patient. Utilities, test performance, and available actions must be supplied from the clinical context.

STARD 2015 addressed a different evidentiary weakness: incomplete reporting of diagnostic-accuracy studies. Its 30-item list covers participant sampling, intended use and clinical role of the test, test and reference procedures, positivity cutoffs, blinding, indeterminate and missing results, analyses of variability, sample size, timing between tests, adverse events, and precision [4]. The STARD group notes that publishing the list is not sufficient to improve reporting, as the modest improvement after the 2003 version showed [4]. This suggests that adherence to a reporting list does not by itself show that a study is unbiased or that a test improves patient outcomes. The evidence chain remains analytic performance, clinical accuracy in the intended population, effect on decisions, and net effect on patients.

### Overtesting evidence is heterogeneous but consistently identifies harm mechanisms

Muskens and colleagues systematically reviewed 35 studies containing 118 assessments of diagnostic overuse. Estimates ranged from 0.09 to 97.5 percent. Median estimates differed by measurement lens: 11.0 percent for patient-indication assessments, 2.0 percent for patient-population assessments, and 30.7 percent for service-level assessments. Imaging dominated the literature, and low-risk preoperative testing and early imaging for uncomplicated low back pain were frequent subjects [8]. The wide range reflects clinical, definitional, and methodological heterogeneity; it is evidence against quoting one universal overtesting rate. The stable conclusion is that low-value testing occurs across care settings and can cause false positives, radiation or procedural burden, anxiety, cascades, and cost [8].

Ganguli and colleagues surveyed US outpatient internists about cascades after incidental findings; 376 completed the survey (response rate 44.7 percent) and responses were weighted to be nationally representative. Respondents reported that cascades had caused their patients psychological harm (68.4 percent of respondents), financial burden (57.5 percent), and physical harm (15.6 percent). For their most recent cascade, 33.7 percent said the test that revealed the incidental finding may not have been clinically appropriate, and 53.2 percent said no follow-up guideline existed to their knowledge [9]. These are self-reported experiences and perceptions, subject to the recall bias the authors acknowledge, and not independently validated incidence. The study nevertheless identifies three actionable gaps: avoid low-value initiating tests, provide accessible evidence-based guidance for incidental findings, and discuss the possibility and harms of incidental findings with patients [9].

Naugler and Ma examined abnormal laboratory results through the logic of 95 percent reference intervals and a mean abnormal result rate (MARR) metric developed by their group. In a Calgary family-physician population, an 8.6 percent MARR implied, under their simplified assumptions, that about 58 percent of abnormal results were likely false positives [12]. The authors note that the MARR was calculated from 39 analytes without disease-specific cutoffs, in one specialty, jurisdiction, and population, so the estimate should not be applied as a universal rate [12]. Its durable lesson is that indiscriminate panels generate abnormalities by design and that pretest probability is required to distinguish a signal from an expected tail value.

### Safety-netting and closed-loop follow-up are necessary but incompletely tested

Friedemann Smith and colleagues used a realist review to develop recommendations for safety-netting in primary care. They found that explaining diagnostic uncertainty, the expected course, the management and follow-up plan, and the reason for reconsultation could improve understanding and reduce false reassurance. They also emphasized documentation for continuity [10]. The review included research, guidelines, reports, web sources, books, and commentary, so it synthesized mechanisms across heterogeneous evidence rather than estimating one intervention effect. Its authors identified the limited evidence base as a gap [10].

Wright and colleagues combined a rapid review of systematic and narrative reviews with five practitioner interviews and a 15-member citizen panel on test-result communication in hospital settings. The reviews grouped interventions into information technology, following up on results, and point-of-care testing, and practitioners and patients emphasized technology and clear lines of responsibility [11]. Responsibility can diffuse: an intervention that notified two clinicians of an abnormal result was followed by a lower rate of follow-up, which Wright and colleagues attribute to each clinician believing the other would act [11]. In the underlying Veterans Affairs study, dual alerts roughly doubled the odds that an alert would not be read and followed up in a timely way (odds ratio 1.99, 95% confidence interval 1.06 to 3.48) [16]. Callen and colleagues' systematic review of 19 studies found that failure to follow up abnormal results ranged from 6.8 to 62 percent for laboratory tests and from 1.0 to 35.7 percent for radiology in ambulatory care, with missed cancer diagnoses among the reported consequences, and that results were still missed under electronic alert systems (for example, 4 percent of 1,017 critical imaging alerts) [16]. This evidence supports designing ownership and completion into the process rather than assuming that additional messages close the loop.

The combined record is asymmetric. There is substantial evidence describing error mechanisms, low-value testing, and communication failures, but less direct evidence that one universal debiasing or safety-netting intervention reduces severe patient harm across settings [1][10][11]. The author's synthesis is that improvement should use condition-specific, workflow-specific safeguards with measured outcomes: correct and timely diagnosis, time to action, missed follow-up, unnecessary procedures, patient understanding, and adverse events. Process adoption alone is not proof of safety.

## Implications

### For clinicians: use a bounded diagnostic loop

The author's synthesis is a nine-step loop. First, define the patient's problem in the patient's own terms and identify instability or time-critical threats. Second, build a ranked differential with common explanations, high-consequence exclusions, and plausible comorbidity. Third, estimate a bounded pretest probability for each decision-relevant target and name the reference class. Fourth, identify the action threshold and the consequences of delay, false positives, and false negatives. Fifth, choose a test only if at least one plausible result changes action. Sixth, interpret the observed result with its likelihood ratio, limitations, and dependence on prior tests. Seventh, make and communicate the current decision, including what remains uncertain. Eighth, close referrals and results with named ownership. Ninth, compare the later outcome with the earlier reasoning so calibration improves [1][2][3][11][13].

This loop is not a demand for formal arithmetic in every encounter. It is a structure for making the hidden logic visible. A clinician can use natural frequencies or qualitative probability ranges when exact values are unavailable. What should not remain hidden is whether a test is being used to rule in, rule out, stage severity, guide treatment, or relieve anxiety; what probability is being assumed; and what result would actually change care [2][13].

For low-risk patients, restraint should be active rather than dismissive. Explain why the target disease is currently unlikely, why a test may produce more false alarms than useful answers, what course is expected, which changes would raise concern, when review should occur, and how to return. For high-risk patients, do not let a weak negative result erase the pretest evidence. For intermediate-risk patients, select the test or sequence most likely to cross an action threshold with the least total harm [2][10][13].

A diagnostic time-out is most useful at transitions: before discharge, after an unexpected result, when the patient fails to improve, before an invasive confirmation, and when several tests have produced discordant answers. The questions are concrete: What else could explain the findings? What result does not fit? Is the patient inside the study population for this test? Are multiple results dependent? What is the harm of waiting, and what is the harm of pursuing the next branch? The evidence for generic reflection is limited: the National Academies list metacognition and debiasing among proposed strategies for improving clinical reasoning [1], and Graber and colleagues propose a complete differential and a prospective-hindsight question (what alternatives would be considered if the working diagnosis were wrong?) without testing them [14]. The author's assessment is that the time-out should therefore be tied to a specific decision and to outcome feedback.

### For patients and families: ask how the test changes the plan

Patients can improve the diagnostic process without assuming responsibility for professional interpretation. Useful questions include: What condition are we testing for? How likely is it before the test? What can the result miss? What can look positive when the condition is absent? What will we do after a positive, negative, or unclear result? What are the burdens of the test and its follow-up? When will the result arrive, who will review it, and how will I receive it? What should make me return sooner? These questions follow the National Academies' model of patients as diagnostic-team members [1].

A result should be communicated as a probability and action, not as a color on a portal. "Abnormal" can mean a small departure from a population reference range, a clinically important signal, a result expected from known disease, or a value requiring urgent action. "Negative" can mean that the target is less likely, not impossible. Natural frequencies can make the distinction visible: among a stated number of comparable patients, how many with and without disease would have this result [2][3][12][15].

Preferences matter when the trade-off is close. Some patients prioritize avoiding an invasive procedure, while others accept more testing to reduce a small risk of severe disease. Those preferences should influence thresholds only after the probabilities, available alternatives, and consequences are explained. Shared decision-making does not require clinicians to offer tests that cannot change care, and it does not require patients to accept a test merely because uncertainty remains [1][2][13].

Patients should not be told simply to call if worse. A safety net should identify the expected trajectory, specific warning signs, time limit, route of contact, and backup if the first route fails. When the clinician judges active review necessary, the appointment or tracking task should be arranged rather than transferred entirely to memory and access [10][11].

### For health systems: design ownership and measurement around the pathway

Health systems should treat diagnosis as a longitudinal service. Order entry, specimen collection, laboratory or imaging performance, interpretation, communication, referral, scheduling, patient access, and follow-up are one chain. Each transition needs a named owner, expected completion time, escalation rule, and visible status. Sending an alert is not completion. A result is closed only when the responsible person has interpreted it, communicated it appropriately, and completed or deliberately declined the next action with a recorded reason [1][11][16].

Electronic systems should reduce rather than multiply ambiguity. The author's assessment is that high-value functions include showing the indication and pretest estimate with the order, preventing duplicate tests, attaching result-specific guidance, distinguishing urgent from routine findings, tracking unacknowledged results, linking referrals to completion, and recording model or assay version. Alerts alone do not close the loop: in the Veterans Affairs studies reviewed by Callen and colleagues, results were still missed despite electronic alerts, acknowledging an alert did not reliably indicate that the result had been acted on, and alerts sent to two recipients were less likely to be read and followed up [16]. Every alert should answer who must act, by when, and how completion will be measured.

Laboratories and radiology departments are diagnostic partners. Reports should identify important limitations, indeterminate results, comparison studies, and recommended urgency without converting every incidental finding into an automatic cascade. Where evidence-based follow-up pathways exist, they can standardize action; where evidence is weak, the report should state uncertainty rather than imply that more testing is mandatory. Health systems should audit whether incidental-finding recommendations improve consequential outcomes or chiefly generate low-yield cascades [8][9].

The author's assessment is that dashboards need both underdiagnosis and overdiagnosis measures. Useful metrics include time from presentation to correct action for high-risk conditions, unexpected return visits, missed abnormal results, referral completion, proportion of tests ordered outside evidence-based indications, repeat testing, downstream procedures after incidental findings, diagnostic revisions, patient-reported understanding, and harm. A test-volume reduction target alone can encourage undertesting, while a detection target alone can reward false positives and incidental findings [7][8][9].

Feedback should reach individuals and teams in a learning system rather than only after litigation or severe harm. Case review should compare the evidence available at the time with later outcomes, distinguish reasonable uncertainty from preventable failure, and identify which pathway link should change. Near misses and correct restrained decisions belong in the learning set; otherwise clinicians may infer that ordering everything is the safest strategy [1][2].

### For educators: teach probability inside real decisions

Teaching should integrate probability with histories, examinations, and management thresholds. Learners can estimate a pretest range, express the test result as natural frequencies, update to a posttest range, and state whether the result crosses a decision threshold. The same case can be replayed with different prevalence, severity, test performance, or patient preferences to show why one rule does not transfer mechanically [2][3][13][15].

Disease recognition and feedback require deliberate practice. Learners should compare common and dangerous alternatives for the same presenting symptom, identify discriminating findings, and later receive the outcome. AHRQ describes repeated practice with clear, actionable feedback as an effective way to build an intuitive sense of probability and cautions against teaching probability only as memorized definitions and two-by-two tables [2]. Bias education can name premature closure or single-cause bias, but the author's assessment is that it should not imply that all errors originate in fast thinking or that simply slowing down repairs broken measurement or follow-up: in Graber's 100 cases, system-related and cognitive factors occurred together in 46 percent [14], and in Singh's primary-care series 43.7 percent of errors involved more than one process dimension [6].

Assessment should reward calibrated reasoning, not exhaustive testing. A high-quality answer can be a provisional diagnosis with a safe observation plan. Learners should receive credit for explaining why a test will not change management, for identifying when immediate treatment should precede confirmation, and for assigning responsibility for pending results. This aligns education with the actual diagnostic process rather than with a puzzle whose examiner already knows one final answer [1][2].

### For researchers and guideline developers: evaluate complete testing strategies

Diagnostic-accuracy studies should follow STARD and report the intended use, participant spectrum, setting, thresholds, reference standard, handling of missing and indeterminate results, time between tests, adverse events, and uncertainty [4]. External validation is necessary when prevalence, referral, equipment, readers, or competing diagnoses differ. A sensitivity and specificity pair from a selected study population should not be marketed as a context-free property.

Accuracy is an intermediate outcome. Where feasible, studies should compare complete strategies: who is tested, with which sequence and threshold, how results alter management, what confirmation follows, and whether patient-important outcomes improve. A more sensitive test can detect more disease and still worsen net outcomes if it creates many false positives, delays treatment, or finds abnormalities that do not benefit from intervention. Conversely, a modest test can improve outcomes when it targets a high-risk population and triggers an effective action [4][8][13].

Guidelines should specify probability thresholds or at least the risk categories and consequences that justify testing. They should state the intended population, result-action branches, stopping rule, follow-up responsibility, and evidence gaps. Incidental-finding guidance should distinguish strong evidence, consensus, and uncertainty. The national cascade survey suggests that absent or inaccessible guidance leaves clinicians and patients vulnerable to inconsistent follow-up [9].

Research on diagnostic safety should preserve denominators and avoid claiming one universal error rate. Trigger tools, malpractice claims, autopsy, chart review, and patient and clinician surveys observe different subsets of failure. Estimates should state the setting, error definition, harm definition, adjudication, and extrapolation assumptions [1][5][7]. Improvement trials should measure patient outcomes and balancing harms, not only checklist completion or reduced order counts.

### A practical stopping rule

The author's synthesis is that testing should stop when one of four conditions is met. First, the probability has fallen below a boundary where further work is less beneficial than observation and safety-netting. Second, the probability has risen above a boundary where action should begin and additional confirmation would add harmful delay. Third, the available tests cannot discriminate the remaining hypotheses enough to change management. Fourth, the patient, after informed discussion, prefers not to pursue a close and preference-sensitive trade-off. Stopping is not abandonment when the plan includes a working explanation, uncertainty, expected course, specific return triggers, and ownership of follow-up [2][10][13].

The opposite stopping rule also matters: reopen diagnosis when the course violates the prediction, a new discriminating finding appears, treatment response is inconsistent, a result was never closed, or another clinician or the patient supplies evidence the current explanation did not account for. Diagnostic reasoning is safe not because it eliminates uncertainty, but because it turns uncertainty into explicit probabilities, bounded actions, and reliable opportunities to correct the course.

## Sources

1. National Academies of Sciences, Engineering, and Medicine. (2015).
   "Improving Diagnosis in Health Care." National Academies Press.
   https://doi.org/10.17226/21794 [high]

2. Agency for Healthcare Research and Quality. (2022). "Improved
   Diagnostic Accuracy Through Probability-Based Diagnosis: Probability
   and the Diagnostic Pathway."
   https://www.ahrq.gov/diagnostic-safety/resources/issue-briefs/probabilistic-thinking3.html [high]

3. Deeks, J. J., and Altman, D. G. (2004). "Diagnostic Tests 4:
   Likelihood Ratios." BMJ, 329, 168-169.
   https://doi.org/10.1136/bmj.329.7458.168 [high]

4. Bossuyt, P. M. et al. (2015). "STARD 2015: An Updated List of
   Essential Items for Reporting Diagnostic Accuracy Studies." BMJ,
   351, h5527. https://doi.org/10.1136/bmj.h5527 [high]

5. Singh, H., Meyer, A. N. D., and Thomas, E. J. (2014). "The
   Frequency of Diagnostic Errors in Outpatient Care: Estimations From
   Three Large Observational Studies Involving US Adult Populations."
   BMJ Quality & Safety, 23, 727-731.
   https://doi.org/10.1136/bmjqs-2013-002627 [high]

6. Singh, H. et al. (2013). "Types and Origins of Diagnostic Errors in
   Primary Care Settings." JAMA Internal Medicine, 173, 418-425.
   https://doi.org/10.1001/jamainternmed.2013.2777 [high]

7. Newman-Toker, D. E. et al. (2022). "Diagnostic Errors in the
   Emergency Department: A Systematic Review." AHRQ Comparative
   Effectiveness Review No. 258.
   https://doi.org/10.23970/AHRQEPCCER258 [high]

8. Muskens, J. L. J. M. et al. (2022). "Overuse of Diagnostic Testing
   in Healthcare: A Systematic Review." BMJ Quality & Safety, 31,
   54-63. https://doi.org/10.1136/bmjqs-2020-012576 [high]

9. Ganguli, I. et al. (2019). "Cascades of Care After Incidental
   Findings in a US National Survey of Physicians." JAMA Network Open,
   2, e1913325. https://doi.org/10.1001/jamanetworkopen.2019.13325 [high]

10. Friedemann Smith, C., Lunn, H., Wong, G., and Nicholson, B. D.
    (2022). "Optimising GPs' Communication of Advice to Facilitate
    Patients' Self-care and Prompt Follow-up When the Diagnosis Is
    Uncertain: A Realist Review of Safety-netting in Primary Care."
    BMJ Quality & Safety, 31, 541-554.
    https://doi.org/10.1136/bmjqs-2021-014529 [high]

11. Wright, B. et al. (2020). "Closing the Loop on Test Results to
    Reduce Communication Failures: A Rapid Review of Evidence, Practice
    and Patient Perspectives." BMC Health Services Research, 20, 897.
    https://doi.org/10.1186/s12913-020-05737-x [high]

12. Naugler, C., and Ma, I. (2018). "More Than Half of Abnormal Results
    From Laboratory Tests Ordered by Family Physicians Could Be
    False-positive." Canadian Family Physician, 64(3), 202-203.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC5851398/ [high]

13. Sox, H., Stern, S., Owens, D., et al.; Institute of Medicine (US)
    Council on Health Care Technology. (1989). "The Use of Diagnostic
    Tests: A Probabilistic Approach." Chapter 2 in Assessment of
    Diagnostic Technology in Health Care: Rationale, Methods, Problems,
    and Directions. National Academies Press.
    https://www.ncbi.nlm.nih.gov/books/NBK235178/ [high]

14. Graber, M. L., Franklin, N., and Gordon, R. (2005). "Diagnostic
    Error in Internal Medicine." Archives of Internal Medicine,
    165(13), 1493-1499. https://doi.org/10.1001/archinte.165.13.1493 [high]

15. Whiting, P. F. et al. (2015). "How Well Do Health Professionals
    Interpret Diagnostic Information? A Systematic Review." BMJ Open,
    5(7), e008155. https://doi.org/10.1136/bmjopen-2015-008155 [high]

16. Callen, J. L., Westbrook, J. I., Georgiou, A., and Li, J. (2012).
    "Failure to Follow-Up Test Results for Ambulatory Patients: A
    Systematic Review." Journal of General Internal Medicine, 27(10),
    1334-1348. https://doi.org/10.1007/s11606-011-1949-5 [high]

17. Newman-Toker, D. E. et al. (2024). "Burden of Serious Harms From
    Diagnostic Error in the USA." BMJ Quality & Safety, 33(2), 109-120.
    https://doi.org/10.1136/bmjqs-2021-014130 [high]

18. Donner-Banzhoff, N. (2018). "Solving the Diagnostic Challenge: A
    Patient-Centered Approach." Annals of Family Medicine, 16(4),
    353-358. https://doi.org/10.1370/afm.2264 [high]

19. Van Calster, B. et al. (2019). "Calibration: The Achilles Heel of
    Predictive Analytics." BMC Medicine, 17, 230.
    https://doi.org/10.1186/s12916-019-1466-7 [high]

## See Also

- `library/health-medicine/preventive-screening-and-overdiagnosis.md` --
  applies probability and net-benefit logic to testing people without
  relevant symptoms.
- `library/health-medicine/clinical-trials-and-evidence-based-medicine.md`
  -- evaluates the intervention evidence that diagnostic decisions later use.
- `library/probabilistic-thinking-forecasting/bayesian-reasoning.md` --
  develops the formal prior, likelihood, and posterior framework.
- `library/probabilistic-thinking-forecasting/base-rate-neglect.md` --
  explains why vivid evidence can overwhelm relevant prevalence.
