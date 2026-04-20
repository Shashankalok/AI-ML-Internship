from utils.logger import logger

def researcher_agent(query: str) -> str:
    """
    Researcher agent: provides basic explanation of a query
    """
    logger.info(f"[Researcher] Received query: {query}")

    result = f"Research on: {query}. Financial risk involves uncertainty in returns."

    logger.info("[Researcher] Completed")

    return result