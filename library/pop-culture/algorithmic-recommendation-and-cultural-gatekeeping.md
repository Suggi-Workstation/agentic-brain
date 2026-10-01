---
name: algorithmic-recommendation-and-cultural-gatekeeping
id: 20261001T003727Z
tier: library-topic
domain: pop-culture
author: Librarian
tags: [algorithmic-recommendation, cultural-gatekeeping, discoverability, platform-culture, popularity-bias, cultural-diversity, creator-economy, taste]
links: [library/pop-culture/music-as-cultural-phenomenon.md, library/pop-culture/transnational-popular-culture.md, library/pop-culture/internet-culture-memetics.md, library/communication/media-ecosystem-and-platform-dynamics.md]
---

# Recommendation Systems Co-Produce Cultural Visibility Rather Than Merely Predict Taste

Ranking, recommendation, search, autoplay, and personalized feeds decide which cultural artifacts become easy to encounter inside catalogs too large for anyone to inspect. These systems do not act alone: platform objectives, audience behavior, creator adaptation, human curation, advertising, moderation, rights, and inherited popularity form feedback loops that can widen discovery or repeatedly privilege what is already visible [1][5][11]. The central cultural claim is therefore relational: algorithms participate in gatekeeping by allocating exposure, but they neither create taste from nothing nor determine reception without users and institutions [7][9][13].

## Background

Cultural gatekeeping predates machine learning. Editors, critics, broadcasters, cinema programmers, record labels, retailers, festival selectors, and social networks have long reduced an abundant field of possible works to a manageable set. Recommendation systems continue this selection function while changing its speed, scale, personalization, and observability. Helberger, Karppinen, and D'Acunto define exposure diversity as the content audiences actually select rather than everything formally available, and they emphasize that commercial and strategic choices sit behind decisions about what is prioritized or excluded [1]. Bucher's study of Facebook's former EdgeRank system made the same issue visible in an early social-feed setting: software did not merely transmit posts but organized a scarce field of visibility in which interaction helped produce further visibility [2]. These sources concern different platforms and periods, but both establish that distribution architecture is part of cultural mediation.

Digital catalogs intensified the selection problem. A streaming service can make far more films, programs, songs, games, or creator videos technically available than can fit on one screen or inside one person's attention. Netflix engineers described their 2015 service not as one algorithm but as a collection of rankers, row selectors, search systems, and evidence-selection processes; they reported that recommendations then influenced about 80 percent of hours streamed and that experiments were evaluated partly through retention and medium-term engagement [3]. This is primary evidence about Netflix's design and business purpose at that time, not a universal measure for other services or the present platform. Its cultural importance lies in the location of choice: a catalog title can exist while receiving little practical exposure if it is placed low, represented weakly, or never offered in a relevant row [3][13].

Music streaming joined algorithmic ranking to older forms of playlisting, radio, retail display, and editorial promotion. Bonini and Gandini describe this as hybrid gatekeeping: automated analysis, interface design, human curation, aggregate popularity, autoplay, and platform management operate together rather than as separable algorithmic and human regimes [5]. Their comparative walkthrough of Spotify, Apple Music, and Tidal counted only the items reachable on small front pages without search in May 2020 and identified mechanisms such as choice narrowing, novelty boosting, flow prolonging, and context confirmation [5]. The finding does not show that every listener saw the same items or that one mechanism caused a particular taste. It shows that an interface structures the route from an effectively immense catalog to a finite set of convenient choices.

Social feeds extended recommendation beyond previously followed accounts. TikTok's For You feed made content-level recommendation a default mode of cultural encounter, while Instagram, YouTube, and other services incorporated related feed, short-video, and autoplay systems. Boeker and Urman used controlled sock-puppet accounts to isolate the effects of language, location, following, liking, and viewing behavior on TikTok recommendations; all tested factors affected the feed, with following strongest, followed by liking and video-view rate [6]. The result documents personalization pathways under the tested conditions. It does not show that one action permanently fixes a user's feed or that recommendation determines what the user believes.

The creator side changed at the same time. Cotter's thematic analysis of online discussions among aspiring and established Instagram influencers from September 2017 through January 2018 found that participants treated visibility as a game whose partly hidden rules had to be inferred through discussion, trial, analytics, and improvised tests [7]. Some emphasized authentic relationship-building; others used reciprocal engagement, follow-unfollow tactics, or other ways of making popularity legible to the system [7]. This evidence rejects a simple picture of creators passively obeying code. Creators interpret the platform, exchange folklore about it, change their work, and sometimes manufacture the signals that the system then treats as evidence.

Concerns about diversity emerged because recommendation can convert past attention into future exposure. Popular items generate interaction data, high interaction can increase predicted relevance, increased exposure generates more interaction, and the enlarged record can justify still more exposure [2][10][14]. Yet the opposite effect is also possible. A recommender can help a listener find an obscure artist, connect a viewer with a foreign series, or introduce a creator without an inherited audience. Helberger and colleagues therefore reject technological inevitability: recommender systems can be designed to support autonomy, deliberative breadth, or minority visibility, although those goals conflict and require different definitions and measurements of diversity [1].

Regulation and cultural policy have begun to treat discoverability as a public issue. UNESCO's 2022 global report, based predominantly on reports from 94 parties to the 2005 Convention, identified platform concentration, digital-access gaps, unsustainable creator remuneration, and business models that do not favor discovery of diverse content as risks in the digital cultural environment [11]. The European Union's Digital Services Act requires covered online platforms to disclose the main parameters of recommender systems and options for influencing them; it additionally requires very large online platforms and search engines to offer at least one recommender option not based on profiling, assess systemic risks involving algorithmic systems, and support specified forms of regulatory and vetted-researcher scrutiny [12]. These measures do not prescribe one culturally correct feed. They make ranking objectives, alternatives, risks, and evidence more contestable.

