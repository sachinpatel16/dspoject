from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_intestion import DataIngestion


import sys


if __name__=="__main__":
    logging.info("The execution has started")

    try:
        #data_ingestion_config=DataIngestionConfig()
        data_intestion=DataIngestion()
        data_intestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)