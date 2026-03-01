GenAI Learner Helper (RAG-Based AI Tutor)

A Retrieval-Augmented Generation (RAG) powered AI tutor built using LangChain, FAISS, HuggingFace embeddings, and LLM inference API.

This project demonstrates how to build a grounded AI system that retrieves knowledge from custom documents before generating responses.

FEATURES:
        Retrieval-Augmented Generation (RAG)
        Semantic search using FAISS
        HuggingFace sentence-transformer embeddings
        LLM-powered response generation
        Multi-document knowledge base
        Chunking with RecursiveCharacterTextSplitter
        Grounded responses from local documents

ARCHITECTURE:
        User Query
            ↓
        Convert to Embedding
            ↓
        FAISS Similarity Search
            ↓
        Retrieve Top-K Chunks
            ↓
        Send Context + Query to LLM
            ↓
        Generated Grounded Response