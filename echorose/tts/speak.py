import pyttsx3

engine = pyttsx3.init()

# Get a list of available voices
voices = engine.getProperty('voices')

# Find a female voice
female_voice = None
for voice in voices:
    if 'female' in voice.name.lower() or 'woman' in voice.name.lower():
        female_voice = voice.id
        break

# Set the female voice if found
if female_voice:
    engine.setProperty('voice', female_voice)

def speak_response(text):
    engine.say(text)
    engine.runAndWait()
