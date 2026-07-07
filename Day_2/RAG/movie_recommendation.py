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

url = "https://dummyjson.com/posts"

response = requests.get(url)

response_json = response.json()
posts = response_json["posts"]

print("----------------------------------------------------")
print("Posts Loaded:", len(posts))
print("----------------------------------------------------")

# --------------------
# convert json to documents
# ---------------------

data = []

for post in posts:

    text = f"""
    ID : {post['id']}
    Title : {post['title']}
    Body : {post['body']}
    Tags : {', '.join(post['tags'])}
    Reactions : likes={post['reactions']['likes']}, dislikes={post['reactions']['dislikes']}
    Views : {post['views']}
    User_ID : {post['userId']}

    """

    data.append(Document(page_content=text))

print("----------------------------------------------------")
print("Data Created:", len(data))
print("----------------------------------------------------")

# --------------------
# split documents into chunks
# --------------------

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
)

docs = splitter.split_documents(data)

print("----------------------------------------------------")
print("Movies Split into Chunks:", len(docs))
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

retriever = vector_db.as_retriever(search_kwargs={"k": 10})
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

    for doc in result["source_documents"]:
        print("----------------------------------------------------")
        print(doc.page_content)
