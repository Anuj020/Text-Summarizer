import os
import yaml
from box.exceptions import BoxValueError
from textsummarizer.logging import logger

"""
    Ensure_annotations basically helps when we have two arguments in int type but
    unfortunately we give str value from one of them , it gives us error.
    
    F.E: def any(a:int , b:int):
                return a * b
        any(a=2 ,b="4") # output is 44
    but when we use ensure annotations, it gives us error.
"""
from ensure import ensure_annotations

"""
    let say we want to get value from Dict so we use: d['key'], 
    now if we use configBox then we directly use: d.key 
"""
from box import ConfigBox 
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input
    
    Raises:
        valueError: if yaml  file  is Empty
        e: empty file
    
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create list of directories
    
    Args:
      path_to_directories (list): list of path of directories
      ignore_log (bool, optional): ignore if multiple dirs is to be created. defualts to False.
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"