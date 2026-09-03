---
name: gold-query-maintenance-procedure
id: 20260725T213429Z
tier: insight
source:
  - 20260719T223002Z
  - brain-index/eval.py
author: Link
tags: [gold-queries, evaluation, information-retrieval, test-collections, brain-index, maintenance]
links:
  - brain-index/eval.py
  - brain-index/gold-queries.yaml
  - research/insights/brain-search-system.md
  - research/insights/stale-index-problem.md
---

# Gold Query Maintenance -- When Recall@20 Masks the Pool Depth Problem

## The Insight

A test collection with single-file gold queries cannot distinguish
retrieval degradation from healthy collection growth as the corpus
expands, because unjudged relevant documents increasingly populate
top ranks where they are indistinguishable from noise.

## Evidence

### Source: The Brain Search System Insight (20260719T223002Z)

The brain-index eval system was designed with a binary PASS/FAIL gate:
each gold query checks whether one specific file appears in the top-20
results. This was sufficient at 126 files. The eval was run on
2026-07-25 with the current 184-file corpus: all 20 gold queries
passed, but the ranking distribution had shifted. Query g012 (library
system) fell from rank 3 to rank 12. The eval reported PASS because
the gold file appeared at position 12, within the top-20 boundary --
but the metric could not say whether ranks 1-11 contained genuinely
relevant newer library topics or irrelevant noise. This diagnostic gap
is the pool depth problem.

### The Pool Depth Problem (TREC, Buckley & Voorhees 2000)

Test collections in information retrieval are built from a fixed corpus
using a technique called pooling: human assessors judge the top N
results from multiple systems, creating a set of known-relevant documents
for each query. A document not in the pool is assumed irrelevant -- but
this assumption weakens as new documents enter the collection. A new
document may be genuinely relevant to the query but was never judged
because it did not exist when the pool was created. When it appears in
ranked results above the known gold file, the eval sees a lower rank for
the gold file and reports degradation -- but the system is actually
performing correctly: it found new relevant content.

Buckley and Voorhees (2000, "Evaluating Evaluation Measure Stability,"
SIGIR 2000) demonstrated that this effect is not theoretical. As
collection size grows, unjudged documents increasingly populate top
ranks, making single-file gold queries unreliable metrics of system
quality. TREC addresses this through annual re-assessment cycles where
new pools are created for each year's expanded collection, with human
assessors re-judging the top-ranked documents against each query.

### The Standard Response: Multiple Gold Files Per Query (Manning, Raghavan & Schutze 2008)

The standard IR textbook (Manning, Raghavan, and Schutze, *Introduction
to Information Retrieval*, 2008, Chapter 8) defines evaluation in terms
of *relevance assessments*: a query has a set of relevant documents, not
a single correct answer. Metrics like precision@k and recall@k are
computed against this set of known-relevant documents. A perfect system
would return ALL relevant documents in the top ranks, not just one.

Our current eval tests the weakest form of this: "is at least one
known-relevant document in the top 20?" This is a minimum viability
check, not a quality measure. To measure quality, we need the full set
of known-relevant documents for each query, and the eval should check
how many of them appear (recall across the set) and how high they rank
(MRR and nDCG computed across all gold files for that query).

### Relevance Drift (TREC, Voorhees & Harman 2005)

A related but distinct problem: as the collection matures, the
*information need* behind a query can shift. The query "how should the
library be populated?" had one clear answer on July 21, 2026 (the
library-system design document). By late July 2026, the best answer may
be a curated list of the highest-quality library topics actually written
since. The gold file is correct but no longer the *best* answer. For our
system, this means:

- Gold queries about governance and research artifacts (which rarely
  change) remain stable. Queries about governance templates, the
  logbook protocol, or the system blueprint should maintain their
  rankings indefinitely because the target documents are the definitive
  sources and no competing documents address the same questions.

- Gold queries about the library require periodic refresh because the
  library IS growing. The answer to "how does valuation work?" expands
  as more valuation topics are written. The original DCF methodology
  topic may still be relevant, but newer topics on valuation multiples
  and the Graham Number should also rank highly for that query.

### What We Could Not Verify

Academic databases (ACM Digital Library, MIT Press, Springer, Google
Scholar) were inaccessible from this session's environment -- all
returned Cloudflare bot-detection pages. The paper titles and concepts
cited above are based on the author's prior knowledge of the IR
literature. A follow-up session with working browser access should
retrieve and verify the full text of:

- Buckley, C. & Voorhees, E.M. (2000). "Evaluating Evaluation Measure
  Stability." SIGIR 2000.
- Voorhees, E.M. & Harman, D.K. (2005). *TREC: Experiment and
  Evaluation in Information Retrieval*. MIT Press.
- Sanderson, M. (2010). "Test Collection Based Evaluation of
  Information Retrieval Systems." Foundations and Trends in Information
  Retrieval.
- TREC overview papers (annual, trec.nist.gov) -- the pooling
  methodology and relevance assessment procedures are documented in
  each year's overview.

## Implications

### Gold Query Format Uses Relevance Sets

The implemented format maps one query to a set of relevant files:

```yaml
gold_files:
  - "library/valuation-screening/discounted-cash-flow-dcf-methodology.md"
  - "library/valuation-screening/valuation-multiples-pe-ev-ebitda-pb-analysis.md"
  - "library/value-investing/margin-of-safety.md"
```

The eval then checks: how many of the gold files appear in the top 20?
Recall becomes: 2/3 gold files found = 0.67 recall across the set. This
is more informative than binary PASS/FAIL on a single file, and it
degrades gracefully: if one gold file drops out of the top 20, the
metric drops proportionally rather than flipping from PASS to FAIL.

