from setuptools import find_packages , setup 
from typing import List


HYPHEN_E_DOT = '-e .'

def get_requirements(file_path : str) -> List[str]:
    ''''
    This function returns the list of  requiremets
    '''
    requirements = list()
    with open(file_path) as f:
        requirements= f.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
  name='azure-nsql-350m',
  version='0.0.1',
  author='Anmol',
  author_email='course.anmolraj@gmail.com',
  packages=find_packages(),
  install_requires=get_requirements('requirements.txt')
  )