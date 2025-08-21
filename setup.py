from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirments(file_path:str)->List[str]:
    '''
    this function returns list of requirments
    '''
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","") for req in requirments]

        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)

    return requirments

setup(
name='mlproject',
version='0.0.1',
author='Dhananjay',
author_email='dhananjaymane2125@gmail.com',
pakages=find_packages(),
install_requires=get_requirments('requirments.txt')



)
