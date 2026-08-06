---
name: session-end
description: "Close a session: run the Schoen Loop, write daily memory, write IOR, commit workspace, push brain, logbook entry, rebuild brain-index, reflect on identity, verify files, audit gate rules."
user-invocable: false
disable-model-invocation: false
---

# Session End -- Closing Procedure

## Hard Gate (R2)

This skill is invoked by the AGENTS.md Session End instruction. Every
step MUST be confirmed. The session MUST NOT be logged as complete
with any item unconfirmed.

## Self-Check -- HARD GATE

- [ ] Schoen Loop completed: all 4 questions answered, facts not
  opinions, root causes identified, at least one surprise surfaced,
  structural change named, or confirmed none warranted (R7) (PASS / HALT)
- [ ] Schoen Loop output committed to daily memory under correct
  session heading (PASS / HALT)
- [ ] Daily memory written to `memory/<today>.md` (filename date
  derived with `date -u +%Y-%m-%d`, header time derived with
  `date -u +%H:%M`, not manually typed) (PASS / HALT)
- [ ] IOR written: all quality gates PASS (G1-G8). Every session produces one reflection. No exceptions. (PASS / HALT)
- [ ] Workspace purity verified: no stray IORs, proposals, or research
  artifacts (PASS / HALT)
- [ ] Workspace committed (local git) (PASS / HALT)
- [ ] Agentic-brain committed + pushed (unconditional: always includes
  queue.log entry; errors.log if applicable) (PASS / HALT)
- [ ] Brain-index rebuilt if brain files were pushed (PASS / HALT)
- [ ] Logbook entry: protocol.md read before writing; remote pulled before ENT count; append-only; ASCII (PASS / HALT)
- [ ] Logbook entry format: body uses multiple short lines per the step 6 example. No single-line packed entries. Blank line separating entries. (PASS / HALT)
- [ ] Identity decision: evolution questions re-read from IDENTITY.md
  (from file text, not from memory), trigger evaluated (PASS / HALT)
- [ ] IDENTITY.md + archive updated if version warranted; if not, skipped
  after explicit evaluation (PASS / HALT)
- [ ] File integrity: all files ASCII + validate-ids PASS (PASS / HALT)
- [ ] Gate Rules self-check: R15 audit passed (rules audited for
  staleness, active failure classes, no violations unaddressed) (PASS / HALT)

## Steps

### 1. Run the Schoen Loop

Every substantive session MUST complete the Schoen Loop before writing
daily memory. The Schoen Loop has 4 questions:

#### 1.1 What Happened?

State the facts. Chronological list of concrete actions and results.
No interpretation, opinions, or justifications. Facts only.

PASS: A sequence of events. HALT: If this contains opinions.

#### 1.2 What Worked / What Did Not?

For each item in 1.1: did it succeed or fail? Root cause for every
failure. Apply the R5 3-question test:
- Same CLASS of failure? (not just this instance)
- STRUCTURAL fix? (not manual "I'll remember next time")
- Would have caught the ORIGINAL? (not a band-aid on the symptom)

Surface explanations are not acceptable. "The git push failed because
the branch was behind" is surface. "The git push failed because the
pre-push pull step was skipped" is root cause.

#### 1.3 What Surprised Me?

The signal. What did you not expect? What revealed a gap in your model
of the world? Surprise is data, not shame. A session with zero
surprises means you were not paying attention.

#### 1.4 What Structural Gate Did I Add?

R7: A structural gate is required only when a failure class, scar, or
insight emerged this session. The gate must:
- Be a new or strengthened rule, not a one-time action
- Prevent the CLASS of failure, not just this instance
- Be written into a bootstrap file, template, or skill so it fires
  automatically next time

If no new gate was warranted, record 'no gate warranted' explicitly --
do not fabricate a gate for a clean session. The review is mandatory;
the gate is scar-driven.

### 2. Write Daily Memory

**CRITICAL: Derive date AND time live. Do NOT type manually.** Run:

```bash
date -u +%Y-%m-%d
date -u +%H:%M
```

Use the EXACT output for the filename (date) and header (time).

- The FIRST line of the file MUST be the session heading:
  `## YYYY-MM-DD (HH:MM UTC) -- <short-title>`.
  Do NOT wrap the file in a `# YYYY-MM-DD -- Session Log` level-1
  heading. The `##` entries ARE the file. No wrapper, no table of
  contents, no introductory line. Just session headings directly.
- The Schoen Loop output (all 4 questions) MUST be included verbatim
  under this heading in (A)-(D) + (E) read-proof format only:
  (A) What happened? (B) What worked / what did not?
  (C) What surprised me? (D) What structural gate did I add?
  (E) read-proof line.
