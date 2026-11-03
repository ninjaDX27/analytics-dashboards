# 05 — Business case e decisão de piloto

## Alternativas de decisão
A. Manter processo atual e reforçar normas / formação;
B. Implementar piloto CRM + checklist + alertas com supervisão humana;
C. Automatização abrangente multicanal (não recomendada antes de dados e testes de B).

## Cálculo (modelo, não resultado real)
- **Custo inicial:** configuração + integrações + migração + formação + segurança.
- **Custo recorrente:** licenças + operações + manutenção + auditorias.
- **Benefício operacional anual (€):** (minutos manuais poupados por processo / 60) × volume anual × custo/hora totalmente carregado × taxa de adoção.
- **Benefício comercial incremental (€):** processos financiados adicionais atribuíveis ao piloto × margem de contribuição por processo, **não** volume de financiamento.
- **Benefício líquido anual:** benefícios operacionais + incrementais − custos recorrentes.
- **Payback (meses):** 12 × custo inicial / benefício líquido anual, apenas se benefício líquido > 0.

## Exemplo aritmético estritamente hipotético
100 processos/mês × 20 minutos poupados × 12 meses / 60 = 400 horas anuais.
A 15 €/hora carregados = 6 000 € anuais brutos em capacidade potencial.
**Não equivale automaticamente a poupança de caixa:** o tempo poupado pode ser absorvido noutras atividades, e o modelo não inclui licenças, implementação ou adoção.

## Métricas de avaliação do piloto
Primary: mediana do tempo desde criação até submissão na mesma definição de coorte.
Secondary: retrabalho documental, SLA 24h, lead-to-funded rate, satisfação de operador.
Guardrails: erros documentais, acessos indevidos, reclamações, falhas de integração.

## Desenho de avaliação
Medir baseline; aplicar piloto a uma equipa ou segmento comparável; assegurar consistência de registos, sazonalidade e mix de canais; rever quinzenalmente; registar custos reais. Sem grupo ou ajuste adequado, não atribuir causalmente variações ao software.

## Go / no-go
Só avançar após: processo TO-BE aceite; validação legal/privacidade; contrato e segurança técnica revistos; orçamento aprovado; owner e plano de apoio definidos; indicadores baseline confiáveis. **Não há decisão de investimento justificável baseada apenas nos 40 registos sintéticos.**
