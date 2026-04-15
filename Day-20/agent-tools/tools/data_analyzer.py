from langchain.tools import tool
import pandas as pd

@tool
def analyze_data(file_path: str) -> str:
    """
    Analyze a dataset and return summary statistics.
    Input should be a CSV file path.
    """
    try:
        # Robust reading (handles encoding issues)
        df = pd.read_csv(
            file_path,
            encoding='latin1',   # most compatible
            on_bad_lines='skip'  # skip corrupted rows
        )

        summary = df.describe(include='all').to_string()
        columns = list(df.columns)
        missing = df.isnull().sum().to_string()

        return f"""
Columns:
{columns}

Summary Statistics:
{summary}

Missing Values:
{missing}
"""
    except Exception as e:
        return f"Error analyzing data: {str(e)}"