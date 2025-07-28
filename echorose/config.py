import os
from dotenv import load_dotenv
load_dotenv()

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
NEMO_API_URL = "https://ai.api.nvidia.com/v1/vlm/nvidia/neva-22b"
