<div align="center">

# 🎵 Spotify Music Popularity Analysis

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?logo=github-actions)](https://github.com/features/actions)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)](https://www.docker.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![FastAPI](https://img.shields.io/badge/FastAPI-REST%20API-009688?logo=fastapi)](https://fastapi.tiangolo.com/)

**Advanced Machine Learning Analysis of Music Popularity on Spotify**

[📊 Demo Dashboard](https://github.com/tavs-coelho/An-lise-Spotify) • [📖 Documentation](docs/) • [🔬 Research Paper](relatorio_tecnico.md) • [🚀 Quick Start](#-quick-start)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Methodology](#-methodology)
- [Results](#-results)
- [Technologies](#-technologies)
- [API Documentation](#-api-documentation)
- [Contributing](#-contributing)
- [License](#-license)
- [Citation](#-citation)
- [Contact](#-contact)

---

## 🎯 Overview

This project implements a **complete end-to-end machine learning pipeline** for predicting music popularity on Spotify using the **CRISP-DM methodology**. It combines supervised learning (Regression & Classification), unsupervised learning (Clustering), and recommendation systems to provide comprehensive insights into what makes music popular.

### 🎓 Academic Context

- **Course:** Data Science & Machine Learning
- **Author:** Geyson de Araujo
- **Date:** December 2025
- **Institution:** Academic Research Project

### 🎤 Business Problem

*How can we predict music popularity based on intrinsic audio features to help artists, record labels, and streaming platforms make data-driven decisions?*

---

## ✨ Features

### 🔬 Machine Learning Models
- **6 Regression Models:** Ridge, Lasso, ElasticNet, Random Forest, Gradient Boosting, XGBoost
- **Classification:** Multi-class popularity categorization
- **Clustering:** K-Means for music profile discovery
- **Recommendation System:** Content-based filtering using cosine similarity

### 📊 Interactive Dashboards
- **Streamlit Dashboard:** Real-time visualization and prediction interface
- **Plotly Visualizations:** Interactive charts and graphs
- **Model Comparison:** Side-by-side performance metrics

### 🚀 Production-Ready Features
- **REST API:** FastAPI-based microservice for predictions
- **Docker Support:** Containerized deployment with Docker Compose
- **CI/CD Pipeline:** Automated testing and quality checks
- **Comprehensive Testing:** Unit and integration tests with pytest
- **Type Safety:** Full type hints with mypy validation
- **Code Quality:** Black, isort, flake8, and bandit integration

### 📈 Advanced Analytics
- **Feature Importance:** SHAP and tree-based importance analysis
- **Cross-Validation:** Robust model evaluation
- **Hyperparameter Tuning:** Optimized model configurations
- **Model Interpretability:** Clear explanations of predictions

---

## 🏗️ Architecture

```
┌─────────────────┐         ┌──────────────────┐
│  Data Sources   │────────▶│  Data Pipeline   │
│  (Spotify API)  │         │  (Preprocessing) │
└─────────────────┘         └──────────────────┘
                                     │
                                     ▼
                            ┌──────────────────┐
                            │  ML Models       │
                            │  (6 Regressors)  │
                            └──────────────────┘
                                     │
                    ┌────────────────┼────────────────┐
                    ▼                ▼                ▼
            ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
            │  REST API    │  │  Dashboard   │  │  Jupyter     │
            │  (FastAPI)   │  │  (Streamlit) │  │  Notebooks   │
            └──────────────┘  └──────────────┘  └──────────────┘
```

---

## 🚀 Quick Start

### Using Docker (Recommended)

```bash
# Clone the repository
git clone https://github.com/tavs-coelho/An-lise-Spotify.git
cd An-lise-Spotify

# Start all services with Docker Compose
docker-compose up -d

# Access the services
# - API Documentation: http://localhost:8000/docs
# - Streamlit Dashboard: http://localhost:8501
```

### Local Development

```bash
# 1. Clone and navigate
git clone https://github.com/tavs-coelho/An-lise-Spotify.git
cd An-lise-Spotify

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
pip install -e .

# 4. Run the application
# Option A: Streamlit Dashboard
streamlit run app.py

# Option B: FastAPI Server
uvicorn api:app --reload

# Option C: Jupyter Notebook
jupyter notebook analise_completa_final.ipynb
```

---

## 📦 Installation

### Prerequisites

- **Python 3.8+** (3.10 recommended)
- **pip** (latest version)
- **Git**
- **Docker & Docker Compose** (optional, for containerized deployment)

### Step-by-Step Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/tavs-coelho/An-lise-Spotify.git
cd An-lise-Spotify
```

#### 2. Create Virtual Environment

```bash
# Using venv
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Or using conda
conda create -n spotify-analysis python=3.10
conda activate spotify-analysis
```

#### 3. Install Dependencies

```bash
# Install core dependencies
pip install -r requirements.txt

# Install package in development mode
pip install -e .

# Optional: Install development dependencies
pip install -r requirements-dev.txt  # If exists
```

#### 4. Download Dataset (Optional)

The project works with sample data, but for full analysis:

```bash
# Download from Kaggle (requires Kaggle API)
kaggle datasets download -d zaheenhamidani/ultimate-spotify-tracks-db
unzip ultimate-spotify-tracks-db.zip -d data/
```

---

## 💻 Usage

### 1. Interactive Dashboard

Launch the Streamlit dashboard for interactive exploration:

```bash
streamlit run app.py
```

Features:
- 📊 Explore data statistics and distributions
- 🤖 Compare model performances
- 📈 Visualize feature importance
- 🎯 Make real-time predictions

### 2. REST API

Start the FastAPI server:

```bash
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

Access API documentation:
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

Example API request:

```python
import requests

url = "http://localhost:8000/predict"
payload = {
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

response = requests.post(url, json=payload)
print(response.json())
```

### 3. Python Package

Use as a Python library:

```python
from spotify_analysis.data import DataLoader, DataPreprocessor
from spotify_analysis.models import ModelTrainer
from spotify_analysis.visualization import plot_feature_importance

# Load and preprocess data
loader = DataLoader()
df = loader.load_data()

preprocessor = DataPreprocessor()
X_processed = preprocessor.fit_transform(df)

# Train model
trainer = ModelTrainer('xgboost')
trainer.fit(X_train, y_train)

# Evaluate and visualize
metrics = trainer.evaluate(X_test, y_test)
importance_df = trainer.get_feature_importance()
plot_feature_importance(importance_df)
```

### 4. Jupyter Notebooks

Explore the complete analysis:

```bash
jupyter notebook analise_completa_final.ipynb
```

---

## 📁 Project Structure

```
An-lise-Spotify/
├── 📂 src/spotify_analysis/          # Main package
│   ├── 📂 data/                      # Data loading & preprocessing
│   │   └── __init__.py
│   ├── 📂 models/                    # ML models
│   │   └── __init__.py
│   ├── 📂 visualization/             # Plotting utilities
│   │   └── __init__.py
│   ├── 📂 utils/                     # Helper functions
│   │   └── __init__.py
│   ├── __init__.py
│   └── config.py                     # Configuration
│
├── 📂 tests/                         # Unit & integration tests
│   ├── test_data.py
│   ├── test_models.py
│   └── conftest.py
│
├── 📂 notebooks/                     # Jupyter notebooks
│   ├── analise_completa_final.ipynb
│   └── 📂 figures/                   # Generated plots
│
├── 📂 docs/                          # Documentation
│   ├── 1_entendimento_negocio.md
│   └── relatorio_tecnico.md
│
├── 📂 .github/                       # GitHub Actions
│   └── workflows/
│       └── ci.yml
│
├── 📂 data/                          # Data directory (gitignored)
│   └── .gitkeep
│
├── 📂 models/                        # Saved models (gitignored)
│   └── .gitkeep
│
├── 📄 app.py                         # Streamlit dashboard
├── 📄 api.py                         # FastAPI application
├── 📄 setup.py                       # Package setup
├── 📄 pyproject.toml                 # Modern Python config
├── 📄 requirements.txt               # Dependencies
├── 📄 Dockerfile                     # Docker configuration
├── 📄 docker-compose.yml             # Multi-container setup
├── 📄 .gitignore                     # Git ignore rules
├── 📄 LICENSE                        # MIT License
└── 📄 README.md                      # This file
```

---

## 🔬 Methodology (CRISP-DM)


### 1. **Business Understanding** 🎯
- **Problem:** Predict music popularity using audio features
- **Goal:** R² > 0.20, MAE < 15
- **Stakeholders:** Artists, record labels, streaming platforms

### 2. **Data Understanding** 📊
- **Dataset:** 113,999 Spotify tracks
- **Features:** 23 variables (9 core audio features)
- **Target:** Popularity score (0-100)
- **Source:** Spotify Web API

### 3. **Data Preparation** 🔧
- Missing value handling (< 1% of data)
- Feature scaling with StandardScaler
- One-hot encoding for categorical variables
- 80/20 train-test split with stratification

### 4. **Modeling** 🤖

#### Regression Models (Popularity Prediction)
| Model | R² | MAE | RMSE | Training Time |
|-------|-----|-----|------|---------------|
| **XGBoost** ⭐ | **0.254** | **12.48** | **16.92** | ~15s |
| Gradient Boosting | 0.241 | 12.73 | 17.15 | ~45s |
| Random Forest | 0.228 | 13.02 | 17.48 | ~30s |
| ElasticNet | 0.185 | 14.21 | 18.92 | ~2s |
| Ridge | 0.182 | 14.35 | 19.01 | ~1s |
| Lasso | 0.179 | 14.48 | 19.12 | ~1s |

#### Additional Techniques
- **Classification:** Multi-class categorization (Low/Medium/High)
- **Clustering:** K-Means with 4 distinct music profiles
- **Recommendation:** Cosine similarity-based system

### 5. **Evaluation** 📈
- **Metrics:** MAE, RMSE, R², Accuracy, F1-Score, Silhouette
- **Cross-Validation:** 5-fold CV for robust estimates
- **Feature Importance:** SHAP and tree-based analysis

### 6. **Deployment** 🚀
- **REST API:** FastAPI microservice
- **Dashboard:** Interactive Streamlit application
- **Docker:** Containerized for easy deployment
- **CI/CD:** Automated testing and quality checks

---

## 📊 Results

### 🏆 Best Model: XGBoost

- **R² Score:** 0.254 (explains 25% of variance)
- **MAE:** 12.48 points (acceptable error on 0-100 scale)
- **Interpretation:** Audio features explain ~25% of popularity; external factors (marketing, artist fame, virality) account for the rest

### 🎯 Top 5 Most Important Features

1. **Loudness** (28.5%) - Volume is the strongest predictor
2. **Energy** (19.8%) - High-energy tracks tend to be more popular
3. **Danceability** (15.6%) - Danceable music performs better
4. **Valence** (12.4%) - Positive-sounding tracks are favored
5. **Acousticness** (8.9%) - Less acoustic = more popular

### 💡 Key Insights

✅ **Audio features have moderate predictive power** - R² of 0.25 indicates intrinsic musical characteristics explain a significant but not complete portion of popularity

✅ **Intensity matters** - Loud, energetic tracks dominate popularity charts

✅ **Tree-based models outperform linear models** - Non-linear relationships are important

✅ **Four distinct music profiles exist** - Natural clustering reveals different musical archetypes

⚠️ **External factors are critical** - Marketing, artist reputation, and timing play major roles not captured by audio features alone

---

## 🛠️ Technologies

### Core Stack
```
┌─────────────────────────────────────────────────────────┐
│  Language        │  Python 3.8+                         │
│  ML Framework    │  scikit-learn 1.3+, XGBoost 2.0+    │
│  Data Processing │  Pandas 2.1+, NumPy 1.26+           │
│  Visualization   │  Matplotlib, Seaborn, Plotly        │
└─────────────────────────────────────────────────────────┘
```

### Web & API
- **FastAPI** - Modern REST API framework
- **Streamlit** - Interactive dashboards
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation

### ML & Analytics
- **scikit-learn** - ML algorithms & pipelines
- **XGBoost** - Gradient boosting
- **SHAP** - Model interpretability
- **MLflow** - Experiment tracking (optional)

### Development & Deployment
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration
- **GitHub Actions** - CI/CD pipeline
- **pytest** - Testing framework
- **Black** - Code formatting
- **mypy** - Type checking
- **flake8** - Linting
- **bandit** - Security analysis

---

## 📚 API Documentation

### REST API Endpoints

Base URL: `http://localhost:8000`

#### 🏥 Health Check
```http
GET /health
```

Response:
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "model_loaded": true
}
```

#### 🎯 Single Prediction
```http
POST /predict
Content-Type: application/json
```

Request Body:
```json
{
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
```

Response:
```json
{
  "predicted_popularity": 65.32,
  "category": "Medium",
  "confidence": 0.78,
  "top_features": {
    "loudness": 1.59,
    "energy": 0.11,
    "danceability": 0.11
  }
}
```

#### 📊 Batch Prediction
```http
POST /predict/batch
Content-Type: application/json
```

Request: Array of track features (max 100)

#### ℹ️ Model Info
```http
GET /model/info
```

#### 📖 Feature Descriptions
```http
GET /features
```

---

## 🧪 Testing

### Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/spotify_analysis --cov-report=html

# Run specific test file
pytest tests/test_models.py

# Run with verbose output
pytest -v

# Run and show print statements
pytest -s
```

### Code Quality Checks

```bash
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Lint code
flake8 src/ tests/

# Type check
mypy src/

# Security scan
bandit -r src/
```

---

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guide
- Add type hints to all functions
- Write unit tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

### Code Style

This project uses:
- **Black** for code formatting (line length: 100)
- **isort** for import sorting
- **flake8** for linting
- **mypy** for type checking

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Geyson de Araujo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 📖 Citation

If you use this project in your research or work, please cite:

```bibtex
@software{araujo2025spotify,
  author = {Araujo, Geyson de},
  title = {Spotify Music Popularity Analysis: A Machine Learning Approach},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/tavs-coelho/An-lise-Spotify}
}
```

---

## 📧 Contact

**Geyson de Araujo**

- GitHub: [@tavs-coelho](https://github.com/tavs-coelho)
- Repository: [An-lise-Spotify](https://github.com/tavs-coelho/An-lise-Spotify)
- Project Link: [https://github.com/tavs-coelho/An-lise-Spotify](https://github.com/tavs-coelho/An-lise-Spotify)

---

## 🙏 Acknowledgments

- **Spotify** for providing the Web API
- **Kaggle** community for dataset compilation
- **scikit-learn** and **XGBoost** teams for excellent ML libraries
- Academic advisors and peer reviewers

---

## 📚 Additional Resources

- [Technical Report (Portuguese)](relatorio_tecnico.md) - Detailed analysis and methodology
- [Business Understanding](docs/1_entendimento_negocio.md) - Problem definition and objectives
- [Jupyter Notebook](notebooks/analise_completa_final.ipynb) - Complete analysis walkthrough
- [API Documentation](http://localhost:8000/docs) - Interactive API docs (when server is running)

---

## 🌟 Future Enhancements

- [ ] Add temporal analysis (popularity trends over time)
- [ ] Include artist metadata and social media metrics
- [ ] Implement NLP analysis on song lyrics
- [ ] Add deep learning models (Neural Networks)
- [ ] Create mobile application
- [ ] Integrate with Spotify API for real-time data
- [ ] Add A/B testing framework
- [ ] Implement MLOps pipeline with MLflow

---

<div align="center">

**⭐ If you find this project useful, please consider giving it a star!**

Made with ❤️ and 🎵 by [Geyson de Araujo](https://github.com/tavs-coelho)

[⬆ Back to Top](#-spotify-music-popularity-analysis)

</div>
