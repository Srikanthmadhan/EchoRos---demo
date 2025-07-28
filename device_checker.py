import sounddevice as sd
import pyaudio

def check_sound_devices():
    """Lists available audio devices and their properties."""
    print("--- Checking with sounddevice ---")
    try:
        devices = sd.query_devices()
        print(devices)
        for i, device in enumerate(devices):
            if device['max_input_channels'] > 0:
                print(f"\nInput Device ID {i}: {device['name']}")
                print(f"  Default sample rate: {device['default_samplerate']}")
    except Exception as e:
        print(f"Could not query devices with sounddevice: {e}")

    print("\n--- Checking with PyAudio ---")
    p = pyaudio.PyAudio()
    try:
        info = p.get_host_api_info_by_index(0)
        numdevices = info.get('deviceCount')
        for i in range(0, numdevices):
            if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))
    except Exception as e:
        print(f"Could not query devices with PyAudio: {e}")
    finally:
        p.terminate()

if __name__ == "__main__":
    check_sound_devices()
