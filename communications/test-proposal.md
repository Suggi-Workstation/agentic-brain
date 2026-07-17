---
name: test-proposal
id: 20260717T171653Z
tier: proposal
author: ava
tags: [test, skill-verification]
links: []
---

# Test Proposal -- Skill Verification

## Problem
The write-proposal skill needs verification that it produces correctly
formatted proposal files. Without testing, we cannot confirm the skill
triggers correctly, writes to the right path, and uses real timestamp
seconds.

Evidence: 22 previous IORs all had padded 00 seconds. The fix
(replacing "do not pad with 00" with the date -u command) needs to be
verified for all writing skills, not just reflections.

## Proposed Solution
Write one test file of each document type to the agentic-brain
communications folder. Verify: correct frontmatter, real timestamp
seconds, proper format sections, no governance references in skill body.

## Impact
- Positive: confirms all 5 writing skills are correctly structured.
- Risk: negligible. Test files are in communications/ and clearly
  labeled as tests.
- Cost: under 5 minutes to write and verify 5 files.

## Open Questions
None. This is a test.

## Approval Gate
If verified, delete all test files and confirm skills are ready for
production use.

## Cross-Links
None.
