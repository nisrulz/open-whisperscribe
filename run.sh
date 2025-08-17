#!/bin/bash
source venv/bin/activate
nohup python3 -u open_whisperscribe.py &
echo "Open-WhisperScribe script is now running in the background."
echo "You can close this terminal window, if you want." 