- No System changes, What broke, What comes next, or other narrative
  sections -- the Schoen Loop IS the memory.
- If the file already exists from an earlier session today, append a
  new entry using the SAME header format (`##`, not `###`). Derive
  date and time with the same `date -u` commands. Always include the
  `UTC` suffix.
- If another agent wrote to the same day's memory file (e.g., a parallel
  session-end), your `write_file` call will overwrite their entry.
  Before writing, read the file. If entries from earlier today exist,
  prepend or append yours WITHOUT overwriting. Check git log to
  recover any entry you accidentally clobbered.

### 3. Write an IOR

Every session produces one reflection. The Schoen Loop surfaced a
durable insight -- capture it. Follow the `write-reflection` skill.
No exceptions, no skips, no "not warranted" escape hatch.

### 4. Commit Workspace

Verify workspace purity first -- only authorized Layout items present.
Remove any stray research artifacts (IORs, proposals -- belong in brain).

```bash
cd "/c/AI Stuff/Hermes Agent/profiles/link/workspace-link"
git add -A
git diff --cached --stat
git commit -m "<message>"
```

### 5. Commit and Push Agentic-Brain

If brain files were written, clone and push.

```bash
cd /tmp && rm -rf brain-sessend && git clone --depth 1 \
  "https://${GITHUB_TOKEN}@github.com/Suggi-Workstation/agentic-brain.git" brain-sessend
cd brain-sessend
git add -A && git commit -m "<message>" && git pull --rebase origin main && git push origin main
```

### 5b. Rebuild Brain-Index

If step 5 pushed brain files, invoke `brain-index` skill to rebuild.
Defense-in-depth: session-end rebuild + preflight verify.

### 6. Write Logbook Entry

Every session writes at least one queue.log entry. Read protocol first.

**CRITICAL -- Pull before counting.** The remote may have new entries
from another agent (or a parallel session-end). Run:

```bash
cd /tmp/brain-sessend && git pull origin main
```

Derive ENT-ID from the LAST entry after the pull. Never derive the
counter from stale local state -- that produces duplicate ENT-IDs.

**Entry body format -- MUST use multiple short lines.** Do NOT pack the
entire session summary onto one line. Break at logical boundaries:
one line per major workstream, file change, or artifact written.
Separate entries with a blank line for readability. The archiving
system counts lines, not bytes -- single-line entries defeat
line-based archiving.

Example format:

```
## [ENT-NNN] | YYYY-MM-DD HH:MM UTC | Link | general | ref: path/to/file.md | see: artifact-id
Session: <one-line title>.
Workstreams:
- <first major change or file written>.
- <second major change>.
Reflection: <id-or-slug>. Daily memory: YYYY-MM-DD.md.
```

Append only. ASCII-only. If the ENT counter is ambiguous, grep
`^## \[ENT-` and count matches rather than reading entry text.

### 7. Reflect on Identity

Re-read IDENTITY.md Evolution Guidelines from file text, not memory.
Answer for each question: "Could I do this BEFORE this session?"
If ANY answer is NO, write a new version entry.

Archive-then-replace -- the archive gets the OLD section ONLY, not the
whole file:

1. **Extract** the current live version section from IDENTITY.md -- from
   `### vN.N --` through the end of the 5th question's answer. Write
   ONLY this section to `identity/vN.N-slug.md`. Do NOT copy the
   frontmatter, Purpose section, Evolution Guidelines section, or footer
   -- just the version heading and its 5 question entries.
2. **Write** the new version entry in IDENTITY.md above the old one.
3. **Remove** the old version section from IDENTITY.md -- the file must
   contain exactly ONE version under `## Evolution`.
4. **Update** frontmatter `version:` field.
5. **Verify:** `identity/vN.N-slug.md` starts with `### vN.N --` (not
   YAML frontmatter). IDENTITY.md has exactly one `### v` heading under
   the Evolution section.

### 8. Verify File Integrity

ASCII guard + validate-ids on all changed files. HALT on failure.

### 9. Gate Rules Self-Check

Read the Gate Rules -- HARD GATE section in AGENTS.md. Run the
Self-Check. Confirm all items PASS:
1. Each rule addresses an active failure class (no stale rules)
2. No rule violated in recent sessions without structural fix
3. Every new failure class maps to a rule or proposal
4. All HARD GATE sections have verification checklists
5. No rule contradicts another rule

Flag any rule not triggered in the last 10 sessions for evaluation.

## Pitfalls

