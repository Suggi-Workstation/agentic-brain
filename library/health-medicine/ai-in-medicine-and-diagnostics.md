---
name: ai-in-medicine-and-diagnostics
id: 20260829T131915Z
tier: library-topic
domain: health-medicine
author: Library Runner
tags: [artificial-intelligence, machine-learning, deep-learning, medical-imaging, clinical-decision-support, radiology, diagnostic-ai, large-language-models, algorithmic-bias]
links: [library/technology/large-language-models.md, library/health-medicine/drug-development-from-molecule-to-medicine.md, library/health-medicine/public-health-epidemiology.md]
---

# AI in Medicine and Diagnostics -- How Deep Learning Reached Clinician-Level Accuracy and Why Clinical Deployment Still Lags the Benchmarks

AI in medicine and diagnostics is the application of machine learning to
medical data -- most visibly images, but increasingly text and structured
records -- for the detection, classification, and triage of disease. Deep
learning systems now match or exceed clinicians on narrow image-interpretation
tasks in controlled studies, and the US Food and Drug Administration (FDA)
has authorized more than 1,400 AI-enabled medical devices, roughly three
quarters of them in radiology. Yet the field's defining tension remains
unresolved: benchmark accuracy has raced ahead of prospective clinical
evidence, and deployment is constrained by weak external validation,
algorithmic bias, and integration costs that no benchmark measures.

## Background

The idea of automated medical reasoning predates modern machine learning by
decades. In the 1970s, rule-based expert systems such as MYCIN -- developed at
Stanford by Edward Shortliffe to recommend antibiotic therapy for bacterial
infections -- encoded medical knowledge as hand-written if-then rules, and
INTERNIST-1 attempted the same for internal medicine diagnosis. These systems
could sometimes reason at the level of specialists, but they never entered
routine clinical practice, for a structural reason: the knowledge-acquisition
bottleneck. Every rule had to be authored and maintained by a human expert,
and medical knowledge outgrew the rule bases faster than they could be
updated. The same limitation afflicted the first commercial computer-aided
detection (CADe) systems for mammography, cleared by the FDA in 1998, which
flagged suspicious regions using hand-crafted image features. Eric Topol's
history of the field notes that this era demonstrated clinical AI's ambition
while exposing its fragility -- systems were rigid, brittle, and expensive to
maintain (Topol, 2019).

The turning point was the deep learning revolution. In 2012, a convolutional
neural network (CNN) called AlexNet won the ImageNet competition with an
error rate roughly half that of its nearest competitor, demonstrating that
networks trained on millions of labeled photographs could learn visual
features directly from data instead of relying on hand-engineered rules
(Topol, 2019). The technique transferred almost immediately to medicine:
medical images are, at the pixel level, the same kind of data as photographs,
and the same architectures that classified cats and dogs could be retrained
to classify tumors, hemorrhages, and lesions.

Two landmark papers marked the shift. In 2016, Google researchers trained a
CNN on 128,175 retinal fundus photographs graded by 54 ophthalmologists and
showed that it detected referable diabetic retinopathy with sensitivity and
specificity matching ophthalmologists on two independent validation datasets
(Gulshan et al., 2016). In 2017, researchers at Stanford trained a network on
129,450 clinical images and showed it could classify skin lesions at a level
on par with 21 board-certified dermatologists (Esteva et al., 2017). Both
studies were retrospective, but they established the core empirical claim
that now anchors the field: on narrow, well-defined visual tasks, learned
algorithms can match specialist human performance.

Regulation followed. On April 11, 2018, the FDA granted De Novo authorization
to IDx-DR (now LumineticsCore), an autonomous system that detects
more-than-mild diabetic retinopathy in adults with diabetes without a
clinician interpreting the image -- the first autonomous AI diagnostic system
authorized in any field of medicine (FDA, 2018). The authorization created a
new device classification (21 CFR 886.1100, product code PIB) that became
the predicate for subsequent 510(k) clearances of competitors such as EyeArt
(2020) and AEYE-DS (2022).

