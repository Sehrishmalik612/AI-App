import streamlit as st

st.title("Sehrish Smart AI 🤖✨")

# Mood AI
moods = ["happy", "sad", "angry"]
responses_mood = ["Yay! 😍", "Don’t worry 💪", "Relax 😌"]

# Chatbot responses
responses_chat = {
    "hi": "Hello 😄",
    "how are you": "I am fine 🤖",
    "what is ai": "AI is smart system 🤓",
    "bye": "Goodbye 👋"
}

def mood_ai(user):
    user = user.lower()
    if user in moods:
        index = moods.index(user)
        return responses_mood[index]
    return None

def chatbot(user):
    user = user.lower()
    for key in responses_chat:
        if key in user:
            return responses_chat[key]
    return None

user_input = st.text_input("You:")

if user_input:
    mood_reply = mood_ai(user_input)
    chat_reply = chatbot(user_input)

    if mood_reply:
        st.write("Mood AI:", mood_reply)
    elif chat_reply:
        st.write("Chatbot:", chat_reply)
    else:
        st.write("AI: I don't understand 😅")