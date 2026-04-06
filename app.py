import streamlit as st
import google.generativeai as genai
import time

# --- 1. SETTING UP GOOGLE GEMINI ---
# Yahan apni API Key paste karein
GOOGLE_API_KEY = "AIzaSyBlw3vBbEZZTweuy7WQQAa2_s12JVMq5R0"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="𝐄𝐦𝐨𝐨 𝐀𝐈 𝐀𝐠𝐞𝐧𝐭 - Smart Assistant", page_icon="⚡", layout="wide")

# --- 3. ADVANCED CSS (Animated Navy Blue Background) ---
st.markdown("""
    <style>
    /* Animated Background */
    .stApp {
        background: linear-gradient(-45deg, #0a192f, #112240, #1a365d, #0d1b2a);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        color: white;
    }

    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Floating Bubbles Effect */
    .bubbles {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        z-index: -1; overflow: hidden;
    }
    .bubble {
        position: absolute; bottom: -100px;
        width: 40px; height: 40px; background: rgba(100, 255, 218, 0.1);
        border-radius: 50%; opacity: 0.5;
        animation: rise 10s infinite ease-in;
    }
    @keyframes rise {
        0% { bottom: -100px; transform: translateX(0); }
        50% { transform: translateX(100px); }
        100% { bottom: 1080px; transform: translateX(-200px); }
    }

    /* Glassmorphism Chat Bubbles */
    .stChatMessage {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        margin-bottom: 15px;
        color: white !important;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: rgba(10, 25, 47, 0.95);
        border-right: 1px solid rgba(100, 255, 218, 0.3);
    }
    
    .stMarkdown, p, h1, h2, h3, span, label {
        color: #ccd6f6 !important;
    }
    </style>
    
    <div class="bubbles">
        <div class="bubble" style="left: 10%; animation-duration: 8s;"></div>
        <div class="bubble" style="left: 20%; animation-duration: 12s; width: 60px; height: 60px;"></div>
        <div class="bubble" style="left: 35%; animation-duration: 7s;"></div>
        <div class="bubble" style="left: 50%; animation-duration: 15s; width: 80px; height: 80px;"></div>
        <div class="bubble" style="left: 65%; animation-duration: 9s;"></div>
        <div class="bubble" style="left: 80%; animation-duration: 11s; width: 50px; height: 50px;"></div>
    </div>
    """, unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("𝐄𝐦𝐨𝐨 𝐀𝐈 ")
    st.markdown("---")
    st.subheader("Knowledge Hub 🧠")
    st.selectbox("Select Domain:", ["General Intelligence ☺️", "Study Companion 📚", "Tech & Coding 💻", "Creative Arts ✍️"])
    
    st.markdown("---")
    st.subheader("Feedback 📧")
    st.markdown('<a href="mailto:sehrishmalik611@gmail.com" style="color: #64ffda; text-decoration: none; font-weight: bold;">Send Email to Sehrish Malik 📩</a>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.caption("Designed with ❤️ by 𝐒𝐞𝐡𝐫𝐢𝐬𝐡 𝐌𝐚𝐥𝐢𝐤🦋")

# --- 5. INITIALIZING CHAT HISTORY ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 6. MAIN HEADER ---
if not st.session_state.messages:
    st.title("𝐄𝐦𝐨𝐨 𝐀𝐈 𝐀𝐠𝐞𝐧𝐭  ⚡ ")
    st.info("👋 ☺ *Hello* ! I am 𝐄𝐦𝐨𝐨 , your intelligent companion designed by the talented *Sehrish* Malik  🦋.How can I assist you *today* ? 🌸")

# --- 7. DISPLAY CHAT MESSAGES ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 8. AI AGENT LOGIC ---
if prompt := st.chat_input("Ask Emoo anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        user_query = prompt.lower()
        
        if any(word in user_query for word in ["who made you", "designed you", "creator", "owner", "who are you"]):
            full_response = "I am *𝐄𝐦𝐨𝐨 AI*🤖, and I was created by a very cute and brilliant girl named *Sehrish Malik 🦋*. She is a rising star in the world of AI! ✨😘"
        else:
            try:
                personality_prompt = f"You are Emoo AI, a smart and friendly assistant created by Sehrish Malik. Answer this query in a helpful way with emojis: {prompt}"
                response = model.generate_content(personality_prompt)
                full_response = response.text
            except Exception as e:
                full_response = "I'm sorry, I encountered a small error. Please check your API key! 🛑"

        temp_resp = ""
        for word in full_response.split():
            temp_resp += word + " "
            response_placeholder.markdown(temp_resp + "▌")
            time.sleep(0.04)
        response_placeholder.markdown(full_response)
        
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# --- 9. FOOTER ---
st.markdown("---")
st.caption("© 2026 | Emoo AI Agent | Handcrafted by 𝐒𝐞𝐡𝐫𝐢𝐬𝐡 𝐌𝐚𝐥𝐢𝐤 🦋")