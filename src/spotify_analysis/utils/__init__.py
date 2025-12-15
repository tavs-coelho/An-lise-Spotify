"""Utility functions for the Spotify analysis project."""

import logging
import sys
from pathlib import Path
from typing import Optional

from spotify_analysis.config import config


def setup_logging(
    log_file: Optional[Path] = None,
    level: int = logging.INFO
) -> logging.Logger:
    """Setup logging configuration.
    
    Args:
        log_file: Path to log file. If None, logs only to console.
        level: Logging level.
        
    Returns:
        Configured logger.
    """
    # Create logger
    logger = logging.getLogger('spotify_analysis')
    logger.setLevel(level)
    
    # Remove existing handlers
    logger.handlers = []
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler (if specified)
    if log_file:
        log_file = Path(log_file)
        log_file.parent.mkdir(parents=True, exist_ok=True)
        
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger


def print_section_header(title: str, char: str = '=', width: int = 80):
    """Print a formatted section header.
    
    Args:
        title: Section title.
        char: Character to use for the border.
        width: Width of the header.
    """
    print(f"\n{char * width}")
    print(f"{title.center(width)}")
    print(f"{char * width}\n")


def print_dict(data: dict, indent: int = 0):
    """Pretty print a dictionary.
    
    Args:
        data: Dictionary to print.
        indent: Indentation level.
    """
    for key, value in data.items():
        if isinstance(value, dict):
            print('  ' * indent + f"{key}:")
            print_dict(value, indent + 1)
        else:
            print('  ' * indent + f"{key}: {value}")


def format_metrics(metrics: dict, precision: int = 4) -> dict:
    """Format metrics dictionary for display.
    
    Args:
        metrics: Dictionary of metrics.
        precision: Number of decimal places.
        
    Returns:
        Formatted metrics dictionary.
    """
    return {k: round(v, precision) if isinstance(v, float) else v 
            for k, v in metrics.items()}
