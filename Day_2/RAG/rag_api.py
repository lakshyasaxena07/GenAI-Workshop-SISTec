import os
import requests
from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

users = response.json()

print("----------------------------------------------------")
print("Users Loaded:", len(users))
print("----------------------------------------------------")

# --------------------
# convert json to documents
# --------------------

documents = []

for user in users:

    text = f"""
    ID : {user['id']}
    Name : {user['name']}
    Username : {user['username']}
    Email : {user['email']}
    Phone : {user['phone']}
    Website : {user['website']}

    Company :
    {user['company']['name']}

    Catch Phrase :
    {user['company']['catchPhrase']}

    City :
    {user['address']['city']}

    Street :
    {user['address']['street']}
    """

    documents.append(Document(page_content=text))

print("----------------------------------------------------")
print("Documents Created:", len(documents))
print("----------------------------------------------------")

# --------------------
# split documents into chunks
# --------------------

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
)

docs = splitter.split_documents(documents)

print("----------------------------------------------------")
print("Documents Split into Chunks:", len(docs))
print("----------------------------------------------------")

# --------------------
# create embedding model
# --------------------

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# --------------------
# create vector store
# --------------------

vector_db = FAISS.from_documents(docs, embeddings)

print("----------------------------------------------------")
print("FAISS Vector Store Created")
print("----------------------------------------------------")

# --------------------
# create retriever
# --------------------

retriever = vector_db.as_retriever(search_kwargs={"k": 3})
print("----------------------------------------------------")
print("Retriever Created")
print("----------------------------------------------------")

# --------------------
# create Groq LLM
# --------------------

llm = ChatGroq(
    api_key=groq_api_key,
    model_name="llama-3.3-70b-versatile",
    temperature=0,
)

# --------------------
# create RAG chain
# --------------------

qa = RetrievalQA.from_chain_type(
    llm=llm, retriever=retriever, chain_type="stuff", return_source_documents=True
)
print("----------------------------------------------------")
print("RAG Chain Created")
print("----------------------------------------------------")

# --------------------
# chat Loop
# --------------------

while True:
    question = input("\nAsk Question : ")

    if question.lower() in ["exit", "quit"]:
        print("Exiting...")
        break

    result = qa.invoke({"query": question})

    print("\nAnswer : ", result["result"])

    print("\nRetrieved Documents : ")

    # for doc in result["source_documents"]:
    #     print("----------------------------------------------------")
    #     print(doc.page_content)
