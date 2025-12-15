"""Machine learning models for Spotify popularity prediction."""

import logging
from typing import Dict, Any, Optional, Tuple, List
import joblib
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import cross_val_score
from xgboost import XGBRegressor

from spotify_analysis.config import config

logger = logging.getLogger(__name__)


class ModelTrainer:
    """Train and evaluate regression models."""
    
    def __init__(self, model_name: str = 'xgboost'):
        """Initialize ModelTrainer.
        
        Args:
            model_name: Name of the model to use.
        """
        self.model_name = model_name
        self.model = self._create_model(model_name)
        self.is_fitted = False
        self.metrics: Dict[str, float] = {}
    
    def _create_model(self, model_name: str):
        """Create a model instance.
        
        Args:
            model_name: Name of the model.
            
        Returns:
            Sklearn/XGBoost model instance.
        """
        model_config = config.get_model_config(model_name)
        
        models = {
            'ridge': Ridge,
            'lasso': Lasso,
            'elasticnet': ElasticNet,
            'random_forest': RandomForestRegressor,
            'gradient_boosting': GradientBoostingRegressor,
            'xgboost': XGBRegressor
        }
        
        if model_name not in models:
            raise ValueError(f"Unknown model: {model_name}. Choose from {list(models.keys())}")
        
        return models[model_name](**model_config)
    
    def fit(self, X: np.ndarray, y: np.ndarray) -> 'ModelTrainer':
        """Fit the model.
        
        Args:
            X: Training features.
            y: Training target.
            
        Returns:
            Self for method chaining.
        """
        logger.info(f"Training {self.model_name} model...")
        self.model.fit(X, y)
        self.is_fitted = True
        logger.info(f"{self.model_name} model trained successfully")
        return self
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """Make predictions.
        
        Args:
            X: Features to predict on.
            
        Returns:
            Predictions array.
        """
        if not self.is_fitted:
            raise ValueError("Model not fitted. Call fit() first.")
        
        return self.model.predict(X)
    
    def evaluate(
        self, 
        X: np.ndarray, 
        y: np.ndarray, 
        dataset_name: str = 'test'
    ) -> Dict[str, float]:
        """Evaluate model performance.
        
        Args:
            X: Features.
            y: True target values.
            dataset_name: Name of the dataset (for logging).
            
        Returns:
            Dictionary of metrics.
        """
        y_pred = self.predict(X)
        
        metrics = {
            f'{dataset_name}_mae': mean_absolute_error(y, y_pred),
            f'{dataset_name}_mse': mean_squared_error(y, y_pred),
            f'{dataset_name}_rmse': np.sqrt(mean_squared_error(y, y_pred)),
            f'{dataset_name}_r2': r2_score(y, y_pred)
        }
        
        self.metrics.update(metrics)
        
        logger.info(f"{self.model_name} - {dataset_name} metrics:")
        for metric_name, value in metrics.items():
            logger.info(f"  {metric_name}: {value:.4f}")
        
        return metrics
    
    def cross_validate(
        self, 
        X: np.ndarray, 
        y: np.ndarray, 
        cv: int = 5
    ) -> Dict[str, Any]:
        """Perform cross-validation.
        
        Args:
            X: Features.
            y: Target.
            cv: Number of cross-validation folds.
            
        Returns:
            Dictionary with CV results.
        """
        logger.info(f"Performing {cv}-fold cross-validation for {self.model_name}...")
        
        scoring_metrics = ['neg_mean_absolute_error', 'neg_mean_squared_error', 'r2']
        cv_results = {}
        
        for metric in scoring_metrics:
            scores = cross_val_score(
                self.model, X, y, cv=cv, scoring=metric, n_jobs=-1
            )
            
            # Convert negative metrics back to positive
            if 'neg_' in metric:
                scores = -scores
                metric_name = metric.replace('neg_', '')
            else:
                metric_name = metric
            
            cv_results[f'cv_{metric_name}_mean'] = scores.mean()
            cv_results[f'cv_{metric_name}_std'] = scores.std()
        
        logger.info(f"CV results for {self.model_name}:")
        for key, value in cv_results.items():
            logger.info(f"  {key}: {value:.4f}")
        
        return cv_results
    
    def get_feature_importance(
        self, 
        feature_names: Optional[List[str]] = None
    ) -> Optional[pd.DataFrame]:
        """Get feature importance if available.
        
        Args:
            feature_names: List of feature names.
            
        Returns:
            DataFrame with feature importance or None if not available.
        """
        if not self.is_fitted:
            raise ValueError("Model not fitted. Call fit() first.")
        
        # Check if model has feature_importances_ attribute
        if not hasattr(self.model, 'feature_importances_'):
            logger.warning(f"{self.model_name} doesn't support feature importance")
            return None
        
        importance = self.model.feature_importances_
        
        if feature_names is None:
            feature_names = [f"feature_{i}" for i in range(len(importance))]
        
        importance_df = pd.DataFrame({
            'feature': feature_names,
            'importance': importance
        }).sort_values('importance', ascending=False).reset_index(drop=True)
        
        return importance_df
    
    def save(self, filepath: Optional[Path] = None):
        """Save the trained model.
        
        Args:
            filepath: Path to save the model. If None, uses default path.
        """
        if not self.is_fitted:
            raise ValueError("Model not fitted. Nothing to save.")
        
        if filepath is None:
            filepath = config.models_dir / f"{self.model_name}_model.pkl"
        
        filepath = Path(filepath)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        joblib.dump(self.model, filepath)
        logger.info(f"Model saved to {filepath}")
    
    @classmethod
    def load(cls, filepath: Path, model_name: str = 'xgboost') -> 'ModelTrainer':
        """Load a trained model.
        
        Args:
            filepath: Path to the saved model.
            model_name: Name of the model.
            
        Returns:
            ModelTrainer instance with loaded model.
        """
        trainer = cls(model_name)
        trainer.model = joblib.load(filepath)
        trainer.is_fitted = True
        logger.info(f"Model loaded from {filepath}")
        return trainer