This topic remains within pop-culture analysis by asking how visibility changes the cultural field: which works become recognizable, which styles creators imitate, which communities encounter one another, and which artifacts acquire the status of a hit, niche, canon, or trend. Recommender engineering belongs primarily to technology; platform market power belongs primarily to industries-sectors; content-moderation doctrine belongs primarily to law-regulation; and individual persuasion effects belong partly to psychology-behavior. Those adjacent questions enter here only where they explain the production, circulation, interpretation, and diversity of popular culture [5][7][11][12].

## Core Concepts

### Gatekeeping Is the Allocation of Exposure

Availability and exposure are different states. Availability means that a work can in principle be accessed in a catalog or platform. Exposure means that it is placed where a person can plausibly encounter it. Consumption adds a further step: the exposed person chooses, continues, or returns. Cultural influence is a still stronger claim requiring evidence that the encounter affected memory, preference, practice, identity, or institutional action. Helberger and colleagues center this distinction by defining exposure diversity through what audiences actually select, while UNESCO distinguishes availability, accessibility, and discoverability in cultural policy [1][11]. A large catalog can therefore coexist with narrow attention, and a varied recommendation slate can coexist with repetitive consumption.

Algorithmic gatekeeping differs from a single editor's decision because it is continuous and individualized. A ranked page is assembled for a person, session, device, region, or inferred context; the person reacts; and the next page may change. Yet individualization should not be confused with unlimited uniqueness. Collaborative systems group people through shared behavior, content-based systems group artifacts through represented features, popularity systems reuse aggregate attention, and business rules reserve positions for current priorities [3][14]. The author's synthesis is that recommendation produces patterned personalization: people receive different slates, but those slates are built from common catalogs, models, metrics, and institutional decisions.

### A Recommender Is a Pipeline, Not an Autonomous Agent

A cultural recommendation normally results from several stages. Candidate generation retrieves a manageable pool from a much larger catalog. Prediction or scoring estimates relevance, watch probability, completion, satisfaction, revenue, novelty, or another target. Ranking orders candidates. Re-ranking can add diversity, freshness, safety, rights, language, or policy constraints. Interface design decides rows, labels, thumbnails, previews, autoplay, defaults, and how much effort search requires. Netflix's technical account explicitly describes multiple algorithms and separate evidence-selection processes, while current recommender research distinguishes collaborative, content-based, fairness, and diversity objectives [3][14].

The target matters because a proxy becomes a cultural incentive when it controls exposure. A system optimized for a click may favor immediate recognizability; one optimized for completion may favor short or easily consumed works; one optimized for retention may value a different sequence; one given an explicit diversity term may sacrifice some predicted relevance to broaden the slate [3][14]. No single proxy equals cultural value. The author's synthesis is that the objective function acts as an editorial constitution: it does not write every artifact, but it defines which observable responses count when the platform allocates future attention.

Interface and automation cannot be separated cleanly. Bonini and Gandini show that autoplay, playlist organization, front-page limits, and human curation combine with recommendation logic to create pathways through music [5]. A title in the first visible row, a track that begins automatically, and a clip that requires a deliberate search impose different friction even if all are technically available. The cultural unit of analysis is therefore the recommendation pathway: model, policy rule, visual presentation, default action, and the user's available exit.

### Taste Is Elicited and Shaped, Not Simply Read

Recommenders use past behavior as evidence of preference, but behavior occurs inside an already selected environment. A listener cannot click a track never shown; a viewer may finish a film because autoplay removed a stopping point; a person may inspect an outrageous clip without endorsing it. When those actions become training signals, the system treats behavior under one arrangement as evidence for the next arrangement [3][4]. The author's synthesis is that platforms do not merely discover taste. They elicit partial expressions of taste under specific conditions and then use those expressions to reorganize future choice.

This does not imply that users lack agency. Frey's user-centered study of Netflix places algorithmic suggestions among critics, trailers, word of mouth, memory, marketing, and other choice aids; he argues that viewers neither trust nor use recommendations as completely as deterministic accounts assume [13]. Guess and colleagues similarly show why exposure cannot be collapsed into opinion: replacing Facebook and Instagram's default ranked feeds with reverse-chronological feeds for three months changed time spent, activity, and the composition of exposure, but did not significantly change the measured political attitudes, knowledge, or polarization outcomes [9]. A recommendation changes an opportunity to encounter; its downstream meaning depends on selection, attention, interpretation, repetition, and competing influences.

### Feedback Loops Turn Popularity Into an Input and an Outcome

Popularity bias occurs when already popular items receive disproportionate recommendation exposure. Zhao and colleagues' survey explains the general loop: greater exposure generates attention and consumption, which can enlarge popularity and thereby strengthen the item's future recommendation position [14]. Kowald and coauthors reproduced popularity-bias analysis in music using 1,755,361 user-artist interactions from 3,000 Last.fm users and 352,805 artists. Across six tested algorithms, recommendation frequency increased with artist popularity; users least oriented toward mainstream artists received significantly worse recommendations from the personalized algorithms [10]. The study concerns an offline dataset and tested algorithms, not the live ranking of every music service, but it demonstrates a mechanism by which aggregate accuracy can conceal unequal service to niche taste.

