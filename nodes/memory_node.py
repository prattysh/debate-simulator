def memory_node(state):
    current_round = state.round
    next_round = current_round + 1

    if next_round > state.max_rounds:
        return {
            "terminated": True,
            "next": "judge",
            "round": current_round
        }

    return {
        "round": next_round,
        "next": "agent",
        "terminated": False
    }
