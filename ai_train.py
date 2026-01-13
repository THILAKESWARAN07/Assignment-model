import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

def generate_assignment_content(topic, level):
    """Handles the AI generation logic separately from the UI."""
    if not api_key:
        return "Error: GOOGLE_API_KEY not found."

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", 
        google_api_key=api_key,
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