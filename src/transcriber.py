from faster_whisper import WhisperModel
from src.constants import MODEL_NAME, AUDIO_FILE
import warnings

# Suppress Whisper Warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Initialize faster-whisper model (uses CPU by default, can be set to "cuda" for GPU)
model = WhisperModel(MODEL_NAME, device="cpu", compute_type="int8")

def transcribe_with_whisper():
    print("Transcribing with Whisper...")
    try:
        segments, info = model.transcribe(AUDIO_FILE, beam_size=5)
        text = " ".join([segment.text for segment in segments]).strip()
        if not text:
            print("Warning: transcription text is empty.")
        else:
            print(f"Transcription complete: {text}")
        return text
    except Exception as e:
        print("Transcription error.")
        print(str(e))
        return ""
