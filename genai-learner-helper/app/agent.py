from retriever import get_retriever
from generator import generate_response


def build_agent():
    retriever = get_retriever()

    def rag_pipeline(query: str):
        # Retrieve relevant docs
        docs = retriever.invoke(query)

        # Combine context
        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
        You are an expert AI tutor.
        Answer ONLY using the context below.
        If the answer is not in the context, say "I don't know based on provided documents."

        Context:
        {context}

        Question:
        {query}

        Answer:
        """
        response = generate_response(prompt)

        return response

    return rag_pipeline