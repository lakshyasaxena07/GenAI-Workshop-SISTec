import os
from dotenv import load_dotenv

from langchain_community.document_loaders import JSONLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

# --------------------
# Load Pdf
# --------------------

loader = JSONLoader("data/sample.json",jq_schema=".[]", text_content=False)

documents = loader.load()

print("----------------------------------------------------")
print(f"\nTotal Pages in PDF : {len(documents)}")


# --------------------
# Split Documents
# --------------------

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

docs=splitter.split_documents(documents)

print("----------------------------------------------------")
print(f"\nTotal Chunks Created : {len(docs)}")

# --------------------
# Create Embeddings
# --------------------

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# --------------------
# Create Vector Store   
# --------------------

vector_db = FAISS.from_documents(docs, embeddings)

print("----------------------------------------------------")
print("\nFAISS Vector Database Store Created")

# --------------------
# Create Retriever
# --------------------

retriever = vector_db.as_retriever(search_kwargs={"k": 3})

print("----------------------------------------------------")
print("\nRetriever Created")

# --------------------
# Create Groq LLM
# --------------------

llm = ChatGroq(
    api_key=groq_api_key,
    model_name="llama-3.3-70b-versatile",
    temperature=0,
)

# --------------------
# Retrieval QA
# --------------------

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
)

print("----------------------------------------------------")
print("RAG System Ready")

# --------------


while True:

    question=input("\n Ask Question : ")

    if question.lower() in ["exit", "quit"]:
        print("Exiting...")
        break

    result = qa.invoke({"query": question})

    print("\nAnswer : ", result["result"])

    # print("\nRetrieved Context \n ")

    # for i,doc in enumerate(result["source_documents"]):
    #     print(f"\nChunk {i+1}")
    #     print("----------------------------------------------------")
    #     print(doc.page_content)
