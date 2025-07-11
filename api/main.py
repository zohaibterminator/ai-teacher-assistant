from fastapi import FastAPI, UploadFile, Form
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import os
load_dotenv()
chat_histories = {} # for keeping track of users and their chat histories


app = FastAPI()


def get_session_history(user_id: str):
    if user_id not in chat_histories:
        memory = ChatMessageHistory(memory_key="chat_history")
        chat_histories[user_id] = memory
    return chat_histories[user_id]


@app.get('/history/{user_id}')
async def history(user_id: str):
    return {
        'history': get_session_history(user_id)
    }


@app.post('/infer/{user_id}')
async def infer_diagnosis( user_id: str, user_input: str = Form(...), Depends=llm: ChatGroq = ChatGroq()):
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful and polite AI doctor who can diagnose medical conditions and give recommendations for treating diseases. If you don't know the answer to a specific medical inquiry, advise seeking professional help. Keep your diagnoses concise."
            ),  # The persistent system prompt
            MessagesPlaceholder(
                variable_name="chat_history"
            ),  # Where the memory will be stored.
            ("human", "{user_input}")  # Where the human input will injected
        ]
    )

    runnable = prompt | llm | StrOutputParser()

    conversation = RunnableWithMessageHistory(
        runnable,
        get_session_history,
        history_messages_key="chat_history",
        input_messages_key="user_input"
    )

    # Generate response
    response = conversation.invoke(
        {"user_input": user_input},
        config={"configurable": {"session_id": user_id}}
    )

    return {
        'response': response
    }