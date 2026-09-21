---
name: information-architecture-and-content-design
id: 20260921T091555Z
tier: library-topic
domain: communication
author: Librarian
tags: [information-architecture, content-design, findability, taxonomy, navigation, accessibility]
links: [library/communication/writing-craft-and-style.md, library/communication/semiotics-and-meaning-making.md]
reviewed: 2026-09-21
---

# Information Architecture and Content Design -- Structure Determines Whether Information Can Be Found and Understood

Information architecture and content design make information usable by aligning organization, labels, navigation, search, and page structure with the tasks and language of the people who need it. Their central claim is that clear prose is not sufficient: information must also appear in an expected place, under a meaningful name, through more than one usable route, and in a form whose relationships remain perceptible to people and machines ([1] [8] [9] [10]).

## Background

Information architecture emerged as a response to a problem that grew with networked publishing: producing information became much easier than arranging it into a coherent environment. Rosenfeld, Morville, and Arango define the field broadly through systems for organizing, labeling, navigating, and searching information, and through the design of information spaces that help people complete tasks and understand where they are. The field draws on library classification, information retrieval, human-computer interaction, wayfinding, and communication design, but its practical object is not a discipline-specific theory. It is the experience of a person trying to locate, interpret, and act on information within a larger body of content ([1]).

Content design developed around the related observation that a page should not begin with what an institution wants to publish. It should begin with evidence of what a person needs to know or do. GOV.UK expresses that position operationally: every published content item should meet a valid user need, and user needs should be framed around a person's task or action rather than a predetermined document ([3]). Its current guidance adds that designers must decide the appropriate amount, format, and place for content, use clear and accessible language, and keep published information current ([11]). Content design therefore joins editorial judgment to structure. It asks not only how a sentence should be written, but whether the sentence belongs on this page, whether the page should exist, how it relates to other content, and what route should lead a user to it.

Information architecture and content design overlap without being identical. Information architecture operates primarily at the level of systems and relationships: content types, taxonomies, hierarchies, labels, navigation, metadata, search, and cross-channel coherence. Content design operates primarily at the level of user needs, page purposes, sequences, formats, headings, links, and maintenance. The boundary is porous because a label is simultaneously a taxonomic decision and a piece of writing, while a page's purpose affects both its content and its location. The author's synthesis is that the two disciplines form a single causal chain: user needs determine content requirements; content requirements determine models and relationships; those relationships determine routes and labels; and page structure determines whether the information is understood after it is found ([1] [3] [11]).

A sitemap is one representation of that chain, not the architecture itself. Nielsen Norman Group distinguishes a sitemap, which visualizes pages in a hierarchy, from the broader work of inventorying and auditing content, defining taxonomies, researching users, and designing organization, navigation, search, and metadata ([12]). This distinction matters because a tidy diagram can conceal vague labels, duplicate pages, missing metadata, inaccessible headings, or routes that reflect an internal organization rather than a user's task. Information architecture is the set of decisions and rules that produces the visible map and the less visible retrieval behavior behind it.

The human-centered basis of the work is formalized beyond web practice. ISO 9241-210:2019 specifies requirements and recommendations for human-centered design activities throughout the life cycle of interactive systems, including planning, understanding context, developing design solutions, and evaluating them against requirements ([2]). Applied to information, the standard's life-cycle orientation rejects the idea that architecture is a one-time launch artifact. Users, inventories, terminology, laws, products, and channels change. The structures that mediate them therefore require observation, evaluation, and revision.

Information-foraging research supplied a cognitive account of why structural cues matter. Pirolli, Card, and Van Der Wege describe information scent as proximal cues that indicate the likely value, cost, and location of information not yet seen; link text and surrounding summaries are examples of such cues ([4]). A user does not know the destination in advance. The user estimates whether a label, category, result, or branch is worth following. Structure is consequently communicative before it is navigational: every node makes a promise about what lies beyond it. Weak or misleading promises increase search effort even when the target technically exists.

Accessibility standards make the same structural problem explicit. WCAG 2.2 requires information, structure, and relationships conveyed visually to be programmatically determinable or available in text; its guidance also requires headings and labels to describe topic or purpose ([8] [10]). WCAG further calls for more than one way to locate pages within a set, except where a page is a step in a process ([9]). These requirements show that architecture is not merely a matter of visual menus. Headings, lists, regions, relationships, tables of contents, search, sitemaps, and related links create an information environment that must survive different displays and assistive technologies.