What followed was regulatory acceleration. FDA authorization of AI-enabled
devices grew from 6 in 2015 to 295 in 2025, a record year up 16.6 percent
from 2024, with a cumulative 1,451 AI-enabled devices authorized by the end
of 2025. Radiology dominates: 1,104 devices, or 76 percent of the list.
About 97 percent of authorizations came through the 510(k) pathway, which
requires substantial equivalence to a predicate device rather than new
clinical trials, and 62 percent of 2025 clearances were pure Software as a
Medical Device (SaMD), with 63 percent diagnostic in purpose (Healthcare AI
Insights, 2026; The Imaging Wire, 2025).

Most recently, the large language model (LLM) era arrived in medicine.
ChatGPT and its successors scored at or near passing thresholds on the United
States Medical Licensing Examination (USMLE) in 2022-2023 (Kung et al.,
2023), Google's Med-PaLM 2 reached 86.5 percent accuracy on the MedQA
USMLE-style benchmark (Singhal et al., 2024), and in February 2025 Aidoc's
CARE1 became the first FDA-cleared foundation-model-enabled medical device
(Healthcare AI Insights, 2026).

The stakes justify the attention. Diagnostic error contributes to a large
share of preventable harm, imaging volume grows faster than the radiologist
workforce, and screening access is scarce precisely where disease burden is
highest. But the evidence base lags the device count: among 717 radiology
devices with submission documentation, a 2025 systematic review found that
only 33 (5 percent) underwent prospective testing, 56 (8 percent) included
human-in-the-loop evaluation, and 208 (29 percent) incorporated any clinical
testing at all (FDA Approval of AI/ML Devices in Radiology systematic
review, 2025). The gap between what models can do in a paper and what they
have been shown to do in a clinic is the central problem of the field.

## Core Concepts

### Convolutional Neural Networks and Supervised Learning

Nearly all diagnostic imaging AI rests on supervised learning with
convolutional neural networks. A CNN learns a hierarchy of representations:
early layers detect edges and textures, middle layers detect shapes and
structures, and late layers assemble disease-relevant patterns such as
microaneurysms, hemorrhages, and exudates -- the lesions that define diabetic
retinopathy. The model is trained on labeled examples (images paired with
grades from human experts), adjusts millions of internal weights to minimize
classification error, and is then evaluated on data it never saw during
training. The Gulshan diabetic retinopathy study illustrates the scale
required: 128,175 images, each graded 3 to 7 times by a panel of 54
ophthalmologists, producing the labels that the network learned to imitate
(Gulshan et al., 2016).

The discipline of the train/validate/test split is the field's core
epistemic tool, and violating it is its most common sin. A model evaluated
on data drawn from the same hospitals, scanners, and patient populations it
was trained on will overestimate real-world performance, because it has
memorized the quirks of that data. The Liu meta-analysis found that of 82
eligible studies comparing deep learning with clinicians, only 25 used
external validation datasets, and the small subset with rigorous out-of-sample
validation showed performance closer to, rather than exceeding, clinicians
(Liu et al., 2019). External validation -- testing on data from a different
site, scanner vendor, or population -- is the single most important quality
signal in the field, and it is still the exception rather than the rule.

### The Three Deployment Modes: Autonomous, Assistive, and Decision Support

Medical AI deploys in three distinct configurations with very different
risk profiles. Autonomous AI makes a clinical decision without a clinician
reviewing the primary data. The reference example is IDx-DR, authorized to
diagnose more-than-mild diabetic retinopathy from retinal photographs taken
in primary care, with explicit scope constraints: adults 22 and older, with
a diabetes diagnosis, and no prior diabetic retinopathy diagnosis (FDA,
2018; Healthcare AI Insights, 2026). Assistive AI (computer-aided triage or
detection, CADt) flags or prioritizes findings for a human reader who
remains the decision-maker -- the dominant configuration among the 1,104
radiology devices on the FDA list. Clinical decision support (CDS) computes
risk scores or suggestions from structured data -- for example, sepsis
prediction, deterioration alerts, or LLM-generated summaries and treatment
suggestions -- and sits closest to the clinician's judgment. The triage
assistive mode is where most evidence of benefit accumulates, because it
combines machine throughput with human accountability (Xue et al., 2023).

