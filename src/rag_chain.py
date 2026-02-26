import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


def setup_gemini():
    """
    Setup Gemini using new SDK
    """

    api_key = os.getenv("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    return client


def ask_question(client, vectordb, question):
    """
    Ask question using RAG
    """

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
        # model="gemini-1.0-pro",
        model="gemini-3-flash-preview",
        contents=prompt,
    )

    return response.text, docs