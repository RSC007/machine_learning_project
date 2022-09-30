
import json
import sys, os
from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
import pandas as pd
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab

import logging
from housing.constant import *
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from housing.exception import HousingException


class DataValidation:

    def __init__(self, validation_config: DataValidationConfig,
        data_ingestion_artifact: DataIngestionArtifact) -> None:
        try:
            self.data_validation_congif = validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise HousingException(e, sys) from e


    def is_train_test_file_exists(self) -> bool:
        try:
            logging.info("Checking is training and test file is available")
            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path= self.data_ingestion_artifact.test_file_path
            if (os.path.exists(train_file_path) and os.path.exists(test_file_path)):
                return True
            else:
                error_message=f"Training File: {train_file_path} or Test file: {test_file_path} is not present"
                raise Exception(error_message)
        except Exception as e:
            raise HousingException(e, sys)

    def validate_dataset_schema(self):
        try:
            # do it leter
            validation_status = True
            return validation_status
        except Exception as e:
            raise HousingException(e,sys) from e

    def get_train_test_df(self):
        try:
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path) 
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            return train_df, test_df
        except Exception as e:
            raise HousingException(e, sys) from e

    def get_and_save_data_drift_report(self):
        try:
            logging.info(f"Get and save the data drift report.")
            profile = Profile(sections=[DataDriftProfileSection()])

            train_df, test_df = self.get_train_test_df()

            profile.calculate(train_df, test_df)
            
            report = json.loads(profile.json())

            report_file_path = self.data_validation_congif.report_file_path
            report_dir = os.path.dirname(report_file_path)
            os.makedirs(report_dir, exist_ok=True)

            with open(report_file_path, 'w') as write_report_file:
                json.dump(report, write_report_file, indent=6)
            return report
        except Exception as e:
            raise HousingException(e, sys) from e

    def save_data_drift_report_page(self):
        try:
            logging.info(f"Save the data drift report page.")
            dashboard = Dashboard(tabs=[DataDriftTab()])
            train_df, test_df = self.get_train_test_df()
            dashboard.calculate(train_df, test_df)

            report_page_file_path = self.data_validation_congif.report_page_file_path
            report_page_dir = os.path.dirname(report_page_file_path)
            os.makedirs(report_page_dir, exist_ok=True)

            dashboard.save(report_page_file_path)
        except Exception as e:
            raise HousingException(e, sys) from e

    def is_data_drift_found(self):
        try:
            report = self.get_and_save_data_drift_report()
            self.save_data_drift_report_page()
        except Exception as e:
            raise HousingException(e, sys) from e

    def initiate_data_validation(self) -> DataValidationConfig:
        try:
            self.is_train_test_file_exists()
            self.validate_dataset_schema()
            self.is_data_drift_found()

            data_validation_artifact=DataValidationArtifact(
                schema_file_path=self.data_validation_congif.schema_file_path,
                report_file_path=self.data_validation_congif.report_file_path,
                report_page_file_path=self.data_validation_congif.report_page_file_path,
                is_validated=True,
                message="Data Validation is completed"              
            )
            logging.info(f"{'='*20} Data Validation log is complete. {'='*20}")
            return data_validation_artifact
        except Exception as e:
            HousingException(e, sys)