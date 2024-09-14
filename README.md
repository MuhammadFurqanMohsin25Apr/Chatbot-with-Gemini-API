# Chatbot with Gemini API

This project is a simple chatbot web application built with Flask and integrated with Google Gemini API for generating chatbot responses. The chatbot can have interactive conversations with users, where user messages are sent to the Gemini API for response generation.


https://github.com/user-attachments/assets/0d75adc3-b167-411a-afd2-677d497446aa


## Features

- **Flask Web Framework**: The chatbot runs on a Flask server.
- **Gemini API Integration**: Responses are generated using the Google Gemini API (Generative AI).
- **Interactive Chat Interface**: The UI allows users to type messages and receive responses from the chatbot.
- **Real-time Conversations**: Chat interface provides a smooth, real-time conversation experience.
  
## Prerequisites

- Python 3.x
- Flask
- Google Gemini API key

**Start chatting** with the chatbot!

## Usage

- Once the app is running, you can type your message in the chat input and press the send button.
- The chatbot will respond using the Gemini API in real time.

## Files Description

### `app.py`
The main Flask application. It includes:
- Chatbot integration with the Gemini API.
- Routes for rendering the chat interface and handling user inputs.

### `chat.html`
This file is responsible for the chat interface and user interaction. It's styled using Bootstrap and custom CSS from the `style.css` file.

### `style.css`
The custom CSS file used to style the chat interface, ensuring a clean and modern look.

## Dependencies

- Flask
- Google Generative AI SDK (`google-generativeai`)
- Bootstrap (for styling)


### Notes:
1. Replace `"your-api-key-here"` with your actual Gemini API key.
2. Adjust any file paths if necessary, based on your directory structure.