### Regulatory Pathways: 510(k), De Novo, PMA, and PCCP

Understanding the FDA's pathways is essential to interpreting any claim
about an "FDA-approved" AI. The 510(k) pathway -- used for roughly 97
percent of AI-enabled devices -- clears a device by showing substantial
equivalence to an existing predicate; it is a market-entry mechanism, not a
requirement for new prospective clinical trials. The De Novo pathway
classifies novel device types without a predicate and was used for IDx-DR
(about 2-3 percent of authorizations). Premarket Approval (PMA), the most
demanding route with clinical evidence requirements, accounts for less than
1 percent of AI authorizations (Healthcare AI Insights, 2026). Because AI
models are updated after deployment, the FDA issued final guidance in
December 2024 on Predetermined Change Control Plans (PCCPs), letting
manufacturers describe planned modifications and their validation methods in
advance; 10 percent of 2025 clearances included PCCPs (Healthcare AI
Insights, 2026). The practical consequence: authorization answers "may this
be marketed," not "does it improve outcomes," and procurement must treat the
two questions separately.

### Generalizability and Dataset Shift

Dataset shift is the technical name for the field's deployment problem. A
model trained on images from one scanner vendor, one hospital network, or
one demographic composition encodes that distribution; when the input
distribution changes -- a different manufacturer, a sicker population, a
different image protocol -- performance degrades, sometimes silently. A 2025
JAMA Network Open study of the evidence underlying 691 FDA-authorized
AI-enabled devices documented how thin the generalizability evidence often
is, and a systematic review of radiology AI devices found that only a small
fraction of authorizations rested on prospective or human-in-the-loop
testing (Windecker et al., 2025; FDA Approval of AI/ML Devices in Radiology
systematic review, 2025). Aggarwal and colleagues reached the same
conclusion from the research side: of 279 studies, few compared algorithms
against clinicians on the same test set, reporting standards were poor, and
published accuracy estimates likely overstate true performance (Aggarwal et
al., 2021). The synthesis across these sources is that benchmark
performance is a ceiling, not a floor, for clinical performance.

### Algorithmic Bias and Proxy Labels

Algorithmic bias in medicine is not primarily a matter of malicious design;
it is the product of proxies. The canonical demonstration is Obermeyer and
colleagues' analysis of a widely used commercial risk-prediction algorithm
that targeted extra care to patients with complex health needs. The
algorithm used predicted healthcare cost as its proxy for health need --
and because Black patients receive less spending at every level of sickness
in the US system, the proxy encoded the disparity. At a given risk score,
Black patients were considerably sicker than White patients, and correcting
the proxy would have raised the share of Black patients flagged for
additional care from 17.7 percent to 46.5 percent (Obermeyer et al., 2019).
The same mechanism generalizes: any label that reflects access, billing, or
documentation rather than biology -- and any training set that
underrepresents a population -- produces a model that performs differently
across groups. Subgroup performance auditing is therefore not an
afterthought but a core requirement of safe deployment.

### Large Language Models in Medicine

The LLM wave extends medical AI from perception to language. The sequence of
benchmarks is striking: GPT-3.5 reached 60.2 percent on MedQA (USMLE-style
questions), Flan-PaLM 67.6 percent, GPT-4 86.1 percent, and Med-PaLM 2
achieved 86.5 percent -- above the roughly 60 percent pass threshold
(Singhal et al., 2023; Singhal et al., 2024). ChatGPT passed all three USMLE
steps at or near the passing threshold without medical fine-tuning (Kung et
al., 2023). On long-form answers to consumer medical questions, physicians
rated Med-PaLM 2's responses as reflecting medical consensus 72.9 percent of
the time, and specialists preferred Med-PaLM 2 answers over generalist
physician answers 65 percent of the time -- though specialists' own answers
were still preferred overall (Singhal et al., 2024). The failure modes are
equally well documented: hallucination, outdated knowledge, and plausible
but wrong reasoning, which is why grounded retrieval -- having the model
cite retrieved sources -- is a design requirement rather than a feature.
Med-PaLM 2's authors made this explicit by introducing "chain of retrieval"
precisely to anchor model claims in sources (Singhal et al., 2024).

