
# Name: Drew Girton
# Username: xmjv0622

import sys

# Show the number of non-empty lines in a text file
# Usage: python file_line_count.py <filename>
# Example: python file_line_count.py textexample.txt
# You must use the error messages precisely as defied below.

# filename is a command line argument 
# Error message: "Usage: python file_line_count.py <filename.txt>"
# Open the file and read its content
# Error message: "File not found: python file_line_count.py {file_name}"
# count number of lines that are not blank
# success - report the number of lines
# Success message: "{file_name} has {number_of_lines} lines"
# Test on the 'text_example.txt' file. The answer should be 4.
file_name = "text_example.txt"
if file_name == '':
    print("Usage: python file_line_count.py <filename.txt>")
try:
    number_of_lines = 0
    with open(file_name) as file:
        for x in file:
            if x !='\n':
                number_of_lines = number_of_lines + 1
    print(f"{file_name} has {number_of_lines} lines")
    file.close()
except FileNotFoundError:
    print(f"File not found: python file_line_count.py {file_name}")