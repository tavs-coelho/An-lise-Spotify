"""
Model training and prediction module.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
from pathlib import Path
from typing import Dict, Tuple, Optional
import logging

logger = logging.getLogger(__name__)


class PopularityPredictor:
    """Class for training and predicting music popularity."""
    
    def __init__(self, config: dict):
        """
        Initialize the PopularityPredictor.
        
        Args:
            config: Configuration dictionary
        """
        self.config = config
        self.models = {}
        self.preprocessor = None
        self.feature_names = []
        
    def create_preprocessor(self, X: pd.DataFrame) -> ColumnTransformer:
        """
        Create preprocessing pipeline.
        
        Args:
            X: Features DataFrame
            
        Returns:
            ColumnTransformer for preprocessing
        """
        numerical_features = [
            col for col in self.config['features']['numerical'] 
            if col in X.columns
        ]
        
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), numerical_features)
            ],
            remainder='passthrough'
        )
        
        self.feature_names = numerical_features
        logger.info(f"Created preprocessor with {len(numerical_features)} features")
        
        return preprocessor
    
    def train_models(
        self, 
        X: pd.DataFrame, 
        y: pd.Series
    ) -> Dict[str, Dict]:
        """
        Train multiple models and compare performance.
        
        Args:
            X: Features DataFrame
            y: Target Series
            
        Returns:
            Dictionary with model results
        """
        logger.info("Starting model training...")
        
        # Split data
        test_size = self.config['model']['test_size']
        random_state = self.config['model']['random_state']
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )
        
        logger.info(f"Train size: {len(X_train)}, Test size: {len(X_test)}")
        
        # Create preprocessor
        self.preprocessor = self.create_preprocessor(X)
        
        # Define models
        models_config = {
            'Ridge': Ridge(**self.config.get('ridge', {'random_state': 42})),
            'RandomForest': RandomForestRegressor(
                **self.config.get('random_forest', {'random_state': 42})
            ),
            'XGBoost': XGBRegressor(**self.config.get('xgboost', {'random_state': 42}))
        }
        
        results = {}
        
        for name, model in models_config.items():
            logger.info(f"Training {name}...")
            
            # Create pipeline
            pipeline = Pipeline([
                ('preprocessor', self.preprocessor),
                ('model', model)
            ])
            
            # Train
            pipeline.fit(X_train, y_train)
            
            # Predict
            y_pred = pipeline.predict(X_test)
            
            # Evaluate
            mae = mean_absolute_error(y_test, y_pred)
            rmse = np.sqrt(mean_squared_error(y_test, y_pred))
            r2 = r2_score(y_test, y_pred)
            
            # Cross-validation
            cv_scores = cross_val_score(
                pipeline, X_train, y_train, 
                cv=self.config['model']['cv_folds'],
                scoring='r2'
            )
            
            results[name] = {
                'model': pipeline,
                'mae': mae,
                'rmse': rmse,
                'r2': r2,
                'cv_mean': cv_scores.mean(),
                'cv_std': cv_scores.std()
            }
            
            self.models[name] = pipeline
            
            logger.info(
                f"{name} - MAE: {mae:.2f}, RMSE: {rmse:.2f}, "
                f"R²: {r2:.3f}, CV R²: {cv_scores.mean():.3f} (±{cv_scores.std():.3f})"
            )
        
        # Find best model
        best_model_name = max(results, key=lambda x: results[x]['r2'])
        logger.info(f"Best model: {best_model_name}")
        
        return results
    
    def predict(self, X: pd.DataFrame, model_name: str = 'XGBoost') -> np.ndarray:
        """
        Make predictions using trained model.
        
        Args:
            X: Features DataFrame
            model_name: Name of model to use
            
        Returns:
            Array of predictions
        """
        if model_name not in self.models:
            raise ValueError(f"Model {model_name} not found. Train models first.")
        
        return self.models[model_name].predict(X)
    
    def save_model(self, model_name: str = 'XGBoost', path: str = 'models/best_model.pkl'):
        """
        Save trained model to disk.
        
        Args:
            model_name: Name of model to save
            path: Path to save the model
        """
        if model_name not in self.models:
            raise ValueError(f"Model {model_name} not found")
        
        save_path = Path(path)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        
        joblib.dump(self.models[model_name], save_path)
        logger.info(f"Model saved to {path}")
    
    def load_model(self, path: str = 'models/best_model.pkl', model_name: str = 'XGBoost'):
        """
        Load trained model from disk.
        
        Args:
            path: Path to load the model from
            model_name: Name to assign to loaded model
        """
        load_path = Path(path)
        
        if not load_path.exists():
            raise FileNotFoundError(f"Model file not found: {path}")
        
        self.models[model_name] = joblib.load(load_path)
        logger.info(f"Model loaded from {path}")
