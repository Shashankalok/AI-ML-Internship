from tavily import TavilyClient
from config.settings import TAVILY_API_KEY

client = TavilyClient(api_key=TAVILY_API_KEY)


def web_search(query):
    """
    Real web search using Tavily API
    """
    response = client.search(
        query=query,
        search_depth="advanced",  
        max_results=3
    )

    results = []

    for res in response["results"]:
        results.append(f"{res['title']}: {res['content']}")

    return "\n\n".join(results)