import gzip

'''
Below there are two examples of writing and reading to .gz filetypes using the gzip library
This library simply provides an api for interfacing with this specific filetype
'''

PATH = 'New Text Document.txt.gz'
CONTENT = 'This is a text string that I wrote myself.'
BINARY_CONTENT = b'This is a text string that I wrote myself.'

with gzip.open(PATH, 'wb') as f:  # Open the file to be written to in binary format
    f.write(BINARY_CONTENT)  # Use the binary content
f.close()  # Close the file that has been written to

with gzip.open(PATH, 'rb') as f:  # Open the file to be read in binary format
    file_content = f.read()
f.close()
print(file_content)  # Print the data from the file that was read

with gzip.open(PATH, 'wt') as f:  # Open the file to be written to in text format
    f.write(CONTENT)  # Use the string content
f.close()  # Close the file that has been written to

with gzip.open(PATH, 'rt') as f:  # Open the file to be read in text format
    file_content = f.read()
f.close()
print(file_content)  # Print the data from the file that was read
