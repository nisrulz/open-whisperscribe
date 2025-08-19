#!/bin/bash
# Exit on any error and treat unset variables as an error
set -eu

# Activate the virtual environment
echo "Activating the virtual environment..."
source venv/bin/activate

echo "Stopping any running Open-WhisperScribe processes..."
./stop.sh

echo "Starting the GUI..."
nohup python3 -u gui.py &

echo "✅ GUI started successfully"
