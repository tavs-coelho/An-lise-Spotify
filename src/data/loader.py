"""
Data loading and preprocessing module.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Tuple, Optional
import logging

logger = logging.getLogger(__name__)


class DataLoader:
    """Class for loading and preprocessing Spotify music data."""
    
    def __init__(self, config: dict):
        """
        Initialize the DataLoader.
        
        Args:
            config: Configuration dictionary with data paths
        """
        self.config = config
        self.data_path = config['data']['raw_path']
        
    def load_data(self) -> pd.DataFrame:
        """
        Load raw data from CSV file.
        
        Returns:
            DataFrame with loaded data
            
        Raises:
            FileNotFoundError: If data file doesn't exist
        """
        data_file = Path(self.data_path)
        
        if not data_file.exists():
            logger.warning(f"Data file not found at {self.data_path}")
            logger.info("Generating sample data for demonstration...")
            return self._generate_sample_data()
        
        logger.info(f"Loading data from {self.data_path}")
        df = pd.read_csv(data_file)
        logger.info(f"Loaded {len(df)} records with {len(df.columns)} columns")
        
        return df
    
    def _generate_sample_data(self, n_samples: int = 1000) -> pd.DataFrame:
        """
        Generate sample data for demonstration purposes.
        
        Args:
            n_samples: Number of samples to generate
            
        Returns:
            DataFrame with sample data
        """
        np.random.seed(42)
        
        data = {
            'track_id': [f'track_{i}' for i in range(n_samples)],
            'track_name': [f'Song {i}' for i in range(n_samples)],
            'track_artist': [f'Artist {i % 100}' for i in range(n_samples)],
            'danceability': np.random.uniform(0, 1, n_samples),
            'energy': np.random.uniform(0, 1, n_samples),
            'loudness': np.random.uniform(-60, 0, n_samples),
            'speechiness': np.random.uniform(0, 1, n_samples),
            'acousticness': np.random.uniform(0, 1, n_samples),
            'instrumentalness': np.random.uniform(0, 1, n_samples),
            'liveness': np.random.uniform(0, 1, n_samples),
            'valence': np.random.uniform(0, 1, n_samples),
            'tempo': np.random.uniform(50, 200, n_samples),
            'duration_ms': np.random.uniform(120000, 300000, n_samples),
            'key': np.random.randint(0, 12, n_samples),
            'mode': np.random.randint(0, 2, n_samples),
            'time_signature': np.random.choice([3, 4, 5], n_samples),
            'popularity': np.random.randint(0, 101, n_samples)
        }
        
        logger.info(f"Generated {n_samples} sample records")
        return pd.DataFrame(data)
    
    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean the data by handling missing values and outliers.
        
        Args:
            df: Input DataFrame
            
        Returns:
            Cleaned DataFrame
        """
        logger.info("Cleaning data...")
        
        # Handle missing values
        initial_rows = len(df)
        df = df.dropna()
        removed_rows = initial_rows - len(df)
        
        if removed_rows > 0:
            logger.info(f"Removed {removed_rows} rows with missing values")
        
        # Remove duplicates
        initial_rows = len(df)
        df = df.drop_duplicates()
        removed_duplicates = initial_rows - len(df)
        
        if removed_duplicates > 0:
            logger.info(f"Removed {removed_duplicates} duplicate rows")
        
        logger.info(f"Data cleaned. Final shape: {df.shape}")
        return df
    
    def split_features_target(
        self, 
        df: pd.DataFrame
    ) -> Tuple[pd.DataFrame, pd.Series]:
        """
        Split data into features and target variable.
        
        Args:
            df: Input DataFrame
            
        Returns:
            Tuple of (features DataFrame, target Series)
        """
        target_col = self.config['features']['target']
        feature_cols = (
            self.config['features']['numerical'] + 
            self.config['features']['categorical']
        )
        
        # Filter to only existing columns
        feature_cols = [col for col in feature_cols if col in df.columns]
        
        X = df[feature_cols]
        y = df[target_col]
        
        logger.info(f"Features shape: {X.shape}, Target shape: {y.shape}")
        
        return X, y
