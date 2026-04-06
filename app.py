import streamlit as st
import time

# --- PAGE CONFIG (Professional & Clean) ---
st.set_page_config(page_title="𝑺𝒆𝒉𝒓𝒊𝒔𝒉 𝑺𝒎𝒂𝒓𝒕 𝑨𝑰", page_icon="⚡", layout="wide")

# --- CUSTOM CSS (Colorful & Readable) ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background: linear-gradient(to right, #f8f9fa, #e9ecef);
    }
    /* Text Color */
    .main .block-container {
        color: #1a1a1a;
    }
    /* Chat Bubbles */
    .stChatMessage {
        background-color: #ffffff !important;
        border: 1px solid #ddd;
        border-radius: 15px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
        color: #333 !important;
    }
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 2px solid #ff4b4b;
    }
    /* Header Title */
    h1 {
        color: #ff4b4b !important;
        font-family: 'Trebuchet MS', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (The 3 lines menu) ---
with st.sidebar:
    st.title("𝑺𝒆𝒉𝒓𝒊𝒔𝒉 𝑺𝒎𝒂𝒓𝒕 𝑨𝑰 🤖🔥")
    st.markdown("---")
    st.subheader("Knowledge Center 🧠")
    st.write("𝘞𝘩𝘢𝘵 𝘥𝘰 𝘺𝘰𝘶 𝘸𝘢𝘯𝘵 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘧𝘳𝘰𝘮 𝘈𝘐?😊")
    
    st.selectbox("Select a Topic:", ["General Chat☺", "Study Help 📚", "Tech Support 💻", "Creative Writing ✍️"])
    
    st.markdown("---")
    st.subheader("Feedback 📝")
    st.text_area("Pleas𝘦 𝘵𝘦𝘭𝘭 𝘶𝘴 𝘩𝘰𝘸  𝘺𝘰𝘶 𝘧𝘰𝘶𝘯𝘥 𝘵𝘩𝘪𝘴 𝘈𝘐:")
    if st.button("Submit Feedback"):
        st.success("Thank you! 💖")
    
    st.markdown("---")
    st.caption("Designed with ❤️ by 𝑺𝒆𝒉𝒓𝒊𝒔𝒉 𝑴𝒂𝒍𝒊𝒌👻")

# --- INITIALIZING CHAT HISTORY ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- MAIN HEADER ---
if not st.session_state.messages:
    st.title("𝑺𝒆𝒉𝒓𝒊𝒔𝒉 𝑺𝒎𝒂𝒓𝒕 𝑨𝑰🤖⚡")
    st.info("👋☺️ Hello! I am a smart AI designed to help you with studies and chat. How can I assist you today?")

# --- DISPLAY CHAT MESSAGES ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(f'<div style="color: #333;">{message["content"]}</div>', unsafe_allow_html=True)

# --- SMART AI LOGIC ---
if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        user_query = prompt.lower()
        
        # 1. Identity & Creator (The "Cute Girl" part)
        if any(word in user_query for word in ["who made you", "designed you", "creator", "owner", "who are you"]):
            full_response = "I was designed and created by a very talented and cute girl, **Sehrish Malik 🦋**. She is a brilliant mind in AI development! ✨😘"
            
        # 2. Study Help Logic
        elif any(word in user_query for word in ["study", "help", "explain", "math", "science", "history"]):
            full_response = f"I would be happy to help you with your studies! 📚 Regarding '{prompt}', I can explain the concepts in detail. What should we focus on? 🧠📖"
            
        # 3. General Greetings
        elif any(word in user_query for word in ["hello", "hi", "hey"]):
            full_response = "Hello! I'm your Smart AI Assistant. I'm ready to help you with anything you need today. What's on your mind? 😊✨"
            
        # 4. General Knowledge / Anything else
        else:
            full_response = f"That's a great question about '{prompt}'! 💡 I'm analyzing this for you. I can help you research this topic or explain its importance. Tell me more! 🚀🧠"

        # Typing Effect
        temp_resp = ""
        for word in full_response.split():
            temp_resp += word + " "
            response_placeholder.markdown(f'<div style="color: #333;">{temp_resp}▌</div>', unsafe_allow_html=True)
            time.sleep(0.05)
        response_placeholder.markdown(f'<div style="color: #333;">{full_response}</div>', unsafe_allow_html=True)
        
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# --- FOOTER ---
st.markdown("---")
st.caption("© 2026 | 𝐒𝐞𝐡𝐫𝐢𝐬𝐡 𝐌𝐚𝐥𝐢𝐊 𝐀𝐈🦋 | Smart & Elegant")