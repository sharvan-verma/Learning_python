import os
import shutil

# 81. List Files: List all files in a directory using the os module.
def list_files(directory):
    try:
        files = os.listdir(directory)
        return files
    except FileNotFoundError:
        return "Directory not found."

# Example (create a dummy directory and files for testing):
if not os.path.exists("test_dir"):
    os.makedirs("test_dir")
    with open("test_dir/file1.txt", "w") as f: f.write("File 1")
    with open("test_dir/file2.txt", "w") as f: f.write("File 2")

print(f"Files in test_dir: {list_files('test_dir')}")

# 82. Create Directory: Create a new directory using the os module.
def create_directory(directory):
    try:
        os.makedirs(directory)
        return f"Directory '{directory}' created."
    except FileExistsError:
        return f"Directory '{directory}' already exists."

print(create_directory("new_dir"))
print(create_directory("new_dir")) #second time to show FileExistsError

# 83. Check File Existence: Check if a file exists using the os module.
def file_exists(filepath):
    return os.path.exists(filepath)

print(f"file1.txt exists: {file_exists('test_dir/file1.txt')}")
print(f"nonexistent_file.txt exists: {file_exists('nonexistent_file.txt')}")

# 84. Read File: Read the contents of a text file.
def read_file(filepath):
    try:
        with open(filepath, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "File not found."

print(f"Contents of file1.txt: {read_file('test_dir/file1.txt')}")

# 85. Write File: Write data to a text file.
def write_file(filepath, data):
    with open(filepath, "w") as f:
        f.write(data)
    return f"Data written to {filepath}."

print(write_file("test_dir/new_file.txt", "This is some data."))
print(read_file("test_dir/new_file.txt"))

# 86. Append File: Append data to an existing text file.
def append_file(filepath, data):
    with open(filepath, "a") as f:
        f.write(data)
    return f"Data appended to {filepath}."

print(append_file("test_dir/new_file.txt", " More data appended."))
print(read_file("test_dir/new_file.txt"))

# 87. Copy File: Copy a file to another location.
def copy_file(src, dest):
    try:
        shutil.copy(src, dest)
        return f"File copied from {src} to {dest}."
    except FileNotFoundError:
        return "File not found."

print(copy_file("test_dir/file1.txt", "test_dir/file1_copy.txt"))

# 88. Rename File: Rename a file.
def rename_file(src, dest):
    try:
        os.rename(src, dest)
        return f"File renamed from {src} to {dest}."
    except FileNotFoundError:
        return "File not found."

print(rename_file("test_dir/file1_copy.txt", "test_dir/renamed_file.txt"))

# 89. Delete File: Delete a file.
def delete_file(filepath):
    try:
        os.remove(filepath)
        return f"File {filepath} deleted."
    except FileNotFoundError:
        return "File not found."

print(delete_file("test_dir/renamed_file.txt"))

# 90. File Size: Get the size of a file.
def get_file_size(filepath):
    try:
        size = os.path.getsize(filepath)
        return f"File size of {filepath}: {size} bytes."
    except FileNotFoundError:
        return "File not found."

print(get_file_size("test_dir/new_file.txt"))

#cleanup (remove test files and directories)
shutil.rmtree("test_dir")
os.rmdir("new_dir")