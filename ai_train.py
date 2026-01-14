import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env ONLY for local development
load_dotenv()

# Get API key (Local → .env | Cloud → Streamlit Secrets)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise RuntimeError("GOOGLE_API_KEY not found. Add it to Streamlit Secrets.")

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# Load model (this one WORKS)
model = genai.GenerativeModel("gemini-pro")

def generate_assignment_content(topic, level):
    """Generate academic assignment content using Gemini"""

    prompt = f"""
    Write a {level} level academic assignment on "{topic}".

    Instructions:
    - Use '##' for headings
    - Each heading must have 2–3 long paragraphs
    - Maintain a formal, academic tone
    - Include an introduction and conclusion
    """

    response = model.generate_content(prompt)
    return response.text