### Clinical Integration and Human Factors

The least glamorous and most decisive layer is integration. A model that
works in a benchmark but slows workflow, fires alerts clinicians ignore, or
creates liability ambiguity will fail in practice. Automation bias -- the
documented tendency to over-trust machine outputs -- cuts both ways:
clinicians may accept wrong AI suggestions, or conversely override correct
ones out of distrust, and both behaviors erode net benefit (Topol, 2019).
Alert fatigue is the limiting factor for CDS tools, and the reimbursement
and liability arrangements for AI-assisted readings remain unsettled in
most health systems. The deployment gap is therefore a socio-technical
problem: the technical accuracy is the easy part; the workflow,
accountability, and economic fit are the hard part. Integration has a
concrete checklist of its own. Before deployment, a system should be run
silently on local data to confirm its operating characteristics at the
deploying site; its alerts must be triaged by severity to avoid fatigue;
the distribution of its inputs must be monitored for drift; and its outputs
must remain attributable to a named clinician in the record. None of these
steps appears in any accuracy benchmark, which is precisely why benchmark
performance and clinical value diverge in practice (Windecker et al., 2025;
Topol, 2019).

## Evidence

The empirical literature spans four tiers of evidence: retrospective
benchmark studies, prospective pivotal trials, meta-analyses comparing
algorithms with clinicians, and field studies of deployed systems. Each tier
has produced a distinct, stable finding.

The retrospective benchmark tier established that deep learning can match
specialists on narrow tasks. Gulshan and colleagues trained a CNN on 128,175
retinal images graded by 54 ophthalmologists and validated it on two
external datasets, EyePACS-1 (9,963 images) and Messidor-2 (1,748 images).
For detecting referable diabetic retinopathy, the algorithm achieved areas
under the receiver operating curve of 0.991 and 0.990, with sensitivity of
90.3 percent and 87.0 percent at specificity of 98.1 and 98.5 percent at the
high-specificity operating point, and 97.5 and 96.1 percent sensitivity at
the high-sensitivity point. The algorithm's F-score of 0.95 slightly
exceeded the median F-score of 0.91 across eight ophthalmologists grading
the same set (Gulshan et al., 2016; Peng and Gulshan, 2016). Esteva and
colleagues, training on 129,450 clinical images, demonstrated classification
of keratinocyte carcinomas and melanomas at a level on par with 21
board-certified dermatologists, making dermatology-level image
classification the model for the whole field (Esteva et al., 2017).

The prospective pivotal-trial tier is represented by IDx-DR. In a
prospective study of 900 participants across 10 primary care sites, the
system detected more-than-mild diabetic retinopathy with sensitivity of
87.2 percent against a prespecified target of above 82.5 percent,
specificity of 90.7 percent, and an imageability rate of 96.1 percent
(Abramoff et al., 2018; Medscape coverage of the pivotal trial, 2018). This
trial is the evidence model the rest of the device list mostly has not
followed: it was prospective, multisite, and evaluated against a
prespecified endpoint -- and it underpinned the first autonomous
authorization (FDA, 2018).

