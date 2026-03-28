#!/bin/bash
set -e

echo "Setting up Object Detection app..."

# Create virtual environment
python3 -m venv .venv
echo "Virtual environment created."

# Activate and install dependencies
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "Setup complete! To run the app:"
echo "  source .venv/bin/activate"
echo "  python -m src.main"
echo ""
echo "Options:"
echo "  --gpu           Enable Metal GPU acceleration"
echo "  --confidence 0.3  Lower detection threshold"
echo "  --model yolov8s.pt  Use a larger model for better accuracy"
