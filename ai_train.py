import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Securely fetch the API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")

def generate_assignment_content(topic, level):
    """Handles the AI generation logic."""
    
    if not GOOGLE_API_KEY:
        return "Error: API Key not found. Please configure it in your environment or Streamlit Secrets."

    # Updated to a currently available model version
    llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro", 
    google_api_key=GOOGLE_API_KEY,
    temperature=0.7
)

    system_msg = (
        f"You are a professional academic writer. Write a {level} level assignment. "
        "Use '##' for headings. Each heading MUST have 2-3 long, detailed paragraphs. "
        "The tone must be academic, formal, and include citations where appropriate."
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_msg),
        ("human", "Topic: {topic}")
    ])

    try:
        chain = prompt | llm
        response = chain.invoke({"topic": topic})
        return response.content
    except Exception as e:
        return f"AI Error: {str(e)}"