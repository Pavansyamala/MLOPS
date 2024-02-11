import pandas as pd 
import sys
import os 
import numpy as np 
from src.logger.logging import logging 
from src.exception.exception import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path 

from src.components.dataingestion import DataIngestion
from src.components.datatransformation import DataTransformation
from src.utils.utils import save_object , evaluate_model
from sklearn.linear_model import LinearRegression , Ridge , Lasso 

@dataclass
class ModelTrainerConfig:
    def __init__(self):
        self.model_path = os.path.join("artifacts" , "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self , train_array , test_array):
        try :
            logging.info("Model Training Started ") 
            x_train , y_train = train_array[:,:-1] , train_array[:,-1]
            x_test , y_test = test_array[:,:-1] , test_array[:,-1]

            models = {
                'LinearRegression' : LinearRegression(),
                'Lasso' : Lasso(),
                'Ridge' : Ridge()
            }

            report  = evaluate_model(x_train,y_train,x_test,y_test , models) 

            logging.info("Model Training Completed")

            best_score = -1*10**9 
            best_model = 'LinearRegression'
            for key , val in report.items():
                logging.info(f"Model {key} is having r2_score as {val}")
                if val > best_score :
                    best_score = val 
                    best_model = key 
            
            logging.info(f"Selected Best Model Found with the Score {best_score} and the model name is {best_model}") 

            save_object(self.model_config.model_path , models[best_model])

            logging.info("Succesfully Saved Best Model")

        except Exception as e :
            logging.info(e)
            raise CustomException(e , sys)

if __name__ == "__main__" :
    obj = DataIngestion()
    train_path , test_path = obj.initiate_data_ingestion()
    obj1 = DataTransformation()
    train_arr , test_arr = obj1.initiate_data_transformation(train_path , test_path) 
    obj3 = ModelTrainer()
    obj3.initiate_model_trainer(train_arr,test_arr)