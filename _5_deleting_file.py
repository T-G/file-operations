'''
Deleting file - Two ways

os.remove(path)
os.unlink(path)

These methods do not return values if they execute successfully
'''

import os

# RENAME
file_name = 'file_with_new_name.txt'
try:
    # os.remove('file_with_new_name.txt')
    os.unlink('unlink.txt')
except FileNotFoundError:
    print(f'File not found')
