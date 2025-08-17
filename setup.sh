#!/bin/bash
# Exit on any error and treat unset variables as an error
set -eu

# Create virtual environment if it doesn't exist
echo "Checking if virtual environment exists..."
if [ ! -d "venv" ]; then
  echo "Virtual environment not found. Creating one..."
  python3 -m venv venv
else
  echo "Virtual environment already exists."
fi

# Activate virtual environment
echo "Activating the virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip to the latest version..."
pip install --upgrade pip

# Install project dependencies
echo "Installing project dependencies from requirements.txt..."
pip install -r requirements.txt

echo "Setup complete. The environment is ready to use."