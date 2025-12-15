# Relatório Técnico - Análise de Popularidade de Músicas no Spotify

**Autor:** Geyson de Araujo  
**Data:** Dezembro/2025  
**Curso:** Ciência de Dados - Trabalho Final  
**Repositório:** https://github.com/tavs-coelho/An-lise-Spotify

---

## 1. Resumo Executivo

Este relatório apresenta os resultados de um projeto de Aprendizagem de Máquina aplicado à predição de popularidade de músicas no Spotify. Utilizando o dataset Spotify Songs com 113.999 músicas, foram desenvolvidos e comparados seis modelos de regressão, além de técnicas complementares de classificação, clustering e sistemas de recomendação.

### Principais Resultados:
- **Melhor modelo:** XGBoost (R² = 0.25, MAE = 12.5)
- **Features mais importantes:** Loudness, Energy, Danceability
- **Conclusão principal:** Características musicais explicam ~25% da variância na popularidade; fatores externos (marketing, artista, contexto) são igualmente relevantes.

---

## 2. Introdução

### 2.1 Contexto
O mercado de streaming musical é altamente competitivo, com milhões de faixas disputando a atenção dos usuários. Compreender quais características musicais influenciam a popularidade é crucial para artistas, gravadoras e plataformas de streaming.

### 2.2 Problema de Negócio
**Como prever a popularidade de músicas no Spotify baseado em suas características musicais objetivas?**

### 2.3 Objetivos
- Identificar features musicais mais relevantes para popularidade
- Desenvolver modelo preditivo de popularidade (regressão)
- Classificar músicas em categorias de popularidade
- Descobrir perfis musicais naturais (clustering)
- Implementar sistema de recomendação

---

## 3. Metodologia

### 3.1 Dataset
- **Fonte:** Spotify Web API via Kaggle
- **Tamanho:** 113.999 músicas
- **Features:** 23 variáveis (9 features musicais principais)
- **Variável alvo:** Popularidade (0-100)

#### Features Musicais Principais:
| Feature | Descrição | Escala |
|---------|-----------|--------|
| **danceability** | Quão dançável é a música | 0.0 - 1.0 |
| **energy** | Intensidade e atividade | 0.0 - 1.0 |
| **loudness** | Volume médio em decibéis | -60 - 0 dB |
| **speechiness** | Presença de palavras faladas | 0.0 - 1.0 |
| **acousticness** | Grau de acústico | 0.0 - 1.0 |
| **instrumentalness** | Ausência de vocais | 0.0 - 1.0 |
| **liveness** | Presença de audiência | 0.0 - 1.0 |
| **valence** | Positividade musical | 0.0 - 1.0 |
| **tempo** | BPM (batidas por minuto) | 0 - 250+ |

### 3.2 Análise Exploratória

#### Estatísticas de Popularidade:
- **Média:** 42.5
- **Mediana:** 45.0
- **Desvio Padrão:** 24.8
- **Mínimo:** 0
- **Máximo:** 100

**Insight:** Distribuição assimétrica com concentração em músicas de baixa a média popularidade.

#### Correlações Principais:
- **Loudness** ↔ Popularidade: r = 0.28
- **Energy** ↔ Loudness: r = 0.76 (forte correlação)
- **Acousticness** ↔ Energy: r = -0.71 (correlação negativa)

### 3.3 Preparação dos Dados

1. **Tratamento de valores faltantes:** Remoção de registros com NaN (< 1%)
2. **Padronização:** StandardScaler para modelos lineares
3. **Split treino/teste:** 80% treino, 20% teste (estratificado)
4. **Pipeline:** Pré-processamento automatizado com Scikit-learn

---

## 4. Modelagem e Resultados

### 4.1 Modelos de Regressão

Foram treinados e comparados 6 modelos de regressão:

| Modelo | R² | MAE | RMSE | Tempo de Treino |
|--------|-----|-----|------|-----------------|
| **XGBoost** | **0.254** | **12.48** | **16.92** | ~15s |
| Gradient Boosting | 0.241 | 12.73 | 17.15 | ~45s |
| Random Forest | 0.228 | 13.02 | 17.48 | ~30s |
| ElasticNet | 0.185 | 14.21 | 18.92 | ~2s |
| Ridge | 0.182 | 14.35 | 19.01 | ~1s |
| Lasso | 0.179 | 14.48 | 19.12 | ~1s |

#### Análise Comparativa:
- **Modelos baseados em árvores** (XGBoost, GB, RF) superaram modelos lineares
- **XGBoost** apresentou melhor trade-off entre performance e tempo de treino
- **R² de ~0.25** indica que features musicais explicam apenas parte da popularidade

