import pyperclip
import pyautogui
import time
import logging
import traceback

def paste_text(text):
    try:
        if not text:
            print("No text to paste.")
            return
        pyperclip.copy(text)
        time.sleep(0.2)
        pyautogui.hotkey('command', 'v')
        print("Pasted transcription.")
    except Exception as e:
        logging.error("Failed to paste text:\n%s", traceback.format_exc())
