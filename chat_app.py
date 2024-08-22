import streamlit as st
# from langchain_openai.chat_models import ChatOpenAI

import streamlit as st
import random
import time

# st.title("Wine Stain")


openai_api_key = st.secrets["openai_api_key"]
pinecone_api_key = st.secrets["pinecone_api_key"]

# Use the secrets in your app



# def generate_response(input_text):
#     model = ChatOpenAI(temperature=0.7, api_key=openai_api_key)
#     st.info(model.invoke(input_text))




# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("Wine chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
