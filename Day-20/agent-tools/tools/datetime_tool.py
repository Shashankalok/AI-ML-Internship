from datetime import datetime, timedelta
from langchain.tools import tool

@tool
def get_current_datetime() -> str:
    """Returns the current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@tool
def calculate_date(days: int) -> str:
    """
    Adds or subtracts days from current date.
    Positive = future, Negative = past
    """
    try:
        new_date = datetime.now() + timedelta(days=days)
        return new_date.strftime("%Y-%m-%d")
    except Exception as e:
        return f"Error: {str(e)}"