# 📊 PROGRESS.md - Rastreamento Semanal

**Atualize este arquivo toda semana.**

---

## 📅 Semana 1 (15-06-2026 a 20-06-2026)

### ✅ Completado
- [x] 4 notebooks NumPy criados (aula 1 a 4)
- [x] Aula 5 — Broadcasting
- [x] helper_functions.py com docstring profissional
- [x] Exercícios práticos resolvidos em todas as aulas
- [x] Desafio final — Análise de farmácias
- [x] Nomes dos arquivos corrigidos (removido espaço)
- [x] Markdown realizado nas aulas 1, 2, 3 e 4
- [x] Projeto de portfólio — Análise de Churn de filiais
- [x] README de fixação NumPy criado
- [x] PROGRESS.md criado e atualizado

### 📚 Aprendizados
1. Arrays NumPy são mais rápidos que listas Python por serem homogêneos e contíguos na memória
2. Boolean indexing substitui loops — `mascara = array > valor`
3. `axis=1` opera nas linhas, `axis=0` opera nas colunas
4. Scripts `.py` guardam funções reutilizáveis, notebooks `.ipynb` são para exploração
5. Células markdown no Jupyter separam explicação de código — padrão profissional
6. Broadcasting: `reshape(4, 1)` alinha operações por linha em matrizes
7. `[:, 0]` pega coluna, não linha — `array[LINHA, COLUNA]` é a regra

### 🔴 Bloqueios
- Confundi `[:, 0]` achando que pegava a linha do motoboy, mas pega a coluna inteira
- Solução: entendi que `array[LINHA, COLUNA]` — `[:, 0]` significa todas as linhas, coluna 0
- Broadcasting não clicou de primeira — solução: reshape de `(4,)` para `(4, 1)`
- Configuração do Git sem email — commits não apareciam no gráfico verde
- Solução: `git config --global user.email`

### 📈 Próxima semana
- [x] Terminar markdown nas aulas 2, 3 e 4
- [x] Commitar tudo com mensagem descritiva
- [x] NumPy 100% concluído
- [ ] Continuar Pandas — Series, DataFrames, `.loc` e `.iloc`

### 🔗 Commits
```
[SEMANA-1] feat: NumPy basics - 4 aulas + helper_functions
[SEMANA-1] feat: NumPy broadcasting - aula 5
[SEMANA-1] feat: desafio final NumPy - análise farmácias
[SEMANA-1] fix: corrigir célula aula3, import aula4, remover Untitled
[SEMANA-1] feat: projeto portfólio - análise churn filiais
[SEMANA-1] docs: README fixação completa NumPy
```

### ⏱️ Tempo gasto
- Estudo: 5h
- Prática: 5h
- **Total: 10h**

### 📌 Notas pessoais
Semana mais produtiva do que o esperado. NumPy fechado com 5 aulas, projeto integrador e desafio.
Errei axis e broadcasting na primeira tentativa mas entendi e corrigi sem ajuda.
Casa foi furtada durante a semana — perdi o notebook mas continuei estudando.
Configurei novo ambiente na máquina substituta sem travar.

---

## 📅 Semana 2 (22-06-2026 a 27-06-2026)

### ✅ Completado
- [x] Revisão de NumPy com aula complementar (linspace, ndim, size)
- [x] Pandas aula 1 — DataFrames, Series, `.loc` e `.iloc`
- [x] Markdown estruturado durante a codagem
- [x] Erro clássico documentado (SettingWithCopyWarning)
- [x] Distinção `iloc[0]` vs `iloc[0:1]` vs `iloc[0, :]` documentada

### 📚 Aprendizados
1. Series é uma única coluna com índice — DataFrame é um conjunto de Series
2. `.loc[linha, coluna]` busca pelo nome do rótulo
3. `.iloc[linha, coluna]` busca pela posição numérica
4. `iloc[0, :]` é mais explícito e profissional que `iloc[0:1]` em entrevistas
5. Para modificar dados selecionados, usar sempre `.loc` — evita SettingWithCopyWarning
6. `linspace` gera valores igualmente espaçados entre dois pontos

### 🔴 Bloqueios
- Ambiente virtual não existia na nova máquina após o furto
- Solução: recriado o venv com Python 3.11
- Python 3.14 tem bug com venv — usar sempre 3.11

### 📈 Próxima semana
- [ ] Pandas aula 2 — Leitura de arquivos CSV e Excel
- [ ] Pandas aula 3 — Limpeza de dados
- [ ] Atualizar PROGRESS.md

### 🔗 Commits
```
[SEMANA-2] feat: Pandas aula 1 - DataFrames, Series, loc e iloc
```

### ⏱️ Tempo gasto
- Estudo: 3h
- Prática: 2h
- **Total: 5h**

### 📌 Notas pessoais
Semana com intercorrências — furto, nova máquina, reconfiguração do ambiente.
Mesmo assim entregou aula 1 de Pandas com qualidade.
Documentar o erro dentro da própria aula virou padrão — boa evolução.

---

## 📅 Semana 3 (29-06-2026 a 04-07-2026)

*(Copie o template da semana anterior)*

---

## 📅 Semana 4

---

## 📅 Semana 5

---

## 📅 Semana 6

---

## 📅 Semana 7

---

## 📅 Semana 8

---

## 📊 Resumo Mensal (Mês 1)

### 📈 Progresso
- [ ] Fundamentos 50% completo
- [ ] Projetos iniciados

### 🎯 Metas alcançadas
1.
2.

### 🔴 Desafios
1.
2.

### 🚀 Ajustes para Mês 2
1.
2.

---

## 📊 Resumo Mensal (Mês 2)

---

## 📊 Resumo Mensal (Mês 3)

---

## 📊 Resumo Mensal (Mês 4)

---

## 📊 Resumo Mensal (Mês 5)

---

## 📊 Resumo Mensal (Mês 6)

---

## 🎓 Reflexão Final (Semana 24)

### ✅ Atingi meu objetivo?
- [ ] Sim
- [ ] Quase
- [ ] Não

### 📊 Estatísticas finais
- Total de commits:
- Total de horas investidas:
- Projetos completados: 3
- Notebooks criados:
- Linhas de código:

### 🏆 Maiores aprendizados
1.
2.
3.
4.
5.

### 💼 Pronto para trabalhar como Junior DS?
- [ ] Confiante
- [ ] Parcialmente
- [ ] Ainda não

### 🚀 Próximos passos
1.
2.
3.

---

**Mantenha este documento atualizado. Ele é seu portfólio de disciplina.**
