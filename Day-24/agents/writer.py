from utils.logger import logger

def writer_agent(text: str) -> str:
    """
    Writer agent: generates final structured report
    """
    logger.info("[Writer] Generating final report")

    result = f"Final Report: {text}"

    logger.info("[Writer] Completed")

    return result