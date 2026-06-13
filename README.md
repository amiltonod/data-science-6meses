# Data Science: Zero → Junior em 6 Meses 📊

**Status atual:** ⏳ Em andamento | **Data de início:** [15/06/2026] | **Meta:** [15/12/2026 + 6 meses]

> Um repositório público documentando minha jornada de **zero experiência** em Data Science até **capacidade Junior**, com projetos práticos, aprendizados e código testado.

---

## 📋 Visão Geral do Roadmap

```
MESES 1-2: FUNDAMENTOS   → Python, Estatística, SQL
MESES 2-3: FERRAMENTAS   → ML, EDA, Análise aplicada  
MESES 3-5: PROJETOS      → 3 Projetos reais com dados
MESES 5-6: PORTFÓLIO     → Deploy, documentação, entrevistas
```

**Por que este repositório existe:**
- 🎯 Accountability pública
- 📈 Rastrear progresso semanal
- 🏆 Portfólio vivo que demonstra conhecimento
- 📚 Documentação clara de cada aprendizado
- 🔗 Prova de que "eu sei o que estou fazendo"

---

## 📍 Estrutura do Repositório

```
data-science-6meses/
│
├── README.md                          (Este arquivo)
├── ROADMAP.md                         (Cronograma detalhado)
├── PROGRESS.md                        (Atualizações semanais)
│
├── 01-FUNDAMENTOS/                    (Mês 1-2)
│   ├── 01-python-numpy-pandas/
│   │   ├── notebooks/
│   │   │   ├── 01-numpy-basico.ipynb
│   │   │   ├── 02-pandas-series.ipynb
│   │   │   ├── 03-pandas-dataframes.ipynb
│   │   │   └── 04-limpeza-dados.ipynb
│   │   ├── scripts/
│   │   │   └── helper_functions.py
│   │   └── README.md
│   │
│   ├── 02-matematica-estatistica/
│   │   ├── notebooks/
│   │   │   ├── 01-distribuicoes.ipynb
│   │   │   ├── 02-teste-hipoteses.ipynb
│   │   │   ├── 03-correlacao.ipynb
│   │   │   └── 04-probabilidade.ipynb
│   │   └── README.md
│   │
│   └── 03-sql-intermediario/
│       ├── queries/
│       │   ├── 01-joins.sql
│       │   ├── 02-agregacoes.sql
│       │   └── 03-otimizacao.sql
│       ├── databases/
│       │   └── examples.db
│       └── README.md
│
├── 02-FERRAMENTAS/                    (Mês 2-3)
│   ├── 01-machine-learning/
│   │   ├── notebooks/
│   │   │   ├── 01-regressao-linear.ipynb
│   │   │   ├── 02-regressao-logistica.ipynb
│   │   │   ├── 03-arvores-decisao.ipynb
│   │   │   └── 04-ensemble.ipynb
│   │   └── README.md
│   │
│   ├── 02-eda-visualizacao/
│   │   ├── notebooks/
│   │   │   ├── 01-eda-completa.ipynb
│   │   │   ├── 02-matplotlib-seaborn.ipynb
│   │   │   └── 03-dashboards.ipynb
│   │   └── README.md
│   │
│   └── 03-estatistica-aplicada/
│       ├── notebooks/
│       │   ├── 01-analise-dados-reais.ipynb
│       │   └── 02-metricas-modelo.ipynb
│       └── README.md
│
├── 03-PROJETOS/                       (Mês 3-5)
│   ├── projeto-01-imoveis/
│   │   ├── data/
│   │   │   ├── raw/
│   │   │   ├── processed/
│   │   │   └── README.md
│   │   ├── notebooks/
│   │   │   ├── 01-eda.ipynb
│   │   │   ├── 02-preprocessamento.ipynb
│   │   │   ├── 03-modelo.ipynb
│   │   │   └── 04-resultados.ipynb
│   │   ├── src/
│   │   │   ├── data_loader.py
│   │   │   ├── preprocessor.py
│   │   │   ├── model.py
│   │   │   └── utils.py
│   │   ├── relatorio.md
│   │   └── README.md
│   │
│   ├── projeto-02-credito/
│   │   ├── (mesma estrutura acima)
│   │   └── README.md
│   │
│   └── projeto-03-series-temporais/
│       ├── (mesma estrutura acima)
│       └── README.md
│
├── 04-PORTFOLIO/                      (Mês 5-6)
│   ├── streamlit-app/
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   └── pages/
│   │       ├── projeto1.py
│   │       ├── projeto2.py
│   │       └── projeto3.py
│   │
│   ├── apresentacoes/
│   │   ├── COMO-EXPLICAR-PROJETOS.md
│   │   └── PERGUNTAS-FREQUENTES.md
│   │
│   └── deploy/
│       ├── deployment.md
│       └── docker/
│
├── resources/
│   ├── cursos-recomendados.md
│   ├── artigos-importantes.md
│   └── datasets-usados.md
│
├── APRENDIZADOS.md                    (Insights principais)
├── requirements.txt                   (Dependências Python)
├── environment.yml                    (Conda environment)
└── .gitignore
```

