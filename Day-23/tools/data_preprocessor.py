from tools.logger import log_info


def preprocess_data(df):
    """
    Basic preprocessing (can expand later)
    """

    log_info(" Preprocessing data")

    # Example: fill missing values
    df = df.fillna(0)

    return df