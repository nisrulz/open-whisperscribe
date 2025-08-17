import logging
from src.constants import LOG_FILE, LOG_LEVEL

logging.basicConfig(
    filename=LOG_FILE,
    level=LOG_LEVEL,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

