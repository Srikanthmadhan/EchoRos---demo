import wave
import numpy as np

def save_audio_to_wav(filename, audio, fs):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(fs)
        wf.writeframes((audio * 32767).astype(np.int16).tobytes())
