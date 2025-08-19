import sounddevice as sd

def is_mic_permission_granted():
    """
    Checks if the microphone permission is granted by attempting to open an audio stream.
    Returns True if permission is granted, False otherwise.
    """
    try:
        with sd.InputStream():
            return True
    except Exception as e:
        print(f"Microphone permission not granted: {e}")
        return False

def trigger_mic_permission(duration=1, sample_rate=44100, channels=1):
    """
    Triggers macOS microphone permission prompt by recording a short audio snippet.
    """
    try:
        print("Accessing microphone...")
        sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
        sd.wait()
        print("Microphone access triggered.")
    except Exception as e:
        print(f"Error accessing microphone: {e}")

def main():
    if not is_mic_permission_granted():
        trigger_mic_permission()

if __name__ == "__main__":
    main()
