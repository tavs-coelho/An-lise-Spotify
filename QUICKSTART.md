# Guia de Início Rápido

Este guia irá ajudá-lo a começar com o projeto de Análise de Popularidade de Músicas no Spotify em 5 minutos.

## Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git

## Opção 1: Demo Rápida com Docker (Mais Rápida) 🐳

```bash
# 1. Clone o repositório
git clone https://github.com/tavs-coelho/An-lise-Spotify.git
cd An-lise-Spotify

# 2. Inicie com Docker Compose
docker-compose up -d

# 3. Acesse os serviços
# - API: http://localhost:8000/docs
# - Dashboard: http://localhost:8501
```

Pronto! 🎉

## Opção 2: Instalação Local (Recomendada para Desenvolvimento) 💻

### Passo 1: Clone e Configure

```bash
# Clone o repositório
git clone https://github.com/tavs-coelho/An-lise-Spotify.git
cd An-lise-Spotify

# Crie ambiente virtual
python -m venv venv

# Ative o ambiente virtual
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instale dependências
pip install -r requirements.txt
pip install -e .
```

### Passo 2: Escolha Sua Interface

#### A. Dashboard Interativo (Mais Fácil)

```bash
streamlit run app.py
```

Depois abra seu navegador em `http://localhost:8501`

#### B. API REST

```bash
uvicorn api:app --reload
```

Documentação da API disponível em `http://localhost:8000/docs`

#### C. Jupyter Notebook

```bash
jupyter notebook notebooks/analise_completa_final.ipynb
```

#### D. Código Python

```python
from spotify_analysis.models import ModelTrainer
from spotify_analysis.data import DataLoader, DataPreprocessor
import numpy as np

# Crie dados de exemplo
X_train = np.random.randn(100, 10)
y_train = np.random.randint(0, 100, 100)

# Treine o modelo
trainer = ModelTrainer('xgboost')
trainer.fit(X_train, y_train)

# Faça predições
X_test = np.random.randn(20, 10)
predictions = trainer.predict(X_test)
print(predictions)
```

## Opção 3: Teste a API 🚀

### Usando cURL

```bash
# Verificação de saúde
curl http://localhost:8000/health

# Faça uma predição
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "danceability": 0.735,
    "energy": 0.578,
    "loudness": -5.594,
    "speechiness": 0.0461,
    "acousticness": 0.514,
    "instrumentalness": 0.0000124,
    "liveness": 0.127,
    "valence": 0.693,
    "tempo": 123.0
  }'
```

### Usando Python requests

```python
import requests

url = "http://localhost:8000/predict"
data = {
    "danceability": 0.735,
    "energy": 0.578,
    "loudness": -5.594,
    "speechiness": 0.0461,
    "acousticness": 0.514,
    "instrumentalness": 0.0000124,
    "liveness": 0.127,
    "valence": 0.693,
    "tempo": 123.0
}

response = requests.post(url, json=data)
print(response.json())
```

## Próximos Passos 📚

1. **Explore o Dashboard:** Teste diferentes combinações de features para ver como elas afetam a popularidade
2. **Leia a Documentação:** Confira o [README](README.md) e [Relatório Técnico](docs/relatorio_tecnico.md)
3. **Execute os Testes:** `pytest tests/`
4. **Contribua:** Veja [CONTRIBUTING.md](CONTRIBUTING.md)

## Comandos Comuns 🛠️

```bash
# Execute testes
pytest

# Formate código
black src/ tests/

# Lint de código
flake8 src/ tests/

# Verificação de tipos
mypy src/

# Execute todas as verificações de qualidade
make quality

# Inicie API
make run-api

# Inicie dashboard
make run-dashboard
```

## Solução de Problemas 🔧

### Erros de Importação

```bash
# Certifique-se de estar no ambiente virtual
source venv/bin/activate

# Reinstale o pacote
pip install -e .
```

### Porta Já em Uso

```bash
# Para API (mude a porta)
uvicorn api:app --port 8001

# Para Streamlit (mude a porta)
streamlit run app.py --server.port 8502
```

### Problemas com Docker

```bash
# Reconstrua os containers
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

## Precisa de Ajuda? 💬

- 📖 Confira a [documentação completa](README.md)
- 🐛 [Reporte problemas](https://github.com/tavs-coelho/An-lise-Spotify/issues)
- 💡 [Inicie uma discussão](https://github.com/tavs-coelho/An-lise-Spotify/discussions)

Boas análises! 🎵✨
