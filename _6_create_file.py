'''
CREATE file
open() - mode='x'
'''
file_name = 'create-file.txt'
try:
    with open(file_name, mode='x') as new_file:
        new_file.write('\nI am new text with file mode: x')
except FileExistsError:
    print(f'File exists: {file_name}')