Feedback loops can be positive for discovery as well as concentration. Once a previously obscure artifact receives exposure, new audience data can help the system find other receptive users. A local track can move across borders, a back-catalog film can become newly salient, and a small creator can reach people outside a follower graph. The author's assessment is that the relevant question is not whether a feedback loop exists but which starting conditions, exploration rules, and constraints determine who can enter it. A system with no exploration budget may reproduce inherited visibility; a system with random or diversity-aware exploration may generate opportunities but still distribute them unevenly [1][10][14].

Path dependence follows because early signals affect later opportunity. Two comparable works can diverge after one receives a prominent placement, external publicity, or an initial burst of engagement. Creators then observe the visible winner and reproduce its length, hook, thumbnail, genre label, sound, or release pattern. The system records the resulting supply response as new evidence about audience preference. The author's synthesis is a recursive cultural mechanism: selection affects production, production affects available candidates, and the next selection is made from a field already reshaped by the previous one [5][7].

### Cultural Gatekeeping Is Hybrid

Calling a system algorithmic can conceal human and institutional gates. Rights determine which works enter a catalog and in which territories. Metadata determines whether a work can be classified. Editors assemble playlists or featured collections. Advertisers and sponsors purchase visibility. Moderators remove, restrict, or label material. Marketing campaigns create off-platform attention that becomes an on-platform popularity signal. Users follow, search, skip, share, and abandon. Creators adapt to the metrics. Bonini and Gandini's hybrid-gatekeeping framework is useful because it treats these operations as one coupled process rather than asking whether a human or machine made the final choice [5].

The hybrid view also prevents algorithms from becoming autonomous villains. A model trained on an unequal cultural record can reproduce that record without an explicit instruction to discriminate. A diversity intervention can fail if rights, metadata, language support, or promotion exclude the relevant work before ranking begins. Conversely, a human-curated list can reproduce popularity or institutional bias. The author's assessment is that accountability should follow control: catalog owners answer for acquisition and metadata, platform teams for objectives and interface, moderators for policy and process, creators for deliberate manipulation, and researchers for the limits of their measurements [3][5][10][11].

### Visibility Disciplines Creators

Bucher described a threat of invisibility: participation is governed not only through surveillance or removal but through the possibility of disappearing from the default feed [2]. Cotter later found that influencers responded by learning perceived rules, comparing tactics, and treating engagement and follower growth as both evidence and generators of visibility [7]. These studies are historically bounded to earlier Facebook and Instagram systems, yet their conceptual contribution survives platform change. When exposure is uncertain, metrics are public, and ranking rules are incomplete, creators must decide how much labor to devote to an inferred evaluator.

This creates an algorithmic imaginary: shared beliefs about what the system rewards. Those beliefs may be accurate, obsolete, platform-promoted, or folklore. They still matter if creators change behavior in response. Cotter's participants performed informal A/B tests, debated authenticity, used engagement groups, and distinguished relational from simulated influence [7]. The author's synthesis is that opacity has cultural effects even before the true mechanism is known. Uncertainty can standardize production because imitating visible success feels safer than testing forms whose value the system may not register.

Strategic gaming is therefore endogenous to the system. If watch time, comments, saves, or completion affect exposure, some actors will design for those signals. This does not make every optimization deceptive: a clearer title or stronger opening can help an audience understand a work. The boundary is whether the tactic improves the cultural encounter or merely manufactures a proxy while degrading it. Spam, synthetic engagement, misleading thumbnails, repetitive trend imitation, and engagement bait are different methods, but each exploits a gap between the measured signal and the quality the signal was intended to represent [7][14].

### Filter Bubbles Are Hypotheses, Not a Universal Outcome

A filter bubble claim requires a baseline and a measured dimension. Compared with what would exposure be narrower: a chronological feed, direct search, broadcast schedule, editor's list, friends' choices, or random sampling? Which diversity matters: genre, ideology, language, nationality, gender, race, creator size, style, or source? Over what period, and at what stage: recommendations, clicks, completed consumption, or durable taste? Helberger and colleagues show that diversity serves different purposes under autonomy, deliberative, and adversarial models, so one diversity score cannot resolve every normative question [1].

Empirical findings are correspondingly mixed. Anderson and colleagues analyzed fine-grained Spotify data from more than 100 million users and a behavioral embedding of millions of songs. They found that algorithmically programmed listening was associated with lower musical diversity than user-directed listening, while greater diversity was strongly associated with conversion and retention; they also used a randomized recommendation experiment to test effectiveness across more and less diverse users [4]. The observational comparison does not by itself prove that recommendations caused the diversity difference because listeners select modes differently. It does establish a platform-scale association and a short-term versus long-term design tension.

Haroon and colleagues trained 100,000 YouTube sock puppets across five ideological categories and collected more than 15 million watched videos in training and testing. Recommendations were generally congenial; very-right sock puppets received 37 percent more very-right recommendations at the end of an autoplay trail than at its beginning. Average ideological extremity changed only slightly, while recommendations from listed problematic channels rose from 1.2 percent at depth one to 2.5 percent at depth ten and were encountered by 36.1 percent of sock puppets [8]. Because the puppets always followed recommendations, the audit estimates a system pathway under that behavior, not what ordinary viewers necessarily choose or believe.

Guess and colleagues provide the complementary downstream test. Their randomized three-month intervention replaced default ranked feeds with reverse chronology for consenting Facebook and Instagram users. The change reduced platform use and activity and altered exposure, including increasing political and untrustworthy content while changing other content categories, yet it produced no significant changes in the measured political attitudes or knowledge outcomes [9]. Together, these studies show why deterministic language fails: algorithms can measurably change exposure without producing one uniform trajectory or a detectable short-term change in belief.

