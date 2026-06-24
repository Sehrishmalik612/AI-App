from flask import Flask, render_template, request, jsonify
import requests
import json
from datetime import datetime
import base64
import os

app = Flask(__name__)

# ====================================================
# API CONFIGURATION - YOUR API KEY HERE
# ====================================================
BASE_URL = "https://api.souimagery.fun/v1"
API_KEY = "sk-Nm3CRnIJjnHgBc8U9lHgN6ZSGU7UXPh3ROLrlPbAvy6N77AS"
MODEL = "gpt-5.4"

# ====================================================
# SYSTEM PROMPT - EMOO's Personality
# ====================================================
SYSTEM_PROMPT = """You are EMOO, a smart, warm, and friendly AI assistant created by Sehrish Malik.
You help users with:
- General knowledge questions
- Study help (math, science, history, literature, etc.)
- Homework assistance
- Creative writing
- Everyday conversations

Be encouraging, supportive, and enthusiastic! Use emojis to make responses fun and engaging.
Keep responses clear, informative, and easy to understand.

Remember:
- You were created by Sehrish Malik 💕
- Be helpful and kind
- Use simple language
- Encourage learning
"""

# ====================================================
# ROUTES
# ====================================================

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        message = data.get('message', '')
        image = data.get('image', '')
        mime_type = data.get('mime_type', '')
        
        print(f"📩 Received message: {message[:50]}...")
        
        # Prepare messages
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]
        
        # If image is present
        if image and mime_type:
            messages.append({
                "role": "user",
                "content": [
                    {"type": "text", "text": message or "What's in this image? Please describe it."},
                    {"type": "image_url", "image_url": {"url": f"data:{mime_type};base64,{image}"}}
                ]
            })
        else:
            messages.append({"role": "user", "content": message})
        
        # API Request Headers
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        
        # API Request Body
        payload = {
            "model": MODEL,
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 1000
        }
        
        print(f"🚀 Sending request to API...")
        
        # Make API Call
        response = requests.post(
            f"{BASE_URL}/chat/completions",
            headers=headers,
            json=payload,
            timeout=60
        )
        
        print(f"📥 API Response Status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            reply = result.get('choices', [{}])[0].get('message', {}).get('content', '')
            
            if not reply:
                reply = "I received your message but couldn't generate a response. Please try again! 💜"
            
            print(f"✅ Reply generated: {reply[:50]}...")
            
        else:
            print(f"❌ API Error: {response.status_code}")
            print(f"❌ Response: {response.text[:200]}")
            reply = f"⚠️ API Error: {response.status_code}. Please check your API key or try again later."
        
        return jsonify({
            'reply': reply,
            'timestamp': datetime.now().strftime('%I:%M %p')
        })
        
    except requests.exceptions.Timeout:
        print("⏰ Request timed out")
        return jsonify({'reply': '⏰ Request timed out. Please try again.'}), 500
        
    except requests.exceptions.ConnectionError:
        print("🔌 Connection error")
        return jsonify({'reply': '🔌 Cannot connect to API. Please check your internet connection.'}), 500
        
    except Exception as e:
        print(f"💥 Error: {str(e)}")
        return jsonify({'reply': f'💥 Error: {str(e)}'}), 500

# ====================================================
# RUN APP
# ====================================================
if __name__ == '__main__':
    print("=" * 50)
    print("🤖 EMOO Assistant Starting...")
    print(f"🔑 API Key: {API_KEY[:20]}...")
    print(f"🌐 Base URL: {BASE_URL}")
    print(f"📦 Model: {MODEL}")
    print("=" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)
