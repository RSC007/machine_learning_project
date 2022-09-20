from setuptools import setup, find_packages
from typing import List

# Declairing variables for setup function
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Rushikesh"
DESCRIPTION="This first project in ml"
REQUIREMENT_FILE_NAME="requirements.txt"


def get_requirements_list()-> List[str]:
    '''
    Description: This function is going to return the list of requirement
    mention in requirements.txt file

    return This function going to return a list which contain name of libraries mention in requirements.txt
    '''
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        # return requirement_file.readlines().remove("-e .") for windows
        return requirement_file.readlines()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(), # ["housing"] : it return folder name all that folder name which contains __init__.py file
    install_requires=get_requirements_list()
)
