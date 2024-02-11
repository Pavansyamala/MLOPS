import pandas as pd 
import os 
import sys
import numpy as np 
from src.logger.logging import logging 
from src.exception.exception import CustomException
from src.components.dataingestion import DataIngestion
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
        self.preprocessor_obj = os.path.join("artifacts" , "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.transformation_config = DataTransformationConfig()
    
    def get_data_transformation(self):
        try :
            categorical_cols = ['cut', 'color','clarity']
            numerical_cols = ['carat', 'depth','table', 'x', 'y', 'z']
            
            # Define the custom ranking for each ordinal variable
            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF'] 

            logging.info('Pipeline Initiated')
            
            ## Numerical Pipeline
            num_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy="median")),
                ('scaler',StandardScaler())
                ]
            )

            # Categorigal Pipeline
            cat_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('ordinalencoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                ('scaler',StandardScaler())
                ]
            )
            
            preprocessor=ColumnTransformer([
            ('num_pipeline',num_pipeline,numerical_cols),
            ('cat_pipeline',cat_pipeline,categorical_cols)
            ])
            
            return preprocessor

        except Exception as e :
            logging.info(e)
            raise CustomException(e , sys)
    
    def initiate_data_transformation(self , train_path , test_path) :

        try :
            logging.info("Data Transformation started")
            logging.info("Reading of Training and Testing Data Started")
            self.train_data = pd.read_csv(train_path)
            self.test_data = pd.read_csv(test_path)
            logging.info("Succesfully Readed Training and Testing Data ")

            preprocessing_obj = self.get_data_transformation() 

            target_column_name = 'price'
            drop_columns = [target_column_name]
            
            input_feature_train_df = self.train_data.drop(columns=drop_columns,axis=1)
            target_feature_train_df=self.train_data[target_column_name]

            input_feature_test_df = self.test_data.drop(columns=drop_columns,axis=1)
            target_feature_test_df=self.test_data[target_column_name] 

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)
            
            logging.info("Applying preprocessing object on training and testing datasets.")
            
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            save_object(
                file_path=self.transformation_config.preprocessor_obj,
                obj=preprocessing_obj
            )
            
            logging.info("preprocessing pickle file saved")
            
            logging.info("preprocessing pickle file saved")
            
            return (
                train_arr,
                test_arr
            )
        
        except Exception as e :
            logging.info(e)
            raise CustomException(e , sys)


if __name__ == "__main__" :
    obj = DataIngestion()
    train_path , test_path = obj.initiate_data_ingestion()
    obj1 = DataTransformation()
    obj1.initiate_data_transformation(train_path , test_path) 