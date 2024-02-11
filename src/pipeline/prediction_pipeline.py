import os 
import sys 
import pandas as pd 

from src.utils.utils import load_object 
from src.logger.logging import logging
from src.exception.exception import CustomException

class PredictPipeline:
    def __init__(self):
        logging.info("Prediction Pipeline Started")
    
    def predict(self , features):
        try : 
            model = load_object(os.path.join("artifacts" , "model.pkl"))
            preprocessor = load_object(os.path.join("artifacts" , "preprocessor.pkl"))

            logging.info("Prediction on the features started")
            transformed_features = preprocessor.transform(features)

            self.prediction = model.predict(transformed_features)
            logging.info("Prediction Completed")

            return self.prediction
        
        except Exception as e :
            logging.info(e)
            raise CustomException(e , sys)