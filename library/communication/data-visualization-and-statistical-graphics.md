---
name: data-visualization-and-statistical-graphics
id: 20260930T020755Z
tier: library-topic
domain: communication
author: Librarian
tags: [data-visualization, statistical-graphics, visual-encoding, graphical-perception, uncertainty, accessibility, data-provenance]
links: [library/communication/public-speaking-and-presentation-design.md, library/communication/source-verification-and-fact-checking.md, library/communication/information-architecture-and-content-design.md, library/probabilistic-thinking-forecasting/communicating-forecast-uncertainty.md, library/mathematics-statistics/regression-analysis.md, library/notable-people/florence-nightingale-data-institutions-modern-nursing.md]
reviewed: 2026-09-30
---

# Data Visualizations Communicate Evidence Only When Encoding, Context, and Access Remain Verifiable

Data visualization turns values and relationships into spatial, visual, and interactive forms so an audience can compare evidence, detect structure, and make a decision. A chart is not truthful merely because its plotted numbers are correct: its encodings, scales, transformations, labels, uncertainty, narrative emphasis, accessibility, and provenance must preserve the meaning and limits of the underlying evidence [2][3][5][6].

## Background

Quantitative graphics developed from the convergence of mapping, measurement, statistics, printing, and administrative data collection rather than from one isolated invention. Michael Friendly's historical synthesis traces early quantitative displays through thematic cartography and scientific recording, then identifies William Playfair's 1786 line and bar charts and his 1801 pie and circle charts as major steps toward the familiar grammar of statistical graphics [1]. Nineteenth-century practitioners extended that grammar to public health, transportation, demography, and state administration. Charles Joseph Minard combined position, direction, width, area, and annotation in flow maps; Florence Nightingale used statistical diagrams as part of an evidentiary campaign about military mortality and institutional responsibility [1][18]. These examples established a durable purpose: a graphic can compress a large record into a perceptible argument for readers who would not inspect every row [1][18].

That compression creates both power and risk. Every display selects variables, transforms values, maps them to visual properties, chooses a comparison frame, and omits material that is not shown. The viewer then decodes the result through perception, learned conventions, domain knowledge, and the surrounding text. Cleveland and McGill called this decoding process graphical perception and argued that graph design required an empirical foundation rather than taste alone [2]. Their work shifted the design question from "Which chart looks attractive?" to "Which perceptual judgment must a viewer perform, and how accurately can people perform it?" Position, length, angle, area, color, shape, and motion are therefore not interchangeable decorations. They are channels with different capabilities, error profiles, and dependencies on context [2][3].

The computer changed both the scale and the form of visualization. Static printed charts remained important, but digital systems added rapid filtering, zooming, linking, animation, and details on demand. Shneiderman organized interactive information seeking around seven tasks - overview, zoom, filter, details on demand, relate, history, and extract - and summarized the design sequence as "overview first, zoom and filter, then details on demand" [10]. Interaction can reveal subsets and alternative views that a fixed image cannot contain. The author's synthesis is that it can also conceal state: a filter, hover action, default range, aggregation, or prior selection may determine what the user sees without surviving in a screenshot or citation. The communicative artifact is then not one chart but a data state, interface, transformation history, and rendered view [10][12].

Research also weakened the idea that one graphic form is universally superior. Schonlau and Peters found that comprehension depended on the task: graphs supported estimates of differences, whereas tables better supported judgments of equality and sums; gratuitous three-dimensional treatment reduced comprehension for pie charts [4]. A table is therefore not a failed visualization, nor is a chart automatically an improvement. Tables preserve exact values and permit lookup; charts externalize patterns and comparisons; maps add geographic context but weight areas visually; dashboards coordinate several views and controls. The appropriate form follows the audience's question, the required precision, and the consequences of misreading [3][4][17].

A second shift made uncertainty part of the message rather than an afterthought. Error bars, shaded intervals, fan charts, ensembles, hypothetical outcome plots, and scenarios encode different uncertainty objects. They are not interchangeable. A confidence interval around a parameter, a prediction interval for an outcome, an ensemble spread, and a scenario range answer different questions. The Office for National Statistics advises showing uncertainty when it changes interpretation and retaining complete uncertainty data in downloadable form, while research on hypothetical outcome plots shows that alternative representations can materially change multivariable probability judgments [7][13]. The author's synthesis is that uncertainty must be matched to the claim and task; adding a generic band does not make a chart honest.

Accessibility widened the definition of successful communication. WCAG requires text alternatives for non-text content and states that information must not depend on color alone [8][9]. A chart that works only for a sighted reader with typical color vision is not a complete communication artifact. Short alternative text can identify the figure; a longer description can explain its structure, principal pattern, and implications; and a data table can expose the values in a form available to assistive technology [8]. Labels, patterns, shape, and position provide redundancy when color or spatial scanning is unavailable, while keyboard operation and programmatically exposed names, roles, states, and values make interactive controls usable through assistive technology [9][20].