### Cultural Diversity Has Several Dimensions

Individual diversity asks how varied one person's slate or consumption is. Aggregate diversity asks how many distinct works or creators receive exposure across the whole audience. Commonality asks whether members of a society still encounter shared works that support cultural conversation. Supplier fairness asks whether creators with different popularity, language, region, identity, or institutional backing receive comparable opportunity. Serendipity asks whether a recommendation is both relevant and unexpectedly useful. Zhao and colleagues review formal measures across fairness and diversity, while UNESCO frames discoverability and local-cultural availability as policy concerns [11][14]. Improving one dimension can reduce another: complete personalization may increase individual relevance while reducing common exposure, and equal exposure may reduce fit when catalog groups differ greatly in size or audience interest.

Cultural diversity is also not equivalent to random variety. A list of unrelated artifacts can be diverse by distance but unusable to a person. Repeating only global hits can create commonality while marginalizing local expression. Promoting minority work without context can produce brief exposure but little understanding. Helberger and colleagues therefore connect diversity design to purpose and user autonomy [1]. The author's synthesis is that a defensible system must state which diversity it seeks, why that dimension matters, how it is measured, which trade-off it accepts, and how users can contest the result.

### Transparency Requires More Than Publishing a Formula

A complete source-code release would not by itself explain a recommendation. Production systems depend on changing models, training data, experiments, business rules, inventories, and user histories. Useful transparency is layered. Users need a plain explanation of major factors and controls. Creators need stable rules and notice of consequential changes. Researchers need impression-level, ranking, catalog, and outcome data under privacy safeguards. Regulators need access to system logic, testing, risk assessments, and audit evidence. The DSA separates these functions through parameter disclosure, user options, systemic-risk duties, non-profiled alternatives for the largest services, and data access for specified authorities and vetted researchers [12].

Transparency also creates risks. Exact tactical details can support spam or manipulation; raw data can expose private behavior; and a simple explanation can falsely imply that a dynamic system follows one fixed recipe. The author's assessment is that the objective is contestability rather than total legibility. A person should be able to identify why a class of content is being suggested, choose a materially different mode, report a harmful pattern, and obtain a reasoned response. An independent researcher should be able to test exposure distributions and changes without accepting a platform's public narrative as evidence [7][12][14].

## Evidence

### Spotify Shows a Tension Between Immediate Relevance and Long-Term Breadth

Anderson and colleagues constructed a musical-diversity measure from a high-dimensional embedding trained on Spotify listening behavior and applied it to fine-grained interaction records for more than 100 million users over several years [4]. They separated user-directed listening, such as search and self-selection, from programmed listening in which subsequent tracks were chosen algorithmically. User-directed consumption was typically more diverse; users who became more diverse over time shifted toward user-directed listening; and higher consumption diversity was strongly associated with conversion and retention [4]. The paper also reports a randomized experiment showing that personalized recommendations were more effective for users with less diverse listening histories.

The method has unusual scale and uses behavior rather than stated preference, but interpretation must preserve its design. The comparison between programmed and user-directed streams is observational, so unmeasured user motives can explain part of the difference. The song embedding operationalizes musical distance through listening patterns rather than through every possible cultural dimension. The result supports a bounded claim: relevance-optimized recommendation and diverse consumption can pull in different directions, and the users most responsive to immediate recommendations may be the users whose prior consumption is already narrow [4]. It does not show that Spotify inevitably traps listeners or that broader listening is always better.

### Last.fm Tests Popularity Bias Across Users and Algorithms

Kowald and coauthors used a public Last.fm dataset containing 1,755,361 interactions among 3,000 users and 352,805 artists, divided users by their orientation toward mainstream artists, and compared six recommendation algorithms [10]. For all six algorithms, artist recommendation frequency increased with artist popularity. Except for random and nonnegative matrix-factorization approaches under the study's group-average-popularity measure, tested methods recommended artists that were too popular relative to users' profiles; the least mainstream-oriented group also received significantly worse accuracy from all four personalized algorithms evaluated for error [10].

This reproducibility study makes distributional inequality visible. An average accuracy score can improve while a minority taste group receives worse service, and long-tail artists can remain underexposed even when some listeners prefer them. The dataset does not reproduce the private production systems, catalogs, or interfaces of current streaming services. Its evidentiary role is mechanism testing: when historical interaction data are long-tailed and algorithms learn relevance from those interactions, popularity can be amplified and niche users can bear disproportionate error [10].

### Netflix Demonstrates That Presentation and Business Goals Belong to the System

Gomez-Uribe and Hunt's primary account describes Netflix's 2015 recommender as multiple algorithms assembled across the homepage, search, rows, rankings, and evidence-selection mechanisms [3]. They reported that the system influenced about 80 percent of streamed hours, while search accounted for the remainder through its own algorithms. Netflix evaluated changes with offline historical data and A/B tests, with improved member retention and medium-term engagement as central targets [3]. The authors also explained that intuition about a better algorithm often failed when tested, which made controlled experiments the operational decision rule.

The paper documents a production system from one company at one historical moment, and its authors wrote from inside Netflix. It therefore establishes design, objectives, and reported scale more directly than it establishes cultural consequences. The cultural inference is nevertheless important: ranking and evidence selection jointly shape not only which film or series appears but which artwork, explanation, or row makes it appear relevant [3]. Frey's later user-centered work limits the inference by showing that viewers combine platform suggestions with word of mouth, criticism, memory, marketing, and other filters and do not uniformly trust recommendation aids [13]. The case supports co-production of choice, not algorithmic sovereignty.

