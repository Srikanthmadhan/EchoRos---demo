# echorose/utils/command_handler.py

import os
import json
import tkinter as tk
from tkinter import filedialog
import tempfile
import shutil
from echorose.tts.speak import speak_response
from echorose.utils.scraper import auto_scrape

CACHE_DIR = tempfile.mkdtemp(prefix="echorose_upload_")

STATE = {
    "voice_enabled": True,
    "user_profile": {
        "name": "User",
        "preferences": {}
    }
}

USER_PROFILE_PATH = os.path.join(os.path.dirname(__file__), "user_profile.json")

# Load saved user preferences
def load_user_profile():
    if os.path.exists(USER_PROFILE_PATH):
        with open(USER_PROFILE_PATH, "r") as f:
            STATE["user_profile"] = json.load(f)

# Save preferences to file
def save_user_profile():
    with open(USER_PROFILE_PATH, "w") as f:
        json.dump(STATE["user_profile"], f, indent=2)

# List of available commands
COMMANDS = {
    "voice turn on": "Enable speech feedback (TTS)",
    "voice turn off": "Disable speech feedback",
    "upload files": "Open directory dialog to select folder for upload",
    "upload": "Upload files from cache",
    "scrape [URL]": "Scrape a webpage and extract main content",
    "clear memory": "Clear chat history/context",
    "live": "Enable live transcription/chat mode",
    "exit / quit": "Exit EchoRose",
    "set name to [your_name]": "Set user name",
    "set preference [key] to [value]": "Set a custom user preference",
    "list commands": "Show this list of available commands"
}

def execute_command(command: str, history: list):
    command = command.lower().strip()
    load_user_profile()

    if "voice" in command and "on" in command:
        STATE["voice_enabled"] = True
        return "Speech feedback turned ON."

    elif "voice" in command and "off" in command:
        STATE["voice_enabled"] = False
        return "Speech feedback turned OFF."

    elif command == "upload files":
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        folder_path = filedialog.askdirectory(title="Select directory to upload")
        if folder_path:
            # Copy all files from the selected directory to cache
            files_copied = 0
            for item in os.listdir(folder_path):
                src = os.path.join(folder_path, item)
                if os.path.isfile(src):
                    shutil.copy(src, CACHE_DIR)
                    files_copied += 1
            return f"Selected directory {folder_path}. {files_copied} files copied to cache. Say 'upload' to proceed."
        else:
            return "No directory selected."

    elif command == "upload":
        files = os.listdir(CACHE_DIR)
        if files:
            # Here, implement the actual upload. For now, just a placeholder.
            return f"Uploading {len(files)} files: {', '.join(files)}."
            # After upload, clear the cache
            shutil.rmtree(CACHE_DIR)
            CACHE_DIR = tempfile.mkdtemp(prefix="echorose_upload_")
        else:
            return "No files in cache to upload."

    elif command.startswith("scrape "):
        url = command.split("scrape ", 1)[1].strip()
        content = auto_scrape(url)
        return "\n".join(content)

    elif command == "clear memory":
        history.clear()
        return "Memory cleared."

    elif command == "exit" or command == "quit":
        return "Exiting EchoRose."

    elif command == "live":
        return "[Live mode enabled] Say 'stop' to exit."

    elif command.startswith("set name to "):
        name = command.split("set name to ", 1)[1].strip().capitalize()
        STATE["user_profile"]["name"] = name
        save_user_profile()
        return f"Got it! I'll call you {name} from now on."

    elif command.startswith("set preference "):
        try:
            _, key_val = command.split("set preference ", 1)
            key, value = key_val.split(" to ")
            STATE["user_profile"]["preferences"][key.strip()] = value.strip()
            save_user_profile()
            return f"Preference '{key.strip()}' set to '{value.strip()}'."
        except ValueError:
            return "Invalid format. Use: set preference [key] to [value]"

    elif command == "list commands":
        cmd_list = "\n".join([f"- {cmd}: {desc}" for cmd, desc in COMMANDS.items()])
        return f"📜 Available EchoRose Commands:\n{cmd_list}"

    return None  # Not a command
