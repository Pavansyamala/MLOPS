import pandas as pd 
import sys
import numpy as np 
from src.logger.logging import logging 
from src.exception.exception import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path 

from src.utils.utils import evaluate_model

@dataclass
class ModelEvaluvationConfig:
    def __init__(self):
        pass 

class ModelEvaluation:
    def __init__(self):
        pass 
    
    def initiate_model_evaluvation(self):
        try :
            pass 
        except Exception as e :
            logging.info(e)
            raise CustomException(e , sys)