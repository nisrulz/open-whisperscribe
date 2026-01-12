#!/bin/bash
# Exit on any error and treat unset variables as an error
set -eu

# Find the PID(s) of running Open-WhisperScribe processes
echo "Searching for Open-WhisperScribe and GUI processes..."
PIDS=$(pgrep -f "open_whisperscribe.py|gui.py" || true)

if [ -z "$PIDS" ]; then
  echo "No Open-WhisperScribe or GUI process found. Nothing to stop."
  exit 0
fi

echo "Killing Open-WhisperScribe process(es): $PIDS"

# Attempt graceful termination
kill $PIDS
echo "Sent termination signal to process(es). Waiting for them to stop..."

sleep 2

# Force kill if still running
echo "Checking if any processes are still running..."
PIDS=$(pgrep -f "open_whisperscribe.py|gui.py" || true)
if [ -n "$PIDS" ]; then
  echo "Force killing remaining process(es): $PIDS"
  kill -9 $PIDS
fi

echo "All Open-WhisperScribe and GUI processes stopped successfully."