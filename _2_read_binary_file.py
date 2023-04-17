'''
Mode: 
r -> read
mode ='r' read
mode = 'rt' read as text e.g. html, xml, txt, py, java etc.
mode = 'rb' read as binary e.g. png, images, pdf etc.
'''
# Ex - Reading binary File
# with is a context manager
# with
file_name = 'single-room.jpg'
try:
    with open(file_name, mode='rb') as file:
        content = file.read()
        print(content)
except Exception as ex:
    print(ex)