---

## 📅 Cronograma Detalhado (6 Meses)

### **MESES 1-2: FUNDAMENTOS** ⚙️

**Objetivo:** Dominar Python para Data Science + Matemática base

| Semana | Tópico | Deliverable | Status |
|--------|--------|-------------|--------|
| 1-2 | NumPy: Arrays, operações, broadcasting | 3 notebooks + 1 script | ⬜ |
| 2-3 | Pandas: Series, DataFrames, indexing | 4 notebooks com datasets reais | ⬜ |
| 3-4 | Limpeza de dados: tratamento de NaN, duplicatas | Projeto prático em notebook | ⬜ |
| 4-5 | Estatística: Média, desvio padrão, distribuições | 3 notebooks + exercícios | ⬜ |
| 5-6 | Testes de hipóteses e probabilidade | 2 notebooks + 1 relatório | ⬜ |
| 6-7 | SQL avançado: JOINs, GROUPs, subconsultas | 10+ queries documentadas | ⬜ |
| 7-8 | Revisão integrada + Mini-projeto | 1 análise de dataset completa | ⬜ |

**Recursos:**
- 📚 "Introduction to Statistical Learning" (Cap 1-3)
- 🎥 StatQuest (YouTube): Normal distribution, hypothesis testing
- 🔗 Official docs: NumPy, Pandas, SQLite

---

### **MESES 2-3: FERRAMENTAS** 🔧

**Objetivo:** Aprender Machine Learning frameworks e Análise Exploratória

| Semana | Tópico | Deliverable | Status |
|--------|--------|-------------|--------|
| 8-9 | Scikit-learn: Pipeline, model selection | 2 notebooks + 1 script | ⬜ |
| 9-10 | Regressão linear: Teoria + implementação | Notebook com 5 datasets | ⬜ |
| 10-11 | Classificação: Logística, árvores de decisão | 3 notebooks + comparações | ⬜ |
| 11-12 | Ensemble: Random Forest, Gradient Boosting | 2 notebooks + benchmark | ⬜ |
| 12-13 | EDA completa: Matplotlib + Seaborn | Dashboard em 2 datasets | ⬜ |
| 13-14 | Métricas e validação cruzada | Relatório técnico | ⬜ |

**Recursos:**
- 📚 "Hands-On Machine Learning" (Cap 1-6)
- 🎥 Andrew Ng ML Course (Coursera)
- 📊 Kaggle Learn: Intro to ML

---

### **MESES 3-5: PROJETOS PRÁTICOS** 🚀

**Objetivo:** 3 projetos reais que demonstram competência

#### **Projeto 1: Previsão de Preços (Regressão)**
- **Dataset:** Housing prices
- **Tarefas:** EDA → Preprocessamento → Modelo → Avaliação
- **Métricas:** MSE, RMSE, R²
- **Duração:** 3 semanas
- **Entregáveis:** Código + Notebook + Relatório

#### **Projeto 2: Classificação Risco de Crédito**
- **Dataset:** Credit card default
- **Tarefas:** Balanceamento → Feature engineering → Classificação
- **Métricas:** ROC-AUC, Precision, Recall
- **Duração:** 3 semanas
- **Entregáveis:** Código + Notebook + Análise de importância

#### **Projeto 3: Análise Real (Sua Empresa)**
- **Dataset:** Dados de coleta Almeida Ambiental (você!)
- **Tarefas:** Análise temporal → Otimização de rotas → Previsão de demanda
- **Métricas:** KPIs operacionais
- **Duração:** 4 semanas
- **Entregáveis:** Código + Notebook + Recomendações para negócio

---

### **MESES 5-6: PORTFOLIO + DEPLOY** 🎯

**Objetivo:** Apresentar publicamente como Junior DS pronto para trabalhar

| Semana | Tarefa | Entregável |
|--------|--------|-----------|
| 20-21 | Criar Streamlit app com 3 projetos | App rodando em Streamlit Cloud |
| 21-22 | Documentar explicações técnicas | COMO-EXPLICAR-PROJETOS.md |
| 22-23 | Deploy em produção | URL pública funcional |
| 23-24 | Criar "Sobre mim" + LinkedIn update | Perfil atualizado + GitHub star |

---

## 🎯 Critérios de Sucesso (Junior DS)

Você será considerado **Junior em Data Science** quando:

- [ ] **Fundamentos** ✅
  - [ ] Código Python limpo, modular, documentado
  - [ ] Entende NumPy/Pandas até nível intermediário
  - [ ] Escreve SQL complex sem ajuda

