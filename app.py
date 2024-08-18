import streamlit as st
from openai import OpenAI
import time

st.title('Lavender!')
st.write('Answer to all your questions!')

OPENAI_API_KEY =  "" #Write your API Key Here
client =  OpenAI(api_key = OPENAI_API_KEY) 

st.logo("logo-latest.png")
st.sidebar.title("Chats") 
st.sidebar.button("First chat", use_container_width=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# check if the prompt is not None and simuntaneously assign it a value 
if prompt := st.chat_input("Ask lavendar"):
    with st.chat_message("user"):
        st.write(prompt)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    if  OPENAI_API_KEY:
        reply = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}])
        response = reply.choices[0].message.content

        with st.chat_message("assistant"):
            st.write (response)
        
        # Add response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

    else:
        st.warning("Please add an API Key to get a response")


# # inserts delay in responses to give a thinking like effect
# def response_converter(response):
#     chunks = response.split('\n') 

#     for chunk in chunks:
#         yield chunk + '\n'
#         time.sleep(0.10)