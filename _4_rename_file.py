'''
renaming a file: os.rename(src, dst) src -> actual name of the file and dst -> new name
'''

import os

# RENAME
file_name = 'file_to_rename.txt'
try:
    os.rename(file_name, 'file_with_new_name.txt')
except FileNotFoundError:
    print(f'File not found: {file_name}')
