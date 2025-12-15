# 🚀 Quick Start Guide

Comece a usar o sistema de Análise de Popularidade no Spotify em minutos!

## ⚡ Setup Rápido (Recomendado)

### Opção 1: Script Automático

```bash
# 1. Clone o repositório
git clone https://github.com/tavs-coelho/An-lise-Spotify.git
cd An-lise-Spotify

# 2. Execute o script de setup
chmod +x setup.sh
./setup.sh

# Isso irá:
# ✓ Criar ambiente virtual
# ✓ Instalar dependências
# ✓ Criar diretórios necessários
# ✓ Executar testes
# ✓ Treinar modelo inicial
```

### Opção 2: Setup Manual

```bash
# 1. Clone o repositório
git clone https://github.com/tavs-coelho/An-lise-Spotify.git
cd An-lise-Spotify

# 2. Crie ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 3. Instale dependências
pip install -r requirements.txt

# 4. Execute análise principal
python main.py
```

### Opção 3: Docker (Mais Fácil!)

```bash
# 1. Clone o repositório
git clone https://github.com/tavs-coelho/An-lise-Spotify.git
cd An-lise-Spotify

# 2. Inicie todos os serviços
docker-compose up

# Pronto! Acesse:
# - API: http://localhost:8000
# - Dashboard: http://localhost:8501
```

## 🎯 Primeiros Passos

### 1. Treinar o Modelo

```bash
# Treinar e comparar modelos
python main.py
```

**Output esperado:**
```
================================================================================
Spotify Music Popularity Analysis - Starting
================================================================================

1. Loading and preparing data...
✓ Generated 1000 sample records
✓ Data cleaned

2. Training machine learning models...
✓ Ridge trained
✓ RandomForest trained
✓ XGBoost trained

3. Model Comparison Results:
Best model: XGBoost
R²: 0.254, MAE: 12.48

4. Saving best model...
✓ Model saved to models/xgboost_model.pkl
```

### 2. Explorar o Dashboard

```bash
# Iniciar dashboard interativo
streamlit run src/dashboard/app.py
```

Acesse: http://localhost:8501

**O que você pode fazer:**
- 📊 Ver estatísticas do dataset
- 🔍 Explorar dados interativamente
- 🎯 Fazer predições em tempo real
- 📈 Analisar features individuais

### 3. Usar a API

```bash
# Terminal 1: Iniciar API
python -m uvicorn src.api.app:app --reload

# Terminal 2: Testar API
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

**Documentação interativa:** http://localhost:8000/docs

### 4. Executar Testes

```bash
# Todos os testes
pytest tests/ -v

# Com cobertura
pytest tests/ --cov=src
```

## 📓 Usar o Notebook

```bash
# 1. Iniciar Jupyter
jupyter notebook

# 2. Abrir analise_completa_final.ipynb

# 3. Execute as células sequencialmente
```

## 🐳 Comandos Docker Úteis

```bash
# Iniciar todos os serviços
docker-compose up

# Iniciar em background
docker-compose up -d

# Ver logs
docker-compose logs -f

# Parar serviços
docker-compose down

# Rebuild após mudanças
docker-compose up --build

# Executar comando específico
docker-compose run app python main.py
```

## 🔧 Comandos Úteis

### Verificar Status

```bash
# Listar arquivos importantes
ls -la

# Ver estrutura do projeto
tree -L 2

# Verificar Python
python --version

# Verificar dependências
pip list
```

### Logs

```bash
# Ver últimos logs
tail -f logs/app.log

# Ver logs de erro
grep ERROR logs/app.log
```

### Limpeza

```bash
# Limpar cache Python
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type f -name "*.pyc" -delete

# Limpar modelos antigos
rm -rf models/*.pkl

# Limpar logs
rm -rf logs/*.log
```

## ❓ Troubleshooting Rápido

### Erro: ModuleNotFoundError

```bash
# Solução: Instalar dependências
pip install -r requirements.txt
```

### Erro: Port already in use

```bash
# Solução: Usar outra porta
uvicorn src.api.app:app --port 8001
streamlit run src/dashboard/app.py --server.port 8502
```

### Erro: Model not found

```bash
# Solução: Treinar modelo
python main.py
```

### Erro: Permission denied (setup.sh)

```bash
# Solução: Dar permissão de execução
chmod +x setup.sh
./setup.sh
```

## 📚 Próximos Passos

1. ✅ **Ler documentação completa**: `docs/USAGE.md`
2. ✅ **Explorar exemplos**: Ver notebook `analise_completa_final.ipynb`
3. ✅ **Entender arquitetura**: `docs/ARCHITECTURE.md`
4. ✅ **Usar API**: `docs/API.md`
5. ✅ **Contribuir**: `CONTRIBUTING.md`

## 🎓 Tutoriais Rápidos

### Tutorial 1: Fazer uma Predição (Python)

```python
from src.utils.config import load_config
from src.models.predictor import PopularityPredictor
import pandas as pd

# Setup
config = load_config('config.yaml')
predictor = PopularityPredictor(config)
predictor.load_model('models/xgboost_model.pkl', 'XGBoost')

# Fazer predição
features = pd.DataFrame([{
    'danceability': 0.8,
    'energy': 0.7,
    'loudness': -8.0,
    'speechiness': 0.05,
    'acousticness': 0.2,
    'instrumentalness': 0.0,
    'liveness': 0.1,
    'valence': 0.8,
    'tempo': 128.0,
    'duration_ms': 180000,
    'key': 5,
    'mode': 1,
    'time_signature': 4
}])

prediction = predictor.predict(features, 'XGBoost')
print(f"Popularidade prevista: {prediction[0]:.1f}")
```

### Tutorial 2: Visualizar Dados

```python
from src.visualization.plots import SpotifyVisualizer
from src.data.loader import DataLoader
from src.utils.config import load_config
import matplotlib.pyplot as plt

# Carregar dados
config = load_config('config.yaml')
loader = DataLoader(config)
df = loader.load_data()

# Criar visualizador
viz = SpotifyVisualizer()

# Plotar distribuições
features = ['danceability', 'energy', 'valence']
fig = viz.plot_feature_distributions(df, features)
plt.savefig('distributions.png', dpi=300)
plt.show()
```

### Tutorial 3: Comparar Modelos

```python
from src.models.predictor import PopularityPredictor
from src.data.loader import DataLoader
from src.utils.config import load_config, setup_logging

# Setup
config = load_config('config.yaml')
setup_logging(config)

# Carregar dados
loader = DataLoader(config)
df = loader.load_data()
df_clean = loader.clean_data(df)
X, y = loader.split_features_target(df_clean)

# Treinar e comparar
predictor = PopularityPredictor(config)
results = predictor.train_models(X, y)

# Mostrar resultados
for name, metrics in results.items():
    print(f"{name}:")
    print(f"  MAE: {metrics['mae']:.2f}")
    print(f"  R²: {metrics['r2']:.3f}")
    print()
```

## 💡 Dicas Finais

1. **Use o dashboard** para exploração rápida
2. **Use a API** para integração com outros sistemas
3. **Use o notebook** para análise detalhada
4. **Leia os logs** quando algo der errado
5. **Consulte a documentação** em `docs/`

## 🆘 Precisa de Ajuda?

- 📖 Leia a documentação completa em `docs/`
- 🐛 Reporte bugs via GitHub Issues
- 💬 Pergunte no repositório
- 📧 Entre em contato: GitHub @tavs-coelho

---

**Pronto para começar! 🎵**
