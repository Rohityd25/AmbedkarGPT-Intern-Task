# AmbedkarGPT – Text Retrieval and Question Answering

This project is a console-based application that loads a text file, splits it into small segments, stores the segments in a vector database, and answers queries based on the stored content. The program retrieves the most relevant text pieces and generates answers strictly from the provided context.

The system uses:
- LangChain for text loading, splitting, and retrieval
- HuggingFace sentence embeddings
- ChromaDB for vector storage
- Ollama (Mistral model) for generating responses
- A local text file named `speech.txt` as the source material

---

## How It Works

1. The project checks if a Chroma database already exists.
2. If not, it loads `speech.txt`, splits the content into chunks, and creates embeddings.
3. The embeddings are stored inside a local folder named `chroma_db`.
4. The user can type questions in the console.
5. The system retrieves the most relevant text chunks and answers based only on them.

---

## Project Structure

