---
name: template-inv-management
id: 20260819T172744Z
tier: core-template
lock: approval-required
approved_by: Suggi
author: Neo
links:
  - investing/frameworks/simple-management-scoring.md
  - library/value-investing/anchor-value-investing.md
---

# Investment Template -- Management Scoreboard

The output format for a management quality assessment. Produces a
5-dimension score: insider ownership (skin in the game), capital
allocation, acquisition track record, say-do gap (overpromising/
underdelivering), and communication candor. Includes the integrity
red flag catalog. The methodology lives in
`investing/frameworks/simple-management-scoring.md`; this template
defines what the completed analysis looks like.

## What This Template Is

A scoreboard for management character and competence. Management
quality is measured by actions, not words. What they do with capital
reveals character more reliably than anything they say.

## Global Formatting Rules

Same as all brain files: 7-bit ASCII, lowercase, hyphen-delimited.

## Compliance Checklist -- HARD GATE

Pre-commit gate. Every item MUST be confirmed.

- [ ] Ticker and company name stated  (PASS / HALT)
- [ ] Insider ownership: % stated, source (proxy + Form 4)  (PASS / HALT)
- [ ] Insider ownership adjustments applied (net buyer/seller, hedging)  (PASS / HALT)
- [ ] Capital allocation: 10yr cash flow deployment table  (PASS / HALT)
- [ ] ROIIC calculated and trend assessed  (PASS / HALT)
- [ ] Acquisition track record: deal list with prices and outcomes  (PASS / HALT)
- [ ] Goodwill impairment check performed  (PASS / HALT)
- [ ] Say-do gap: guidance vs actual results compared (8+ quarters)  (PASS / HALT)
- [ ] Communication candor: 3+ shareholder letters assessed  (PASS / HALT)
- [ ] GAAP vs non-GAAP gap checked  (PASS / HALT)
- [ ] Integrity red flag scan: all 7 items checked  (PASS / HALT)
- [ ] 5 dimensions scored 1-5 with cited evidence  (PASS / HALT)
- [ ] Composite score calculated (weighted sum)  (PASS / HALT)
- [ ] Moat-management matrix classification  (PASS / HALT)
- [ ] Pipeline verdict: PASS / CONDITIONAL / DISCARD  (PASS / HALT)
- [ ] Every score of 4+ has at least one primary source  (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters  (PASS / HALT)

## Frontmatter Schema

```yaml
---
name: <ticker>-management
id: <YYYYMMDDTHHMMSSZ>
tier: investment-management
author: Neo
tags: [management, capital-allocation, integrity, <ticker>]
links:
  - investing/frameworks/simple-management-scoring.md
  - investing/companies/<ticker>.md
---
```

## Scoreboard

### Header

```
Company:    <name>
Ticker:     <ticker>
CEO:        <name> (tenure: <years>)
```

### Dimension 1: Insider Ownership (Skin in the Game) -- Weight 25%

```
Insider ownership:     <X>%
Dollar value:          $<X>
Source:                <proxy DEF 14A + Form 4>
Net buyer/seller (2yr): <buyer / seller / neutral>
Adjustment:            <+/- adjustment + rationale>
Adjusted score:        <X>  (1-5)
```

| Score | Ownership | Signal |
|:--|:--|:--|
| 1 | <1% | Token, hired-gun CEO |
| 2 | 1-3% | Modest, may be option grants |
| 3 | 3-10% | Meaningful, net worth tied to stock |
| 4 | 10-20% | Significant, founder-level |
| 5 | >20% | Founder/owner-operator |

### Dimension 2: Capital Allocation -- Weight 20%

10-year cash deployment:

| Use of Cash | 10yr Total | % of Total |
|:--|--:|--:|
| CapEx (maintenance + growth) | $X | X% |
| Acquisitions | $X | X% |
| Dividends | $X | X% |
| Buybacks (net of issuance) | $X | X% |
| Debt repayment | $X | X% |

```
ROIIC (3yr):           <X>%
ROIIC trend:           <rising / stable / falling>
Dividend vs FCF:       <X>  (sustainable if < 1.0x)
Score:                 <X>  (1-5)
```

| Score | Capital Allocation | Signal |
|:--|:--|:--|
| 1 | Value-destroying | ROIC < WACC, empire-building |
| 3 | Adequate | Generally rational, some mistakes |
| 5 | Exceptional | Ruthlessly rational, counter-cyclical |

### Dimension 3: Acquisition Track Record -- Weight 20%

| Deal | Year | Price | Method | Outcome |
|:--|:--|:--|:--|:--|
| <acquisition 1> | YYYY | $X | cash/stock | <created/destroyed value> |
| <acquisition 2> | YYYY | $X | cash/stock | <created/destroyed value> |
| <acquisition 3> | YYYY | $X | cash/stock | <created/destroyed value> |

```
Goodwill impairment (5yr): <Y/N, how many times>
Goodwill as % of assets:   <X>%
Score:                     <X>  (1-5)
```

| Score | Track Record | Signal |
|:--|:--|:--|
| 1 | Serial value destroyer | Frequent peak deals, write-downs |
| 3 | Moderate discipline | Infrequent, reasonable |
| 5 | Exceptional | Bolt-on only, walks away from overpriced |

### Dimension 4: Say-Do Gap (Overpromising / Underdelivering) -- Weight 15%

Compare guidance to actual results over 8+ quarters:

| Quarter | Guidance | Actual | Gap |
|:--|:--|:--|:--|
| Q1 | <X> | <X> | <beat/miss/by how much> |
| Q2 | <X> | <X> | <beat/miss/by how much> |
| ... | ... | ... | ... |

```
Pattern:              <systematic overpromiser / sandbagger / honest>
Consistency:          <X>% of quarters where actual >= guidance
Score:                <X>  (1-5)
```

| Score | Say-Do Pattern | Signal |
|:--|:--|:--|
| 1 | Systematic overpromiser | Consistently misses guidance, blames external |
| 2 | Frequent underdeliverer | Misses more than hits, excuses pile up |
| 3 | Mixed | Some beats, some misses, roughly honest |
| 4 | Reliable | Generally delivers what they promise |
| 5 | Under-promises, over-delivers | Sandbags guidance, consistently beats |

### Dimension 5: Communication Candor -- Weight 20%

```
Shareholder letters read:    <N> (years)
Earnings calls scanned:      <N> (quarters)
GAAP vs non-GAAP gap:        <X>%  (flag if > 20%)
Mistakes admitted:           <Y/N -- examples>
Promotional language:        <Y/N -- examples>
Score:                       <X>  (1-5)
```

| Score | Communication | Signal |
|:--|:--|:--|
| 1 | Opaque/deceptive | Hides behind adjusted metrics, never admits |
| 3 | Adequate | Standard reporting, some candor |
| 5 | Exceptional | Plain language, admits mistakes, educates |

### Composite Score

```
Management Score = (Insider Ownership    * 0.25)
                 + (Capital Allocation   * 0.20)
                 + (Acquisition Track     * 0.20)
                 + (Say-Do Gap            * 0.15)
                 + (Communication Candor  * 0.20)
               = <X.X>
```

### Integrity Red Flag Scan

| # | Red Flag | Present? | Evidence |
|:--|:--|:--|:--|
| 1 | Accounting manipulation | Y/N | <evidence> |
| 2 | Excessive comp without performance | Y/N | <evidence> |
| 3 | Related-party transactions | Y/N | <evidence> |
| 4 | Insider selling while promoting | Y/N | <evidence> |
| 5 | SBC treadmill | Y/N | <evidence> |
| 6 | Serial restructuring charges | Y/N | <evidence> |
| 7 | Earnings guidance manipulation | Y/N | <evidence> |

**2+ integrity red flags = automatic DISCARD.**

### Moat-Management Matrix

| Moat \ Mgmt | Exceptional (4-5) | Good (3-3.9) | Adequate (2-2.9) | Poor (1-1.9) |
|:--|:--|:--|:--|:--|
| Wide (4-5) | Ideal: PASS | PASS | Conditional | DISCARD |
| Narrow (3-3.9) | PASS | PASS | Conditional | DISCARD |
| Weak (2-2.9) | Conditional | WATCHLIST | WATCHLIST | DISCARD |
| None (<2) | WATCHLIST | DISCARD | DISCARD | DISCARD |

### Verdict

```
MANAGEMENT SCORE: <X.X>
CLASSIFICATION: <Exceptional / Good / Adequate / Poor>
INTEGRITY RED FLAGS: <N> (auto-DISCARD if 2+)
PIPELINE VERDICT: <PASS / CONDITIONAL / DISCARD>

Key risk: <single most concerning management behavior>
```

---

*Last updated: 2026-08-19 by Neo. Scoreboard format; methodology in the framework file.*