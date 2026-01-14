import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# Load .env ONLY for local development
load_dotenv()

# Get API key (Local → .env | Cloud → Streamlit Secrets)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise RuntimeError("GOOGLE_API_KEY not found. Add it to Streamlit Secrets.")

def generate_assignment_content(topic, level):
    """Handles the AI generation logic separately from the UI."""

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.0-pro",
        google_api_key=GOOGLE_API_KEY,
        temperature=0.7
    )

    system_msg = (
        f"Write a {level} level assignment. Use '##' for headings. "
        "Each heading MUST have 2-3 long paragraphs. Be academic and formal."
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_msg),
        ("human", f"Topic: {topic}")
    ])

    try:
        chain = prompt | llm
        response = chain.invoke({"topic": topic})
        return response.content
    except Exception as e:
        return f"AI Error: {str(e)}"
