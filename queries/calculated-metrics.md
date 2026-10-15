# Calculated metrics

All numerators and denominators use the same filtered acquisition cohorts, attribution rule and reporting window. Sum components before dividing. Never average campaign-level ratios.

$$CAC_{media}=\frac{\sum MediaCost_{EUR}}{\sum NewCustomers}$$

$$CPQL=\frac{\sum MediaCost_{EUR}}{\sum QualifiedLeads}$$

$$LeadQualificationRate=\frac{\sum QualifiedLeads}{\sum Leads}$$

$$ROAS=\frac{\sum AttributedRevenue_{EUR}}{\sum MediaCost_{EUR}}$$

The requested CAC field is explicitly **media CAC** because the supplied CSV has media cost only. A fully loaded CAC additionally needs acquisition payroll, agency, software and other agreed cost inputs. Conversions represent unique new customers in this synthetic dataset. That equivalence must be verified against the production CRM.

ROAS is a revenue multiple, not profit or ROI. Organic rows have zero media cost; their ROAS is unavailable. A combined all-channel ratio is blended attributed revenue / paid media cost and is labeled blended ROAS. Qualification rate is a fraction, displayed as a percentage. Zero-denominator results remain NULL, not zero.

The production aggregation is [acquisition-metrics.sql](acquisition-metrics.sql). It uses BigQuery `SAFE_DIVIDE`, typed amounts, a partition-friendly date filter and explicit grouping. Bind DATE parameters, replace the project/table identifier and enforce source uniqueness before running. BigQuery execution is not claimed without a connected dataset.

[BigQuery mathematical functions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/mathematical_functions) documents `SAFE_DIVIDE` and its NULL behavior.
