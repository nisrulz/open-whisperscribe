#!/bin/bash
# Exit on any error and treat unset variables as an error
set -eu

echo "Stopping any running Open-WhisperScribe processes..."
./stop.sh

echo "Starting the GUI..."
nohup uv run gui.py &

echo "✅ GUI started successfully"
