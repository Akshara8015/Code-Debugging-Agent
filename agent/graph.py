from langgraph.graph import StateGraph, END
from agent.state import DebugState
from agent.nodes import run_node, analyze_node, fix_node, should_continue

builder = StateGraph(DebugState)

# Add nodes
builder.add_node("run", run_node)
builder.add_node("analyze", analyze_node)
builder.add_node("fix", fix_node)

builder.set_entry_point("run")
builder.add_conditional_edges(
    "run",
    should_continue,
    {
        "fix code": "analyze",
        "end": END
    }
)
builder.add_edge("analyze", "fix")
builder.add_edge("fix", "run")

graph = builder.compile()
