import os
from agent import build_agent
from rag_pipeline import create_vectorstore

if __name__ == "__main__":

    if not os.path.exists("vectorstore/index.faiss"):
        print("Creating vectorstore...")
        create_vectorstore()

    agent = build_agent()

    print("\n🎓 GenAI Learner Helper (HuggingFace RAG)")
    print("Type 'exit' to quit\n")

while True:
    query = input("Ask your question: ")

    if query.lower() == "exit":
        print("Goodbye! See you next time! in the meantime, keep exploring and learning with GenAI!")
        break

    response = agent(query)

    print("\n📘 Answer:\n", response)
    print("\n" + "-"*50)