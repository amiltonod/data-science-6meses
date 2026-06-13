# 🎤 COMO-EXPLICAR-PROJETOS.md - Estratégia de Entrevista

**Guia prático para explicar seus 3 projetos de Data Science em entrevistas.**

---

## 🎯 Filosofia Geral

Você terá **3-5 minutos** para explicar cada projeto. Não é muito. Aqui está como estruturar:

```
1️⃣ Contexto (30 segundos)    → "Qual era o problema?"
2️⃣ Abordagem (1 minuto)      → "Como você atacou?"
3️⃣ Resultados (1 minuto)     → "Qual foi o resultado?"
4️⃣ Aprendizados (1 minuto)   → "O que você aprendeu?"
```

**Total: 3:30 minutos. Pronto para expandir se perguntarem.**

---

## 📌 Estrutura de Resposta

### **NÃO faça isto:**
❌ "Eu carguei os dados com pandas..."  
❌ "Depois escalei com StandardScaler..."  
❌ "Aí fiz um loop e..."  

### **Faça isto:**
✅ "O desafio era prever X. Eu fiz Y. Resultado: Z."

---

# 🏠 PROJETO 1: Previsão de Preços de Imóveis

## 30 segundos (Elevator Pitch)

> "Construi um modelo de regressão que prediz preços de imóveis. Comecei com 1.460 casas com 80 features, fiz feature engineering, testei 4 algoritmos e consegui um R² de 0.85 no teste."

## 2 minutos (Completo)

> "O problema era prever preços de imóveis dado características como tamanho, localização, número de quartos. 
>
> Comecei com análise exploratória e descobri que:
> - Dataset tinha 1.460 casos e 80 features (muita colinearidade)
> - Distribuição de preços era skewed
> - 5 features explicavam 60% da variância
>
> Limpei dados, fiz feature engineering (razões úteis, transformações), escalei e testei:
> - Linear Regression (baseline)
> - Ridge (melhor que linear)
> - Random Forest
> - XGBoost (melhor)
>
> Resultado final: R² = 0.85 no teste, RMSE = R$ 35mil.
>
> O maior aprendizado foi que feature engineering importa mais que algoritmo complexo."

## Se perguntarem "Problemas enfrentados?"

> "A maior dificuldade foi lidar com 80 features. Inicialmente rodei o modelo com todas, overfitou. Solução: fiz análise de correlação, dropei features colineares, e reduzir para 15 features relevantes melhorou generalization.
>
> Segundo desafio: escala. Até escalá eu, um modelo com feature 'preço' (0-1M) vs 'quartos' (1-10) não funcinava. StandardScaler resolveu."

## Se perguntarem "Como você sabe que funciona?"

> "Usei validação cruzada 5-fold em todo o dataset, não só treino/teste. Métricas: R², RMSE, MAE. Comparei com baseline (dummy regressor que sempre prediz a média) e o modelo foi 10x melhor.
>
> Também visualizei: gráfico de resíduos, predicted vs actual, feature importance. Tudo consistente."

## Se perguntarem "Você deployaria?"

> "Não, não está 100% pronto. Eu trabalharia em:
> - Mais dados (1460 é pouco pra 80 features, ideal seria 5x)
> - Validação em dados NOVO (fora do período)
> - API REST (FastAPI) + testes unitários
> - Monitoramento (como acompanhar performance em produção?)
> - Documentação (como o modelo vai ser usado?)"

---

# 💳 PROJETO 2: Classificação Risco de Crédito

## 30 segundos

> "Previ risco de default de cartão de crédito em 30mil clientes. Problema: classe desbalanceada (1% default). Testei 3 algoritmos, considerei custo de false positives vs false negatives, e enteguei modelo com AUC 0.92."

## 2 minutos