class ModelComparison:
    """Compare multiple models."""
    
    def __init__(self, model_names: Optional[List[str]] = None):
        """Initialize ModelComparison.
        
        Args:
            model_names: List of model names to compare.
        """
        self.model_names = model_names or list(config.model_configs.keys())
        self.trainers: Dict[str, ModelTrainer] = {}
        self.results: Dict[str, Dict[str, float]] = {}
    
    def train_all(
        self, 
        X_train: np.ndarray, 
        y_train: np.ndarray,
        X_test: np.ndarray,
        y_test: np.ndarray
    ):
        """Train all models and evaluate them.
        
        Args:
            X_train: Training features.
            y_train: Training target.
            X_test: Test features.
            y_test: Test target.
        """
        for model_name in self.model_names:
            logger.info(f"\n{'='*60}")
            logger.info(f"Training {model_name.upper()}")
            logger.info(f"{'='*60}")
            
            trainer = ModelTrainer(model_name)
            trainer.fit(X_train, y_train)
            
            # Evaluate on both train and test
            train_metrics = trainer.evaluate(X_train, y_train, 'train')
            test_metrics = trainer.evaluate(X_test, y_test, 'test')
            
            self.trainers[model_name] = trainer
            self.results[model_name] = {**train_metrics, **test_metrics}
    
    def get_comparison_df(self) -> pd.DataFrame:
        """Get comparison results as DataFrame.
        
        Returns:
            DataFrame with comparison results.
        """
        if not self.results:
            raise ValueError("No results available. Train models first.")
        
        df = pd.DataFrame(self.results).T
        df.index.name = 'model'
        return df.reset_index()
    
    def get_best_model(self, metric: str = 'test_r2') -> Tuple[str, ModelTrainer]:
        """Get the best performing model.
        
        Args:
            metric: Metric to use for comparison.
            
        Returns:
            Tuple of (model_name, trainer).
        """
        if not self.results:
            raise ValueError("No results available. Train models first.")
        
        # For error metrics (MAE, MSE, RMSE), lower is better
        reverse = 'mae' in metric or 'mse' in metric or 'rmse' in metric
        
        best_model = min(
            self.results.items(),
            key=lambda x: x[1][metric] if reverse else -x[1][metric]
        )[0]
        
        return best_model, self.trainers[best_model]
