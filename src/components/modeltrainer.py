import pandas as pd 
import sys
import os 
import numpy as np 
from src.logger.logging import logging 
from src.exception.exception import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path 
import mlflow 
import mlflow.sklearn 
from mlflow.models import infer_signature
from urllib.parse import urlparse

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

            mlflow.set_registry_uri("")
            tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme

            mlflow.set_experiment("MLflow Quickstart")

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

            with mlflow.start_run():
                mlflow.log_metric("accuracy", best_score)
                mlflow.set_tag("Training Info", "Basic LinearRegression model")
                params = {
                    'learning_rate' : 0.01 
                }
                mlflow.log_params(params) 
                signature = infer_signature(x_train, models[best_model].predict(x_train))
                model_info = mlflow.sklearn.log_model(
                        sk_model=models[best_model],
                        artifact_path="Dimond_Price_Prediction",
                        signature=signature,
                        input_example=x_train,
                        registered_model_name="tracking-quickstart",
                    )

        except Exception as e :
            logging.info(e)
            raise CustomException(e , sys)

