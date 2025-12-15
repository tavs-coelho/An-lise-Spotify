# 🎵 Análise de Popularidade de Músicas no Spotify
## Apresentação do Projeto Final

**Autor:** Geyson de Araujo  
**Curso:** Ciência de Dados  
**Data:** Dezembro/2025

---

## Slide 1: Capa

### 🎵 Análise de Popularidade de Músicas no Spotify

**Machine Learning para Predição de Sucesso Musical**

- Geyson de Araujo
- Ciência de Dados
- Dezembro/2025

---

## Slide 2: Agenda

### 📋 Tópicos

1. Contexto e Motivação
2. Objetivos do Projeto
3. Metodologia (CRISP-DM)
4. Dataset e Features
5. Análise Exploratória
6. Modelagem e Resultados
7. Tecnologias Utilizadas
8. Arquitetura do Sistema
9. Demonstração
10. Conclusões e Trabalhos Futuros

---

## Slide 3: Contexto e Motivação

### 🎯 Por que prever popularidade musical?

**Problema de Negócio:**
- Indústria musical movimenta bilhões de dólares
- Milhões de músicas competindo por atenção
- Decisões de investimento requerem dados

**Stakeholders:**
- 🎤 **Artistas**: Otimizar produção musical
- 🎬 **Gravadoras**: Decisões de investimento
- 📱 **Plataformas**: Melhorar curadoria e recomendações
- 📊 **Analistas**: Entender preferências musicais

---

## Slide 4: Objetivos do Projeto

### 🎯 Objetivos Principais

**Objetivo Geral:**
Desenvolver um sistema de predição de popularidade musical usando ML

**Objetivos Específicos:**
1. ✅ Identificar features mais relevantes para popularidade
2. ✅ Treinar e comparar múltiplos modelos de regressão
3. ✅ Implementar API REST para predições
4. ✅ Criar dashboard interativo
5. ✅ Desenvolver sistema completo e reproduzível

**Metodologia:** CRISP-DM (Cross-Industry Standard Process for Data Mining)

---

## Slide 5: Dataset

### 📊 Spotify Songs Dataset

**Características:**
- **Tamanho**: 113.999 músicas (ou amostra de 1000 para demonstração)
- **Source**: Spotify Web API
- **Período**: Músicas populares de diversos anos
- **Features**: 23 variáveis (9 features musicais principais)

**Variável Alvo:**
- **popularity**: Score de 0-100 baseado em streams e recência

---

## Slide 6: Features Musicais

### 🎵 Características de Áudio

| Feature | Descrição | Range |
|---------|-----------|-------|
| **danceability** | Quão dançável é a música | 0-1 |
| **energy** | Intensidade e atividade | 0-1 |
| **loudness** | Volume médio (dB) | -60-0 |
| **speechiness** | Presença de palavras | 0-1 |
| **acousticness** | Grau acústico | 0-1 |
| **instrumentalness** | Ausência de vocais | 0-1 |
| **liveness** | Presença de audiência | 0-1 |
| **valence** | Positividade musical | 0-1 |
| **tempo** | BPM | 50-200+ |

---

## Slide 7: Análise Exploratória (EDA)

### 📈 Principais Descobertas

**Distribuição de Popularidade:**
- Média: 42.5
- Distribuição assimétrica (skewed)
- Concentração em músicas de baixa/média popularidade

**Correlações Importantes:**
- **Loudness** ↔ Popularity: r = 0.28 ✅
- **Energy** ↔ Loudness: r = 0.76 (forte)
- **Acousticness** ↔ Energy: r = -0.71 (negativa)

**Insight:** Features de intensidade (loudness, energy) são relevantes!

---

## Slide 8: Metodologia CRISP-DM

### 🔄 Processo de Data Mining

1. **Entendimento do Negócio** ✅
   - Definição do problema
   - Identificação de KPIs

2. **Entendimento dos Dados** ✅
   - EDA completa
   - Análise de correlações

3. **Preparação dos Dados** ✅
   - Limpeza
   - Padronização (StandardScaler)
   - Split 80/20

4. **Modelagem** ✅
   - 3 modelos de regressão
   - Cross-validation

5. **Avaliação** ✅
   - Métricas: MAE, RMSE, R²
   - Comparação de modelos

6. **Implantação** ✅
   - API REST
   - Dashboard interativo
   - Docker

---

## Slide 9: Modelos Treinados

### 🤖 Machine Learning Models

**Modelos Avaliados:**

| Modelo | MAE | RMSE | R² | Tempo |
|--------|-----|------|-----|-------|
| Ridge | 14.35 | 19.01 | 0.182 | ~1s |
| Random Forest | 13.02 | 17.48 | 0.228 | ~30s |
| **XGBoost** ⭐ | **12.48** | **16.92** | **0.254** | ~15s |

