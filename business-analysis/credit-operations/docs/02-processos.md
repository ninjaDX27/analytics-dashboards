# 02 — Process analysis: AS-IS and TO-BE

Os diagramas Mermaid abaixo são esquemas conceptuais de síntese, não BPMN. A modelação formal inicial está nos ficheiros BPMN 2.0 XML com BPMN DI: **[AS-IS](../bpmn/AS-IS.bpmn)** e **[TO-BE](../bpmn/TO-BE.bpmn)**. Consulta o **[guia BPMN](../bpmn/GUIA-BPMN.md)** para compreender pools, lanes, eventos, gateways, message flows, pressupostos e limitações. Ambos são modelos analíticos não executáveis, ainda sujeitos a validação com stakeholders.

## AS-IS hipotético

```mermaid
flowchart TD
  A[Lead entra via website / WhatsApp / Ads] --> B[Registo manual ou em canais separados]
  B --> C[Gestor verifica disponibilidade]
  C --> D{Consegue contactar?}
  D -- Não --> E[Follow-up manual sem rastreio consistente]
  E --> C
  D -- Sim --> F[Triagem e recolha de informação]
  F --> G[Pedido manual de documentos]
  G --> H{Documentação completa?}
  H -- Não --> G
  H -- Sim --> I[Conferência por humano]
  I --> J[Submissão a instituição financeira]
  J --> K[Decisão / comunicação por humano]
```

**Riscos a confirmar em entrevista:** duplicação de leads; responsabilidade indefinida; ausência de trilho de auditoria; pedidos de documentos redundantes; fontes de lead não reconciliadas.

## TO-BE proposto para piloto

```mermaid
flowchart TD
  A[Website / WhatsApp / Ads] --> B[Registo CRM e deduplicação]
  B --> C[Consentimento e atribuição de responsável]
  C --> D[Triagem assistida com revisão humana]
  D --> E[Checklist documental contextual]
  E --> F{Documentos válidos e completos?}
  F -- Não --> G[Notificação de pendências e novo prazo]
  G --> E
  F -- Sim --> H[Validação por profissional autorizado]
  H --> I[Submissão à instituição financeira]
  I --> J[Estado e comunicações auditáveis]
  J --> K[Fecho: financiado / perdido / ativo]
  K --> L[Dashboard com definições consistentes]
```

## Pontos de controlo
1. O chatbot não aprova crédito nem valida legalmente a documentação de forma autónoma.
2. Regras de recolha documental apenas após definição jurídica de finalidade, minimização, base legal e retenção.
3. O cliente deve poder falar com uma pessoa e contestar/corrigir dados.
4. Cada transição precisa de timestamp, responsável, origem e razão da alteração.
5. Integrações WhatsApp, webform e CRM necessitam autenticação, logging e tratamento de duplicados.

## O que medir antes e depois
- Tempo para primeiro contacto, qualificação e submissão.
- Percentagem de dossiês devolvidos por documentação incompleta.
- Número de interações manuais por processo.
- Taxa de qualificação e de financiamento com segmentos comparáveis.
- Incidentes, reclamações e erros no tratamento de dados.

## Lacunas por validar
Volumes reais, disponibilidade de integrações, requisitos regulamentares aplicáveis, custo de licenças, acessos e permissões, política de conservação documental.
