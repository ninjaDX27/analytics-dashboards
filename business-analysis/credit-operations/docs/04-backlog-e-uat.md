# 04 — User stories, prioritização e UAT

## Backlog inicial
| ID | Story | MoSCoW | Dependência |
| --- | --- | --- | --- |
| US-01 | Como gestor, quero ver origem, estado e responsável de cada lead para distribuir trabalho. | Must | FR-01, FR-03 |
| US-02 | Como intermediário, quero ser alertado para o SLA de contacto para reduzir esquecimentos. | Must | FR-03 |
| US-03 | Como intermediário, quero uma checklist de documentos por perfil para evitar pedidos repetidos. | Must | FR-05 |
| US-04 | Como cliente, quero saber quais os documentos em falta e quem me acompanha. | Should | FR-06, privacy review |
| US-05 | Como gestor de operações, quero comparar funis por origem e coorte para priorizar melhorias. | Should | FR-07 |
| US-06 | Como auditor, quero saber quem alterou o estado de um processo e quando. | Must | FR-04 |

## User story detalhada — US-03
**Given** uma lead com perfil validado por colaborador, **when** o intermediário abre a área documental, **then** vê a lista aplicável de documentos obrigatórios e opcionais, distinguindo pendente/recebido/validado.

**Regras:** um upload não significa validação; documentos sensíveis não devem surgir em logs públicos; só um perfil autorizado marca como validado.

## UAT — exemplos
| Caso | Pré-condição | Passos | Esperado |
| --- | --- | --- | --- |
| UAT-01 | Lead nova com fonte web | Criar lead | ID único; timestamp; origem e responsável |
| UAT-02 | Contacto repetido | Enviar mesmo identificador normalizado | Sinalização de duplicado; revisão autorizada |
| UAT-03 | SLA ultrapassado | Simular lead sem contacto dentro do SLA | Alerta ao responsável e trilho de auditoria |
| UAT-04 | Documentos incompletos | Marcar um documento pendente | Estado não avança para pronto para submissão |
| UAT-05 | Permissão insuficiente | Utilizador sem perfil adequado tenta exportar | Export bloqueado e ocorrência registada |
| UAT-06 | Alteração de estado | Utilizador autorizado muda estado | Histórico com antes/depois, autor e timestamp |
| UAT-07 | Métrica do dashboard | Reconciliar amostra CRM com SQL | Identidade de denominadores e resultado |

## Definition of Done da primeira iteração
Requisitos aprovados pelo Product Owner; processo revisto por operadores; UAT críticos aprovados; incidentes de segurança/privacidade fechados; definição e rastreabilidade dos KPIs documentadas; plano de rollback e suporte definido.
