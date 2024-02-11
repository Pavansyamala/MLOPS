import pandas as pd 
import sys
import numpy as np 
from src.logger.logging import logging 
from src.exception.exception import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path 

@dataclass
class DataIngestionConfig:
    def __init__(self):
        pass 

class DataIngestion:
    def __init__(self):
        pass 
    
    def initiate_data_ingestion(self):
        try :
            pass 
        except Exception as e :
            logging.info(e)
            raise CustomException(e , sys)

if __name__ == "__main__" :
    obj = DataIngestion()
    obj.initiate_data_ingestion()