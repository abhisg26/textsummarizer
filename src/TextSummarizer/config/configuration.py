from TextSummarizer.constants import *
from TextSummarizer.utils.common import read_yaml,create_directories
from TextSummarizer.entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(self,
                config_filepath = CONFIG_FILE_PATH,
                params_filepath = PARAMS_FILE_PATH) -> None:
        self.config = read_yaml(config_filepath)
        self.param = read_yaml(params_filepath)
        
        create_directories([self.config.artifacts_root])
    


    def get_data_ingestion_config(self):
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URl,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config