The modern field therefore joins statistical graphics, visual perception, communication design, human-computer interaction, accessibility, and reproducible computation. It does not replace statistical analysis. A graphic cannot repair biased sampling, invalid measurement, confounding, or an inappropriate model. Its narrower and essential responsibility is to transmit what the analysis does and does not establish without introducing a second layer of error. The author's synthesis is that a visualization is best treated as an evidence interface: it should make the intended comparison easy, the underlying choices inspectable, and the result usable through more than one sensory or technical route [3][8][12].

## Core Concepts

### Start with the audience, question, and decision

A visualization should be specified backward from the inference or action it must support. The designer needs to know who will use it, what those readers already understand, which comparison they must make, how precisely they must make it, and what error would matter. A manager monitoring an operational threshold, a scientist checking residual structure, a journalist explaining a trend, and a citizen locating a value do not have the same task even when they use the same dataset. Franconeri and colleagues' review emphasizes tailoring visualizations to the audience and directing attention toward the comparisons relevant to the intended conclusion [3].

The author's synthesis is a compact design contract: state the audience, question, evidence state, comparison, required precision, decision, and foreseeable misreading before selecting a chart. If the task is exact lookup, a well-structured table may be superior. If the task is comparing magnitudes on one scale, aligned position may be appropriate. If the task is seeing association, a scatterplot may be appropriate. If the task is locating a spatial pattern, a map may be justified. If the same chart is asked to serve lookup, exploration, explanation, and monitoring simultaneously, conflicting demands should be separated into coordinated views rather than hidden inside one crowded display [3][4][10].

### Encode variables with perceptually appropriate channels

A statistical graphic maps data fields to marks and visual channels. Marks include points, lines, areas, and regions. Channels include horizontal and vertical position, length, angle, area, color hue, color lightness, shape, orientation, texture, and motion. Cleveland and McGill's experiments found two kinds of position judgment to be most accurate, length second, angle and slope third, and area last among the tested quantitative judgments [2]. The ranking is not a universal law for every task, display, or population, but it establishes a defensible default: encode the comparison most important to the reader with a channel that supports accurate comparison [2][3].

Channel choice must also respect data type. Nominal categories require distinction without implying order, so hue, shape, or separate position can work. Ordered categories require a perceptible sequence, so lightness, position, or ordered size is more appropriate. Quantities require proportional mappings whose mathematical relationship matches their appearance. Because circle area is proportional to the square of radius, using area to represent a nonnegative value requires radius to vary with the square root of that value; mapping value directly to radius makes the displayed area proportional to the value squared [3]. A map that shades administrative areas should ordinarily encode standardized rates or ratios rather than raw totals, because area-based color otherwise confounds the measured phenomenon with population or land area [17].

Redundant encoding can improve resilience when it does not overload the display. A line series can combine color with direct labels or line patterns. A warning can combine hue, symbol, text, and position. Redundancy is especially important when a distinction must survive grayscale printing, color-vision deficiency, low contrast, or screen-reader use [8][9]. The test is not whether each channel is individually attractive; it is whether the combination preserves one stable distinction across the conditions in which the artifact will travel.

### Scales, baselines, and transformations define the comparison

An axis is part of the claim. Its domain, baseline, interval, direction, transformation, and tick labels determine how distances in the display relate to differences in the data. Bars use length from a baseline, so truncating that baseline breaks the ordinary proportional relation between bar length and value. Lines primarily encode position and change, so nonzero baselines can sometimes be useful for inspecting variation, but the displayed range still changes the perceived magnitude of change. Pandey and colleagues showed experimentally that truncated axes, altered aspect ratios, area distortions, and inverted axes can produce exaggerated or reversed interpretations even when accurate values remain printed on the chart [5].

Logarithmic, indexed, standardized, and normalized scales can reveal structure that raw scales hide, but each transformation changes meaning. A logarithmic axis represents ratios as equal distances; an index represents change relative to a chosen base; a per-capita rate changes a count into an exposure-adjusted comparison. These are analytical choices, not formatting choices. A defensible chart names the transformation, preserves units, identifies the denominator or baseline, and explains why the transformed comparison answers the stated question. When a transformation makes a familiar visual metaphor unreliable, the design should add explanation or provide an untransformed companion view [3][17].

Dual axes deserve special scrutiny because independently adjustable scales can create or erase apparent alignment. Small multiples, indexed series, direct comparison on one scale, or a table often expose the relationship more honestly. When dual axes are unavoidable, each unit, range, and mapping should be explicit, and causal language should not be inferred from visual co-movement. The author's assessment is that the worst scale failure is not an obvious drafting mistake but a technically legal scale that invites the intended audience to make a predictable false comparison [1][5].

