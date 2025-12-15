# Contributing to Spotify Music Popularity Analysis

First off, thank you for considering contributing to this project! 🎉

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project adheres to a Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

### Our Standards

- **Be respectful** and inclusive
- **Be collaborative** and constructive
- **Focus on what is best** for the community
- **Show empathy** towards other community members

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the problem
- **Expected vs actual behavior**
- **System information** (OS, Python version, etc.)
- **Code samples** if applicable

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear title and description**
- **Rationale** for the enhancement
- **Possible implementation** approach
- **Examples** of how it would work

### Pull Requests

- Fill in the required template
- Follow the coding standards
- Include tests for new features
- Update documentation as needed
- Ensure CI/CD pipeline passes

## Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub
# Clone your fork
git clone https://github.com/YOUR_USERNAME/An-lise-Spotify.git
cd An-lise-Spotify

# Add upstream remote
git remote add upstream https://github.com/tavs-coelho/An-lise-Spotify.git
```

### 2. Create Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -e .

# Install development dependencies
pip install pytest pytest-cov black flake8 mypy isort bandit
```

### 3. Create Feature Branch

```bash
git checkout -b feature/your-feature-name
```

## Coding Standards

### Python Style Guide

This project follows **PEP 8** with some modifications:

- **Line length:** 100 characters (not 79)
- **String quotes:** Use double quotes for strings
- **Imports:** Organized with isort
- **Formatting:** Black for auto-formatting

### Type Hints

All functions should include type hints:

```python
def process_data(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """Process the DataFrame.
    
    Args:
        df: Input DataFrame
        threshold: Processing threshold
        
    Returns:
        Processed DataFrame
    """
    # Implementation
    return df
```

### Documentation

All modules, classes, and functions must have docstrings:

```python
def calculate_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> Dict[str, float]:
    """Calculate evaluation metrics.
    
    Computes MAE, MSE, RMSE, and R² score for the predictions.
    
    Args:
        y_true: True values
        y_pred: Predicted values
        
    Returns:
        Dictionary containing metric names and values
        
    Raises:
        ValueError: If arrays have different shapes
        
    Example:
        >>> y_true = np.array([1, 2, 3])
        >>> y_pred = np.array([1.1, 2.1, 2.9])
        >>> metrics = calculate_metrics(y_true, y_pred)
        >>> print(metrics['mae'])
        0.1
    """
    # Implementation
```

### Testing

- Write unit tests for all new features
- Aim for >80% code coverage
- Use descriptive test names
- Follow AAA pattern (Arrange, Act, Assert)

```python
def test_model_training_with_valid_data():
    """Test that model trains successfully with valid input data."""
    # Arrange
    X_train = np.random.randn(100, 10)
    y_train = np.random.randint(0, 100, 100)
    trainer = ModelTrainer('xgboost')
    
    # Act
    trainer.fit(X_train, y_train)
    
    # Assert
    assert trainer.is_fitted
    assert trainer.model is not None
```

## Code Quality Tools

### Run Before Committing

```bash
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Check code quality
flake8 src/ tests/

# Type check
mypy src/

# Run tests
pytest

# Security scan
bandit -r src/
```

### Pre-commit Hook (Optional)

Create `.git/hooks/pre-commit`:

```bash
#!/bin/bash
black src/ tests/ --check
isort src/ tests/ --check-only
flake8 src/ tests/
pytest
```

## Commit Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat:** New feature
- **fix:** Bug fix
- **docs:** Documentation changes
- **style:** Code style changes (formatting, etc.)
- **refactor:** Code refactoring
- **test:** Adding or updating tests
- **chore:** Maintenance tasks

### Examples

```
feat(models): add SHAP explainer for model interpretability

Implemented SHAP values calculation to provide detailed
explanations for XGBoost predictions.

Closes #123
```

```
fix(api): correct validation error in prediction endpoint

Fixed issue where certain valid input values were being
rejected due to incorrect validation bounds.

Fixes #456
```

## Pull Request Process

### Before Submitting

1. **Update your fork:**
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Run all checks:**
   ```bash
   make test  # Or run tests manually
   black src/ tests/
   flake8 src/ tests/
   ```

3. **Update documentation** if needed

4. **Add tests** for new features

### PR Template

When creating a PR, include:

- **Description:** What does this PR do?
- **Motivation:** Why is this change needed?
- **Testing:** How was it tested?
- **Screenshots:** If applicable
- **Checklist:** 
  - [ ] Tests pass
  - [ ] Code formatted
  - [ ] Documentation updated
  - [ ] CHANGELOG updated (if applicable)

### Review Process

- Maintainers will review your PR
- Address review comments
- Keep PR focused and small
- Be patient and respectful

## Development Workflow

```bash
# 1. Sync with upstream
git checkout main
git fetch upstream
git merge upstream/main

# 2. Create feature branch
git checkout -b feature/my-feature

# 3. Make changes
# ... code, test, commit ...

# 4. Run quality checks
black src/ tests/
pytest
flake8 src/

# 5. Push to your fork
git push origin feature/my-feature

# 6. Create Pull Request on GitHub
```

## Questions?

Feel free to:
- Open an issue for questions
- Contact maintainers
- Join discussions

## Recognition

Contributors will be recognized in:
- README acknowledgments
- CONTRIBUTORS.md file
- Release notes

Thank you for contributing! 🎵✨
