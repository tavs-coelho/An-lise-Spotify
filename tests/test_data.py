"""Tests for data loading and preprocessing."""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path

from spotify_analysis.data import DataLoader, DataPreprocessor, split_data, clean_data
from spotify_analysis.config import config


@pytest.fixture
def sample_data():
    """Create sample data for testing."""
    np.random.seed(42)
    n_samples = 100
    
    data = {
        'danceability': np.random.uniform(0, 1, n_samples),
        'energy': np.random.uniform(0, 1, n_samples),
        'loudness': np.random.uniform(-60, 0, n_samples),
        'speechiness': np.random.uniform(0, 1, n_samples),
        'acousticness': np.random.uniform(0, 1, n_samples),
        'instrumentalness': np.random.uniform(0, 1, n_samples),
        'liveness': np.random.uniform(0, 1, n_samples),
        'valence': np.random.uniform(0, 1, n_samples),
        'tempo': np.random.uniform(60, 200, n_samples),
        'duration_ms': np.random.uniform(180000, 300000, n_samples),
        'key': np.random.randint(0, 12, n_samples),
        'mode': np.random.randint(0, 2, n_samples),
        'time_signature': np.random.randint(3, 6, n_samples),
        'track_popularity': np.random.randint(0, 100, n_samples)
    }
    
    return pd.DataFrame(data)


class TestDataPreprocessor:
    """Tests for DataPreprocessor class."""
    
    def test_create_preprocessor(self):
        """Test preprocessor creation."""
        preprocessor = DataPreprocessor()
        pipeline = preprocessor.create_preprocessor()
        
        assert pipeline is not None
        assert 'num' in pipeline.named_transformers_
        assert 'cat' in pipeline.named_transformers_
    
    def test_fit_transform(self, sample_data):
        """Test fitting and transforming data."""
        preprocessor = DataPreprocessor()
        
        X = sample_data.drop(columns=['track_popularity'])
        X_transformed = preprocessor.fit_transform(X)
        
        assert X_transformed is not None
        assert X_transformed.shape[0] == len(sample_data)
        assert X_transformed.shape[1] > 0
    
    def test_feature_names(self, sample_data):
        """Test feature name extraction."""
        preprocessor = DataPreprocessor()
        
        X = sample_data.drop(columns=['track_popularity'])
        preprocessor.fit_transform(X)
        
        feature_names = preprocessor.get_feature_names()
        
        assert feature_names is not None
        assert len(feature_names) > 0
        assert all(isinstance(name, str) for name in feature_names)


class TestSplitData:
    """Tests for data splitting function."""
    
    def test_split_data(self, sample_data):
        """Test train-test split."""
        X_train, X_test, y_train, y_test = split_data(sample_data, test_size=0.2)
        
        total_samples = len(sample_data)
        
        assert len(X_train) + len(X_test) == total_samples
        assert len(y_train) == len(X_train)
        assert len(y_test) == len(X_test)
        assert isinstance(X_train, pd.DataFrame)
        assert isinstance(y_train, pd.Series)
    
    def test_split_data_ratio(self, sample_data):
        """Test split ratio."""
        test_size = 0.3
        X_train, X_test, y_train, y_test = split_data(sample_data, test_size=test_size)
        
        total = len(X_train) + len(X_test)
        actual_test_ratio = len(X_test) / total
        
        assert abs(actual_test_ratio - test_size) < 0.05  # Allow 5% tolerance


class TestCleanData:
    """Tests for data cleaning function."""
    
    def test_clean_data_no_missing(self, sample_data):
        """Test cleaning data without missing values."""
        cleaned = clean_data(sample_data)
        
        assert len(cleaned) == len(sample_data)
        assert cleaned.isnull().sum().sum() == 0
    
    def test_clean_data_with_missing(self, sample_data):
        """Test cleaning data with missing values."""
        # Introduce missing values
        data_with_missing = sample_data.copy()
        data_with_missing.loc[0:5, 'danceability'] = np.nan
        
        cleaned = clean_data(data_with_missing, drop_na=True)
        
        assert len(cleaned) < len(data_with_missing)
        assert cleaned.isnull().sum().sum() == 0
    
    def test_clean_data_duplicates(self, sample_data):
        """Test removing duplicates."""
        # Create duplicates
        data_with_dupes = pd.concat([sample_data, sample_data.head(5)], ignore_index=True)
        
        cleaned = clean_data(data_with_dupes)
        
        assert len(cleaned) <= len(data_with_dupes)
