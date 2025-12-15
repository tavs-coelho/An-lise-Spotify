"""Data loading and preprocessing utilities."""

import logging
from pathlib import Path
from typing import Tuple, Optional, Union

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from spotify_analysis.config import config

logger = logging.getLogger(__name__)


class DataLoader:
    """Handle data loading operations."""
    
    def __init__(self, data_path: Optional[Union[str, Path]] = None):
        """Initialize DataLoader.
        
        Args:
            data_path: Path to the data file. If None, uses default path.
        """
        self.data_path = data_path or config.data_dir / "spotify_songs.csv"
        self.df: Optional[pd.DataFrame] = None
    
    def load_data(self) -> pd.DataFrame:
        """Load Spotify dataset from CSV.
        
        Returns:
            DataFrame with Spotify songs data.
            
        Raises:
            FileNotFoundError: If data file doesn't exist.
        """
        if not Path(self.data_path).exists():
            logger.error(f"Data file not found: {self.data_path}")
            raise FileNotFoundError(
                f"Data file not found: {self.data_path}. "
                "Please download the dataset from Kaggle."
            )
        
        logger.info(f"Loading data from {self.data_path}")
        self.df = pd.read_csv(self.data_path)
        logger.info(f"Loaded {len(self.df)} records")
        return self.df
    
    def get_basic_info(self) -> dict:
        """Get basic information about the dataset.
        
        Returns:
            Dictionary with dataset statistics.
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        
        return {
            'n_rows': len(self.df),
            'n_cols': len(self.df.columns),
            'columns': list(self.df.columns),
            'missing_values': self.df.isnull().sum().to_dict(),
            'dtypes': self.df.dtypes.to_dict(),
            'memory_usage': self.df.memory_usage(deep=True).sum() / 1024**2  # MB
        }


class DataPreprocessor:
    """Handle data preprocessing and feature engineering."""
    
    def __init__(self, numerical_features=None, categorical_features=None):
        """Initialize DataPreprocessor.
        
        Args:
            numerical_features: List of numerical feature names.
            categorical_features: List of categorical feature names.
        """
        self.numerical_features = numerical_features or config.numerical_features
        self.categorical_features = categorical_features or config.categorical_features
        self.preprocessor: Optional[ColumnTransformer] = None
        self.feature_names_: Optional[list] = None
    
    def create_preprocessor(self) -> ColumnTransformer:
        """Create preprocessing pipeline.
        
        Returns:
            Sklearn ColumnTransformer for preprocessing.
        """
        numeric_transformer = Pipeline(steps=[
            ('scaler', StandardScaler())
        ])
        
        categorical_transformer = Pipeline(steps=[
            ('onehot', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'))
        ])
        
        self.preprocessor = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, self.numerical_features),
                ('cat', categorical_transformer, self.categorical_features)
            ]
        )
        
        return self.preprocessor
    
    def fit_transform(self, X: pd.DataFrame) -> np.ndarray:
        """Fit preprocessor and transform data.
        
        Args:
            X: Input features DataFrame.
            
        Returns:
            Transformed feature array.
        """
        if self.preprocessor is None:
            self.create_preprocessor()
        
        X_transformed = self.preprocessor.fit_transform(X)
        self._set_feature_names()
        return X_transformed
    
    def transform(self, X: pd.DataFrame) -> np.ndarray:
        """Transform data using fitted preprocessor.
        
        Args:
            X: Input features DataFrame.
            
        Returns:
            Transformed feature array.
        """
        if self.preprocessor is None:
            raise ValueError("Preprocessor not fitted. Call fit_transform() first.")
        
        return self.preprocessor.transform(X)
    
    def _set_feature_names(self):
        """Extract feature names after preprocessing."""
        feature_names = []
        
        # Numerical features
        feature_names.extend(self.numerical_features)
        
        # Categorical features (one-hot encoded)
        if 'cat' in self.preprocessor.named_transformers_:
            cat_transformer = self.preprocessor.named_transformers_['cat']
            onehot = cat_transformer.named_steps['onehot']
            for i, cat_feature in enumerate(self.categorical_features):
                categories = onehot.categories_[i][1:]  # Skip first due to drop='first'
                feature_names.extend([f"{cat_feature}_{cat}" for cat in categories])
        
        self.feature_names_ = feature_names
    
    def get_feature_names(self) -> list:
        """Get feature names after preprocessing.
        
        Returns:
            List of feature names.
        """
        if self.feature_names_ is None:
            raise ValueError("Feature names not available. Fit preprocessor first.")
        return self.feature_names_


def split_data(
    df: pd.DataFrame,
    target_col: str = None,
    test_size: float = 0.2,
    random_state: int = None
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Split data into train and test sets.
    
    Args:
        df: Input DataFrame.
        target_col: Name of target column.
        test_size: Proportion of test set.
        random_state: Random seed for reproducibility.
        
    Returns:
        Tuple of (X_train, X_test, y_train, y_test).
    """
    target_col = target_col or config.target_variable
    random_state = random_state or config.random_state
    
    # Separate features and target
    X = df.drop(columns=[target_col])
    y = df[target_col]
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, shuffle=True
    )
    
    logger.info(f"Train set: {len(X_train)} samples")
    logger.info(f"Test set: {len(X_test)} samples")
    
    return X_train, X_test, y_train, y_test


def clean_data(df: pd.DataFrame, drop_na: bool = True) -> pd.DataFrame:
    """Clean the dataset.
    
    Args:
        df: Input DataFrame.
        drop_na: Whether to drop rows with missing values.
        
    Returns:
        Cleaned DataFrame.
    """
    df_clean = df.copy()
    
    # Log missing values
    missing = df_clean.isnull().sum()
    if missing.any():
        logger.info(f"Missing values:\n{missing[missing > 0]}")
    
    # Drop rows with missing values if requested
    if drop_na:
        before = len(df_clean)
        df_clean = df_clean.dropna()
        after = len(df_clean)
        if before != after:
            logger.info(f"Dropped {before - after} rows with missing values")
    
    # Remove duplicates
    before = len(df_clean)
    df_clean = df_clean.drop_duplicates()
    after = len(df_clean)
    if before != after:
        logger.info(f"Dropped {before - after} duplicate rows")
    
    return df_clean
