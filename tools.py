from db import query_mysql

def fetch_documents_by_topic(topic: str, from_date: str, to_date: str) -> str:
    query = f"""
    SELECT title, summary, publication_date 
    FROM federal_documents 
    WHERE (title LIKE '%{topic}%' OR summary LIKE '%{topic}%') 
      AND publication_date BETWEEN '{from_date}' AND '{to_date}'
    ORDER BY publication_date DESC
    LIMIT 5;
    """
    results = query_mysql(query)
    if not results:
        return "No documents found."
    return "\n\n".join(f"{r['publication_date']} - {r['title']}\n{r['summary']}" for r in results)
