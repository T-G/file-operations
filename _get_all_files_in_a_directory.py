# Three ways to get the list of files in a directory
# Way 1: os.pathdir(path). os.path.isfile(item)
# Way 2: os.scandir() -> path.is_file()
# List all files in a directory
import os

cwd = os.getcwd()

print('\nWay 1: os.listdir()')
dir_list = os.listdir(cwd)

# check if the item in the list is a file or a directory
for item in dir_list:
    if os.path.isfile(item):
        print(item)

# Way 2: os.scandir() -> path.is_file()
print('\nWay 2: os.scandir()')
folder = os.scandir(cwd)
for file in folder:
    if file.is_file():
        print(file)

# Way 3: os.scandir() -> path.is_file()
print('\nWay 3: using pathlib ')

from pathlib import Path

folder_in_path = Path(cwd)
for file in folder_in_path.iterdir():
    if file.is_file():
        print(file)