The meta-analytic tier delivers the field's most important correction.
Liu and colleagues, after a systematic search of the major medical
literature databases that yielded 82 eligible studies, found that only 25
of those studies used external validation, and that in the few studies with
rigorous out-of-sample validation, deep learning performance was equivalent
to -- not better than -- healthcare professionals, with pooled sensitivity
of 90.1 percent for algorithms versus 90.5 percent for clinicians in
matched samples, and pooled specificity of 93.3 versus 91.9 percent (Liu et
al., 2019). The review's most sobering observation was structural: of the
studies screened, a large majority reported algorithm performance alone,
never comparing it with human clinicians, which means the literature could
not support strong claims of machine superiority even where individual
papers made them. Aggarwal and colleagues' meta-analysis of 279 studies --
the largest appraisal to date -- reached the same caution from a different
angle. Most studies were retrospective, used artificially balanced test
sets in which disease prevalence was far higher than in real populations,
reported a shifting menu of metrics that made cross-study comparison
difficult, and only a small minority applied the same test set to both
algorithms and clinicians. The authors concluded that published accuracy
estimates likely overstate clinical performance and that externally
validated, head-to-head comparisons should be the standard before
deployment (Aggarwal et al., 2021).

The regulatory-evidence tier quantifies the same gap from the device side.
Among 717 radiology AI devices with submission documentation, only 33 (5
percent) underwent prospective testing, 56 (8 percent) included
human-in-the-loop evaluation, and 208 (29 percent) incorporated any
clinical testing; only 15 devices employed both prospective and clinical
testing, and 6 included all three (FDA Approval of AI/ML Devices in
Radiology systematic review, 2025). The device cohort itself is becoming
more software-shaped over time: 62 percent of 2025 clearances were pure
Software as a Medical Device rather than AI embedded in a scanner or
workstation, and 63 percent were diagnostic in purpose, which shifts the
evidence and governance burden from hardware validation toward model
monitoring, data routing, and cloud architecture (Healthcare AI Insights,
2026). Ten percent of 2025 clearances carried Predetermined Change Control
Plans, the mechanism the FDA finalized in December 2024 for governing
planned post-market model modifications (Healthcare AI Insights, 2026).

Taken together, the four tiers support a consistent reading. Retrospective
benchmarks show that deep learning can match specialists on narrow visual
tasks; the one prospective pivotal trial shows that an autonomous system
can meet prespecified endpoints in primary care; meta-analyses show that
human-plus-machine outperforms human alone and that unverified claims of
machine superiority are mostly artifacts of weak methods; and the
regulatory record shows that most authorized devices have not yet earned
prospective clinical evidence. The author's synthesis is that the field's
bottleneck has moved: accuracy is no longer the constraint, and rigorous
prospective evaluation in real workflows is.

The human-machine collaboration tier shows where benefit actually accrues.
Xue and colleagues' meta-analysis of 48 studies of image-based cancer
diagnostics -- with 25 contributing to statistical synthesis -- found that
deep-learning-assisted clinicians outperformed unassisted clinicians, with
pooled sensitivity of 88 percent versus 83 percent and pooled specificity
of 88 percent versus 86 percent, a consistent advantage across cancer types
and imaging modalities (Xue et al., 2023). The pattern that emerges across
tiers is coherent: machines alone match humans; machines plus humans beat
humans alone.

The deployed-systems tier demonstrates the failure modes of the evidence
gap. Obermeyer and colleagues documented large-scale racial bias in a
commercial algorithm affecting millions of patients, tracing it to the
cost-as-proxy mechanism described above and quantifying the correction at
17.7 to 46.5 percent of Black patients flagged (Obermeyer et al., 2019).
Windecker and colleagues examined the evidence supporting 691 FDA-authorized
AI devices and documented wide variability in the clinical evidence base
(Windecker et al., 2025), while the radiology-specific systematic review
quantified the same finding: 5 percent prospective testing, 8 percent
human-in-the-loop evaluation, and 29 percent any clinical testing among 717
radiology devices with submission documentation (FDA Approval of AI/ML
Devices in Radiology systematic review, 2025).

## Implications

