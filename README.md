# 🎵 Análise de Popularidade de Músicas no Spotify

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen)

</div>

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
├── src/                            # Código fonte principal
│   ├── data/                       # Módulos de processamento de dados
│   │   └── loader.py              # Carregamento e preparação de dados
│   ├── models/                    # Módulos de modelagem ML
│   │   └── predictor.py          # Treinamento e predição
│   ├── visualization/             # Módulos de visualização
│   │   └── plots.py              # Gráficos e análises visuais
│   ├── api/                       # API REST (FastAPI)
│   │   └── app.py                # Endpoints da API
│   ├── dashboard/                 # Dashboard interativo
│   │   └── app.py                # Interface Streamlit
│   └── utils/                     # Utilitários e configurações
│       └── config.py             # Gerenciamento de configurações
├── tests/                         # Testes automatizados
│   ├── test_data_loader.py       # Testes de carregamento de dados
│   └── test_predictor.py         # Testes de modelos
├── docs/                          # Documentação completa
│   ├── QUICKSTART.md             # Guia de início rápido
│   ├── USAGE.md                  # Guia de uso detalhado
│   ├── API.md                    # Documentação da API
│   ├── ARCHITECTURE.md           # Arquitetura do sistema
│   ├── PRESENTATION.md           # Slides da apresentação
│   └── references.bib            # Referências em BibTeX
├── data/                          # Dados brutos e processados
│   ├── raw/                      # Dados originais
│   └── processed/                # Dados preprocessados
├── models/                        # Modelos treinados salvos
├── logs/                          # Logs da aplicação
├── .github/workflows/            # Pipelines CI/CD
│   └── ci.yml                   # Workflow de integração contínua
├── 1_entendimento_negocio.md     # Contexto e objetivos (legacy)
├── analise_completa_final.ipynb  # Notebook completo de análise
├── relatorio_tecnico.md          # Relatório técnico detalhado (legacy)
├── *.py (root)                   # Scripts Python originais (legacy)
├── config.yaml                   # Configurações do projeto
├── requirements.txt              # Dependências Python
├── Dockerfile                    # Container Docker
├── docker-compose.yml            # Orquestração de serviços
├── setup.sh                      # Script de instalação automática
├── main.py                       # Script principal
├── CHANGELOG.md                  # Histórico de mudanças
├── LICENSE                       # Licença MIT
├── CONTRIBUTING.md               # Guia de contribuição
└── README.md                     # Este arquivo
```

**Nota sobre scripts legacy:** Os arquivos Python na raiz (`import_libraries.py`, `train_*.py`, etc.) são scripts originais mantidos para referência. O código de produção está organizado no diretório `src/`.

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
- Python 3.9+ 
- Docker (opcional, para containerização)
- Git

### 🔧 Instalação Local

```bash
# 1. Clonar o repositório
git clone https://github.com/tavs-coelho/An-lise-Spotify.git
cd An-lise-Spotify

# 2. Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Executar análise principal
python main.py
```

### 📓 Executar Jupyter Notebook

```bash
# Iniciar Jupyter
jupyter notebook

# Abrir analise_completa_final.ipynb
# Execute célula por célula (Shift + Enter)
# Ou execute tudo (Cell → Run All)
```

### 🐳 Executar com Docker

```bash
# Construir imagem
docker build -t spotify-analytics .

# Executar análise principal
docker run spotify-analytics

# Ou usar docker-compose para todos os serviços
docker-compose up

# Acessar serviços:
# - API: http://localhost:8000
# - Dashboard: http://localhost:8501
# - Documentação API: http://localhost:8000/docs
```

### 🌐 Executar API REST

```bash
# Iniciar servidor FastAPI
python -m uvicorn src.api.app:app --reload

# Acessar:
# - API: http://localhost:8000
# - Documentação interativa: http://localhost:8000/docs
# - Documentação alternativa: http://localhost:8000/redoc
```

### 📊 Executar Dashboard Interativo

```bash
# Iniciar dashboard Streamlit
streamlit run src/dashboard/app.py

# Acessar: http://localhost:8501
```

### 🧪 Executar Testes

```bash
# Executar todos os testes
pytest tests/ -v

# Executar com cobertura
pytest tests/ --cov=src --cov-report=html

