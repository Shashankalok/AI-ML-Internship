def calculator_basic(expression: str):
    """
    Basic calculator that evaluates simple expressions like '2+2'
    """
    try:
        result = eval(expression)
        return str(result)
    except Exception:
        return "error"