import shutil
import os

home = os.path.expanduser("~")
target_path = os.path.join(home, ".cache", "whisper", "medium.pt")

# Only run this once
shutil.copy("D:/RoseVerse AI/Echo Rosé/medium.pt", target_path)
