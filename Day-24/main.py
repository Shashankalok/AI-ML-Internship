from utils.cost_tracker import get_usage
from agents.coordinator import coordinator_agent

def run():
    """
    Runs the multi-agent system from user input
    """
    query = input("Enter your query: ").strip()

    if not query:
        print("Please enter a valid query.")
        return

    result = coordinator_agent(query)

    tokens, cost = get_usage()

    print("\nFinal Output:\n", result)
    print(f"\nTokens Used: {tokens}")
    print(f"Total Cost: ${cost:.6f}")


if __name__ == "__main__":
    run()