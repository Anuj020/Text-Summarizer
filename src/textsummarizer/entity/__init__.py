from dataclasses import dataclass
from pathlib import Path

# This class create directory folder for data
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path