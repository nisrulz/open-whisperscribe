#!/bin/bash
# Exit on any error and treat unset variables as an error
set -eu

# Create virtual environment if it doesn't exist
echo ""
echo "====================================================================="
echo "Checking if virtual environment exists..."
if [ ! -d "venv" ]; then
  echo "Virtual environment not found. Creating one..."
  python3 -m venv venv
else
  echo "Virtual environment already exists."
fi

# Activate virtual environment
echo ""
echo "====================================================================="
echo "Activating the virtual environment..."
source venv/bin/activate

# Upgrade pip
echo ""
echo "====================================================================="
echo "Upgrading pip to the latest version..."
pip install --upgrade pip

# Install project dependencies
echo ""
echo "====================================================================="
echo "Installing project dependencies from requirements.txt..."
pip install -r requirements.txt

# Check if python-tk is already installed
if ! python3 -c "import tkinter" &> /dev/null; then
  echo "Installing python-tk..."
  brew install python-tk
else
  echo "python-tk is already installed."
fi

# Check if microphone permission is already granted
python3 src/check_mic_permission.py

# Check for Accessibility permission
echo ""
echo "====================================================================="
echo "Please enable Accessibility permissions for your Terminal app:"
echo "1. Open 'System Settings' > 'Privacy & Security' > 'Accessibility'."
echo "2. Click the '+' button and add your Terminal app."
echo "3. Enable the checkbox next to your Terminal app."
open "x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility"
echo "Press Enter once you have granted Accessibility permissions."
read -p "Press Enter to continue..."


# Check for Input Monitoring permission
echo ""
echo "====================================================================="
echo "Please enable Input Monitoring permissions for your Terminal app:"
echo "1. Open 'System Settings' > 'Privacy & Security' > 'Input Monitoring'."
echo "2. Click the '+' button and add your Terminal app."
echo "3. Enable the checkbox next to your Terminal app."
open "x-apple.systempreferences:com.apple.preference.security?Privacy_ListenEvent"
echo "Press Enter once you have granted Input Monitoring permissions."
read -p "Press Enter to continue..."

# Check for Microphone permission
echo ""
echo "====================================================================="
echo "Please enable Microphone permissions for your Terminal app:"
echo "1. Open 'System Settings' > 'Privacy & Security' > 'Microphone'."
echo "3. Ensure that the checkbox next to your Terminal app is enabled."
open "x-apple.systempreferences:com.apple.preference.security?Privacy_Microphone"
echo "Press Enter once you have granted Microphone permissions."
read -p "Press Enter to continue..."

echo "Setup complete. The environment is ready to use."