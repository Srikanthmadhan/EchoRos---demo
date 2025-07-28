import pyaudio
import numpy as np

def record_audio(duration=5, fs=44100, device_index=None):
    """Record audio using PyAudio."""
    try:
        p = pyaudio.PyAudio()
        
        if device_index is None:
            device_info = p.get_default_input_device_info()
            device_index = device_info['index']
            print(f"No device specified, using default: {device_info['name']}")
        
        stream = p.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=fs,
                        input=True,
                        input_device_index=device_index,
                        frames_per_buffer=1024)

        print(f"Recording {duration}s...")
        frames = []
        for i in range(0, int(fs / 1024 * duration)):
            data = stream.read(1024)
            frames.append(data)

        print("Recording finished!")
        stream.stop_stream()
        stream.close()
        p.terminate()

        audio_data = b''.join(frames)
        audio_array = np.frombuffer(audio_data, dtype=np.int16)
        audio_float = audio_array.astype(np.float32) / 32768.0

        return audio_float, fs

    except Exception as e:
        print(f"Recording failed: {e}")
        raise
