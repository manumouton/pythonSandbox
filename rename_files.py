import os


# 1. Get all the file names
# 2. For each of the file name, rename it
def rename_files(source_folder):
    # Get the files names
    files_list = os.listdir(source_folder)
    print(files_list)

    # Save the current working path
    current_path = os.getcwd()

    # Change working directory
    os.chdir(source_folder)

    # 2. For each of the file name, rename it
    for file_name in files_list:
        print("Old file name : " + file_name)
        print("New file name : " + rename_a_file(file_name))
        os.rename(file_name, rename_a_file(file_name))

    # Go back to the original working directory
    os.chdir(current_path)


# Define what pattern to define to rename a file
# Here we gonna translate a String by removing all numbers from a file name
def rename_a_file(file_name):
    file_name.translate(None, "0123456789")


# Fill me in
folder = ""
rename_files(folder)
