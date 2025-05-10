from setuptools import find_packages,setup   # Here we are using a inbuild module to import find function and setup model
from typing import List      # We are using list function from the typing module to convert the string into list
HYPEN_E_DOT='-e.'   # As this symbol is present in the requirement.txt to remove that symbol we are creating a constant
 # As the -e. is connecting both the setup.py and requirement.txt that is why we are taking -e.
def get_requirements(file_path:str)->List[str]:           # Here we are defining a function that will help us install all the modules that will present in the requirement.txt to download in any devices 
     """
     this function will return the list of requirements the above code is first we will define a path that will convert it in to list from string
     """
     requirements=[] # creating an empty list with name requirements all the given module will store in this list
     with open(file_path) as file_obj:     # Here we are opening path of the file and assining it as an temp object
         requirements=file_obj.readlines()     #  Here we are opening the Requirements file in read mode to read the modules inside It
         requirements=[req.replace ("\n"," ")for req in requirements]   # Replacing the -e. from the requirement with space and putting it in a for loop and storing it 
         if HYPEN_E_DOT in requirements:  # We are giving the condition if the -e. is present then it will be replaced by space 
             requirements.remove(HYPEN_E_DOT)    #now the -e. will be removed and stored in new requirements list
        
     return requirements # returning the stored value by return function 
 
setup(      # Setting up the setup.py to set the below functionality 
name ='DSproject', # this will show in the DSeoject.info
version='0.0.11',
author='Rashed',
author_email='Maaz53425@gmail.com',
packages=find_packages(), # here all the packages that are stored in the package folder gets installed
install_requires=get_requirements('requirements.txt') # here the packages gets checked if installed or not
)