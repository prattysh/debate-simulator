def is_turn_valid(state):
    if state.last_speaker == "Agent A":
        return True 
    elif state.last_speaker == "Agent B":
        return True 
    else:
        return True  
def is_round_valid(state, max_rounds=8):
    return state.round <= max_rounds

