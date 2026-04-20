from tools.analyzer import analyze_error
from tools.code_fix import fix_code
from tools.runner import run_code
from tools.database import insert_code, get_recent_attempts

def run_node(state):
    result = run_code(state["code"])
    return {
        "error": result["error"]
    }

def analyze_node(state):
    analysis = analyze_error(state["error"])
    print(analysis)
    return {"analysis": analysis}

def fix_node(state):

    memory = get_recent_attempts(state["problem_id"], limit=3)
    memory_context = "\n".join([
        f"Code: {m['code']}\nError: {m['error']}\nAnalysis: {m['analysis']}"
        for m in memory
    ])

    new_code = fix_code(
        state["problem_statement"],
        state["code"],
        state["error"],
        f"{state['analysis']}\n\nPrevious attempts:\n{memory_context}"
    )

    insert_code(
        state["problem_id"],
        state["code"],
        state["problem_statement"],
        state["error"],
        state["analysis"],
        state["iteration"]
    )

    return {
        "code": new_code,
        "iteration": state["iteration"] + 1
    }

def should_continue(state):
    if state["error"] == "" or state["iteration"] > 5:
        return "end"
    return "fix code"
