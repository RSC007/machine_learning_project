
import logging
import sys,os
from housing.component.data_ingestion import DataIngestion

from housing.config.configuration import Configuration
from housing.exception import HousingException


class Pipeline:
    def __init__(self, config: Configuration = Configuration()) -> None:
        try:
            self.config=config
        except Exception as e:
            raise HousingException(e, sys) from e
        

    def start_data_ingestion(self):
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise HousingException(e, sys) from e

    def run_pipeline(self):
        try:
            logging.info(f"{'-'*20} Pipeline start {'-'*20}")
            data_ingestion_artifact = self.start_data_ingestion()
            logging.info(f"{'+'*40}")

        except Exception as e:
            raise HousingException(e,sys) from e