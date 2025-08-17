import whisper
from src.constants import MODEL_NAME, AUDIO_FILE
import warnings

# Suppress Whisper Warnings
warnings.filterwarnings("ignore", category=UserWarning, module="whisper")

model = whisper.load_model(MODEL_NAME)

def transcribe_with_whisper():
    print("Transcribing with Whisper...")
    try:
        result = model.transcribe(AUDIO_FILE)
        text = result.get("text", "").strip()
        if not text:
            print("Warning: transcription text is empty.")
        else:
            print(f"Transcription complete: {text}")
        return text
    except Exception as e:
        print("Transcription error.")
        return ""
