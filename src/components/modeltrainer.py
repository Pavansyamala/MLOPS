import pandas as pd 
import sys
import numpy as np 
from src.logger.logging import logging 
from src.exception.exception import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path 

from src.utils.utils import save_object , evaluate_model
from sklearn.linear_model import LinearRegressio , Ridge , Lasso 

@dataclass
class ModelTrainerConfig:
    def __init__(self):
        pass 

class ModelTrainer:
    def __init__(self):
        pass 
    
    def initiate_model_trainer(self):
        try :
            a = 1/0
            pass 
        except Exception as e :
            logging.info()
            raise CustomException(e , sys)

if __name__ == "__main__" :
    obj = ModelTrainer()
    obj.initiate_model_trainer()