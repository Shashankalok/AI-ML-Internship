import logging
import os
from config import Config


def setup_logger():
    # Ensure logs directory exists
    log_path = Config.LOG_FILE
    log_dir = os.path.dirname(log_path)

    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


def log_info(message):
    logging.info(message)


def log_error(message):
    logging.error(message)