The field's enduring problem is therefore coordination across scales. A reader encounters individual words and pages, while an organization manages collections, workflows, owners, and channels. Good architecture connects those scales with explicit models and tested rules. Poor architecture leaves every page locally plausible but makes the collection globally confusing. The distinction explains why findability and comprehension are system properties rather than qualities that can be secured by editing isolated pages alone ([1] [8] [12]).

## Core Concepts

### Begin with user tasks, not the publisher's structure

A user need identifies who needs something, what that person must find or do, and why the outcome matters. GOV.UK recommends recording evidence for the need and defining acceptance criteria that describe when it has been met ([3]). These criteria turn an abstract audience description into testable information requirements. For an applicant, for example, success may require understanding eligibility, preparing evidence, submitting information, and knowing what happens next. Each requirement can then be mapped to content, navigation, and measurements.

Task orientation prevents a common structural error: copying an institution's departments, product lines, or policy categories into public navigation. Fang and Holsapple's experiments compared subject-oriented, usage-oriented, and combined navigation structures. Usage-oriented and combined hierarchies produced significantly better performance usability than a subject-oriented hierarchy for both simple and more complex knowledge-acquisition tasks ([7]). The result does not imply that every subject taxonomy should disappear. It shows that a classification can be internally rigorous yet externally inefficient when it fails to match the purpose that brought a user to the system.

A practical task model records the trigger, desired outcome, prerequisite knowledge, likely vocabulary, constraints, and next action. The author's synthesis is that this model should govern both macro-architecture and page content. Categories should expose recognizable goals, page titles should name the promised outcome, and body sections should follow the order in which decisions must be made. The same model supplies test tasks later, preserving traceability from research through evaluation ([2] [3]).

### Inventory before reorganizing

Architecture begins with evidence about the actual collection. A content inventory records what exists, while a content audit evaluates whether each item should be retained, revised, merged, redirected, or removed. Nielsen Norman Group identifies inventories and audits as distinct IA activities and treats their outputs as inputs to taxonomy and navigation decisions ([12]). Without them, teams design a new hierarchy around an imagined corpus and discover late that duplicates, obsolete material, unsupported formats, and ownership gaps do not fit it.

The author's synthesis is that an effective inventory assigns each item stable attributes such as identifier, title, URL or location, content type, audience or task, owner, status, review date, sensitivity, language, relationships, and evidence of use. The exact fields vary by context, but decisions should be made from a structured record rather than from memory. The author's assessment is that inventory data also exposes organizational risk. A page with no owner, no review rule, and no relationship to a validated need is not simply untidy; it is an uncontrolled claim that may become wrong without anyone noticing ([12]).

Auditing should separate content quality from structural fit. A page can be accurate but redundant, useful but mislocated, popular but aimed at the wrong task, or well written but unreachable. Conversely, low traffic is not conclusive evidence of low value because weak labeling or poor navigation may suppress visits. This suggests that audit judgments should combine content review with search queries, referral paths, task evidence, and user testing rather than treating page views as a verdict ([11] [12]).

### Model content as reusable types and relationships

A content model defines recurring types, their required fields, and the relationships among them. A policy, procedure, eligibility rule, product, person, event, and glossary term are different types because users ask different questions of them. Modeling those differences makes structure explicit: a procedure may require prerequisites, ordered steps, exceptions, evidence, completion signals, and related policies; a person record may require role, authority, dates, and organizational relationships ([1]).

Models separate meaning from a particular page layout. The same structured content can support a web page, search result, in-product instruction, voice response, or generated index without losing its identity. This is not primarily a platform-architecture claim; it is a communication claim about preserving semantics across presentations. WCAG's requirement that relationships be programmatically determinable reinforces the same principle at the rendered-content level: meaning encoded only by visual position or styling is fragile when presentation changes ([8]).

