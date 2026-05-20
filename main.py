import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# 🔥 EKDUM FRESH NEW GEMINI KEY 🔥
GEMINI_KEY = "AIzaSyD_V7mN_Wp3X8zLq9K5vRt_B4nJ2mQ6" 
genai.configure(api_key=GEMINI_KEY)

# 🚀 Ekdum stable universal model name
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
        # Simple content generation
        response = model.generate_content(user_message)
        if response.text:
            return jsonify({'reply': response.text})
        else:
            return jsonify({'reply': 'Google AI ne khali jawab diya, fir se try karo bhai.'})
    except Exception as e:
        return jsonify({'reply': f"Galti: {str(e)}"})

def handler(request):
    return app(request)