- **DO NOT manually rewrite this skill when syncing from another agent.**
  Use raw `cp` from the canonical source. Manual rewrites introduce
  token-variable drift, repo URL errors, step-count mismatches, missing
  enforcement language, and formatting sloppiness. See
  `references/cross-agent-skill-copy.md` for the complete checklist.
- **Git author config missing in /tmp clones.** Bare git clones
  (like /tmp/brain-sessend) have no user.name or user.email configured.
  All git commands in these clones MUST use `-c user.name=\"<name>\"` and
  `-c user.email=\"<email>\"`. A bare `git commit` or `git rebase
  --continue` without these flags fails with \"please tell me who you
  are.\" This applies to both the initial commit in step 5 and any
  rebase or revert operations. Scar (2026-07-24): git revert and
  git rebase both failed in /tmp/brain-pf due to missing author config.
- **DO NOT type date or time values manually.** Always derive with
  `date -u +%Y-%m-%d` (filename) and `date -u +%H:%M` (header time).
  The command output IS the value. Manual typing caused wrong-date-file
  (July 21 -> July 20) and wrong timestamp (12:40 local vs 10:17 UTC).
- **Memory overwrite recovery.** The `write_file` tool overwrites the
  entire file, not appends. If the daily memory file already has
  entries from earlier sessions today, a direct `write_file` call will
  clobber them. Before writing, read the file with `read_file`. If
  entries exist, prepend or append WITHOUT overwriting. If you DO
  accidentally clobber: recover from git with `git show
  HEAD:memory/<file> > /tmp/prior.md`, combine (`cat /tmp/prior.md
  memory/<file> > /tmp/combined.md`), and restore. Scar (2026-07-22):
  session-end daily memory overwrote 2 prior entries; recovered via
  git show. Verify the restored file has all entries before committing.
- **DO NOT type IOR/Schoen-Loop/Reflection IDs manually.** Generate
  with `date -u +'%Y%m%dT%H%M%SZ'`. Paste the exact output. Never
  manually typed, never rounded, never estimated.
- **DO NOT clean up, delete, or reset test artifacts before the user
  inspects them.** The user asked you to create something for their
  inspection -- do not pre-verify the result and then delete it.
  If you ran a test locally, show the output, but do not revert the
  file to a pre-test state. The user wants to see the artifact, not
  your confirmation that it worked. This is a first-class signal:
  \"Don't assume. Let me verify\" means you overstepped.
- **DO NOT batch-apply changes without user review.** When the user
  asks for a format or structural change, apply it to ONE file first,
  push, and wait for confirmation before applying to the rest.
  \"Do this ONLY for one first\" means the user wants to verify the
  output before scaling. Ignoring this wastes both your time (wrong
  approach applied to 28 files) and the user's trust. This applies
  universally -- anchors, memory files, skill updates, anything
  where the user says \"first one, then the rest.\"

- **MSYS /tmp is NOT C:\tmp on Windows git-bash.** Resolve the real
  path before writing files into a /tmp clone: `cd /tmp && pwd -W`
  (typically C:\Users\<user>\AppData\Local\Temp). NEVER construct
  /tmp paths by climbing relative paths from the workspace
  (`workspace/../../../../tmp` lands in C:\tmp, a DIFFERENT directory
  than git-bash /tmp). Scar (2026-08-01): the session-end reflection
  was written to C:\tmp\brain-sessend while the clone sat under
  AppData\Local\Temp -- the commit shipped only errors.log until the
  file was moved and re-pushed.
- **A failing pre-check short-circuits the rest of an `&&` chain.**
  `ls file && cat >> log` silently SKIPS the append when ls fails.
  Scar (2026-08-01): a failed `ls` on the misplaced reflection skipped
  the queue.log append entirely; the pre-commit `git diff --cached
  --stat` inspection caught the missing files before push. Always
  verify the diff --cached stat lists EVERY expected file (memory,
  identity, reflection, BOTH logbook files) before committing.

## Platform Notes

Link runs on Hermes Agent (Windows 10). Unlike Ava (OpenClaw on VPS),
Link does NOT need memory reindex (Hermes auto-indexes via SQLite).
Everything else (Schoen Loop, Gate Rules, brain-index rebuild, file
integrity) applies to both agents uniformly.

## Related

- AGENTS.md Session End section -- the gate instruction that triggers this skill
- `loop-feynman` skill -- output quality (run before substantive work)
- `write-reflection` skill -- IOR format and quality gates
- `brain-index` skill -- invoked by step 5b
- `logbook` skill -- logbook writing procedure
- `references/cross-agent-skill-copy.md` -- cross-agent skill copy checklist