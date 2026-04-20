def analyze_error(error_msg):

    if not error_msg:
        return "No error"

    if "NameError" in error_msg:
        return "Variable not defined"

    elif "SyntaxError" in error_msg:
        return "There is a syntax error in the code"

    elif "TypeError" in error_msg:
        return "Operation applied to wrong data type"

    elif "IndexError" in error_msg:
        return "Index out of range"

    elif "ZeroDivisionError" in error_msg:
        return "Division by zero"

    elif "IndentationError" in error_msg:
        return "Incorrect indentation"

    else:
        return error_msg
    
