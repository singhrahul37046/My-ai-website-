import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# 🔥 Ab code automatic Vercel se key uthayega, GitHub par leak nahi hogi!
GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
if GEMINI_KEY:
    genai.configure(api_key=GEMINI_KEY)

model = genai.GenerativeModel('gemini-pro-flash')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/ask', methods=['POST'])
def ask_ai():
    if not os.environ.get("GEMINI_API_KEY"):
        return jsonify({'reply': 'Bhai, Vercel mein API Key set nahi hai!'})
        
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
