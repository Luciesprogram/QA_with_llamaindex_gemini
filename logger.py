from datetime import datetime
import os
import logging

LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILEPATH = os.path.join(LOG_DIR, LOG_FILE)

logger = logging.getLogger()          # root logger
logger.setLevel(logging.INFO)

# Prevent duplicate handlers
if not logger.handlers:
    file_handler = logging.FileHandler(LOG_FILEPATH)
    formatter = logging.Formatter(
        "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
