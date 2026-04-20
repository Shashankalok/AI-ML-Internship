import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """
    Central configuration for the fraud intelligence system
    """

    # -----------------------------
    #  Data Configuration
    # -----------------------------
    DATA_PATH = os.getenv(
        "DATA_PATH",
        r"C:\Users\User\Desktop\vccodepy\Day-23\data\sample\creditcard.csv"
    )

    # -----------------------------
    #  Model Configuration
    # -----------------------------
    CONTAMINATION = float(os.getenv("CONTAMINATION", 0.002))
    RANDOM_STATE = int(os.getenv("RANDOM_STATE", 42))

    # -----------------------------
    #  Risk Thresholds
    # -----------------------------
    HIGH_RISK_THRESHOLD = int(os.getenv("HIGH_RISK_THRESHOLD", 70))
    MEDIUM_RISK_THRESHOLD = int(os.getenv("MEDIUM_RISK_THRESHOLD", 40))

    # -----------------------------
    #  System Controls
    # -----------------------------
    MAX_RETRIES = int(os.getenv("MAX_RETRIES", 2))

    # -----------------------------
    #  Logging
    # -----------------------------
    import os

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    LOG_FILE = os.path.join(BASE_DIR, "logs", "system.log")