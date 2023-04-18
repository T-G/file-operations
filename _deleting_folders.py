'''
Ex: Deleting Folder
Modules used: os, pathlib and shutil
os.rmdir() -> if folder is empty
pathlib.Path.rmdir() -> if folder is empty
shutil.rmtree() -> removes all directory (empty or not)

'''
import os
import pathlib
import shutil

# os.mkdir('dir_to_delete')
# os.makedirs('dir_to_delete2/sub_folder2')

# using os
# os.rmdir('dir_to_delete') # if folder is empty

# Using pathlib
# pathlib.Path('dir_to_delete2').rmdir()  # OSError: The directory is not empty


# using shutil
shutil.rmtree('dir_to_delete2')
