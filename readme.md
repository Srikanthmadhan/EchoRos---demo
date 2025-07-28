# EchoRosé AI Assistant

EchoRosé is a versatile AI assistant that can handle voice commands, file uploads, web scraping, and more. It features:

- Voice feedback (TTS) that can be toggled on/off
- File upload functionality with directory selection
- Web scraping capabilities
- Live transcription mode
- Customizable user preferences

## Features

- **Voice Commands**: Control TTS, upload files, scrape websites, etc.
- **File Management**: Upload files from a directory and manage cache
- **Web Scraper**: Extract main content from webpages
- **Live Mode**: Continuous transcription and chat
- **User Preferences**: Set name and custom preferences

## Getting Started

1. Clone the repository:
   ```
   git clone https://github.com/Srikanthmadhan/EchoRos---demo.git
   cd EchoRos---demo
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables in `.env` (e.g., API keys).

5. Run the application:
   ```
   python echorose/__main__.py
   ```

## Usage

Use voice commands like:
- "voice turn on" to enable TTS
- "upload files" to select a directory for upload
- "scrape [URL]" to scrape a webpage
- "list commands" to see all available commands

## Configuration

- `.env` file for API keys and configuration
- `config.py` for additional settings