### Color must preserve order, difference, and access

Color performs several distinct jobs. Categorical palettes separate groups; sequential palettes represent movement from low to high; diverging palettes encode departure in two directions from a meaningful midpoint; and highlighting color directs attention to selected evidence. These jobs require different structures. Crameri, Shephard, and Heron show that nonuniform rainbow palettes can introduce artificial boundaries, hide variation, destroy intuitive order, and fail for readers with color-vision deficiencies [6]. A perceptually uniform palette instead seeks comparable perceived change for comparable data change.

Palette design should begin with the data relationship, not brand colors. Sequential data need an ordered lightness path. Diverging data need a justified center, such as zero or a policy threshold, placed at the perceptual midpoint. Nominal groups need distinguishable categories without a false magnitude order. Highlight color should be reserved so it remains salient. WCAG adds a nonnegotiable rule: color cannot be the only visual means by which information, action, or distinction is communicated [9]. Direct labels, symbols, patterns, or position should carry the same distinction.

Color meaning is also contextual. Red can signal loss, danger, political affiliation, or simply one category; darker tones may imply more on a light background, but the mapping can become less intuitive on a dark background [3]. A legend or direct label defines the intended code, yet labels do not remove all connotation. The author's synthesis is to test a palette in grayscale, with color-vision simulations, at the smallest expected display size, and with representative readers. If the central comparison disappears under any common condition, color is carrying too much of the message.

### Choose among charts, tables, maps, and dashboards by task

Charts excel when spatial arrangement externalizes a relation the viewer would otherwise compute: ranking, trend, association, distribution, part-to-whole structure, or deviation from a baseline. Tables excel at exact retrieval, heterogeneous units, and comparisons that require the printed values. Schonlau and Peters' experiments support a task-dependent choice rather than a simple chart-over-table hierarchy [4]. A useful report can pair them: the chart makes the pattern visible, while the table supplies exact values and an accessible alternative.

Maps are justified when geography is explanatory or decision-relevant. A choropleth assigns visual weight to geographic area, so it should normally show rates or ratios rather than raw totals; otherwise large or populous areas can dominate for reasons unrelated to the intended variable [17]. Classification breaks, projection, geographic unit, missing regions, disputed boundaries, and within-area variation can each change the apparent pattern. If the question is simply which of a small set of regions has a higher value, a sorted bar chart may support comparison better than a map [17].

Dashboards combine views for recurring monitoring or exploration. Their value is coordination: a user can see an overview, filter the relevant population, inspect detail, relate views, and preserve or extract a state [10]. The author's synthesis is that their risk is fragmented attention. Every tile competes for a limited visual and working-memory budget; inconsistent scales, duplicate legends, hidden filters, and decorative indicators force the user to reconcile several representations before reaching the evidence. A dashboard should therefore expose a small hierarchy of decisions, not display every available metric. Global time, population, and filter state should remain visible, and each view should answer a distinct question that contributes to the shared decision.

### Labels, titles, and annotations guide attention without replacing evidence

Text and graphics form one communication system. A descriptive title identifies the subject; a claim-oriented title states the principal pattern; subtitles carry population, period, geography, units, and status; annotations connect events or qualifications to the marks they concern. Franconeri and colleagues recommend direct labels and placing relevant text near the visual pattern so readers do not spend working memory matching distant legends and prose [3]. Annotation is especially valuable for novice readers who may not know which of many possible comparisons matters.

Guidance can become bias. Kong and colleagues found that slanted titles led viewers to derive opposing messages from the same visualization [14]. A title can therefore identify a supported pattern without asserting a cause the chart does not establish or omitting a material counterpattern. An annotation should distinguish observed value, contextual event, source statement, and interpretation. If the data show a decline after a policy date, the display can state the temporal relation; it should not label the decline as an effect of the policy unless a causal design supports that conclusion [3][14].

Narrative sequencing presents a related trade-off. Segel and Heer identified genres and design strategies through case studies of narrative visualizations, while Hullman and colleagues analyzed 42 professional examples and found evidence for memory and preference benefits from sequences using parallel structure [15][16]. Sequence can reduce overload by introducing evidence progressively and maintaining one comparison at a time. It can also suppress alternatives by fixing the route. The author's synthesis is to preserve a distinction between explanation and exploration: use a guided sequence to establish definitions, context, and central evidence, then provide stable access to the full data, alternative views, and source material.

### Uncertainty is a property of the claim, not a decorative layer

An uncertainty display should identify what is uncertain, what the interval or distribution means, which sources of uncertainty are represented, and which decision it affects. Error bars can represent standard deviations, standard errors, confidence intervals, or prediction intervals; identical glyphs do not make those quantities equivalent. Shaded bands can make changes over time readable but may be mistaken for hard bounds or uniform probability. ONS guidance recommends showing uncertainty when it changes interpretation and avoiding noise when intervals add no decision-relevant information [13].

