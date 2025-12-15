"""
Tests for predictor module.
"""

import pytest
import pandas as pd
import numpy as np
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from src.models.predictor import PopularityPredictor
from src.data.loader import DataLoader
from src.utils.config import load_config


@pytest.fixture
def config():
    """Load configuration for testing."""
    return load_config('config.yaml')


@pytest.fixture
def sample_data(config):
    """Generate sample data for testing."""
    data_loader = DataLoader(config)
    df = data_loader._generate_sample_data(n_samples=200)
    return data_loader.split_features_target(df)


@pytest.fixture
def predictor(config):
    """Create PopularityPredictor instance."""
    return PopularityPredictor(config)


def test_create_preprocessor(predictor, sample_data):
    """Test preprocessor creation."""
    X, _ = sample_data
    preprocessor = predictor.create_preprocessor(X)
    
    assert preprocessor is not None
    assert len(predictor.feature_names) > 0


def test_train_models(predictor, sample_data):
    """Test model training."""
    X, y = sample_data
    results = predictor.train_models(X, y)
    
    assert len(results) > 0
    assert 'XGBoost' in results
    assert 'mae' in results['XGBoost']
    assert 'r2' in results['XGBoost']


def test_predict(predictor, sample_data):
    """Test prediction."""
    X, y = sample_data
    predictor.train_models(X, y)
    
    predictions = predictor.predict(X.iloc[:5], 'XGBoost')
    
    assert len(predictions) == 5
    assert all(0 <= p <= 100 for p in predictions)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
