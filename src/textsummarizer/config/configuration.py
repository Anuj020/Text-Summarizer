from textsummarizer.constants import *
from textsummarizer.utils.common import read_yaml, create_directories
from textsummarizer.entity import DataIngestionConfig
'''
    we use constants variable and use read_yaml method 
    to read data from config.yaml 
'''
class ConfigurationManager:
    def __init__(self,
                 config_filename = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_filename)
        self.params = read_yaml(params_filepath)

        ''' read_yaml function take config.yaml file and wrapped all return value into configBox object
            so we can use key-value pair like used below to make directory.
        '''
        create_directories([self.config.artifacts_root])
        
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_URL= config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir,
        )
        return data_ingestion_config
