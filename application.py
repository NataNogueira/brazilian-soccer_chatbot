# Libraries
import streamlit as st
import pandas as pd
import google.generativeai as genai
import logging
import os

from dotenv import load_dotenv

load_dotenv()

# Configure API_KEY
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Gemini Model
model = genai.GenerativeModel('gemini-1.5-flash')


# Configuration setup
st.set_page_config(page_title="ChatBot Brasileirão", page_icon="⚽")
st.markdown("<h1 style='text-align: center;'>Chatbot Brasileirão</h1>", unsafe_allow_html=True)
# st.markdown("<p style='text-align: center; color: #888;'>Your AI assistant is here to help you! 🚀</p>", unsafe_allow_html=True)

# Sidebar setup
st.sidebar.header("**Natã Nogueira**")
st.sidebar.write("Data Scientist & Machine Learning")

st.sidebar.header("Contact Information", divider='rainbow')
st.sidebar.write("Feel free to reach out through the following")
st.sidebar.write("[LinkedIn](https://www.linkedin.com/in/natã-nogueira-227a01181)")
st.sidebar.write("[GitHub](https://github.com/NataNogueira)")
st.sidebar.write("[Email](mailto:natanogueirasktt@gmail.com)")
st.sidebar.write("Developed by Natã Nogueira", unsafe_allow_html=True)

# Main content area
st.markdown("## ✍️ Enter your query below:")


def getResponseFromModel(user_input):
    """
    This function sends the user's input to the Gemini model and returns the generated response.
    """
    try:
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return "Sorry, something went wrong. Please try again later."

# Iniciar uma sessão de chat
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Função para exibir as mensagens do chat
def display_chat():
    for msg in st.session_state.messages:
        if msg['role'] == 'user':
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**Bot:** {msg['content']}")

# Formulário para entrada de mensagem
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("", placeholder="Ask me anything...", key='user_input')
    submit_button = st.form_submit_button(label='Send')

    if submit_button and user_input:
        # Adicionar mensagem do usuário
        st.session_state.messages.append({'role': 'user', 'content': user_input})

        # Resposta do modelo
        with st.spinner("🤔 Thinking..."):
            bot_response = getResponseFromModel(user_input)
        
        # Adicionar resposta do bot
        st.session_state.messages.append({'role': 'bot', 'content': bot_response})

display_chat()

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Developed by Natã Nogueira</p>", unsafe_allow_html=True)