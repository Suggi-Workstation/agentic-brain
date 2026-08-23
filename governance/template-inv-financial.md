---
name: template-inv-financial
id: 20260819T172745Z
tier: core-template
lock: approval-required
approved_by: Suggi
author: Neo
links:
  - investing-hub:frameworks/deep-financial-scoring.md
  - library/value-investing/anchor-value-investing.md
---

# Investment Template -- Financial Health Scoreboard

The output format for a financial health and red flag assessment.
Produces normalized earnings, FCF conversion quality, debt structure
analysis, ROIIC, Altman Z-Score, Beneish M-Score, and a structured
red flag scan. The methodology lives in
`investing-hub:frameworks/deep-financial-scoring.md`; this template
defines what the completed analysis looks like.

## What This Template Is

A scoreboard for financial trustworthiness and survival. Answers:
Are the numbers real? Can this company survive a crisis? The
framework explains the ratios; this template enforces the output.

## Global Formatting Rules

Same as all brain files: 7-bit ASCII, lowercase, hyphen-delimited.

## Compliance Checklist -- HARD GATE

Pre-commit gate. Every item MUST be confirmed.

- [ ] Ticker and company name stated  (PASS / HALT)
- [ ] Normalized earnings: 5yr table with adjustments  (PASS / HALT)
- [ ] SBC not added back (rule confirmed)  (PASS / HALT)
- [ ] Cyclical normalization applied if cyclical business  (PASS / HALT)
- [ ] OCF/NI ratio: 5yr calculated and trend assessed  (PASS / HALT)
- [ ] FCF/NI ratio: 5yr calculated  (PASS / HALT)
- [ ] FCF consistency: 8 quarters or 5 years counted  (PASS / HALT)
- [ ] Accruals ratio calculated  (PASS / HALT)
- [ ] Cash conversion cycle: 5yr trend  (PASS / HALT)
- [ ] Leverage ratios: all 6 calculated  (PASS / HALT)
- [ ] Debt maturity ladder mapped  (PASS / HALT)
- [ ] Altman Z-Score calculated and trend assessed  (PASS / HALT)
- [ ] ROIIC calculated and trend assessed  (PASS / HALT)
- [ ] Red flag scan: all 5 categories checked  (PASS / HALT)
- [ ] Beneish M-Score calculated (or simplified 5-variable)  (PASS / HALT)
- [ ] Financial health verdict: PASS / WATCHLIST / DISCARD  (PASS / HALT)
- [ ] Every number sourced (filing year, data provider)  (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters  (PASS / HALT)

## Frontmatter Schema

```yaml
---
name: <ticker>-financial
id: <YYYYMMDDTHHMMSSZ>
tier: investment-financial
author: Neo
tags: [financial-health, earnings-quality, red-flags, <ticker>]
links:
  - investing-hub:frameworks/deep-financial-scoring.md
  - investing-hub:companies/<ticker>.md
---
```

## Scoreboard

### Header

```
Company:    <name>
Ticker:     <ticker>
Sector:     <sector>
```

### 1. Normalized Earnings

| Year | Reported NI | Adjustments | Normalized NI | Normalized EPS |
|:--|--:|--:|--:|--:|
| Y-4 | $X | +/- $Y | $Z | $Z/sh |
| Y-3 | $X | +/- $Y | $Z | $Z/sh |
| Y-2 | $X | +/- $Y | $Z | $Z/sh |
| Y-1 | $X | +/- $Y | $Z | $Z/sh |
| Current | $X | +/- $Y | $Z | $Z/sh |

3-5yr avg normalized EPS: $<X>
SBC treatment: <NOT added back -- SBC is a real cost>

### 2. FCF Conversion Quality

| Year | OCF/NI | FCF/NI | FCF-positive? |
|:--|:--|:--|:--|
| Y-4 | X.Xx | X.Xx | Y/N |
| Y-3 | X.Xx | X.Xx | Y/N |
| Y-2 | X.Xx | X.Xx | Y/N |
| Y-1 | X.Xx | X.Xx | Y/N |
| Current | X.Xx | X.Xx | Y/N |

```
OCF/NI trend:         <improving / stable / deteriorating>
FCF consistency:      <N>/8 quarters or <N>/5 years
Accruals ratio:       <X>%  (flag if > 15%)
Cash conversion cycle: <X> days (5yr trend: <improving/worsening>)
```

### 3. Debt Structure

| Ratio | Value | Zone (Safe/Caution/Danger) |
|:--|:--|:--|
| Debt/Equity | X.Xx | <zone> |
| Debt/EBITDA | X.Xx | <zone> |
| Net Debt/EBITDA | X.Xx | <zone> |
| Interest Coverage | X.Xx | <zone> |
| Debt/FCF | X.Xx | <zone> |
| Current Ratio | X.Xx | <zone> |

Debt maturity ladder:

| Year | Debt Maturing | % of Total | FCF Coverage |
|:--|--:|--:|:--|
| Y+1 | $X | X% | <X>x |
| Y+2 | $X | X% | <X>x |
| Y+3 | $X | X% | <X>x |
| Y+4 | $X | X% | <X>x |
| Y+5+ | $X | X% | N/A |

Refinance risk: <Y/N -- which year(s) breach>

### 4. Altman Z-Score

```
Z = 1.2(X1) + 1.4(X2) + 3.3(X3) + 0.6(X4) + 0.99(X5) = <X.XX>
Zone: <Safe (>2.99) / Grey (1.81-2.99) / Distress (<1.81)>
5yr trend: <improving / stable / deteriorating>
```

### 5. ROIIC

```
ROIIC (3yr):  <X>%
Trend:        <rising / stable / falling>
vs WACC:      <above / below>
Signal:       <exceptional / strong / adequate / poor / value-destroying>
```

### 6. Red Flag Scan

| Category | Flags Found | Severity |
|:--|:--|:--|
| Earnings quality | <list or none> | <HIGH/CRITICAL> |
| Balance sheet | <list or none> | <HIGH/CRITICAL> |
| Cash flow | <list or none> | <HIGH/CRITICAL> |
| Governance | <list or none> | <HIGH/CRITICAL> |
| Munger psychology | <list or none> | <MEDIUM/HIGH> |

### 7. Beneish M-Score

```
M-Score: <X.XX>
Interpretation: <unlikely / possible / likely manipulator>
Simplified 5-variable: <used / not needed>
```

### Verdict

```
EARNINGS QUALITY:    <trustworthy / questionable / manipulative>
BALANCE SHEET:       <strong / adequate / fragile>
FCF CONVERSION:      <strong / moderate / weak>
FINANCIAL HEALTH:    <PASS / WATCHLIST / DISCARD>

Key risk: <single most dangerous financial vulnerability>
```

---

*Last updated: 2026-08-19 by Neo. Scoreboard format; methodology in the framework file.*