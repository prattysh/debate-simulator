import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph
from schema.debate_state import DebateState
from nodes.agent_node import agent_node
from nodes.memory_node import memory_node
from nodes.judge_node import judge_node
from utils.logger import get_logger
from utils.dag_diagram import generate_dag_diagram
from utils.state_validator import is_turn_valid, is_round_valid

load_dotenv()

logger = get_logger()

def main():
    print("\n Welcome to the AI Debate Simulator\n")

    topic = input("Enter the debate topic: ")
    agent_a = input("Enter Agent A's profession: ")
    agent_b = input("Enter Agent B's profession: ")

    
    init_state = DebateState(
        topic=topic,
        agent_a=agent_a,
        agent_b=agent_b,
        round=1,
        max_rounds=8,           
        memory=[],
        final_judgment=None,
        judge_runs=0,
        terminated=False
    )

    graph = StateGraph(DebateState)
    graph.add_node("Agent", agent_node)
    graph.add_node("Memory", memory_node)
    graph.add_node("Judge", judge_node)

    graph.set_entry_point("Agent")
    graph.add_edge("Agent", "Memory")
    graph.add_edge("Memory", "Agent")
    graph.add_edge("Memory", "Judge")
    graph.set_finish_point("Judge")

    compiled = graph.compile()

    print("\nGenerating DAG diagram...\n")
    generate_dag_diagram()

    try:
        print("\nRunning the debate...\n")
        output = compiled.invoke(init_state, config={"recursion_limit": 25})
        if output.get("terminated"):
           print("\n Debate complete!")
           print(" Final Judgment:", output.get("final_judgment"))

        logger.info("\nFinal Output:\n" + str(output))
        print("\nDebate finished! Check chat_log.txt for full transcript.")
        print("\nFinal Judgment:\n", output.final_judgment)

    except Exception as e:
        logger.error(" DAG execution failed.")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