Hypothetical outcome plots animate draws from a distribution rather than encode the distribution as one static shape. Hullman, Resnick, and Adar found that HOPs lowered error for three-variable ordering judgments compared with violin plots and error bars, but HOPs produced higher error for one high-variance mean-estimation task and required viewers to integrate frames over time [7]. The correct lesson is not that animation is always better. It is that uncertainty formats support different judgments, and the format should be evaluated on the actual inference.

A display should separate measured uncertainty from unmodeled uncertainty. A confidence interval does not include every data-quality problem, structural misspecification, or future regime change. A scenario is conditional on assumptions and need not have a probability. An ensemble samples futures generated by its members and shared model structure, not every possible future. The author's synthesis is to label coverage, method, assumptions, and omissions beside the visual, while linking to a table or downloadable distribution for readers who need exact values [7][13][19].

### Interaction should expose state, support recovery, and preserve meaning

Interaction is useful when it reduces visible complexity without deleting access to evidence. Filtering can focus a population, brushing can relate cases across views, zooming can reveal local structure, and details on demand can preserve precision without printing every value [10]. These actions should not alter a chart's meaning invisibly. The current filters, aggregation, time window, units, and comparison baseline should remain visible; reset and backtracking should be available; and keyboard and assistive-technology operation should be tested [10][20].

Defaults are editorial choices. A dashboard that opens on one subgroup, truncates a range, or sorts by a selected metric frames the first interpretation before the user acts. Tooltips are also weak containers for essential evidence because they may be unavailable in print, screenshots, touch interfaces, keyboard navigation, or screen readers. Essential values, caveats, and sources should remain available outside hover state [8][10][20]. The author's assessment is that interactivity passes the communication gate only when a reader can recover what state produced the visible claim.

### Provenance and reproducibility make the display auditable

Source verification applies to graphics as strictly as to prose. Each displayed value should trace to a source, version, population, period, unit, and transformation. Calculated fields should disclose formulas; exclusions and missing values should be identified; annotations should distinguish external events from inferences. Lerner and colleagues describe provenance as the history of data and computation and show how scripts, input data, output files, plots, and execution traces can be captured to support reproducibility and trust [12].

A reproducible visualization needs more than a final image. It needs the input data or a lawful, documented substitute; code or a precisely described transformation; software and package versions where behavior may vary; chart configuration; and the source and output identifiers that connect the artifacts. An interactive display also needs its default and selected state. Reproducibility does not prove the analysis is valid, but it allows another person to discover whether a filter, changed input, rounding rule, or software default produced the observed graphic [12].

The author's synthesis is an evidence ledger for visual communication. For each important mark or annotation, record the source field, transformation, visual channel, scale, uncertainty rule, and explanatory claim. This makes graphical review a claim-level activity rather than a final aesthetic inspection. A citation under a chart is not enough if the cited file cannot reproduce the plotted values, just as a bibliography does not verify a sentence that misstates its source.

## Evidence

### Graphical-perception experiments established unequal channel accuracy

Cleveland and McGill developed a program of theory and experiments around elementary perceptual judgments. Their 1986 experiment included 24 high-school students, 60 college students, and 43 technically trained professionals who judged position on common and nonaligned scales, length, angle, slope, and area. The two position tasks were most accurate, length was second, angle and slope were third, and area was last; distance between compared objects also affected accuracy [2]. The study's importance is methodological as much as ordinal. It treated a chart as an encoding-decoding system whose component judgments can be experimentally tested.

The result supports aligned dots or bars for precise magnitude comparisons and warns against requiring readers to compare areas or angles when precision matters. Its boundaries also matter. The tested stimuli, participants, and tasks do not establish a universal ranking for every chart, audience, or judgment. Later work reviewed by Franconeri and colleagues shows that familiarity, task, grouping, salience, and semantic conventions can change performance [3]. The defensible conclusion is a default design priority, not a prohibition: give the most important quantitative comparison the clearest available positional structure, then test the complete artifact with representative users.

### Task-specific studies reject a universal chart hierarchy

Schonlau and Peters conducted two web-based studies with a large and diverse sample to compare tables, bar charts, pie charts, and three-dimensional variants. They found that format effects depended on the question: graphs were better for estimating differences, while tables were better for estimating equality and sums. Three-dimensional treatment reduced comprehension for pie charts, and pie charts did not improve comprehension in their tested tasks [4].

This evidence corrects two common overgeneralizations. First, replacing a table with a chart is not automatically an improvement. Second, performance on one perceptual task does not establish superiority for a different task. A product that requires exact retrieval, comparison of many printed values, and a trend overview may therefore need both table and chart views. The display should be evaluated against task completion, not against a style preference [3][4].

