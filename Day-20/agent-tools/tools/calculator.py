from langchain.tools import tool
import math

# 1. Calculator (Structured Input)
@tool
def calculator_basic(operation: str, a: float, b: float) -> str:
    """
    Perform basic arithmetic operations.

    Parameters:
    - operation: add, subtract, multiply, divide
    - a: first number
    - b: second number
    """

    try:
        if operation == "add":
            result = a + b

        elif operation == "subtract":
            result = a - b

        elif operation == "multiply":
            result = a * b

        elif operation == "divide":
            if b == 0:
                return "Error: Division by zero"
            result = a / b

        else:
            return "Error: Invalid operation"

        return f"Result: {result}"

    except Exception as e:
        return f"Error: {str(e)}"


#  2. Advanced Calculator (Expression Based - LLM Friendly)
@tool
def calculator_expression(expression: str) -> str:
    """
    Evaluate a mathematical expression.
    Example: '2 + 3 * 4', 'sqrt(16)'
    """

    try:
        allowed_names = {
            "sqrt": math.sqrt,
            "pow": pow,
            "abs": abs,
            "round": round
        }

        result = eval(expression, {"__builtins__": None}, allowed_names)

        return f"Result: {result}"

    except Exception as e:
        return f"Error: Invalid expression ({str(e)})"