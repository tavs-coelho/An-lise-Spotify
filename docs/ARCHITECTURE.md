# 🏗️ Arquitetura do Sistema

## Visão Geral

Este documento descreve a arquitetura técnica do projeto de Análise de Popularidade de Músicas no Spotify, incluindo componentes, fluxos de dados e decisões de design.

## 📐 Diagrama de Arquitetura

```
┌─────────────────────────────────────────────────────────────────┐
│                         User Interface                           │
├───────────────────┬─────────────────┬──────────────────────────┤
│   Jupyter         │   Streamlit     │      FastAPI             │
│   Notebook        │   Dashboard     │      REST API            │
└────────┬──────────┴────────┬────────┴──────────┬───────────────┘
         │                   │                   │
         └───────────────────┴───────────────────┘
                             │
         ┌───────────────────┴───────────────────┐
         │          Application Layer            │
         │                                       │
         │   ┌──────────────────────────────┐   │
         │   │   Model Predictor            │   │
         │   │   - PopularityPredictor      │   │
         │   │   - Model Training           │   │
         │   │   - Predictions              │   │
         │   └──────────────────────────────┘   │
         │                                       │
         │   ┌──────────────────────────────┐   │
         │   │   Data Loader                │   │
         │   │   - Load & Clean Data        │   │
         │   │   - Feature Engineering      │   │
         │   └──────────────────────────────┘   │
         │                                       │
         │   ┌──────────────────────────────┐   │
         │   │   Visualization              │   │
         │   │   - SpotifyVisualizer        │   │
         │   │   - Plot Generation          │   │
         │   └──────────────────────────────┘   │
         └───────────────────────────────────────┘
                             │
         ┌───────────────────┴───────────────────┐
         │         Infrastructure Layer          │
         │                                       │
         │  ┌─────────┐  ┌─────────┐  ┌──────┐ │
         │  │ Config  │  │ Logging │  │MLflow│ │
         │  └─────────┘  └─────────┘  └──────┘ │
         └───────────────────────────────────────┘
                             │
         ┌───────────────────┴───────────────────┐
         │            Data Storage               │
         │                                       │
         │  ┌─────────┐  ┌─────────┐  ┌──────┐ │
         │  │Raw Data │  │ Models  │  │ Logs │ │
         │  └─────────┘  └─────────┘  └──────┘ │
         └───────────────────────────────────────┘
```

## 🎯 Componentes Principais

### 1. User Interface Layer

#### 1.1 Jupyter Notebook
- **Propósito**: Análise exploratória e documentação interativa
- **Arquivo**: `analise_completa_final.ipynb`
- **Características**:
  - Análise exploratória de dados (EDA)
  - Treinamento de modelos step-by-step
  - Visualizações interativas
  - Documentação executável

#### 1.2 Streamlit Dashboard
- **Propósito**: Interface web interativa para análise e predição
- **Arquivo**: `src/dashboard/app.py`
- **Páginas**:
  - Overview: Estatísticas gerais do dataset
  - Data Explorer: Exploração interativa dos dados
  - Model Prediction: Interface de predição em tempo real
  - Feature Analysis: Análise detalhada de features
- **Tecnologias**: Streamlit, Matplotlib, Seaborn

#### 1.3 FastAPI REST API
- **Propósito**: API para integração com outros sistemas
- **Arquivo**: `src/api/app.py`
- **Endpoints**:
  - `GET /`: Informações da API
  - `GET /health`: Health check
  - `POST /predict`: Predição individual
  - `POST /predict/batch`: Predição em lote
- **Tecnologias**: FastAPI, Pydantic, Uvicorn

### 2. Application Layer

#### 2.1 Model Predictor (`src/models/predictor.py`)
**Responsabilidades**:
- Treinamento de modelos ML
- Cross-validation
- Predições
- Salvamento/carregamento de modelos

**Modelos Suportados**:
- Ridge Regression
- Random Forest Regressor
- XGBoost Regressor

**Principais Métodos**:
```python
class PopularityPredictor:
    def create_preprocessor(X)       # Pipeline de pré-processamento
    def train_models(X, y)           # Treinar múltiplos modelos
    def predict(X, model_name)       # Fazer predições
    def save_model(model_name, path) # Salvar modelo
    def load_model(path, model_name) # Carregar modelo
```

#### 2.2 Data Loader (`src/data/loader.py`)
**Responsabilidades**:
- Carregamento de dados
- Limpeza de dados
- Feature engineering
- Geração de dados de amostra

**Principais Métodos**:
```python
class DataLoader:
    def load_data()                  # Carregar CSV ou gerar amostra
    def clean_data(df)               # Limpar dados
    def split_features_target(df)    # Separar X e y
```

#### 2.3 Visualizer (`src/visualization/plots.py`)
**Responsabilidades**:
- Geração de gráficos e visualizações
- Análise visual de dados
- Comparação de modelos

**Principais Métodos**:
```python
class SpotifyVisualizer:
    def plot_feature_distributions()  # Distribuições
    def plot_correlation_heatmap()    # Heatmap de correlação
    def plot_feature_importance()     # Importância de features
    def plot_model_comparison()       # Comparação de modelos
    def plot_actual_vs_predicted()    # Scatter plot
    def plot_residuals()              # Análise de resíduos
```

