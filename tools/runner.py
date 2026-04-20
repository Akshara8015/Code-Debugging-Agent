import subprocess

def run_code_logic(file_path="temp/code.py"):
    try:
        result = subprocess.run(
            ["python", file_path],
            capture_output=True,   # capture stdout + stderr
            text=True,             # return as string (not bytes)
            timeout=5              # prevent infinite loops
        )

        return {
            "output": result.stdout.strip(),
            "error": result.stderr.strip(),
            "success": result.returncode == 0
        }

    except subprocess.TimeoutExpired:
        return {
            "output": "",
            "error": "Time Limit Exceed",
            "success": False
        }

    except Exception as e:
        return {
            "output": "",
            "error": str(e),
            "success": False
        }

def run_code(code):
    file_path = "tools/code.py"
    # code = code.strip()
    with open(file_path, "w") as f:
        f.write(code)
    return run_code_logic(file_path)

