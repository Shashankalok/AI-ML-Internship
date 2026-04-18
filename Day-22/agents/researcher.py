from agents.base_agent import BaseAgent
from tools.web_search import web_search


class ResearcherAgent(BaseAgent):
    def run(self, state):
        query = state.get("query", "")

        self.log(f"Searching for: {query}")

        # Call tool
        results = web_search(query)

        # Update state
        state["research"] = results

        self.log("Research completed")

        return state