# db.py
from dotenv import load_dotenv
# pyrefly: ignore [missing-import]
import mysql.connector
import os

load_dotenv()


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        port=os.getenv("DB_PORT"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )


def get_all_employees():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
                    SELECT id,name,department,salary
                    FROM employees
                """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def get_employee_by_department(department):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
                    SELECT id,name,department,salary
                    FROM employees
                    WHERE department = %(department)s
                """,{"department":department})
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