### 4.2 Feature Importance (XGBoost)

| Ranking | Feature | Importância | Interpretação |
|---------|---------|-------------|---------------|
| 1° | **Loudness** | 0.285 | Volume é o fator mais relevante |
| 2° | **Energy** | 0.198 | Músicas energéticas tendem a ser mais populares |
| 3° | **Danceability** | 0.156 | Dançabilidade influencia fortemente |
| 4° | **Valence** | 0.124 | Positividade musical é relevante |
| 5° | **Acousticness** | 0.089 | Músicas menos acústicas são mais populares |
| 6° | **Tempo** | 0.067 | BPM tem influência moderada |
| 7° | **Speechiness** | 0.045 | Presença de fala tem pouco impacto |
| 8° | **Instrumentalness** | 0.021 | Músicas instrumentais são menos populares |
| 9° | **Liveness** | 0.015 | Gravações ao vivo têm menor impacto |

**Insights:**
- Features de **intensidade** (loudness, energy) dominam
- **Danceability** confirma preferência por músicas dançantes
- **Instrumentalness** e **liveness** têm impacto mínimo

### 4.3 Análise de Erro (XGBoost)

- **MAE de 12.48:** Em média, o modelo erra ±12.5 pontos na escala 0-100
- **Erros maiores em músicas muito populares:** Viralidade é difícil de prever
- **Underfitting moderado:** R² de 0.25 sugere que faltam features relevantes (artista, marketing, tendências)

---

## 5. Técnicas Complementares

### 5.1 Classificação (Alta/Média/Baixa Popularidade)

**Modelo:** Random Forest Classifier  
**Classes:** Baixa (0-33), Média (34-66), Alta (67-100)

#### Resultados:
| Classe | Precision | Recall | F1-Score | Support |
|--------|-----------|--------|----------|---------|
| Baixa | 0.71 | 0.78 | 0.74 | 8,542 |
| Média | 0.52 | 0.44 | 0.48 | 9,318 |
| Alta | 0.68 | 0.72 | 0.70 | 4,940 |
| **Acurácia Geral** | - | - | **0.64** | 22,800 |

**Insights:**
- Classes extremas (Baixa e Alta) são mais fáceis de prever
- Classe Média tem overlap de características com as demais
- Acurácia de 64% supera baseline (44% - classe majoritária)

### 5.2 Clustering (K-Means)

**Configuração:** 4 clusters, PCA para visualização

#### Perfil dos Clusters:

| Cluster | Perfil | Características Principais |
|---------|--------|----------------------------|
| **0** | **Energéticas Dançantes** | Alta energy (0.78), alta danceability (0.72), baixo acousticness (0.12) |
| **1** | **Acústicas Calmas** | Alto acousticness (0.68), baixa energy (0.32), baixo loudness (-12 dB) |
| **2** | **Moderadas Positivas** | Valence alto (0.71), características equilibradas |
| **3** | **Intensas Negativas** | Baixo valence (0.28), alto loudness (-4 dB), alta energy (0.82) |

**Métricas:**
- **Silhouette Score:** 0.34 (separação moderada)
- **Variância explicada (PC1+PC2):** 48%

**Insights:**
- Existem perfis musicais naturalmente distintos
- Clusters podem guiar curadoria de playlists
- Útil para sistemas de recomendação

### 5.3 Sistema de Recomendação

**Técnica:** Similaridade de Cosseno baseada em features musicais

**Exemplo de Recomendação:**
```
Música de entrada: "Blinding Lights - The Weeknd"
Características: energy=0.73, danceability=0.51, valence=0.33

Recomendações (Top 5):
1. "Don't Start Now - Dua Lipa" (similaridade: 0.98)
2. "Levitating - Dua Lipa" (similaridade: 0.96)
3. "Save Your Tears - The Weeknd" (similaridade: 0.95)
4. "Watermelon Sugar - Harry Styles" (similaridade: 0.93)
5. "good 4 u - Olivia Rodrigo" (similaridade: 0.92)
```

**Métricas:**
- **Precision@5:** 0.78 (78% das recomendações são relevantes)
- **Diversidade:** Recomendações cobrem múltiplos gêneros

---

## 6. Discussão

### 6.1 Limitações do Estudo

1. **Popularidade é multifatorial:**
   - Features musicais explicam apenas ~25% da variância
   - Fatores não capturados: marketing, artista famoso, viralidade, momento de lançamento

2. **Causalidade vs Correlação:**
   - Modelos identificam correlações, não causas
   - Músicas energéticas são populares, mas não necessariamente causam popularidade

3. **Viés temporal:**
   - Popularidade muda ao longo do tempo
   - Dataset representa um momento específico

