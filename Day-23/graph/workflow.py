from langgraph.graph import StateGraph, END

from graph.state import AgentState
from graph.routing import route_after_critic

# Agents
from agents.researcher import researcher
from agents.analyzer import analyzer
from agents.critic import critic
from agents.writer import generate_report

from tools.logger import log_info


def build_graph():
    """
    Builds the multi-agent fraud intelligence workflow

    Flow:
    researcher → analyzer → critic → (retry OR writer) → END
    """

    log_info(" Building workflow graph")

    graph = StateGraph(AgentState)


    # Agents
    graph.add_node("researcher", researcher)
    graph.add_node("analyzer", analyzer)
    graph.add_node("critic", critic)
    graph.add_node("writer", generate_report)

    
    #  Entry Point
    
    graph.set_entry_point("researcher")

    
    #  Linear Flow
    
    graph.add_edge("researcher", "analyzer")
    graph.add_edge("analyzer", "critic")

    
    #  Conditional Routing (Critic)
    # Prevents infinite loops via retry control
    graph.add_conditional_edges(
        "critic",
        route_after_critic
    )

    #  End Node
    
    graph.add_edge("writer", END)

    
    #  Compile Graph
    
    app = graph.compile()

    log_info(" Workflow graph compiled successfully")

    return app