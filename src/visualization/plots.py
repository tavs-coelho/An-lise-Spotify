"""
Advanced visualization module for Spotify data analysis.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from typing import List, Tuple, Optional
import logging

logger = logging.getLogger(__name__)


class SpotifyVisualizer:
    """Class for creating visualizations for Spotify music data."""
    
    def __init__(self, style: str = 'seaborn-v0_8-darkgrid'):
        """
        Initialize visualizer with style.
        
        Args:
            style: Matplotlib style to use
        """
        try:
            plt.style.use(style)
        except OSError:
            plt.style.use('default')
            logger.warning(f"Style '{style}' not found, using default style")
        
        # Set Spotify-like colors
        self.colors = {
            'primary': '#1DB954',
            'secondary': '#191414',
            'accent': '#535353',
            'light': '#B3B3B3'
        }
        
        sns.set_palette([self.colors['primary'], self.colors['accent']])
    
    def plot_feature_distributions(
        self, 
        df: pd.DataFrame, 
        features: List[str],
        figsize: Tuple[int, int] = (15, 10)
    ) -> plt.Figure:
        """
        Plot distributions of multiple features.
        
        Args:
            df: Input DataFrame
            features: List of feature names to plot
            figsize: Figure size
            
        Returns:
            Matplotlib figure
        """
        n_features = len(features)
        n_cols = 3
        n_rows = (n_features + n_cols - 1) // n_cols
        
        fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
        axes = axes.flatten() if n_features > 1 else [axes]
        
        for idx, feature in enumerate(features):
            if feature not in df.columns:
                continue
                
            ax = axes[idx]
            ax.hist(df[feature], bins=50, color=self.colors['primary'], 
                   alpha=0.7, edgecolor='black')
            ax.set_xlabel(feature.replace('_', ' ').title(), fontsize=10)
            ax.set_ylabel('Frequency', fontsize=10)
            ax.set_title(f'Distribution of {feature.replace("_", " ").title()}', 
                        fontsize=11, fontweight='bold')
            ax.grid(True, alpha=0.3)
        
        # Hide empty subplots
        for idx in range(n_features, len(axes)):
            axes[idx].axis('off')
        
        plt.tight_layout()
        logger.info(f"Created distribution plots for {n_features} features")
        
        return fig
    
    def plot_correlation_heatmap(
        self,
        df: pd.DataFrame,
        features: Optional[List[str]] = None,
        figsize: Tuple[int, int] = (12, 10)
    ) -> plt.Figure:
        """
        Plot correlation heatmap.
        
        Args:
            df: Input DataFrame
            features: List of features to include (None for all numeric)
            figsize: Figure size
            
        Returns:
            Matplotlib figure
        """
        if features is None:
            features = df.select_dtypes(include=[np.number]).columns.tolist()
        
        fig, ax = plt.subplots(figsize=figsize)
        
        correlation = df[features].corr()
        
        mask = np.triu(np.ones_like(correlation, dtype=bool))
        
        sns.heatmap(
            correlation, 
            mask=mask,
            annot=True, 
            fmt='.2f', 
            cmap='RdYlGn',
            center=0,
            square=True,
            linewidths=1,
            cbar_kws={"shrink": 0.8, "label": "Correlation"},
            ax=ax
        )
        
        ax.set_title('Feature Correlation Matrix', 
                    fontsize=14, fontweight='bold', pad=20)
        
        plt.tight_layout()
        logger.info("Created correlation heatmap")
        
        return fig
    
    def plot_feature_importance(
        self,
        feature_names: List[str],
        importances: np.ndarray,
        top_n: int = 10,
        figsize: Tuple[int, int] = (10, 6)
    ) -> plt.Figure:
        """
        Plot feature importance.
        
        Args:
            feature_names: List of feature names
            importances: Array of importance values
            top_n: Number of top features to show
            figsize: Figure size
            
        Returns:
            Matplotlib figure
        """
        # Sort by importance
        indices = np.argsort(importances)[::-1][:top_n]
        
        fig, ax = plt.subplots(figsize=figsize)
        
        ax.barh(
            range(top_n), 
            importances[indices][::-1],
            color=self.colors['primary'],
            alpha=0.8
        )
        
        ax.set_yticks(range(top_n))
        ax.set_yticklabels([feature_names[i] for i in indices[::-1]])
        ax.set_xlabel('Importance Score', fontsize=11)
        ax.set_title(f'Top {top_n} Most Important Features', 
                    fontsize=13, fontweight='bold')
        ax.grid(True, alpha=0.3, axis='x')
        
        plt.tight_layout()
        logger.info(f"Created feature importance plot for top {top_n} features")
        
        return fig
    
    def plot_model_comparison(
        self,
        results: dict,
        metric: str = 'r2',
        figsize: Tuple[int, int] = (10, 6)
    ) -> plt.Figure:
        """
        Plot model comparison.
        
        Args:
            results: Dictionary with model results
            metric: Metric to compare ('r2', 'mae', 'rmse')
            figsize: Figure size
            
        Returns:
            Matplotlib figure
        """
        model_names = list(results.keys())
        metric_values = [results[name][metric] for name in model_names]
        
        fig, ax = plt.subplots(figsize=figsize)
        
        bars = ax.bar(
            model_names,
            metric_values,
            color=[self.colors['primary'], self.colors['accent'], self.colors['light']],
            alpha=0.8,
            edgecolor='black'
        )
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2.,
                height,
                f'{height:.3f}',
                ha='center',
                va='bottom',
                fontsize=10,
                fontweight='bold'
            )
        
        ax.set_ylabel(metric.upper(), fontsize=11)
        ax.set_title(f'Model Comparison - {metric.upper()}', 
                    fontsize=13, fontweight='bold')
        ax.grid(True, alpha=0.3, axis='y')
        
        plt.tight_layout()
        logger.info(f"Created model comparison plot for {metric}")
        
        return fig
    
    def plot_actual_vs_predicted(
        self,
        y_true: np.ndarray,
        y_pred: np.ndarray,
        figsize: Tuple[int, int] = (10, 8)
    ) -> plt.Figure:
        """
        Plot actual vs predicted values.
        
        Args:
            y_true: Actual values
            y_pred: Predicted values
            figsize: Figure size
            
        Returns:
            Matplotlib figure
        """
        fig, ax = plt.subplots(figsize=figsize)
        
        ax.scatter(
            y_true, 
            y_pred, 
            alpha=0.5, 
            color=self.colors['primary'],
            s=20,
            edgecolors='black',
            linewidth=0.5
        )
        
        # Perfect prediction line
        min_val = min(y_true.min(), y_pred.min())
        max_val = max(y_true.max(), y_pred.max())
        ax.plot(
            [min_val, max_val], 
            [min_val, max_val], 
            'r--', 
            lw=2, 
            label='Perfect Prediction'
        )
        
        ax.set_xlabel('Actual Popularity', fontsize=11)
        ax.set_ylabel('Predicted Popularity', fontsize=11)
        ax.set_title('Actual vs Predicted Popularity', 
                    fontsize=13, fontweight='bold')
        ax.legend(fontsize=10)
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        logger.info("Created actual vs predicted plot")
        
        return fig
    
    def plot_residuals(
        self,
        y_true: np.ndarray,
        y_pred: np.ndarray,
        figsize: Tuple[int, int] = (12, 5)
    ) -> plt.Figure:
        """
        Plot residual analysis.
        
        Args:
            y_true: Actual values
            y_pred: Predicted values
            figsize: Figure size
            
        Returns:
            Matplotlib figure
        """
        residuals = y_true - y_pred
        
        fig, axes = plt.subplots(1, 2, figsize=figsize)
        
        # Residuals vs Predicted
        axes[0].scatter(
            y_pred, 
            residuals, 
            alpha=0.5, 
            color=self.colors['primary'],
            s=20
        )
        axes[0].axhline(y=0, color='r', linestyle='--', lw=2)
        axes[0].set_xlabel('Predicted Values', fontsize=10)
        axes[0].set_ylabel('Residuals', fontsize=10)
        axes[0].set_title('Residuals vs Predicted', fontsize=11, fontweight='bold')
        axes[0].grid(True, alpha=0.3)
        
        # Residuals distribution
        axes[1].hist(
            residuals, 
            bins=50, 
            color=self.colors['primary'],
            alpha=0.7,
            edgecolor='black'
        )
        axes[1].set_xlabel('Residuals', fontsize=10)
        axes[1].set_ylabel('Frequency', fontsize=10)
        axes[1].set_title('Residuals Distribution', fontsize=11, fontweight='bold')
        axes[1].axvline(x=0, color='r', linestyle='--', lw=2)
        axes[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        logger.info("Created residuals analysis plot")
        
        return fig
    
    def plot_box_plots(
        self,
        df: pd.DataFrame,
        features: List[str],
        figsize: Tuple[int, int] = (15, 10)
    ) -> plt.Figure:
        """
        Plot box plots for multiple features.
        
        Args:
            df: Input DataFrame
            features: List of features to plot
            figsize: Figure size
            
        Returns:
            Matplotlib figure
        """
        n_features = len(features)
        n_cols = 3
        n_rows = (n_features + n_cols - 1) // n_cols
        
        fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
        axes = axes.flatten() if n_features > 1 else [axes]
        
        for idx, feature in enumerate(features):
            if feature not in df.columns:
                continue
                
            ax = axes[idx]
            box = ax.boxplot(
                df[feature].dropna(),
                vert=True,
                patch_artist=True,
                widths=0.5
            )
            
            for patch in box['boxes']:
                patch.set_facecolor(self.colors['primary'])
                patch.set_alpha(0.7)
            
            ax.set_ylabel('Value', fontsize=10)
            ax.set_title(f'{feature.replace("_", " ").title()}', 
                        fontsize=11, fontweight='bold')
            ax.grid(True, alpha=0.3, axis='y')
        
        # Hide empty subplots
        for idx in range(n_features, len(axes)):
            axes[idx].axis('off')
        
        plt.tight_layout()
        logger.info(f"Created box plots for {n_features} features")
        
        return fig


def save_figure(fig: plt.Figure, filename: str, dpi: int = 300):
    """
    Save figure to file.
    
    Args:
        fig: Matplotlib figure
        filename: Output filename
        dpi: Resolution in dots per inch
    """
    fig.savefig(filename, dpi=dpi, bbox_inches='tight')
    logger.info(f"Saved figure to {filename}")
