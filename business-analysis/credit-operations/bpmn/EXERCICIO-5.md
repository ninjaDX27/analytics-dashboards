# Exercício 5/5 — Validação paralela com IRS opcional

> Cenário fictício. Este ficheiro é um modelo conceptual BPMN 2.0, não executável. Não representa procedimentos da MaxFinance Top nem uma proposta de decisão de crédito automática.

Abrir [IRS-OPCIONAL.bpmn](IRS-OPCIONAL.bpmn) no Camunda Desktop Modeler ou no bpmn.io demo.

## Enunciado
Verificar identidade e rendimentos de todos os clientes em paralelo. Para trabalhadores independentes, realizar uma verificação documental adicional de IRS. Nenhum dossiê pode ser submetido enquanto houver verificações aplicáveis pendentes ou inválidas.

## Padrão correto
1. AND-Split cria dois tokens: identidade e rendimentos.
2. Identidade: verificação e registo do resultado (válido/inválido).
3. Rendimentos: verificação e registo; XOR pergunta se o cliente é trabalhador independente.
4. Se independente: verificar IRS e registar resultado; caso contrário saltar apenas a tarefa adicional.
5. XOR-Merge reúne os caminhos *alternativos* do ramo de rendimentos — passa um token.
6. AND-Join espera exatamente um token do ramo da identidade e outro do ramo de rendimentos.
7. Consolidar estados: verificação completa não significa aprovação.
8. XOR "Todas satisfatórias?": se sim, enviar dossiê ao banco; se não, rever falhas.
9. XOR "Falhas corrigíveis?": se não, encerrar sem submissão; se sim, solicitar correção e aguardar documentos.
10. Se houver nova documentação, recomeçar o bloco de verificações. Se o prazo de resposta expirar, um **boundary timer interruptivo** termina o pedido de correção e conduz a encerramento controlado. P5D é **apenas parâmetro didático**, não SLA contratual.

## Porque não existe deadlock estrutural no AND-Join
Os dois ramos paralelos têm sempre um caminho de retorno ao AND-Join após as verificações. A tarefa de IRS é opcional mas o respetivo XOR merge fica **antes** do AND join: o segundo token chega ao AND-Join, independentemente do tipo de trabalhador. Resultados negativos são registos de estado avaliados **depois** do AND-Join, em vez de terminar apenas um dos ramos obrigatórios.

## Pontos a validar em caso real
- Se a identificação do perfil está correta; documentação de IRS efetivamente exigível por tipo de processo e entidade.
- Como são obtidos e armazenados resultados: `identity_valid`, `income_valid`, `irs_valid`, `independent`.
- Quem pode aprovar ou rejeitar cada documento e o estado de "inconclusivo".
- Duração real e natureza (dias corridos/úteis) do prazo de resposta e política de encerramento.
- Como evitar recomeçar verificações desnecessariamente após uma pequena correção documental.
- Políticas de retenção, autorizações, logs e tratamento de dados financeiros.
- Como tratar indisponibilidade de verificadores; erros operacionais; abandono; retrabalho repetido.

## Limitações técnicas
Os Sequence Flows têm nomes que ilustram as condições, mas o XML não possui expressões executáveis. Mesmo sendo XML BPMN 2.0 com BPMN DI, **não deve ser implantado num motor BPMN**. É necessário validar a apresentação visual, semântica e os caminhos de exceção com um modelador e stakeholders.

Fontes:
- https://www.omg.org/spec/BPMN/2.0.2/
- https://docs.camunda.io/docs/components/modeler/bpmn/parallel-gateways/
- https://docs.camunda.io/docs/components/modeler/bpmn/exclusive-gateways/