Relationships should be named rather than left implicit. "Part of," "applies to," "supersedes," "requires," "example of," and "related to" have different consequences for navigation and interpretation. The author's synthesis is that named relationships allow systems to generate useful routes while constraining misleading ones. A generic related-content block can connect pages by superficial similarity; an explicit "prerequisite for" relationship can guide a user through a task in the correct order ([1] [8]).

### Build taxonomies from distinctions users can apply

A taxonomy is a controlled system of categories and terms used to classify content. Hierarchies express broader and narrower relationships, while facets classify the same item along independent dimensions such as topic, audience, format, location, or status. Controlled vocabularies reduce variation by selecting preferred terms and mapping synonyms, abbreviations, deprecated labels, and alternative spellings to them ([1] [12]). These structures support browsing, filtering, indexing, and consistent metadata.

Categories must be mutually intelligible even when they cannot be perfectly exclusive. Real information often belongs in more than one place, so polyhierarchy or faceted access may represent user expectations better than forcing a single canonical path. Multiple placement should not mean copying the content. One maintained item can appear through several governed classifications. This approach preserves a source of truth while allowing different audiences to begin from different conceptual frames ([1] [9]).

The decisive quality is whether users can predict category contents from the label. Internal jargon, broad containers such as "Resources," and clever campaign language provide weak evidence about a destination. Information-scent guidance emphasizes that link text and accompanying summaries should use language the intended audience understands and should communicate the value of the destination ([14]). A controlled vocabulary therefore needs both governance and research: governance to keep terms consistent, and research to determine whether the terms mean what designers think they mean.

Card sorting can reveal patterns in how representative participants group and name content. Open card sorting lets participants create groups and labels, while closed sorting asks them to place items into predefined groups. The method supplies evidence about mental models but does not mechanically generate a correct taxonomy. Katsanos and colleagues found substantial consistency among groups with similar profiles, yet they also noted that final structures require qualitative interpretation, workable labels, information scent, and design constraints ([6]). Card-sort output is evidence for architectural judgment, not a substitute for it.

### Design navigation as a set of complementary routes

Navigation exposes selected relationships at useful moments. Global navigation communicates the major stable areas of a system; local navigation shows options within the current area; contextual links connect relevant items; sequential navigation supports ordered tasks; breadcrumbs communicate location and ancestry; and indexes, sitemaps, and search provide alternative strategies ([1] [9]). A single hierarchy cannot satisfy every information-seeking behavior, so the route set should be designed as a system rather than as competing menus.

WCAG's multiple-ways criterion gives this principle an accessibility basis. Search may be easier than traversing a large menu for a person using magnification or a screen reader, while a table of contents or sitemap may provide an overview that is more comprehensible for someone with cognitive limitations ([9]). Alternative routes are not redundant decoration. They allow people with different goals, knowledge, devices, and abilities to select a lower-cost strategy.

Depth and breadth require balance rather than a universal numeric rule. Larson and Czerwinski tested three hierarchy shapes over a large, expertly categorized information space. The moderate 16-by-32 hierarchy produced the fastest average search time and the lowest lostness. It significantly outperformed the deeper 8-by-8-by-8 hierarchy, while its advantages over the broader 32-by-16 hierarchy were not statistically reliable ([5]). The practical inference is not to copy those dimensions. It is to minimize unnecessary decisions without confronting users with an undifferentiated wall of options. Label quality, grouping coherence, scanning cost, and task context mediate the tradeoff.

Navigation must also communicate state. Users need to know where they are, what level they occupy, what choices are peers, what has been completed, and how to recover from a wrong turn. The author's synthesis is that orientation reduces the cost of testing a hypothesis about the structure. When a route fails, visible ancestry, descriptive headings, and stable navigation let the user revise the hypothesis without restarting ([1] [4]).

### Treat labels and summaries as predictive cues

Information scent explains why short pieces of text carry disproportionate architectural weight. A label is a compressed prediction of distal content. Its quality depends on the user's task and vocabulary, not only on its literal accuracy. A category named "Governance" may be exact for specialists yet weak for someone trying to report a conflict of interest. A task label such as "Declare a conflict" exposes the action and therefore narrows the expected destination ([4] [7] [14]).

