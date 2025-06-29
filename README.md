# AI Debate Simulator 

This project is an **AI Debate Simulator** built using [LangGraph](https://github.com/langchain-ai/langgraph) and [Together.ai](https://www.together.ai/). It enables two AI agents to engage in a multi-round debate on any given topic, while a Judge node evaluates their arguments and produces a final judgment.

---

## Features

- Multi-agent debate simulation on dynamic user-provided topics
- Customizable agent roles for realistic debate personas
- Automatic memory tracking of all arguments
- Intelligent judgment by LLM after debate rounds
- Fully modular architecture with LangGraph DAG
- User-friendly command-line interface

---

## Project Structure

```
debate_LLM/
├── main.py                     # Entry point for running the debate CLI
├── .env                        # Contains TOGETHER_API_KEY
├── schema/
│   └── debate_state.py         # Defines the state of the debate
├── nodes/
│   ├── agent_node.py           # Generates arguments for agents
│   ├── memory_node.py          # Manages debate flow, turn logic, and memory
│   └── judge_node.py           # Uses LLM to evaluate the final arguments
├── utils/
│   ├── logger.py               # Logs outputs to text file
│   ├── dag_diagram.py          # Visualizes the LangGraph flow
│   └── state_validator.py      # Ensures debate turn and round correctness
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/debate_LLM.git
cd debate_LLM
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Key
Create a `.env` file:
```
TOGETHER_API_KEY=your_together_api_key_here
```

> You can get a free API key at [https://together.ai](https://together.ai)

---

## How to Run

```bash
python main.py
```

You will be prompted to:

- Enter the debate topic  
- Assign roles to Agent A and Agent B  
- Watch the AI agents argue their positions  
- View the Judge’s final verdict

---

## Demo Video

 Watch the full project walkthrough:  
 

---

## Example

```
Topic: Should tourism be allowed in North Korea?
Agent A: International Relations Professor
Agent B: Human Rights Activist
```

---

## Author

**Pratyush Sharma**  