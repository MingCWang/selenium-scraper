import os 

folder_path = "./Computer-Security"  # Replace with the path to your folder

# List all files in the folder
file_list = os.listdir(folder_path)

# Iterate through each file
for file_name in file_list:
    # Construct the current file's full path
    current_path = os.path.join(folder_path, file_name)

    # Extract the file's base name and extension
    base_name, extension = os.path.splitext(file_name)

    # Modify the file name as desired (e.g., adding a prefix or suffix)
    new_file_name = base_name + ".mp4"

    # Construct the new file's full path
    new_path = os.path.join(folder_path, new_file_name)

    # Rename the file
    os.rename(current_path, new_path)

    print(f"Renamed file: {file_name} to {new_file_name}")


