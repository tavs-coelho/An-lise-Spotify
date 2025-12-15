"""Configuration settings for the Spotify Analysis project."""

import os
from pathlib import Path
from typing import List, Dict, Any

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data"
MODELS_DIR = PROJECT_ROOT / "models"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
LOGS_DIR = PROJECT_ROOT / "logs"

# Create directories if they don't exist
for directory in [DATA_DIR, MODELS_DIR, LOGS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# Random seed for reproducibility
RANDOM_STATE = 42

# Feature configurations
NUMERICAL_FEATURES: List[str] = [
    'danceability',
    'energy',
    'loudness',
    'speechiness',
    'acousticness',
    'instrumentalness',
    'liveness',
    'valence',
    'tempo',
    'duration_ms'
]

CATEGORICAL_FEATURES: List[str] = [
    'key',
    'mode',
    'time_signature'
]

TARGET_VARIABLE = 'track_popularity'

# Model configurations
MODEL_CONFIGS: Dict[str, Dict[str, Any]] = {
    'ridge': {
        'alpha': 1.0,
        'random_state': RANDOM_STATE
    },
    'lasso': {
        'alpha': 1.0,
        'random_state': RANDOM_STATE
    },
    'elasticnet': {
        'alpha': 1.0,
        'l1_ratio': 0.5,
        'random_state': RANDOM_STATE
    },
    'random_forest': {
        'n_estimators': 100,
        'max_depth': 10,
        'random_state': RANDOM_STATE,
        'n_jobs': -1
    },
    'gradient_boosting': {
        'n_estimators': 100,
        'learning_rate': 0.1,
        'max_depth': 5,
        'random_state': RANDOM_STATE
    },
    'xgboost': {
        'n_estimators': 100,
        'learning_rate': 0.1,
        'max_depth': 5,
        'random_state': RANDOM_STATE,
        'n_jobs': -1
    }
}

# Train-test split configuration
TRAIN_TEST_SPLIT_CONFIG = {
    'test_size': 0.2,
    'random_state': RANDOM_STATE,
    'shuffle': True
}

# Cross-validation configuration
CV_CONFIG = {
    'n_splits': 5,
    'shuffle': True,
    'random_state': RANDOM_STATE
}

# Clustering configuration
CLUSTERING_CONFIG = {
    'n_clusters': 4,
    'random_state': RANDOM_STATE,
    'n_init': 10,
    'max_iter': 300
}

# Visualization configuration
PLOT_CONFIG = {
    'style': 'whitegrid',
    'context': 'notebook',
    'palette': 'husl',
    'figure_size': (12, 8),
    'dpi': 100,
    'font_scale': 1.2
}

# API configuration
API_CONFIG = {
    'host': '0.0.0.0',
    'port': 8000,
    'reload': True
}

# Streamlit configuration
STREAMLIT_CONFIG = {
    'page_title': 'Spotify Analysis Dashboard',
    'page_icon': '🎵',
    'layout': 'wide'
}


class Config:
    """Central configuration class."""
    
    def __init__(self):
        self.project_root = PROJECT_ROOT
        self.data_dir = DATA_DIR
        self.models_dir = MODELS_DIR
        self.notebooks_dir = NOTEBOOKS_DIR
        self.logs_dir = LOGS_DIR
        self.random_state = RANDOM_STATE
        self.numerical_features = NUMERICAL_FEATURES
        self.categorical_features = CATEGORICAL_FEATURES
        self.target_variable = TARGET_VARIABLE
        self.model_configs = MODEL_CONFIGS
        self.train_test_split_config = TRAIN_TEST_SPLIT_CONFIG
        self.cv_config = CV_CONFIG
        self.clustering_config = CLUSTERING_CONFIG
        self.plot_config = PLOT_CONFIG
        self.api_config = API_CONFIG
        self.streamlit_config = STREAMLIT_CONFIG
    
    def get_model_config(self, model_name: str) -> Dict[str, Any]:
        """Get configuration for a specific model."""
        return self.model_configs.get(model_name, {})


# Global config instance
config = Config()
