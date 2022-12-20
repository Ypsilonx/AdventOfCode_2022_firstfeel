

def total_size(directory):
  # Find all subdirectories and files in the directory.
  subdirectories = []
  files = []
  for item in directory:
    if isinstance(item, directory):
      subdirectories.append(item)
    else:
      files.append(item)

  # Calculate the total size of the files in the directory.
  total_size = sum(file.size for file in files)

  # Recursively calculate the total size of each subdirectory.
  for subdirectory in subdirectories:
    total_size += total_size(subdirectory)

  return total_size