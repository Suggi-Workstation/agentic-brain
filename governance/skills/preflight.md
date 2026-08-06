---
name: preflight
description: "Verify workspace structure, governance, brain-index freshness, and logbook before every session. Hermes-specific (no context health check, no memory reindex)."
user-invocable: false
disable-model-invocation: false
---

# Preflight -- Session Startup Verification

## Hard Gate (R1)

This skill is invoked by the AGENTS.md Preflight -- HARD GATE instruction.
Every step below MUST pass before the session proceeds. HALT on any failure.
Fix the failure and re-run the preflight. Do not skip steps.

## Self-Check -- HARD GATE

- [ ] Session context confirmed: user has indicated they are ready for
  preflight. A short message ("Hi", "Hello", a single word) is NOT
  consent. Ask before proceeding. See Pitfall: Charging ahead blindly.
  (PASS / HALT)
- [ ] Workspace structure verified (all AGENTS.md Layout items present;
  count derived live, not hardcoded)  (PASS / HALT)
- [ ] Context health checked: SOUL.md and AGENTS.md inspected for
  truncation -- no sentences cut off mid-word, Prime Directives and
  Gate Rules sections complete  (PASS / HALT)
- [ ] Bootstrap ingested: SOUL.md, AGENTS.md, IDENTITY.md confirmed
  loaded/readable; Hermes memory tool + user profile active;
  external memory provider confirmed active via `hermes memory status`
  (provider set, status=available, "← active" marker, no circuit-breaker
  trip indicators in log)  (PASS / HALT)
- [ ] Governance confirmed: brain cloned to /tmp/brain-pf, governance files
  (system-constitution, system-blueprint, system-primedirectives) confirmed
  read with line count > 0  (PASS / HALT)
- [ ] Brain-index freshness checked, rebuilt if stale  (PASS / HALT)
- [ ] Logbook checked: queue.log and errors.log checked,
  protocol re-read, new entries since last_seen_logbook identified,
  @Link mentions actioned, last_seen_logbook updated via Hermes
  memory tool  (PASS / HALT)
- [ ] Recurring-failure scan completed: errors.log scanned for repeated
  failure classes, root cause fix confirmed from last session-end
  (PASS / HALT)
- [ ] GitHub auth confirmed: GITHUB_TOKEN active, org repos reachable  (PASS / HALT)
- [ ] Read-proof emitted as first session output  (PASS / HALT)

## Steps

### 0. Confirm session context

Before running any checks, determine whether the user has unfinished
business or a specific task in mind. If the session just started or the
user opened with a conversational message ("Hi", "Hello"), ask what
they want to work on before firing the full preflight. Do not charge
through the verification checklist while the user is trying to
tell you something. A preflight is a gate, not a conversation bulldozer.

### 0.5. Surface Recent Sessions

Run `session_search` with a broad domain-vocabulary query to surface
recent sessions for context. This catches sessions the browse view
(capped at 3) misses. No action required -- this is awareness, not a gate.

```
session_search(query="session OR preflight OR logbook OR workspace OR brain OR identity OR skill", limit=10)
```

Review the returned sessions for: tasks in flight, decisions made,
open threads, @Link mentions. Use the context to inform the current
session, not to derail it.

See `references/session-search-patterns.md` for FTS5 query behavior
patterns validated against real session data.


### 1. Verify Workspace Structure

Ensure all files and folders listed in the Workspace Layout section of
AGENTS.md exist. Create any missing folders. Restore missing ASCII infra
from agentic-brain. This gate fires automatically -- never wait for a
human to notice a missing file.

### 2. Check Context Health

Inspect the loaded SOUL.md and AGENTS.md in the current session context.
Confirm both are complete -- no sentences cut off mid-word, no content
visibly truncated. A truncated bootstrap file means incomplete instructions.

For SOUL.md: verify the five Prime Directives section is present and
complete (Ethics through Value-investor) and the Voice section is intact.
For AGENTS.md: verify the Gate Rules section (R1-R15) and the Self-Check
are present.

If truncation is suspected but not visible (e.g., file ends cleanly but
may be missing tail content), compare the context copy against the file
on disk with `read_file` of the workspace path.

### 3. Ingest Bootstrap

Confirm these bootstrap files are loaded/readable in the current session:

