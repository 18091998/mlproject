import logging 
import os
from datetime import datetime 
LOG_File=f"{datetime.now().strftime('%m-%d-%y_%H-%M-%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_File) 
os.makedirs(logs_path, exist_ok=True)
LOG_FILE_PATH=os.path.join(logs_path, LOG_File) 
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
) 
