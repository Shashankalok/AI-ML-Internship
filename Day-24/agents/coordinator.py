from agents.researcher import researcher_agent
from agents.analyzer import analyzer_agent
from agents.critic import critic_agent
from agents.writer import writer_agent
from utils.logger import logger
from utils.cost_tracker import track_usage, get_usage

def coordinator_agent(query: str) -> str:
    """
    Coordinator agent: manages full workflow across all agents
    """
    logger.info("[Coordinator] Workflow started")

    # Step 1: Research
    research = researcher_agent(query)
    logger.info("[Coordinator] Research completed")

    # Step 2: Analyze
    analysis = analyzer_agent(research)
    logger.info("[Coordinator] Analysis completed")

    # Step 3: Critique
    critique = critic_agent(analysis)
    logger.info("[Coordinator] Critique completed")

    # Step 4: Final Report
    final = writer_agent(critique)
    logger.info("[Coordinator] Writing completed")

    # Cost tracking
    tokens, cost = track_usage(final)
    logger.info(f"[Cost] Tokens: {tokens}, Cost: ${cost:.6f}")

    total_tokens, total_cost = get_usage()
    logger.info(f"[Total Cost] Tokens: {total_tokens}, Cost: ${total_cost:.6f}")

    logger.info("[Coordinator] Workflow completed")

    return final