from tools.data_loader import load_data
from tools.logger import log_info, log_error


def researcher(state):
    """
    Researcher Agent:
    Responsible for loading and validating dataset
    """

    try:
        # Get file path from state
        file_path = state.get("file_path")

        if not file_path:
            raise ValueError(" File path not provided in state")

        log_info(f"📥 Loading dataset from: {file_path}")

        # Load dataset
        df = load_data(file_path)

        log_info(f" Dataset loaded successfully with {len(df)} rows")

        return {
            "data": df,
            "status": "data_loaded"
        }

    except Exception as e:
        log_error(f" Researcher Agent Error: {str(e)}")

        return {
            "status": "error",
            "message": str(e)
        }