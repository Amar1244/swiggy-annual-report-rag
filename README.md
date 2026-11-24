# Swiggy Annual Report RAG AI

A Retrieval-Augmented Generation (RAG) app that answers questions **only from the Swiggy Annual Report (FY 2023-24)**. Ask a question, get an answer grounded in the report, and see the page numbers it came from.

**🔗 Live demo: [swiggy-rag-ai.streamlit.app](https://swiggy-rag-ai.streamlit.app)**

## How it works

1. **Load:** the report PDF is read page by page with `PyPDFLoader`.
2. **Chunk:** the text is split into 800-character chunks with 100 characters of overlap.
3. **Embed and store:** chunks are embedded with `sentence-transformers/all-MiniLM-L6-v2` and saved in a **Chroma** vector database. It is built on the first run and reused after that.
4. **Retrieve:** for each question, the 3 most similar chunks are fetched.
5. **Generate:** the chunks and the question go to **Google Gemini**, with an instruction to answer only from that context. If the answer isn't in the report, the app replies *"Answer not found in document"*.
6. **Cite:** the page numbers of the retrieved chunks are shown under the answer.

## Features

- Answers grounded in the report, with source page numbers
- Refuses to answer from outside the document
- Vector database is persisted, so later runs start faster
- Simple Streamlit interface

## Keywords

Generative AI · Retrieval-Augmented Generation (RAG) · LLM · Vector database · Semantic search · Question answering · Document Q&A · NLP · Chatbot · LangChain · ChromaDB · Google Gemini · Hugging Face · Streamlit · Python

## Tech Stack

- Python and [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/) for loading and splitting
- [ChromaDB](https://www.trychroma.com/) as the vector store
- [Hugging Face sentence-transformers](https://www.sbert.net/) for embeddings
- [Google Gemini](https://ai.google.dev/) for answer generation

## Project Structure

| Path | Purpose |
| :--- | :--- |
| `app.py` | Streamlit UI |
| `main.py` | Builds the RAG system and runs queries |
| `src/pdf_loader.py` | Loads the report PDF (and uploaded PDFs) |
| `src/chunking.py` | Splits documents into chunks |
| `src/vectordb.py` | Creates or loads the Chroma vector database |
| `src/rag_chain.py` | Retrieval, prompt and Gemini call |
| `data/swiggy_report.pdf` | The source document |

## Author

**Amar Chaurasiya**, open to full-time roles and freelance work.

- Email: [amarchaurasiya124@gmail.com](mailto:amarchaurasiya124@gmail.com)
- LinkedIn: [amar-chaurasiya-163788262](https://www.linkedin.com/in/amar-chaurasiya-163788262)
- Portfolio: [amarchaurasiya.vercel.app](https://amarchaurasiya.vercel.app)
