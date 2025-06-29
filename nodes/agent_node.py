import os
from langchain_together import Together
from dotenv import load_dotenv

load_dotenv()

def agent_node(state):
    llm = Together(
        model="mistralai/Mistral-7B-Instruct-v0.1",
        temperature=0.7,
        max_tokens=512,
        together_api_key=os.getenv("TOGETHER_API_KEY")
    )

    role = "Agent A" if state.last_speaker != "Agent A" else "Agent B"
    agent_key = "agent_a_history" if role == "Agent A" else "agent_b_history"

    context = "\n".join(state.memory[-4:])
    prompt = (
        f"You are {role} ({getattr(state, 'agent_a' if role == 'Agent A' else 'agent_b')}).\n"
        f"Debate Topic: {state.topic}\n"
        f"Previous arguments:\n{context}\n"
        "Make your argument."
    )

    argument = llm.invoke(prompt).strip()
    round_number = state.round

    print(f"{role} (Round {round_number}): {argument}")

    updated_fields = {
        agent_key: getattr(state, agent_key) + [argument],
        "memory": state.memory + [f"[Round {round_number}] {role}: {argument}"],
        "last_speaker": role,
    }

    return {
        "next": "Memory",
        **updated_fields
    }