### Controlled distortions changed interpretation despite accurate printed data

Pandey and colleagues tested four distortion techniques through Amazon Mechanical Turk with 330 unique U.S. participants whose prior approval rate was at least 99 percent. The message-exaggeration study assigned 250 participants across control and deceptive versions of bar, bubble, and line charts; after attention filtering, 240 observations remained. Deceptive versions produced higher perceived magnitudes for altered aspect ratio, area-as-quantity, and truncated-axis treatments, with all three control-deceptive differences reported as highly significant [5].

The message-reversal study assigned 80 participants to a control or inverted-axis area chart; 78 passed filtering. In the control condition, 39 of 40 participants answered correctly. In the deceptive condition, 7 of 38 answered correctly, 30 answered incorrectly, and one selected uncertainty; the treatment difference was reported as highly significant [5]. Accurate numerical labels were present, so the effect cannot be dismissed as missing data. The visual mapping itself changed the inferred message.

The study used one exemplar family for each distortion, crowd-sourced participants, and simplified questions, so its estimates should not be generalized to all visualizations. Its central finding is nevertheless strong: readers do not neutralize a misleading encoding merely because correct values appear somewhere on the chart. Scale direction, aspect ratio, baseline, and area mapping are part of the factual claim [5].

### Uncertainty experiments show a trade-off between intuitive sampling and exact static reading

Hullman, Resnick, and Adar compared hypothetical outcome plots, error bars, and violin plots on judgments involving one, two, and three random variables. Their reported analyses included 288 subjects. For three-variable ordering judgments, HOP viewers had lower mean absolute error than viewers of violin plots or error bars. For a high-variance one-variable mean-estimation task, however, HOP viewers had significantly higher error than both static alternatives [7]. Viewers saw a median of 89 animated frames across displays, which made sampling relationships concrete but imposed temporal integration.

The evidence rejects the idea that uncertainty has one best visual form. HOPs can make joint probability and ordering visible as repeated outcomes, while static plots can support direct reading of central values and persistent inspection. Designers should state the inference being tested, compare formats on that inference, and disclose whether the uncertainty comes from sampling, modeling, judgment, or scenario choice [7][13].

### Color research identifies perceptual and accessibility failures

Crameri, Shephard, and Heron analyzed the scientific use of color maps and documented how uneven lightness gradients can create false boundaries, suppress real variation, remove intuitive order, and become unreadable for common color-vision deficiencies. They recommend perceptually uniform palettes whose visible changes correspond more consistently to data changes and palette classes matched to the data relationship [6]. The work is a peer-reviewed perspective and methodological guide rather than one randomized user experiment, but it synthesizes color science and provides diagnostic methods in perceptual color spaces.

WCAG supplies an independent normative gate. Success Criterion 1.4.1 prohibits using color as the only visual means of conveying information, while Success Criterion 1.1.1 requires text alternatives for non-text content and identifies longer descriptions and tables as solutions for charts whose purpose cannot be captured by a short label [8][9]. Together, the sources show that a palette can fail in two ways: it can distort the quantitative pattern for typical vision, or it can make the distinction unavailable to part of the audience. A defensible display addresses both.

### Narrative and annotation research shows that guidance changes interpretation

Kong and colleagues studied titles for visualizations on controversial topics. Before the experiments, they coded 200 visualization titles from four major news sites and found that more than 20 percent contained evaluative or framing statements. Experiment 1 then collected 888 participant-composed titles; Experiment 2 tested how title slant affected interpretation. Slant influenced the perceived main message, with readers deriving opposing messages from the same graphic, while the study found no significant effect on attitude change [14]. Text near a chart is therefore not neutral metadata; it can direct attention and inference.

Sequence also has measurable effects. Hullman and colleagues qualitatively analyzed 42 professional narrative visualizations, modeled local transitions, and conducted two validation studies. Their results included audience rankings of transition types and memory and subjective-rating benefits for sequences using parallelism [16]. Segel and Heer's earlier design study identified recurring genres, narrative structures, visual highlighting, and interaction strategies across online journalism and visualization examples [15]. These findings support deliberate ordering and annotation, but they also require a counterweight: guided reading should not erase the source, uncertainty, or alternative views that would let a reader audit the story.

### Reproducibility evidence turns a graphic into a traceable computational result

Lerner and colleagues describe data provenance as the record of inputs, scripts, outputs, plots, and execution steps behind an analysis. Their R tooling captures coarse-grained artifacts and fine-grained execution traces, then supports summaries, debugging, comparison, and visual inspection of provenance [12]. The work demonstrates a technical mechanism rather than proving that provenance automatically improves every reader's judgment. It also reports limitations, including incomplete capture for some language behavior.

