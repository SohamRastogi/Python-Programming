import os

# Specify the directory you want to list
directory = "/"  # You can replace "." with any specific path

# Get the list of files and directories in the specified directory
contents = os.listdir(directory)

# Print the contents
print("Contents of the directory:", directory)
for item in contents:
    print(item)
