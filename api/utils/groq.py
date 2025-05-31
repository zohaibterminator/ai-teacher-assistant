from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

def getGroq():
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        groq_api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.5,
    )

    try:
        yield llm
    finally:
        print("LLM Loaded Successfully")