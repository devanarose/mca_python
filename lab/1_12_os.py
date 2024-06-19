# Use the OS module to perform
#  Create a directory
# Directory Listing
# Search for “.py” files
#  Remove a particular file

import os

def create_directory(directory_path):

  try:
    os.makedirs(directory_path, exist_ok=True)  # Create directories recursively
    print(f"Directory created successfully: {directory_path}")
  except OSError as e:
    print(f"Error creating directory: {e}")

def list_directory(directory_path):

  try:
    for item in os.listdir(directory_path):
      print(item)
  except FileNotFoundError:
    print(f"Error: Directory not found: {directory_path}")
  except PermissionError:
    print(f"Error: Access denied for directory: {directory_path}")

def search_py_files(directory_path):

  py_files = []
  for root, _, files in os.walk(directory_path):
    for file in files:
      if file.endswith(".py"):
        py_files.append(os.path.join(root, file))  # Construct full path
  return py_files

def remove_file(file_path):

  try:
    os.remove(file_path)
    print(f"File removed successfully: {file_path}")
  except FileNotFoundError:
    print(f"Error: File not found: {file_path}")
  except PermissionError:
    print(f"Error: Permission denied for removing file: {file_path}")

# Example usage
directory_path = "C:\\Users\\devan\\OneDrive\\Desktop\\RCSS\\python\\py"  

create_directory(directory_path)
print("\nDirectory listing:")
list_directory(directory_path)

print("\nSearching for .py files:")
py_files = search_py_files(directory_path)
if py_files:
  for file in py_files:
    print(file)
else:
  print("No .py files found.")

# Example file to remove (replace with actual file path)
file_to_remove = "file.py"  
remove_file(os.path.join(directory_path, file_to_remove))  # Join path with directory
