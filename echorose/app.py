from .speech.recorder import record_audio
from .speech.transcriber import transcribe
from .chat.chat_model import get_gemini_response
from .tts.speak import speak_response
from .utils.scraper import smart_scrape
from .config import GEMINI_API_KEY
from echorose.utils.command_handler import execute_command, STATE

def main():
    if not GEMINI_API_KEY or GEMINI_API_KEY == "YOUR_GEMINI_API_KEY":
        print("Please set your GEMINI_API_KEY in the .env file.")
        return
    history = []
    while True:
        # Get user input from the terminal
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        # If the user provides text input, use it directly
        if user_input.strip():
            transcript = user_input
        # else:
            # If the user doesn't provide text input, record audio
            # print("\n🎤 Speak something in Tamil/English...")
            # audio, fs = record_audio(duration=6)
            # transcript = transcribe(audio, fs)

        print(f"\n📝 You said: {transcript}")

        response = execute_command(transcript, history)
        if response:
            print(f"🛠️ [EchoRose Command]: {response}")
            if STATE["voice_enabled"]:
                speak_response(response)
            if "Exiting" in response:
                break
            continue  # skip LLM

        # Get the chatbot's response
        reply = get_gemini_response(transcript, history)
    
        print(f"\n🌹 Rosé: {reply}")

        # Update history
        history.append({"role": "user", "parts": [transcript]})
        history.append({"role": "model", "parts": [reply]})

        # Speak the response
        if STATE["voice_enabled"]:
            speak_response(reply)

if __name__ == "__main__":
    main()