### 3. Infrastructure Layer

#### 3.1 Configuration Management
- **Arquivo**: `config.yaml`
- **Gerenciamento**: `src/utils/config.py`
- **Conteúdo**:
  - Paths de dados
  - Hiperparâmetros de modelos
  - Configurações de API e Dashboard
  - Configurações de logging

#### 3.2 Logging
- **Configuração**: `src/utils/config.py`
- **Arquivo de log**: `logs/app.log`
- **Níveis**: INFO, WARNING, ERROR, DEBUG

#### 3.3 MLflow (Planejado)
- Rastreamento de experimentos
- Versionamento de modelos
- Registro de métricas e parâmetros

## 🔄 Fluxos de Dados

### Fluxo 1: Treinamento de Modelo

```
1. Carregar configuração (config.yaml)
2. Carregar dados (DataLoader)
3. Limpar e preparar dados
4. Dividir features e target
5. Criar pipeline de pré-processamento
6. Treinar múltiplos modelos
7. Avaliar com cross-validation
8. Comparar métricas (MAE, RMSE, R²)
9. Salvar melhor modelo
10. Gerar visualizações
```

### Fluxo 2: Predição via API

```
1. Receber requisição HTTP POST
2. Validar entrada (Pydantic)
3. Converter para DataFrame
4. Carregar modelo treinado
5. Fazer predição
6. Determinar categoria e confiança
7. Retornar resposta JSON
```

### Fluxo 3: Dashboard Interativo

```
1. Carregar dados e configuração
2. Renderizar interface Streamlit
3. Usuário interage com widgets
4. Processar entrada do usuário
5. Gerar visualizações/predições
6. Atualizar interface
```

## 🛠️ Stack Tecnológico

### Backend
- **Python 3.9+**: Linguagem principal
- **FastAPI**: Framework web
- **Uvicorn**: Servidor ASGI
- **Pydantic**: Validação de dados

### Machine Learning
- **scikit-learn**: Modelos clássicos, pipelines
- **XGBoost**: Gradient boosting
- **pandas/numpy**: Manipulação de dados
- **scipy**: Análise estatística

### Visualização
- **matplotlib**: Plots base
- **seaborn**: Visualizações estatísticas
- **plotly**: Gráficos interativos

### Frontend
- **Streamlit**: Dashboard web
- **Jupyter**: Notebooks interativos

### DevOps
- **Docker**: Containerização
- **docker-compose**: Orquestração
- **pytest**: Testes automatizados
- **GitHub Actions**: CI/CD

## 📦 Estrutura de Diretórios

```
src/
├── __init__.py           # Package initialization
├── data/                 # Data processing
│   ├── __init__.py
│   └── loader.py
├── models/               # ML models
│   ├── __init__.py
│   └── predictor.py
├── visualization/        # Plotting
│   ├── __init__.py
│   └── plots.py
├── api/                  # REST API
│   ├── __init__.py
│   └── app.py
├── dashboard/            # Web dashboard
│   ├── __init__.py
│   └── app.py
└── utils/                # Utilities
    ├── __init__.py
    └── config.py
```

## 🔐 Segurança

### Validação de Entrada
- Pydantic schemas para validação de tipos
- Ranges de valores para features musicais
- Tratamento de erros robusto

### Logging
- Registro de todas as operações críticas
- Tracking de erros e exceções
- Logs estruturados com timestamps

### Boas Práticas
- Separação de configuração do código
- Variáveis de ambiente para secrets
- Princípio do menor privilégio

## 🚀 Deployment

### Opções de Deploy

#### 1. Local
```bash
python main.py
```

#### 2. Docker
```bash
docker-compose up
```

#### 3. Cloud (Planejado)
- AWS (EC2, ECS, Lambda)
- GCP (Cloud Run, App Engine)
- Azure (App Service, Container Instances)

## 📊 Monitoramento

### Métricas de Sistema
- CPU usage
- Memory usage
- Request latency
- Error rates

### Métricas de Modelo
- Prediction accuracy
- Response times
- Model drift
- Data quality

## 🔄 Versionamento

### Código
- Git/GitHub para controle de versão
- Semantic versioning (v1.0.0)

### Modelos
- Joblib para serialização
- Versionamento por timestamp/hash
- MLflow para tracking (planejado)

### Dados
- DVC (Data Version Control) - planejado
- Checksums para integridade

## 🎓 Decisões de Design

### Por que FastAPI?
- Performance superior (baseado em Starlette/Pydantic)
- Documentação automática (OpenAPI)
- Type hints nativos
- Async support

### Por que Streamlit?
- Prototipagem rápida
- Foco em data science
- Componentes prontos
- Deploy simples

### Por que XGBoost?
- Melhor performance em dados tabulares
- Feature importance built-in
- Regularização integrada
- Treinamento eficiente

### Por que Docker?
- Reprodutibilidade
- Isolamento de dependências
- Portabilidade
- Facilita deploy

## 📚 Referências

- [FastAPI Best Practices](https://fastapi.tiangolo.com/tutorial/)
- [Scikit-learn Pipeline](https://scikit-learn.org/stable/modules/compose.html)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [Streamlit Documentation](https://docs.streamlit.io/)