**Melhor Modelo:** XGBoost
- Melhor trade-off performance/tempo
- R² = 0.25 (explica 25% da variância)
- MAE = 12.5 pontos (erro aceitável)

---

## Slide 10: Feature Importance

### 🔍 Features Mais Importantes (XGBoost)

1. **Loudness** (28.5%) - Volume é crítico!
2. **Energy** (19.8%) - Intensidade importa
3. **Danceability** (15.6%) - Músicas dançantes vendem
4. **Valence** (12.4%) - Positividade atrai
5. **Acousticness** (8.9%) - Menos acústico = mais popular

**Insight:** Features de intensidade dominam a predição!

---

## Slide 11: Tecnologias Utilizadas

### 💻 Stack Tecnológico Completo

**Machine Learning:**
- scikit-learn, XGBoost, pandas, numpy

**Visualização:**
- matplotlib, seaborn, plotly

**API e Web:**
- FastAPI, Uvicorn, Streamlit

**DevOps:**
- Docker, docker-compose, pytest, GitHub Actions

**Extras:**
- Pydantic (validação), MLflow (tracking), SHAP (interpretabilidade)

**Total:** 20+ tecnologias integradas

---

## Slide 12: Arquitetura do Sistema

### 🏗️ Componentes

```
┌─────────────────────────────────────┐
│      User Interfaces                │
│  Jupyter | Streamlit | FastAPI      │
└────────────┬────────────────────────┘
             │
┌────────────┴────────────────────────┐
│    Application Layer                │
│  - Model Predictor                  │
│  - Data Loader                      │
│  - Visualizer                       │
└────────────┬────────────────────────┘
             │
┌────────────┴────────────────────────┐
│   Infrastructure                    │
│  Config | Logging | MLflow          │
└─────────────────────────────────────┘
```

**Modular, escalável e testável!**

---

## Slide 13: Funcionalidades

### ✨ O que o Sistema Faz

**1. API REST (FastAPI)**
- Predição individual e em lote
- Documentação automática (Swagger)
- Validação de entrada

**2. Dashboard Interativo (Streamlit)**
- Exploração de dados
- Predição em tempo real
- Visualizações dinâmicas

**3. Pipeline ML**
- Treinamento automatizado
- Cross-validation
- Salvamento de modelos

**4. Testes e CI/CD**
- Testes unitários (pytest)
- Pipeline automatizado (GitHub Actions)

---

## Slide 14: Demonstração - API

### 🌐 FastAPI em Ação

**Exemplo de Requisição:**

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "danceability": 0.75,
    "energy": 0.60,
    "loudness": -10.0,
    "valence": 0.70,
    "tempo": 120.0,
    "duration_ms": 200000
  }'
