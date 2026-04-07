import streamlit as st
import google.generativeai as genai
import time

# --- 1. DIRECT API KEY (No more Secrets needed!) ---
# Aapki Key: AIzaSyAFRm0bN8ZqL8jtPXp8egSDQuWY098umCA
try:
    GOOGLE_API_KEY = "AIzaSyAFRm0bN8ZqL8jtPXp8egSDQuWY098umCA"
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error(f"Error connecting to AI: {e}")

# --- 2. PAGE CONFIG (Professional & Decent) ---
st.set_page_config(page_title="Nora AI - Smart Assistant", page_icon="🦋", layout="wide")

# --- 3. CUSTOM CSS (Dark Navy Theme & White Text) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        background-image: linear-gradient(45deg, #0a192f 25%, transparent 25%, transparent 50%, #0a192f 50%, #0a192f 75%, transparent 75%, transparent);
        background-size: 100px 100px;
        animation: move 4s linear infinite;
    }
    @keyframes move {
        from { background-position: 0 0; }
        to { background-position: 100px 100px; }
    }
    .stMarkdown, p, h1, h2, h3, span, label, div {
        color: #FFFFFF !important;
    }
    .stChatMessage {
        background-color: #262730 !important;
        border-radius: 15px;
        margin-bottom: 10px;
        border: 1px solid #333;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("🦋 Nora AI Menu")
    st.markdown("---")
    if st.button("🗑️ Delete Chat History"):
        st.session_state.messages = []
        st.rerun()
    
    st.subheader("📬 Feedback")
    user_feedback = st.text_area("Hamein batayein aapko Nora AI kaisa laga:", placeholder="Write your feedback here...")
    if st.button("Send Feedback"):
        if user_feedback:
            # Ye link user ka email app khol dega aur feedback aapko bhej dega
            st.markdown(f'<a href="mailto:nonomalik612@gmail.com?subject=Nora AI Feedback&body={user_feedback}" target="_blank" style="text-decoration:none; color:white; background-color:#ff4b4b; padding:10px; border-radius:10px;">Click here to confirm & Send Email 📩</a>', unsafe_allow_html=True)
            st.success("Feedback box ready! Click the button above to send.")

# --- 5. MAIN PAGE ---
st.title("Nora AI Smart Assistant 🦋✨")
st.write("Welcome to your personal space to talk, learn, and explore.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        resp_placeholder = st.empty()
        user_query = prompt.lower()
        
        # 1. Identity Check
        if any(word in user_query for word in ["who are you", "designed", "creator", "made you"]):
            full_response = "I am **Nora AI**, and I was created by a very cute and brilliant girl named **Sehrish Malik 🦋**. She is a rising star in the world of AI! ✨🥰"
        else:
            try:
                # Real AI Response from Gemini
                ai_response = model.generate_content(f"You are Nora AI, a smart assistant created by Sehrish Malik. Answer this query clearly with emojis: {prompt}")
                full_response = ai_response.text
            except Exception as e:
                full_response = f"❌ AI Error: {e}. Please make sure your internet is working and API Key is correct!"

        # Typing Effect
        curr_text = ""
        for word in full_response.split():
            curr_text += word + " "
            resp_placeholder.markdown(curr_text + "▌")
            time.sleep(0.05)
        resp_placeholder.markdown(full_response)
        
    st.session_state.messages.append({"role": "assistant", "content": full_response})

st.markdown("---")
st.caption("© 2026 | Nora AI | Handcrafted by Sehrish Malik 🦋")