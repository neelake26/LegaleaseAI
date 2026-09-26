<>

code

View code

import streamlit as st

from docx import Document

import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="LegalEaseAl")

FILE 2: requirements.txt

Itha copy pannu:

>

code

View code

streamlit

python-docx

google-generativeai
