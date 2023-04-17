# Ex: Adding directories
'''
Two ways to create directories:
Way 1: using os module.
    os.mkdir() - To create a single directory
    os.mkdirs() - To create one or more directories at once / nested directories

Way 2: using pathlib
    pathlib.Path.mkdir() - creates single or multiple/nested directories
'''

# Way 1: using os module.
#     os.mkdir() - To create a single directory
#     os.mkdirs() - To create one or more directories at once

import os
cwd = os.getcwd()

print('Way 1: using os')

try:
    os.mkdir('dir_1') # create single directory
    os.mkdir('dir_2') # create single directory

except FileExistsError:
    print("Directory already exist: ", )

# Way 2: using pathlib
print('\nWay 2: using pathlib')
from pathlib import Path

# create a path object
path_obj = Path('dir_3')

try:
    path_obj.mkdir() # create single directory

except FileExistsError:
    print('Directory already exists')