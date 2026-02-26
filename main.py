from src.pdf_loader import load_default_pdf
from src.chunking import split_documents
from src.vectordb import create_or_load_vector_db
from src.rag_chain import setup_gemini, ask_question


def build_rag_system():
    """
    Build RAG system using only Swiggy Annual Report
    """

    documents = load_default_pdf()

    chunks = split_documents(documents)

    vectordb = create_or_load_vector_db(chunks)

    model = setup_gemini()

    return model, vectordb


def query_rag(model, vectordb, question):

    answer, docs = ask_question(
        model,
        vectordb,
        question
    )

    return answer, docs