```

**Resposta:**
```json
{
  "popularity": 67.5,
  "confidence": "High",
  "category": "High Popularity"
}
```

**Documentação:** http://localhost:8000/docs

---

## Slide 15: Demonstração - Dashboard

### 📊 Streamlit Dashboard

**Páginas Disponíveis:**

1. **Overview**
   - Estatísticas do dataset
   - Distribuição de popularidade

2. **Data Explorer**
   - Tabela interativa
   - Heatmap de correlação

3. **Model Prediction**
   - Sliders para features
   - Predição em tempo real

4. **Feature Analysis**
   - Análise individual de features
   - Correlações com popularidade

---

## Slide 16: Resultados e Métricas

### 📊 Performance dos Modelos

**XGBoost (Melhor Modelo):**
- **R² = 0.254**: Explica 25% da variância
- **MAE = 12.48**: Erro médio de ±12.5 pontos
- **CV R² = 0.241 (±0.028)**: Resultado consistente

**Interpretação:**
- ✅ Features musicais têm poder preditivo moderado
- ⚠️ 75% da variância não explicada
- 💡 Fatores externos (marketing, artista, momento) também importam

**Baseline Superado:** Modelo supera predição pela média!

---

## Slide 17: Insights de Negócio

### 💡 Aprendizados Práticos

**Para Artistas:**
- Priorizar loudness e energy na produção
- Músicas dançantes têm maior potencial
- Equilíbrio entre features atrai audiências diversas

**Para Gravadoras:**
- Ferramenta de apoio à decisão
- Identificar músicas com "DNA" de sucesso
- Complementar com análise de marketing

**Para Plataformas:**
- Melhorar curadoria automática
- Segmentação por perfis musicais
- Recomendações mais precisas

---

## Slide 18: Limitações

### ⚠️ Desafios e Limitações

**1. Popularidade é Multifatorial**
- Features musicais = apenas 25% da explicação
- Marketing, viralidade, momento não capturados

**2. Causalidade vs Correlação**
- Modelos identificam padrões, não causas
- Músicas energéticas são populares, mas não causam popularidade

**3. Viés Temporal**
- Popularidade muda ao longo do tempo
- Dataset representa momento específico

**4. Viés de Plataforma**
- Dados específicos do Spotify
- Outras plataformas podem ter padrões diferentes

---

## Slide 19: Trabalhos Futuros

### 🔮 Próximos Passos

**Curto Prazo:**
- ✅ Adicionar mais visualizações
- ✅ Implementar SHAP values
- ✅ Hyperparameter tuning (GridSearchCV)

**Médio Prazo:**
- 📅 Incluir dados temporais (séries temporais)
- 🎤 Adicionar features de artista e contexto
- 📝 NLP em letras das músicas

**Longo Prazo:**
- 🧠 Deep Learning (Redes Neurais, Transformers)
- ☁️ Deploy em cloud (AWS, GCP, Azure)
- 📊 Monitoramento com Prometheus/Grafana
- 🔄 A/B testing de modelos

---

## Slide 20: Contribuições do Projeto

### 🎓 Competências Demonstradas

**Técnicas:**
- ✅ Machine Learning Supervisionado
- ✅ Análise Exploratória de Dados
- ✅ Engenharia de Features
- ✅ Avaliação de Modelos
- ✅ API Development (FastAPI)
- ✅ Web Dashboard (Streamlit)
- ✅ Containerização (Docker)
- ✅ CI/CD (GitHub Actions)
- ✅ Testes Automatizados
- ✅ Documentação Profissional

**Acadêmicas:**
- ✅ Metodologia CRISP-DM completa
- ✅ Análise crítica de resultados
- ✅ Comunicação técnica efetiva

---

## Slide 21: Conclusões

### 🎯 Principais Conclusões

1. **Features musicais têm poder preditivo moderado**
   - R² de 0.25 indica relevância, mas não determinismo

2. **Loudness, Energy e Danceability dominam**
   - Características de intensidade são mais importantes

3. **Modelos baseados em árvores superam lineares**
   - XGBoost > Random Forest > Ridge

4. **Sistema completo e profissional desenvolvido**
   - API, Dashboard, Testes, Docker, CI/CD

5. **Popularidade é fenômeno complexo**
   - Análise de features deve ser complementada com contexto

---

## Slide 22: Repositório e Recursos

### 📚 Onde Encontrar

**GitHub:**
- 📦 Repositório: https://github.com/tavs-coelho/An-lise-Spotify
- 📖 README completo com instruções
- 🐳 Docker-compose para setup rápido

**Documentação:**
- 📄 `docs/API.md` - Documentação da API
- 🏗️ `docs/ARCHITECTURE.md` - Arquitetura do sistema
- 📖 `docs/USAGE.md` - Guia de uso completo

**Notebooks:**
- 📓 `analise_completa_final.ipynb` - Análise exploratória
- 📊 Visualizações e resultados

**Licença:** MIT (uso acadêmico e comercial)

---

## Slide 23: Demonstração ao Vivo

### 🎬 Demo Time!

**O que vamos ver:**

1. ✅ Executar pipeline de treinamento
2. ✅ Fazer predições via API
3. ✅ Interagir com dashboard Streamlit
4. ✅ Visualizar métricas e gráficos

**Comandos:**
```bash
# Treinar modelo
python main.py

# Iniciar API
uvicorn src.api.app:app --reload

# Iniciar Dashboard
streamlit run src/dashboard/app.py
```

---

## Slide 24: Perguntas?

### ❓ Q&A

**Geyson de Araujo**

📧 Contato: GitHub @tavs-coelho  
🔗 Repositório: https://github.com/tavs-coelho/An-lise-Spotify  
📚 Documentação completa disponível

---

**Obrigado pela atenção! 🎵**

---

## Slide 25: Referências

### 📚 Bibliografia

1. GERON, A. *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow*. 3rd ed. O'Reilly Media, 2022.

2. CHEN, T.; GUESTRIN, C. *XGBoost: A Scalable Tree Boosting System*. Proceedings of the 22nd ACM SIGKDD, 2016.

3. SPOTIFY. *Web API Documentation*. https://developer.spotify.com/documentation/web-api/

4. PEDREGOSA, F. et al. *Scikit-learn: Machine Learning in Python*. Journal of Machine Learning Research, v. 12, 2011.

5. FastAPI Documentation. https://fastapi.tiangolo.com/

6. Streamlit Documentation. https://docs.streamlit.io/

---

**Fim da Apresentação**
