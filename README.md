# Acquisition Analytics & Dashboard Architecture

A reproducible six-month acquisition dataset, documented KPI definitions, BigQuery aggregation and a Looker Studio implementation specification. **Every campaign result in this repository is synthetic.**

## Run

Node.js 22+, no dependencies:

```sh
npm test
npm run validate
npm run generate
```

The committed CSV contains **1,464 rows**: April–September 2026, eight channel/campaign combinations per day. The seeded generator recreates it exactly. [Metadata](datasets/metadata.json) records grain, period, currency, seed and cost scope.

## Three dashboard audiences

| View | Decision | Content |
| --- | --- | --- |
| Executive board | Review acquisition economics and revenue | Monthly media cost, customers, media CAC, attributed revenue and blended ROAS |
| Performance marketing | Investigate efficiency and lead quality | Channel/campaign trends, CTR, CPC, CPQL and qualification rate |
| CRM sales pipeline | Identify stage bottlenecks | Leads, qualified leads, conversions, close rate and reconciliation exceptions |

```text
Ads exports + CRM outcomes
          ↓
Typed source tables → grain and freshness checks
          ↓
BigQuery cohort aggregation / metric definitions
          ↓
Looker Studio: Board / Marketing / Sales
```

[Calculated metrics](queries/calculated-metrics.md) distinguish media CAC from fully loaded CAC and ROAS from profitability. [BigQuery SQL](queries/acquisition-metrics.sql) uses SUM components and SAFE_DIVIDE. [Looker Studio setup](docs/looker-studio.md) specifies controls, drill-downs, scorecards and illustrative operating thresholds.

## Simulation assumptions and verification

Daily acquisition cohorts have resolved synthetic outcomes with no conversion lag. Conversions are unique new customers within the simulation. The generator models weekday/weekend demand, channel-specific economics, seasonal volume and an intentionally lower Meta qualification rate in June. These are simulation inputs, not findings about real campaigns.

Money is denominated in EUR. Cost is paid media only; zero organic media spend does not mean organic acquisition is free. Counts obey Impressions ≥ Clicks ≥ Leads ≥ Qualified_Leads ≥ Conversions. Tests check complete dates, unique grain, funnel consistency, deterministic regeneration, NULL ratios and cent-level reconciliation.

No real customer or campaign data is included. BigQuery and Looker Studio execution require your own dataset and account; the repository does not fabricate a live dashboard link or verified commercial outcomes.

[Portfolio hub](https://github.com/ninjaDX27/ninjaDX27) · [Tracking](https://github.com/ninjaDX27/martech-tracking-architecture)
