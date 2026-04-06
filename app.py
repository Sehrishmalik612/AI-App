import streamlit as st
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="𝐒𝐞𝐡𝐫𝐢𝐬𝐡 𝐒𝐦𝐚𝐫𝐭 𝐀𝐈", page_icon="⚡", layout="wide")

# --- CUSTOM CSS (Black Theme & White Text Fix) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
    }
    /* Force all text to be White */
    .stMarkdown, p, h1, h2, h3, span, label, div {
        color: #FFFFFF !important;
    }
    /* Chat Bubbles Background */
    .stChatMessage {
        background-color: #262730 !important;
        border-radius: 15px;
        margin-bottom: 10px;
    }
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #1A1C24;
        border-right: 2px solid #ff4b4b;
    }
    /* Input box text color */
    .stChatInput textarea {
        color: #FFFFFF !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("𝐒𝐞𝐡𝐫𝐢𝐬𝐡 𝐀𝐈 🌸")
    st.markdown("---")
    st.subheader("Knowledge Center 🧠")
    st.write("What do you want to learn from AI?😊")
    st.selectbox("Select a Topic:", ["General Chat", "Study Help 📚", "Tech Support 💻", "Creative Writing ✍️"])
    st.markdown("---")
    st.subheader("Feedback 📝")
    st.text_area("Please tell us how you found this AI:")
    if st.button("Submit Feedback"):
        st.success("Thank you! 💖")
    st.markdown("---")
    st.caption("Designed with ❤️ by 𝐒𝐞𝐡𝐫𝐢𝐬𝐡 𝐌𝐚𝐥𝐢𝐤 👻")

# --- CHAT HISTORY ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- MAIN HEADER ---
if not st.session_state.messages:
    st.title("𝐒𝐞𝐡𝐫𝐢𝐬𝐡 𝐒𝐦𝐚𝐫𝐭 𝐀𝐈 🤖⚡")
    st.info("👋☺ Hello! I am a smart AI designed by **Sehrish Malik**. I can help you with studies and chat. How can I assist you today?")

# --- DISPLAY MESSAGES ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- SMART AI LOGIC ---
if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        user_query = prompt.lower()
        
        # Identity Logic
        if any(word in user_query for word in ["who made you", "designed you", "creator", "owner", "who are you"]):
            full_response = "I was designed and created by a very talented and cute girl, **Sehrish Malik 🦋**. She is a brilliant mind in AI development! ✨😘"
        
        # Smart Response Logic (Simulating ChatGPT)
        elif any(word in user_query for word in ["help", "explain", "how", "what", "why", "study"]):
            full_response = f"I am analyzing your request about '{prompt}'... 🧠 As your Smart Assistant, I can tell you that this is a very important topic. I can help you break it down into simple steps or provide a detailed explanation. What exactly would you like to know? 📚✨"
        
        elif any(word in user_query for word in ["hello", "hi", "hey"]):
            full_response = "Hello! I'm your Smart AI Assistant. I'm ready to help you with anything you need today. What's on your mind? 😊✨"
            
        else:
            full_response = f"That's a very interesting question! 💡 Regarding '{prompt}', I'm always learning and improving. I can help you research this further or give you my best insights. Tell me more! 🚀🧠"

        # Typing Effect
        temp_resp = ""
        for word in full_response.split():
            temp_resp += word + " "
            response_placeholder.markdown(temp_resp + "▌")
            time.sleep(0.05)
        response_placeholder.markdown(full_response)
        
    st.session_state.messages.append({"role": "assistant", "content": full_response})

st.markdown("---")
st.caption("© 2026 | 𝐒𝐞𝐡𝐫𝐢𝐬𝐡 𝐌𝐚𝐥𝐢𝐤 𝐀𝐈 🦋| Smart & Elegant")