from agents.base_agent import BaseAgent
from tools.critic_tool import evaluate_text


class CriticAgent(BaseAgent):
    def run(self, state):
        analysis = state.get("analysis", "")

        self.log("Evaluating analysis...")

        feedback = evaluate_text(analysis)

        # Update state
        state["critique"] = feedback

        self.log("Critique completed")

        return state