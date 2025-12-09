
# Name: Drew Girton
# Username: xmjv0622

# Lists contents of a zip archive
# usage: python ziplist.py <zipfile>
# eg. python ziplist.py testdir/test.zip
# You must use the error messages precisely as defined below.

# Hint: look at the documentation for the "zipfile" module

import sys
#from zipfile import ...   # tools in this module can be used
import zipfile
# filename is a command line argument 
# Error message: "Usage: python ziplist.py <filename.zip>"
# Error message: "File not found: python ziplist.py {file_name}"
# Error message: "Bad zip file: python ziplist.py {file_name}"
# Hint: There is an exception for this defined in the zipfile module

# Use zipfile methods to list the contents of the zip file.

file_name = "zip_example.zip"

if file_name == '':
    print("Usage: python ziplist.py <filename.zip>")
try:
    with zipfile.ZipFile(file_name) as file:
        print(file.namelist())
    file.close()

except FileNotFoundError:
    print(f"File not found: python ziplist.py {file_name}")
except zipfile.BadZipFile:
    print(f"Bad zip file: python ziplist.py {file_name}")

# Test your script on the zip_example.zip file. The response should be:
# README.md
# cmd_line.py
# find_file.py
# password.py
# rockpaperscissors.py
