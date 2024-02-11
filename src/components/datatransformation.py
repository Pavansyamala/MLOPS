import pandas as pd 
import sys
import numpy as np 
from src.logger.logging import logging 
from src.exception.exception import CustomException
from dataclasses import dataclass
from pathlib import Path 
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline 
from sklearn.preprocessing import StandardScaler , OrdinalEncoder
from sklearn.impute import SimpleImputer
from src.utils.utils import save_object

@dataclass
class DataTransformationConfig:
    def __init__(self):
        pass 

class DataTransformation:
    def __init__(self):
        pass 
    
    def initiate_data_transformation(self):
        try :
            pass 
        except Exception as e :
            logging.info(e)
            raise CustomException(e , sys)

if __name__ == "__main__" :
    obj = DataTransformation()
    obj.initiate_data_transformation() 