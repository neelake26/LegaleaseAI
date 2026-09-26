
import streamlit as st
from docx import Document
import google.generativeai as genai

# API Key Streamlit secrets la irunthu edukkum
api_key = st.secrets.get("GOOGLE_API_KEY", "YOUR_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="LegalEaseAI", page_icon="⚖️")
st.title("⚖️ LegalEaseAI - Legal Document Simplifier")

uploaded_file = st.file_uploader("Upload your legal document (.docx / .txt)", type=["docx", "txt"])

if uploaded_file:
    text = ""
    if uploaded_file.name.endswith(".docx"):
        doc = Document(uploaded_file)
        text = "\n".join([p.text for p in doc.paragraphs])
    else:
        text = uploaded_file.read().decode("utf-8")

    st.subheader("Original Document")
    st.write(text[:2000])

    if st.button("Simplify"):
        with st.spinner("AI is simplifying..."):
            prompt = f"Simplify this legal document in simple English and Tamil mixed, explain like I'm 5: \n\n{text}"
            response = model.generate_content(prompt)
            st.subheader("Simplified Version")
            st.write(response.text)
