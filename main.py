from agent.graph import graph
from tools.database import init_db
import uuid

init_db()

debug_code = """def add(a,b): 
return a-b"""

problem_statement = "Return sum of two numbers"

initial_state = {
    "code": debug_code,
    "error": "",
    "analysis": "",
    "problem_statement" : "",
    "iteration": 0,
    "problem_id": str(uuid.uuid4())
}

result = graph.invoke(initial_state)

print("Final Code:\n", result["code"])
