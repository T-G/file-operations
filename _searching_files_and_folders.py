import os
from pathlib import Path

# Ex: String Methods
'''
We will search .py files in the current project
- os, pathlib nd endswith() string method 
'''

# search path for current project
search_path = '.'

for k in os.listdir(search_path):
    print(k)

# Context manager with
with Path(search_path) as path:
    # get content
    for content in path.iterdir():
        # check type in file and ends with .py
        if content.is_file() and content.name.endswith('.py'):
            print(content.name)

