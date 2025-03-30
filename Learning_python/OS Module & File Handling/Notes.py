""" File Handling in Python: Notes
I. Opening Files:

open(filename, mode):
filename: Path to the file (string).
mode: String defining how to open the file.
'r' (Read):
Opens for reading (default).
FileNotFoundError if file doesn't exist.
'w' (Write):
Opens for writing.
Truncates existing file or creates a new one.
'a' (Append):
Opens for appending.
Writes to the end of existing or creates new.
'x' (Exclusive Creation):
Creates a new file.
Fails if file exists.
'b' (Binary):
Binary mode (non-text files).
't' (Text):
Text mode (default).
'+' (Updating):
Read and write access.
Combined Modes:
'r+', 'w+', 'a+', 'x+' (and combinations with 'b' or 't').
II. Reading Files:

file.read():
Reads entire file into a single string.
file.readline():
Reads one line at a time.
file.readlines():
Reads all lines into a list of strings.
III. Writing Files:

file.write(string):
Writes a string to the file.
file.writelines(list_of_strings):
Writes a list of strings to the file.
IV. Closing Files:

file.close():
Releases system resources.
Essential after file operations.
V. with Statement:

with open(...) as file::
Automatically closes the file.
Handles exceptions gracefully.
Preferred method.
VI. Example Code Snippets:

Reading:"""

with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())

        with open("output.txt", "w") as f:
    f.write("Hello, world!\n")
    f.writelines(["Line 1\n", "Line 2\n"])

    with open("log.txt", "a") as f:
    f.write("New log entry\n")

    """VII. Key Considerations:

Always close files (or use with).
Choose the correct file mode.
Handle potential FileNotFoundError exceptions.
Binary files must be opened in binary mode.
Text files will be opened in text mode by default."""