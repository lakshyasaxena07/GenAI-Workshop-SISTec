import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_connection():

    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )


def get_all_employees():

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""
        SELECT id,name,department,salary
        FROM employees
    """)

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows


def get_employee_by_department(department):

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""
        SELECT id,name,salary
        FROM employees
        WHERE department=%s
    """, (department,))

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows