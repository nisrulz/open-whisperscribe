import pyperclip
import pyautogui
import time
from src.logger import logger

def paste_text(text):
    try:
        if not text:
            logger.warning("No text to paste.")
            return
        pyperclip.copy(text)
        time.sleep(0.2)
        pyautogui.hotkey('command', 'v')
        logger.success("Pasted transcription.")
    except Exception as e:
        logger.error("Failed to paste text.")
        logger.error(str(e))