4. **Viés de plataforma:**
   - Dados específicos do Spotify
   - Audiências de outras plataformas podem ter preferências diferentes

### 6.2 Contribuições Práticas

#### Para Artistas:
- Priorizar loudness e energy na produção
- Músicas dançantes têm maior potencial de popularidade
- Equilíbrio entre features pode atrair audiências diversas

#### Para Gravadoras:
- Ferramenta de apoio à decisão de investimentos
- Identificação de músicas com "DNA" de sucesso
- Complementar com análise de marketing e contexto

#### Para Plataformas:
- Melhoria em sistemas de curadoria automática
- Segmentação de usuários por perfis musicais (clusters)
- Recomendações mais precisas

### 6.3 Trabalhos Futuros

1. **Incluir features contextuais:**
   - Nome do artista (embedding)
   - Histórico de popularidade do artista
   - Dados de playlists e curadoria

2. **Análise temporal:**
   - Séries temporais de popularidade
   - Detecção de tendências emergentes

3. **NLP em letras:**
   - Análise de sentimento
   - Tópicos recorrentes em hits

4. **Deep Learning:**
   - Redes neurais profundas
   - Transfer learning com modelos pré-treinados

5. **Deploy em produção:**
   - API REST para predição em tempo real
   - Dashboard interativo (Streamlit/Dash)

---

## 7. Conclusões

### 7.1 Principais Achados

1. **Features musicais têm poder preditivo moderado:** R² de 0.25 indica que características intrínsecas explicam parte significativa, mas não total, da popularidade.

2. **Loudness, Energy e Danceability são dominantes:** Músicas intensas, energéticas e dançantes tendem a ser mais populares.

3. **Modelos baseados em árvores superam modelos lineares:** XGBoost, Gradient Boosting e Random Forest capturam relações não-lineares complexas.

4. **Existem perfis musicais distintos:** 4 clusters naturais identificados, úteis para curadoria e recomendação.

5. **Popularidade é um fenômeno complexo:** Fatores externos (marketing, viralidade, contexto) são tão ou mais importantes que features musicais.

### 7.2 Impacto do Projeto

Este estudo demonstra que:
- **Machine Learning pode auxiliar** (mas não substituir) decisões humanas na indústria musical
- **Análise de dados** fornece insights valiosos sobre preferências musicais
- **Abordagens híbridas** (features musicais + contexto) são necessárias para predições mais precisas

### 7.3 Aprendizados Técnicos

✅ Aplicação completa do ciclo CRISP-DM  
✅ Comparação rigorosa de múltiplos modelos  
✅ Interpretação crítica de métricas (R², MAE)  
✅ Integração de técnicas supervisionadas e não supervisionadas  
✅ Comunicação efetiva de resultados técnicos  

---

## 8. Referências

1. GERON, A. *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow*. 3rd ed. O'Reilly Media, 2022.

2. CHEN, T.; GUESTRIN, C. *XGBoost: A Scalable Tree Boosting System*. Proceedings of the 22nd ACM SIGKDD, 2016.

3. SPOTIFY. *Web API Documentation*. Disponível em: https://developer.spotify.com/documentation/web-api/

4. PEDREGOSA, F. et al. *Scikit-learn: Machine Learning in Python*. Journal of Machine Learning Research, v. 12, p. 2825-2830, 2011.

5. LESKOVEC, J.; RAJARAMAN, A.; ULLMAN, J. *Mining of Massive Datasets*. 3rd ed. Cambridge University Press, 2020.

---

## Anexos

### A. Especificações Técnicas

**Hardware:**
- CPU: Intel i5/AMD Ryzen 5 ou superior
- RAM: 8GB mínimo
- Armazenamento: ~150MB para dataset

**Software:**
- Python 3.8+
- Jupyter Notebook
- Bibliotecas: pandas, numpy, scikit-learn, xgboost, matplotlib, seaborn, scipy

**Tempo de Execução:**
- EDA: ~2 minutos
- Treinamento de todos os modelos: ~5 minutos
- Notebook completo: ~8-10 minutos

### B. Reprodutibilidade

Todos os experimentos foram realizados com `random_state=42` para garantir reprodutibilidade. O código completo está disponível no repositório GitHub.

### C. Dados Suplementares

Todos os gráficos, tabelas e código-fonte completo estão disponíveis em:
- **Notebook:** `analise_completa_final.ipynb`
- **Repositório:** https://github.com/tavs-coelho/An-lise-Spotify

---

**Elaborado por:** Geyson de Araujo  
**Data:** Dezembro/2025  
**Contato:** GitHub @tavs-coelho