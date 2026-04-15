from langchain.tools import tool

@tool
def calculator(expression: str) -> str:
    """Performs basic math calculations"""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {str(e)}"