import streamlit as st

moods = ["happy", "sad", "angry", "excited"]
responses = ["Yay! Keep smiling 😍", "Don’t worry 💪", "Take a deep breath 😌", "Awesome energy! 🔥"]

def mood_ai(user_mood):
    user_mood = user_mood.lower()
    if user_mood in [m.lower() for m in moods]:
        index = [m.lower() for m in moods].index(user_mood)
        return responses[index]
    else:
        return "I don’t understand 😅"

st.title("Mood AI 🤖")

user_input = st.text_input("Enter your mood:")
if user_input:
    reply = mood_ai(user_input)
    st.write("AI Reply:", reply)