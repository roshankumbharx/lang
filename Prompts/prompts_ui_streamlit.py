from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

llm = HuggingFaceEndpoint(model='openai/gpt-oss-120b')

model = ChatHuggingFace(llm=llm)

st.header('Research Tool')

userInput = st.text_input('Enter Your Prompt')

if st.button('Summarize'):
    res = model.invoke(userInput)   
    st.write(res.content)