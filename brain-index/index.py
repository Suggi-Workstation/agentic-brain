#!/usr/bin/env python3
"""
Build the brain-index from agentic-brain markdown files.

Usage:
    python index.py              # incremental build
    python index.py --force      # full rebuild
    python index.py --check      # check freshness only (no rebuild)
"""

import json
import os
import re
import sys
import time
import hashlib
from datetime import datetime, timezone
from pathlib import Path

import yaml
import numpy as np

# --- Config ---
SCRIPT_DIR = Path(__file__).resolve().parent
BRAIN_ROOT = SCRIPT_DIR.parent

with open(SCRIPT_DIR / "config.yaml") as f:
    cfg = yaml.safe_load(f)

DATA_DIR = Path(os.path.expanduser(cfg["index"]["data_dir"]))
DATA_DIR.mkdir(parents=True, exist_ok=True)

META_PATH = DATA_DIR / "meta.json"
CHUNKS_PATH = DATA_DIR / "chunks.jsonl"
VECTORS_PATH = DATA_DIR / "vectors.npy"


def load_embedder():
    """Lazy-load sentence-transformers (heavy import, done once)."""
    from sentence_transformers import SentenceTransformer
    model_name = cfg["embedding"]["model"]
    print(f"Loading embedder: {model_name} ...", flush=True)
    model = SentenceTransformer(model_name, device=cfg["embedding"]["device"])
    print(f"  Loaded. dim={model.get_sentence_embedding_dimension()}", flush=True)
    return model


def iter_markdown_files(root: Path, exclude_dirs: set, exclude_exts: set):
    """Yield (rel_path, abs_path) for every indexable markdown file."""
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in exclude_dirs]
        for fn in sorted(filenames):
            if fn.startswith("."):
                continue
            ext = os.path.splitext(fn)[1].lower()
            if ext in exclude_exts:
                continue
            if ext not in (".md",):
                continue
            abs_path = os.path.join(dirpath, fn)
            rel_path = os.path.relpath(abs_path, root).replace("\\", "/")
            yield rel_path, abs_path


def parse_frontmatter(text: str):
    """Extract YAML frontmatter and body from markdown text."""
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        fm = {}
    body = parts[2].strip()
    return fm, body


