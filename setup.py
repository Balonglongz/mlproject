from setuptools import find_packages, setup

def get_requirements(file_path: str):
    """
    This function will return the list of requirements excluding '-e .'
    """
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj if req.strip() and req.strip() != '-e .']
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Leon',
    author_email='wfleong1983@yahoo.com.sg',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
