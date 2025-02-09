from textsummarizer.components.data_validation import DataValidation 
from textsummarizer.config.configuration import ConfigurationManager
from textsummarizer.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_validation_config()
        data_ingestion = DataValidation(config=data_ingestion_config)
        data_ingestion.validate_all_files_exist()