import sys
import os

from housing.constant import *
from housing.exception import HousingException
from housing.logger import logging
from housing.util.util import read_yaml_file
from housing.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig


class Configuration:
    def __init__(self, config_file_path: str = CONFIG_FILE_PATH, time_stamp: str = CURRENT_TIME_STAMP) -> None:
        try:
            self.config = read_yaml_file(config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = time_stamp
        except Exception as e:
            raise HousingException(e, sys) from e

    def get_data_ingestion_config(self):
        try:
            logging.info("Data Ingestion start")
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_ingestion_artifact_dir = os.path.join(
                artifact_dir,
                DATA_INGESTION_ARTIFACT_DIR,
                self.time_stamp
            )

            data_ingestion_config = self.config[DATA_INGESTION_CONFIG_KEY]

            dataset_download_url = data_ingestion_config[DATA_INGESTION_DOWNLOAD_URL_KEY]
            tgz_download_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_config[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY]
            )

            raw_data_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_config[DATA_INGESTION_RAW_DATA_DIR_KEY]
            )

            ingestion_data_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_config[DATA_INGESTION_INGESTED_DIR_NAME_KEY]
            )

            ingested_train_dir = os.path.join(
                ingestion_data_dir,
                data_ingestion_config[DATA_INGESTION_TRAIN_DIR_KEY]
            )

            ingestion_test_dir = os.path.join(
                ingestion_data_dir,
                data_ingestion_config[DATA_INGESTION_TEST_DIR_KEY]
            )

            data_ingestion_config = DataIngestionConfig(
                dataset_download_url=dataset_download_url,
                tgz_download_dir=tgz_download_dir,
                raw_data_dir=raw_data_dir,
                ingested_train_dir=ingested_train_dir,
                ingested_test_dir=ingestion_test_dir
            )
            logging.info(f"Data Ingestion config: {data_ingestion_config}")
            return data_ingestion_config
        except Exception as e:
            raise HousingException(e, sys) from e

    def get_training_pipeline_config(self):
        try:
            training_pipeline_config = self.config[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(
                ROOT_DIR,
                training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
                training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            )

            training_pipeline_config = TrainingPipelineConfig(
                artifact_dir=artifact_dir)
            logging.info(
                f"Training Pipeline config: {training_pipeline_config}")
            return training_pipeline_config

        except Exception as e:
            raise HousingException(e, sys) from e
