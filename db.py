import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password=os.getenv("MYSQL_PASSWORD"),
        database="rag_demo",
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )

def query_mysql(query: str):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
    finally:
        conn.close()