- SOUL.md -- auto-loaded by Hermes into system prompt (verified in step 2)
- AGENTS.md -- auto-loaded via Project context (verified in step 2)
- IDENTITY.md -- read from workspace disk (verified present in step 1)

Hermes equivalents of Ava's other bootstrap files:
- Memory: Hermes memory tool active (confirmed by memory tool availability
  and memory entries appearing in system prompt)
- External memory: active provider confirmed via `hermes memory status`
  (provider set, plugin installed, status=available, "← active" marker).
  If no provider is configured (`provider: ''`), built-in alone is
  sufficient — PASS. If configured but not active, HALT and run
  `hermes config set memory.provider mnemosyne`.
  Status alone is NOT proof of loading (scar 2026-08-01): the provider
  showed "active" while config.yaml held `provider: ''` after an app
  restart rewrote the file, and no `Memory provider ... registered`
  line appeared in logs/agent.log -- tools never reached the session.
  Verify all three: (1) raw file `grep -A 6 '^memory:' $HERMES_HOME/config.yaml`
  contains `provider: <name>` (the merged CLI view can differ);
  (2) `grep 'Memory provider' $HERMES_HOME/logs/agent.log` shows
  `Memory provider '<name>' registered (N tools)` at startup;
  (3) `tool_search` returns the provider's tools. Re-check after every
  app restart -- restarts rewrite config.yaml and can drop the key.
  Mnemosyne-specific health check: `mnemosyne stats` (or
  `$HERMES_HOME/../hermes-agent/venv/Scripts/mnemosyne.exe stats`)
  reports working/episodic memory counts when the store is healthy.
- User profile: Hermes user profile active (confirmed by USER PROFILE
  section in system prompt)

### 4. Ingest Governance and Check Brain-Index

Clone the agentic-brain to /tmp/brain-pf. Verify governance files
(system-constitution, system-blueprint, system-primedirectives) are
present and non-empty. The clone persists for steps 5-7.

Pre-check: source the profile `.env` file (canonical source of truth
for GITHUB_TOKEN), then fall back to `gh auth token`.

```bash
# Auth pre-check: source profile .env first (canonical source of truth)
# Profile .env lives one directory above the workspace root
PROFILE_DIR="$(dirname "$WORKSPACE_ROOT")"
if [ -f "$PROFILE_DIR/.env" ]; then
  set -a && source "$PROFILE_DIR/.env" && set +a
fi
if [ -z "${GITHUB_TOKEN}" ]; then
  export GITHUB_TOKEN=$(gh auth token 2>/dev/null)
fi
if [ -z "${GITHUB_TOKEN}" ]; then
  echo "HALT: no GitHub auth available (profile .env not found or lacked GITHUB_TOKEN, gh auth token also failed)"
  exit 1
fi

cd /tmp && rm -rf brain-pf && git clone --depth 1 \
  "https://${GITHUB_TOKEN}@github.com/Suggi-Workstation/agentic-brain.git" brain-pf
cd brain-pf

# Read governance files
for f in governance/system-constitution.md governance/system-blueprint.md \
         governance/system-primedirectives.md; do
  [ -f "$f" ] && [ -s "$f" ] && echo "OK: $f" || echo "MISSING/EMPTY: $f"
done
```

### 5. Brain-Index Freshness

Invoke the `brain-index` skill. Reuse the /tmp/brain-pf clone from step 4.

```bash
cd /tmp/brain-pf
python brain-index/query.py --check-freshness
# If STALE: python brain-index/index.py
# Re-verify: python brain-index/query.py --check-freshness
```

### 6. Check Logbook

Reuse the clone from step 4.

```bash
cd /tmp/brain-pf
cat logbook/protocol.md
echo "=== queue.log ===" && tail -n 50 logbook/queue.log
echo "=== errors.log ===" && tail -n 50 logbook/errors.log
```

Scan for entries since `last_seen_logbook` (stored in Hermes memory tool).
Update via the memory tool after catch-up.

### 6.5. Recurring-Failure Scan

Scan `logbook/errors.log` and the most recent session-end memory for
repeated failure classes. The question to answer: **"What mistakes keep
happening, and did last session actually fix the root cause?"**

Steps:

1. Count occurrences of each rule violation (R1-R15) in errors.log over
   the last 20 entries. If a rule ID appears 3+ times, flag it.