The relevant communication result is bounded but important. A visualization can change when its data, script, library, configuration, or default changes, even if the final image gives no visible account of the transformation. Provenance provides a way to locate that change and reproduce the path from source to output. It does not validate the source data, but it makes undisclosed transformations and irreproducible screenshots harder to treat as self-authenticating evidence [12].

## Implications

### For analysts and researchers

The analytical workflow should preserve the distinction between discovering a pattern and communicating a supported conclusion. Explore broadly with multiple scales, encodings, filters, and diagnostics, then reconstruct the explanatory graphic from verified data and an explicit question. Matejka and Fitzmaurice's Datasaurus Dozen shows why this separation matters: datasets can share means, standard deviations, and correlations while forming radically different plotted patterns [11]. Summary statistics and visualization therefore check different failure modes; neither replaces the other.

Before publication, build a claim inventory for the graphic. Record the source, data vintage, population, denominator, unit, missingness rule, transformations, uncertainty definition, and software state. Recalculate displayed values from the source and compare them with labels and tooltips. Inspect outliers rather than deleting them silently. If the display uses a model output, distinguish observed data, fitted values, prediction, and scenario. Preserve the code and inputs necessary to regenerate the artifact or document why an input cannot be shared [12].

Chart selection should follow the comparison. Use aligned position for important quantitative judgments where feasible [2]. Use a table for exact retrieval or mixed units, and pair it with a chart when pattern recognition also matters [4][8]. Normalize choropleth data to a meaningful population or exposure and label the denominator [17]. Avoid decorative three-dimensional forms that add occlusion or perspective without adding a variable [4]. Test alternate scale choices and ask whether any legal setting creates a predictable false impression [5].

Uncertainty should be designed with the analysis rather than added after the central estimate. Name the interval, coverage, method, and represented error sources. If the conclusion changes when intervals overlap or a threshold is crossed, make that uncertainty visible. If the interval would add no interpretive information, retain it in the downloadable data and explain the evidentiary status in text [13]. Use animation only when temporal sampling supports the intended judgment and when pause, restart, and static alternatives are available [7][8][20].

### For editors, journalists, and public communicators

A visual fact-check should examine the data chain and the rhetorical layer separately. First verify the values, definitions, dates, sources, transformations, and uncertainty. Then inspect axis direction, baseline, aspect ratio, sorting, color, geographic normalization, annotations, and title. Pandey and colleagues show why correct labels do not excuse a distorted visual relation [5]. A chart can contain no fabricated number and still induce a false message.

Titles should state only what the displayed evidence supports. A claim-oriented title can reduce search and make the intended comparison explicit, but title slant can also change the perceived takeaway [3][14]. Separate four classes of text: the observed pattern, the source or event context, the analytical interpretation, and the causal claim. If a line falls after an event, annotate the event and describe the temporal sequence. Do not label the event as the cause unless the evidence supports causation. Material counterpatterns and qualifications should remain adjacent to the claim, not hidden in a distant note.

Narrative sequence should reduce complexity without manufacturing inevitability. Introduce definitions and the broad view first, move to the decisive comparison, expose uncertainty and counterevidence, and end with the warranted conclusion. Parallel visual structure can aid memory [16]. Readers should still be able to inspect the full time range, obtain exact values, and reach source material. An interactive story should not require animation or scrolling to recover an essential fact; a static summary and data alternative should survive when the presentation layer fails [8][15].

Publication metadata should travel with the graphic. Include a source line, date or vintage, population, unit, transformation, and a stable route to data and methods. A screenshot separated from these fields is an orphan claim. Where redistribution is likely, place the essential qualifier inside the exported artifact rather than relying on surrounding prose. Corrections should update the chart, data, caption, accessible description, embedded copies, and downstream exports; correcting only the dashboard leaves the circulated image wrong [8][12].

### For dashboard and product teams

A dashboard should be designed around a recurring decision and a visible state model. Define the primary audience, monitoring interval, thresholds, comparison population, and response. Make global filters, time windows, data freshness, and units persistent. Coordinate scales and colors across tiles. A reader should not have to remember that blue means revenue in one panel and incidents in another, or that one chart uses monthly values while another uses year-to-date totals [3][10][12].

Apply Shneiderman's interaction tasks deliberately [10]. The overview should show the whole relevant collection without implying that everything is equally important. Zoom and filtering should narrow the evidence without losing visible context. Details on demand should supply exact values and definitions, not hide the only explanation. Relating views should use stable highlighting. History should allow users to understand and undo prior actions. Extract should preserve the state, source, and metadata required to interpret the exported result.

