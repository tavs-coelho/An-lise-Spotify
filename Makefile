# Makefile for Spotify Music Popularity Analysis

.PHONY: help install test lint format clean run-api run-dashboard docker-build docker-up docker-down

# Variables
PYTHON := python3
PIP := pip3
PYTEST := pytest
BLACK := black
ISORT := isort
FLAKE8 := flake8
MYPY := mypy

# Default target
help:
	@echo "Spotify Music Popularity Analysis - Makefile Commands"
	@echo ""
	@echo "Setup:"
	@echo "  make install          Install dependencies"
	@echo "  make install-dev      Install with development dependencies"
	@echo ""
	@echo "Development:"
	@echo "  make format           Format code with black and isort"
	@echo "  make lint             Run flake8 linter"
	@echo "  make typecheck        Run mypy type checker"
	@echo "  make test             Run tests"
	@echo "  make test-cov         Run tests with coverage"
	@echo "  make quality          Run all quality checks"
	@echo ""
	@echo "Running:"
	@echo "  make run-api          Start FastAPI server"
	@echo "  make run-dashboard    Start Streamlit dashboard"
	@echo "  make notebook         Start Jupyter notebook"
	@echo ""
	@echo "Docker:"
	@echo "  make docker-build     Build Docker images"
	@echo "  make docker-up        Start all services"
	@echo "  make docker-down      Stop all services"
	@echo ""
	@echo "Cleanup:"
	@echo "  make clean            Remove generated files"
	@echo "  make clean-all        Deep clean including caches"

# Installation
install:
	$(PIP) install -r requirements.txt
	$(PIP) install -e .

install-dev:
	$(PIP) install -r requirements.txt
	$(PIP) install -e .
	$(PIP) install pytest pytest-cov black flake8 mypy isort bandit

# Code quality
format:
	$(BLACK) src/ tests/ --line-length=100
	$(ISORT) src/ tests/

lint:
	$(FLAKE8) src/ tests/ --max-line-length=100 --extend-ignore=E203

typecheck:
	$(MYPY) src/ --ignore-missing-imports

quality: format lint typecheck

# Testing
test:
	$(PYTEST) tests/ -v

test-cov:
	$(PYTEST) tests/ --cov=src/spotify_analysis --cov-report=html --cov-report=term

test-fast:
	$(PYTEST) tests/ -x --ff

# Security
security:
	bandit -r src/ -f json -o bandit-report.json

# Running applications
run-api:
	uvicorn api:app --reload --host 0.0.0.0 --port 8000

run-dashboard:
	streamlit run app.py

notebook:
	jupyter notebook

# Docker
docker-build:
	docker-compose build

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

docker-logs:
	docker-compose logs -f

# Cleanup
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf htmlcov
	rm -rf .coverage
	rm -f bandit-report.json

clean-all: clean
	rm -rf venv
	rm -rf dist
	rm -rf build
	find . -type d -name "mlruns" -exec rm -rf {} + 2>/dev/null || true
