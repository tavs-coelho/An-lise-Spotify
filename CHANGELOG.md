# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-12-15

### Added
- Complete professional package structure with `src/spotify_analysis/`
- FastAPI REST API for model serving with OpenAPI documentation
- Interactive Streamlit dashboard with real-time predictions
- Docker and Docker Compose support for containerized deployment
- Comprehensive CI/CD pipeline with GitHub Actions
- Unit and integration tests with pytest
- Code quality tools integration (black, flake8, mypy, isort, bandit)
- Type hints on all functions
- Comprehensive docstrings following Google style
- Data processing module with preprocessing pipelines
- Model training module with 6 regression algorithms
- Visualization utilities with publication-quality plots
- Configuration management system
- Logging and error handling utilities
- MIT License for open source distribution
- Professional README with badges and documentation
- CONTRIBUTING.md with development guidelines
- Makefile for common development tasks
- Requirements.txt with pinned dependencies
- pyproject.toml for modern Python packaging

### Changed
- Reorganized project structure following Python best practices
- Moved legacy scripts to `legacy_scripts/` folder
- Moved documentation to `docs/` folder
- Moved notebook to `notebooks/` folder
- Updated README with comprehensive instructions

### Fixed
- Import errors and module dependencies
- Security issues identified by CodeQL
- Code quality issues identified by linters
- Duplicate dependencies in requirements.txt
- Missing permissions in GitHub Actions workflow

### Security
- Added security scanning with bandit
- Implemented proper GITHUB_TOKEN permissions
- Added dependency security checks with safety

## [0.1.0] - Initial Release

### Added
- Basic analysis notebook
- Simple Python scripts for data processing
- XGBoost model training
- Basic visualizations
- Technical report in Portuguese
