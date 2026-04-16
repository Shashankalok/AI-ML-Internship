from langchain.tools import tool
import pandas as pd

@tool
def read_text_file(file_path: str) -> str:
    """
    Reads a text file and returns its content.
    Provide full file path.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"


@tool
def read_csv_file(file_path: str) -> str:
    """
    Reads a CSV file and returns first 5 rows.
    Provide full file path.
    """
    try:
        df = pd.read_csv(file_path, encoding='latin1', on_bad_lines='skip')
        return df.head().to_string()
    except Exception as e:
        return f"Error reading CSV: {str(e)}"