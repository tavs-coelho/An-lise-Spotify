"""Visualization utilities for Spotify analysis."""

import logging
from typing import Optional, List, Tuple
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

from spotify_analysis.config import config

logger = logging.getLogger(__name__)

# Set default style
sns.set_style(config.plot_config['style'])
sns.set_context(config.plot_config['context'], font_scale=config.plot_config['font_scale'])


def setup_plot_style():
    """Setup matplotlib and seaborn plot style."""
    plt.rcParams['figure.figsize'] = config.plot_config['figure_size']
    plt.rcParams['figure.dpi'] = config.plot_config['dpi']
    plt.rcParams['font.size'] = 11
    plt.rcParams['axes.labelsize'] = 12
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize'] = 10
    plt.rcParams['legend.fontsize'] = 10


def plot_distribution(
    data: pd.Series,
    title: str = "Distribution",
    xlabel: str = "Value",
    bins: int = 50,
    save_path: Optional[Path] = None
) -> plt.Figure:
    """Plot distribution histogram.
    
    Args:
        data: Data to plot.
        title: Plot title.
        xlabel: X-axis label.
        bins: Number of bins.
        save_path: Path to save the figure.
        
    Returns:
        Matplotlib figure.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.hist(data, bins=bins, color='skyblue', edgecolor='black', alpha=0.7)
    ax.axvline(data.mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {data.mean():.2f}')
    ax.axvline(data.median(), color='green', linestyle='--', linewidth=2, label=f'Median: {data.median():.2f}')
    
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight')
        logger.info(f"Plot saved to {save_path}")
    
    return fig


def plot_correlation_heatmap(
    data: pd.DataFrame,
    features: Optional[List[str]] = None,
    title: str = "Correlation Heatmap",
    save_path: Optional[Path] = None
) -> plt.Figure:
    """Plot correlation heatmap.
    
    Args:
        data: DataFrame with features.
        features: List of features to include. If None, uses all numerical columns.
        title: Plot title.
        save_path: Path to save the figure.
        
    Returns:
        Matplotlib figure.
    """
    if features is None:
        features = data.select_dtypes(include=[np.number]).columns.tolist()
    
    corr_matrix = data[features].corr()
    
    fig, ax = plt.subplots(figsize=(14, 12))
    
    sns.heatmap(
        corr_matrix,
        annot=True,
        fmt='.2f',
        cmap='coolwarm',
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={'shrink': 0.8},
        ax=ax
    )
    
    ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    
    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight')
        logger.info(f"Plot saved to {save_path}")
    
    return fig


def plot_feature_importance(
    importance_df: pd.DataFrame,
    top_n: int = 15,
    title: str = "Feature Importance",
    save_path: Optional[Path] = None
) -> plt.Figure:
    """Plot feature importance.
    
    Args:
        importance_df: DataFrame with 'feature' and 'importance' columns.
        top_n: Number of top features to show.
        title: Plot title.
        save_path: Path to save the figure.
        
    Returns:
        Matplotlib figure.
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    
    top_features = importance_df.head(top_n)
    
    colors = plt.cm.viridis(np.linspace(0, 1, len(top_features)))
    bars = ax.barh(top_features['feature'], top_features['importance'], color=colors)
    
    ax.set_xlabel('Importance', fontsize=12)
    ax.set_ylabel('Feature', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.invert_yaxis()
    ax.grid(True, alpha=0.3, axis='x')
    
    # Add value labels
    for i, bar in enumerate(bars):
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height()/2, 
                f'{width:.4f}',
                ha='left', va='center', fontsize=9)
    
    plt.tight_layout()
    
    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight')
        logger.info(f"Plot saved to {save_path}")
    
    return fig


