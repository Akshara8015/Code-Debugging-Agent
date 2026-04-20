import ollama
# from tools.analyzer import analyze_error
# from tools.runner import run_code

def fix_code(problem_statement, code, error, analysis):

    prompt = f"""
                    You are an expert Python debugger and code repair assistant.

                    Your task is to fix the given Python code using:
                    1. the runtime error,
                    2. the analysis,
                    3. the problem statement.

                    You must preserve the user's original intent as much as possible.

                    Problem Statement:
                    {problem_statement}

                    Code:
                    {code}

                    Error:
                    {error}

                    Analysis:
                    {analysis}

                    Strict Rules:

                    1. Preserve original logic whenever possible.
                    2. Only modify parts required to fix:
                    - syntax errors
                    - runtime errors
                    - indentation issues
                    - missing imports
                    - variable initialization
                    - wrong function/return usage
                    - minor logical mistakes that conflict with the problem statement
                    3. If a variable is used before initialization:
                    - initialize it with a safe default value
                    - do not remove the variable
                    - do not unnecessarily rewrite code structure
                    4. If indentation is broken, correct indentation properly.
                    5. If imports are missing, add required standard Python imports.
                    6. If input/output handling is broken, repair it while preserving expected behavior.
                    7. If loops or recursion can crash due to obvious base-case/index issues, fix minimally.
                    8. If logic conflicts with the Problem Statement, prioritize the Problem Statement.
                    9. Do not rename variables/functions unless absolutely necessary.
                    10. Do not remove useful code unless it is clearly invalid.
                    11. Do not add comments, explanations, markdown, or text outside code.
                    12. Return ONLY corrected executable Python code.
                    13. Ensure final code runs without errors.
                    14. Prefer minimal edits over complete rewrites.
                    15. If multiple fixes are possible, choose the simplest correct fix.

                    Output:
                    ONLY the corrected Python code.
            """

    response = ollama.chat(
        model="mistral",  
        messages=[{"role": "user", "content": prompt}]
    )

    fixed_code = response["message"]["content"]

    return fixed_code.strip()

# debug_code = """def add(a,b): 
# return a-b"""

# problem_statement = "Return sum of two numbers"

# # code = """print(i)"""

# result = run_code(debug_code)
# print(result, "\n")

# error = result["error"]
# error_analyse = analyze_error(error)
# print(error_analyse, "\n")

# corrected_code = fix_code(problem_statement, debug_code, error, error_analyse)
# print(corrected_code)