> "O negócio queria prever quem ia dar default no cartão de crédito pra aumentar controle.
>
> Descoberta importante na EDA: apenas 1% dos clientes dão default (classe muito desbalanceada). Isso significava que um dummy classifier que sempre prediz 'não default' teria 99% de acurácia mas seria inútil!
>
> Por isso escolhi as métricas certas:
> - Precision: de quem eu classifiquei como risco, quanto realmente é?
> - Recall: de todos os riscos, quantos eu identifiquei?
> - ROC-AUC: visão holística
>
> Treino balanceei as classes com SMOTE (oversampling dos minortários).
>
> Modelos testados: Logistic Regression, Random Forest, XGBoost. Vencedor: XGBoost com AUC 0.92.
>
> Aprendizado-chave: a métrica importa MUITO. Se eu tivesse otimizado só pra acurácia, teria um modelo inútil."

## Se perguntarem "Precision vs Recall?"

> "Ótima pergunta! Depende do negócio:
> - Alta Precision: 'Quando digo risco, quero ter certeza.' Custa menos (menos falso alerta)
> - Alto Recall: 'Não quero perder NENHUM risco.' Custa mais (mais investigação)
>
> Nesse caso, default é caro, então otimizei pra Recall (~90%), aceitando Precision menor (~70%).
> 
> Daí tuneei o threshold: ao invés de usar 0.5, testei 0.3, 0.4, etc. e escolhi o que dava melhor trade-off."

## Se perguntarem "Como validou?"

> "Validação cruzada 5-fold. Mas tem um detalhe importante: quando você tem classe desbalanceada, você usa StratifiedKFold, que garante que cada fold tem mesma proporção de classes.
>
> Resultado: AUC médio 0.92 +/- 0.02 nas 5 folds. Variação pequena = modelo robusto."

---

# 📊 PROJETO 3: Análise Almeida Ambiental

## 30 segundos

> "Analisei dados de coleta de resíduos de minha empresa (Almeida Ambiental). Identifiquei padrões sazonais, clientes com maior risco de inadimplência e oportunidades de otimização de rotas que poderiam economizar 15% de combustível."

## 2 minutos

> "Trabalhei com dados reais de coleta de resíduos: 2 anos, 500+ clientes, 50mil eventos de coleta.
>
> Análises principais:
>
> 1. **Sazonalidade**: Volume de coleta sobe 40% em verão (mais construção). Implicação: precisa de recursos pra pico.
>
> 2. **Segmentação de clientes**: Usei RFM (Recência, Frequência, Monetário). Identifiquei 3 grupos:
>    - 'Gold': 20% dos clientes, 60% da receita
>    - 'Silver': 30% dos clientes, 30% da receita
>    - 'Bronze': 50% dos clientes, 10% da receita
>
> 3. **Análise de rotas**: Clusterizei 500 clientes em 15 grupos geográficos. Cada grupo = 1 rota potencial. Economia estimada: 15% de combustível.
>
> 4. **Previsão de demanda**: Modelo ARIMA pra prever volume 4 semanas adiante. Erro ~8%. Útil pra planejar equipe.
>
> Entreguei: Notebook, relatório executivo, 3 recomendações acionáveis.
> Impacto: Gerente disse que ia usar a segmentação RFM pra estratégia comercial."

## Se perguntarem "Por que um projeto próprio importa?"

> "Ótima pergunta! Esse projeto mostra:
> - Entendo contexto operacional (não só estatística)
> - Posso trabalhar com dados REAIS (messy)
> - Consigo comunicar com não-técnicos (relatório pra gerente, não pra cientista)
> - Tenho disciplina (coletei, limpei e analisei dados próprios)
> - Agreguei valor (recomendações que vão ser usadas)
>
> Muitos portfolios têm notebooks legais mas desconectados da realidade. Esse não."

## Se perguntarem sobre tecnologia

> "Stack simples: Python, Pandas, Scikit-learn, Matplotlib. Notebooks Jupyter documentados.
>
> Não usei Deep Learning ou cloud porque não precisa. Simples e efetivo. Fácil de manter e explicar."

---

# 🎤 Cenários Específicos

## Pergunta: "Qual foi seu maior desafio?"

**NÃO diga:** "Tudo foi fácil, aprendi rápido."

**DIGA:** "O maior desafio foi [X]. Solução: [Y]. Aprendizado: [Z]."

Exemplos:
- "Overfitting no Projeto 1. Solução: regularização + validação cruzada."
- "Desbalanceamento no Projeto 2. Solução: SMOTE + threshold tuning."
- "Dados sujos no Projeto 3. Solução: EDA rigorosa + documentação de limpeza."

