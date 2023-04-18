'''
Ex: fnmatch() recommended method
Filter directory content using fnmatch()
fnmatch.fnmatch(filename, pattern)

Patterns
* -> search everyting
? -> search a single character
[seq] -> matching any characters in seq
[!seq] -> matching any characters not in seq
'''
from pathlib import Path
import fnmatch as fm


# match pattern with * character
search_path = "."
pattern = "*.py"  # we want any file name that ends with .py

with Path(search_path) as folder:
    for f in folder.iterdir():  # folder is an iterator
        # print(f)
        if f.is_file() and fm.fnmatch(f.name, pattern):
            print(f.name)