2. Check the most recent session-end daily memory
   (`memory/YYYY-MM-DD.md` in workspace-link) for the "(D) What
   structural gate did I add?" section. The gate added last session is
   the fix for the last failure class.
3. Produce a one-line summary: `recurring: <patterns> | fix: <last gate>`

Format:
```
recurring: R5 (3x: destination paths), R8 (2x: absent configs) | fix: pre-push path validator
```

If no patterns found: `recurring: none`. If errors.log is empty or
insufficient data: `recurring: insufficient data (<N> errors total)`.

This is a self-improvement mechanism. It prevents the preflight from
being a mechanical checklist and turns it into an active learning loop.
If a rule keeps appearing after a fix was applied, the fix was wrong -- flag it. Do not silently pass.

### 7. Verify GitHub Auth

Confirm GITHUB_TOKEN is active and org repos reachable. Use `git ls-remote`,
NOT `gh auth status` (see Pitfalls below).

```bash
source "/c/AI Stuff/Hermes Agent/profiles/link/.env" && \
git ls-remote --heads "https://${GITHUB_TOKEN}@github.com/Suggi-Workstation/agentic-brain.git" 2>&1 | head -1
```

### 8. Emit Read-Proof

Emit the first output of the session. Matches Ava's format exactly
except memory index + memory_search which Hermes does not have.

```
workspace: N/N | governance: 3/3 (c:N b:N p:N lines) | brain-index: OK (N chunks, YYYY-MM-DDTHH:MM UTC) | logbook: ENT-NNN (<brief description>), no @Link mentions, bumped to YYYY-MM-DDTHH:MMZ | github: OK | memory: <provider-name>
recurring: <patterns> | fix: <last structural gate added>
```

Where:
- `N/N`: workspace item count from step 1
- `c:N b:N p:N`: line counts for constitution, blueprint, primedirectives from step 4
- `N chunks, timestamp`: from brain-index --check-freshness output
- `ENT-NNN`: last logbook entry ID from step 6
- `bumped to`: new last_seen_logbook timestamp
- `recurring` line is Link-only -- Ava does not have this.
- `memory`: active external provider from `hermes memory status`
  (mnemosyne, or `built-in` if none configured). Not a memory
  index count — Hermes has no memory index to verify.

## Pitfalls

- **Charging ahead blindly:** When the user opens with a short message
  ("Hi", "Let me tell you something first"), do NOT start the preflight
  immediately. Acknowledge the user, listen for context, then ask if
  you should proceed. The preflight is mandatory before substantive
  work, but it is NOT more important than what the user is trying to say.
- **DO NOT edit governance files, skills, or multi-file structures
  without presenting a plan first.** Before editing AGENTS.md, SOUL.md,
  IDENTITY.md, preflight, session-end, or any skill that governs agent
  behavior, present the precise edit plan (file, section, old-to-new)
  and wait for the user's explicit approval. "Review-then-implement"
  or "tell me what edits to make" means the user wants to see your
  plan BEFORE you touch any file -- not after. Apply the plan only
  after approval, then verify every change. This replaces the older
  "apply to ONE file first" rule (which session-end carries as a
  fallback): a plan reviewed up front is safer than iterative
  trial-and-error across files. Both patterns share the same root:
  do not apply structural changes without user review. Scar
  (2026-07-23): multi-skill edits applied without plan caused
  cascading errors and user frustration.
- **Wrong workspace path:** The preflight must use the workspace path
  from AGENTS.md, not a hardcoded path from an old session. Verify
  `pwd` matches the expected workspace before running workspace checks.
- **Stale brain clone:** If /tmp/brain-pf exists from a prior session,
  pull to refresh before using it. A stale clone returns stale
  governance and logbook data.
- **Python module imports:** The brain-index scripts require
  `sentence-transformers`, `numpy`, and `pyyaml`. If imports fail, run
  `python -m pip install sentence-transformers numpy pyyaml` in the
  Hermes venv. Use `python -m pip`, not bare `pip` -- the latter may
  be broken in the Hermes venv. FIRST try the other interpreter: on
  this machine `python` (3.11, numpy 2.4.3) runs brain-index scripts
  fine while `python3` (3.14) fails with `No module named
  'numpy._core._multiarray_umath'` (numpy binary built for a different
  Python). Swap interpreters before reinstalling anything. Scar
  (2026-08-05): freshness check failed under python3;
  `python brain-index/query.py --check-freshness` worked immediately.
