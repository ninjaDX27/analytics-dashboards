-- SQLite. Leads criadas em setembro de 2026, observadas até outubro.
-- 1: Funil global. Não interpretar como uma comparação causal.
SELECT COUNT(*) AS leads,
       SUM(qualified_at IS NOT NULL) AS qualified,
       SUM(submitted_at IS NOT NULL) AS submitted,
       SUM(funded_at IS NOT NULL) AS funded,
       ROUND(100.0 * SUM(qualified_at IS NOT NULL)/NULLIF(COUNT(*),0),1) AS qualification_pct,
       ROUND(100.0 * SUM(funded_at IS NOT NULL)/NULLIF(COUNT(*),0),1) AS funded_pct
FROM lead;

-- 2: Funil por canal, denominador consistente.
SELECT source,
       COUNT(*) AS leads,
       SUM(qualified_at IS NOT NULL) AS qualified,
       SUM(submitted_at IS NOT NULL) AS submitted,
       SUM(funded_at IS NOT NULL) AS funded,
       ROUND(100.0*SUM(funded_at IS NOT NULL)/NULLIF(COUNT(*),0),1) AS funded_pct
FROM lead GROUP BY source ORDER BY source;

-- 3: Primeiro contacto, horas e SLA <=24h para todas as leads.
SELECT COUNT(*) AS leads,
       SUM(contacted_at IS NOT NULL) AS contacted,
       SUM(contacted_at IS NOT NULL AND
           (julianday(contacted_at)-julianday(created_at))*24 <= 24.00001) AS within_24h,
       ROUND(100.0*SUM(contacted_at IS NOT NULL AND
           (julianday(contacted_at)-julianday(created_at))*24 <= 24.00001)
           /NULLIF(COUNT(*),0),1) AS sla_24h_pct,
       ROUND(AVG((julianday(contacted_at)-julianday(created_at))*24),1) AS mean_hours
FROM lead;

-- 4: Eficiência de media só para canais pagos; sem custos laborais ou incrementality.
SELECT l.source, COUNT(*) AS leads, SUM(l.funded_at IS NOT NULL) AS funded,
       MAX(c.media_spend_eur) AS media_spend_eur,
       ROUND(MAX(c.media_spend_eur)/NULLIF(COUNT(*),0),2) AS media_cpl_eur,
       ROUND(MAX(c.media_spend_eur)/NULLIF(SUM(l.funded_at IS NOT NULL),0),2) AS media_cost_per_funded_eur
FROM lead l JOIN channel_spend c ON c.source=l.source
GROUP BY l.source ORDER BY l.source;

-- 5: Controlos de consistência: todos os contadores devem ser zero.
SELECT
  SUM(qualified_at IS NOT NULL AND contacted_at IS NULL) AS qualified_without_contact,
  SUM(submitted_at IS NOT NULL AND qualified_at IS NULL) AS submitted_without_qualify,
  SUM(funded_at IS NOT NULL AND submitted_at IS NULL) AS funded_without_submit,
  SUM(funded_at IS NOT NULL AND status != 'won') AS funded_not_won,
  SUM(contacted_at < created_at) AS contact_before_create
FROM lead;
