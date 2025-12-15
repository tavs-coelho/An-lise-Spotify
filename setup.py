"""Setup configuration for Spotify Music Popularity Analysis package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="spotify-analysis",
    version="1.0.0",
    author="Geyson de Araujo",
    description="Machine Learning analysis of Spotify music popularity",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tavs-coelho/An-lise-Spotify",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "scikit-learn>=1.3.0",
        "xgboost>=2.0.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "scipy>=1.10.0",
        "joblib>=1.3.0",
        "tqdm>=4.65.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
        "ml": [
            "shap>=0.42.0",
            "mlflow>=2.9.0",
        ],
        "web": [
            "streamlit>=1.28.0",
            "fastapi>=0.108.0",
            "uvicorn>=0.24.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "spotify-analysis=spotify_analysis.cli:main",
        ],
    },
)
