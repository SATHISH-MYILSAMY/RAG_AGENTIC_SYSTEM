import aiohttp
import asyncio
from db import get_connection

API_URL = "https://www.federalregister.gov/api/v1/documents.json"

async def fetch_data(session, page=1):
    params = {
        "per_page": 10,
        "page": page,
        "order": "newest",
        "conditions[publication_date][gte]": "2025-01-01"
    }
    async with session.get(API_URL, params=params) as resp:
        return await resp.json()

async def download_documents():
    async with aiohttp.ClientSession() as session:
        data = await fetch_data(session)
        docs = data.get("results", [])
        return [{
            "title": d["title"],
            "summary": d["abstract"],
            "publication_date": d["publication_date"]
        } for d in docs]

def save_to_mysql(docs):
    conn = get_connection()
    with conn.cursor() as cursor:
        for d in docs:
            cursor.execute(
                "INSERT IGNORE INTO federal_documents (title, summary, publication_date) VALUES (%s, %s, %s)",
                (d["title"], d["summary"], d["publication_date"])
            )
    conn.close()

def run_pipeline():
    docs = asyncio.run(download_documents())
    save_to_mysql(docs)
