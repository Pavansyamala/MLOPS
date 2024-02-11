import pandas as pd 
import sys
import numpy as np 
from src.logger.logging import logging 
from src.exception.exception import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path 
import os 
import requests
from io import StringIO

@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.train_path = os.path.join("artifacts" , "train.csv")
        self.test_path = os.path.join("artifacts","test.csv")
        self.raw_path = os.path.join("artifacts" , "raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() 
    
    def initiate_data_ingestion(self):
        logging.info("Data Ingestion Started")
        try :
            url = "https://raw.githubusercontent.com/Pavansyamala/Deep-Learning/main/archive/cubic_zirconia.csv"
            response = requests.get(url)
            data = StringIO(response.text)
            logging.info("Reading Data Started")
            data = pd.read_csv(data)
            logging.info("Reading Data Completed")
            path_name = os.path.join(os.getcwd(),os.path.dirname(self.ingestion_config.raw_path))
            os.makedirs(path_name , exist_ok = True) 
            logging.info("Saving Raw Data  Started")
            data.to_csv(self.ingestion_config.raw_path)
            logging.info("Succesfully Saved Raw Data") 

            train_data , test_data = train_test_split(data , test_size = 0.2)

            logging.info("Started Saving Train and Test Data")
            train_data.to_csv(self.ingestion_config.train_path)
            test_data.to_csv(self.ingestion_config.test_path)
            logging.info("Succesfully Saved Training and Testing Data")

            logging.info("Data ingestion Completed")

            return self.ingestion_config.train_path , self.ingestion_config.test_path


        except Exception as e :
            logging.info(e)
            raise CustomException(e , sys)

if __name__ == "__main__" :
    obj = DataIngestion()
    a,b = obj.initiate_data_ingestion()
    print(a)
    print(b)