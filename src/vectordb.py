# src/vectordb.py

import os
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


PERSIST_DIRECTORY = "vectorstore"


def create_or_load_vector_db(chunks):
    """
    Create or load vector database for Swiggy report
    """

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    if os.path.exists(PERSIST_DIRECTORY):

        vectordb = Chroma(
            persist_directory=PERSIST_DIRECTORY,
            embedding_function=embedding_model
        )

        print("Loaded Existing Swiggy Vector DB")

    else:

        vectordb = Chroma.from_documents(
            documents=chunks,
            embedding=embedding_model,
            persist_directory=PERSIST_DIRECTORY
        )

        vectordb.persist()

        print("Created New Swiggy Vector DB")

    return vectordb