### TikTok Audits Isolate Personalization Signals

Boeker and Urman created paired sock-puppet users that were identical except for one tested factor, then compared the metadata of posts appearing in their For You feeds [6]. They tested language and location, following, liking, and the rate at which videos were watched. All tested factors changed recommendations; following had the strongest measured influence, followed by liking and video-view rate [6]. The paired-control design improves causal attribution for the platform conditions observed because variation beyond expected noise can be linked to the manipulated factor.

The audit does not measure a human user's interpretation, long-term cultural development, or every undisclosed signal. Automated accounts cannot reproduce all social histories and motivations, and a platform can change after observation. Its contribution is narrower and foundational: user actions and contextual attributes measurably alter the cultural stream, so a For You feed is neither a universal popularity chart nor a fixed reflection of explicit preferences [6]. It is an adaptive encounter in which small acts help select subsequent material.

### Creator Research Shows How Ranking Changes Cultural Production

Cotter conducted a thematic analysis of influencer discussions collected from closed Facebook groups and linked online materials between September 2017 and January 2018 [7]. Participants described learning Instagram's rules through shared advice, trial, analytics, and improvised A/B tests. They agreed that engagement and followers affected visibility but split between relational tactics centered on authentic interaction and simulated tactics such as reciprocal engagement groups and follow-unfollow strategies [7]. The study does not verify every participant theory about Instagram. It measures how those theories organized labor and strategy.

That distinction is the evidence. Creators do not need complete knowledge of a ranking system for the system to affect culture; they need only believe that some forms are rewarded and act on that belief. Cotter found that culture shaped the response as much as code: existing ideals of authenticity and entrepreneurship supplied different ways to interpret the same perceived rules [7]. The evidence therefore contradicts both technological determinism and a neutral-tool account. Ranking structured the field of possible success, while creator communities translated uncertain signals into conventions and tactics.

### YouTube and Meta Separate Exposure From Downstream Effects

Haroon and colleagues' YouTube audit used 100,000 trained sock puppets, five ideology categories, homepage recommendations, and autoplay trails, collecting 15,323,930 watched videos across training and testing [8]. The system produced substantial ideological congeniality, especially for very-right accounts, but moderate and cross-cutting content remained present. Ideological extremity rose only slightly for the most partisan accounts. Listed problematic-channel recommendations were a small share, peaking at 2.5 percent at trail depth ten, yet at least one such recommendation appeared for 36.1 percent of sock puppets [8]. These results support concern about pathways without supporting the simple claim that every autoplay trail becomes steadily radical.

Guess and colleagues randomized consenting Facebook and Instagram users during the 2020 United States election to reverse-chronological rather than default ranked feeds for three months [9]. The intervention reduced time and activity and changed the content mix: political and untrustworthy exposure increased, some uncivil exposure decreased on Facebook, and exposure to moderate friends and ideologically mixed sources changed. Despite these substantial on-platform differences, the study found no significant change in issue polarization, affective polarization, political knowledge, or other measured attitudes over the study period [9]. The result does not prove that long-term or different recommendation systems have no effects. It shows that a major exposure intervention can alter behavior and content without producing the expected downstream attitude change within the measured interval.

Read together, the audits establish an evidence ladder. Recommendation can be shown to change what is offered. Click or watch data can show what is selected. Experiments can test whether a changed feed alters later attitudes or behavior. Each step requires separate evidence, and a finding at one level cannot substitute for another [8][9]. Cultural analysis is strongest when it preserves that ladder instead of treating visibility, consumption, and conversion as synonyms.

### Policy Evidence Treats Discoverability as a Cultural System

UNESCO's 2022 report used quadrennial reports from 94 parties, other datasets, literature, and expert contributions to monitor the 2005 Convention on the Diversity of Cultural Expressions [11]. It found that digitalization widened access and cultural exchange while platform concentration, unequal connectivity and skills, unsustainable remuneration, and business models unfavorable to diverse discoverability risked reproducing inequality. The report noted that 68 percent of reporting parties used quotas involving local content, languages, or social groups, while warning that quotas cannot compensate for insufficient local production or guarantee discovery [11]. This is comparative policy evidence rather than a causal platform audit.

The DSA supplies a legal response centered on transparency, alternatives, risk assessment, auditing, and data access [12]. Article 27 requires providers using recommender systems to explain the main parameters and user options in plain language. Article 34 requires very large services to assess systemic risks arising from design and functioning, including recommender systems. Article 38 requires at least one non-profiled option for each recommender system used by very large platforms or search engines, and Article 40 creates routes for regulatory and vetted-researcher data access under specified conditions [12]. These provisions do not measure whether cultural diversity improved. They create procedural conditions under which claims about ranking can be investigated rather than left entirely to platform self-description.

### The Convergent Finding Is Conditional Gatekeeping

Across technical papers, audits, creator research, audience research, and policy records, the common finding is not that algorithms homogenize culture in every setting. Recommendation systems change exposure, and the direction depends on catalogs, objectives, data, interface, user behavior, and institutional constraints [3][4][6][8][9]. Popularity can be amplified and niche users underserved [10][14]. Diversity can also be designed into ranking and can support user satisfaction or cultural-policy goals, although definitions and trade-offs must be explicit [1][11]. Creators alter production in response to perceived rules, while audiences retain other sources of choice and may not undergo the downstream change inferred from exposure alone [7][9][13].

