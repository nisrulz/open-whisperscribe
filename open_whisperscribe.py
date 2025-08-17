import sounddevice as sd
import numpy as np
import scipy.io.wavfile
import whisper
import time
import pyperclip
import pyautogui
from pynput import keyboard
import threading
import atexit

SAMPLE_RATE = 16000
CHANNELS = 2
DEVICE_INDEX = 2  # Adjust for your microphone device index
AUDIO_FILE = "output.wav"

# Hotkey combination example: Alt + Shift_Left
COMBINATION = {keyboard.Key.alt, keyboard.Key.shift_l}
current_keys = set()

is_recording = False
recorded_frames = []
stream = None

# Load model once globally for efficiency
model = whisper.load_model("base")

def start_recording():
    global is_recording, stream, recorded_frames
    if is_recording:
        print("Recording already in progress.")
        return
    is_recording = True
    recorded_frames = []

    def callback(indata, frames, time, status):
        if status:
            print(f"Recording status: {status}")
        # If stereo, convert to mono by averaging channels
        if indata.shape[1] > 1:
            mono_data = indata.mean(axis=1, keepdims=True).astype(indata.dtype)
            recorded_frames.append(mono_data.copy())
        else:
            recorded_frames.append(indata.copy())


    stream = sd.InputStream(samplerate=SAMPLE_RATE,
                           channels=CHANNELS,
                           dtype='int16',
                           device=DEVICE_INDEX,
                           callback=callback)
    stream.start()
    print("Recording... (Hold hotkey)")

def stop_recording_and_save():
    global is_recording, stream, recorded_frames
    if not is_recording:
        print("No active recording to stop.")
        return
    is_recording = False
    if stream is not None:
        stream.stop()
        stream.close()
        stream = None
    if recorded_frames:
        audio_np = np.concatenate(recorded_frames, axis=0)
        scipy.io.wavfile.write(AUDIO_FILE, SAMPLE_RATE, audio_np)
        print("Stopped recording. Audio saved.")
    else:
        print("No audio captured.")

def transcribe_with_whisper():
    print("Transcribing with Whisper Python package...")
    try:
        result = model.transcribe(AUDIO_FILE)
    except Exception as e:
        print("Error during transcription:", e)
        return ""

    text = result.get("text", "").strip()
    if not text:
        print("Warning: transcription text is empty.")
    else:
        print(f"Transcription complete: {text}")
    return text

def paste_text(text):
    if not text:
        print("No text to paste.")
        return
    pyperclip.copy(text)
    time.sleep(0.2)
    pyautogui.hotkey('command', 'v')
    print("Pasted transcription.")

def on_press(key):
    current_keys.add(key)
    if all(k in current_keys for k in COMBINATION):
        if not is_recording:
            start_recording()

def on_release(key):
    try:
        current_keys.remove(key)
    except KeyError:
        pass
    if not all(k in current_keys for k in COMBINATION):
        if is_recording:
            stop_recording_and_save()
            text = transcribe_with_whisper()
            if text:
                paste_text(text)

def cleanup():
    global stream, is_recording
    if stream is not None:
        print("Cleaning up audio stream...")
        try:
            stream.stop()
            stream.close()
        except Exception as e:
            print("Error during cleanup:", e)
        stream = None
    is_recording = False
    print("Cleanup complete.")

atexit.register(cleanup)

def main():
    print(f"Hold {' + '.join([k.name for k in COMBINATION])} to record, release to transcribe and paste.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    cleanup()

if __name__ == "__main__":
    main()