Labels should be specific, distinct from neighboring choices, and consistent with destination headings. Summary text should add discriminating detail rather than repeat the title. Links such as "Learn more" or "Click here" discard context and become especially ambiguous when presented outside the surrounding paragraph. Nielsen Norman Group's information-scent guidance treats clear link labels and useful summaries as the main visible evidence by which users judge whether a destination is worth the cost ([14]).

Consistency is not the same as uniform wording. A shared vocabulary should preserve the same concept across navigation, search, headings, and metadata, but labels can include context where ambiguity would otherwise remain. The author's synthesis is that good labeling minimizes the translation users must perform between their goal, the system's terms, and the page's explanation. Translation cannot always be eliminated, particularly in legal or technical domains, but definitions and synonym mappings can make it explicit ([1] [10]).

### Structure pages for scanning, sequence, and assistive navigation

Page architecture continues the work of site architecture. A descriptive title confirms arrival. An opening summary states purpose and scope. Headings divide the information according to questions or decisions. Lists represent real sets or sequences, tables represent relationships that depend on rows and columns, and links state their destination or action. W3C explains that clear headings help users find information and understand relationships, and that correct markup lets screen-reader users navigate headings in generated lists or by jumping from heading to heading ([8] [10]).

Heading text and heading semantics are separate requirements. Visually prominent text can describe a section well but remain unavailable as a heading to assistive technology; a correctly marked-up heading can still fail if its wording is vague. WCAG's guidance explicitly distinguishes these cases ([10]). Content design must therefore coordinate language, hierarchy, and markup rather than treating accessibility as a final technical check.

Sequence should follow the user's decision path. Prerequisites should precede instructions that depend on them; exceptions should appear where they affect action; consequences should be visible before commitment; and next steps should follow completion. The author's synthesis is that progressive disclosure is useful only when the collapsed label has enough scent and the hidden detail is not needed to decide whether to proceed. Hiding complexity without preserving the decision structure merely transfers effort from reading to repeated opening, backtracking, and search ([4] [14]).

### Use metadata to connect browsing, search, and governance

Metadata describes content so that people and systems can retrieve, display, relate, and maintain it. Descriptive metadata includes title, summary, topic, audience, and keywords; structural metadata records type and relationships; administrative metadata records owner, status, dates, permissions, and retention rules. Search can use these fields for indexing, filtering, result presentation, ranking constraints, and synonym handling, while governance can use them to find unowned or stale content ([1]).

Search is not a repair for incoherent architecture. It depends on titles, vocabulary, metadata, content quality, and result summaries produced by the same system. Search logs can reveal unmatched queries, repeated reformulations, and vocabulary gaps, but the data require interpretation. A high-volume query may indicate demand, a hidden route, ambiguous terminology, or all three. The author's synthesis is that browsing and search should be treated as complementary observations of one semantic model: browsing makes selected relationships visible, while search provides direct access through language ([1] [9]).

Metadata should be limited to fields with a defined use and owner. A field that no interface, search rule, workflow, or audit consumes becomes inconsistent because contributors receive no feedback from it. Conversely, required fields should have validation rules, controlled values where appropriate, and a migration plan when the model changes. These controls turn classification from an editorial aspiration into repeatable infrastructure ([1] [2]).

### Govern the architecture as a living system

Governance assigns decision rights and maintenance duties. It specifies who can create a content type, approve a preferred term, change a navigation label, merge duplicates, archive material, or revise a relationship. It also defines review triggers, quality criteria, exception processes, and evidence to retain. GOV.UK's guidance that content be kept up to date and ISO's life-cycle framing both make maintenance part of design rather than an activity after design ([2] [11]).

A durable architecture records rationale as well as outcomes. A taxonomy entry should identify its definition, synonyms, scope note, owner, and change history. A content type should identify the user need it serves. A major navigation decision should identify the tests and constraints behind it. The author's assessment is that such records reduce institutional memory loss and make later changes falsifiable: a team can compare new evidence against an explicit prior assumption instead of debating an undocumented preference.

Governance should not freeze the system. Its purpose is controlled adaptation. Search behavior, support requests, content failures, accessibility audits, and user research should create review signals; changes should be tested against tasks and monitored after release. The cycle is continuous: model, publish, observe, diagnose, revise, and document. This is how information remains usable as the corpus and its users change ([2] [11] [13]).

## Evidence

### Information scent changes retrieval performance

