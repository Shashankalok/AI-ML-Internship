import pandas as pd
from utils.validators import validate_dataset
from tools.logger import log_info, log_error


def load_data(file_path):
    """
    Loads and validates dataset
    """

    try:
        log_info(f" Reading dataset: {file_path}")

        df = pd.read_csv(file_path)

        # Normalize column names
        df.columns = df.columns.str.lower()

        # Validate dataset
        valid, message = validate_dataset(df)

        if not valid:
            raise ValueError(message)

        log_info(" Dataset validated successfully")

        return df

    except Exception as e:
        log_error(f" Data loading error: {str(e)}")
        raise e