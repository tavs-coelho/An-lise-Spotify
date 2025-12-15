# 📖 Guia de Uso

Este guia fornece instruções detalhadas sobre como usar o sistema de Análise de Popularidade de Músicas no Spotify.

## 🎯 Casos de Uso

### 1. Análise Exploratória de Dados

#### Usando Jupyter Notebook

```bash
# Iniciar Jupyter
jupyter notebook

# Abrir analise_completa_final.ipynb
# Execute as células sequencialmente
```

**O que você encontrará:**
- Estatísticas descritivas do dataset
- Análise de distribuições
- Correlações entre features
- Visualizações interativas

### 2. Treinamento de Modelos

#### Usando o script principal

```bash
# Executar pipeline completo
python main.py
```

**O que acontece:**
1. Carrega configuração do `config.yaml`
2. Carrega e limpa os dados
3. Treina múltiplos modelos (Ridge, Random Forest, XGBoost)
4. Compara métricas (MAE, RMSE, R²)
5. Salva o melhor modelo em `models/xgboost_model.pkl`
6. Gera logs em `logs/app.log`

**Saída esperada:**
```
================================================================================
Spotify Music Popularity Analysis - Starting
================================================================================

1. Loading and preparing data...
Generated 1000 sample records
Cleaned data. Final shape: (1000, 17)
Features shape: (1000, 13), Target shape: (1000,)

2. Training machine learning models...
Training Ridge...
Ridge - MAE: 14.25, RMSE: 18.92, R²: 0.182, CV R²: 0.178 (±0.023)
Training RandomForest...
RandomForest - MAE: 13.15, RMSE: 17.58, R²: 0.228, CV R²: 0.215 (±0.031)
Training XGBoost...
XGBoost - MAE: 12.48, RMSE: 16.92, R²: 0.254, CV R²: 0.241 (±0.028)

3. Model Comparison Results:
--------------------------------------------------------------------------------
Model           MAE        RMSE       R²         CV R²
--------------------------------------------------------------------------------
Ridge           14.25      18.92      0.182      0.178 (±0.023)
RandomForest    13.15      17.58      0.228      0.215 (±0.031)
XGBoost         12.48      16.92      0.254      0.241 (±0.028)
```

### 3. Fazer Predições

#### Opção A: Via Python

```python
from src.utils.config import load_config
from src.models.predictor import PopularityPredictor
import pandas as pd

# Carregar configuração e modelo
config = load_config('config.yaml')
predictor = PopularityPredictor(config)
predictor.load_model('models/xgboost_model.pkl', 'XGBoost')

# Preparar features
features = pd.DataFrame([{
    'danceability': 0.75,
    'energy': 0.60,
    'loudness': -10.0,
    'speechiness': 0.05,
    'acousticness': 0.30,
    'instrumentalness': 0.0,
    'liveness': 0.10,
    'valence': 0.70,
    'tempo': 120.0,
    'duration_ms': 200000,
    'key': 0,
    'mode': 1,
    'time_signature': 4
}])

# Fazer predição
prediction = predictor.predict(features, 'XGBoost')
print(f"Popularidade prevista: {prediction[0]:.1f}")
```

#### Opção B: Via API REST

```bash
# Iniciar a API
python -m uvicorn src.api.app:app --reload

# Em outro terminal, fazer requisição
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "danceability": 0.75,
    "energy": 0.60,
    "loudness": -10.0,
    "speechiness": 0.05,
    "acousticness": 0.30,
    "instrumentalness": 0.0,
    "liveness": 0.10,
    "valence": 0.70,
    "tempo": 120.0,
    "duration_ms": 200000
  }'
```

#### Opção C: Via Dashboard

```bash
# Iniciar dashboard
streamlit run src/dashboard/app.py

# Acessar http://localhost:8501
# Navegar para "Model Prediction"
# Ajustar sliders com as features desejadas
# Clicar em "Predict Popularity"
```

### 4. Visualizar Dados

#### Usando SpotifyVisualizer

```python
from src.visualization.plots import SpotifyVisualizer
from src.data.loader import DataLoader
from src.utils.config import load_config

# Carregar dados
config = load_config('config.yaml')
loader = DataLoader(config)
df = loader.load_data()

# Criar visualizador
viz = SpotifyVisualizer()

# Plotar distribuições
features = ['danceability', 'energy', 'valence']
fig = viz.plot_feature_distributions(df, features)
plt.show()

# Plotar correlação
fig = viz.plot_correlation_heatmap(df)
plt.show()
```

### 5. Executar Testes

```bash
# Todos os testes
pytest tests/ -v

# Teste específico
pytest tests/test_predictor.py -v

# Com cobertura
pytest tests/ --cov=src --cov-report=html

# Ver relatório
open htmlcov/index.html
```

## 🐳 Usando Docker

### Setup Completo

```bash
# Build e start todos os serviços
docker-compose up --build

# Serviços disponíveis:
# - API: http://localhost:8000
# - Dashboard: http://localhost:8501
```

### Serviços Individuais

```bash
# Apenas treinar modelo
docker-compose run app python main.py

# Apenas API
docker-compose up api

# Apenas Dashboard
docker-compose up dashboard
```

## ⚙️ Configuração

### Arquivo config.yaml

