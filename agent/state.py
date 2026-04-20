from typing import TypedDict

class DebugState(TypedDict):
    code: str
    error: str
    analysis: str
    problem_statement: str
    iteration: int
    problem_id: str

