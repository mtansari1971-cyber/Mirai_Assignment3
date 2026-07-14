import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Page Config

st.set_page_config(
    page_title="AI Multiverse",
    page_icon="🌌"
)

st.title("🌌 AI Multiverse")
st.write("Talk with different AI personalities!")


# Sidebar

personality = st.sidebar.selectbox(
    "Choose Personality",
    [
        "Common Indian Man",
        "Crazy Salman Khan Fan",
        "Little Boy",
        "Motivational Coach",
        "Software Engineer",
        "College Professor",
        "Stand-up Comedian",
        "Entrepreneur",
        "Friendly Teacher",
        "AI Assistant"
    ]
)


# Task 1:
# Initialize Session State

if "messages" not in st.session_state:
    st.session_state.messages = []


# Optional Clear Chat Button

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()


# Task 2:
# Display Chat History

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Task 3:
# Chat Input

if user_message := st.chat_input("Say something..."):

  
    # Task 4:
    # Save User Message
    
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    # Show user message immediately
    with st.chat_message("user"):
        st.markdown(user_message)

    # Personality Prompt
    instruction = f"""
You are acting as {personality}.user:{user_message}

Stay completely in character.

Reply naturally.

Never mention you are an AI unless the user explicitly asks.

Keep responses engaging.
"""

    # Generate Response
    with st.spinner("🌌 Travelling through the Multiverse..."):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"{instruction}\n\nUser: {user_message}"
            )

            assistant_reply = response.text

        except Exception as e:

            assistant_reply = f"❌ Error: {e}"

   
    # Task 4:
    # Save AI Response
    
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )

    # Display Assistant Response
    with st.chat_message("assistant"):
        st.markdown(assistant_reply)