import streamlit as st
from main import build_rag_system, query_rag

st.set_page_config(page_title="Swiggy RAG AI")

st.title("📄 Swiggy Annual Report RAG AI")

st.write("Ask questions based ONLY on Swiggy Annual Report")


# Build RAG System
if st.button("Build RAG System"):

    with st.spinner("Building RAG System..."):

        model, vectordb = build_rag_system()

        st.session_state.model = model
        st.session_state.vectordb = vectordb

    st.success("✅ RAG System Ready")


# Ask Question
question = st.text_input("Ask a Question")

if st.button("Ask Question"):

    if "model" not in st.session_state:
        st.warning("⚠️ Build RAG System first")

    elif question == "":
        st.warning("⚠️ Enter a question")

    else:
        with st.spinner("Searching..."):

            answer, docs = query_rag(
                st.session_state.model,
                st.session_state.vectordb,
                question
            )

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Sources")

        for doc in docs:
            page = doc.metadata.get("page", "Unknown")
            st.write(f"Page: {page}")