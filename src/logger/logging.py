import logging 
import os
from datetime import datetime 

LOG_PATH = f'{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log'
log_path = os.path.join(os.getcwd() , 'logs')
os.makedirs(log_path , exist_ok = True)
logs_path = os.path.join(log_path , LOG_PATH)

logging.basicConfig(
    level = logging.INFO ,
    filename = logs_path ,
    format = '%(asctime)s %(lineno)d %(name)s %(levelname)s %(message)s'
)