The author's synthesis is that cultural gatekeeping has become recursive and partially personalized. Earlier gates selected a common schedule, shelf, or edition; contemporary gates repeatedly update a probabilistic slate using reactions to prior slates. This makes cultural power less visible but not wholly centralized. Platforms control objectives and infrastructure, creators influence signals and supply, audiences choose and interpret, institutions regulate, and external publicity changes the data entering the loop. Any adequate explanation must include all five.

## Implications

### For Audiences: Treat the Feed as a Situated Suggestion

A recommended item is evidence that a system expects a response under its current objective, not evidence that the item is culturally important, true, representative, or even the user's settled preference [3][14]. Audiences can reconstruct the gate by asking which action preceded the suggestion, whether popularity or similarity is visible, which catalog and territory constrain the choice, and what alternative route would produce a different result. Search, direct subscription, editorial lists, libraries, critics, friends, local cultural institutions, and non-profiled or chronological modes provide different gates rather than gate-free access [1][9][13].

The practical objective is controlled variation, not rejection of personalization. A listener can alternate recommendation with deliberate search, inspect artist or label contexts, and create sessions that begin outside the familiar genre. A viewer can compare the personalized homepage with catalog categories, external criticism, or a non-profiled ranking option. A creator-video user can reset a mistaken signal by intentionally selecting contrary material where the platform permits. These are the author's recommendations derived from evidence that user actions affect feeds and that audience choice remains part of exposure [6][9][13]. They are not guaranteed methods for defeating every ranking system.

Media literacy should separate four claims. The system showed the item; the user selected it; the user liked or completed it; and the encounter changed taste or conduct. Platform interfaces often compress these stages into engagement, but research does not support that compression. Haroon and colleagues measured offered pathways, while Guess and colleagues directly tested downstream attitudes and found substantial exposure change without corresponding significant attitude change in the measured period [8][9]. A disciplined audience should resist both fatalism and innocence: feeds matter because they structure opportunity, but seeing is not obeying.

### For Creators: Optimize a Portfolio, Not a Single Proxy

Creators face a real visibility problem. Bucher and Cotter show that ranking can make exposure feel conditional on continual participation, and creator communities respond by inferring rules and imitating visible success [2][7]. The worst-case strategy is total dependence on one opaque metric: a format change, ranking update, moderation decision, or platform shift can then erase reach and push the creator toward increasingly narrow imitation. A reversible strategy maintains a stable creative claim while diversifying distribution, audience contact, formats, and revenue paths.

Creators should distinguish useful adaptation from proxy manufacture. Clear metadata, accessible captions, intelligible openings, appropriate genre labels, and responsive audience relationships can improve discovery and the work itself. Synthetic engagement, misleading packaging, indiscriminate trend copying, or content stretched solely to satisfy an assumed duration signal can raise a metric while weakening trust or cultural distinctiveness. Cotter's evidence shows that creators already debate this boundary through authenticity and entrepreneurship [7]. The author's proposed test is simple: would the tactic still improve the audience's encounter if it produced no ranking advantage? If not, it is probably optimization of the gate rather than of the work.

Creators also need an evidence ledger. Record the date, content type, audience source, impression count, completion, saves, direct responses, and off-platform outcomes before attributing success or failure to the algorithm. Compare several releases rather than one anecdote, and preserve changes in platform guidance. Because systems and audiences change together, informal tests cannot identify every cause, but they can prevent folklore from becoming production doctrine. The principle follows from the paired controls in the TikTok audit and the explicit experimental approach described by Netflix: comparison is stronger than intuition, and a metric should be interpreted in relation to the objective that generated it [3][6].

### For Platforms: Make Cultural Objectives Explicit and Measurable

Platforms cannot optimize an undefined concept of diversity. They should specify whether the goal is individual variety, aggregate catalog coverage, local-language discoverability, exposure for less-popular creators, shared cultural commonality, or representation across identified groups [1][11][14]. Each goal requires a baseline, a metric, and an explanation of trade-offs with relevance, satisfaction, safety, and rights. Reporting only catalog size or the number of countries represented does not show what users actually encountered.

A multi-objective design can reserve controlled exposure for novelty, long-tail works, local content, and new creators while preserving relevance. The Spotify and Last.fm studies suggest why both user history and provider exposure require monitoring: recommendation-driven listening can be narrower than user-directed listening, and users with niche preferences can receive worse recommendations [4][10]. Possible tests include exposure share by popularity decile, creator reach conditional on catalog availability, language and territory coverage, repeat concentration, exploration acceptance, and long-term retention. Zhao and colleagues' survey shows that fairness and diversity can be included through training constraints or re-ranking rather than treated as after-the-fact commentary [14].

Cold-start policy deserves explicit treatment. New artifacts lack interaction records, so a system that treats existing engagement as quality can prevent them from obtaining the evidence needed to compete. Exploration can provide a bounded trial audience selected by content, context, or randomization; subsequent ranking can then use response without assuming that zero history means zero value. The author labels this as a design implication from popularity-bias evidence, not a finding that one exploration rate is correct [10][14]. Platforms should publish the goal and evaluation method because exploration also imposes attention costs on users.

User controls must be materially different. A hidden toggle that changes one weak parameter does not provide meaningful agency. Helberger and colleagues connect autonomy to awareness and the ability to adjust recommendations, while the DSA requires plain-language main parameters and, for the largest covered services, a non-profiled alternative [1][12]. Useful controls could include chronological, local, followed-only, editorial, diverse-discovery, and reduced-personalization modes where appropriate. Platforms should explain what changes, preserve an easy return path, and avoid designing the alternative as an inferior punishment for declining profiling.

