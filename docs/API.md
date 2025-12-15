# 🌐 API Documentation

## Visão Geral

A API REST do projeto Spotify Music Analytics foi desenvolvida usando FastAPI, fornecendo endpoints para predição de popularidade musical baseada em características de áudio.

## 🚀 Início Rápido

### Iniciar o Servidor

```bash
# Método 1: Usando Python diretamente
python -m uvicorn src.api.app:app --reload

# Método 2: Usando Docker
docker-compose up api

# Método 3: A partir do código
cd src/api
python app.py
```

O servidor estará disponível em: `http://localhost:8000`

## 📚 Documentação Interativa

FastAPI gera automaticamente documentação interativa:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔌 Endpoints

### 1. Root Endpoint

**GET /** - Informações básicas da API

```bash
curl http://localhost:8000/
```

**Resposta:**
```json
{
  "message": "Spotify Music Popularity Prediction API",
  "version": "1.0.0",
  "endpoints": {
    "/predict": "POST - Predict popularity for a single track",
    "/predict/batch": "POST - Predict popularity for multiple tracks",
    "/health": "GET - Health check"
  }
}
```

### 2. Health Check

**GET /health** - Verificar status da API e modelo

```bash
curl http://localhost:8000/health
```

**Resposta:**
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

### 3. Predição Individual

**POST /predict** - Prever popularidade de uma música

**Request Body:**
```json
{
  "danceability": 0.735,
  "energy": 0.578,
  "loudness": -11.84,
  "speechiness": 0.0598,
  "acousticness": 0.514,
  "instrumentalness": 0.0000234,
  "liveness": 0.0902,
  "valence": 0.636,
  "tempo": 121.274,
  "duration_ms": 200000,
  "key": 0,
  "mode": 1,
  "time_signature": 4
}
```

**Exemplo usando cURL:**
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "danceability": 0.735,
    "energy": 0.578,
    "loudness": -11.84,
    "speechiness": 0.0598,
    "acousticness": 0.514,
    "instrumentalness": 0.0000234,
    "liveness": 0.0902,
    "valence": 0.636,
    "tempo": 121.274,
    "duration_ms": 200000
  }'
```

**Exemplo usando Python:**
```python
import requests

url = "http://localhost:8000/predict"
data = {
    "danceability": 0.735,
    "energy": 0.578,
    "loudness": -11.84,
    "speechiness": 0.0598,
    "acousticness": 0.514,
    "instrumentalness": 0.0000234,
    "liveness": 0.0902,
    "valence": 0.636,
    "tempo": 121.274,
    "duration_ms": 200000
}

response = requests.post(url, json=data)
print(response.json())
```

**Resposta:**
```json
{
  "popularity": 67.5,
  "confidence": "High",
  "category": "High Popularity"
}
```

### 4. Predição em Lote

**POST /predict/batch** - Prever popularidade de múltiplas músicas

**Request Body:**
```json
[
  {
    "danceability": 0.735,
    "energy": 0.578,
    "loudness": -11.84,
    "speechiness": 0.0598,
    "acousticness": 0.514,
    "instrumentalness": 0.0000234,
    "liveness": 0.0902,
    "valence": 0.636,
    "tempo": 121.274,
    "duration_ms": 200000
  },
  {
    "danceability": 0.5,
    "energy": 0.6,
    "loudness": -10.0,
    "speechiness": 0.05,
    "acousticness": 0.3,
    "instrumentalness": 0.0,
    "liveness": 0.1,
    "valence": 0.7,
    "tempo": 120.0,
    "duration_ms": 180000
  }
]
```

**Resposta:**
```json
{
  "predictions": [
    {
      "popularity": 67.5,
      "category": "High Popularity"
    },
    {
      "popularity": 52.3,
      "category": "Medium Popularity"
    }
  ]
}
```

## 📋 Schema de Dados

### MusicFeatures (Input)

| Campo | Tipo | Range | Descrição |
|-------|------|-------|-----------|
| `danceability` | float | 0.0 - 1.0 | Quão adequada para dançar |
| `energy` | float | 0.0 - 1.0 | Intensidade e atividade |
| `loudness` | float | -60.0 - 0.0 | Volume em decibéis |
| `speechiness` | float | 0.0 - 1.0 | Presença de palavras faladas |
| `acousticness` | float | 0.0 - 1.0 | Confiança acústica |
| `instrumentalness` | float | 0.0 - 1.0 | Ausência de vocais |
| `liveness` | float | 0.0 - 1.0 | Presença de audiência |
| `valence` | float | 0.0 - 1.0 | Positividade musical |
| `tempo` | float | 0 - 300 | Tempo em BPM |
| `duration_ms` | float | > 0 | Duração em milissegundos |
| `key` | int | 0 - 11 | Tonalidade (opcional) |
| `mode` | int | 0 - 1 | Modo (0=menor, 1=maior, opcional) |
| `time_signature` | int | 3 - 7 | Assinatura de tempo (opcional) |

### PredictionResponse (Output)

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `popularity` | float | Score de popularidade (0-100) |
| `confidence` | string | Nível de confiança (High/Medium) |
| `category` | string | Categoria (High/Medium/Low Popularity) |

## 🔒 Códigos de Status HTTP

| Código | Significado |
|--------|-------------|
| 200 | Sucesso - Requisição processada com sucesso |
| 422 | Validation Error - Dados de entrada inválidos |
| 500 | Internal Server Error - Erro no servidor |
| 503 | Service Unavailable - Modelo não carregado |

## ⚠️ Tratamento de Erros

### Exemplo de erro de validação:

**Request:**
```json
{
  "danceability": 1.5,  // Valor fora do range
  "energy": 0.5
}
```

**Response (422):**
```json
{
  "detail": [
    {
      "loc": ["body", "danceability"],
      "msg": "ensure this value is less than or equal to 1.0",
      "type": "value_error.number.not_le"
    }
  ]
}
```

## 🧪 Testes da API

### Usando pytest

```bash
# Executar testes da API
pytest tests/test_api.py -v
```

### Teste manual com curl

```bash
# Teste de health check
curl http://localhost:8000/health

# Teste de predição
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d @test_data.json
```

## 🐳 Deploy com Docker

```bash
# Build da imagem
docker build -t spotify-api .

# Run do container
docker run -p 8000:8000 spotify-api

# Ou com docker-compose
docker-compose up api
```

## 📊 Monitoramento

A API pode ser monitorada através de:

1. **Logs**: Arquivo `logs/app.log`
2. **Métricas**: Endpoint `/health`
3. **FastAPI built-in**: Documentação automática em `/docs`

## 🔧 Configuração

Configurações podem ser ajustadas em `config.yaml`:

```yaml
api:
  host: "0.0.0.0"
  port: 8000
  title: "Spotify Popularity Prediction API"
  version: "1.0.0"
```

## 📝 Notas Importantes

- **Rate Limiting**: Não implementado nesta versão
- **Autenticação**: Não requerida nesta versão
- **CORS**: Habilitado por padrão para desenvolvimento
- **Modelo**: Precisa ser treinado antes de usar a API (execute `python main.py`)

## 🔗 Links Úteis

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Validation](https://pydantic-docs.helpmanual.io/)
- [Uvicorn Server](https://www.uvicorn.org/)
