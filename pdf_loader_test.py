from src.pdf_loader import load_default_pdf

docs = load_default_pdf()
print(len(docs))
print(docs[0].page_content[:500])