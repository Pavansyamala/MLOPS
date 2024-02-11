import pandas as pd
import numpy as np
import sys
import os 

from src.exception.exception import CustomException
from src.logger.logging import logging
from src.components.dataingestion import DataIngestion 
from src.components.datatransformation import DataTransformation
from src.components.modeltrainer import ModelTrainer 

try :
    logging.info(" ******* Model Training Pipeline Started *******")
    obj = DataIngestion()
    train_path , test_path = obj.initiate_data_ingestion()
    obj1 = DataTransformation()
    train_arr , test_arr = obj1.initiate_data_transformation(train_path , test_path) 
    obj3 = ModelTrainer()
    obj3.initiate_model_trainer(train_arr,test_arr) 
    logging.info(" ******* Model Training Pipeline Completed *******")
except Exception as e :
    logging,info(e)
    raise CustomException(e , sys)