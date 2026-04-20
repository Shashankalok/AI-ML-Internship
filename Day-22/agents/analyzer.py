from agents.base_agent import BaseAgent
from tools.summarizer import summarize_text


class AnalyzerAgent(BaseAgent):
    def run(self, state):
        research_data = state.get("research", "")
        critique = state.get("critique", "")

        self.log("Analyzing research data...")

        #  If critique exists → improve using feedback
        if critique:
            prompt = f"""
            Improve the following analysis based on the feedback.

            Research Data:
            {research_data}

            Feedback:
            {critique}

            Provide a better, more detailed analysis.
            """
        else:
            prompt = research_data

        summary = summarize_text(prompt)

        state["analysis"] = summary

        self.log("Analysis completed")

        return state