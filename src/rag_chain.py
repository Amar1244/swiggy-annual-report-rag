import os
import streamlit as st
from google import genai


def setup_gemini():
    """
    Setup Gemini for both local and Streamlit Cloud
    """

    # Try local .env first
    api_key = os.getenv("GEMINI_API_KEY")

    # If not found, try Streamlit secrets
    if not api_key:
        api_key = st.secrets.get("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY not found")

    client = genai.Client(api_key=api_key)

    return client


def ask_question(client, vectordb, question):

    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    docs = retriever.invoke(question)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
Answer ONLY from the context below.

If answer not found say:
Answer not found in document

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
    )

    return response.text, docs