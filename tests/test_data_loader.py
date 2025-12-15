"""
Tests for data loader module.
"""

import pytest
import pandas as pd
from pathlib import Path

from src.data.loader import DataLoader
from src.utils.config import load_config


@pytest.fixture
def config():
    """Load configuration for testing."""
    return load_config('config.yaml')


@pytest.fixture
def data_loader(config):
    """Create DataLoader instance."""
    return DataLoader(config)


def test_generate_sample_data(data_loader):
    """Test sample data generation."""
    df = data_loader._generate_sample_data(n_samples=100)
    
    assert len(df) == 100
    assert 'popularity' in df.columns
    assert 'danceability' in df.columns
    assert df['popularity'].min() >= 0
    assert df['popularity'].max() <= 100


def test_clean_data(data_loader):
    """Test data cleaning."""
    # Create test data with missing values
    df = pd.DataFrame({
        'popularity': [50, None, 70, 80],
        'danceability': [0.5, 0.6, None, 0.8],
        'energy': [0.7, 0.8, 0.9, 0.8]
    })
    
    df_clean = data_loader.clean_data(df)
    
    assert len(df_clean) < len(df)  # Some rows should be removed
    assert df_clean.isnull().sum().sum() == 0  # No missing values


def test_split_features_target(data_loader):
    """Test splitting features and target."""
    df = data_loader._generate_sample_data(n_samples=100)
    X, y = data_loader.split_features_target(df)
    
    assert len(X) == len(y) == 100
    assert 'popularity' not in X.columns
    assert y.name == 'popularity'


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