For clinicians, the operative question is not whether machines will replace
them but which configuration of human and machine performs best -- and the
evidence points to augmentation. The Xue meta-analysis finding that
assisted clinicians outperform both unassisted clinicians and standalone
algorithms translates directly into practice: the highest-value deployments
are triage and second-read configurations where the algorithm preprocesses,
prioritizes, or checks, and the clinician retains authority (Xue et al.,
2023). This comes with obligations. Clinicians must manage automation bias
in both directions -- neither reflexive deference nor reflexive dismissal
-- and institutions must preserve the skill base that makes human oversight
meaningful, since deskilling quietly erodes the human side of the
human-machine pair (Topol, 2019). There are also unanswered questions of
accountability: when an assisted or autonomous system errs, responsibility
must remain assignable to a named professional, which is why autonomous
deployments so far are confined to narrow, constrained indications such as
the IDx-DR population limits rather than open-ended diagnosis (FDA, 2018).
For trainees, the practical implication is that clinical curricula must now
teach model interpretation and error -- how a system was validated, on whom,
and where it fails -- as a core clinical skill, not an elective.

For health systems and procurement, the regulatory landscape demands a
distinction most buyers currently blur. An FDA authorization -- 97 percent
of which are 510(k) clearances based on substantial equivalence -- certifies
marketability, not clinical benefit (Healthcare AI Insights, 2026). Systems
that treat the device list as an effectiveness list buy risk: a device whose
evidence base is retrospective and single-site needs local validation on
the purchasing system's own scanners, populations, and workflows before
deployment, plus continuous post-deployment monitoring, because dataset
shift degrades models silently (Windecker et al., 2025; Aggarwal et al.,
2021). The shift toward pure software devices compounds the operational
burden: 62 percent of 2025 clearances were Software as a Medical Device,
which enters the hospital through a different set of questions -- cloud
architecture, user provisioning, data routing, alert governance, model
monitoring, and contractual controls -- than an AI feature embedded in a
scanner (Healthcare AI Insights, 2026). The economic case for autonomous
screening is strongest where the alternative is no screening at all: the
IDx-DR model shows that a non-specialist-operated camera with autonomous
reading extends diabetic retinopathy screening into primary care settings
that lack ophthalmologists, converting a specialist bottleneck into a
point-of-care workflow (Abramoff et al., 2018).

For regulators and policymakers, three instruments follow from the
evidence. First, Predetermined Change Control Plans provide a mechanism for
governing post-market model updates, and their adoption (10 percent of 2025
clearances) needs to grow in step with the software-centeredness of the
device list (Healthcare AI Insights, 2026). Second, authorization standards
should reflect the tier of evidence a device actually possesses -- the 5
percent prospective-testing rate among radiology devices is a gap waiting
to produce harm, and the systematic review data suggest that a modest
requirement for prospective or human-in-the-loop evaluation would
discriminate the substantial from the speculative (FDA Approval of AI/ML
Devices in Radiology systematic review, 2025). Third, the Obermeyer finding
demonstrates that bias audits must operate on the ground-truth problem --
what the label measures -- rather than only on model outputs, and that
post-market equity surveillance is a regulatory responsibility, not a
vendor courtesy (Obermeyer et al., 2019).

For patients and public health, AI in diagnostics is an access technology
with an equity risk. The clearest benefit case is population screening in
under-resourced settings: diabetic retinopathy is a leading cause of
blindness whose early detection depends on specialists who are concentrated
where the disease is not, and autonomous screening extends detection into
primary care and community settings (Abramoff et al., 2018; FDA, 2018).
Google's retinopathy work was developed in collaboration with clinicians in
both the United States and India precisely because specialist grading
capacity is scarce where diabetes is prevalent (Peng and Gulshan, 2016).
The risk case is equally concrete: models trained and validated on
privileged populations, deployed without subgroup audits, can
systematically underserve the populations they were meant to help -- the
Obermeyer mechanism at diagnostic scale (Obermeyer et al., 2019). Patients
also have a stake in the transparency question that LLMs sharpen: when a
model drafts, summarizes, or suggests, the boundary between machine
contribution and clinician judgment must remain legible, because consent
and accountability attach to humans, not weights (Singhal et al., 2024).
The same principle extends to data governance: models trained on patient
data inherit questions of consent, security, and secondary use that no
technical benchmark addresses.

