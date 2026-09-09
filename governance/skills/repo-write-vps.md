---
name: repo-write-vps
description: "Use when writing to watcher-managed VPS repositories."
user-invocable: true
disable-model-invocation: false
---

# Repo Write (VPS)

## When to Invoke

Use for writing, committing, and verifying publication in an existing
watcher-managed VPS repository. If the task requires a dedicated publisher,
follow that publication procedure instead.

## Procedure

1. Select the requested repository's existing VPS clone. Run commands as
   its owner, directly or through your approved connection. Replace all
   placeholders before execution.

   ```bash
   REPO="<absolute target repository path>"
   cd "$REPO"
   git rev-parse --show-toplevel
   git branch --show-current
   crontab -l
   ```

   Confirm the target path, main branch, and matching watcher entry.
   Verify that watcher publishes this clone to origin/main. HALT if the
   target or publication owner is unconfirmed. Do not create another clone.
2. Read the target files and repository instructions. Make only authorized
   changes. Follow its artifact format; preserve existing document authorship.
3. Verify ASCII and required repository checks. Match permissions to sibling files.
4. Stage only your paths. Inspect the staged diff; HALT on unrelated work.

   ```bash
   git add -- <artifact-paths>
   git diff --cached --stat
   ```

5. Commit with your own Git name and email. Do not change repository or
   global Git settings.

   ```bash
   AGENT_NAME="<your Git name>"
   AGENT_EMAIL="<your Git email>"
   env GIT_AUTHOR_NAME="$AGENT_NAME" GIT_AUTHOR_EMAIL="$AGENT_EMAIL" \
       GIT_COMMITTER_NAME="$AGENT_NAME" GIT_COMMITTER_EMAIL="$AGENT_EMAIL" \
       git commit -m "<type>: <message>"
   ```

6. Use the returned commit hash to verify both identities. HALT on a
   mismatch; do not rewrite history.

   ```bash
   git show -s --format='Author: %an <%ae>%nCommitter: %cn <%ce>' <commit-sha>
   ```

7. Let the existing watcher push naturally. Do not push manually or force
   a watcher run. Verify publication; if pending, wait for the next tick
   and check again.

   ```bash
   git fetch origin
   git merge-base --is-ancestor <commit-sha> origin/main
   ```

8. Remove only your temporary files after successful verification.

## Verification -- PASS / HALT

- [ ] Target clone, main branch, and its origin/main watcher confirmed.
- [ ] Authorized paths only; ASCII, repository checks, and permissions pass.
- [ ] Staged diff and exact commit contain only the intended changes.
- [ ] Commit author and committer match your name/email; Git settings unchanged.
- [ ] Exact commit is on origin/main after the watcher's natural push.
- [ ] Task-owned temporary files cleaned; unrelated files untouched.

PASS requires every applicable check. Otherwise HALT and report the failed check.