# Ver relatório de cobertura
open htmlcov/index.html  # Linux/Mac
# start htmlcov/index.html  # Windows
```

---

## 📚 Tecnologias e Bibliotecas

### Core Data Science
- **pandas** - Manipulação e análise de dados
- **numpy** - Computação numérica
- **scipy** - Análise estatística avançada

### Machine Learning
- **scikit-learn** - Modelos clássicos de ML, pré-processamento, métricas
- **xgboost** - Gradient boosting otimizado
- **imbalanced-learn** - Técnicas para dados desbalanceados

### Visualização
- **matplotlib** - Gráficos base
- **seaborn** - Visualizações estatísticas
- **plotly** - Gráficos interativos

### Interpretabilidade
- **shap** - Explicação de modelos (SHAP values)

### MLOps e Experimentação
- **mlflow** - Rastreamento de experimentos e versionamento de modelos

### API e Web
- **fastapi** - Framework web moderno para APIs REST
- **uvicorn** - Servidor ASGI de alta performance
- **streamlit** - Dashboard interativo

### Validação e Configuração
- **pydantic** - Validação de dados e settings
- **pyyaml** - Gerenciamento de configurações

### Desenvolvimento e Testes
- **pytest** - Framework de testes
- **black** - Formatação de código
- **flake8** - Linting
- **mypy** - Type checking

### Deployment
- **Docker** - Containerização
- **docker-compose** - Orquestração de containers

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

### Técnicas de Machine Learning
✅ Análise Exploratória de Dados (EDA)  
✅ Visualização de Dados  
✅ Feature Engineering  
✅ Machine Learning Supervisionado (Regressão e Classificação)  
✅ Machine Learning Não Supervisionado (Clustering)  
✅ Sistemas de Recomendação  
✅ Avaliação e Comparação de Modelos  
✅ Interpretação de Resultados  

### Engenharia de Software
✅ Arquitetura de Software (Modular e Escalável)  
✅ API REST (FastAPI)  
✅ Web Development (Streamlit)  
✅ Testes Automatizados (pytest)  
✅ CI/CD (GitHub Actions)  
✅ Containerização (Docker)  
✅ Documentação Técnica  
✅ Type Hints e Validação (Pydantic)  
✅ Logging e Monitoramento  
✅ Git/GitHub  

### Habilidades Acadêmicas
✅ Metodologia CRISP-DM  
✅ Pesquisa Bibliográfica  
✅ Análise Crítica de Resultados  
✅ Comunicação Técnica  
✅ Apresentação de Resultados  

---

## 📝 Limitações

1. **Popularidade é multifatorial**: características musicais são apenas parte da explicação
2. **Dados históricos**: popularidade muda ao longo do tempo
3. **Viés de plataforma**: dados específicos do Spotify
4. **Causalidade**: correlações não implicam causalidade

---

## ✨ Funcionalidades Principais

### 🤖 Machine Learning Pipeline
- ✅ Treinamento automático de múltiplos modelos (Ridge, Random Forest, XGBoost)
- ✅ Cross-validation e métricas de avaliação completas
- ✅ Salvamento e versionamento de modelos
- ✅ Feature importance e interpretabilidade (SHAP)

### 🌐 API REST (FastAPI)
- ✅ Endpoints para predição individual e em lote
- ✅ Documentação interativa automática (Swagger/OpenAPI)
- ✅ Validação de entrada com Pydantic
- ✅ Health checks e monitoramento

### 📊 Dashboard Interativo (Streamlit)
- ✅ Visualização de dados exploratória
- ✅ Interface para predição em tempo real
- ✅ Análise de features e correlações
- ✅ Gráficos interativos e métricas

### 🐳 Deployment
- ✅ Containerização com Docker
- ✅ Orquestração multi-serviço com docker-compose
- ✅ CI/CD com GitHub Actions
- ✅ Testes automatizados

## 🔮 Trabalhos Futuros

- [ ] Incluir dados temporais (análise de séries temporais)
- [ ] Adicionar informações de contexto (artista, gravadora, playlists)
- [ ] Aplicar técnicas de NLP em letras das músicas
- [ ] Testar modelos de Deep Learning (Redes Neurais, Transformers)
- [ ] Implementar modelo de recomendação baseado em collaborative filtering
- [ ] Adicionar autenticação e autorização na API
- [ ] Deploy em cloud (AWS, GCP, Azure)
- [ ] Monitoramento de performance em produção com Prometheus/Grafana
- [ ] A/B testing framework para comparação de modelos
- [ ] Feature store para gerenciamento de features

---

## 📖 Referências

### Livros
- GERON, A. *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow*. O'Reilly, 2022.
- LESKOVEC, J.; RAJARAMAN, A.; ULLMAN, J. *Mining of Massive Datasets*. Cambridge University Press, 2020.
- HASTIE, T.; TIBSHIRANI, R.; FRIEDMAN, J. *The Elements of Statistical Learning*. Springer, 2009.

### Artigos Científicos
- CHEN, T.; GUESTRIN, C. *XGBoost: A Scalable Tree Boosting System*. KDD, 2016.
- PEDREGOSA, F. et al. *Scikit-learn: Machine Learning in Python*. JMLR, 2011.
- BREIMAN, L. *Random Forests*. Machine Learning, 2001.

### Documentação Técnica
- [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)

### Referências Completas
📚 Veja arquivo completo em formato BibTeX: [`docs/references.bib`](docs/references.bib)

---

## 📧 Contato

**Geyson de Araujo**  
GitHub: [@tavs-coelho](https://github.com/tavs-coelho)  
Repositório: [An-lise-Spotify](https://github.com/tavs-coelho/An-lise-Spotify)

## 📑 Documentação Adicional

- 🚀 [**Guia de Início Rápido**](docs/QUICKSTART.md) - Comece em minutos!
- 📖 [Guia de Uso Completo](docs/USAGE.md)
- 🌐 [Documentação da API](docs/API.md)
- 🏗️ [Arquitetura do Sistema](docs/ARCHITECTURE.md)
- 📊 [Apresentação do Projeto](docs/PRESENTATION.md)
- 📚 [Referências Bibliográficas](docs/references.bib)

---

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos.

---

**⭐ Se este projeto foi útil, deixe uma estrela no repositório!**