Pirolli, Card, and Van Der Wege operationalized information scent as the proportion of participants who could infer a target's correct location from upper-level labels in a large tree. They first gathered normative judgments from 48 participants over 128 tasks, then used selected tasks in two browser experiments. Experiment 1 used eight participants, 56 test tasks spanning retrieval and comparison, eye tracking, counterbalanced browser conditions, and a retest one to three weeks later. Higher scent significantly reduced task time overall and especially for retrieval tasks; low scent increased visual-search cost in the dense hyperbolic display ([4]).

Their second experiment used eight participants, four experienced and four novice, and eight simple retrieval tasks split between high- and low-scent conditions. The hyperbolic browser averaged 26.98 seconds against 43.74 seconds for the conventional comparison browser, but both interfaces were much slower under low scent than high scent. Low-scent tasks also required many more fixations, and the hyperbolic interface's ability to expose more nodes became a disadvantage when cues did not direct attention ([4]). The experiments were small and used an artificial hierarchy, so their exact timings should not be generalized to contemporary sites. Their causal contribution is narrower and stronger: making more options visible does not guarantee faster retrieval; the semantic cues that distinguish promising paths materially affect performance.

### Hierarchy shape has a context-dependent optimum

Larson and Czerwinski tested 19 participants searching expertly categorized encyclopedia content through three web hierarchy structures. The study measured reaction time and lostness, collected subjective ratings, and assessed visual scanning and memory. Average search times were 36 seconds for the 16-by-32 structure, 46 seconds for 32-by-16, and 58 seconds for 8-by-8-by-8. The overall hierarchy effect was significant; post-hoc tests found 8-by-8-by-8 significantly slower than both two-level structures, but no significant reaction-time difference between 16-by-32 and 32-by-16. Lostness was lowest for 16-by-32, highest for 8-by-8-by-8, and intermediate for 32-by-16 ([5]).

This study directly challenges simplistic rules such as "shallower is always better" or "menus should never exceed a fixed number." Its evidence supports a balancing model: each added level creates another categorical decision and interaction, while each additional option on a page creates scanning and discrimination work. The researchers used a single well-organized information space and a small sample, which limits generalization. The defensible design implication is therefore to test representative tasks and labels rather than to treat the reported hierarchy dimensions as a universal recipe ([5]).

### Task-oriented structures outperform institution-oriented structures

Fang and Holsapple constructed experimental websites with subject-oriented, usage-oriented, and combined navigation hierarchies and tested both simple and comparatively complex knowledge-acquisition tasks. They ran two experimental rounds, one with participants trained in production and operations management and one with participants who had not received that domain training. The study measured task accuracy, speed, and perceived usability. Across rounds, usage-oriented and combined hierarchies produced significantly higher performance usability than the subject-oriented hierarchy for both task-complexity levels; domain knowledge also affected perceived usability ([7]).

The evidence is relevant because it isolates structure while keeping the information domain and task sets controlled. It supports organizing public-facing routes around what people are trying to accomplish, while retaining subject classifications where they aid expert browsing or support combined access. Its limitation is also instructive: a laboratory website and knowledge-acquisition task cannot represent every transactional, exploratory, or longitudinal information environment. The result should guide hypotheses, not replace local research ([7]).

### Card sorting yields repeatable patterns but not a finished architecture

Katsanos and colleagues examined the cross-study reliability of open card sorting through six studies with 140 technology-oriented participants. Three groups sorted 38 items for a travel site and three groups sorted 55 items for an online shop. The researchers compared item-distance matrices with Mantel tests, compared base clusters in hierarchical analyses, and compared navigation schemes derived with an elbow criterion. Correlations between distance matrices were significant, base-cluster similarity ranged from 90.9 to 96.5 percent, and derived navigation-scheme agreement ranged from 63.2 to 92.7 percent ([6]).

The study supports card sorting as a reproducible source of evidence among participants with similar profiles, but it also defines important limits. The authors did not analyze qualitative labels and comments in their reliability comparisons, their participants were technologically experienced, and the work did not test the usability of the resulting architectures. They state that final schemes must also account for information scent and visual constraints ([6]). The practical conclusion is not that a dendrogram is an architecture. It is that repeated groupings can identify stable candidate relationships that designers must label, reconcile with requirements, and evaluate through retrieval tasks.

