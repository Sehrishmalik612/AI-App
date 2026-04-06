
import streamlit as st
import time

# Page Config (This makes it look professional)
st.set_page_config(page_title="Sehrish Smart AI ✨", page_icon="🤖", layout="centered")

# Custom Styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar for extra features
with st.sidebar:
    st.title("Settings ⚙️")
    st.write("Welcome to your personal AI!")
    st.info("Created by Nono Malik 🌟")
    if st.button("Reset Chat"):
        st.rerun()

# Main Title
st.title("Your AI Companion 🤖✨")
st.subheader("I'm here to listen and help. How are you today?")

# Input Box
user_input = st.text_input("Type your mood or how you feel:", placeholder="e.g. I am feeling very happy today!")

# Mood Logic
if user_input:
    with st.spinner('Thinking...'):
        time.sleep(1) # Simulated thinking time
        
        text = user_input.lower()
        
        if any(word in text for word in ["happy", "great", "good", "excited", "amazing"]):
            st.balloons()
            st.success("### That's Wonderful! 🌟")
            st.write("Your energy is contagious! Keep spreading that joy. What made your day so special?")
            st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueW9ueW9ueW9ueW9ueW9ueW9ueW9ueW9ueW9ueW9ueW9ueSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0HlHFRbmaZtBRhXG/giphy.gif", width=300)
            
        elif any(word in text for word in ["sad", "bad", "down", "unhappy", "crying"]):
            st.warning("### I'm sending you a virtual hug! 🫂")
            st.write("It's okay to feel down sometimes. Take a deep breath. Remember, after every storm, there's a rainbow. 🌈 Would you like to hear a joke to cheer up?")
            
        elif any(word in text for word in ["angry", "mad", "frustrated", "annoyed"]):
            st.error("### Take a deep breath... 🧘‍♀️")
            st.write("I can feel you're upset. Try counting to ten. Sometimes talking about it helps. What's bothering you?")
            
        elif any(word in text for word in ["tired", "sleepy", "exhausted"]):
            st.info("### Time for some rest! 😴")
            st.write("You've worked hard today. Grab a cup of tea, listen to some soft music, and give yourself a break. You deserve it!")
            
        elif any(word in text for word in ["bored", "nothing to do"]):
            st.write("### Let's find something fun! 🎨")
            st.write("How about learning a new Python trick or watching a movie? You could also try drawing something!")
            
        else:
            st.write("### Thanks for sharing! 💬")
            st.write("I'm always here to chat. Tell me more about it!")

# Footer
st.markdown("---")
st.caption("Powered by Streamlit & Nono's Creativity 🚀")