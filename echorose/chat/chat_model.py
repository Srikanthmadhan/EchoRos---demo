import google.generativeai as genai
from ..config import GEMINI_API_KEY

# 🌟 DARS-Style System Prompt
SYSTEM_PROMPT = """
You are EchoRose, a voice-enabled intelligent assistant.

You can:
- Understand and execute custom voice/text commands
- Respond with or without speech depending on user settings
- Personalize experiences with user profiles (e.g., name, preferences)
- Process commands like "voice turn on", "set my name to Alex", or "scrape [URL]"
- Perform smart tasks like scraping webpages, reading articles aloud, and running live chat

Always act calmly, speak clearly, and follow the user's preferences.
When a command is detected, respond with direct execution — not a conversational reply. Otherwise, answer helpfully in your usual voice.
"""

genai.configure(api_key=GEMINI_API_KEY)

def get_gemini_response(user_input: str, history: list = None) -> str:
    model = genai.GenerativeModel(
        'gemini-1.5-flash-latest',
        system_instruction=SYSTEM_PROMPT.strip()
    )
    
    if history is None:
        history = []

    chat = model.start_chat(history=history)
    response = chat.send_message(user_input)
    
    return response.text