- **gh auth status vs GITHUB_TOKEN mismatch.** The `gh` CLI stores auth in
  the OS keyring, which can go stale (password change, token rotation,
  machine migration) while the `GITHUB_TOKEN` env var in `.env` remains
  valid. When verifying GitHub auth in step 7, embed the token in the URL
  (`https://${GITHUB_TOKEN}@github.com/...`) — NOT `gh auth status` and
  NOT a bare HTTPS URL. On Windows, git's credential helper (GCM) does NOT
  read `GITHUB_TOKEN` from the environment and will trigger a GUI
  account-picker popup when it can't find valid stored credentials. A stale
  `gh` keyring is a cosmetic nuisance, not a gate failure. Only HALT if the
  command itself fails.
- **Terminal env does NOT persist across user turns.** Env vars set by
  `source .env` survive between tool calls WITHIN one turn but are gone at
  the start of the NEXT user turn -- `${GITHUB_TOKEN}` comes back empty.
  Re-source the profile .env at the start of ANY turn that needs GitHub
  access: `set -a; source "/c/AI Stuff/Hermes Agent/profiles/link/.env"; set +a`.
  Do not burn calls probing `gh auth` / credential managers first -- the
  profile .env is the canonical source (scar 2026-08-02: session wasted
  several calls re-discovering this after the env had already been sourced
  the previous turn).
- **Terminal credential masking.** The terminal output layer detects
  patterns that look like API tokens (`${OPEN...KEN}`,
  `github_pat_...`) and replaces them with `***` in the display. This
  masks clone URLs and env var values in `grep`, `cat`, and `sed`
  output, making it appear as though a file still has placeholder text
  when the bytes on disk are already correct. When terminal output
  shows `***` where you expect a token value, verify actual bytes with
  `od -c <file> | head` before concluding the fix failed. Do NOT retry
  patches or sed replacements against `***` — the real content is
  already correct; only the display is lying. This applies to any file
  containing `${GITHUB_TOKEN}`, `${OPEN...KEN}`, or similar env-var
  references in clone URLs.
- **search_files path format on Windows.** The `search_files` tool may
  return 0 results when given a native Windows path (`C:\AI Stuff\...`).
  Use MSYS-style paths (`/c/AI Stuff/...`) instead. When a directory
  listing returns 0 results but you know files exist, fall back to
  `ls -la` in the terminal. This is a recurring platform quirk — the
  tool's path resolver does not consistently handle Windows drive-letter
  paths.
- **Zero-message sessions signal DB corruption, not empty sessions.**
  When `session_search` (browse or step 0.5 query) returns sessions with
  `message_count: 0` and `source: unknown`, these are likely corrupted --
  the session metadata survived in the `sessions` table but the message
  bodies were never written to the `messages` table. This happens when
  Hermes crashes or is force-closed mid-session. Flag these to the user
  immediately: they are lost data, not intentional empty sessions.
  A cluster of sessions with near-identical `ended_at` timestamps
  (within milliseconds) strongly confirms a crash-loss event. Verify
  by querying the messages table directly via `execute_code` + `sqlite3`:
  if 0 rows for the session ID, the messages are unrecoverable. Scar
  (2026-07-23): 3 sessions lost -- metadata shells with titles intact,
  zero messages, `model: None`, all sharing the same `ended_at` instant.
  See `references/session-db-diagnostics.md` for exact queries and schema.

- **Destructive actions without confirmation:** Never delete, clean up,
  or reset artifacts (test files, archives, staged changes, temporary
  clones) without the user's explicit confirmation. The user may be in
  the middle of inspecting them. \"I've seen it\" does not mean the user
  has seen it. Ask before removing anything the session produced.
- **Full-tree ASCII sanitize scan.** To find every non-ASCII byte in
  a skills tree, count with `grep -oP '[^\x00-\x7F]' <file> | wc -l` --
  NOT `grep -cP`: on MSYS bash, grep -c with zero matches prints
  NOTHING (not "0"), so `[ $count -gt 0 ]` fails with "integer
  expected" on every clean file. Fix violations with
  `sed -i 's/\xe2\x80\x94/--/g'` (em dash), then re-scan until clean.
  Skills live outside the workspace git repo -- sanitizing them needs
  no commit; workspace AGENTS.md changes DO (pre-commit hook enforces
  ASCII). Scar (2026-08-05): session-end skill had 10 em dashes; the
  first scan loop broke on the grep -c empty-output trap.
