# Workflow Financeiro

## 1. O Raio-X
- Leia os arquivos: `receitas.csv`, `Controle Gastos Fixos.csv` e `Controle Entrada Financiamento.csv`.
- Some todas as Receitas e todas as Despesas.
- Apresente o Saldo Líquido do mês.

## 2. A Bola de Neve (Projeção Futura)
Use a fórmula: `M = C * (1 + i)^n`
- **C**: Valor da dívida atual (ex: fatura do cartão, saldo negativo).
- **i**: Taxa de juros mensal (ex: 0.08 para cheque especial, 0.12 para cartão).
- **n**: Meses de projeção (padrão 3).
Mostre uma tabela Markdown com a evolução mês a mês. Explique quanto o usuário vai pagar de juros se não abater o principal.

## 3. O que pagar primeiro?
Se o usuário tiver um valor `X` sobrando:
1. Priorize contas com multas/contratos (ex: Entrada do financiamento).
2. Depois, a maior taxa de juros (geralmente o cartão de crédito).
3. Por último, o cheque especial.
Explique o "custo de oportunidade" de cada escolha.