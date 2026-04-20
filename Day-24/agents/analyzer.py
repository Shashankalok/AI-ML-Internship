from utils.logger import logger

def analyzer_agent(text: str) -> str:
    """
    Analyzer agent: analyzes given text and extracts insights
    """
    logger.info("[Analyzer] Running analysis")

    result = f"Analysis: The given content discusses key aspects related to: {text}"

    logger.info("[Analyzer] Completed")

    return result