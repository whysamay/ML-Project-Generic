from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        ##readlines wiill add a /n
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "")for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

setup(   
name = "mlproject",
version="0.0.1",
author="samay",
author_email="samaypawar2200@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirement.txt')

)
