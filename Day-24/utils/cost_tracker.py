total_tokens = 0
total_cost = 0.0

COST_PER_1K_TOKENS = 0.002  # example of cost 


def track_usage(text: str):
    """
    Tracks token usage and calculates cost based on text length
    """
    global total_tokens, total_cost

    tokens = len(text.split())  # simple approximation
    cost = (tokens / 1000) * COST_PER_1K_TOKENS

    total_tokens += tokens
    total_cost += cost

    return tokens, cost


def get_usage():
    """
    Returns total tokens used and total cost
    """
    return total_tokens, total_cost