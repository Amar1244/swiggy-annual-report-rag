# src/pdf_loader.py
from langchain_community.document_loaders import PyPDFLoader
import tempfile
import os


def load_default_pdf():
    """
    Loads the default Swiggy Annual Report
    """
    pdf_path = "data/swiggy_report.pdf"
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    return documents


def load_uploaded_pdf(uploaded_file):
    """
    Loads user uploaded PDF file
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    loader = PyPDFLoader(tmp_path)
    documents = loader.load()

    os.remove(tmp_path)

    return documents