### Standards encode structural requirements for comprehension and access

WCAG 2.2 supplies normative requirements for minimum properties of accessible content. Success Criterion 1.3.1 requires information, structure, and relationships conveyed through presentation to be programmatically determinable or available in text. Success Criterion 2.4.6 requires headings and labels to describe topic or purpose. Success Criterion 2.4.5 requires multiple ways to locate a page within a set, except where the page is a process step ([8] [9] [10] [15]). These criteria were developed through the W3C standards process and apply beyond any one research sample ([15]).

The supporting guidance explains the user consequences. Descriptive headings help people orient, predict section content, and navigate through heading lists; multiple routes accommodate people who find search, a table of contents, a sitemap, sequential movement, or hierarchical navigation easier to comprehend or operate ([9] [10]). Standards do not prove that a specific taxonomy is understandable, and conformance does not guarantee overall usability. They establish that semantic structure, descriptive labels, and alternative routes are accessibility requirements rather than optional refinements.

### Method triangulation diagnoses different failure layers

Card sorting, tree testing, and interface usability testing answer different questions. Card sorting generates evidence about grouping and terminology. Tree testing removes visual interface cues and asks participants to locate targets in a proposed hierarchy, thereby testing category placement and labels. Interface usability testing observes the combined effect of architecture, navigation components, layout, content, and interaction. Nielsen Norman Group explicitly distinguishes card sorting as generative from tree testing as evaluative and recommends testing a hierarchy that emerges from sorting ([13]).

The author's synthesis is that no single metric identifies an architectural cause. A failed task in a rendered interface may result from the hierarchy, a hidden menu, a weak label, a poor result summary, inaccessible markup, or content that does not answer the question. Separating tests by layer allows the team to isolate these possibilities, while analytics and search logs show their frequency in actual use. Evidence becomes actionable when each method is tied to the decision it can and cannot validate ([2] [12] [13]).

## Implications

### For writers and editors

Writers are architects whenever they choose a title, heading, link, sequence, category, or related item. The implication is that editing should begin before sentence-level revision. First state the user need and page purpose; then identify prerequisite decisions, relationships, and next actions; only then optimize prose. GOV.UK's guidance places user needs, amount, format, publication location, accessibility, and maintenance within content design rather than treating them as separate production stages ([3] [11]).

A practical editorial test is predictive: can a reader infer what each link, heading, and section will provide before investing effort? Titles should distinguish pages in search results and navigation. Headings should describe the topic or decision, not merely decorate a visual break. Summaries should add evidence about scope. Link text should state the destination or action. These practices strengthen information scent for all readers and make heading and link lists useful to assistive-technology users ([10] [14]).

Editors should also challenge page boundaries. If several pages answer fragments of one task, merging or sequencing may reduce search and reconciliation work. If one page serves unrelated tasks, splitting it may improve labels, metadata, and maintenance. If the same explanation is copied across pages, a reusable content model or authoritative source may prevent divergence. The author's synthesis is that content design quality should be judged at the task level, not by the polish of each isolated page ([1] [3]).

### For technical documentation and knowledge systems

Documentation teams should model entities and task relationships before selecting navigation. Concepts, procedures, references, tutorials, troubleshooting items, release notes, and policies serve different retrieval purposes. Giving these types explicit fields and links enables filtered search, generated indexes, version-aware relationships, and reliable next steps. The communication objective is semantic continuity: the reader should be able to move from a symptom to a diagnosis, from a requirement to a procedure, or from a changed feature to its migration guidance without reconstructing the system from unrelated pages ([1] [8]).

Multiple access routes are especially important in expert systems because novice and experienced users begin with different knowledge. A novice may browse by goal or symptom; an expert may search an exact term, identifier, or command; an auditor may navigate by policy and evidence. One maintained body of content can serve these routes through taxonomy, metadata, synonyms, and explicit relationships rather than duplicated manuals ([1] [9]).

Search behavior should feed governance. Unmatched queries can identify vocabulary gaps; frequent reformulation can indicate weak result scent; repeated exits from a result can indicate a mismatch between title and content; support tickets can reveal absent task paths. These signals do not diagnose themselves. The team should formulate a structural hypothesis, test it with users, change the model or content, and compare outcomes after release. This preserves the human-centered evaluation cycle required by ISO 9241-210 ([2]).

