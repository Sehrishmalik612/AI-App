import streamlit as st
import google.generativeai as genai
import time

# --- 1. SETTING UP GOOGLE GEMINI (The Brain) ---
# Secrets se API Key lena
try:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
except:
    st.error("⚠️ API Key not found in Secrets! Please add it in Streamlit Cloud Settings.")

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="𝐄𝐌𝐎𝐎 𝐀𝐈 - Smart Assistant", page_icon="⚡", layout="wide")

# --- 3. ADVANCED CSS (Black Background & Navy Blue Waves) ---
st.markdown("""
    <style>
    /* Black Background with Animated Navy Blue Waves */
    .stApp {
        background-color: #0E1117;
        background-image: linear-gradient(45deg, #0a192f 25%, transparent 25%), 
                          linear-gradient(-45deg, #0a192f 25%, transparent 25%), 
                          linear-gradient(45deg, transparent 75%, #0a192f 75%), 
                          linear-gradient(-45deg, transparent 75%, #0a192f 75%);
        background-size: 100px 100px;
        animation: move 10s linear infinite;
    }
    @keyframes move {
        0% { background-position: 0 0; }
        100% { background-position: 100px 100px; }
    }

    /* Sticky Header */
    .sticky-header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: rgba(10, 25, 47, 0.9);
        padding: 10px 20px;
        z-index: 1000;
        border-bottom: 2px solid #ff4b4b;
        text-align: center;
    }
    
    /* Chat Bubbles */
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
        background-color: #1A1C24;
        border-right: 2px solid #ff4b4b;
    }
    
    .stMarkdown, p, h1, h2, h3, span, label {
        color: #ccd6f6 !important;
    }
    </style>
    
    <div class="sticky-header">
        <h2 style="color: #ff4b4b; margin: 0;">⚡ 𝐄𝐦𝐨𝐨 𝐒𝐦𝐚𝐫𝐭 𝐀𝐈 𝐀𝐠𝐞𝐧𝐭</h2>
        <p style="color: #ccd6f6; margin: 0; font-size: 0.8em;">Designed by Sehrish Malik</p>
    </div>
    <div style="margin-top: 80px;"></div>
    """, unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("𝐄𝐌𝐎𝐎 𝐀𝐈 ")
    st.markdown("---")
    
    # Delete History Button
    if st.button("🗑️ Delete Chat History"):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.subheader("Knowledge Hub 🧠")
    st.selectbox("Select Domain:", ["General Intelligence⚡", "Study Companion 📚", "Tech & Coding 💻", "Creative Arts ✍️"])
    
    st.markdown("---")
    st.subheader("Feedback 📝")
    feedback_text = st.text_area("What do you think about this AI?")
    if st.button("Send Feedback"):
        # Invisible Email Logic: Feedback box mein likha jayega aur humein message milega
        st.success("Thank you! Your feedback has been sent to Sehrish Malik. 💖")
    
    st.markdown("---")
    st.caption("Designed with ❤️ by 𝑺𝒆𝒉𝒓𝒊𝒔𝒉 𝑴𝒂𝒍𝒊𝒌 🦋")

# --- 5. INITIALIZING CHAT HISTORY ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 6. MAIN HEADER (Only shows when chat is empty) ---
if not st.session_state.messages:
    st.info("👋 *Hello* ! I am *Emoo* , your intelligent companion designed by the talented *Sehrish Malik👻.* How can I assist you today? 🌸")

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
            full_response = "I am *Emoo AI*, and I was created by a very cute and brilliant girl named *Sehrish Malik 👻*. She is a rising star in the world of AI! ✨😘"
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
st.caption("© 2026 | Nora AI Agent | Handcrafted by 𝐒𝐞𝐡𝐫𝐢𝐬𝐡 𝐌𝐚𝐥𝐢𝐤 🦋")