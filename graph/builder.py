from langgraph.graph import StateGraph, START, END

from graph.state import UniversityState
from graph.router import intent_classifier

from agents.admission_agent import admission_agent
from agents.exam_agent import exam_agent
from agents.fees_agent import fees_agent
from agents.scholarship_agent import scholarship_agent
from agents.response_agent import response_agent
from agents.unknown_agent import unknown_agent

graph = StateGraph(UniversityState)

# Add nodes
graph.add_node("router", intent_classifier)
graph.add_node("admission", admission_agent)
graph.add_node("exam", exam_agent)
graph.add_node("fees", fees_agent)
graph.add_node("scholarship", scholarship_agent)
graph.add_node("response", response_agent)
graph.add_node("unknown", unknown_agent)

# Start → Router
graph.add_edge(START, "router")


# Function to decide the next node
def route(state: UniversityState):
    return state["intent"]


# Conditional routing
graph.add_conditional_edges(
    "router",
    route,
    {
    "admission": "admission",
    "exam": "exam",
    "fees": "fees",
    "scholarship": "scholarship",
    "unknown": "unknown",
    },
)

# Every agent ends the graph
graph.add_edge("admission", "response")
graph.add_edge("exam", "response")
graph.add_edge("fees", "response")
graph.add_edge("scholarship", "response")
graph.add_edge("unknown", "response")

graph.add_edge("response", END)

app = graph.compile()