### For journalism and public information

News and public-information systems must support both immediate discovery and later context. Topic pages, timelines, explainers, entity records, and explicit links between an event and its background can prevent a stream of updates from becoming an archive that is chronological but incomprehensible. Metadata should distinguish reporting, analysis, opinion, correction, and reference material so labels and relationships do not blur their communicative roles. The author's synthesis is that architecture carries editorial meaning: how material is grouped and labeled affects what relationships readers perceive, even when every individual article is accurate.

Public services face a higher consequence of findability failure because information may determine eligibility, deadlines, rights, or required action. Routes should therefore reflect recognizable tasks, surface prerequisites and exceptions before commitment, and provide alternative navigation or search. Content owners should be explicit because stale guidance can remain highly findable. GOV.UK's user-need and maintenance principles, combined with WCAG's structure and navigation criteria, provide a minimum operational baseline ([3] [8] [9] [11]).

### For accessibility and inclusive design

Accessibility must be designed into the architecture rather than added after visual design. Programmatic headings, landmarks, lists, table relationships, and labels preserve the structure when presentation changes. Descriptive wording makes those structures intelligible. Multiple ways of locating content accommodate different navigation strategies and technologies ([8] [9] [10]). A visual menu can therefore appear orderly while the underlying information environment remains inaccessible if its relationships are encoded only through placement, color, or styling.

Inclusive research must also affect taxonomy. A grouping that works for staff, fluent readers, or experienced users may fail for people who use different terminology, approach through translation, navigate sequentially with assistive technology, or possess limited domain knowledge. Distinct user groups should be represented in research and analyzed separately when their mental models or tasks differ; Katsanos and colleagues limit their reliability finding to participants with similar profiles ([6]). The implication is not to seek a single average user but to test whether the structure supplies workable routes for the populations it claims to serve.

### For product and organizational governance

Product leaders should treat information architecture as shared infrastructure. Navigation, search, support, onboarding, policy, and in-product help all depend on the same names and relationships. If each team invents labels locally, users must relearn the system at every boundary. A governed vocabulary and content model can preserve coherence while allowing context-specific presentation ([1]).

Decision rights should match risk. Routine metadata corrections may be delegated, while changes to a top-level taxonomy, regulated instruction, or cross-channel term may require broader review. Every important type and term should have an owner, and every critical item should have a review trigger. Lifecycle data should support reports for missing owners, expired reviews, broken relationships, and deprecated vocabulary. This makes governance measurable rather than ceremonial ([2] [11]).

Architecture also constrains organizational behavior. If publishing a new page is easier than updating or retiring an existing one, duplication will accumulate. If teams are rewarded for launches rather than task completion, inventories will grow without evidence of value. The author's assessment is that the worst failure is not a visibly bad menu; it is a system that continuously produces plausible, unowned content faster than it can test, connect, and maintain it. Preventing that failure requires workflow controls as well as design skill.

### A practical design and evaluation loop

A disciplined project can use the following sequence. First, define priority users, tasks, evidence, and success criteria. Second, inventory the current corpus and identify owners, duplication, gaps, and risks. Third, model content types and named relationships. Fourth, develop candidate taxonomies, vocabularies, metadata, and routes. Fifth, use card sorting where grouping evidence is needed, then tree-test candidate hierarchies and labels. Sixth, prototype page and navigation behavior and run task-based usability and accessibility tests. Seventh, publish with analytics, search logging, ownership, review dates, and change records. Eighth, monitor real behavior and repeat the cycle ([2] [3] [6] [13]).

Evaluation measures should remain tied to tasks. Useful measures include successful destination selection, directness of the path, time on task, backtracking, first-click distribution, search reformulation, zero-result queries, comprehension of the answer, and successful next action. No measure is sufficient alone: a fast path to misunderstood content is not success, and a high-traffic page may be evidence of demand or of users repeatedly failing elsewhere. The author's synthesis is that the strongest acceptance criterion combines findability, comprehension, action, and accessibility for a defined user and context.

