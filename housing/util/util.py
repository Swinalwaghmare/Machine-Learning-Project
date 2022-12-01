import os,sys
from housing.exception import HousingException
import yaml

def read_yaml_file(file_path:str) ->dict:
    """Read a YAML file 

    Args:
        file_path (str): Absoulute address of file

    Returns:
        The contents as a dictionary
    """
    
    try: 
        with open(file_path,"rb")  as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as  e:
        raise HousingException(e,sys) from e