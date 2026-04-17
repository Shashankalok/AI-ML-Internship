import streamlit as st

from agents.researcher import ResearcherAgent
from agents.analyzer import AnalyzerAgent
from agents.critic import CriticAgent
from agents.writer import WriterAgent
from agents.coordinator import CoordinatorAgent

# Page configration
st.set_page_config(page_title="AI Research Assistant", layout="wide")

st.title(" Multi-Agent Research Assistant")
st.write("Enter a topic and generate an research report.")

# Input
query = st.text_input("Enter your research topic:")

if st.button("Generate Report"):
    if query:
        with st.spinner("Running multi-agent system..."):

            # Initialize state
            state = {"query": query}

            # Create agents
            researcher = ResearcherAgent("Researcher")
            analyzer = AnalyzerAgent("Analyzer")
            critic = CriticAgent("Critic")
            writer = WriterAgent("Writer")

            coordinator = CoordinatorAgent(
                "Coordinator",
                agents=[researcher, analyzer, critic, writer]
            )

            # Run system
            state = coordinator.run(state)

        st.success("Report Generated!")

        # Output
        st.subheader("📄 Final Report")
        st.write(state.get("final_output", "No output generated"))

    else:
        st.warning("Please enter a query.")