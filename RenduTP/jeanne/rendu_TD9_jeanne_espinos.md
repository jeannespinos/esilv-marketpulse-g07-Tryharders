# Bloomberg Field Mapping - TD09 - Jeanne Espinos

## Access mode

APPROVED_SAMPLE

- Source: data/sample/bloomberg_reference_sample.json
- Reference: docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md
- Live connectivity: not demonstrated
- I did not have access to a Bloomberg terminal, so I used the approved sample file.

## Market instruments

| Role | Canonical ticker | Bloomberg identifier |
|---|---|---|
| Instrument | AAPL | AAPL US Equity |
| Benchmark | SP500 | SPX Index |

## What I inspected

| Series | Observations | First date | Last date | Missing values |
|---|---|---|---|---|
| AAPL US Equity -> AAPL | 21 | 2026-09-01 | 2026-09-30 | none |
| SPX Index -> SP500 | 21 | 2026-09-01 | 2026-09-30 | none (volume = 0) |

## Field mapping

| MarketPulse field | Source field or mapping | Status / notes |
|---|---|---|
| date | observation_date | teaching wrapper key, text YYYY-MM-DD |
| ticker | application mapping (canonical_ticker) | AAPL or SP500, never the Bloomberg identifier |
| open | open_value | teaching wrapper key, number |
| high | high_value | teaching wrapper key, number |
| low | low_value | teaching wrapper key, number |
| close | close_value | teaching wrapper key, number |
| volume | volume_value | teaching wrapper key, integer, 0 for SPX Index |

Important: these keys are teaching wrapper keys, not real Bloomberg field names.
I did not invent any LIVE Bloomberg field name.

## TD10 handoff

- Access mode: APPROVED_SAMPLE
- Instrument identifier: AAPL US Equity -> AAPL
- Benchmark identifier: SPX Index -> SP500
- Date representation: text YYYY-MM-DD in observation_date
- Input structure: JSON with a "series" list, each series has role, canonical_ticker, provider_identifier and observations
- Missing fields: none
- Special normalization notes: ticker comes from canonical_ticker, prices become float, volume becomes int, SPX volume is 0 because an index has no traded volume
- Expected canonical reference: data/sample/bloomberg_reference_expected.json

## Security

No password, login or session information in this document.
