from langchain_community.vectorstores import (
    FAISS
)

from rag.vector_store import (
    embeddings
)

db = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

def search_documents(
    query: str
):

    docs = db.similarity_search(
        query,
        k=3
    )

    return docs