from agents.base_agent import BaseAgent


class CoordinatorAgent(BaseAgent):
    def __init__(self, name, agents, max_iterations=2):
        super().__init__(name)
        self.agents = agents
        self.max_iterations = max_iterations

    def run(self, state):
        self.log("Starting workflow...")

        iteration = 0

        #  Improvement loop
        while iteration < self.max_iterations:
            self.log(f"Iteration {iteration + 1} started")

            for agent in self.agents:
                if iteration > 0 and agent.name == "Researcher":
                    continue

                self.log(f"Running {agent.name}...")
                state = agent.run(state)

                if agent.name == "Critic":
                    critique = state.get("critique", "").lower()

                    if self._needs_improvement(critique):
                        self.log("Critique suggests improvement")

                        analyzer = self._get_agent("Analyzer")
                        if analyzer:
                            self.log("Re-running Analyzer...")
                            state = analyzer.run(state)

                        iteration += 1
                        break
            else:
                self.log("No improvements needed")
                break

        #  Run Writer at end
        writer = self._get_agent("Writer")
        if writer:
            self.log("Running Writer for final output...")
            state = writer.run(state)

        self.log("Workflow completed")
        return state

    # ------------------------
    def _needs_improvement(self, critique):
        keywords = ["improve", "more", "better", "lack", "missing"]
        return any(word in critique for word in keywords)

    def _get_agent(self, name):
        for agent in self.agents:
            if agent.name == name:
                return agent
        return None