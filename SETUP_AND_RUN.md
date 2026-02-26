# 🚀 Swiggy Annual Report RAG AI – Setup & Run Guide

This guide explains how to run the Retrieval-Augmented Generation (RAG) application locally.

The system answers questions ONLY from the Swiggy Annual Report.

------------------------------------------------------------

## 📌 Prerequisites

- Python 3.10 or higher installed
- Internet connection (for installing packages and Gemini API)

------------------------------------------------------------

## 📥 Step 1: Download the Project

Option A: Clone from GitHub

git clone <repository_link>
cd swiggy-rag-ai

OR

Option B: Download ZIP and extract it.
Then open the project folder in terminal.

------------------------------------------------------------

## 📦 Step 2: Create Virtual Environment

Windows:

python -m venv .venv
.venv\Scripts\activate

Mac/Linux:

python3 -m venv .venv
source .venv/bin/activate

------------------------------------------------------------

## 📦 Step 3: Install Dependencies

pip install -r requirements.txt

------------------------------------------------------------

## 🔑 Step 4: Add Gemini API Key

Create a file named:

.env

Inside the .env file, add:

GEMINI_API_KEY=your_api_key_here

You can generate an API key from:
https://aistudio.google.com/app/apikey

------------------------------------------------------------

## ▶ Step 5: Run the Application

streamlit run app.py

------------------------------------------------------------

## 🌐 Step 6: Open in Browser

After running the above command, Streamlit will show:

http://localhost:8501

Open that URL in your browser.

------------------------------------------------------------

## ✅ How to Use the Application

1. Click "Build RAG System"
2. Enter a question (example: "What is Swiggy total income?")
3. View the generated answer
4. Check source page numbers below the answer

------------------------------------------------------------

## 📌 Important Notes

- The system answers ONLY from the Swiggy Annual Report.
- If the answer is not present in the document, it will return:
  
  "Answer not found in document"

- The vector database is created during first run and reused later for faster performance.

------------------------------------------------------------

Thank you for reviewing this project.