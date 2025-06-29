from typing import List, Optional, Annotated
from pydantic import BaseModel, Field

class DebateState(BaseModel):
    topic: Annotated[str, Field(metadata={"readonly": True})]
    agent_a: Annotated[str, Field(metadata={"readonly": True})]
    agent_b: Annotated[str, Field(metadata={"readonly": True})]

    round: Annotated[int, Field(default=1, metadata={"write": True})]
    max_rounds: Annotated[int, Field(default=8, metadata={"write": True})] 

    memory: Annotated[List[str], Field(default_factory=list, metadata={"write": True})]
    last_speaker: Annotated[Optional[str], Field(default=None, metadata={"write": True})]
    agent_a_history: Annotated[List[str], Field(default_factory=list, metadata={"write": True})]
    agent_b_history: Annotated[List[str], Field(default_factory=list, metadata={"write": True})]
    final_judgment: Annotated[Optional[str], Field(default=None, metadata={"write": True})]
    terminated: Annotated[bool, Field(default=False, metadata={"write": True})]
    judge_runs: Annotated[int, Field(default=0, metadata={"write": True})]
