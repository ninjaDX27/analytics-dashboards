# BPMN 2.0 — Guia de modelação e validação (AS-IS / TO-BE)

> **Versão de portefólio, não modelo de produção**. Os fluxos são hipóteses sobre uma intermediária fictícia. Não representam processos validados da MaxFinance Top. As automatizações são propostas, não funcionalidades implementadas.

## Ficheiros editáveis
- [AS-IS — BPMN 2.0 XML](AS-IS.bpmn)
- [TO-BE — BPMN 2.0 XML](TO-BE.bpmn)

Os dois ficheiros incluem BPMN DI (posições das formas e ligações), 3 pools — **Cliente**, **Intermediário de crédito**, **Instituição financeira** — e swimlanes internas. A pool do cliente e a pool do banco são **black-box**: o processo detalhado é apenas o da intermediária.

## 1. Abrir no Camunda Modeler
1. Instalar **Camunda Desktop Modeler** a partir de https://camunda.com/download/modeler/ .
2. Abrir `AS-IS.bpmn` através de **File → Open File**.
3. Usar **Fit viewport** para visualizar o processo completo e depois aumentar o zoom.
4. Abrir `TO-BE.bpmn` e comparar decisões, lanes e tarefas.
5. Guardar as alterações em ficheiros separados para preservar o original.

Ambos estão com `isExecutable="false"`. **Um ficheiro BPMN editável não é uma automação funcional**: para executar seriam necessárias integrações, dados, decisões de negócio e propriedades específicas do motor escolhido.

## 2. A semântica que tens de dominar
| Símbolo | Significado | Exemplo |
|---|---|---|
| Pool | Participante independente | Cliente, intermediária, banco |
| Lane | Papel ou equipa no mesmo participante | Captação, CRM, crédito, gestão |
| Start Event | Início do caso de processo | Lead recebida |
| Task / User Task | Trabalho / trabalho por pessoa | Contactar, validar documento |
| Service Task | Sistema automatizado (proposto) | Registar lead no CRM |
| Send Task | Enviar comunicação | Pedido documental / submissão |
| Receive Task | Aguardar comunicação externa | Decisão bancária |
| Exclusive Gateway | Selecionar apenas um caminho | Documentação completa? |
| Boundary Timer (TO-BE) | Alerta não interruptivo após prazo | Alerta ilustrativo de 24 horas |
| End Event | Terminar uma instância / um ramo | Duplicado reconciliado / caso fechado |
| Sequence Flow | Ordem entre atividades no **mesmo pool** | Triage → checklist |
| Message Flow | Comunicação **entre pools diferentes** | Intermediária → banco |

**Regra crítica:** sequence flows podem cruzar lanes internas, mas não podem cruzar pools. Mensagens são fluxos distintos e não substituem a ordem interna do processo.

## 3. AS-IS — Passo a passo
1. Identifica o evento inicial **Pedido recebido** (mensagem enviada pelo Cliente).
2. Na lane Captação, identifica o registo manual.
3. Segue a distribuição interna para Operações e o contacto feito pelo Intermediário.
4. Percorre o gateway **Contactado?**. Se não, follow-up manual e nova avaliação; o número de tentativas tem de ser definido com stakeholders.
5. Depois da triagem, localiza o pedido de documentos e o gateway de completude.
6. Segue o ciclo de pedidos repetidos e a validação humana.
7. Localiza o envio do dossiê ao banco, a receção da resposta e a comunicação ao cliente.
8. Anota onde falta registo de estados, responsável, tempo e motivo de rejeição.

## 4. TO-BE — Passo a passo
1. Localiza **Lead recebida** e **Registar lead e origem no CRM**.
2. Repara que deteção automática de duplicados termina em **revisão por humano**, nunca em fusão autónoma irreversível.
3. Verifica atribuição de owner e o gate de privacidade antes de contactos e documentos.
4. Segue a tarefa de contacto, com **boundary timer não interruptivo** (24h ilustrativas; definição contratual ainda pendente). O alerta vai para a lane Gestão sem cancelar o contacto.
5. Segue a triagem com humano, checklist contextual e verificação documental.
6. Documentos pendentes geram notificação e voltam à conferência; inválidos voltam ao ciclo.
7. A validação final antes da submissão é humana.
8. O banco é pool externa: recebe dossiê e envia decisão; a intermediária regista o estado, comunica e atualiza métricas.

## 5. Distinção AS-IS ↔ TO-BE
| Eixo | AS-IS | TO-BE |
|---|---|---|
| Entrada | Registo manual | Registo centralizado no CRM |
| Duplicados | Não explicitamente controlados | Sinalização e revisão humana |
| Owner/SLA | Distribuição manual, sem tracking consistente | Atribuição rastreável e alerta de SLA |
| Documentos | Repetição manual | Checklist contextual e notificações |
| Decisão | Humana + banco | Continua humana + banco |
| Reporting | Sem etapa explícita | Atualização de métricas auditáveis |

## 6. Perguntas que deves fazer a stakeholders
- O que distingue uma lead nova de um contacto duplicado?
- Quem recebe a lead e quanto tempo máximo pode passar até ao primeiro contacto?
- Quantas tentativas de contacto são permitidas e em que canais?
- O que é uma lead "qualificada"? Quem valida?
- Que documentos são pedidos por perfil e quando são efetivamente necessários?
- Quem pode ver, descarregar ou apagar documentos?
- O que acontece quando não há resposta do banco / cliente?
- O que define o fim de um processo: decisão comunicada, escritura, cancelamento?
- Como o CRM mantém um histórico imutável de alterações e origem de dados?
- Quem aprova tratamento de dados, regras de retenção, WhatsApp e integrações?

## 7. Limitações que impedem produção
- O AS-IS ainda não foi observado no terreno, logo é **hipótese**, não constatação.
- Os ficheiros têm semântica BPMN e DI; não possuem serviços reais, API calls ou execução.
- Os gateways estão identificados por ramos Sim/Não, mas expressões de decisão executáveis não estão implementadas.
- Não modelámos todos os limites de tempo, erros, recusas, reapresentações, desvios ou escaladas.
- A pool bancária é black-box porque não controlamos o workflow da instituição.
- 24h é um parâmetro de treino, não SLA aprovado; atualizar depois da entrevista de stakeholders.
- As transições de estados precisam de regras de auditoria, autorização e tratamento de privacidade.

## 8. Exercício de Business Analyst
Entrega uma tabela `Problema | Evidência necessária | Requisito | Métrica | Critério de aceitação` para as três fricções prioritárias. Faz a ligação às FR-01…FR-07 do [BRD](../docs/03-requisitos.md) e apresenta uma versão de processo revista.

## Validações
Verificação inicial de coerência de IDs, referências de flows, lanes e presença de BPMN DI realizada no gerador. Executa também, a partir da pasta do case study, `python tests/test_bpmn.py` para validar XML, referências, gateways, pools e DI. **É indispensável abrir ambos os ficheiros num modelador BPMN e validar visualmente layout, fluxo e semântica antes de uma apresentação formal.**
