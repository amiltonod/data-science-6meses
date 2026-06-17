# 📚 NumPy — Guia de Fixação Completo

> Resumo consolidado de todos os conceitos estudados na Semana 1.
> Use como folha de consulta rápida antes de entrevistas ou ao iniciar um novo projeto.

---

## 📋 Índice

1. [O que é um Array NumPy](#1-o-que-é-um-array-numpy)
2. [Criando Arrays](#2-criando-arrays)
3. [Indexação e Fatiamento](#3-indexação-e-fatiamento)
4. [Boolean Indexing](#4-boolean-indexing-filtro-sem-loop)
5. [Operações Vetorizadas](#5-operações-vetorizadas)
6. [Axis — O conceito que separa Junior de Pleno](#6-axis--o-conceito-que-separa-junior-de-pleno)
7. [Scripts .py vs Notebooks .ipynb](#7-scripts-py-vs-notebooks-ipynb)
8. [Mapa Mental](#8-mapa-mental-rápido)
9. [Desafio Final](#9-desafio-final)

---

## 1. O que é um Array NumPy

**Regra de ouro:** Array é uma lista de tipo único, armazenada de forma contígua na memória. Por isso é rápido.

```python
import numpy as np

# Lista Python (lenta, mistura tipos)
lista = [1, 2.5, "três"]  # aceita qualquer coisa

# Array NumPy (rápido, tipo único)
array = np.array([1, 2, 3, 4])
print(array.dtype)   # int64
print(array.shape)   # (4,) → 4 elementos, 1 dimensão
```

> ⚠️ **Nunca esqueça:** Colocou string junto com número → NumPy converte tudo para string e suas operações matemáticas quebram.

---

## 2. Criando Arrays

```python
# Sequência (como range do Python, mas é array)
ids = np.arange(100, 110, 2)      # [100, 102, 104, 106, 108]

# Preenchido com zero ou um
estoque = np.zeros(5)              # [0. 0. 0. 0. 0.]
mascara = np.ones(5)               # [1. 1. 1. 1. 1.]

# Preenchido com valor específico
meta = np.full(5, 1000)            # [1000 1000 1000 1000 1000]

# Matriz 2D
vendas = np.array([
    [100, 200, 300],   # Loja A
    [400, 500, 600]    # Loja B
])
print(vendas.shape)   # (2, 3) → 2 linhas, 3 colunas
```

---

## 3. Indexação e Fatiamento

**A regra que você não erra mais:**

```array[LINHA, COLUNA]
  :  → "tudo desse eixo"
  0  → índice específico
```

```python
dados = np.array([
    [10, 45, 150000],   # Filial 10
    [11, 12, 320000],   # Filial 11
    [12, 85,  95000],   # Filial 12
])

dados[0, :]     # Linha 0 inteira   → [10, 45, 150000]
dados[:, 2]     # Coluna 2 inteira  → [150000, 320000, 95000]
dados[1, 2]     # Linha 1, col 2    → 320000
dados[0:2, 1:]  # Linhas 0-1, col 1 em diante
```

> ⚠️ **Pegadinha clássica:** `[:, 0]` pega uma coluna inteira, não uma linha. Para pegar a linha 0 use `[0, :]`.

---

## 4. Boolean Indexing (Filtro sem loop)

**Nunca use `and`/`or` no NumPy. Use `&` e `|` com parênteses.**

```python
faturamento = np.array([2500, 1800, 4000, 900, 5000])

# Máscara → array de True/False
mascara = faturamento > 2000
# [True, False, True, False, True]

# Aplicar máscara
resultado = faturamento[mascara]
# [2500, 4000, 5000]

# Múltiplas condições — SEMPRE com parênteses
entre = faturamento[(faturamento > 2000) & (faturamento < 4500)]
# [2500, 4000]
```

> ⚠️ **Erro clássico de entrevista:**
> ```python
> # ERRADO — quebra o código
> vendas[(vendas > 50) and (vendas < 150)]
>
> # CORRETO
> vendas[(vendas > 50) & (vendas < 150)]
> ```

---

## 5. Operações Vetorizadas

**Nunca use loop para calcular. NumPy faz em todo o array de uma vez.**

```python
precos = np.array([100, 200, 300, 400])

precos * 0.9           # Desconto 10% em todos   → [90, 180, 270, 360]
precos + 50            # Aumento fixo em todos    → [150, 250, 350, 450]

np.sum(precos)         # Total      → 1000
np.mean(precos)        # Média      → 250.0
np.max(precos)         # Maior      → 400
np.min(precos)         # Menor      → 100
np.argmax(precos)      # Índice do maior → 3
np.argmin(precos)      # Índice do menor → 0
```

---

## 6. Axis — O conceito que separa Junior de Pleno

**Macete visual:**

```
            col0  col1  col2
Loja A →   [100,  200,  300]   ← axis=1 vai nessa direção →
Loja B →   [400,  500,  600]
               ↓     ↓     ↓
             axis=0 vai nessa direção
```

```python
vendas = np.array([
    [100, 200, 300],  # Loja A
    [400, 500, 600]   # Loja B
])

np.sum(vendas, axis=0)   # Total por coluna (mês)  → [500, 700, 900]
np.sum(vendas, axis=1)   # Total por linha (loja)   → [600, 1500]
np.mean(vendas, axis=1)  # Média por loja           → [200.0, 500.0]
```

> 💡 **Macete de memorização:** `axis=0` lembra a letra **"O"** de **"Olhar para baixo"** (direção vertical).
> `axis=1` opera horizontalmente, resultado por linha.

---

## 7. Scripts `.py` vs Notebooks `.ipynb`

| Arquivo | Para que serve |
|---------|---------------|
| `script.py` | Funções reutilizáveis, importadas em qualquer lugar |
| `notebook.ipynb` | Exploração, análise, visualização, apresentação |

```python
# helper_functions.py
import numpy as np

def filtrar_valores_altos(vendas):
    """
    Filtra valores acima de 5000.
    Input:  vendas → array NumPy
    Output: array filtrado
    """
    mascara = vendas > 5000
    return vendas[mascara]
```

```python
# No notebook .ipynb
from helper_functions import filtrar_valores_altos

vendas = np.array([3000, 6000, 1500, 7000])
print(filtrar_valores_altos(vendas))  # [6000 7000]
```

---

## 8. Mapa Mental Rápido

```
NumPy
├── Criar array
│   ├── np.array([...])
│   ├── np.arange(inicio, fim, passo)
│   ├── np.zeros(n) / np.ones(n)
│   └── np.full(n, valor)
│
├── Inspecionar
│   ├── .shape  → dimensões
│   ├── .dtype  → tipo de dado
│   └── .ndim   → nº de dimensões
│
├── Fatiar
│   ├── array[i]       → elemento i
│   ├── array[i, j]    → linha i, coluna j
│   └── array[:, j]    → coluna j inteira
│
├── Filtrar
│   ├── array[array > x]
│   └── array[(cond1) & (cond2)]
│
└── Calcular
    ├── np.sum / np.mean / np.max / np.min
    ├── np.argmax / np.argmin
    └── axis=0 (colunas) / axis=1 (linhas)
```

---

## 9. Desafio Final

**Cenário:** Você é analista de dados de uma rede de farmácias. Recebeu a matriz abaixo com dados de 4 filiais no mês:

```python
import numpy as np

# Colunas: [ID Filial, Vendas (unidades), Faturamento (R$), Devoluções]
farmacias = np.array([
    [1, 320, 48000, 15],
    [2, 510, 76500,  8],
    [3, 190, 28500, 42],
    [4, 430, 64500, 20]
])
```

### Missão 1 — Fatiamento
Isole as colunas `faturamento` e `devolucoes` em variáveis separadas.

### Missão 2 — Filtro de risco
Identifique os IDs das filiais com devoluções acima de 18.
Essas filiais vão para auditoria.

### Missão 3 — Métricas
Calcule o faturamento total da rede e a média de vendas por filial.

### Missão 4 — Ranking
Descubra o **índice** da filial com maior faturamento e use esse índice para exibir todos os dados dela.

```python
# Dica da Missão 4
indice = np.argmax(faturamento)
print(farmacias[indice, :])
```

**Commit após resolver:**
```bash
git add .
git commit -m "[SEMANA-1] feat: desafio final NumPy - análise farmácias"
git push
```

---

## ✅ Checklist de Domínio

Você domina NumPy quando consegue, **sem consultar**:

- [x] Criar array 1D e 2D com tipos diferentes
- [x] Fatiar linha, coluna e submatriz
- [x] Filtrar com máscara booleana simples e composta
- [x] Calcular soma, média, max, min com e sem axis
- [x] Usar argmax/argmin para localizar índice
- [x] Importar função de um script `.py` no notebook

---

*Semana 1 — NumPy concluído.*
*Próximo: Pandas — Series e DataFrames.*
