-- Standard SQL. Replace YOUR_PROJECT and provision the typed, date-partitioned source.
-- Parameters: @start_date DATE inclusive; @end_date DATE exclusive.
-- Grain: acquisition cohort date × channel × campaign. Source must be unique at this grain.
WITH aggregated AS (
  SELECT DATE_TRUNC(Date, MONTH) AS month, Channel, Campaign,
    SUM(Impressions) AS impressions, SUM(Clicks) AS clicks,
    SUM(Cost_EUR) AS media_cost_eur, SUM(Leads) AS leads,
    SUM(Qualified_Leads) AS qualified_leads, SUM(Conversions) AS customers,
    SUM(Revenue_EUR) AS attributed_revenue_eur
  FROM `YOUR_PROJECT.portfolio.acquisition_funnel`
  WHERE Date >= @start_date AND Date < @end_date
  GROUP BY month, Channel, Campaign
)
SELECT *,
  SAFE_DIVIDE(media_cost_eur, customers) AS media_cac_eur,
  SAFE_DIVIDE(media_cost_eur, qualified_leads) AS cpql_eur,
  SAFE_DIVIDE(qualified_leads, leads) AS lead_qualification_rate,
  SAFE_DIVIDE(attributed_revenue_eur, media_cost_eur) AS roas,
  SAFE_DIVIDE(clicks, impressions) AS ctr,
  SAFE_DIVIDE(media_cost_eur, clicks) AS cpc_eur
FROM aggregated
ORDER BY month, Channel, Campaign;