The implications also extend beyond clinical walls. The same deep learning
methods described here are reshaping drug development -- from target
identification to trial design -- which means the evidence-quality lessons
of diagnostics transfer directly to pharmaceutical applications: external
validation, subgroup audits, and prospective confirmation are as binding
for a target-prediction model as for a retinal screener. For public health,
AI-augmented screening changes the arithmetic of population programs: if
autonomous retinal screening becomes routine in primary care, the
bottleneck shifts from specialist capacity to the follow-up care pathway,
and epidemiology gains new case-finding tools whose sensitivity and
specificity are documented rather than assumed (Peng and Gulshan, 2016).
Across every domain, the transferable lesson is the same one the meta-
analyses teach: measure the system as deployed, not the model as published.

The trajectory implied by the evidence is specific and testable. Device
authorizations will keep growing; the fraction that matters is the fraction
backed by prospective, multisite, subgroup-audited evidence. The field's
history -- expert systems that reasoned but did not deploy, retrospective
models that overpromised, and one autonomous system that cleared a real
prospective bar -- suggests that AI in medicine will be judged less by
what it can compute than by what it can prove in a clinic. That is the
discipline this domain's next decade will be about.

## Common Pitfalls

Confusing authorization with validation is the most expensive error in the
field. A 510(k)-cleared device may have never been tested prospectively in
a clinic; buying on the strength of the FDA list is buying a legal status,
not an outcome (Healthcare AI Insights, 2026; Windecker et al., 2025).

Reporting only area under the curve on balanced test sets overstates
real-world value: disease prevalence is low, and sensitivity and specificity
at clinically chosen operating points on representative populations are the
numbers that matter (Aggarwal et al., 2021).

Skipping external validation is the research-side version of the same
failure. A model validated only on its training institutions' data has
memorized local quirks; the Liu meta-analysis shows how rarely external
validation is performed and how much it matters (Liu et al., 2019).

Proxy-label blindness produces biased systems that are technically
"accurate" by their own metrics. The cost-proxy algorithm in the Obermeyer
study was well calibrated to its target; its target was wrong (Obermeyer et
al., 2019).

Automation bias and alert fatigue are deployment killers. Models that
clinicians over-trust cause wrong decisions; models that over-alert get
ignored; both failings are behavioral, not technical, and neither is fixed
by a better architecture (Topol, 2019).

Treating LLM fluency as clinical reliability is the newest pitfall.
Benchmark scores on USMLE-style questions measure knowledge recall under
multiple-choice constraints, not the open-ended, source-grounded reasoning
real care requires; ungrounded LLM output in a clinical workflow is a
liability engine (Singhal et al., 2024; Kung et al., 2023).

## Sources

1. Gulshan, V. et al. (2016). "Development and Validation of a Deep Learning Algorithm for Detection of Diabetic Retinopathy in Retinal Fundus Photographs." JAMA, 316(22), 2402-2410. https://jamanetwork.com/journals/jama/fullarticle/2588763 [high]

2. Esteva, A. et al. (2017). "Dermatologist-level classification of skin cancer with deep neural networks." Nature, 542(7639), 115-118. https://www.nature.com/articles/nature21056 [high]

3. Abramoff, M.D. et al. (2018). "Pivotal trial of an autonomous AI-based diagnostic system for detection of diabetic retinopathy in primary care offices." npj Digital Medicine, 1, 39. https://www.nature.com/articles/s41746-018-0040-6 [high]

4. Medscape (2018). "AI Speeds Diabetic Retinopathy Diagnosis Without Specialist." Coverage of the IDx-DR pivotal trial results. https://www.medscape.com/viewarticle/901297 [medium]

5. FDA (2018). "FDA permits marketing of artificial intelligence-based device to detect certain diabetes-related eye problems." Press announcement, April 11, 2018. https://www.fda.gov/news-events/press-announcements/fda-permits-marketing-artificial-intelligence-based-device-detect-certain-diabetes-related-eye [high]

