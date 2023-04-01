'''The OS module in Python provides functions for
    creating and removing a directory (folder),
    fetching its contents,
    changing and identifying the current directory, etc'''
import os


path='//Users/kkd/Downloads/NEW_FOLDER'   # For windows the path might look like 'D:/'.

try:
    os.mkdir(path)      # This mkdir() function will create a new folder(directory).
    print('Folder created.')
except FileExistsError:
    print('Folder already exisited.')