from setuptools import setup,find_packages
from typing import List

## Declaring the Function name for setup  
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "SWinal waghmare"
DESCRIPTION = "This is the hosuing price prediction project"
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description : This function is going to return list of requirement mention
    in requirements.txt file 
    
    return This function is going to return which will contain name of libraries 
    mentioned in requirements.txt
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
name = PROJECT_NAME,
version = VERSION,
author= AUTHOR,
description= DESCRIPTION,
packages=find_packages(),
install_requires = get_requirements_list()
)

