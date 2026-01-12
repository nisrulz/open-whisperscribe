import sounddevice as sd
import numpy as np
import scipy.io.wavfile
from src.logger import logger
from src.constants import SAMPLE_RATE, CHANNELS, DEVICE_INDEX, AUDIO_FILE

recorded_frames = []

stream = None
is_recording = False

def get_stream():
    global stream
    return stream

def reset_stream():
    global stream
    stream = None

def set_is_recording(value):
    global is_recording
    is_recording = value

def start_recording():
    global is_recording, stream, recorded_frames
    try:
        if is_recording:
            logger.warning("Recording already in progress.")
            return
        is_recording = True
        recorded_frames = []

        def callback(indata, frames, time_info, status):
            if status:
                logger.warning(f"Recording status: {status}")
            try:
                if indata.shape[1] > 1:
                    mono_data = indata.mean(axis=1, keepdims=True).astype(indata.dtype)
                    recorded_frames.append(mono_data.copy())
                else:
                    recorded_frames.append(indata.copy())
            except Exception as e:
                logger.error("Error in audio callback.")
                logger.error(str(e))

        stream = sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype='int16',
            device=DEVICE_INDEX,
            callback=callback
        )
        stream.start()
        logger.info("Recording... (Hold hotkey)")
    except Exception as e:
        logger.error("Failed to start recording.")
        logger.error(str(e))
        is_recording = False

def stop_recording_and_save():
    global is_recording, stream, recorded_frames
    try:
        if not is_recording:
            logger.warning("No active recording to stop.")
            return
        is_recording = False
        if stream:
            stream.stop()
            stream.close()
            stream = None
        if recorded_frames:
            audio_np = np.concatenate(recorded_frames, axis=0)
            scipy.io.wavfile.write(AUDIO_FILE, SAMPLE_RATE, audio_np)
            logger.success("Stopped recording. Audio saved.")
        else:
            logger.warning("No audio captured.")
    except Exception as e:
        logger.error("Failed to stop recording and save.")
        logger.error(str(e))
        
        
def get_is_recording():
    return is_recording
