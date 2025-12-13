# 🎵 Análise de Popularidade de Músicas no Spotify

## 📊 Projeto Final - Aprendizagem de Máquina

**Autor:** Geyson de Araujo  
**Data:** Dezembro/2025  
**Curso:** Ciência de Dados  
**Repositório:** https://github.com/tavs-coelho/An-lise-Spotify

---

## 🎯 Sobre o Projeto

Este projeto aplica o ciclo completo de **CRISP-DM** para prever a popularidade de músicas no Spotify com base em suas características musicais. Utilizamos técnicas de **Aprendizagem de Máquina Supervisionada** (Regressão e Classificação), **Não Supervisionada** (Clustering) e **Sistemas de Recomendação**.

### Problema de Negócio
Como prever a popularidade de músicas baseado em features musicais objetivas (danceability, energy, valence, etc.) para auxiliar artistas, gravadoras e plataformas de streaming?

---

## 📁 Estrutura do Projeto

```
An-lise-Spotify/
├── 1_entendimento_negocio.md       # Contexto e objetivos do projeto
├── analise_completa_final.ipynb    # Notebook completo com todas as análises
├── relatorio_tecnico.md            # Relatório técnico detalhado
├── apresentacao.md                 # Slides da apresentação
├── spotify_songs.csv               # Dataset (113.999 músicas)
└── README.md                       # Este arquivo
```

---

## 🔬 Metodologia (CRISP-DM)

### 1. **Entendimento do Negócio**
- Definição do problema: prever popularidade musical
- Identificação de KPIs: R² > 0.20, MAE < 15
- Formulação de 5 perguntas de negócio

### 2. **Entendimento dos Dados**
- Dataset: 113.999 músicas do Spotify
- 23 variáveis (9 features musicais principais)
- Análise exploratória completa (EDA)

### 3. **Preparação dos Dados**
- Tratamento de valores faltantes
- Padronização (StandardScaler)
- Split treino/teste (80/20)
- Pipeline de pré-processamento

### 4. **Modelagem**

#### Regressão (Predição de Popularidade)
- Ridge Regression
- Lasso
- ElasticNet
- Random Forest Regressor
- Gradient Boosting
- **XGBoost** ⭐ (melhor desempenho)

#### Classificação (Alta/Média/Baixa Popularidade)
- Random Forest Classifier
- Matriz de Confusão

#### Clustering (Perfis Musicais)
- K-Means (4 clusters)
- Visualização com PCA

#### Sistema de Recomendação
- Similaridade de Cosseno
- Recomendações baseadas em features musicais

### 5. **Avaliação**
- Métricas: MAE, RMSE, R², Accuracy, Precision, Recall, F1-Score, Silhouette
- Comparação crítica entre modelos
- Dashboard com visualizações integradas

### 6. **Implantação**
- Documentação completa no GitHub
- Notebook executável
- Relatório técnico e apresentação

---

## 📈 Principais Resultados

### 🏆 Melhor Modelo: XGBoost
- **R²**: ~0.25 (explica 25% da variância)
- **MAE**: ~12.5 pontos (erro médio aceitável)

### 🎯 Features Mais Importantes
1. **Loudness** (volume)
2. **Energy** (intensidade)
3. **Danceability** (dançabilidade)
4. **Valence** (positividade)
5. **Acousticness** (acústico)

### 📊 Insights Principais
- Features musicais explicam parcialmente a popularidade (~25%)
- Fatores externos (marketing, artista, momento) também são críticos
- Modelos baseados em árvores superam modelos lineares
- Existem 4 perfis distintos de músicas (clusters)

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8+
- Jupyter Notebook

### Instalação

```bash
# 1. Clonar o repositório
git clone https://github.com/tavs-coelho/An-lise-Spotify.git
cd An-lise-Spotify

# 2. Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 3. Instalar dependências
pip install pandas numpy matplotlib seaborn scikit-learn xgboost jupyter scipy

# 4. Abrir o notebook
jupyter notebook analise_completa_final.ipynb
```

### Execução
No Jupyter Notebook:
- **Opção 1**: Execute célula por célula (`Shift + Enter`)
- **Opção 2**: Execute tudo de uma vez (`Cell → Run All`)

---

## 📚 Bibliotecas Utilizadas

```python
# Manipulação de dados
pandas, numpy

# Visualização
matplotlib, seaborn

# Machine Learning
scikit-learn, xgboost

# Análise estatística
scipy
```

---

## 📊 Visualizações Principais

- ✅ Distribuição de Popularidade
- ✅ Matriz de Correlação (Heatmap)
- ✅ Feature Importance (XGBoost)
- ✅ Comparação de Modelos (MAE e R²)
- ✅ Real vs Predito (Scatter)
- ✅ Matriz de Confusão (Classificação)
- ✅ Clusters Musicais (PCA)
- ✅ Dashboard Integrado

---

## 🎯 Competências Demonstradas

✅ Análise Exploratória de Dados (EDA)  
✅ Visualização de Dados  
✅ Feature Engineering  
✅ Machine Learning Supervisionado (Regressão e Classificação)  
✅ Machine Learning Não Supervisionado (Clustering)  
✅ Sistemas de Recomendação  
✅ Avaliação e Comparação de Modelos  
✅ Interpretação de Resultados  
✅ Comunicação Técnica  

---

## 📝 Limitações

1. **Popularidade é multifatorial**: características musicais são apenas parte da explicação
2. **Dados históricos**: popularidade muda ao longo do tempo
3. **Viés de plataforma**: dados específicos do Spotify
4. **Causalidade**: correlações não implicam causalidade

---

## 🔮 Trabalhos Futuros

- Incluir dados temporais (tendências ao longo do tempo)
- Adicionar informações de contexto (artista, gravadora, playlists)
- Aplicar técnicas de NLP em letras das músicas
- Testar modelos de Deep Learning (Redes Neurais)
- Implementar API para predição em tempo real

---

## 📖 Referências

- GERON, A. *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow*. O'Reilly, 2022.
- Spotify Web API Documentation
- Scikit-learn Documentation
- XGBoost Documentation

---

## 📧 Contato

**Geyson de Araujo**  
GitHub: [@tavs-coelho](https://github.com/tavs-coelho)  
Repositório: [An-lise-Spotify](https://github.com/tavs-coelho/An-lise-Spotify)

---

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos.

---

**⭐ Se este projeto foi útil, deixe uma estrela no repositório!**