# 03 — Business requirements document (BRD) — v0.1

**Estado:** draft conceptual por validar com stakeholders. **Âmbito:** registo e triagem de leads, checklist de documentos, visibilidade e histórico do funil. **Fora do âmbito:** decisão de crédito autónoma, substituição do profissional, integração bancária real sem contrato / especificação e classificação de risco automatizada.

## Business requirements
- BR-01: garantir que cada contacto tem ID único, origem e responsável.
- BR-02: reduzir atrasos de resposta e falta de documentação sem perder controlo humano.
- BR-03: disponibilizar métricas reconciliáveis de funil e tempos por canal.
- BR-04: permitir auditoria, segregação de acessos e gestão de consentimentos quando aplicável.

## Functional requirements
| ID | Requisito | Prioridade | Critério de aceitação resumido |
| --- | --- | --- | --- |
| FR-01 | Captar lead com ID, timestamp e fonte | Must | Novo contacto válido cria exatamente um registo |
| FR-02 | Deteção e resolução de potenciais duplicados | Must | Registos sinalizados não são fundidos sem regra autorizada |
| FR-03 | Atribuir responsável e definir SLA de contacto | Must | Estado e responsável consultáveis; alertas na violação |
| FR-04 | Registar marcos e histórico de alterações | Must | Toda alteração tem quem, quando e o quê |
| FR-05 | Checklist documental por tipo de perfil | Must | Mostra apenas categorias pertinentes e respeita permissões |
| FR-06 | Lembretes para documentos pendentes | Should | Envio sujeito a opt-in/base aplicável e registo |
| FR-07 | Dashboard de funil por coorte e origem | Should | Métricas batem com export auditável |
| FR-08 | Export para análise autorizada | Could | Exportação restringida por perfis, com log |

## Non-functional requirements
| ID | Categoria | Requisito verificável |
| --- | --- | --- |
| NFR-01 | Segurança | Autorização por papel e mínimo privilégio; teste de acessos |
| NFR-02 | Privacidade | Recolha mínima, prazos de retenção aprovados e pedidos de titulares |
| NFR-03 | Disponibilidade | SLA operacional a contratar e monitorizar; sem número fictício |
| NFR-04 | Observabilidade | Erros de integração, duplicados e falhas de notificação registados |
| NFR-05 | Usabilidade | Testes com operadores; critérios de tarefa/tempo definidos no piloto |

## Dependências e decisões abertas
- Seleção de CRM; canal oficial de WhatsApp e contratos; integração do website.
- DPO/jurídico define base legal, aviso de privacidade, conservação e acesso.
- Direção aprova owners, budget, scope e métricas.
- Equipa operacional valida o BPMN e o significado de qualificado / submetido / financiado.

## Rastreabilidade
BR-01 → FR-01, FR-02, FR-04; BR-02 → FR-03, FR-05, FR-06; BR-03 → FR-07, FR-08; BR-04 → FR-04, NFR-01, NFR-02, NFR-04.
