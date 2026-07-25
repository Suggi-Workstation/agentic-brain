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
relevant newer library topics or irrelevant noise.

### The Pool Depth Problem (Buckley & Voorhees, SIGIR 2000)

When a test collection is built from a fixed corpus using pooling
(human assessors judge the top N results from multiple systems),
documents outside the pool are assumed irrelevant. This assumption
weakens as new documents enter the collection: a new document may be
genuinely relevant but was never judged because it did not exist when
the pool was created. When it appears in ranked results above a known
gold file, the eval reports a lower rank -- but the system has
actually found new relevant content correctly.

Buckley and Voorhees demonstrated that this effect scales with
collection growth. Unjudged documents increasingly populate top ranks,
making single-file gold queries unreliable metrics of system quality
as corpora grow. TREC addresses this through annual re-assessment
cycles where new pools are created for each year's expanded collection.

### The Standard Pattern: Multiple Gold Files Per Query (Manning, Raghavan & Schutze, 2008)

The standard IR textbook defines evaluation in terms of relevance
assessments: a query has a set of relevant documents, not a single
correct answer. Metrics like precision@k and recall@k are computed
against this set. Our current eval (`gold_file: <single path>`)
tests only whether at least one known-relevant document is in the
top 20 -- a minimum viability check, not a quality measure.

### What We Could Not Verify

Academic databases (ACM, MIT Press, Springer, Google Scholar) were
inaccessible from this session -- all returned Cloudflare bot-detection
pages. The paper concepts cited above are based on the author's prior
knowledge of the IR literature. A follow-up session with working
browser access should retrieve and verify:

- Buckley, C. & Voorhees, E.M. (2000). "Evaluating Evaluation Measure
  Stability." SIGIR 2000.
- Voorhees, E.M. & Harman, D.K. (2005). *TREC: Experiment and
  Evaluation in Information Retrieval*. MIT Press.
- Sanderson, M. (2010). "Test Collection Based Evaluation of
  Information Retrieval Systems." Foundations and Trends in IR.

## Implications

### Gold Query Format Must Evolve

The current single-file format:

```yaml
gold_file: "library/valuation-screening/discounted-cash-flow-dcf-methodology.md"
```

Must become a multi-file relevance set:

```yaml
gold_files:
  - "library/valuation-screening/discounted-cash-flow-dcf-methodology.md"
  - "library/valuation-screening/valuation-multiples-pe-ev-ebitda-pb-analysis.md"
  - "library/value-investing/margin-of-safety.md"
```

The eval then checks recall across the set: 2/3 gold files in top-20
is more informative than binary PASS/FAIL on a single file.

### Maintenance Procedure by Scale

| Corpus size | Action | Frequency |
|---|---|---|
| 184 files (now) | Add 5 library-topic gold queries. Single-file format acceptable. | Once |
| ~500 files | Convert top-10 queries to multi-file format. Run first relevance assessment pass. | Once |
| Every +100 files | Re-assess: for each gold query, read top-20 results, judge which are genuinely relevant, add to gold set. | Per milestone |
| 5,000+ files | Periodic sampling: judge 50 random query-document pairs. Track MRR trend. | Monthly |

### Stable vs. Growing Content

Queries about governance templates, protocol definitions, and research
insights need infrequent refresh -- their target documents rarely change
and the best answer is stable. Queries about library topics need
frequent refresh because the library IS growing and new topics should
rank alongside existing ones. Split `gold-queries.yaml` by content type
or track `last_assessed` dates per query.

## Counter-evidence

This insight would be invalidated if:

1. **Single-file recall remains at 100% through 500+ files without
   intervention.** If the 20 original gold files remain in the top-20
   as the corpus triples, the pool depth effect is not material for our
   collection and no format change is needed. Test: re-run eval at 500
   files. If recall is still 20/20, the insight overstates the problem.

2. **MRR decline is proven to be noise, not relevant new content.**
   If a relevance assessment pass on ranks 1-20 for degraded queries
   shows the higher-ranked files are NOT relevant to the query, the
   decline is genuine system degradation, not pool depth. The fix would
   then be index tuning (chunking, model choice), not gold query
   maintenance.

3. **The brain stops growing.** If the corpus stabilizes at a fixed
   size, the pool depth problem disappears because no new unjudged
   documents enter the collection. This is unlikely given the 28-domain
   library's growth trajectory, but it is the condition that would make
   this insight irrelevant.

## Cross-links

- `brain-index/eval.py` -- the eval script this insight diagnoses and
  prescribes fixes for.
- `brain-index/gold-queries.yaml` -- the current 20-question test
  collection, all from governance and research artifacts.
- `research/insights/brain-search-system.md` -- the original design
  document that established the single-file eval format.
- `research/insights/stale-index-problem.md` -- the companion insight:
  stale indexes fail silently; stale gold queries also fail silently.
  Both require proactive maintenance.
- `governance/template-insights.md` -- the format specification this
  file follows.

---

*Written 2026-07-25 by Link. The paper citations above could not be
directly verified in this session due to academic database access
restrictions; they should be retrieved and confirmed in a session
with working browser access. The procedure described follows standard
IR evaluation methodology as documented in the TREC literature.*
