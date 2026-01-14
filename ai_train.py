import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env ONLY for local development
load_dotenv()

# API key (AI Studio key)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise RuntimeError("GOOGLE_API_KEY not found.")

# Configure Gemini (AI Studio mode)
genai.configure(api_key=GOOGLE_API_KEY)

def generate_assignment_content(topic, level):
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config={
            "temperature": 0.7,
            "max_output_tokens": 2048,
        }
    )

    prompt = f"""
    Write a {level} level academic assignment on "{topic}".

    Requirements:
    - Use ## for headings
    - Each heading must contain 2–3 long paragraphs
    - Formal academic tone
    - Include introduction and conclusion
    """

    response = model.generate_content(prompt)
    return response.text
