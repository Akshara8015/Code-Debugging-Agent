def validate_code(code):

    try:
        # local scope for execution
        local_env = {}

        exec(code, {}, local_env)

        # Check if function exists
        if "square" not in local_env:
            return False, "Function 'square' not found"

        func = local_env["square"]

        # Test cases
        if func(2) != 4:
            return False, "Test failed: square(2) != 4"

        if func(3) != 9:
            return False, "Test failed: square(3) != 9"

        return True, "All tests passed"

    except Exception as e:
        return False, str(e)
    