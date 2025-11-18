
import os
from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama


DB_DIR = "chroma_db"
SPEECH_FILE = "speech.txt"


def build_vectorstore():
    if not Path(SPEECH_FILE).exists():
        raise FileNotFoundError(f"{SPEECH_FILE} not found.")

    print("Loading speech.txt...")
    documents = TextLoader(SPEECH_FILE, encoding="utf-8").load()

    print("Splitting text...")
    splitter = CharacterTextSplitter(chunk_size=400, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    print("Creating embeddings...")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Building ChromaDB...")
    vectordb = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=DB_DIR
    )

    print("Vectorstore created!")
    return vectordb


def load_vectorstore():
    print("Loading ChromaDB...")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return Chroma(
        persist_directory=DB_DIR,
        embedding_function=embeddings
    )


def answer_question(query, vectordb, llm):
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    
    docs = retriever.invoke(query)

    # Convert docs to text
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an assistant that answers ONLY from the given context.
If the answer is not present in the context, say so.

Context:
{context}

Question: {query}

Answer:
"""

    response = llm.invoke(prompt)
    return response


def main():
    print("\nAmbedkarGPT\n")

    
    vectordb = load_vectorstore() if os.path.exists(DB_DIR) else build_vectorstore()

    # LLM
    llm = Ollama(model="mistral")  

    print("Ambedkar-gpt is live! Ask any query from speech.txt")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("You: ").strip()

        if query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        try:
            answer = answer_question(query, vectordb, llm)
            print("\nAmbedkarGPT:", answer, "\n")
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
