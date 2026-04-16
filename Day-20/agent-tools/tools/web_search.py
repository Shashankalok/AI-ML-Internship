from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

# Initialize search tool
search = DuckDuckGoSearchRun()

@tool
def web_search(query: str) -> str:
    """
    Search the internet for a given query and return results.
    Input should be a search query string.
    """
    try:
        results = search.run(query)
        return str(results)
    except Exception as e:
        return f"Error during web search: {str(e)}"