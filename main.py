"""
Main entry point for Spotify Music Popularity Analysis.
"""

import logging
from pathlib import Path
from src.utils.config import load_config, setup_logging
from src.data.loader import DataLoader
from src.models.predictor import PopularityPredictor

logger = logging.getLogger(__name__)


def main():
    """Main execution function."""
    # Load configuration
    config = load_config('config.yaml')
    setup_logging(config)
    
    logger.info("="*80)
    logger.info("Spotify Music Popularity Analysis - Starting")
    logger.info("="*80)
    
    # Load and prepare data
    logger.info("\n1. Loading and preparing data...")
    data_loader = DataLoader(config)
    df = data_loader.load_data()
    df_clean = data_loader.clean_data(df)
    X, y = data_loader.split_features_target(df_clean)
    
    logger.info(f"Dataset shape: {df_clean.shape}")
    logger.info(f"Features: {X.shape[1]}")
    logger.info(f"Target (popularity) - Mean: {y.mean():.2f}, Std: {y.std():.2f}")
    
    # Train models
    logger.info("\n2. Training machine learning models...")
    predictor = PopularityPredictor(config)
    results = predictor.train_models(X, y)
    
    # Display results
    logger.info("\n3. Model Comparison Results:")
    logger.info("-" * 80)
    logger.info(f"{'Model':<15} {'MAE':<10} {'RMSE':<10} {'R²':<10} {'CV R²':<15}")
    logger.info("-" * 80)
    
    for model_name, metrics in results.items():
        logger.info(
            f"{model_name:<15} "
            f"{metrics['mae']:<10.2f} "
            f"{metrics['rmse']:<10.2f} "
            f"{metrics['r2']:<10.3f} "
            f"{metrics['cv_mean']:.3f} (±{metrics['cv_std']:.3f})"
        )
    
    # Save best model
    logger.info("\n4. Saving best model...")
    predictor.save_model('XGBoost', 'models/xgboost_model.pkl')
    
    logger.info("\n" + "="*80)
    logger.info("Analysis completed successfully!")
    logger.info("="*80)
    
    # Example prediction
    logger.info("\n5. Example Prediction:")
    sample = X.iloc[:1]
    prediction = predictor.predict(sample, 'XGBoost')
    logger.info(f"Sample features:\n{sample.to_dict('records')[0]}")
    logger.info(f"Predicted popularity: {prediction[0]:.2f}")
    logger.info(f"Actual popularity: {y.iloc[0]:.2f}")


if __name__ == "__main__":
    main()