def plot_predictions_vs_actual(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    title: str = "Predictions vs Actual",
    save_path: Optional[Path] = None
) -> plt.Figure:
    """Plot predictions vs actual values.
    
    Args:
        y_true: True values.
        y_pred: Predicted values.
        title: Plot title.
        save_path: Path to save the figure.
        
    Returns:
        Matplotlib figure.
    """
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Scatter plot
    ax.scatter(y_true, y_pred, alpha=0.5, s=20, color='blue', label='Predictions')
    
    # Perfect prediction line
    min_val = min(y_true.min(), y_pred.min())
    max_val = max(y_true.max(), y_pred.max())
    ax.plot([min_val, max_val], [min_val, max_val], 'r--', lw=2, label='Perfect Prediction')
    
    ax.set_xlabel('Actual Values', fontsize=12)
    ax.set_ylabel('Predicted Values', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Add metrics as text
    from sklearn.metrics import r2_score, mean_absolute_error
    r2 = r2_score(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    
    text_str = f'R² = {r2:.3f}\nMAE = {mae:.3f}'
    ax.text(0.05, 0.95, text_str, transform=ax.transAxes,
            fontsize=11, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    
    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight')
        logger.info(f"Plot saved to {save_path}")
    
    return fig


def plot_model_comparison(
    comparison_df: pd.DataFrame,
    metrics: List[str] = ['test_mae', 'test_r2'],
    save_path: Optional[Path] = None
) -> plt.Figure:
    """Plot model comparison.
    
    Args:
        comparison_df: DataFrame with model comparison results.
        metrics: List of metrics to plot.
        save_path: Path to save the figure.
        
    Returns:
        Matplotlib figure.
    """
    n_metrics = len(metrics)
    fig, axes = plt.subplots(1, n_metrics, figsize=(8 * n_metrics, 6))
    
    if n_metrics == 1:
        axes = [axes]
    
    for i, metric in enumerate(metrics):
        ax = axes[i]
        
        # Determine if lower is better (for error metrics)
        lower_is_better = 'mae' in metric or 'mse' in metric or 'rmse' in metric
        
        data = comparison_df.sort_values(metric, ascending=lower_is_better)
        colors = plt.cm.RdYlGn_r(np.linspace(0.3, 0.9, len(data))) if lower_is_better else \
                 plt.cm.RdYlGn(np.linspace(0.3, 0.9, len(data)))
        
        bars = ax.barh(data['model'], data[metric], color=colors)
        
        ax.set_xlabel(metric.upper(), fontsize=12)
        ax.set_ylabel('Model', fontsize=12)
        ax.set_title(f'{metric.upper()} Comparison', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3, axis='x')
        
        # Add value labels
        for bar in bars:
            width = bar.get_width()
            ax.text(width, bar.get_y() + bar.get_height()/2,
                   f'{width:.3f}',
                   ha='left', va='center', fontsize=10)
    
    plt.tight_layout()
    
    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight')
        logger.info(f"Plot saved to {save_path}")
    
    return fig


def plot_residuals(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    title: str = "Residual Plot",
    save_path: Optional[Path] = None
) -> plt.Figure:
    """Plot residuals.
    
    Args:
        y_true: True values.
        y_pred: Predicted values.
        title: Plot title.
        save_path: Path to save the figure.
        
    Returns:
        Matplotlib figure.
    """
    residuals = y_true - y_pred
    
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Residual scatter plot
    axes[0].scatter(y_pred, residuals, alpha=0.5, s=20, color='purple')
    axes[0].axhline(y=0, color='r', linestyle='--', lw=2)
    axes[0].set_xlabel('Predicted Values', fontsize=12)
    axes[0].set_ylabel('Residuals', fontsize=12)
    axes[0].set_title('Residual Plot', fontsize=14, fontweight='bold')
    axes[0].grid(True, alpha=0.3)
    
    # Residual distribution
    axes[1].hist(residuals, bins=50, color='green', edgecolor='black', alpha=0.7)
    axes[1].axvline(residuals.mean(), color='red', linestyle='--', linewidth=2,
                    label=f'Mean: {residuals.mean():.2f}')
    axes[1].set_xlabel('Residuals', fontsize=12)
    axes[1].set_ylabel('Frequency', fontsize=12)
    axes[1].set_title('Residual Distribution', fontsize=14, fontweight='bold')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    
    fig.suptitle(title, fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    
    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight')
        logger.info(f"Plot saved to {save_path}")
    
    return fig


# Initialize plot style when module is imported
setup_plot_style()
