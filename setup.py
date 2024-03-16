from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path: str) -> List[str]:
        '''
        this function returns a list of requirements
        '''
        get_requirements=[]
        with open(file_path) as file_obj:
            requirements=file_obj.readlines()
            requirements=[req.replace('\n', ' ') for req in requirements]
            
            if HYPHEN_E_DOT in requirements :
                requirements.remove(HYPHEN_E_DOT)
        return requirements


setup(
    name="ML_PROJECTS",
    version='0.0.1',
    author='khd.hamdaoui',
    author_email='khd.hamdaoui@gmail.com',
    packages=find_packages(),
    description='A simple ML project',
    install_requires=get_requirements('requirements.txt')
    
)