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

class CustomData:
    def __init__(self , carat , depth , table , x,y,z,cut,color,clarity):
        self.carat = carat
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y 
        self.z = z
        self.cut = cut
        self.color = color 
        self.clarity = clarity
    
    def get_data_as_dataframe(self):
        
        return pd.DataFrame({
            'carat' : self.carat , 
            'depth' : self.depth , 
            'table' : self.table ,
            'x' : self.x ,
            'y' : self.y , 
            'z' : self.z , 
            'cut' : self.cut , 
            'color' : self.color , 
            'clarity' : self.clarity
        } , index = [0])