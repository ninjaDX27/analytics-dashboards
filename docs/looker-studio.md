# Looker Studio build specification

This repository supplies the dataset, SQL and report specification. It does not claim to contain a published Looker Studio report.

1. Load the CSV into a typed BigQuery table. Use DATE for Date, STRING for dimensions, INT64 for counts and NUMERIC for EUR amounts. Partition on Date and cluster on Channel, Campaign.
2. Reject duplicate Date/Channel/Campaign keys and impossible funnels before refreshing the reporting table.
3. Connect the prepared table/view to Looker Studio. Define ratios from SUM components, with explicit zero-denominator handling.
4. Add date range, channel and campaign controls. Set EUR formatting and consistent acquisition-cohort dates. Show data freshness and the synthetic label.
5. Configure scorecards with previous-period comparisons, a monthly trend, channel drill-down and cross-filtering where it helps an operating decision.
6. Keep the CRM page restricted to aggregate lead stages. Reconcile counts through stable lead/customer IDs in a governed warehouse layer; do not use a many-to-many report blend to join spend to individual leads.
7. Test each filter against the SQL result. Include zero-spend and zero-conversion segments. Define access and scheduled delivery only after an owner approves the audience.

## Operating thresholds for the demo

These parameters are illustrative test settings, not Portuguese market benchmarks or business recommendations.

| Metric | Illustrative target | Alert condition | Owner / action |
| --- | --- | --- | --- |
| CPQL | €80 | >1.25 × target for two complete weeks, at least 30 qualified leads | Growth: inspect channel/creative mix and tracking |
| Media CAC | €400 | >1.25 × target, at least 20 resolved new customers | Growth + Sales: reconcile attribution and close rate |
| Qualification rate | 45% | <35% with at least 100 resolved leads | Sales operations: review qualification reasons |
| ROAS | 3.0× | <2.0× with at least 20 resolved conversions | Commercial lead: inspect revenue completeness and margin context |

Do not automatically change budgets on these thresholds. In production, calibrate targets to measured baselines, unit economics, conversion lag and capacity. Pair efficiency KPIs with lead-quality and data-freshness guardrails.
