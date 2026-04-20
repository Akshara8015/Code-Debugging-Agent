from tools.runner import run_code
from tools.analyzer import analyze_error
from tools.code_fix import fix_code
from tools.database import insert_code, get_recent_attempts

def debug_agent(code, problem_id, max_iter=10):

    iteration = 0
    while iteration < max_iter:
        print(f"\n--- Iteration {iteration+1} ---")

        # Step 1: Run code
        result = run_code(code)

        # Step 2: Check success
        if result["success"]:
            print(" Code executed successfully!")
            return code

        # Step 3: Print error
        print(" Error:", result["error"])

        # Step 4: Analyze error
        analysis = analyze_error(result["error"])
        print(" Analysis:", analysis)

        insert_code(problem_id, code, result["error"], analysis, iteration)
        memory = get_recent_attempts(problem_id, limit=3)
        memory_context = "\n".join([
            f"Code: {m['code']}\nError: {m['error']}\nAnalysis: {m['analysis']}"
            for m in memory
        ])
        
        # Step 5: Fix code using LLM
        new_code = fix_code(
            code,
            result["error"],
            f"{analysis}\n\nPrevious attempts:\n{memory_context}"
        )

        print(" Fixed Code:\n", new_code)

        # Step 6: Update code
        code = new_code
        iteration += 1

    print(" Max iterations reached.")
    return code