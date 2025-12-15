# Quick Start Guide

This guide will help you get started with the Spotify Music Popularity Analysis project in 5 minutes.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## Option 1: Quick Demo with Docker (Fastest) 🐳

```bash
# 1. Clone the repository
git clone https://github.com/tavs-coelho/An-lise-Spotify.git
cd An-lise-Spotify

# 2. Start with Docker Compose
docker-compose up -d

# 3. Access the services
# - API: http://localhost:8000/docs
# - Dashboard: http://localhost:8501
```

That's it! 🎉

## Option 2: Local Installation (Recommended for Development) 💻

### Step 1: Clone and Setup

```bash
# Clone the repository
git clone https://github.com/tavs-coelho/An-lise-Spotify.git
cd An-lise-Spotify

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -e .
```

### Step 2: Choose Your Interface

#### A. Interactive Dashboard (Easiest)

```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501`

#### B. REST API

```bash
uvicorn api:app --reload
```

API docs available at `http://localhost:8000/docs`

#### C. Jupyter Notebook

```bash
jupyter notebook notebooks/analise_completa_final.ipynb
```

#### D. Python Code

```python
from spotify_analysis.models import ModelTrainer
from spotify_analysis.data import DataLoader, DataPreprocessor
import numpy as np

# Create sample data
X_train = np.random.randn(100, 10)
y_train = np.random.randint(0, 100, 100)

# Train model
trainer = ModelTrainer('xgboost')
trainer.fit(X_train, y_train)

# Make predictions
X_test = np.random.randn(20, 10)
predictions = trainer.predict(X_test)
print(predictions)
```

## Option 3: Try the API 🚀

### Using cURL

```bash
# Health check
curl http://localhost:8000/health

# Make a prediction
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

### Using Python requests

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

## Next Steps 📚

1. **Explore the Dashboard:** Try different feature combinations to see how they affect popularity
2. **Read the Documentation:** Check out the [README](README.md) and [Technical Report](docs/relatorio_tecnico.md)
3. **Run Tests:** `pytest tests/`
4. **Contribute:** See [CONTRIBUTING.md](CONTRIBUTING.md)

## Common Commands 🛠️

```bash
# Run tests
pytest

# Format code
black src/ tests/

# Lint code
flake8 src/ tests/

# Type check
mypy src/

# Run all quality checks
make quality

# Start API
make run-api

# Start dashboard
make run-dashboard
```

## Troubleshooting 🔧

### Import Errors

```bash
# Make sure you're in the virtual environment
source venv/bin/activate

# Reinstall the package
pip install -e .
```

### Port Already in Use

```bash
# For API (change port)
uvicorn api:app --port 8001

# For Streamlit (change port)
streamlit run app.py --server.port 8502
```

### Docker Issues

```bash
# Rebuild containers
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

## Need Help? 💬

- 📖 Check the [full documentation](README.md)
- 🐛 [Report issues](https://github.com/tavs-coelho/An-lise-Spotify/issues)
- 💡 [Start a discussion](https://github.com/tavs-coelho/An-lise-Spotify/discussions)

Happy analyzing! 🎵✨