### Implemented Evaluator Gate -- 2026-09-03

The three repository evaluators now implement the same file-level gate:

- Accept one `gold_file` or a `gold_files` relevance set.
- Reject malformed IDs/questions, empty relevance sets, unsafe paths,
  missing or empty targets, and targets absent from the live index
  before scoring.
- Run dense and BM25 retrieval independently and fail if either branch
  is empty; a single-modality result cannot masquerade as hybrid health.
- Fuse with the configured RRF value, deduplicate by file before the
  final result limit, and compute Recall@20, MRR, and nDCG over file
  relevance rather than duplicate chunks.

Gold questions remain offline test data. They do not train, expand, or
rank live queries.

### Maintenance Procedure by Scale

| Trigger | Action | Frequency |
|---|---|---|
| Initial corpus | Cover each distinct information need and stable control surface with realistic questions. | Once |
| Material corpus growth | Reassess top-ranked results, add newly relevant files to `gold_files`, and investigate relevant files that leave the result window. | At growth milestones |
| Retrieval-pipeline change | Validate all targets and compare the complete scored set before and after the change. | Every change |
| Review workload becomes material | Sample query-document judgments using a documented method rather than weakening target validation. | When justified by measured workload |

### Stable vs. Growing Content

Queries about governance templates, protocol definitions, and research
insights need infrequent refresh -- their target documents rarely change
and no competing documents address the same questions. Queries about
library topics need more frequent refresh because the library IS growing
and new topics should rank alongside existing ones.

Maintenance cadence follows information-need stability and corpus
churn, not a fixed ratio to file or chunk counts. No additional tracking
schema is needed until missed reviews become an observed problem.

### Interpreting Eval Results

| Metric trend | Possible meaning | Action |
|---|---|---|
| Recall@20 drops from 100% to 95% | One gold file dropped out of top 20 | Check: pushed out by genuinely relevant new content or by noise? |
| MRR drops from 0.66 to 0.40 | Gold files ranking lower on average | Relevance assessment pass: judge new top-ranked documents |
| Recall stays 100%, MRR drops slightly | New relevant files ranking above gold files (healthy growth) | Add new files to gold set; MRR recovers |
| All metrics drop sharply after index rebuild | Index corruption, code regression, or relevance-set drift | Run state validation and self-tests; rebuild only when artifact/model/config integrity requires it |
| All metrics drop gradually over months | Pool depth accumulating unjudged documents | Scheduled relevance assessment is overdue |

### For the Long-Term Architecture

If manual relevance assessment becomes impractical, candidate
production responses include:

- **Click-through rate as implicit relevance:** track which results
  users actually open. In our agent-only system, this maps to: which
  files does the agent actually `read_file` after a `query.py` call?
  This is automatic relevance feedback requiring no manual judging.

- **Query-document co-occurrence:** if "DCF" and "terminal value"
  appear together in multiple user queries and both return the same
  topic, it is a strong signal of relevance. Co-occurrence patterns
  can be extracted from session logs.

- **Periodic sampling:** judge a random sample of 50 query-document
  pairs rather than every pair. The sample size needed for statistical
  significance is surprisingly small, and random selection eliminates
  the bias of only checking queries that "feel wrong."

These feedback mechanisms are not yet justified for the repository
indexes: corrected relevance sets already satisfy the current retrieval
gate. Multi-file gold queries are supported now, so richer judgments can
be added incrementally without a future format migration.

## Counter-evidence

This insight would be invalidated if:

1. **Single-file recall remains at 100% through 500+ files without
   intervention.** If the 20 original gold files remain in the top-20
   as the corpus triples in size, the pool depth effect is not material
   for our collection scale and no format change is needed. Test: re-run
   the current eval at 500 files without modifying gold-queries.yaml.
   If recall is still 20/20, this insight overstates the problem.

2. **MRR decline is proven to be noise, not relevant new content.**
   If a relevance assessment pass on ranks 1-20 for degraded queries
   shows the higher-ranked files are NOT relevant to the query, the
   decline is genuine system degradation (chunking, embedding model,
   or ranking logic), not pool depth. The fix would then be index
   tuning, not gold query maintenance.

3. **The brain stops growing.** If the corpus stabilizes at a fixed
   size, the pool depth problem disappears because no new unjudged
   documents enter the collection. This is unlikely given the 28-domain
   library's growth trajectory and the planned company 10-K/10-Q
   archive, but it is the condition under which this insight becomes
   irrelevant.

## Cross-links

- `brain-index/eval.py` -- the eval script this insight diagnoses and
  prescribes fixes for. It now validates multi-file relevance sets
  before scoring.
- `brain-index/gold-queries.yaml` -- the live test collection. Counts
  and coverage are derived from this file rather than duplicated here.
- `research/insights/brain-search-system.md` -- the original design
  document that established the retrieval and evaluation gate.
- `research/insights/stale-index-problem.md` -- the companion insight:
  stale indexes fail silently because no one checks freshness; stale
  gold queries also fail silently because recall@20 masks the pool
  depth effect. Both require proactive maintenance that fires
  automatically, not manually.
- `governance/template-insights.md` -- the format specification this
  file follows. Any structural changes to insight format affect this
  file.

---

*Written 2026-07-25 by Link. The paper citations above could not be
directly verified in this session due to academic database access
restrictions (Cloudflare bot detection); they should be retrieved and
confirmed in a session with working browser access. The procedure
described follows standard IR evaluation methodology as documented in
the TREC literature and Manning, Raghavan & Schutze (2008).*
