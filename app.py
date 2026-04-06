import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="𝑺𝒆́𝒉𝒓𝒊𝒔𝒉 𝑨𝑰 𝑨𝒔𝒔𝒊𝒔𝒕𝒂𝒏𝒕", page_icon="👑", layout="wide")

# --- CUSTOM CSS FOR BEAUTY ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stTextInput>div>div>input {
        border-radius: 25px;
        border: 2px solid #ff4b4b;
    }
    .stButton>button {
        border-radius: 20px;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
    }
    .chat-bubble {
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 10px;
    }
    .user-bubble {
        background-color: #e1f5fe;
        text-align: right;
    }
    .ai-bubble {
        background-color: #fff3e0;
        text-align: left;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/000000/female-profile.png")
    st.title("𝑺𝒆𝒉𝒓𝒊𝒔𝒉 Malik 👑")
    st.subheader("AI Developer & Creator")
    st.markdown("---")
    st.write("Welcome! I am Nono's AI Assistant. I can chat, solve problems, and help you with your mood.")
    if st.button("Clear Chat History 🗑️"):
        st.session_state.messages = []
        st.rerun()

# --- CHAT HISTORY INITIALIZATION ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- MAIN HEADER ---
st.title("𝑺𝒆́𝒉𝒓𝒊𝒔𝒉 𝑺𝒎𝒂𝒓𝒕 𝑨𝑰  👻✨")
st.markdown("#### *Your personal space to talk, learn, and explore.*")

# --- STARTING CONVERSATION FOR NEW PERSON ---
if not st.session_state.messages:
    st.info("👋 **Welcome to my world!**..👻I am Nono's AI. Type anything below to start our conversation. I'm ready to answer your questions!")

# --- DISPLAY CHAT HISTORY ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- CHAT INPUT & LOGIC ---
if prompt := st.chat_input("Ask me anything..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI Logic (The "Brain")
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Simple Logic to simulate "Understanding everything"
        user_msg = prompt.lower()
        
        if "hello" in user_msg or "hi" in user_msg:
            full_response = "Hello there! I'm Nono's AI. It's so nice to meet you! How can I make your day better? 😊"
        elif "who are you" in user_msg or "your name" in user_msg:
            full_response = "I am a Smart AI Assistant created by the talented **Nono Malik**. I am here to help you with anything you need! 🚀"
        elif "how are you" in user_msg:
            full_response = "I'm feeling fantastic and ready to help! How about you? How's your day going? ✨"
        elif "what can you do" in user_msg:
            full_response = "I can chat with you, analyze your mood, answer general questions, and even give you advice. Just ask! 🧠"
        elif "nono" in user_msg:
            full_response = "Nono Malik is my creator! She is a brilliant mind and a rising star in the AI world. 👑"
        elif "weather" in user_msg:
            full_response = "I don't have a thermometer, but I hope it's a beautiful day wherever you are! ☀️☁️"
        elif any(word in user_msg for word in ["sad", "bad", "unhappy"]):
            st.balloons()
            full_response = "I'm sorry you're feeling this way. Remember, Nono's AI is here for you. Take a deep breath. Things will get better! 🫂🌈"
        elif any(word in user_msg for word in ["happy", "good", "great"]):
            st.balloons()
            full_response = "That's amazing! Your happiness makes me happy too! Let's celebrate this good vibe! 🎉✨"
        else:
            full_response = f"That's a very interesting point about '{prompt}'! Tell me more about it. I'm always learning from you! 🧠💡"

        # Typing animation effect
        for chunk in full_response.split():
            message_placeholder.markdown(full_response + "▌")
            time.sleep(0.05)
        message_placeholder.markdown(full_response)
        
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# --- FOOTER ---
st.markdown("---")
st.caption("© 2026 | Handcrafted with ❤️ by 𝑺𝒆̂𝒉𝒓𝒊𝒔𝒉 Målik🦋 | Built using Python & Streamlit")