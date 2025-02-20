from llm_script import load_llm  # Import the function from llm_script.py
from chatbot import create_prompt, extract_text_from_pdf  # Import other functions
import streamlit as st

# Load model & prompt
llm = load_llm()
prompt_template = create_prompt()

st.title("📄 AI-Powered PDF Chatbot")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    pdf_text = extract_text_from_pdf("temp.pdf")
    st.success("PDF uploaded and processed!")

    user_input = st.text_input("Ask a question about the PDF:")

    if user_input:
        response = prompt_template | llm
        answer = response.invoke({"pdf_text": pdf_text, "question": user_input})
        st.write("🤖 AI:", answer)
