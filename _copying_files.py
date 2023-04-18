'''
Ex: Copying files from same folder or from one directory to another directory

Module: shutil 
    shutil.copy(src, dst)
    shutil.copy2(src, dst) - same as copy(), except copy2() attempts to preserve file metadata
'''

import shutil

# copying a file from src folder to dst folder with a new name
src = 'src_dir/create-file.txt'
dst = 'dst_dir/final-file.txt'
shutil.copy2(src, dst)
