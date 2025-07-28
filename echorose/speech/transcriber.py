import os
import whisper
from ..utils.audio_utils import save_audio_to_wav
import tempfile
import shutil

# Enhanced model loader with cache clearing on corruption

def load_model_safely(model_name="medium"):
    cache_dir = os.path.join(os.path.expanduser("~"), ".cache", "whisper")
    try:
        print(f"Loading Whisper model: {model_name}...")
        model = whisper.load_model(model_name)
        print("Model loaded successfully!")
        return model
    except RuntimeError as e:
        if "SHA256 checksum" in str(e):
            print("Corrupted model detected. Clearing cache and retrying...")
            if os.path.exists(cache_dir):
                shutil.rmtree(cache_dir)
                print(f"Cache cleared: {cache_dir}")
            print("Downloading model again...")
            model = whisper.load_model(model_name)
            return model
        else:
            raise e
    except Exception as e:
        print(f"Error loading model: {e}")
        raise

# Load model with error handling
# model = load_model_safely("medium")

def transcribe(audio, fs):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
        save_audio_to_wav(tmpfile.name, audio, fs)
        result = model.transcribe(tmpfile.name, language=None)  # auto language detection
        return result["text"]