The loop should preserve reversibility. Taxonomies and labels can be prototyped and tree-tested before expensive implementation; redirects can preserve old routes during migration; metadata can support parallel views without duplicating content; and change logs can make governance decisions auditable. This approach follows human-centered design while preventing the most costly outcome: a large migration that makes the repository look orderly but removes the cues and routes users previously depended on ([2] [5] [13]).

Information architecture and content design ultimately convert a collection into a communicative system. Organization determines which distinctions are visible, labels express those distinctions, navigation and search expose routes through them, page structure preserves their meaning, and governance keeps them reliable. When these parts are aligned with real tasks and evaluated separately and together, information becomes easier not only to find, but to trust, understand, and use ([1] [2] [8]).

## Sources

1. Rosenfeld, L., Morville, P., & Arango, J. (2015). "Information
   Architecture: For the Web and Beyond," 4th edition. O'Reilly Media.
   https://books.google.com/books?id=vJWJCgAAQBAJ [high]

2. International Organization for Standardization. (2019). "ISO
   9241-210:2019 -- Ergonomics of human-system interaction -- Part 210:
   Human-centred design for interactive systems."
   https://committee.iso.org/cms/live/live/en/sites/isoorg/contents/data/standard/07/75/77520.html [high]

3. Government Digital Service. "Identify user needs."
   https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/identify-user-needs [high]

4. Pirolli, P., Card, S. K., & Van Der Wege, M. M. (2000). "The Effect
   of Information Scent on Searching Information Visualizations of Large
   Tree Structures." Proceedings of AVI 2000.
   https://courses.ischool.berkeley.edu/i247/f05/readings/Pirolli_InfoScentHyperbolic_AVI00.pdf [high]

5. Larson, K., & Czerwinski, M. (1998). "Web Page Design: Implications
   of Memory, Structure and Scent for Information Retrieval." Proceedings
   of CHI 1998, 25-32. doi:10.1145/274644.274649.
   https://www.microsoft.com/en-us/research/publication/web-page-design-implications-memory-structure-scent-information-retrieval/ [high]

6. Katsanos, C., Tselios, N., Avouris, N., Demetriadis, S., Stamelos,
   I., & Angelis, L. (2019). "Cross-study Reliability of the Open Card
   Sorting Method." CHI 2019 Extended Abstracts.
   https://arxiv.org/abs/1903.08644 [high]

7. Fang, X., & Holsapple, C. W. (2011). "Impacts of navigation
   structure, task complexity, and users' domain knowledge on Web site
   usability -- an empirical study." Information Systems Frontiers,
   13, 453-469. doi:10.1007/s10796-010-9227-3.
   https://link.springer.com/article/10.1007/s10796-010-9227-3 [high]

8. World Wide Web Consortium. "Understanding Success Criterion 1.3.1:
   Info and Relationships," WCAG 2.2.
   https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html [high]

9. World Wide Web Consortium. "Understanding Success Criterion 2.4.5:
   Multiple Ways," WCAG 2.2.
   https://www.w3.org/WAI/WCAG22/Understanding/multiple-ways.html [high]

10. World Wide Web Consortium. "Understanding Success Criterion 2.4.6:
    Headings and Labels," WCAG 2.2.
    https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html [high]

11. Government Digital Service. "Understand content design."
    https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/understand-content-design [high]

12. Nielsen Norman Group. "Information Architecture vs. Sitemaps."
    https://www.nngroup.com/articles/information-architecture-sitemaps/ [medium]

13. Nielsen Norman Group. "Tree Testing: Evaluate Menu Labels and
    Categories."
    https://www.nngroup.com/articles/tree-testing/ [medium]

14. Nielsen Norman Group. "Information Scent: How Users Decide Where
    to Go Next."
    https://www.nngroup.com/articles/information-scent/ [medium]

15. World Wide Web Consortium. (2024). "Web Content Accessibility
    Guidelines (WCAG) 2.2," W3C Recommendation.
    https://www.w3.org/TR/WCAG22/ [high]

## See Also

- `library/communication/writing-craft-and-style.md` -- sentence and
  paragraph choices that make structured content clear once it is found.
- `library/communication/semiotics-and-meaning-making.md` -- how labels,
  signs, and symbolic relationships acquire meaning for interpreters.

