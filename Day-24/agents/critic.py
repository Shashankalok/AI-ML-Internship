from utils.logger import logger

def critic_agent(text: str) -> str:
    """
    Critic agent: reviews content and suggests improvements
    """
    logger.info("[Critic] Reviewing content")

    result = f"Critique: The content is clear but could be improved by adding more detailed examples and clarity. Content: {text}"

    logger.info("[Critic] Completed")

    return result