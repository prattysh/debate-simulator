# nodes/judge_node.py

import os
import time
from langchain_together import Together
from dotenv import load_dotenv

load_dotenv()  

def judge_node(state):
    time.sleep(15)
    llm = Together(
        model="mistralai/Mistral-7B-Instruct-v0.1",
        temperature=0.3,
        max_tokens=512,
        together_api_key=os.getenv("TOGETHER_API_KEY")
    )

    print(f"\n Round: {state.round}")


    full_debate = "\n".join(state.memory)

    prompt = f"""The following is a debate between two participants.

Topic: {state.topic}

{full_debate}

Based on the arguments presented, who made a more compelling case and why? Please provide a concise and clear explanation.
"""

    judgment = llm.invoke(prompt).strip()

    
    print("-" * 60)
    print(judgment)
    print("-" * 60)

    return {
        "next": None,
        "round": state.round,
        "final_judgment": judgment,
        "terminated": True,
        "judge_runs": state.judge_runs + 1
    }
