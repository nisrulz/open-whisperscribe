from pynput import keyboard
import threading
from src.constants import COMBINATION, DEBOUNCE_TIME
from src.audio_recorder import start_recording, stop_recording_and_save, get_is_recording
from src.transcriber import transcribe_with_whisper
from src.paster import paste_text

transcription_triggered = False
current_keys = set()

def on_press(key):
    try:
        current_keys.add(key)
        if all(k in current_keys for k in COMBINATION):
            if not get_is_recording():
                start_recording()
    except Exception as e:
        print("Error in on_press.")

def on_release(key):
    global transcription_triggered
    try:
        current_keys.discard(key)
        if not all(k in current_keys for k in COMBINATION):
            if get_is_recording() and not transcription_triggered:
                transcription_triggered = True
                stop_recording_and_save()
                text = transcribe_with_whisper()
                if text:
                    paste_text(text)
                # Reset the flag after a short delay
                def reset_flag():
                    global transcription_triggered
                    transcription_triggered = False
                threading.Timer(DEBOUNCE_TIME, reset_flag).start()
    except Exception as e:
        print("Error in on_release.")

