'''
Write to File

mode='w' creates a file if it doesn't exists. cursor at the begining of the file. overrites an existing file. DANGEROUS.
mode='a' creates a file if it doesn't exists. cursor at the end of the file. adds content at the end of an existing file. Preferred.

write(string) - writes the content of a string to a file
writelines() - writes multiple string at a single time
'''

file_name = 'text-file.txt'
try:
   # with open(file_name, mode='w') as file:
    with open(file_name, mode='a') as file:
        #content = '\nNew line in append mode'
        content = ['\nAnother line',
                   '\npost Another line', '\n3 post Another line']
        # file.write(content)
        file.writelines(content)
        print('File saved.')
except Exception as ex:
    print(ex)
