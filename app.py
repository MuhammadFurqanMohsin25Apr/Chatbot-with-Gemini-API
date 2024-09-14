from flask import Flask, render_template, request
import os
import google.generativeai as genai

app = Flask(__name__)


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}


model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config
)


chat_session = model.start_chat(history=[])

@app.route('/')
def index():
    return render_template('chat.html')


@app.route("/get", methods=['POST'])
def chat():
    msg = request.form.get('msg')
    if msg:
        return get_chat_response(msg)
    return "No message received!"


def get_chat_response(text):
   
    response = chat_session.send_message(text)
    return response.text


if __name__ == '__main__':
    app.run(debug=True)