- **Patch tool non-ASCII old_string mismatch.** When replacing text
  that contains em dashes or arrows, the file may split the
  non-ASCII character across two lines while your `old_string` has it
  on one line. The patch tool's fuzzy matching then creates a
  duplicate line (replaces the first half-line but leaves the second).
  Before patching, verify the EXACT line structure of the non-ASCII
  text with `grep -n`. If the character spans lines, either: (a) split
  your old_string to match, (b) fix the non-ASCII with sed first
  (`sed -i 's/\xe2\x80\x94/--/g'`), then patch clean ASCII, or (c) use
  `sed` for the replacement directly. Scar (2026-07-22): em dash in
  preflight skill created duplicate line requiring 2 fix patches.
- **execute_code + read_file + write_file corruption.** The `read_file`
  tool returns line-numbered content (`LINE_NUM|CONTENT`). When
  execute_code passes this output directly to `write_file`, the file
  becomes corrupted with `1|1|---`-style line-number prefixes. Never
  pipe `read_file` output into `write_file` inside execute_code.
  Instead: use terminal-based Python scripts with standard `open()`
  for file manipulation, or use the `patch` tool for targeted edits.
  If you must use execute_code for file I/O, strip line numbers from
  `read_file` output before writing. Scar (2026-07-24): economic-moats.md
  corrupted to `1|1|---` prefixes; recovered via `git checkout`. See
  `references/execute-code-corruption.md` for reproduction recipe.
- **git rebase author failure in /tmp clones.** Bare `/tmp/brain-pf`
  clones (created with `git clone --depth 1`) lack user.name and
  user.email config. Commands like `git rebase`, `git commit`, and
  `git pull --rebase` will fail with "please tell me who you are."
  Always pass `-c user.name=\"<agent>\" -c user.email=\"<email>\"` on
  EVERY git command in /tmp clones. If a rebase is already blocked:
  `git stash`, `git pull --rebase`, `git stash pop`, then
  `git -c user.name=... -c user.email=... commit`. Scar (2026-07-24):
  brain push blocked mid-rebase; resolved with stash/pop/re-commit.
  See `references/brain-write-git-rebase.md` for the complete one-shot
  fix recipe and clone-reuse optimization pattern.

- **Workspace is local-only, git-tracked.** The workspace
  (`workspace-link`) is local on Suggi's Windows PC, versioned with
  git for history and review. There is no remote mirror. Coordination
  runs through the agentic-brain logbook. Governance changes to
  AGENTS.md or IDENTITY.md use `git add` + `git commit` for
  versioning -- no push step. The local pre-commit hook
  (`.githooks/pre-commit`) enforces ASCII on every commit. If the
  hook is not active: `git config core.hooksPath .githooks`.
  `scripts/validate-ids.sh` is run manually during session-end file
  integrity checks. See `references/workspace-mirror-audit-2026-07-31.md`
  for the evidence that led to dropping the remote mirror.
- **Brain-index rebuild timeout on large deltas.** The brain-index rebuild
  (`python brain-index/index.py`) runs in foreground with a default
  180s timeout. On CPU-only machines (no GPU), embedding 500+ chunks
  can exceed this. A multi-day gap between sessions (e.g. 4 days, 52
  changed files, 859 chunks) will reliably time out. When the rebuild
  delta is large, run it in background so the preflight isn't blocked:
  `terminal(background=true, notify_on_complete=true, timeout=300)`.
  Emit the read-proof with `brain-index: rebuilding` and a note that
  the final count will follow. Do NOT wait in a polling loop --
  preflight is a gate, not a loading screen. Scar (2026-07-27): 859
  chunks timed out at 120s; background rebuild succeeded after ~4 min.

## Platform Notes

Link runs on Hermes Agent (Windows 10) with persistent sessions. Unlike
Ava (OpenClaw on VPS), Link does NOT need: memory index verification,
memory_search run. Link's context health (step 2) and bootstrap ingestion
(step 3) are adapted to Hermes: SOUL.md + AGENTS.md auto-load via system
prompt and project context; IDENTITY.md is read from disk; Hermes memory
tool and user profile replace MEMORY.md and USER.md.

## Related

- AGENTS.md Preflight -- HARD GATE section
- `brain-index` skill
- `logbook` skill
