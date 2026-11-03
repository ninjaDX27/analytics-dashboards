# 01 — Problem framing & measurement plan

## Decisão
O diretor de operações deve decidir **se vale a pena iniciar um piloto** de gestão digital de leads e documentos, ou se é preferível corrigir primeiro disciplina operacional e reporting.

## Contexto ilustrativo
Uma intermediária de crédito fictícia recebe contactos pelo website, WhatsApp, campanhas de aquisição e recomendação. A informação é registada em diferentes locais, a recolha documental é repetitiva e o pipeline tem baixa rastreabilidade. Não assumimos que a tecnologia é a causa ou a solução.

## Problema a validar
Há potenciais atrasos entre receção, primeiro contacto, qualificação, documentação, submissão e decisão. Não existe baseline real fornecida. **Não apresentar os valores do dataset como números de uma empresa real.**

## Hipóteses falsificáveis
- H1: leads com primeiro contacto > 24h têm menor taxa de qualificação. Comparar coortes, canal e fonte; observar confundidores.
- H2: documentação incompleta aumenta tempo até submissão.
- H3: padronizar checklist e atribuir responsável reduz retrabalho.
- H4: notificações sem workflow humano provocam falsas sensações de progresso.

## Stakeholder map
| Stakeholder | Necessidade / decisão | Participação |
| --- | --- | --- |
| Diretor de operações | Capacidade, qualidade, ROI | Sponsor / aprova piloto |
| Gestor comercial | Visibilidade do pipeline | Validação diária |
| Intermediário de crédito | Menos tarefas manuais e erros | Entrevistas, UAT |
| Marketing | Qualidade das leads e atribuição | Definições do funil |
| Equipa IT / fornecedor CRM | Viabilidade, integrações | Estimativa / implementação |
| Jurídico / DPO | Base legal, minimização e segurança | Gate pré-produção |
| Cliente | Clareza, consentimentos e comunicação | Teste de experiência |

## KPI dictionary (grão: uma lead)
| KPI | Fórmula | Cuidado interpretativo |
| --- | --- | --- |
| Leads recebidas | COUNT(DISTINCT lead_id) por coorte de criação | Não usar contactos ou duplicados como leads novas |
| Qualification rate | leads qualified_at NOT NULL / leads recebidas | Definir previamente o critério de qualificação |
| Submission rate | leads submitted_at NOT NULL / leads recebidas | Coorte madura; atraso de submissão |
| Funded rate | leads funded_at NOT NULL / leads recebidas | Não é receita e não é aprovação |
| SLA 24h | leads contactadas até 24h / leads criadas | Definir calendário comercial e canal |
| Media CPL | spend de media / leads atribuídas ao canal | Só quando fonte e spend têm a mesma janela |
| Media cost / funded | spend de media / leads financiadas | Não é CAC total nem causalidade |
| Lead-to-submission time | submitted_at - created_at | Reportar mediana e distribuição |

## Qualidade e limites
- `created_at` marca criação da lead; os demais campos representam o primeiro marco efetivo atingido.
- O dataset sintético é deliberadamente simples, sem duplicados, nem correções históricas.
- Uma coorte de setembro foi observada até outubro; em dados reais definir cutoff, censura e dados em atraso.
- Uma fotografia não revela todos os eventos, tempo de cada etapa, motivo de perda ou custos operacionais.
- Para produzir diagnóstico real: recolher exports CRM, custos de media, consentimentos e timestamps, verificar integridade e reconciliar números com equipas.

## Critério de sucesso do piloto — a acordar
Medir redução de tempo até submissão e de retrabalho **sem piorar erros documentais, privacidade, reclamações ou experiência do cliente**. Definir baseline antes de estabelecer metas numéricas.
