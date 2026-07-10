import os
# pyrefly: ignore [missing-import]
import psycopg

from dotenv import load_dotenv
# pyrefly: ignore [missing-import]
from langgraph.checkpoint.postgres import PostgresSaver

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg.connect(
    DATABASE_URL,
    autocommit=True
)

checkpointer = PostgresSaver(conn)

print("Creating LangGraph tables...")

checkpointer.setup()

print("PostgreSQL Checkpointer Ready")