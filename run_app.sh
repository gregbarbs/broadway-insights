#!/bin/bash

# === Setup script for Broadway Gross Prediction App ===

echo "Creating virtual environment..."
python3 -m venv .venv

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Training model..."
PYTHONPATH=. python models/train_linear_model.py

echo "Launching backend server..."
python backend/app.py