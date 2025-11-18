# 📘 AmbedkarGPT – Text Retrieval & Question Answering

AmbedkarGPT is a command-line application that processes a text file, stores its content in a vector database, and answers user queries based strictly on that content.  
It uses sentence embeddings, ChromaDB, and the Mistral model (via Ollama) to retrieve the most relevant information.

---

## 🚀 Features

- Loads and processes `speech.txt`
- Splits text into manageable chunks
- Creates vector embeddings using HuggingFace
- Stores and retrieves text using ChromaDB
- Answers user queries strictly from retrieved context
- Runs completely through the terminal

---

## 📂 Project Structure

.
├── main.py
├── speech.txt
├── requirements.txt
└── README.md

The folder `chroma_db/` will be created automatically on the first run.

##  Installation

### 1️⃣ Install Python dependencies

pip install -r requirements.txt

### 2️⃣ Install Ollama (required for the Mistral model)

Download from:  
https://ollama.com/

Then pull the model:

ollama pull mistral
---

## ▶️ Usage

Run the application:

python main.py

You can now type questions related to the content of `speech.txt`.

To exit:

exit

---

## 📝 Notes

- The application answers **only** from the information available in `speech.txt`.
- If the vector database does not exist, it will be created automatically.
- The program uses local embeddings and local model inference (via Ollama).

---