The author's synthesis is that the worst dashboard failure is a confident action based on an invisible state. Prevent it by displaying active filters near the title, generating state-aware subtitles and exports, offering reset and back navigation, and logging the data version and query behind consequential views. Defaults should be reviewed as editorial choices. If changing a default population, range, or aggregation reverses the apparent conclusion, the dashboard needs either a stronger comparison design or an explicit warning [10][12].

Accessibility belongs in acceptance testing. All controls should work by keyboard and expose names, roles, values, and state to assistive technology [20]. Color distinctions need labels, shapes, patterns, or position [9]. Every chart needs a concise text summary and a route to underlying tabular data where practical [8]. Tooltips should not contain unique essential information. Focus order should follow the analytical sequence, and dynamic updates should be announced without overwhelming the user. Test with screen readers, magnification, color-vision simulation, reduced motion, narrow screens, and representative users rather than assuming framework defaults are sufficient [20].

### For decision-makers and readers

A reader should begin by identifying the display's question, population, period, units, and source. Then inspect what each visual property means. Ask whether position, length, area, color, or animation carries the important difference; whether the scale starts where the visual metaphor implies; whether a rate has an appropriate denominator; whether the map shows geography or merely area; and whether filters or defaults selected the visible cases [2][5][17].

The reader should separate reading from inference. The chart may show that two series moved together, not that one caused the other. It may show a central estimate without the uncertainty needed to compare groups. It may show selected scenarios without probabilities. It may annotate one event while omitting others. The appropriate response is not blanket distrust. It is calibrated inspection: recover the data definition, check the source, compare an alternative view, and ask what unshown evidence would change the conclusion [3][13][19].

Tables, downloads, and accessible descriptions are audit tools, not secondary products. Exact values can reveal whether a dramatic visual difference is small in the original unit. A table can show missing entries, inconsistent precision, or category changes. A downloadable dataset can reveal whether the chart selected only part of the period. Provenance and code can show whether a transformation or software default created the result [4][8][12]. No one reader must repeat the entire analysis, but the artifact should make such inspection possible.

When consequences are high, prefer reversible decisions and explicit thresholds. A dashboard warning should identify the value, uncertainty, trigger, and data freshness. An investment chart should distinguish nominal from real values, stock from flow, and reported from adjusted measures. A public-health graphic should show denominators and absolute as well as relative quantities where the decision depends on both [3][5][13]. The author's synthesis is that visual literacy means asking not "Is this chart attractive?" but "Which comparison does this design make easy, which comparison does it suppress, and is that allocation of attention justified by the decision?" [3][5].

### A publication gate for truthful visual communication

The author's synthesis is a ten-part gate. First, define the audience, question, and decision. Second, verify the source, version, unit, denominator, and population. Third, reproduce every transformation. Fourth, map the central comparison to an accurate channel. Fifth, audit scales, baselines, direction, aspect ratio, normalization, and missing data. Sixth, choose color by data relationship and provide redundant distinctions. Seventh, label observed patterns, context, uncertainty, and interpretation separately. Eighth, expose interactive state and preserve reset, history, and export metadata. Ninth, provide text and tabular alternatives and test assistive access. Tenth, retain data, code, configuration, and provenance sufficient to reproduce the artifact [2][5][6][8][9][10][12][20].

The author's synthesis is that a failure at one gate determines the remedy. A source mismatch returns to verification. A denominator error returns to data preparation. A misleading scale returns to encoding. An inaccessible distinction returns to redundant design and alternative content. A narrative overclaim returns to annotation and wording. An irreproducible image returns to provenance. The goal is not a chart that cannot be criticized. It is a chart whose evidence, design choices, uncertainty, and access routes remain open to inspection and correction.

## Sources

1. Friendly, M. (2006). "A Brief History of Data Visualization." In
   Handbook of Computational Statistics: Data Visualization. Springer.
   https://www.datavis.ca/papers/hbook.pdf [high]

2. Cleveland, W. S., & McGill, R. (1986). "An Experiment in Graphical
   Perception." International Journal of Man-Machine Studies, 25(5),
   491-500. https://doi.org/10.1016/S0020-7373(86)80019-0 [high]

3. Franconeri, S. L., Padilla, L. M., Shah, P., Zacks, J. M., & Hullman,
   J. (2021). "The Science of Visual Data Communication: What Works."
   Psychological Science in the Public Interest, 22(3), 110-161.
   https://doi.org/10.1177/15291006211051956 [high]

4. Schonlau, M., & Peters, E. (2012). "Comprehension of Graphs and Tables
   Depend on the Task: Empirical Evidence from Two Web-Based Studies."
   Statistics, Politics and Policy, 3(2), 1-35.
   https://doi.org/10.1515/2151-7509.1054 [high]

5. Pandey, A. V., Rall, K., Satterthwaite, M. L., Nov, O., & Bertini, E.
   (2015). "How Deceptive Are Deceptive Visualizations? An Empirical
   Analysis of Common Distortion Techniques." Proceedings of CHI 2015,
   1469-1478. https://doi.org/10.1145/2702123.2702608 [high]

