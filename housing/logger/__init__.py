import logging
from datetime import datetime
import os

LOGS_DIR = "housing_logs"

# Get current timestamp
CURRENT_TIME_STAMP = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Construct log file name
LOG_FILE_NAME = f"log_{CURRENT_TIME_STAMP}.log"

# Ensure logs directory exists
os.makedirs(LOGS_DIR, exist_ok=True)

# Construct full log file path
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE_NAME)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode="a",  # Append mode to avoid overwriting log files
    format='[%(asctime)s %(name)s - %(levelname)s - %(message)s]',
    level=logging.INFO  # Set logging level to INFO
)
