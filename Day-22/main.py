from agents.researcher import ResearcherAgent
from agents.analyzer import AnalyzerAgent
from agents.critic import CriticAgent
from agents.writer import WriterAgent
from agents.coordinator import CoordinatorAgent


def run_system(query):
    state = {"query": query}

    researcher = ResearcherAgent("Researcher")
    analyzer = AnalyzerAgent("Analyzer")
    critic = CriticAgent("Critic")
    writer = WriterAgent("Writer")

    coordinator = CoordinatorAgent(
        "Coordinator",
        agents=[researcher, analyzer, critic, writer],
        max_iterations=1   
    )

    state = coordinator.run(state)

    return state


if __name__ == "__main__":
    query = input("Enter your query: ")

    result = run_system(query)

    print("\n=== FINAL OUTPUT ===\n")
    print(result.get("final_output", "No output"))