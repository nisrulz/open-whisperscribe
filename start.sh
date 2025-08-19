#!/bin/bash
# Exit on any error and treat unset variables as an error
set -eu

echo "Starting Open-WhisperScribe in the background..."
nohup python3 -u open_whisperscribe.py &

echo ""
echo "Open-WhisperScribe script is now running in the background."
echo "You can close this terminal window, if you want."