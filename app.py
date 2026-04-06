import streamlit as st
import google.generativeai as genai
import time

# --- 1. SETTING UP GOOGLE GEMINI ---
try:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.warning("⚠️ Waiting for API Key... Please make sure it's saved in Streamlit Secrets.")

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="𝐄𝐦𝐨𝐨 𝐀𝐈 - Smart Assistant", page_icon="⚡", layout="wide")

# --- 3. CUSTOM CSS (Navy Blue Waves & Dark Theme) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        background-image: radial-gradient(circle at 2px 2px, #1a365d 1px, transparent 0);
        background-size: 40px 40px;
    }
    .stMarkdown, p, h1, h2, h3, span, label {
        color: #FFFFFF !important;
    }
    .stChatMessage {
        background-color: #1A1C24 !important;
        border-radius: 15px;
        border: 1px solid #2d3748;
    }
    [data-testid="stSidebar"] {
        background-color: #0E1117;
        border-right: 2px solid #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("𝐄𝐌𝐎𝐎 𝐀𝐈 🤖⚡")
    st.write("Designed by 𝐒𝐞𝐡𝐫𝐢𝐬𝐡 𝐌𝐚𝐥𝐢𝐤🦋")
    st.markdown("---")
    
    if st.button("🗑️ Delete Chat History"):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.subheader("Feedback 📝")
    user_feedback = st.text_area("Write your feedback here:")
    
    # Email Feedback Link (Logo ko email nazar nahi ayegi, link pe click kareinge to mail open hoga)
    email_address = "sehrishmalik611@gmail.com"
    subject = "AI App Feedback"
    body = user_feedback
    mail_link = f"mailto:{email_address}?subject={subject}&body={body}"
    
    if st.button("Send Feedback"):
        if user_feedback:
            st.markdown(f'<a href="{mail_link}" target="_blank" style="text-decoration: none; background-color: #ff4b4b; color: white; padding: 10px; border-radius: 5px;">Click here to Confirm & Send Email 📩</a>', unsafe_allow_html=True)
        else:
            st.warning("Please write something first!")

# --- 5. MAIN PAGE ---
st.title("𝐄𝐌𝐎𝐎 𝐀𝐈")
st.write("Welcome to your professional AI companion. Ask me anything!")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 6. CHAT LOGIC ---
if prompt := st.chat_input("How can I help you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        resp_placeholder = st.empty()
        
        # Identity Check
        if any(word in prompt.lower() for word in ["who made you", "designed", "creator"]):
            full_response = "I was created by a very cute and brilliant girl named **Sehrish Malik 🦋**. She is a rising star in AI! ✨😘"
        else:
            try:
                # Actual AI Response
                ai_response = model.generate_content(f"You are Emoo AI, a smart assistant created by Sehrish Malik. Answer this: {prompt}")
                full_response = ai_response.text
            except:
                full_response = "❌ I'm having trouble thinking. Please check if the API Key is saved correctly in Secrets!"

        # Typing Effect
        curr_text = ""
        for word in full_response.split():
            curr_text += word + " "
            resp_placeholder.markdown(curr_text + "▌")
            time.sleep(0.05)
        resp_placeholder.markdown(full_response)
        
    st.session_state.messages.append({"role": "assistant", "content": full_response})

st.markdown("---")
st.caption("© 2026 | Nora AI | Handcrafted by 𝐒𝐞𝐡𝐫𝐢𝐬𝐡 𝐌𝐚𝐥𝐢𝐤 🦋")