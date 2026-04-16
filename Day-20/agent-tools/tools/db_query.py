from langchain.tools import tool
import sqlite3

DB_PATH = "sample.db"

@tool
def run_sql_query(query: str) -> str:
    """
    Execute SQL query on the database and return results.
    Input should be a valid SQL query.
    """

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute(query)

        # Handle SELECT queries (fetch results)
        if query.strip().lower().startswith("select"):
            columns = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            # Convert to list of dictionaries (LLM-friendly)
            results = [dict(zip(columns, row)) for row in rows]

            conn.close()
            return str(results)

        # Handle INSERT/UPDATE/DELETE
        else:
            conn.commit()
            affected = cursor.rowcount
            conn.close()

            return f"Query executed successfully. Rows affected: {affected}"

    except Exception as e:
        return f"Database error: {str(e)}"