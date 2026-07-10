import os

from langchain_community.document_loaders import (
    PyPDFLoader
)

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import (
    FAISS
)

from rag.vector_store import (
    embeddings
)

documents = []

for file in os.listdir(
    "docs"
):

    if file.endswith(".pdf"):

        loader = PyPDFLoader(
            f"docs/{file}"
        )

        documents.extend(
            loader.load()
        )

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(
    documents
)

db = FAISS.from_documents(
    chunks,
    embeddings
)

db.save_local(
    "faiss_index"
)

print(
    "FAISS Index Created"
)