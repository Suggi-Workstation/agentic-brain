# Research Pipeline -- How Artifacts Flow Through the Agentic-Brain

This folder holds the fleet's research artifacts. Every artifact moves
through one pipeline, regardless of which subfolder it lives in. This
README is the map; the templates in `governance/` are the format law;
the write-x skills are the procedures.

## The Pipeline

    proposal (idea, needs approval)
        |
        v
    report (facts gathered, methodology + findings)
        |
        v
    evaluation (independent scrutiny by a different agent)
        |
        +--> pass  -->  insight (permanent, falsifiable knowledge)
        |
        +--> fail  -->  back to proposal or report (revise, resubmit)

Not every artifact rides the whole chain. A reflection can trigger a
proposal directly; an insight can be promoted from evaluations alone.
The chain is the default path, not a straitjacket.

## The Folders

| Folder | Holds | Written with |
|:--|:--|:--|
| `proposals/` | ideas asking for approval before work happens | `write-proposal` |
| `reports/` | structured research findings awaiting evaluation | `write-report` |
| `evaluations/` | independent verdicts on proposals and reports | `write-evaluation` |
| `insights/` | permanent distilled knowledge that passed evaluation | `write-insight` |

## Status Fields

Every artifact carries a `status:` frontmatter field kept current as
the pipeline moves:

| Tier | Values |
|:--|:--|
| proposal | `open` -> `approved` -> `implemented`, or `rejected`, or `superseded by <id>` |
| report | `draft` -> `evaluated` -> `final` |
| evaluation | (none -- the verdict IS the status) |
| insight | `active`, or `superseded by <id>` |

Supersede references always cite the artifact `id:` (never the
filename slug) -- ids are permanent, slugs are not.

Only two events ever move a proposal's `status:`: Suggi's decision
(to `approved` or `rejected`) and the approved work landing (to
`implemented`). Reports, evaluations, and insights investigate or
distill -- they never approve anything.

Files written before this convention existed have no `status:` field;
treat them as historical records and infer state from their content.

## The One Rule That Keeps the Pipeline Honest

When your new artifact changes the state of an older one -- approves it,
implements it, supersedes it, resolves it -- update the older artifact's
`status:` field in the SAME commit, and link both files to each other.
Superseded files are never deleted; they stay for history with mutual
links (old says "superseded by X", X says "supersedes old").

Before writing anything here, query prior work first with the
`query-brain-vps` skill so you build on what exists instead of
duplicating it.

## Finding Things

Do not browse this folder manually. Use the `query-brain-vps` skill --
hybrid semantic + keyword search over the whole brain, this folder
included.
