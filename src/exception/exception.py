import sys
import os

class CustomException(Exception):

    def __init__(self , error_message , error_detail:sys):
        self.error_message = error_message
        _ , _ , exc_tb = error_detail.exc_info()
        print(type_e)
        self.line_no = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename
    
    def __str__(self):
        return f"Error Occured in the file {self.filename} line number {self.line_no} and error message is {self.error_message}"

if __name__ == '__main__':
    try :
        a = 1/0 
    except Exception as e :
        raise CustomException(e , sys)