```yaml
# Ajustar paths de dados
data:
  raw_path: "data/raw/spotify_songs.csv"
  processed_path: "data/processed/processed_data.csv"

# Modificar hiperparâmetros de modelo
xgboost:
  n_estimators: 200  # Aumentar árvores
  max_depth: 8       # Aumentar profundidade
  learning_rate: 0.05 # Diminuir learning rate
```

### Variáveis de Ambiente

```bash
# .env file (criar se necessário)
export PYTHONPATH=/app
export LOG_LEVEL=INFO
```

## 📊 Interpretando Resultados

### Métricas de Regressão

- **MAE (Mean Absolute Error)**
  - Erro médio absoluto
  - Quanto menor, melhor
  - Interpretação: Em média, o modelo erra ±X pontos na escala 0-100

- **RMSE (Root Mean Squared Error)**
  - Penaliza erros grandes
  - Quanto menor, melhor
  - Similar ao MAE, mas mais sensível a outliers

- **R² (Coefficient of Determination)**
  - Quanto da variância é explicada
  - Range: 0 a 1
  - Interpretação: R²=0.25 significa que o modelo explica 25% da variância na popularidade

### Categorias de Popularidade

- **Alta**: 67-100 pontos
- **Média**: 34-66 pontos
- **Baixa**: 0-33 pontos

## 🔍 Troubleshooting

### Problema: Model not found

```bash
# Solução: Treinar o modelo primeiro
python main.py
```

### Problema: Módulo não encontrado

```bash
# Solução: Instalar dependências
pip install -r requirements.txt

# Ou usar ambiente virtual
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Problema: Porta já em uso

```bash
# API em outra porta
uvicorn src.api.app:app --port 8001

# Dashboard em outra porta
streamlit run src/dashboard/app.py --server.port 8502
```

### Problema: Dados não encontrados

```
# O sistema gera dados de amostra automaticamente
# Para usar dados reais, coloque em:
data/raw/spotify_songs.csv
```

## 📚 Exemplos Práticos

### Exemplo 1: Prever Popularidade de Músicas Reais

```python
# Características de "Blinding Lights - The Weeknd"
features = {
    'danceability': 0.514,
    'energy': 0.730,
    'loudness': -5.934,
    'speechiness': 0.0598,
    'acousticness': 0.00146,
    'instrumentalness': 0.0000234,
    'liveness': 0.0902,
    'valence': 0.334,
    'tempo': 171.005,
    'duration_ms': 200040
}

# Fazer predição
prediction = predictor.predict(pd.DataFrame([features]), 'XGBoost')
print(f"Popularidade prevista: {prediction[0]:.1f}")
# Saída esperada: ~85 (Alta popularidade)
```

### Exemplo 2: Comparar Múltiplas Músicas

```python
tracks = [
    {'name': 'Upbeat Pop', 'danceability': 0.8, 'energy': 0.9, 'valence': 0.8},
    {'name': 'Sad Ballad', 'danceability': 0.3, 'energy': 0.2, 'valence': 0.2},
    {'name': 'Electronic', 'danceability': 0.7, 'energy': 0.8, 'valence': 0.6}
]

for track in tracks:
    # Completar com features padrão
    features = {**track, 'loudness': -10, 'tempo': 120, ...}
    pred = predictor.predict(pd.DataFrame([features]), 'XGBoost')
    print(f"{track['name']}: {pred[0]:.1f}")
```

### Exemplo 3: Análise de Sensibilidade

```python
# Como a danceability afeta popularidade?
import numpy as np

danceability_range = np.linspace(0, 1, 20)
predictions = []

base_features = {
    'energy': 0.6, 'loudness': -10, 'speechiness': 0.05,
    'acousticness': 0.3, 'instrumentalness': 0.0,
    'liveness': 0.1, 'valence': 0.7, 'tempo': 120,
    'duration_ms': 200000
}

for dance in danceability_range:
    features = {**base_features, 'danceability': dance}
    pred = predictor.predict(pd.DataFrame([features]), 'XGBoost')
    predictions.append(pred[0])

# Plotar
plt.plot(danceability_range, predictions)
plt.xlabel('Danceability')
plt.ylabel('Predicted Popularity')
plt.title('Impact of Danceability on Popularity')
plt.show()
```

## 💡 Dicas e Melhores Práticas

1. **Sempre validar dados de entrada**
   - Verificar ranges de valores
   - Tratar missing values
   - Normalizar features se necessário

2. **Monitorar performance do modelo**
   - Avaliar regularmente com dados novos
   - Retreinar periodicamente
   - Comparar com baseline

3. **Usar cross-validation**
   - Evita overfitting
   - Fornece estimativa mais robusta de performance

4. **Documentar experimentos**
   - Registrar hiperparâmetros
   - Salvar métricas
   - Versionar modelos

5. **Interpretar resultados com cuidado**
   - Popularidade é multifatorial
   - Features musicais são apenas parte da história
   - Correlação ≠ Causalidade

## 🆘 Suporte

Para ajuda adicional:
- Consulte a documentação no diretório `docs/`
- Veja exemplos no notebook `analise_completa_final.ipynb`
- Abra uma issue no GitHub
- Leia o arquivo `CONTRIBUTING.md` para contribuir