Transparency should extend to creators without publishing an exploitation manual. Stable rules can identify prohibited manipulation, major ranking objectives, reason codes for loss of eligibility, and notice of consequential policy changes. Aggregate dashboards can show whether exposure is concentrating by creator size, language, geography, or content category. Qualified researchers need access to impressions and ranking conditions, not only public posts, because the absence of exposure is otherwise difficult to observe [12]. The single worst governance outcome is a system that privately changes cultural distribution while allowing neither users, creators, researchers, nor regulators to identify the change.

### For Cultural Institutions: Curate the Conditions of Discovery

Libraries, broadcasters, museums, archives, festivals, schools, public-service media, and independent critics remain important because recommendation need not be monopolized by commercial engagement objectives. Helberger and colleagues argue that public-service institutions may be especially positioned to realize forms of exposure diversity the market will not supply [1]. UNESCO similarly calls for investment in local production, diverse content, discoverability, monitoring, and fair creator remuneration rather than reliance on catalog access alone [11].

These institutions can build contextual gates. A playlist can explain historical lineage, a film collection can connect versions and regions, a game archive can preserve hardware and community context, and a local-culture feed can disclose why an artifact was selected. Context changes exposure from a bare impression into an invitation to understand. The author's synthesis is that public-interest curation should compete on legibility and trust rather than imitate an opaque commercial feed. Its value lies not in being non-algorithmic but in making objectives, selection criteria, and cultural responsibilities visible [1][11].

Funding policy should distinguish supply from discovery. A grant may produce a local work that remains invisible in a dominant interface. A quota may secure catalog presence without placement, language support, or sustained availability. UNESCO's evidence that platforms, local production, remuneration, and discoverability interact means policy evaluation should trace the full chain: creation, rights, metadata, catalog entry, recommendation exposure, audience selection, and creator compensation [11]. A failure at any gate can make nominal diversity culturally ineffective.

### For Regulators: Govern Processes Without Choosing Taste

The regulatory objective should not be a state-approved recommendation list. That would replace private opacity with political gatekeeping and threaten expression and autonomy. A narrower, reversible approach requires platforms to disclose major parameters, provide meaningful alternatives, assess foreseeable risks, preserve records, support audits, and enable qualified independent research [1][12]. These duties make systems contestable while leaving plural creators and audiences free to disagree about cultural value.

Risk assessment should include cultural and linguistic specificity. A globally acceptable aggregate can conceal the disappearance of a minority language, a local genre, or a small creator class. DSA Article 34 requires very large services to consider regional and linguistic aspects when assessing systemic risks, and UNESCO treats local-content discoverability as part of cultural diversity [11][12]. Regulators can therefore ask for exposure distributions and change analyses without assuming that equal outcome across every group is feasible or desirable.

Policy also needs a counterfactual. Before requiring chronology, randomization, or another ranking mode, regulators should ask what that mode changes. Guess and colleagues found that reverse chronology decreased use but increased some political and untrustworthy exposure while changing other categories, with no significant change in measured political attitudes [9]. The result does not settle every platform question; it demonstrates that an intuitive alternative can carry its own trade-offs. Rules should require testing and reporting rather than declare one ordering neutral.

### For Researchers: Measure the Whole Cultural Pathway

Research should begin with a declared dependent variable. Exposure studies need impression and rank data. Consumption studies need selection, duration, completion, and repeat behavior. Creator studies need production routines and resource constraints. Taste studies need longitudinal measures and external choice sources. Cultural-diversity studies need explicit dimensions such as genre, language, nationality, creator size, or identity. Attitude studies need experiments or credible causal designs. The Spotify, TikTok, YouTube, Meta, and creator studies each answer different questions because their methods observe different stages [4][6][7][8][9].

Audits should use more than one baseline. Chronology, popularity, random ordering, followed-only feeds, and personalized ranking each embody selection rules. Testing several can reveal whether a result comes from personalization, popularity, inventory, user history, or the interface. Researchers should report platform version, territory, date, account condition, language, logged-in status, seed behavior, and stopping rule because recommendation systems change continuously [6][8]. Negative and mixed findings deserve preservation; without them, the research literature can reproduce the salience bias it studies.

Cross-platform comparison must preserve media differences. Completion means something different for a song, two-hour film, serial episode, short video, game session, or text post. Autoplay carries different costs, and creator supply responds on different time scales. Bonini and Gandini's hybrid-gatekeeping analysis and Frey's historical account of film recommendation show that an apparently common recommender function inherits older media institutions and genre practices [5][13]. The author's synthesis is that a valid comparison holds the cultural question stable while allowing the mechanisms to differ.

### A Practical Cultural Gatekeeping Audit

The following protocol is the author's synthesis of the evidence, not a validated universal standard. First, define the cultural field and the relevant population. Second, map the catalog gate: rights, territory, language, metadata, moderation, and eligibility. Third, identify candidate generation, ranking objectives, re-ranking constraints, and interface defaults at the level the evidence permits. Fourth, separate availability, exposure, selection, completion, repeat use, and downstream effect. Fifth, measure individual variety, aggregate coverage, popularity concentration, supplier exposure, and shared commonality rather than reporting one diversity number [1][10][14].

