import streamlit as st
from chatbot import response
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize message history in session state
def fetch_conversation_history():
    
    if 'messages' not in st.session_state:
        st.session_state['messages'] = [
            {"role": "system", "content": "You are an educator bot - Teach"}
        ]
    return st.session_state['messages']

# Streamlit UI setup
st.title("Educational Chatbot")
st.write("Ask anything, and the educator bot will assist you!")

# Create a form for user input with a submit button
with st.form("chat_form"):
    user_input = st.text_input("Your question:", key="input")
    submit_button = st.form_submit_button("Send")

# Process input if submit button is pressed
if submit_button and user_input:
    # Fetch and update message history
    messages = fetch_conversation_history()
    messages.append({"role": "user", "content": user_input})  # Capture user input

    # Get bot response and update message history
    answer = response(messages)
    messages.append({"role": "assistant", "content": answer})  # Capture assistant response

    # Display conversation history
    for message in messages:
        if message["role"] == "assistant":
            st.write(f"Assistant: {message['content']}")
        elif message["role"] == "user":
            st.write(f"You: {message['content']}")
        elif message["role"] == "system":
            st.write(f"System: {message['content']}")
