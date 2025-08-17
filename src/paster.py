import pyperclip
import pyautogui
import time

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
        print("Failed to paste text.")
