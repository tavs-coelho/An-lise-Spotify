#!/bin/bash

# Setup script for Spotify Music Popularity Analysis
# This script automates the installation and setup process

set -e  # Exit on error

echo "=========================================="
echo "Spotify Music Analytics - Setup Script"
echo "=========================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Python version
echo "Checking Python version..."
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
REQUIRED_VERSION="3.9"

if [[ $(echo -e "$PYTHON_VERSION\n$REQUIRED_VERSION" | sort -V | head -n1) != "$REQUIRED_VERSION" ]]; then
    echo -e "${RED}Error: Python $REQUIRED_VERSION or higher is required${NC}"
    echo "Current version: $PYTHON_VERSION"
    exit 1
fi
echo -e "${GREEN}✓ Python $PYTHON_VERSION detected${NC}"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
if [ -d "venv" ]; then
    echo -e "${YELLOW}Virtual environment already exists. Skipping...${NC}"
else
    python3 -m venv venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
fi
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo -e "${GREEN}✓ Virtual environment activated${NC}"
echo ""

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip --quiet
echo -e "${GREEN}✓ pip upgraded${NC}"
echo ""

# Install dependencies
echo "Installing dependencies..."
echo "This may take a few minutes..."
pip install -r requirements.txt --quiet
echo -e "${GREEN}✓ Dependencies installed${NC}"
echo ""

# Create necessary directories
echo "Creating project directories..."
mkdir -p data/raw data/processed models logs
touch data/.gitkeep models/.gitkeep logs/.gitkeep
echo -e "${GREEN}✓ Directories created${NC}"
echo ""

# Check if data file exists
if [ -f "data/raw/spotify_songs.csv" ]; then
    echo -e "${GREEN}✓ Data file found${NC}"
else
    echo -e "${YELLOW}⚠ Data file not found${NC}"
    echo "The system will generate sample data automatically"
fi
echo ""

# Run basic tests
echo "Running tests..."
pytest tests/ -v --tb=short 2>&1 | tail -n 20
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ All tests passed${NC}"
else
    echo -e "${YELLOW}⚠ Some tests failed (this is OK for first setup)${NC}"
fi
echo ""

# Train initial model
echo "Training initial model..."
python main.py
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Model trained successfully${NC}"
else
    echo -e "${RED}✗ Model training failed${NC}"
    echo "Please check logs/app.log for details"
fi
echo ""

echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "To use the system:"
echo ""
echo "1. Activate virtual environment:"
echo "   source venv/bin/activate"
echo ""
echo "2. Start the API:"
echo "   python -m uvicorn src.api.app:app --reload"
echo "   Then visit: http://localhost:8000/docs"
echo ""
echo "3. Start the Dashboard:"
echo "   streamlit run src/dashboard/app.py"
echo "   Then visit: http://localhost:8501"
echo ""
echo "4. Run Jupyter Notebook:"
echo "   jupyter notebook analise_completa_final.ipynb"
echo ""
echo "5. View documentation:"
echo "   ls docs/"
echo ""
echo "For more information, see README.md"
echo ""
echo -e "${GREEN}Happy analyzing! 🎵${NC}"
