# ROADMAP DETALHADO: Data Science 6 Meses 🗺️

**Seu plano de ação semana a semana, com recursos específicos, conceitos-chave e entregas.**

---

## 🎯 Filosofia

- **Aprendizado em cascata:** Cada semana depende da anterior
- **Prática + Teoria:** Não só vídeos, código funcionando
- **Público accountability:** Você faz commit toda semana
- **Projetos reais:** Datasets que você entende (Almeida Ambiental no final)

---

# 📅 MESES 1-2: FUNDAMENTOS ⚙️

## **SEMANA 1-2: Python NumPy**

**Objetivo:** Entender arrays multidimensionais, operações vetorizadas, broadcasting

### 📚 O que estudar

| Conceito | Recurso | Tempo |
|----------|---------|-------|
| NumPy basics | [NumPy official tutorial](https://numpy.org/doc/stable/user/absolute_beginners.html) | 3h |
| Arrays & indexing | [W3Schools NumPy](https://www.w3schools.com/python/numpy/) | 2h |
| Broadcasting | [NumPy broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html) + vídeo | 2h |
| Linear Algebra | [StatQuest: Dot products](https://www.youtube.com/watch?v=KuXjwB4LzSA) | 1h |

### 🔑 Conceitos-chave
- `np.array()` vs lists
- `shape`, `dtype`, `reshape`
- Indexing: slicing, fancy indexing, boolean indexing
- Broadcasting rules
- `dot()`, `@`, matriz operations
- `linspace`, `arange`, `ones`, `zeros`, `eye`

### 💻 Código que você vai escrever

```python
# Exemplo 1: Criar e manipular arrays
import numpy as np

# Arrays
arr = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Operações
result = arr * 2
sum_by_row = matrix.sum(axis=0)

# Broadcasting
broadcasted = arr + np.array([[1], [2], [3]])

# Linear algebra
vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])
dot_product = np.dot(vec1, vec2)
```

### 📋 Entregável

**Notebook: `01-FUNDAMENTOS/01-python-numpy-pandas/notebooks/01-numpy-basico.ipynb`**

```markdown
# NumPy Básico

## 1. Criar arrays
## 2. Indexing e slicing
## 3. Operações matemáticas
## 4. Broadcasting
## 5. Álgebra linear
## Conclusões
```

**+ Script: `01-FUNDAMENTOS/01-python-numpy-pandas/scripts/numpy_helpers.py`**
- Funções reutilizáveis
- Bem comentadas
- Com docstrings

### 🏁 Checkpoint
- [ ] Escrever array 3D, acessar elemento específico
- [ ] Fazer broadcast sem erros
- [ ] Multiplicar matrizes 2x3 * 3x4
- [ ] Commit no GitHub com mensagem: `[SEMANA-1] feat: NumPy fundamentos`

---

## **SEMANA 2-3: Pandas Series e DataFrames**

**Objetivo:** Trabalhar com dados tabulares, limpeza básica

### 📚 O que estudar

| Conceito | Recurso | Tempo |
|----------|---------|-------|
| Pandas Series | [Real Python: Pandas Series](https://realpython.com/pandas-series/) | 2h |
| DataFrames | [Pandas official: Getting Started](https://pandas.pydata.org/docs/getting_started/index.html) | 3h |
| Indexing/Seleção | [Pandas indexing](https://pandas.pydata.org/docs/user_guide/indexing.html) | 2h |
| Métodos úteis | [Kaggle Learn: Pandas](https://kaggle.com/learn/pandas) | 2h |

### 🔑 Conceitos-chave
- Series: 1D labeled arrays
- DataFrames: 2D estruturados
- `.loc[]`, `.iloc[]`, `.at[]`, `.iat[]`
- `head()`, `tail()`, `info()`, `describe()`
- Filtros booleanos
- `.groupby()`, `.agg()`, `.apply()`
- Merge/Join
- `.fillna()`, `.drop_duplicates()`

### 💻 Código que você vai escrever

```python
import pandas as pd
import numpy as np

# Series
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s['a'])  # 10

# DataFrame
df = pd.DataFrame({
    'Nome': ['Alice', 'Bob', 'Carol'],
    'Idade': [25, 30, 28],
    'Cidade': ['SP', 'RJ', 'MG']
})

# Seleção
print(df['Nome'])  # Series
print(df[['Nome', 'Idade']])  # DataFrame
print(df.loc[0])  # Row 0

# Filtro
maiores = df[df['Idade'] > 27]

# GroupBy
por_cidade = df.groupby('Cidade')['Idade'].mean()

# Limpeza
df_clean = df.fillna(0).drop_duplicates()
```

### 📋 Entregável

**Notebook: `02-pandas-series.ipynb` + `03-pandas-dataframes.ipynb`**

Cada notebook com:
- 10+ exemplos práticos
- Datasets reais (Kaggle: titanic, flights)
- Exercícios resolvidos

### 🏁 Checkpoint
- [ ] Criar DataFrame com 5 colunas de tipos diferentes
- [ ] Fazer filtro complexo (múltiplas condições)
- [ ] GroupBy + Agg em uma coluna
- [ ] Commit: `[SEMANA-2-3] feat: Pandas Series e DataFrames`

---

## **SEMANA 3-4: Limpeza de Dados**

**Objetivo:** Lidar com dados reais e sujos

### 📚 O que estudar

| Conceito | Recurso | Tempo |
|----------|---------|-------|
| Valores faltantes | [Pandas missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html) | 2h |
| Duplicatas | [Pandas drop_duplicates](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html) | 1h |
| Outliers | [StatQuest: Outliers](https://www.youtube.com/watch?v=DxnMaZ3QH70) | 1.5h |
| Feature engineering | Real Python article | 2h |
| Data validation | Próprio código | 2h |

### 🔑 Conceitos-chave
- `isnull()`, `notna()` pattern
- Imputação: média, mediana, forward fill
- Detecção de duplicatas
- Z-score e IQR para outliers
- Type conversion: `astype()`
- String operations: `.str` accessor
- Normalization: min-max, z-score

### 💻 Código que você vai escrever

```python
import pandas as pd
import numpy as np

# Dataset com problemas
df = pd.DataFrame({
    'id': [1, 2, 2, 4],  # duplicata
    'valor': [100, None, 300, 50],  # faltante
    'categoria': ['A', 'B', 'A', 'C'],
    'data': ['2024-01-01', '2024-01-02', 'invalid', '2024-01-04']
})

# Faltantes
print(df.isnull().sum())
df_filled = df.fillna(df['valor'].mean())

# Duplicatas
df_unique = df.drop_duplicates()

# Outliers (Z-score)
from scipy import stats
z_scores = np.abs(stats.zscore(df['valor'].dropna()))
df_no_outliers = df[z_scores < 3]

# Type conversion
df['data'] = pd.to_datetime(df['data'], errors='coerce')

# String clean
df['categoria'] = df['categoria'].str.strip().str.lower()
```

### 📋 Entregável

**Notebook: `04-limpeza-dados.ipynb`**

Com dataset real sujo que você arruma:
- Identificar problemas
- Documentar decisões
- Mostrar antes/depois

**Script: `helper_functions.py`**
```python
def limpar_dataframe(df, config=None):
    """Limpa um DataFrame seguindo padrão"""
    # Seu código aqui
    pass
```

### 🏁 Checkpoint
- [ ] Receber dataset com 10 problemas diferentes
- [ ] Limpar sem perder info importante
- [ ] Documentar cada decisão
- [ ] Commit: `[SEMANA-3-4] feat: Data cleaning pipeline`

---

## **SEMANA 4-5: Estatística Descritiva**

**Objetivo:** Entender dados através de estatística

### 📚 O que estudar

| Conceito | Recurso | Tempo |
|----------|---------|-------|
| Medidas centrais | [StatQuest: Mean, Median, Mode](https://www.youtube.com/watch?v=kzt3QzAIU10) | 1h |
| Variação | [StatQuest: Variance & SD](https://www.youtube.com/watch?v=E4HAYd0QnRs) | 1.5h |
| Distribuições | [StatQuest: Normal Distribution](https://www.youtube.com/watch?v=Kjy94ZxvqGw) | 2h |
| Correlação | [Pearson Correlation](https://realpython.com/numpy-scipy-pandas-correlation/) | 1.5h |
| Visualização | Matplotlib básico | 2h |

### 🔑 Conceitos-chave
- Média, mediana, moda, quartis
- Variância, desvio padrão, IQR
- Distribuição normal
- Skewness e Kurtosis
- Correlação de Pearson, Spearman
- `.describe()`, `.quantile()`, `.std()`

### 💻 Código que você vai escrever

```python
import pandas as pd
import numpy as np
from scipy import stats

# Dataset
data = np.random.normal(loc=100, scale=15, size=1000)
df = pd.DataFrame({'valores': data})

# Estatísticas descritivas
print(df['valores'].describe())
print(df['valores'].mean())
print(df['valores'].std())

# Distribuição
from scipy.stats import norm
pdf = norm.pdf(np.linspace(70, 130, 100), 100, 15)

# Correlação
df['x'] = np.random.randn(100)
df['y'] = df['x'] * 2 + np.random.randn(100)
corr = df['x'].corr(df['y'])
print(f"Correlação: {corr:.3f}")

# Teste de normalidade
stat, p_value = stats.shapiro(df['valores'])
```

### 📋 Entregável

**Notebook: `02-matematica-estatistica/notebooks/01-distribuicoes.ipynb`**

Com análise completa de 3 datasets:
- Histogramas
- Box plots
- Estatísticas
- Interpretação

### 🏁 Checkpoint
- [ ] Calcular todos os quartis manualmente
- [ ] Identificar distribuição (normal vs skewed)
- [ ] Correlação entre 2 variáveis
- [ ] Commit: `[SEMANA-4-5] feat: Estatística descritiva`

---

## **SEMANA 5-6: Testes de Hipóteses**

**Objetivo:** Validar dados estatisticamente

### 📚 O que estudar

| Conceito | Recurso | Tempo |
|----------|---------|-------|
| Hipóteses | [StatQuest: Hypothesis Testing](https://www.youtube.com/watch?v=0oDwFwJ4Ajc) | 1.5h |
| P-value | [StatQuest: P-value](https://www.youtube.com/watch?v=vemZtEM63GY) | 1.5h |
| T-test | [StatQuest: T-test](https://www.youtube.com/watch?v=NF5_btOaCig) | 2h |
| Chi-square | [Chi-square test](https://realpython.com/chi-square-test/) | 1.5h |

### 🔑 Conceitos-chave
- H0 (null hypothesis) vs H1 (alternative)
- P-value < 0.05 significativo
- T-test (1 sample, 2 samples, paired)
- Chi-square para categorias
- ANOVA para múltiplos grupos
- Type I vs Type II error

### 💻 Código que você vai escrever

```python
from scipy import stats

# 1-sample t-test: média é diferente de 100?
data = np.random.normal(105, 15, 100)
t_stat, p_value = stats.ttest_1samp(data, 100)
print(f"P-value: {p_value:.4f}")
if p_value < 0.05:
    print("Rejeitamos H0: Média é diferente de 100")

# 2-sample t-test: dois grupos são diferentes?
group1 = np.random.normal(100, 15, 50)
group2 = np.random.normal(105, 15, 50)
t_stat, p_value = stats.ttest_ind(group1, group2)

# Chi-square: categorias relacionadas?
from scipy.stats import chi2_contingency
contingency = np.array([[10, 20], [30, 40]])
chi2, p, dof, expected = chi2_contingency(contingency)
```

### 📋 Entregável

**Notebook: `02-teste-hipoteses.ipynb`**

Com 5 exemplos reais:
- Teste cada tipo
- Explique H0 e H1
- Interprete p-value

### 🏁 Checkpoint
- [ ] Fazer 1-sample, 2-sample e chi-square test
- [ ] Entender quando rejeitar H0
- [ ] Commit: `[SEMANA-5-6] feat: Testes de hipóteses`

---

## **SEMANA 6-7: SQL Intermediário**

**Objetivo:** Query dados eficientemente

### 📚 O que estudar

| Conceito | Recurso | Tempo |
|----------|---------|-------|
| JOINs | [Mode Analytics: SQL JOINs](https://mode.com/sql-tutorial/sql-joins/) | 2h |
| GROUP BY | [Mode Analytics: Aggregations](https://mode.com/sql-tutorial/sql-aggregate-functions/) | 1.5h |
| Subqueries | [W3Schools: Subqueries](https://www.w3schools.com/sql/sql_sub_select.asp) | 1.5h |
| Window functions | [PostgreSQL window functions](https://www.postgresql.org/docs/current/functions-window.html) | 2h |
| Otimização | [Query optimization basics](https://mode.com/blog/sql-tutorial/) | 2h |

### 🔑 Conceitos-chave
- `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL OUTER JOIN`
- `GROUP BY`, `HAVING`, `ORDER BY`
- Aggregate functions: `SUM`, `COUNT`, `AVG`, `MAX`, `MIN`
- `DISTINCT`, `LIMIT`
- Subqueries vs CTEs (WITH)
- Window functions: `ROW_NUMBER()`, `RANK()`, `LAG()`, `LEAD()`

### 💻 Código que você vai escrever

```sql
-- Dataset: clientes, pedidos, produtos

-- INNER JOIN
SELECT c.nome, COUNT(p.id) as num_pedidos
FROM clientes c
INNER JOIN pedidos p ON c.id = p.cliente_id
GROUP BY c.id, c.nome;

-- Subquery
SELECT nome, quantidade
FROM pedidos
WHERE quantidade > (SELECT AVG(quantidade) FROM pedidos);

-- Window function
SELECT 
    id, 
    valor,
    ROW_NUMBER() OVER (ORDER BY valor DESC) as rank
FROM pedidos;

-- CTE (Common Table Expression)
WITH pedidos_grandes AS (
    SELECT * FROM pedidos WHERE valor > 1000
)
SELECT cliente_id, COUNT(*) FROM pedidos_grandes
GROUP BY cliente_id;
```

### 📋 Entregável

**Pasta: `03-sql-intermediario/queries/`**

10+ queries:
- `01-joins.sql` (5 queries com JOINs diferentes)
- `02-agregacoes.sql` (5 queries GROUP BY + HAVING)
- `03-otimizacao.sql` (5 queries otimizadas)

**+ Banco de dados de exemplo: `examples.db`**

### 🏁 Checkpoint
- [ ] Fazer JOIN com 3+ tabelas
- [ ] Subquery com agregação
- [ ] Window function
- [ ] Commit: `[SEMANA-6-7] feat: SQL intermediário`

---

## **SEMANA 7-8: Revisão + Mini-Projeto Integrado**

**Objetivo:** Consolidar tudo e fazer 1ª análise real

### 📚 O que fazer

1. **Revisar** conceitos de semanas anteriores (2h)
2. **Integração:** Escolher 1 dataset e fazer análise completa:
   - Carregar com Pandas
   - Limpar dados
   - Análise estatística
   - Visualizações
   - Conclusões

### 📋 Entregável

**Notebook: `01-FUNDAMENTOS/Mini-Projeto-Integrado.ipynb`**

Estrutura:
```markdown
# Análise de [Dataset]

## 1. Carregar dados (Pandas + NumPy)
## 2. EDA (Estatística descritiva)
## 3. Limpeza (tratamento de faltantes, outliers)
## 4. Visualizações (Matplotlib/Seaborn)
## 5. Insights e conclusões

### Arquivo: dados/dataset.csv
```

**Dataset sugerido:** 
- [Iris](https://archive.ics.uci.edu/ml/datasets/iris)
- [Tips dataset](https://github.com/mwaskom/seaborn-data)
- [Brazil flights](https://www.kaggle.com/datasets)

### 🏁 Checkpoint
- [ ] Análise completa de início ao fim
- [ ] Visualizações claras
- [ ] Commit: `[SEMANA-7-8] feat: Mini-projeto integrado - Análise [Dataset]`

---

# 📅 MESES 2-3: FERRAMENTAS 🔧

## **SEMANA 8-9: Scikit-learn Foundations**

**Objetivo:** Aprender framework ML padrão

### 📚 O que estudar

| Conceito | Recurso | Tempo |
|----------|---------|-------|
| Pipeline | [Scikit-learn Pipeline](https://scikit-learn.org/stable/modules/compose.html) | 2h |
| Escalamento | [Scikit-learn Preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html) | 1.5h |
| Train/Test Split | [Scikit-learn model selection](https://scikit-learn.org/stable/modules/cross_validation.html) | 1.5h |
| Validação cruzada | [Cross-validation tutorial](https://scikit-learn.org/stable/modules/model_evaluation.html) | 1.5h |

### 🔑 Conceitos-chave
- `Pipeline`: sequência de transformações + modelo
- `StandardScaler`, `MinMaxScaler`
- `train_test_split()` 80/20
- `cross_val_score()`
- `GridSearchCV`, `RandomizedSearchCV`
- Métricas: `accuracy`, `precision`, `recall`, `f1`

### 💻 Código que você vai escrever

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score

# Carregar dados
X = dados[['feature1', 'feature2', 'feature3']]
y = dados['target']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])

# Treinar
pipeline.fit(X_train, y_train)

# Avaliar
y_pred = pipeline.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.3f}")

# Cross-validation
scores = cross_val_score(pipeline, X, y, cv=5)
print(f"CV Scores: {scores.mean():.3f} (+/- {scores.std():.3f})")
```

### 📋 Entregável

**Notebook: `02-FERRAMENTAS/01-machine-learning/notebooks/01-scikit-learn-basico.ipynb`**

Com:
- Pipeline simples
- Train/test split
- Métrica básica
- Explicações

### 🏁 Checkpoint
- [ ] Criar Pipeline com 2+ etapas
- [ ] Cross-validation com 5 folds
- [ ] Comparar 2 modelos
- [ ] Commit: `[SEMANA-8-9] feat: Scikit-learn fundamentals`

---

## **SEMANA 9-10: Regressão Linear**

**Objetivo:** Prever valores contínuos

### 📚 O que estudar

| Conceito | Recurso | Tempo |
|----------|---------|-------|
| Teoria | [Statquest: Linear Regression](https://www.youtube.com/watch?v=PwFGJa7thdo) | 1.5h |
| Implementação | [Scikit-learn Linear Regression](https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares) | 1.5h |
| Métricas | [Regression metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics) | 1.5h |
| Diagnóstico | [Residuals and diagnostics](https://www.statsmodels.org/) | 2h |

### 🔑 Conceitos-chave
- Equação: y = β₀ + β₁x₁ + β₂x₂ + ... + ε
- Ordinary Least Squares (OLS)
- R² (R-squared), RMSE, MAE
- Resíduos e diagnóstico
- Multicolinearidade
- Regularização: Ridge (L2), Lasso (L1)

### 💻 Código que você vai escrever

```python
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np

# Dados
X = dados[['feature1', 'feature2', 'feature3']]
y = dados['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Predição
y_pred = model.predict(X_test)

# Métricas
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)

print(f"R²: {r2:.3f}, RMSE: {rmse:.2f}, MAE: {mae:.2f}")

# Coeficientes
for feat, coef in zip(X.columns, model.coef_):
    print(f"{feat}: {coef:.4f}")

# Regularização (Ridge)
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)
y_pred_ridge = ridge.predict(X_test)
print(f"Ridge R²: {r2_score(y_test, y_pred_ridge):.3f}")
```

### 📋 Entregável

**Notebook: `02-regressao-linear.ipynb`**

Com 5+ datasets:
- Dados sintéticos
- Dados reais (Housing, Tips)
- Comparação OLS vs Ridge vs Lasso
- Visualizações de resíduos

### 🏁 Checkpoint
- [ ] Treinar modelo linear
- [ ] Calcular R², RMSE, MAE
- [ ] Interpretar coeficientes
- [ ] Commit: `[SEMANA-9-10] feat: Regressão linear`

---

## **SEMANA 10-11: Classificação (Logística + Árvores)**

**Objetivo:** Prever categorias

### 📚 O que estudar

| Conceito | Recurso | Tempo |
|----------|---------|-------|
| Logística | [StatQuest: Logistic Regression](https://www.youtube.com/watch?v=yIYKR4sgstQ) | 1.5h |
| Árvores | [StatQuest: Decision Trees](https://www.youtube.com/watch?v=7VeUAPqLfQU) | 2h |
| Métricas | [Classification metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics) | 1.5h |
| ROC-AUC | [StatQuest: ROC and AUC](https://www.youtube.com/watch?v=4jRBRDbJfN0) | 1.5h |

### 🔑 Conceitos-chave
- Sigmoid function
- Regressão logística (binária + multiclass)
- Árvores de decisão: gini, entropy
- Matriz de confusão
- Precision, Recall, F1-score
- ROC curve, AUC
- Threshold tuning

### 💻 Código que você vai escrever

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    confusion_matrix, 
    classification_report,
    roc_auc_score,
    roc_curve
)

# Dados (classificação binária)
X = dados[['feature1', 'feature2']]
y = dados['target']  # 0 ou 1

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Regressão logística
log_model = LogisticRegression()
log_model.fit(X_train, y_train)
y_pred_log = log_model.predict(X_test)
y_proba_log = log_model.predict_proba(X_test)[:, 1]

# Árvore de decisão
tree_model = DecisionTreeClassifier(max_depth=5)
tree_model.fit(X_train, y_train)
y_pred_tree = tree_model.predict(X_test)

# Métricas
print(confusion_matrix(y_test, y_pred_log))
print(classification_report(y_test, y_pred_log))

# ROC-AUC
auc_score = roc_auc_score(y_test, y_proba_log)
print(f"AUC: {auc_score:.3f}")

# ROC curve
fpr, tpr, _ = roc_curve(y_test, y_proba_log)
```

### 📋 Entregável

**Notebook: `03-regressao-logistica.ipynb` + `04-arvores-decisao.ipynb`**

Com:
- Dados binários e multiclass
- Matriz de confusão
- Relatório de classificação
- ROC curves

### 🏁 Checkpoint
- [ ] Treinar Logistic Regression
- [ ] Treinar Decision Tree
- [ ] Calcular AUC
- [ ] Interpretar matriz de confusão
- [ ] Commit: `[SEMANA-10-11] feat: Classificação`

---

## **SEMANA 11-12: Ensemble Methods**

**Objetivo:** Combinar modelos para melhor performance

### 📚 O que estudar

| Conceito | Recurso | Tempo |
|----------|---------|-------|
| Random Forest | [StatQuest: Random Forest](https://www.youtube.com/watch?v=J4Wdy0Wc_xQ) | 1.5h |
| Gradient Boosting | [StatQuest: Gradient Boosting](https://www.youtube.com/watch?v=3CC4N_yofrA) | 2h |
| XGBoost | [XGBoost documentation](https://xgboost.readthedocs.io/) | 2h |
| Feature importance | [Scikit-learn feature importance](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html) | 1.5h |

### 🔑 Conceitos-chave
- Bootstrap aggregating (Bagging)
- Random Forest: árvores paralelas + agregação
- Boosting: árvores sequenciais + erro
- Gradient Boosting vs Adaptive Boosting
- XGBoost: otimizado, rápido
- Feature importance: Gini vs Permutation
- Overfitting em ensemble

### 💻 Código que você vai escrever

```python
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
import xgboost as xgb
from sklearn.inspection import permutation_importance

# Dados
X_train, X_test, y_train, y_test = split(...)

# Random Forest
rf = RandomForestClassifier(n_estimators=100, max_depth=10)
rf.fit(X_train, y_train)
rf_score = rf.score(X_test, y_test)
print(f"RF Accuracy: {rf_score:.3f}")

# Feature importance
for feat, imp in zip(X.columns, rf.feature_importances_):
    print(f"{feat}: {imp:.4f}")

# Gradient Boosting
gb = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1)
gb.fit(X_train, y_train)
gb_score = gb.score(X_test, y_test)

# XGBoost
xgb_model = xgb.XGBClassifier(n_estimators=100, learning_rate=0.1)
xgb_model.fit(X_train, y_train)
xgb_score = xgb_model.score(X_test, y_test)

# Comparação
print(f"RF: {rf_score:.3f}, GB: {gb_score:.3f}, XGB: {xgb_score:.3f}")
```

### 📋 Entregável

**Notebook: `05-ensemble.ipynb`**

Com:
- 3+ modelos ensemble
- Comparação de performance
- Feature importance
- Benchmark

### 🏁 Checkpoint
- [ ] Treinar Random Forest
- [ ] Treinar XGBoost
- [ ] Comparar com regressão/árvore
- [ ] Feature importance
- [ ] Commit: `[SEMANA-11-12] feat: Ensemble methods`

---

## **SEMANA 12-13: EDA Completa + Visualização**

**Objetivo:** Explorar dados visualmente

### 📚 O que estudar

| Conceito | Recurso | Tempo |
|----------|---------|-------|
| Matplotlib | [Matplotlib tutorial](https://matplotlib.org/stable/tutorials/index.html) | 2h |
| Seaborn | [Seaborn tutorial](https://seaborn.pydata.org/tutorial.html) | 2h |
| EDA workflow | [Real Python: EDA](https://realpython.com/python-data-visualization-bokeh/) | 2h |

### 🔑 Conceitos-chave
- Histogramas, box plots, scatter plots
- Heatmaps para correlação
- Distribuições condicionais
- Faceting/subplots
- Paletas de cores
- Anotações e labels

### 💻 Código que você vai escrever

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Dataset
df = pd.read_csv('dados.csv')

# Figure com subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Histograma
df['coluna1'].hist(bins=30, ax=axes[0, 0])
axes[0, 0].set_title('Distribuição de coluna1')

# Box plot
sns.boxplot(data=df, x='categoria', y='valor', ax=axes[0, 1])

# Scatter
sns.scatterplot(data=df, x='feature1', y='feature2', hue='target', ax=axes[1, 0])

# Heatmap de correlação
sns.heatmap(df.corr(), annot=True, fmt='.2f', ax=axes[1, 1])

plt.tight_layout()
plt.savefig('eda_completo.png', dpi=300)
plt.show()
```

### 📋 Entregável

**Notebook: `02-matplotlib-seaborn.ipynb` + `03-dashboards.ipynb`**

Com:
- 20+ visualizações diferentes
- Dashboard integrado
- Comentários explicativos

### 🏁 Checkpoint
- [ ] Fazer 5+ visualizações diferentes
- [ ] EDA completa de um dataset
- [ ] Commit: `[SEMANA-12-13] feat: EDA e visualização`

---

## **SEMANA 13-14: Métricas e Validação Cruzada**

**Objetivo:** Avaliar modelos corretamente

### 📋 Entregável

**Notebook: `03-metricas-modelo.ipynb`**

Com:
- Todas as métricas de regressão e classificação
- Validação cruzada estratificada
- Comparação de modelos

### 🏁 Checkpoint
- [ ] Implementar 10+ métricas
- [ ] Validação cruzada em 3 modelos
- [ ] Commit: `[SEMANA-13-14] feat: Métricas e validação`

---

# 📅 MESES 3-5: PROJETOS PRÁTICOS 🚀

## **PROJETO 1: Previsão de Preços (Regressão)**

**Duração:** Semanas 15-17  
**Dataset:** House prices  
**Objetivo:** Prever preços de imóvel

### 📁 Estrutura

```
projeto-01-imoveis/
├── data/
│   ├── raw/
│   │   ├── train.csv
│   │   └── test.csv
│   ├── processed/
│   │   └── train_processed.csv
│   └── README.md
├── notebooks/
│   ├── 01-eda.ipynb
│   ├── 02-preprocessamento.ipynb
│   ├── 03-modelo.ipynb
│   └── 04-resultados.ipynb
├── src/
│   ├── data_loader.py
│   ├── preprocessor.py
│   ├── model.py
│   └── utils.py
├── relatorio.md
├── requirements.txt
└── README.md
```

### 📋 Checklist

- [ ] EDA completa (20+ visualizações)
- [ ] Tratamento de faltantes (análise + decisão)
- [ ] Feature engineering (5+ novas features)
- [ ] Modelos: Linear + Ridge + Tree + Ensemble
- [ ] Comparação de performance
- [ ] Relatório com insights
- [ ] Código limpo e modular
- [ ] Commits diários

### 🏆 Entregável

- `notebooks/`: 4 notebooks explicados
- `src/`: Código reutilizável
- `relatorio.md`: Análise, decisões, resultados

---

## **PROJETO 2: Classificação Risco de Crédito**

**Duração:** Semanas 18-20  
**Dataset:** Credit card default  
**Objetivo:** Prever default

### 📋 Checklist

- [ ] EDA com foco em desbalanceamento
- [ ] Balanceamento de classes (SMOTE, class_weight)
- [ ] Feature engineering (razões, agregações)
- [ ] Modelos: Logistic + Tree + XGBoost
- [ ] Threshold tuning (business vs default)
- [ ] Feature importance
- [ ] ROC-AUC e PR curves
- [ ] Relatório com recomendações

---

## **PROJETO 3: Análise Real (Sua Empresa)**

**Duração:** Semanas 21-24  
**Dataset:** Dados Almeida Ambiental  
**Objetivo:** Insights operacionais + previsão

### 📊 Ideias

1. **Análise de coletas:** Padrões, horários ótimos
2. **Previsão de volume:** Próximas 4 semanas
3. **Otimização de rotas:** Clusters de clientes
4. **Análise de eficiência:** Tempo vs coletas
5. **Segmentação de clientes:** RFM

### 📋 Checklist

- [ ] Dados reais da empresa
- [ ] EDA contextualizado
- [ ] Modelo/Análise relevante para negócio
- [ ] Recomendações práticas
- [ ] Apresentação executiva
- [ ] Código production-ready

---

# 📅 MESES 5-6: PORTFÓLIO 🎯

## **SEMANA 20-21: Streamlit App**

**Objetivo:** Apresentar projetos publicamente

### 📁 Estrutura

```
streamlit-app/
├── app.py                    # Home
├── requirements.txt
├── pages/
│   ├── 01_Projeto_1.py      # Imóveis
│   ├── 02_Projeto_2.py      # Crédito
│   └── 03_Projeto_3.py      # Almeida
└── assets/
    ├── logo.png
    └── data/
```

### 💻 Exemplo `pages/01_Projeto_1.py`

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.model import load_model

st.set_page_config(page_title="Previsão de Preços", layout="wide")

st.title("🏠 Previsão de Preços de Imóveis")
st.write("""
Esta aplicação prediz preços de imóveis usando Machine Learning.
""")

# Sidebar
st.sidebar.header("Filtros")
size = st.sidebar.slider("Tamanho (m²)", 500, 5000, 2000)
rooms = st.sidebar.number_input("Quartos", 1, 10, 3)

# Predict
if st.button("Prever Preço"):
    prediction = predict_price(size, rooms)
    st.metric("Preço Estimado", f"R$ {prediction:,.2f}")

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("R²", 0.85)
col2.metric("RMSE", "R$ 50.000")
col3.metric("MAE", "R$ 35.000")

# Feature importance
st.subheader("Importância das Features")
fig, ax = plt.subplots()
# seu plot
st.pyplot(fig)
```

### 🏁 Entregável
- Streamlit app rodando
- Deploy em Streamlit Cloud

---

## **SEMANA 21-22: Documentação Técnica**

**Arquivo: `COMO-EXPLICAR-PROJETOS.md`**

```markdown
# Como Explicar Seus Projetos

## Projeto 1: Previsão de Preços

### 1️⃣ Em 30 segundos
"Construí um modelo de Machine Learning que prediz preços de imóveis."

### 2️⃣ Em 2 minutos
- **Problema:** Prever preço dado tamanho, localização, etc
- **Dados:** 1460 imóveis com 80 features
- **Abordagem:** Regressão (Linear + Ensemble)
- **Resultado:** R² de 0.85 (modelo explica 85% da variação)

### 3️⃣ Detalhado
- EDA: Distribuições, correlações, faltantes
- Preprocessamento: Escalamento, encoding, feature engineering
- Modelos: Comparei Linear, Ridge, Random Forest, XGBoost
- Melhor: XGBoost com R² = 0.85
```

---

## **SEMANA 22-23: Deploy**

Publicar Streamlit App em Streamlit Cloud (grátis)

---

## **SEMANA 23-24: GitHub Polish**

- [ ] README impecável
- [ ] Código com docstrings
- [ ] Requirements.txt atualizado
- [ ] .gitignore configurado
- [ ] Commits bem estruturados

---

# 🎓 COMO DOCUMENTAR PROGRESSO

Arquivo: `PROGRESS.md`

**Atualizar toda semana:**

```markdown
## Semana 1 (2024-01-01 a 2024-01-07)

### ✅ Completado
- [x] NumPy basics: arrays, indexing, operations
- [x] Notebook: 01-numpy-basico.ipynb (50 linhas de código)
- [x] Script: helper_functions.py com 5 funções

### 📚 Aprendizados principais
1. Broadcasting é mais confuso que parecia, mas poderoso
2. NumPy é MUITO mais rápido que loops Python
3. shape vs reshape importante pra debugging

### 🔴 Bloqueios
- Conceito de broadcasting não clicou no 1º dia
- **Solução:** Assisti 2x o StatQuest + pratiquei 1h

### 📈 Próxima semana
- [ ] Pandas Series
- [ ] Pandas DataFrames
- [ ] Primeiro dataset real

### 🔗 Commit
`[SEMANA-1] feat: NumPy fundamentals`

### 📊 Tempo gasto
- Estudo: 6h
- Prática: 4h
- **Total: 10h**
```

---

# 📋 Checklist Final

Ao final de 6 meses, você terá:

- [ ] 8+ notebooks educacionais
- [ ] 50+ queries SQL
- [ ] 3 projetos reais no GitHub
- [ ] 1 app Streamlit publicado
- [ ] ~100-150 commits
- [ ] README e documentação profissional
- [ ] Portfolio pronto para mostrar
- [ ] Capacidade Junior comprovada

---

**Comece hoje. Commit todo dia. Daqui a 6 meses você terá dados.**