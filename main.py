import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# 🔥 EKDUM FRESH TESTED KEY 🔥
GEMINI_KEY = "AIzaSyAs-7r_S5m1M7D8eP9tW0x_K3vB4nG2mQ"
genai.configure(api_key=GEMINI_KEY)

# 🚀 Naya fast model name
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/ask', methods=['POST'])
def ask_ai():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'reply': 'Bhai, kuch likho toh sahi!'})
    try:
        response = model.generate_content(user_message)
        if response.text:
            return jsonify({'reply': response.text})
        else:
            return jsonify({'reply': 'Google AI ne khali jawab diya, fir se try karo bhai.'})
    except Exception as e:
        return jsonify({'reply': f"Galti: {str(e)}"})

def handler(request):
    return app(request)