---

## Pergunta: "Como você abordaria um problema novo?"

**Responda com processo:**

1. **Entender o problema**
   - Qual é a pergunta de negócio?
   - Qual seria sucesso?
   - Quem usa a resposta?

2. **Dados**
   - Que dados tenho?
   - Quanto? Como está a qualidade?
   - Posso acessar mais?

3. **Abordagem**
   - Regressão, classificação, clustering?
   - Qual métrica importa?
   - Qual é o baseline?

4. **Experimento**
   - Teste múltiplos modelos
   - Validação cruzada sempre
   - Feature importance

5. **Resultado**
   - Comunicar claramente
   - Documentar decisões
   - Recomendar próximos passos

---

## Pergunta: "Como você aprende?"

**Responda com evidência:**

"Eu documentei minha jornada de 6 meses em um repositório GitHub público. Cada semana atualizava o PROGRESS.md, commitava código, e registrava aprendizados. Isso força você a ser honesto: ou você fez ou não fez.

Aprendi:
- Formalmente: Cursos (Andrew Ng, StatQuest)
- Praticamente: 3 projetos reais, 100+ commits
- Documentando: Blogpost sobre [X] que escrevi

Esse processo contínuo é mais importante que qualquer certificado."

---

## Pergunta: "Qual algoritmo é melhor?"

**NÃO diga:** "XGBoost!"

**DIGA:** "Depende. Melhor em quê? Acurácia? Interpretabilidade? Velocidade?

- Linear: Rápido, interpretável, bom pra baseline
- Tree: Inteligente com features categóricas
- Ensemble: Melhor acurácia, mas caixa preta
- Deep Learning: Quando tiver MUITOS dados

No Projeto 1, XGBoost foi 5% melhor que Random Forest. Valia a complexidade? Provavelmente não. Mas varia por caso."

---

## Pergunta: "Nunca deployou?"

**Seja honesto:**

"Nos 3 projetos, foquei em análise e modelagem. Não fiz deploy ainda. Mas entendo:
- Salvar modelo (.pkl ou .joblib)
- Criar API (FastAPI é minha próxima meta)
- Testes unitários
- Monitoramento

É proximo passo natural. A ordem que escolhi (aprender bem antes de deployar) foi intencional."

---

# 🔥 Redflags a Evitar

### ❌ "Fiz tudo sozinho sem ajuda"
**Melhor:** "Usei recursos X, Y, Z. Apliquei meu julgamento em decisões A, B, C."

### ❌ "Não tive problemas"
**Melhor:** "Tive desafio X, solução Y, aprendizado Z."

### ❌ "Não sei SQL/cloud/MLOps"
**Melhor:** "Não tenho experiência, mas [entendo conceitos / estou aprendendo / fiz cursinho]. Quero aprender na prática."

### ❌ "Copiava código do tutorial"
**Melhor:** "Comecei com fundamentals, depois apliquei a problemas próprios."

---

# 📝 Checklist Antes de Entrevista

- [ ] Acesso rápido ao GitHub (link memorizado)
- [ ] Podo abrir cada notebook em 10 segundos
- [ ] Consigo explicar cada projeto em 30s e em 2min
- [ ] Memorizo os 3 maiores aprendizados de cada projeto
- [ ] Tenho exemplos de problemas e como resolvi
- [ ] Consigo código rodando no laptop se pedirem
- [ ] Estudei os conceitos por trás (não só decorei código)

---

# 🎓 Template para Estudar

**A noite anterior a entrevista:**

1. Leia os 3 READMEs dos projetos
2. Abra cada notebook e relembre pontos principais
3. Pratique dizer cada pitch em 30s e 2min
4. Prepare respostas para 5 perguntas

**Na entrevista:**

1. Responda a pergunta que fizeram (não mais, não menos)
2. Dê exemplos concretos
3. Mostre código quando apropriado
4. Termine deixando porta aberta: "Quer ver o código?" ou "Quer que aprofunde?"

---

**Você preparado. Eles vão ficar impressionados pela disciplina, não só pela técnica.**