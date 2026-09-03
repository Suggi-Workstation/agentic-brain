# brain-index -- Search agentic-brain

Hybrid file retrieval over the `agentic-brain` repository. It combines
EmbeddingGemma semantic search with BM25 keyword search, merges both rankings
with Reciprocal Rank Fusion (RRF), and returns one best chunk per file.

Gold questions measure the search results. They never influence live ranking.

## VPS Commands

Run from `/srv/brain/agentic-brain`:

```bash
/opt/repo-tools/venv/bin/python brain-index/query.py --check-freshness
/opt/repo-tools/venv/bin/python brain-index/query.py "<question>" --top-k 20
/opt/repo-tools/venv/bin/python brain-index/index.py --check
/opt/repo-tools/venv/bin/python brain-index/eval.py --validate-only
/opt/repo-tools/venv/bin/python brain-index/eval.py --verbose
/opt/repo-tools/venv/bin/python brain-index/self-test.py
```

The watcher owns index builds on the VPS. Do not run `index.py --force` unless
recovering a diagnosed corrupt index or changing the embedding model.

## Files

- `index.py`: incremental/full index builder and freshness check.
- `query.py`: dense + BM25 + RRF retrieval.
- `eval.py`: relevance-set validation and Recall/MRR/nDCG evaluation.
- `gold-queries.yaml`: curated questions and relevant repository files.
- `self-test.py`: package contract and regression tests.
- `config.yaml`: model, chunking, fusion, and data-path settings.

## Data and Evaluation

Index data lives in `~/.brain-index` (`/srv/brain/index` on the VPS), outside
git. Gold entries use `gold_files` because one question can have more than one
relevant file. Every target must exist, be nonempty, and appear in the index.

Refresh relevance judgments when the corpus grows materially. Test any future
chunk-context or reranking change against the same reviewed gold set before
adopting it.