def chunk_text(text: str, max_chars: int, overlap: int):
    """Split text into overlapping chunks, respecting markdown headings."""
    if len(text) <= max_chars:
        return [text]

    chunks = []
    paragraphs = text.split("\n\n")
    current = ""

    for para in paragraphs:
        if len(current) + len(para) + 2 <= max_chars:
            current = (current + "\n\n" + para).strip() if current else para
        else:
            if current:
                chunks.append(current[:max_chars])
            # If a single paragraph is too long, split it
            if len(para) > max_chars:
                words = para.split()
                sub = ""
                for w in words:
                    if len(sub) + len(w) + 1 <= max_chars:
                        sub = (sub + " " + w).strip()
                    else:
                        chunks.append(sub)
                        # Overlap: carry last few words
                        overlap_words = sub.split()[-overlap // 6:]
                        sub = " ".join(overlap_words) + " " + w
                if sub:
                    chunks.append(sub)
                current = ""
            else:
                current = para

    if current:
        chunks.append(current[:max_chars])

    return chunks


def file_hash(path: str) -> str:
    """Fast hash of file contents for change detection."""
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


def build_index(force: bool = False):
    """Build or refresh the brain index."""
    t0 = time.time()

    # --- Change detection ---
    exclude_dirs = set(cfg["index"]["exclude_dirs"])
    exclude_exts = {".json", ".yaml", ".yml", ".py", ".sh", ".bat",
                    ".png", ".jpg", ".gif", ".svg", ".ico"}

    files_now = {}
    for rel, abs_path in iter_markdown_files(BRAIN_ROOT, exclude_dirs, exclude_exts):
        files_now[rel] = {"path": abs_path, "hash": file_hash(abs_path)}

    # Read previous manifest
    prev_manifest = {}
    manifest_path = DATA_DIR / "manifest.json"
    if manifest_path.exists():
        with open(manifest_path) as f:
            prev_manifest = json.load(f)

    # Determine what changed
    new_files = set(files_now) - set(prev_manifest)
    changed_files = {
        f for f in files_now
        if f in prev_manifest and files_now[f]["hash"] != prev_manifest[f]["hash"]
    }
    deleted_files = set(prev_manifest) - set(files_now)

    if not force and not new_files and not changed_files and not deleted_files:
        # Update heartbeat if HEAD moved (tool commits, not content changes)
        import subprocess
        try:
            head = subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=str(BRAIN_ROOT), text=True
            ).strip()
        except Exception:
            head = "unknown"
        hb_path = DATA_DIR / "heartbeat.json"
        old_head = ""
        if hb_path.exists():
            with open(hb_path) as f:
                old_head = json.load(f).get("built_at_head", "")
        if old_head != head:
            heartbeat = {
                "schema_version": 1,
                "last_run_utc": datetime.now(timezone.utc).isoformat(),
                "status": "ok",
                "built_at_head": head,
                "count": len(prev_manifest) if prev_manifest else 0,
                "files": len(files_now),
                "model": cfg["embedding"]["model"],
            }
            with open(hb_path, "w") as f:
                json.dump(heartbeat, f, indent=2)
            print("Index content unchanged. Heartbeat updated to current HEAD.")
        else:
            print("Index is current. No changes detected.")
        return

    if force:
        print(f"Full rebuild: {len(files_now)} files")
        new_files = set(files_now)
        changed_files = set()
        deleted_files = set(prev_manifest) - set(files_now)
    else:
        print(f"New: {len(new_files)}, Changed: {len(changed_files)}, "
              f"Deleted: {len(deleted_files)}")

    # Load embedder
    model = load_embedder()

    # Load existing chunks if incremental
    existing_chunks = []
    if CHUNKS_PATH.exists() and not force:
        with open(CHUNKS_PATH) as f:
            for line in f:
                line = line.strip()
                if line:
                    existing_chunks.append(json.loads(line))

    # Remove deleted file chunks
    existing_chunks = [c for c in existing_chunks
                       if c.get("file") not in deleted_files
                       and c.get("file") not in new_files
                       and c.get("file") not in changed_files]

    # Process new and changed files
    new_chunks = []
    files_to_process = sorted(new_files | changed_files)

    for rel in files_to_process:
        info = files_now[rel]
        try:
            with open(info["path"], encoding="utf-8") as f:
                text = f.read()
        except Exception as e:
            print(f"  SKIP {rel}: {e}", flush=True)
            continue

        fm, body = parse_frontmatter(text)
        if not body:
            continue

        chunks = chunk_text(body, cfg["chunking"]["max_chars"],
                            cfg["chunking"]["overlap_chars"])

        for i, chunk_text_content in enumerate(chunks):
            chunk = {
                "file": rel,
                "chunk_id": f"{rel}::{i}",
                "chunk_idx": i,
                "total_chunks": len(chunks),
                "domain": fm.get("domain", ""),
                "tags": fm.get("tags", []),
                "title": fm.get("name", ""),
                "author": fm.get("author", ""),
                "status": fm.get("status", fm.get("tier", "")),
                "text": chunk_text_content,
            }
            new_chunks.append(chunk)

    print(f"  Chunks to embed: {len(new_chunks)}", flush=True)

    # Embed new chunks
    if new_chunks:
        texts = [c["text"] for c in new_chunks]
        batch_size = cfg["embedding"]["batch_size"]
        vectors = []
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]
            vecs = model.encode(batch, normalize_embeddings=True,
                                show_progress_bar=False)
            vectors.append(vecs)
            if (i + batch_size) % 100 == 0 or i + batch_size >= len(texts):
                print(f"  Embedded {min(i + batch_size, len(texts))}/{len(texts)}",
                      flush=True)
        new_vectors = np.concatenate(vectors, axis=0).astype(np.float16)
    else:
        new_vectors = np.empty((0, cfg["embedding"]["dim"]), dtype=np.float16)

    # Combine with existing
    all_chunks = existing_chunks + new_chunks
    if existing_chunks and VECTORS_PATH.exists():
        old_vectors = np.load(VECTORS_PATH).astype(np.float16)
        all_vectors = np.concatenate([old_vectors, new_vectors], axis=0)
    else:
        all_vectors = new_vectors

    # Write output
    with open(CHUNKS_PATH, "w", encoding="utf-8") as f:
        for c in all_chunks:
            f.write(json.dumps(c, ensure_ascii=True) + "\n")

    np.save(str(VECTORS_PATH), all_vectors)

    # Write manifest
    manifest = {rel: {"hash": info["hash"]} for rel, info in files_now.items()}
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    # Write meta
    meta = {
        "format_version": 1,
        "model": cfg["embedding"]["model"],
        "dim": cfg["embedding"]["dim"],
        "count": len(all_chunks),
        "files": len(files_now),
        "built_at": datetime.now(timezone.utc).isoformat(),
        "mode": "full" if force else "incremental",
    }
    with open(META_PATH, "w") as f:
        json.dump(meta, f, indent=2)

    elapsed = time.time() - t0
    print(f"Done. {len(all_chunks)} chunks from {len(files_now)} files "
          f"in {elapsed:.1f}s", flush=True)

    # Write heartbeat
    import subprocess
    try:
        head = subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=str(BRAIN_ROOT), text=True
        ).strip()
    except Exception:
        head = "unknown"

    heartbeat = {
        "schema_version": 1,
        "last_run_utc": datetime.now(timezone.utc).isoformat(),
        "status": "ok",
        "built_at_head": head,
        "count": len(all_chunks),
        "files": len(files_now),
        "model": cfg["embedding"]["model"],
    }
    heartbeat_path = DATA_DIR / "heartbeat.json"
    with open(heartbeat_path, "w") as f:
        json.dump(heartbeat, f, indent=2)


def check_freshness():
    """Check if index is stale. Returns (ok, message)."""
    import subprocess

    heartbeat_path = SCRIPT_DIR / "heartbeat.json"
    if not heartbeat_path.exists():
        return False, "NO INDEX -- run 'python index.py --force' first"

    with open(heartbeat_path) as f:
        hb = json.load(f)

    try:
        head = subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=str(BRAIN_ROOT), text=True
        ).strip()
    except Exception:
        return True, "HEARTBEAT OK (git unavailable -- freshness unverified)"

    if hb.get("built_at_head") != head:
        return False, f"STALE -- index built at {hb.get('built_at_head','?')[:8]}, "
        f"HEAD is {head[:8]}"

    if not META_PATH.exists():
        return False, "STALE -- index data missing"

    with open(META_PATH) as f:
        meta = json.load(f)

    return True, (f"OK -- {meta['count']} chunks from {meta['files']} files, "
                  f"built {meta['built_at'][:19]}")


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="Full rebuild")
    ap.add_argument("--check", action="store_true", help="Check freshness only")
    args = ap.parse_args()

    if args.check:
        ok, msg = check_freshness()
        print(msg)
        sys.exit(0 if ok else 1)

    build_index(force=args.force)
