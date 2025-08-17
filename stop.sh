#!/bin/bash

# Find the PID(s) of running Open-WhisperScribe processes
PIDS=$(pgrep -f open_whisperscribe.py)

if [ -z "$PIDS" ]; then
  echo "No Open-WhisperScribe process found."
  exit 0
fi

echo "Killing Open-WhisperScribe process(es) with PID(s): $PIDS"

# Attempt graceful termination
kill $PIDS

sleep 2

# Force kill if still running
PIDS=$(pgrep -f open_whisperscribe.py)
if [ ! -z "$PIDS" ]; then
  echo "Force killing remaining process(es): $PIDS"
  kill -9 $PIDS
fi

echo "All Open-WhisperScribe processes stopped."