6. FDA. "Artificial Intelligence-Enabled Medical Devices." Authorized device list. https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-enabled-medical-devices [high]

7. Liu, X. et al. (2019). "A comparison of deep learning performance against health-care professionals in detecting diseases from medical imaging: a systematic review and meta-analysis." The Lancet Digital Health, 1(6), e271-e297. https://www.thelancet.com/journals/landig/article/PIIS2589-7500(19)30123-2/fulltext [high]

8. Aggarwal, R. et al. (2021). "Diagnostic accuracy of deep learning in medical imaging: a systematic review and meta-analysis." npj Digital Medicine, 4, 65. https://www.nature.com/articles/s41746-021-00438-z [high]

9. Xue, P. et al. (2023). "Unassisted Clinicians Versus Deep Learning-Assisted Clinicians in Image-Based Cancer Diagnostics: Systematic Review With Meta-analysis." Journal of Medical Internet Research, 25, e43832. https://www.jmir.org/2023/1/e43832 [high]

10. Obermeyer, Z., Powers, B., Vogeli, C. & Mullainathan, S. (2019). "Dissecting racial bias in an algorithm used to manage the health of populations." Science, 366(6464), 447-453. https://www.science.org/doi/10.1126/science.aax2342 [high]

11. Singhal, K. et al. (2023). "Large language models encode clinical knowledge." Nature, 620(7972), 172-180. https://www.nature.com/articles/s41586-023-06291-2 [high]

12. Singhal, K. et al. (2024). "Toward expert-level medical question answering with large language models." Nature Medicine. https://www.nature.com/articles/s41591-024-03423-7 [high]

13. Kung, T.H. et al. (2023). "Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models." PLOS Digital Health, 2(2), e0000198. https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000198 [high]

14. Windecker, D. et al. (2025). "Generalizability of FDA-Approved AI-Enabled Medical Devices for Clinical Use." JAMA Network Open, 8(4), e258052. https://doi.org/10.1001/jamanetworkopen.2025.8052 [high]

15. FDA Approval of Artificial Intelligence and Machine Learning Devices in Radiology: A Systematic Review (2025). PMC12595527. https://pmc.ncbi.nlm.nih.gov/articles/PMC12595527 [high]

16. Healthcare AI Insights (2026). "The FDA Approved AI Medical Device List Reached 1,451 in 2025." https://healthcareaiinsights.com/evidence-appraisals/fda-approved-ai-medical-device-list [medium]

17. The Imaging Wire / Innolitics (2025). "FDA AI Approvals Surge Past 1k for Radiology." 2025 AI/ML device 510(k) clearance statistics. https://theimagingwire.com/2025/12/10/ai-enabled-medical-devices-granted-fda-marketing-authorization/ [medium]

18. Peng, L. & Gulshan, V. (2016). "Deep Learning for Detection of Diabetic Eye Disease." Google Research Blog. https://research.google/blog/deep-learning-for-detection-of-diabetic-eye-disease/ [medium]

19. Topol, E. (2019). "High-performance medicine: the convergence of human and artificial intelligence." Nature Medicine, 25(1), 44-56. https://www.nature.com/articles/s41591-018-0300-7 [high]

## See Also

- `library/technology/large-language-models.md` -- the foundation models entering clinical workflows; this topic covers their medical application layer.
- `library/health-medicine/drug-development-from-molecule-to-medicine.md` -- machine learning is reshaping drug discovery through the same methods described here.
- `library/health-medicine/public-health-epidemiology.md` -- population-scale screening and surveillance are where autonomous diagnostics have their largest reach.
- `library/health-medicine/chronic-disease-cvd-diabetes.md` -- diabetic retinopathy screening is the flagship autonomous AI use case within chronic disease management.
- `library/science/neuroscience-brain-mind.md` -- artificial neural networks were loosely inspired by the brain; the parallel is real but limited.
