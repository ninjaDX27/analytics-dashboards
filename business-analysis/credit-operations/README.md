# Credit Operations Transformation — Business Analysis Case Study

**Case study de Business Analysis em intermediação de crédito (Portugal).**

> **Cenário fictício.** A empresa, o processo, as 40 leads e os gastos são sintéticos. Não são resultados da MaxFinance Top, de um banco ou de qualquer entidade real. Este é um exercício de análise de requisitos e de decisão, não uma aplicação de decisão de crédito.

## Questão de negócio
**Como reduzir atrasos na qualificação e recolha de documentos, mantendo controlo humano sobre decisões e melhorando a rastreabilidade do funil?**

O entregável demonstra a passagem de problema → evidência → processos → requisitos → backlog → validação → decisão de investimento.

## Entregáveis
| Artefacto | Finalidade |
| --- | --- |
| [01 - Enquadramento](docs/01-problema-e-metricas.md) | Problema, hipóteses, stakeholders e KPI dictionary |
| [02 - AS-IS / TO-BE](docs/02-processos.md) | Modelos de processos, pontos de fricção e controlos |
| [BPMN 2.0 — AS-IS](bpmn/AS-IS.bpmn) | BPMN XML editável, pools/lane, gateways e message flows |
| [BPMN 2.0 — TO-BE](bpmn/TO-BE.bpmn) | BPMN XML editável com CRM, checklist, revisão humana e alerta SLA |
| [Guia BPMN 2.0](bpmn/GUIA-BPMN.md) | Tutorial, comparação e validação antes de produção |
| [03 - Requisitos](docs/03-requisitos.md) | Business requirements, requisitos funcionais e não funcionais |
| [04 - User stories e UAT](docs/04-backlog-e-uat.md) | Priorização MoSCoW e casos de teste |
| [05 - Business case](docs/05-business-case.md) | Modelo de impacto, custos, riscos e regras de decisão |
| [Dados sintéticos](data/leads_sinteticas.csv) | 40 leads fictícias de setembro de 2026 |
| [Setup SQLite](sql/setup.sql) | Base de dados local sem dependências externas |
| [Análises SQL](sql/analysis.sql) | Funil, tempos de resposta e custos pagos |
| [Testes de consistência](tests/test_data.py) | Integridade, contagens e lógica temporal |

## Executar localmente
Requer Python 3.10+ (biblioteca-padrão), ou SQLite CLI.

```bash
python tests/test_data.py
sqlite3 case.db < sql/setup.sql
sqlite3 -header -column case.db < sql/analysis.sql
```

Em Windows, se não tiveres `sqlite3` CLI, executa os testes Python e usa a extensão SQLite no VS Code para abrir `sql/setup.sql` e `sql/analysis.sql`.

## Métricas esperadas apenas no cenário sintético
- 40 leads criadas; 25 qualificadas (62,5%); 18 submetidas a bancos (45%); 10 financiadas (25% do total).
- 32/40 contactadas em até 24 horas (80%).
- Google Ads: 10 leads, 2 financiadas, 600 € em media spend → CPL de media = 60 €; custo de media por processo financiado = 300 €.
- Meta Ads: 10 leads, 1 financiada, 400 € em media spend → CPL de media = 40 €; custo de media por processo financiado = 400 €.
- **Estes custos não são CAC completo**, não incluem salários, ferramentas, comissões, nem atribuição incremental.

É uma fotografia de uma coorte fictícia de leads de setembro, observada até outubro. Não sustenta conclusões causais. Os custos só são comparáveis para canais pagos com spend declarado.

## Resultado de Business Analysis
A recomendação provisória é testar um fluxo único de triagem + checklist documental + alertas + reporting, com controlo humano para verificação dos documentos e decisões comerciais. Um piloto só avança com baseline real, requisitos validados com stakeholders e revisão jurídica/privacidade.

## Próximo exercício
1. Corre o teste de dados e as queries.
2. Explica por que um CPL mais baixo não significa necessariamente melhor economia de aquisição.
3. Conduz uma entrevista simulada com um intermediário de crédito e revê os requisitos.
4. Abre, revê e valida [os modelos BPMN 2.0](bpmn/GUIA-BPMN.md) num modelador; acrescenta matriz RACI e uma estimativa de ROI com custos validados.

**Foco de carreira:** Junior Business Analyst · Business Process Analyst · Digital Transformation Analyst.
