import sounddevice as sd
from pynput import keyboard
from src.config_loader import load_config
from src.hotkey_combination import HOTKEY_COMBINATION

config = load_config()

def list_input_devices():
    print("Available input devices:")
    for i, device in enumerate(sd.query_devices()):
        if device['max_input_channels'] > 0:
            print(f"{i}: {device['name']} (Channels: {device['max_input_channels']})")

default_device = sd.default.device[0]
device_info = sd.query_devices(default_device)
CHANNELS = device_info['max_input_channels']
DEVICE_INDEX = default_device
SAMPLE_RATE = config["audio"]["sample_rate"]
AUDIO_FILE = config["audio"]["audio_file"]
COMBINATION = HOTKEY_COMBINATION
MODEL_NAME = config["whisper"]["model"]
DEBOUNCE_TIME_MS = config["hotkey"]["debounce_time_ms"]
DEBOUNCE_TIME = DEBOUNCE_TIME_MS / 1000.0
