from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import streamlit as st
llm = HuggingFacePipeline.from_model_id(model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",task="text-generation",)
chat_model = ChatHuggingFace(llm = llm)

st.header("Hugging Face Chat Model")
query = st.text_input("Enter Your prompt here :")

if st.button("Submit"):
    response = chat_model.invoke(query)
    st.write(response.content)