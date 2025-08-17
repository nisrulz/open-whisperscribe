from pynput import keyboard
import atexit
import logging
import traceback
from src.hotkey_handler import on_press, on_release
from src.audio_recorder import get_stream, reset_stream, set_is_recording
from src.constants import COMBINATION

def cleanup():
    try:
        stream = get_stream()
        if stream:
            print("Cleaning up audio stream...")
            stream.stop()
            stream.close()
            reset_stream()
        set_is_recording(False)
        print("Cleanup complete.")
    except Exception as e:
        logging.error("Cleanup error:\n%s", traceback.format_exc())

atexit.register(cleanup)

def main():
    try:
        print(f"Hold {' + '.join([k.name for k in COMBINATION])} to record, release to transcribe and paste.")
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except Exception as e:
        logging.error("Main loop error:\n%s", traceback.format_exc())
    finally:
        cleanup()

if __name__ == "__main__":
    main()
