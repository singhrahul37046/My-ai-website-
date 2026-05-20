import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app) # Taaki website bina kisi block ke chale

# --- GOOGLE GEMINI KEY ---
GEMINI_KEY = "AIzaSyA5V-kWwYOBUt2QtqVnQA8waGjIm5I5xfY"
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

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
        return jsonify({'reply': response.text})
    except Exception as e:
        return jsonify({'reply': f"Galti: {str(e)}"})

# Vercel ke liye server setup
def handler(request):
    return app(request)
