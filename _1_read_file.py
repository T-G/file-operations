'''
Mode: 
r -> read
mode ='r' read
mode = 'rt' read as text e.g. html, xml, txt, py, java etc.
mode = 'rb' read as binary e.g. png, images, pdf etc.
'''
# Ex - Reading Text File
# with is a context manager
# with
try:
    with open('lorem-ipsum.txt', mode='rt', encoding='UTF-8') as file:

        # content = file.read() # reading the whole content at once
        # content = file.read(50) # reading the the first 50 characters

        # content = file.readline()  # read the 1st line

        # print(file)  # check the file object

        # iterate through the file line by line and print
        for line in file:
            # split() /t, /n, ''
            line_content = line.split('\n')
            sentence = line_content[0]
            print(sentence)

except Exception as ex:
    print(ex)
