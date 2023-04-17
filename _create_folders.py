# Ex: Adding directories
'''
Two ways to create directories:
Way 1: using os module.
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
    # Nested directories
    # exist_ok=True - an elegant way to overcome FileExistsError

    os.makedirs('level1/level2/level3', exist_ok=True) # create nested directories
except FileExistsError:
    print("Directory already exist: ", )

# Way 2: using pathlib
print('\nWay 2: using pathlib')
from pathlib import Path

# create a path object
path_obj = Path('plevel1/plevel2/plevel3')

try:
    # parents=True tells Python to create all the parents in the folder tree
    path_obj.mkdir(parents=True) # create multiple dirs

except FileExistsError:
    print('Directory already exists')