6. Crameri, F., Shephard, G. E., & Heron, P. J. (2020). "The Misuse of
   Colour in Science Communication." Nature Communications, 11, 5444.
   https://doi.org/10.1038/s41467-020-19160-7 [high]

7. Hullman, J., Resnick, P., & Adar, E. (2015). "Hypothetical Outcome
   Plots Outperform Error Bars and Violin Plots for Inferences About
   Reliability of Variable Ordering." PLOS ONE, 10(11), e0142444.
   https://doi.org/10.1371/journal.pone.0142444 [high]

8. World Wide Web Consortium. "Understanding Success Criterion 1.1.1:
   Non-text Content," Web Content Accessibility Guidelines 2.2.
   https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html [high]

9. World Wide Web Consortium. "Understanding Success Criterion 1.4.1:
   Use of Color," Web Content Accessibility Guidelines 2.2.
   https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html [high]

10. Shneiderman, B. (1996). "The Eyes Have It: A Task by Data Type
    Taxonomy for Information Visualizations." Proceedings of the IEEE
    Symposium on Visual Languages, 336-343.
    https://www.cs.umd.edu/~ben/papers/Shneiderman1996eyes.pdf [high]

11. Matejka, J., & Fitzmaurice, G. (2017). "Same Stats, Different Graphs:
    Generating Datasets With Varied Appearance and Identical Statistics
    Through Simulated Annealing." Proceedings of CHI 2017.
    https://doi.org/10.1145/3025453.3025912 [high]

12. Lerner, B., Boose, E., Brand, O., et al. (2022). "Making Provenance
    Work for You." The R Journal, 14(4), 141-159.
    https://doi.org/10.32614/RJ-2023-003 [high]

13. Office for National Statistics. "Showing Uncertainty in Charts."
    Data Visualisation Service Manual.
    https://service-manual.ons.gov.uk/data-visualisation/guidance/showing-uncertainty-in-charts [high]

14. Kong, H.-K., Liu, Z., & Karahalios, K. (2018). "Frames and Slants in
    Titles of Visualizations on Controversial Topics." Proceedings of
    CHI 2018. https://doi.org/10.1145/3173574.3174012 [high]

15. Segel, E., & Heer, J. (2010). "Narrative Visualization: Telling Stories
    With Data." IEEE Transactions on Visualization and Computer Graphics,
    16(6), 1139-1148. https://doi.org/10.1109/TVCG.2010.179 [high]

16. Hullman, J., Drucker, S., Riche, N. H., Lee, B., Fisher, D., & Adar,
    E. (2013). "A Deeper Understanding of Sequence in Narrative
    Visualization." IEEE Transactions on Visualization and Computer
    Graphics, 19(12), 2406-2415.
    https://doi.org/10.1109/TVCG.2013.119 [high]

17. Office for National Statistics. "Choropleth Maps." Data Visualisation
    Service Manual.
    https://service-manual.ons.gov.uk/data-visualisation/chart-types/choropleth-maps [high]

18. Bradshaw, N. A. (2020). "Florence Nightingale (1820-1910): An
    Unexpected Master of Data." Patterns, 1(2), 100036.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC7660360 [high]

19. Spiegelhalter, D., Pearson, M., & Short, I. (2011). "Visualizing
    Uncertainty About the Future." Science, 333(6048), 1393-1400.
    https://doi.org/10.1126/science.1191181 [high]

20. World Wide Web Consortium. "Web Content Accessibility Guidelines
    (WCAG) 2.2." Success Criteria 2.1.1 (Keyboard), 2.2.2 (Pause, Stop,
    Hide), 2.3.3 (Animation from Interactions), 2.4.3 (Focus Order),
    4.1.2 (Name, Role, Value), and 4.1.3 (Status Messages).
    https://www.w3.org/TR/WCAG22/ [high]

## See Also

- `library/communication/public-speaking-and-presentation-design.md` -- coordinates visual evidence with spoken explanation and audience attention.
- `library/communication/source-verification-and-fact-checking.md` -- verifies data, calculations, provenance, uncertainty, and the claims attached to a display.
- `library/communication/information-architecture-and-content-design.md` -- structures labels, navigation, hierarchy, and alternative routes through information.
- `library/probabilistic-thinking-forecasting/communicating-forecast-uncertainty.md` -- develops intervals, distributions, fan charts, ensembles, and decision thresholds in depth.
- `library/mathematics-statistics/regression-analysis.md` -- includes graphical diagnostics and the evidence that identical summaries can hide different data structures.
- `library/notable-people/florence-nightingale-data-institutions-modern-nursing.md` -- examines statistical graphics as part of an institutional reform and accountability system.