- [ ] **Machine Learning** ✅
  - [ ] Sabe quando usar regressão vs classificação
  - [ ] Implementa modelo sem copiar-colar
  - [ ] Entende overfitting, underfitting, trade-offs
  - [ ] Escolhe métricas apropriadas

- [ ] **Projetos** ✅
  - [ ] 3 projetos no GitHub com dados reais
  - [ ] Cada um tem: dados, código, notebook, relatório
  - [ ] Explica resultados em linguagem não-técnica

- [ ] **Comunicação** ✅
  - [ ] README claro para cada projeto
  - [ ] Notebook bem estruturado com markdown
  - [ ] Consegue explicar seu trabalho em 5 minutos

- [ ] **Portfolio** ✅
  - [ ] Website/Streamlit app mostrando trabalho
  - [ ] GitHub com commits frequentes
  - [ ] LinkedIn com recomendações técnicas

---

## 📊 Tracking de Progresso

**Atualize este documento toda semana (PROGRESS.md):**

```markdown
## Semana X (Data: X - Y)

### ✅ Completado
- [ ] Tópico A
- [ ] Tópico B
- [ ] Entregável

### 📚 Aprendizados principais
- Insight 1
- Insight 2

### 🔴 Bloqueios
- Problema 1
- Solução aplicada

### 📈 Próxima semana
- [ ] Tópico seguinte
```

---

## 🛠️ Como Usar Este Repositório

### 1️⃣ **Clonar e Configurar**
```bash
git clone https://github.com/[seu-usuario]/data-science-6meses
cd data-science-6meses
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

### 2️⃣ **Estrutura de Commits**
```
[SEMANA-X] TOPICO: Descrição curta

feat: Adicionar notebook de NumPy
refactor: Reorganizar estrutura de pastas
docs: Atualizar README do projeto 1
fix: Corrigir lógica de preprocessamento
```

### 3️⃣ **Documentação no Notebook**
Cada notebook deve ter:
- Título + data
- Objetivo claro
- Seções bem marcadas
- Explicações em markdown
- Código comentado
- Conclusões

---

## 📚 Recursos Essenciais

### **Cursos**
- 🎥 [StatQuest with Josh Starmer](https://www.youtube.com/@statquest) - Estatística visual
- 📖 [Andrew Ng - Machine Learning](https://www.coursera.org/learn/machine-learning)
- 🔗 [Kaggle Learn Micro-Courses](https://kaggle.com/learn)

### **Livros**
- "Introduction to Statistical Learning" (ISLR) - Gratuito online
- "Hands-On Machine Learning" - O'Reilly
- "Data Science from Scratch" - Joel Grus

### **Prática**
- 🏆 [Kaggle Competitions](https://kaggle.com) - Projetos reais
- 📊 [UCI ML Repository](https://archive.ics.uci.edu/) - Datasets clássicos
- 🔗 [Awesome DS](https://github.com/academic/awesome-datascience)

---

## 🎓 Aprendizados Principais

*Será atualizado conforme você avança. Documento separado: APRENDIZADOS.md*

Exemplos:
- "Normalização de dados importa MUITO mais do que imaginava"
- "Feature engineering resolve 70% do problema"
- "A métrica certa muda tudo"
- "Documentação economiza 10 horas depois"

---

## 💼 Como Apresentar Isso em Entrevistas

**Você dirá:**

> "Eu segui um roadmap público de 6 meses que documentei integralmente no GitHub. Passei pelos fundamentos (Python, SQL, Estatística), apendi ferramentas (Scikit-learn, Pandas), construí 3 projetos práticos com dados reais, e publiquei tudo. Cada projeto tem dados, código testado, notebook com explicações e relatório. Posso mostrar."

**O que diferencia:**
- ✅ Você planejou, não foi à deriva
- ✅ Documentou publicamente (não é fake)
- ✅ Completou estrutura clara
- ✅ Pode explicar cada parte

---

## 📞 Contato & Atualizações

**LinkedIn:** [https://www.linkedin.com/in/amilton-carvalho-junior-047b5895/]  
**GitHub:** [https://github.com/amiltonod]  
**Email:** [amilton.od@gmail.com]

---

## 📄 Licença

Este repositório é público e pode servir como template para outros aprendizes. MIT License.

---

**Última atualização:** [Data]  
**Próxima revisão:** [Data + 1 semana]

---

## 🚀 Comece Agora

1. Crie o repositório no GitHub
2. Clone estrutura de pastas acima
3. Comece com `01-FUNDAMENTOS/01-python-numpy-pandas`
4. Estude 1-2 horas/dia durante 6 meses
5. Commit **todo dia**, ainda que pequeno
6. Atualize PROGRESS.md toda semana
7. Construa portfólio aos poucos

**Você tem tudo o que precisa. Agora é execução.**
