
from langgraph.graph import StateGraph
from graphviz import Digraph
from schema.debate_state import DebateState
from nodes.agent_node import agent_node
from nodes.memory_node import memory_node
from nodes.judge_node import judge_node

def generate_dag_diagram(output_file="dag_diagram"):
    graph = StateGraph(DebateState)
    graph.add_node("Agent", agent_node)
    graph.add_node("Memory", memory_node)
    graph.add_node("Judge", judge_node)

    graph.set_entry_point("Agent")
    graph.add_edge("Agent", "Memory")
    graph.add_edge("Memory", "Agent")
    graph.add_edge("Memory", "Judge")
    graph.set_finish_point("Judge")

    dot = Digraph(format="png")
    dot.attr(rankdir="LR")

    dot.node("Agent", "Agent")
    dot.node("Memory", "Memory")
    dot.node("Judge", "Judge")

    dot.edge("Agent", "Memory")
    dot.edge("Memory", "Agent")
    dot.edge("Memory", "Judge")

    dot.render(filename=output_file, cleanup=True)
    print(f" DAG diagram saved as {output_file}.png")