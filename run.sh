#!/bin/bash
# Exit on any error and treat unset variables as an error
set -eu

# Activate the virtual environment
echo "Activating the virtual environment..."
source venv/bin/activate

echo "Stopping any running Open-WhisperScribe processes..."
./stop.sh

echo "Starting Open-WhisperScribe in the background..."
nohup python3 -u open_whisperscribe.py &

echo ""
echo "Open-WhisperScribe script is now running in the background."
echo "You can close this terminal window, if you want."