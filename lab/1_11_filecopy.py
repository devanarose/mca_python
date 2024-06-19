def copy_file(source, destination):
  try:
    # Open source file in read mode and destination file in write mode
    with open(source, 'r') as source, open(destination, 'w') as destination:
      for line in source:
        destination.write(line)
    print(f"Successfully copied contents of '{source}' to '{destination}'.")
  except FileNotFoundError:
    print(f"Error: File not found. Please check the source file path '{source}'.")
  except Exception as e:
    print(f"An error occurred during copying: {e}")

# Get source and destination file paths from user
source = input("Enter the path to the source file: ")
destination= input("Enter the path to the destination file: ")

# Call the copy function
copy_file(source, destination)
