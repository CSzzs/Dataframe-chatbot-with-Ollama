import pandas as pd
import streamlit as st
from langchain.agents import AgentType
from langchain_experimental.agents import  create_pandas_dataframe_agent
from langchain_ollama import ChatOllama

#streamlit web page configuration
st.set_page_config(
    page_title="DF Chat",
    page_icon = "💬",
    layout = "centered"
)

def read_data(file):
    if file.name.endswith(".csv"):
        return pd.read_csv(file)
    else:
        return pd.read_excel(file)
    

# streamlit page title
st.title("🤖 DataFrame chatbot - Ollama")

#initialize chat history in streamlit session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#initiate Dataframe in session state
if "df" not in st.session_state:
    st.session_state.df = None

#File upload widget
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "xls"])

if uploaded_file:
    st.session_state.df = read_data(uploaded_file)
    st.write("Dataframe Preview")
    st.dataframe(st.session_state.df.head())

# displat chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

