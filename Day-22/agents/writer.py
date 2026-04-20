from agents.base_agent import BaseAgent
from tools.writer_tool import generate_report


class WriterAgent(BaseAgent):
    def run(self, state):
        self.log("Generating final report...")

        report = generate_report(state)

        state["final_output"] = report

        self.log("Report generated")

        return state