Sixth, document human curation, advertising, editorial promotion, external publicity, and user-network supply so that the algorithm is not treated as an autonomous cause [5]. Seventh, study creator response: format changes, release timing, metadata, engagement tactics, and withdrawal. Eighth, compare at least two counterfactual orderings and preserve null results. Ninth, test for differences by language, region, creator size, and niche orientation. Tenth, disclose uncertainty, platform changes, inaccessible data, and the strongest claim each method can support [4][6][8][9].

The author's synthesis is that the audit's worst-case failure is to label an opaque popularity loop as revealed audience taste. Preventing it requires inversion: ask what cannot become popular because it is not exposed, what cannot be recommended because it never entered the catalog, and what creators stop making because the platform cannot measure its value. Recommendation is culturally legitimate when it helps people navigate abundance while preserving meaningful choice, plural discovery, and contestable rules. It becomes extractive when the platform's preferred proxy quietly defines which culture is visible and then cites the resulting behavior as proof that the public chose it [1][10][11][14].

## Sources

1. Helberger, N., Karppinen, K., and D'Acunto, L. (2018). "Exposure
   Diversity as a Design Principle for Recommender Systems."
   Information, Communication & Society, 21(2), 191-207.
   https://doi.org/10.1080/1369118X.2016.1271900 [high]

2. Bucher, T. (2012). "Want to Be on the Top? Algorithmic Power and the
   Threat of Invisibility on Facebook." New Media & Society, 14(7),
   1164-1180. https://doi.org/10.1177/1461444812440159 [high]

3. Gomez-Uribe, C. A., and Hunt, N. (2015). "The Netflix Recommender
   System: Algorithms, Business Value, and Innovation." ACM Transactions
   on Management Information Systems, 6(4), Article 13.
   https://doi.org/10.1145/2843948 [high]

4. Anderson, A., Maystre, L., Anderson, I., Mehrotra, R., and Lalmas, M.
   (2020). "Algorithmic Effects on the Diversity of Consumption on
   Spotify." Proceedings of The Web Conference 2020, 2155-2165.
   https://doi.org/10.1145/3366423.3380281 [high]

5. Bonini, T., and Gandini, A. (2022). "The Streaming Paradox: Untangling
   the Hybrid Gatekeeping Mechanisms of Music Streaming." Popular Music
   and Society, 45(3), 300-316.
   https://doi.org/10.1080/03007766.2022.2026923 [high]

6. Boeker, M., and Urman, A. (2022). "An Empirical Investigation of
   Personalization Factors on TikTok." Proceedings of the ACM Web
   Conference 2022, 2298-2309.
   https://doi.org/10.1145/3485447.3512102 [high]

7. Cotter, K. (2019). "Playing the Visibility Game: How Digital
   Influencers and Algorithms Negotiate Influence on Instagram." New
   Media & Society, 21(4), 895-913.
   https://doi.org/10.1177/1461444818815684 [high]

8. Haroon, M., Wojcieszak, M., Chhabra, A., Liu, X., Mohapatra, P., and
   Shafiq, Z. (2023). "Auditing YouTube's Recommendation System for
   Ideologically Congenial, Extreme, and Problematic Recommendations."
   Proceedings of the National Academy of Sciences, 120(50), e2213020120.
   https://doi.org/10.1073/pnas.2213020120 [high]

9. Guess, A. M., Malhotra, N., Pan, J., Barbera, P., Allcott, H., et al.
   (2023). "How Do Social Media Feed Algorithms Affect Attitudes and
   Behavior in an Election Campaign?" Science, 381(6656), 398-404.
   https://doi.org/10.1126/science.abp9364 [high]

10. Kowald, D., Schedl, M., and Lex, E. (2020). "The Unfairness of
    Popularity Bias in Music Recommendation: A Reproducibility Study."
    Advances in Information Retrieval, 35-42.
    https://doi.org/10.1007/978-3-030-45442-5_5 [high]

11. UNESCO. (2022). "Re|Shaping Policies for Creativity: Addressing
    Culture as a Global Public Good." Global report executive summary.
    https://www.unesco.de/assets/dokumente/Deutsche_UNESCO-Kommission/02_Publikationen/Publikation_UNESCO_Global_Report_Summary_2022_ReShaping_policies_for_creativity.pdf [high]

12. European Parliament and Council. (2022). "Regulation (EU) 2022/2065
    on a Single Market for Digital Services (Digital Services Act),"
    especially Articles 27, 34, 38, and 40.
    https://eur-lex.europa.eu/eli/reg/2022/2065/oj/eng [high]

13. Frey, M. (2021). "Netflix Recommends: Algorithms, Film Choice, and
    the History of Taste." University of California Press.
    https://www.ucpress.edu/books/netflix-recommends/paper [high]

14. Zhao, Y., Wang, Y., Liu, Y., Cheng, X., Aggarwal, C. C., and Derr, T.
    (2025). "Fairness and Diversity in Recommender Systems: A Survey."
    ACM Transactions on Intelligent Systems and Technology, 16(1),
    Article 2. https://doi.org/10.1145/3664928 [high]

## See Also

- `library/pop-culture/music-as-cultural-phenomenon.md` -- streaming,
  playlists, and collective meaning in music culture.
- `library/pop-culture/transnational-popular-culture.md` -- unequal gates,
  localization, and discoverability as cultural works cross borders.
- `library/pop-culture/internet-culture-memetics.md` -- participatory
  mutation and platform selection in networked culture.
- `library/communication/media-ecosystem-and-platform-dynamics.md` -- the
  adjacent communication-level account of ranking, moderation, and platform
  governance.