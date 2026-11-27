\# Bloomberg Field Mapping



\## Access mode



APPROVED\_SAMPLE



\- Source: `data/sample/bloomberg\_reference\_sample.json`

\- Expected canonical reference: `data/sample/bloomberg\_reference\_expected.json`

\- Instructor reference: `docs/10\_BLOOMBERG\_INSTRUCTOR\_REFERENCE.md` (not present in the team repository; the mapping below was derived by comparing the sample fixture with the expected canonical result)

\- Live connectivity: \*\*not demonstrated\*\*



The fixture declares itself as `"sample\_kind": "instructor\_approved\_fallback\_fixture"` and `"is\_live\_bloomberg\_output": false`. Its values are illustrative teaching values reused from `data/sample/prices.csv`, not certified Bloomberg historical observations.



\## Market instruments



| Role | Canonical ticker | Bloomberg identifier |

|---|---|---|

| Instrument | AAPL | AAPL US Equity |

| Benchmark | SP500 | SPX Index |



Both pairs were checked in the sample fixture (`canonical\_ticker` / `provider\_identifier` keys of each series).



\## Field mapping



| MarketPulse field | Source field or mapping | Status / notes |

|---|---|---|

| date | `observation\_date` | teaching wrapper key; string `YYYY-MM-DD`, kept as is |

| ticker | application mapping from series `canonical\_ticker` | `AAPL` or `SP500`; never the Bloomberg identifier |

| open | `open\_value` | teaching wrapper key; numeric |

| high | `high\_value` | teaching wrapper key; numeric |

| low | `low\_value` | teaching wrapper key; numeric |

| close | `close\_value` | teaching wrapper key; numeric |

| volume | `volume\_value` | teaching wrapper key; integer, `0` for SPX Index |



\*\*Important:\*\* `observation\_date`, `open\_value`, `high\_value`, `low\_value`, `close\_value` and `volume\_value` are \*\*teaching wrapper keys\*\*, not Bloomberg LIVE field mnemonics. No LIVE Bloomberg field name is documented here because none was observed.



\## Inspected inputs



| Series | Observations | First date | Last date | Missing values |

|---|---|---|---|---|

| AAPL US Equity → AAPL | 21 | 2026-09-01 | 2026-09-30 | none |

| SPX Index → SP500 | 21 | 2026-09-01 | 2026-09-30 | none (volume is 0) |



\## TD10 handoff



\- Access mode: APPROVED\_SAMPLE

\- Instrument identifier: `AAPL US Equity` → canonical `AAPL`

\- Benchmark identifier: `SPX Index` → canonical `SP500`

\- Date representation: string `YYYY-MM-DD` in `observation\_date`

\- Input structure: JSON object with a `series` list; each series has `role`, `canonical\_ticker`, `provider\_identifier` and an `observations` list

\- Missing fields: none in the sample

\- Special normalization notes:

&#x20; - set `ticker` from `canonical\_ticker`, not from `provider\_identifier`;

&#x20; - convert prices to `float` and volume to `int` (the JSON contains integers such as `248` or `6600` that must become floats);

&#x20; - SPX Index volume is `0`: an index has no traded volume, so this is expected, not an error;

&#x20; - the output must match `data/sample/bloomberg\_reference\_expected.json` row for row;

&#x20; - `analytics.py` must not change.

\- Expected canonical reference: `data/sample/bloomberg\_reference\_expected.json`



\## Security



No credential, session token or terminal information is included in this document.

