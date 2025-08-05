import os
import logging
import sys
from datetime import datetime

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

LOG_DIR = "logs"
LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
MAX_LOG_SIZE = 5 * 1024 * 1024 
BACKUP_COUNT = 3 # Numbers of backup log files to keep

LOG_FILEPATH = os.path.join(LOG_DIR,LOG_FILE)
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format= logging_str,

    handlers= [
        logging.FileHandler(LOG_FILEPATH),
        logging.StreamHandler(sys.stdout)
    ]
) 

logger = logging.getLogger("cnnClassifierLogger")

 