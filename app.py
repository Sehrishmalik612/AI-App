import streamlit as st
import time

# --- PAGE CONFIG (Professional & Clean) ---
st.set_page_config(page_title="𝑺𝒆𝒉𝒓𝒊𝒔𝒉 𝑺𝒎𝒂𝒓𝒕 𝑨𝑰", page_icon="⚡", layout="wide")

# --- 𝑪𝑼𝑺𝑻𝑶𝑴 𝑪𝑺𝑺 (𝑩𝒍𝒂𝒄𝒌 𝑩𝒂𝒄𝒌𝒈𝒓𝒐𝒖𝒏𝒅 & 𝑾𝒉𝒊𝒕𝒆 𝑻𝒆𝒙𝒕) ---
𝒔𝒕.𝒎𝒂𝒓𝒌𝒅𝒐𝒘𝒏("""
    <𝒔𝒕𝒚𝒍𝒆>
    /* 𝑴𝒂𝒊𝒏 𝑩𝒂𝒄𝒌𝒈𝒓𝒐𝒖𝒏𝒅 𝑩𝒍𝒂𝒄𝒌 */
    .𝒔𝒕𝑨𝒑𝒑 {
        𝒃𝒂𝒄𝒌𝒈𝒓𝒐𝒖𝒏𝒅-𝒄𝒐𝒍𝒐𝒓: #𝟎𝑬𝟏𝟏𝟏𝟕;
        𝒄𝒐𝒍𝒐𝒓: #𝑭𝑭𝑭𝑭𝑭𝑭;
    }
    /* 𝑺𝒊𝒅𝒆𝒃𝒂𝒓 𝑫𝒂𝒓𝒌 */
    [𝒅𝒂𝒕𝒂-𝒕𝒆𝒔𝒕𝒊𝒅="𝒔𝒕𝑺𝒊𝒅𝒆𝒃𝒂𝒓"] {
        𝒃𝒂𝒄𝒌𝒈𝒓𝒐𝒖𝒏𝒅-𝒄𝒐𝒍𝒐𝒓: #𝟏𝑨𝟏𝑪𝟐𝟒;
        𝒃𝒐𝒓𝒅𝒆𝒓-𝒓𝒊𝒈𝒉𝒕: 𝟐𝒑𝒙 𝒔𝒐𝒍𝒊𝒅 #𝒇𝒇𝟒𝒃𝟒𝒃;
    }
    /* 𝑪𝒉𝒂𝒕 𝑩𝒖𝒃𝒃𝒍𝒆𝒔 𝑺𝒕𝒚𝒍𝒊𝒏𝒈 */
    .𝒔𝒕𝑪𝒉𝒂𝒕𝑴𝒆𝒔𝒔𝒂𝒈𝒆 {
        𝒃𝒂𝒄𝒌𝒈𝒓𝒐𝒖𝒏𝒅-𝒄𝒐𝒍𝒐𝒓: #𝟐𝟔𝟐𝟕𝟑𝟎 !𝒊𝒎𝒑𝒐𝒓𝒕𝒂𝒏𝒕;
        𝒃𝒐𝒓𝒅𝒆𝒓-𝒓𝒂𝒅𝒊𝒖𝒔: 𝟏𝟓𝒑𝒙;
        𝒄𝒐𝒍𝒐𝒓: #𝑭𝑭𝑭𝑭𝑭𝑭 !𝒊𝒎𝒑𝒐𝒓𝒕𝒂𝒏𝒕;
        𝒎𝒂𝒓𝒈𝒊𝒏-𝒃𝒐𝒕𝒕𝒐𝒎: 𝟏𝟎𝒑𝒙;
        𝒃𝒐𝒓𝒅𝒆𝒓: 𝟏𝒑𝒙 𝒔𝒐𝒍𝒊𝒅 #𝟑𝟑𝟑;
    }
    /* 𝑰𝒏𝒑𝒖𝒕 𝑩𝒂𝒓 */
    .𝒔𝒕𝑪𝒉𝒂𝒕𝑰𝒏𝒑𝒖𝒕𝑪𝒐𝒏𝒕𝒂𝒊𝒏𝒆𝒓 {
        𝒃𝒂𝒄𝒌𝒈𝒓𝒐𝒖𝒏𝒅-𝒄𝒐𝒍𝒐𝒓: #𝟏𝑨𝟏𝑪𝟐𝟒 !𝒊𝒎𝒑𝒐𝒓𝒕𝒂𝒏𝒕;
    }
    /* 𝑯𝒆𝒂𝒅𝒆𝒓𝒔 & 𝑻𝒆𝒙𝒕 */
    𝒉𝟏, 𝒉𝟐, 𝒉𝟑, 𝒑, 𝒔𝒑𝒂𝒏, 𝒍𝒂𝒃𝒆𝒍 {
        𝒄𝒐𝒍𝒐𝒓: #𝑭𝑭𝑭𝑭𝑭𝑭 !𝒊𝒎𝒑𝒐𝒓𝒕𝒂𝒏𝒕;
    }
    /* 𝑺𝒖𝒄𝒄𝒆𝒔𝒔/𝑰𝒏𝒇𝒐 𝑩𝒐𝒙𝒆𝒔 */
    .𝒔𝒕𝑨𝒍𝒆𝒓𝒕 {
        𝒃𝒂𝒄𝒌𝒈𝒓𝒐𝒖𝒏𝒅-𝒄𝒐𝒍𝒐𝒓: #𝟐𝟔𝟐𝟕𝟑𝟎 !𝒊𝒎𝒑𝒐𝒓𝒕𝒂𝒏𝒕;
        𝒄𝒐𝒍𝒐𝒓: #𝑭𝑭𝑭𝑭𝑭𝑭 !𝒊𝒎𝒑𝒐𝒓𝒕𝒂𝒏𝒕;
        𝒃𝒐𝒓𝒅𝒆𝒓: 𝟏𝒑𝒙 𝒔𝒐𝒍𝒊𝒅 #𝒇𝒇𝟒𝒃𝟒𝒃;
    }
    </𝒔𝒕𝒚𝒍𝒆>
    """, 𝒖𝒏𝒔𝒂𝒇𝒆_𝒂𝒍𝒍𝒐𝒘_𝒉𝒕𝒎𝒍=𝑻𝒓𝒖𝒆)
    
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