import streamlit as st
import time

# --- PAGE CONFIGURATION (Professional & Clean) ---
st.set_page_config(page_title="Sehrish Smart AI", page_icon="🇵🇰", layout="wide")

# --- CUSTOM CSS (Light, Soft & Decent Theme) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #fdfdfd;
    }
    .main {
        color: #333333;
    }
    /* Chat bubbles */
    .stChatMessage {
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 10px;
    }
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #f0f2f6;
    }
    /* Input bar */
    .stChatInputContainer {
        border-radius: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (The 3 lines menu) ---
with st.sidebar:
    st.title("Sehrish Smart AI🤖⚡")
    st.markdown("---")
    st.subheader("Explore Knowledge 🧠")
    st.write("Ap AI se kya seekhna chahte hain?")
    
    # Options in Sidebar
    topic = st.selectbox("Select a Topic:", ["General Chat", "Study Help 📚", "Tech Support 💻", "Creative Writing ✍️"])
    
    st.markdown("---")
    st.subheader("Feedback 📝")
    feedback = st.text_area("Humein batayein aapko ye AI kaisa laga:")
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback! 😊💖")
    
    st.markdown("---")
    st.caption("Designed with ❤️ by Sehrish Malik👻")

# --- INITIALIZING CHAT HISTORY ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- MAIN HEADER (Clean & Minimalist) ---
if not st.session_state.messages:
    st.title("Sehrish Smart AI 🦋✨")
    st.markdown("##### *Your intelligent space for learning and conversation.*")
    st.info("👋 Hello! I am a smart AI designed to help you with studies, chat, and more. How can I assist you today?")

# --- DISPLAY CHAT MESSAGES ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- SMART AI LOGIC (The "Brain") ---
if prompt := st.chat_input("Ask me anything..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI Response Logic
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        user_query = prompt.lower()
        
        # 1. Identity & Creator (The "Cute Girl" part)
        if any(word in user_query for word in ["who made you", "designed you", "creator", "owner"]):
            full_response = "I was designed and created by a very talented and cute girl🥰😘, **Sehrish Malik 🦋**. She is a brilliant mind in AI development! ✨😘"
            
        # 2. Study Help Logic
        elif any(word in user_query for word in ["study", "help me with", "explain", "math", "science", "history"]):
            full_response = f"I would be happy to help you with your studies! 📚 Regarding '{prompt}', I can explain the concepts in detail. What specific part should we focus on first? 🧠📖"
            
        # 3. General Greetings
        elif any(word in user_query for word in ["hello", "hi", "hey"]):
            full_response = "Hello! I'm your Smart AI Assistant. I'm ready to help you with anything you need today. What's on your mind? 😊✨"
            
        # 4. Compliments
        elif "cute" in user_query or "beautiful" in user_query:
            full_response = "Thank you! But all the credit goes to my creator, **Sehrish Malik 🦋**. She's the one who made me look and act so smart! 🥰💖"

        # 5. General Knowledge / Anything else
        else:
            full_response = f"That's a great question about '{prompt}'! 💡 As a smart AI, I'm analyzing this for you. I can help you research this topic or explain its importance. Tell me more! 🚀🧠"

        # Typing Effect
        for word in full_response.split():
            full_response += " "
            response_placeholder.markdown(full_response + "▌")
            time.sleep(0.05)
        response_placeholder.markdown(full_response)
        
    # Save AI response
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# --- MINIMALIST FOOTER ---
st.markdown("---")
st.caption("© 2026 | Sehrish Malik🦋 AI | Smart & Elegant")